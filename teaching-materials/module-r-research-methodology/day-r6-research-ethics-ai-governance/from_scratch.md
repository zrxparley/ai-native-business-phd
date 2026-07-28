# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：模块R · R6 研究伦理 + AI 治理
> **scratch 哲学**：不调 pydantic/pandas，手写 IRB 风险分级模型 + NIST RMF 控制项合规扫描，从 Belmont 善行原则的风险-收益方程与控制项加权合规直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 IRB 风险分级模型（Belmont 善行原则的风险-收益加权方程）+ NIST RMF 控制项合规扫描器**。对应 rohitg00 P18 Regulatory Frameworks EU US UK Korea（监管框架）+ P18 Model System Dataset Cards（透明度卡片）。notes.md/starter.ipynb 用 pydantic 定义 Belmont 审查 schema、用 pandas 做案例×原则热力图，本层把"IRB 风险等级如何从因素算出"与"NIST 合规分如何加权"拆开：从 Belmont 报告善行原则的风险-收益公式与 NIST SP 800-53 控制项加权出发，手写 numpy 实现 IRB 风险分级 + 控制项扫描，让"伦理审查"不再是 pydantic schema 的枚举字段，而是可逐行审计的数值模型。

## core_algorithm

Belmont Report（1979）的**善行原则**（Beneficence）要求"最大化收益、最小化伤害"，IRB 审查的核心是把这一原则量化为风险-收益评估。设研究协议的风险因素 $f_i \in [1,5]$（$i \in$ {harm severity, probability, subject vulnerability, data sensitivity}），权重 $w_i$（$\sum w_i = 1$）；缓解措施 $m_j \in \{0,1\}$（$j \in$ {informed consent, anonymization, IRB oversight, data deletion}），缓解信用权重 $c_j$。**总风险**与**净风险**为：

$$R_{gross} = \sum_{i} w_i f_i \in [1,5], \quad R_{net} = R_{gross} - \lambda \sum_{j} c_j m_j$$

其中 $\lambda \geq 0$ 控制缓解措施的抵扣强度。**风险分级**（IRB tier）：

$$\text{tier}(R_{net}) = \begin{cases} \text{minimal} & R_{net} < \tau_1 \Rightarrow \text{expedited/exempt review} \\ \text{greater\_than\_minimal} & \tau_1 \leq R_{net} < \tau_2 \Rightarrow \text{full board} \\ \text{high} & R_{net} \geq \tau_2 \Rightarrow \text{full board + DSMB + safeguards} \end{cases}$$

关键洞察：无缓解时 $R_{net}=R_{gross}$，高风险协议（severe harm + vulnerable pop）直冲 high tier；引入 anonymization（$c=2.0$，最高信用）与 informed consent 可将 $R_{net}$ 压到 minimal--这是 IRB "伦理审查不只是判风险，更是引导研究者加缓解措施"的数学表达。

**NIST AI RMF**（SP 800-53 控制项简化）：每个控制 $k$（如 AC-2 账户管理、IA-2 身份认证）有临界度 $v_k$ 与合规状态 $x_k \in \{0:\text{fail}, 1:\text{partial}, 2:\text{pass}\}$。**加权合规分**：

$$C = \frac{\sum_k v_k x_k}{2 \sum_k v_k} \in [0,1]$$

阈值 $C \geq 0.8$ 判定"compliant"。$v_k$ 让高临界控制（IA-2 身份认证 $v=1.2$）的失败对总分打击更大--这是 NIST RMF "控制项非等权"的数学化。当某高临界控制 fail（$x=0$）时，即使其他全 pass，$C$ 也可能 $<0.8$，触发 non_compliant，对应 NIST "高优先控制的一票否决"语义。

## code_artifact

```python
import numpy as np

FACTOR_W = np.array([0.35, 0.25, 0.25, 0.15])   # harm, prob, vulnerability, data_sens
MITIGATION_C = np.array([1.5, 2.0, 1.0, 1.0])    # consent, anonym, irb, deletion

def irb_risk(factors, mitigations, lam=0.3):
    gross = float(np.dot(FACTOR_W, factors))
    credit = float(np.dot(MITIGATION_C, mitigations))
    net = gross - lam * credit
    return {"gross": gross, "credit": credit, "net": net}

def risk_tier(net):
    if net < 2.5:
        return ("minimal", "expedited/exempt")
    elif net < 3.5:
        return ("greater_than_minimal", "full_board")
    return ("high", "full_board + DSMB + safeguards")

NIST = {"AC-2": ("account_mgmt", 1.0), "AU-2": ("audit_events", 1.0),
        "IA-2": ("ident_auth", 1.2), "SC-8": ("transmission_conf", 1.0),
        "SI-12": ("info_handling", 0.8)}

def nist_compliance(states):
    num = den = 0.0
    for cid, (_, crit) in NIST.items():
        x = states.get(cid, 0)
        num += crit * x
        den += crit * 2
    score = num / den if den > 0 else 0.0
    return score, "compliant" if score >= 0.8 else "non_compliant"

if __name__ == "__main__":
    hi = irb_risk([5, 4, 5, 4], [0, 0, 0, 0])   # severe + vulnerable, no mitigation
    lo = irb_risk([2, 2, 1, 2], [1, 1, 1, 1])   # mild + mitigated
    assert risk_tier(hi["net"])[0] == "high", "no-mitigation severe must be high"
    assert risk_tier(lo["net"])[0] == "minimal", "mild+mitigated must be minimal"
    assert hi["net"] > lo["net"]
    sc1, st1 = nist_compliance({"AC-2": 2, "AU-2": 2, "IA-2": 2, "SC-8": 1, "SI-12": 0})
    assert 0.5 < sc1 < 0.8 and st1 == "non_compliant", f"partial controls non-compliant: {sc1:.2f}"
    sc2, st2 = nist_compliance({k: 2 for k in NIST})
    assert sc2 == 1.0 and st2 == "compliant"
```

**verification_property**: 高风险协议（severe harm + vulnerable + 无缓解）`risk_tier` 返回 "high"；低风险协议（mild + 全缓解）返回 "minimal"；且 `hi.net > lo.net`。NIST 控制项部分合规（4 pass + 1 partial + 1 fail）$C \in (0.5, 0.8)$ 判 non_compliant；全 pass $C=1.0$ 判 compliant。当高临界控制 IA-2 ($v=1.2$) fail 时，即使其余全 pass，$C$ 仍 $<0.8$--验证"高优先控制一票否决"语义。

## connection_to_unit

1. **库 vs 手写的风险量化**：starter.ipynb TODO3 用 pydantic `assess_checklist_item` 逐项打分（0-100）+ `score_to_status` 枚举映射，from-scratch 版 `irb_risk` 用加权方程 $R_{net} = \sum w_i f_i - \lambda\sum c_j m_j$ 把"风险等级"从枚举字段变成连续数值模型，暴露了"缓解措施如何抵扣风险"这一被 pydantic schema 隐藏的伦理决策。
2. **Belmont 善行的可计算化**：notes.md 把 Belmont 善行原则描述为"最大化收益、最小化伤害"的定性要求，from-scratch 版 `mitigations` 数组把它操作化为"加 anonymization 抵扣 2.0、加 consent 抵扣 1.5"--IRB 审查不只是判风险，更是引导研究者加缓解措施，这是 TODO3 评分器看不到的引导语义。
3. **NIST 控制项非等权**：solution.ipynb TODO4 把 NIST 四步循环映射为表格（等权罗列），from-scratch 版 `NIST` 字典给 IA-2 临界度 1.2、SI-12 临界度 0.8，让"身份认证失败比信息处理失败更严重"可计算--这是 NIST RMF "控制项分级"的数学化。
4. **一票否决的验证**：TODO5 pandas 热力图平均各原则分数，from-scratch 版 `nist_compliance` 的加权分 $C$ 在高临界控制 fail 时直接判 non_compliant，对应 NIST "高优先控制不可缺失"的真实审计语义。

## deep_dive_links

- [P18/24 Regulatory Frameworks EU US UK Korea - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/24-regulatory-frameworks-eu-us-uk-korea/README.md) - 监管框架：IRB + NIST RMF + EU AI Act 风险分级的监管底座，本单元风险分级模型的理论锚点
- [P18/26 Model System Dataset Cards - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/26-model-system-dataset-cards/README.md) - 透明度卡片：NIST 控制项合规扫描与 model card/dataset card 的透明度义务同构

## exercises

1. 在本单元 `starter.ipynb` TODO3（IRB 伦理审查评分器）完成后，用上面的 `irb_risk` 在 TODO2 的 8 个 OECD AI 事件案例上重算 $R_{net}$，对比 pydantic `irb_ethics_review` 的"低/中/高"风险等级与 from-scratch `risk_tier` 的 minimal/greater/high。定位两者分级不一致的案例，解释是"加权方程 vs 逐项打分"差异还是阈值 $\tau$ 选择差异。
2. 实现缓解措施敏感性分析：对高风险案例（factors=[5,4,5,4]），逐一开启 4 个 mitigation（consent/anonym/irb/deletion），绘制 $R_{net}$ 下降曲线。验证"anonymization（$c=2.0$）抵扣最强"且"单靠 deletion（$c=1.0$）无法把 high 降到 minimal"--量化 Belmont 善行的"最小化伤害"工程化路径。
3. 扫描 NIST 控制项临界度：把 IA-2 从 $v=1.2$ 扫到 $v=\{0.8, 1.0, 1.2, 1.5, 2.0\}$，观察"IA-2 fail 时 $C$ 是否跌破 0.8"的临界 $v^*$。讨论"高优先控制的一票否决"在 from-scratch 模型中的 $v^*$ 边界--这是 TODO4 NIST 映射的敏感性验证。
4. TODO: 在 `practice.md` 的伦理审查 drill 中，用 `nist_compliance` 替代 TODO5 pandas 热力图的"平均分"，并为每个案例添加"控制项 fail 列表"输出（哪些控制 $x=0$）。验证"加权合规分 + fail 列表"是否比"原则平均分"更准确反映伦理风险--这是 IRB 审查从"打分表"升级为"加权审计模型"的 from-scratch 交付。
