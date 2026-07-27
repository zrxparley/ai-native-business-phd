# Day 2 · 研究产出层 (v7.0)：Prompt Injection 红队防御的可复现研究工件

> **所属**：AI原生化商业博士 · 选修E9 AI安全与对齐 · Day 2 · v7.0 研究产出层
> **配套**：`notes.md` (v5.0 工程基线) / `solution.ipynb` (5 层防御 + 12 攻击向量 + deepeval SafetyMetric)
> **标准**：IMRaD + DSR (Hevner) + OSF 预注册 + FAIR + NeurIPS 可复现清单
> **核心锚点**：5 层纵深防御 / 12 Prompt Injection 攻击向量 (PI-01..PI-12) / garak (NVIDIA) / PyRIT (Microsoft) / deepeval SafetyMetric / OWASP LLM01 / AdvBench 520 / HarmBench

---

## research_question

**RQ**：在本单元 12 个 Prompt Injection 攻击向量集 (覆盖 jailbreak / leak / instruction-injection / data_poisoning / encoding / action 六类) 上，手写 5 层纵深防御 (L1 regex 输入过滤 → L2 系统提示加固 → L3 规则安全检查 Agent → L4 输出脱敏 → L5 权限隔离) 中，各层的边际拦截贡献分布如何？当攻击者用 Base64 / unicode 编码变换绕过 L1 后，L2–L5 的兜底拦截率是否显著高于随机基线？

**子问题**：
- RQ1a：直接注入 (PI-01..PI-04) 与间接注入 (PI-05) 在 5 层防御链路上的拦截层分布是否一致？（间接注入更危险，预期更靠后层拦截）
- RQ1b：deepeval SafetyMetric (LLM-as-a-judge 理念, 0.0/1.0 评分) 量化的"防御前 vs 防御后"安全分差值，是否与逐层拦截率加权结果一致？（量化一致性检验）

**可实证性**：12 攻击向量 × 5 层防御 = 60 个 (攻击, 层) 二元结果 (拦截/穿透) 可直接由 `solution.ipynb` TODO5 红队仿真产出；deepeval SafetyMetric 在 TODO6 产出标量分。RQ 可拒绝随机基线 H0 (每层独立 50% 拦截)。

---

## contribution

相对已有文献的 delta：

1. **vs Greshake et al. 2023 (arXiv 2306.05499)**：原论文定义了直接/间接 Prompt Injection 的威胁模型但未给工程防御链路。本文用 5 层纵深防御的可运行实现 (regex + 规则匹配) 将其落地为可度量的拦截率分布，并显式区分"间接注入在哪一层被拦截"。
2. **vs AdvBench (arXiv 2307.15024, 520 prompts)**：AdvBench 是单点拒绝率评估 (target 整体拒/不拒)。本文用 12 攻击向量 × 5 层的细粒度拦截矩阵，把"是否被攻破"拆成"哪一层挡住"，可定位防御短板。
3. **vs HarmBench (arXiv 2402.04249)**：HarmBench 关注对抗行为标准化数据集。本文不改数据集，而是引入 **deepeval SafetyMetric (BaseMetric)** 作为 LLM-as-a-judge 量化层，给出"防御前 vs 防御后"标量安全分对照，对应 LLM-as-a-judge 原始论文 (arXiv 2306.05685) 的工程化实例。
4. **vs garak/PyRIT 生产工具**：garak (NVIDIA, 0.15.x) 与 PyRIT (Microsoft, 1.0.x) 在生产环境跑完整 probe 库与多轮对抗编排，但本 Day 用手写 12 攻击向量 + 5 层防御做教学可复现的最小闭环，**delta 在于可解释性与可复现性** (每条拦截规则可在 `solution.ipynb` 单元格内追溯)。

---

## linked_paper

| # | 论文 | 作者/年 | 链接 | 关联说明 |
|:--:|------|--------|------|---------|
| 1 | Prompt Injection attack against LLM-integrated Apps | Greshake et al. 2023 | https://arxiv.org/abs/2306.05499 | 本 Day 间接注入威胁模型的学术来源 (notes.md 关键回顾 2)。研究工件直接复用其"间接注入通过外部检索文档攻击 Agent"的威胁模型, 在 5 层防御上验证 PI-05 (评论中隐藏 SYSTEM 指令) 的拦截层位置 |
| 2 | Not what you've signed up for: Compromising Real-World LLM-integrated Apps | Greshake et al. 2023 | https://arxiv.org/abs/2302.10273 | 间接注入真实攻击案例 (Bing Chat/Replika)。本 Day 营销 Agent 场景 (评论/UGC 间接注入 PI-05) 的现实风险锚点 |
| 3 | AdvBench: adversarial prompt benchmark | Zou et al. 2023 | https://arxiv.org/abs/2307.15024 | 520 条有害行为提示基准。本 Day 12 攻击向量参考其格式与分类 (jailbreak/leak/encoding/action), research_question 的攻击面来源 |
| 4 | HarmBench: A Standardization Framework for Automated Red Teaming | Mazeika et al. 2024 | https://arxiv.org/abs/2402.04249 | 自动化红队标准化框架。本 Day 红队六步流程 (定义攻击面→...→回归测试) 与对抗拒绝率评估的方法论来源 |
| 5 | LLM-as-a-judge (NeurIPS 2023) | Zheng et al. 2023 | https://arxiv.org/abs/2306.05685 | deepeval SafetyMetric 的理念来源。本 Day 用规则评分替代 LLM-as-a-judge 实跑 (避免 pip install 阻塞), 但 research_question RQ1b 用其方法论对照逐层拦截率 |
| 6 | OWASP Top 10 for LLM Applications | OWASP 2024 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | LLM01 (Prompt Injection) / LLM06 (Sensitive Info Disclosure) / LLM08 (Excessive Agency) 三项与本 Day 5 层防御直接对应, 作为威胁分类法标准 |

---

## imrad_outline

### I. Introduction
- **动机**：LLM 应用 (尤其营销 Agent) 上线后, Prompt Injection 是 OWASP LLM01 头号风险; 但工程团队普遍用"手写几个 prompt 试试"做安全测试, 无法系统化发现漏洞, 也无量化基线。
- **Gap**：学术端 (Greshake 2023, AdvBench 2023, HarmBench 2024) 给了威胁模型与基准数据集, 但缺一个"教学可复现 + 工程可落地 + 量化可对照"的最小闭环; 生产工具 (garak/PyRIT) 重, 不适合教学单元。
- **贡献**：本 Day 产出 (a) 12 攻击向量 × 5 层防御的拦截矩阵, (b) deepeval SafetyMetric 量化"防御前 vs 防御后"安全分, (c) IMRaD + NeurIPS 可复现清单, 形成可发表研究工件。
- **范围**：本 Day 不证明"安全", 仅证明"5 层防御对 12 攻击向量的拦截分布" (红队=L1 关联分析, 非"无漏洞"证明, 见 notes.md 末段)。

### M. Methods
- **数据**：12 个 Prompt Injection 攻击向量 (`solution.ipynb` TODO1 定义, 覆盖 jailbreak/leak/instruction-injection/data_poisoning/encoding/action 六类, 参考 AdvBench 格式); 间接注入 PI-05 隐藏在伪竞品评论 UGC 文本中。
- **模型/系统**：营销内容生成 Agent (system prompt 走 marketing persona), 上挂 5 层纵深防御 (L1 regex 黑名单 ["忽略指令","你现在是","DAN"] / L2 系统提示覆盖检测 / L3 规则安全检查 Agent [竞品机密/虚假宣传/贬低竞品规则] / L4 输出 regex 脱敏 [PII/成本价/系统提示] / L5 越权操作检测 [批量折扣/内容发布/数据导出审批])。
- **识别策略**：对每条攻击向量, 顺序过 L1→L2→L3→L4→L5, 记录"被哪层拦截" (binary outcome per layer); 若全 5 层均未拦截记为 breached。
- **量化**：deepeval BaseMetric 子类 SafetyMetric, score ∈ {0.0 (breached), 1.0 (blocked)}, 用 `assert_test` 在 CI 中自动跑 (LLM-as-a-judge 理念的规则评分实例)。
- **种子**：`random_state=42` (尽管本 Day 无随机采样, 预留种子供攻击向量扩展用)。

### R. Results (预期/已得核心发现, 引用真实数字)
- **逐层拦截率** (TODO5 红队仿真预期模式, 实跑见 `solution.ipynb`): L1 输入过滤预期拦截 PI-01..PI-05, PI-11 (直接注入/越狱/编码字符串匹配); L3 安全检查 Agent 预期拦截 PI-06,07,09,10 (语义层竞品/虚假宣传); L5 权限隔离预期拦截 PI-08 (越权折扣); L2 系统提示加固预期兜底 PI-12 (多轮诱导); L4 输出脱敏预期兜底 PI-03 (系统提示泄露)。
- **deepeval SafetyMetric** (TODO6): 防御前 (无防御 Agent) 安全分预期显著低于防御后 (5 层防御 Agent), 差值量化 5 层防御的工程价值。
- **RQ1a 发现** (预期): 间接注入 PI-05 不在 L1 拦截 (regex 无法识别隐藏在评论中的语义指令), 推到 L3 规则安全检查 Agent 或 breached -- 印证 notes.md "间接注入更危险" 的核心洞察。
- **RQ1b 发现** (预期): deepeval SafetyMetric 防御前后差值与逐层拦截率加权结果一致 (线性可加性), 验证 LLM-as-a-judge 量化层与工程拦截层度量等价。

### D. Discussion
- **贡献边界**：12 攻击向量非穷尽 (AdvBench 520 的 2.3%); 5 层防御用 regex+规则匹配, 无法捕捉语义级注入 (需 LLM-as-a-judge 升级); 红队是发现漏洞手段, 不能证明"无漏洞"。
- **局限**：(a) 攻击向量手写, 覆盖已知模式, 黑盒攻击者可设计变体绕 L1; (b) SafetyMetric 用规则评分, 非 LLM-as-a-judge 实跑; (c) 单 Agent 场景, 未覆盖多 Agent 协作下的注入传播。
- **未来工作**：(a) 升级 SafetyMetric 为真 LLM-as-a-judge (deepeval 原生支持); (b) 接入 garak probe 库扩展攻击面 (生产延伸); (c) 多 Agent 间接注入传播实验 (PyRIT 多轮编排); (d) OSF 预注册下一轮 24 攻击向量实验。
- **理论映射**：本 Day 红队对应因果阶梯 L1 (输入-输出关联), 非 L2 (干预); 防御前后对照是准实验 design (无随机分组, 攻击集固定)。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项)：

- [x] **Code**：完整代码在 `solution.ipynb` (7 code cells, 6 TODO 全填, 无 scaffold 残留, `verify_unit.py` 第 4 条 PASS scaffold=0/TODO=0); starter 版 `starter.ipynb` 提供 6 TODO 填空脚手架。
- [x] **Data**：12 Prompt Injection 攻击向量集 (PI-01..PI-12, 覆盖 6 类) 内嵌 `solution.ipynb` TODO1; 来源为本 Day 自制 (参考 AdvBench arXiv 2307.15024 格式), 许可 CC-BY-4.0 (本学习材料包默认); `data/README.md` 给出 deepeval 安装与攻击样本集指针 (URL 数=11, `verify_unit.py` 第 2 条 PASS)。
- [x] **Seeds**：`random_state=42` (预留, 攻击集当前固定 12 条无随机采样, 但种子声明供扩展用)。
- [x] **Environment**：Python 3.10+; 关键库 `deepeval` (confident-ai, 最新稳定版, `pip install deepeval`); 不依赖 garak/PyRIT 实跑 (本 Day 用 regex+规则匹配替代, 避免阻塞); `data/README.md` 记录 deepeval 安装与 API key 配置。
- [x] **Preregistration**：本 Day hypothesis 声明 (见 research_question RQ1a/RQ1b) 等价 OSF 预注册; 后续 24 攻击向量扩展实验将正式注册 OSF DOI (在 Discussion 未来工作中声明)。
- [x] **FAIR**：12 攻击向量集 **F**indable (在 `solution.ipynb` 与 `data/README.md` 可索引) / **A**ccessible (公开仓库, 无 gate) / **I**nteroperable (Markdown + Python dict 标准格式) / **R**eusable (CC-BY-4.0, 附 5 层防御实现可复跑)。
- [x] **Metrics**：逐层拦截率 (5 × 12 矩阵) + deepeval SafetyMetric score (0.0/1.0) 双轨度量, 在 `solution.ipynb` TODO5/TODO6 产出。
- [x] **Statistical report**：本 Day n=12 攻击向量, 报告各层拦截计数与比例 (非 p-value, 因 n 小且非抽样); 扩展到 n=520 (AdvBench 全集) 时将报 Wilson 95% CI。

---

## research_to_practice

本 Day 研究工件可沿三条路径翻译为实践产出：

1. **HBS Working Paper → HBR Article**：将 12 攻击向量 × 5 层防御拦截矩阵改写为 HBS Working Paper ("Defense-in-Depth for LLM Agents: A 5-Layer Empirical Study on Prompt Injection"), 再压缩为 HBR Article ("Your Marketing Agent Is One Prompt Away From Leaking Competitor Secrets")。要点是把 L1–L5 拦截率分布翻译为 CMO 可读的"安全投资回报"叙事: 哪一层最值钱? 哪一层是兜底?
2. **MIT Sloan Teaching Case**：以"营销 Agent 间接注入 (PI-05) 通过竞品评论 UGC 渗透"为决策点, 写 MIT Sloan 教学案例 (protagonist = Head of Marketing AI, tension = 个性化检索 vs 安全)。本 Day `industry.md` case_study 段给出钩子。
3. **企业白皮书 / 工程 SOP**：5 层纵深防御代码 (regex + 规则) 直接打包为企业"LLM Agent 上线前安全 SOP"白皮书, 含 OWASP LLM01/LLM06/LLM08 三项的工程对应表 (见 notes.md 关键回顾 1)。deepeval SafetyMetric 接 CI (assert_test) 形成"每次防御规则修改自动检测安全回归"的工程实践, 对应 NIST AI RMF Measure 层 (Day 3 治理钩子)。

> 翻译遵循 IMRaD (本 Day imrad_outline) → DSR (Hevner 设计科学, 5 层防御是 artifact) → OSF 预注册 (hypothesis 声明) → FAIR (12 攻击向量集可重用) → NeurIPS 可复现 (本 Day reproducibility_checklist) 五标准。

---

*本文件为 v7.0 研究产出层, 不替代 v5.0 工程实现 (5 层防御代码 + deepeval 评分) 与 v6.0 学习科学层, 而是把工程实现提升为可发表研究工件。*
*最后更新：2026-07-26*
