# 技能3 · Day 5：规模实验与营销应用 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能3 因果推断与规模实验 · Day 5
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：从单次 A/B 到规模实验--自适应实验、营销归因、异质效应如何支撑营销决策？
> **v5.0 升级点**：① 真实数据上机（NSW 综合案例 + 真实响应率驱动 MAB）② TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（Uplift Modeling 增量建模 + Qini 曲线）

---

## 学习目标（学完你能做到）

1. 能用 Thompson Sampling 多臂老虎机（MAB）在真实响应率数据上对比固定 A/B，理解自适应实验的"探索-利用"权衡与实验成本节省
2. 能用 econml CausalForestDML 估计异质处理效应（CATE），识别对处理响应最大的用户群，支撑精准投放
3. 能完成"数据 -> 因果 -> 决策"的综合案例流程（问题定义 -> 实验设计 -> 估计 -> CATE -> 决策）
4. 能识别用户增长中的三大因果陷阱（幸存者偏差、辛普森悖论、选择性停止），并在营销分析中规避

---

## 理论部分：精炼索引（详见独立教材）

> Day 5 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md` § Day 5](../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md)（5.1–5.4 节，已包含 MAB/营销归因/用户增长/综合案例）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：多臂老虎机（MAB）与自适应实验

传统 A/B 测试是"固定"的：预设样本量，跑完才看结果，实验期间部分用户被分配到较差版本，造成"实验成本"。

**MAB 三大算法**：
- **ε-Greedy**：以 ε 概率随机探索，1-ε 概率利用当前最优。简单但效率低。
- **UCB**：选"置信区间上界"最高的方案，$\text{UCB}_k = \hat{\mu}_k + \sqrt{2\ln(n)/n_k}$，自动平衡探索（不确定的方案上界高）与利用。
- **Thompson Sampling**：对每个方案维护 CTR 后验分布（Beta），采样选最大，观察后更新。**实践最优**。

**营销应用**：动态创意优化（DCO）、推荐冷启动、定价实验。MAB 自适应分配流量，比固定 A/B 节省实验成本。

**与因果推断的关系**：MAB 是自适应实验，因果效应估计更复杂（后期数据分布受前期策略影响），需 IPW/加权似然消除选择偏差。

### 关键回顾 2：营销归因（从启发式到因果）

传统归因（末次/首次/线性触点）是**启发式规则**，非因果估计。因果归因方法：

| 方法 | 核心 | 营销场景 |
|------|------|---------|
| 增量测试 Incrementality | 随机暂停某渠道，比较暂停/未暂停转化差 | 暂停某城社交广告，看转化降多少 |
| 因果媒介分析 | 总效应 = 间接效应（经品牌认知）+ 直接效应 | 广告 -> 品牌认知 -> 转化 |
| MMM 媒体混合模型 | 时序回归估计各渠道花费对销售的效应 | 处理 adstock 延迟 + 饱和 + 协同 |

**MMM 关键技术**：Adstock 变换（广告效果延迟衰减）、饱和效应（边际递减，log1p）、协同效应。

### 关键回顾 3：用户增长的因果陷阱

1. **幸存者偏差**：只分析留存用户找增长杠杆，忽略流失用户。留存用户本就更活跃，行为不能外推。
2. **辛普森悖论**：总体 A 优于 B，分群后每个子群体 B 更优（子群体样本比例不均所致）。
3. **选择性停止**：看到 p<0.05 就停实验 -> 多重检验，假阳性飙升。应预设样本量或用序贯检验。

### 关键回顾 4：异质处理效应（CATE）

ATE 是平均效应，但不同用户对处理的响应不同。CATE（条件平均处理效应）估计**哪类用户响应最大**：

- **CausalForestDML**（econml）：用因果森林 + 双重机器学习估计 CATE
- 营销应用：找"对优惠券响应最大"的用户群做精准投放，而非全量发券

### 关键回顾 5：综合案例流程（数据 -> 因果 -> 决策）

1. **问题定义**：处理 T、结果 Y、协变量 X、目标（ATE + CATE）
2. **实验设计**：A/B 随机化 + 定性访谈（混合方法）
3. **估计**：ATE（均值差/DoWhy）+ CATE（CausalForestDML）
4. **决策**：基于 ATE 判断"要不要全量"，基于 CATE 判断"对谁全量"

---

## 上机部分：规模实验与营销归因综合案例

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated）
> 📊 **真实数据集**：[`data/README.md`](./data/README.md)（NSW 真实数据驱动综合案例 + MAB + CATE）

### 为什么用真实数据

v4.0 的 MAB/MMM 代码用 `np.random` 模拟 CTR 和广告花费--模拟数据预设了答案。v5.0 改用 **NSW 真实数据**：用真实估计的"响应率"驱动 MAB（对比固定 A/B 的转化损失），用真实协变量做 CATE（找对培训响应最大的群体）。MMM 因需时序媒体数据，本 Day 在 reading.md 给真实数据集指引，starter 聚焦可跑的 MAB + CATE。

### 营销映射

| NSW 变量 | 营销映射 | 角色 |
|---------|---------|------|
| `treat` | 是否收到优惠券/AI推荐 | 处理 T |
| `re78` | GMV/转化 | 结果 Y |
| `age`,`education`,`re74`,`re75`,... | 用户画像/历史消费 | 协变量 X（CATE 用） |
| `treat` 组 `re78>0` 比例 | 真实响应率 | MAB 的 true CTR 类比 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：加载真实 NSW 数据，准备综合案例（T/Y/X）
2. **TODO2**：固定 A/B 基线分析（均值差 + 显著性）--综合案例步骤3的 ATE
3. **TODO3**：Thompson Sampling MAB--用 NSW 真实响应率驱动 bandit，对比固定 A/B 累计转化
4. **TODO4**：CATE--econml CausalForestDML 估计异质效应，找响应最大的用户群
5. **TODO5**：反驳检验（安慰剂）--验证 ATE/CATE 估计稳健性
6. **TODO6（可选）**：辛普森悖论检测--按 `black`/年龄分群看效应是否反转

---

## 2026 前沿补充：Uplift Modeling（增量建模 + Qini 曲线）

> v5.0 新增前沿点。CATE 告诉你"哪类用户响应最大"，**Uplift Modeling** 进一步把用户分四类--**可被说服（persuadables）**、必然转化（sure things）、必不转化（lost causes）、反响应（sleeping dogs，处理反而害他们）--只对"可被说服"投放，实现真正的增量营销。

**核心**：用 CATE 模型 + Qini 曲线评估"按预测 CTE 从高到低投放，累计增量转化"。

**实现**：`scikit-uplift`（PyPI `sklift`）+ `econml` 的 CATE 模型。Qini 曲线类似 ROC，但纵轴是累计增量（uplift），横轴是投放比例。

**营销价值**：传统全量发券浪费在"必然转化"和"反响应"用户上；Uplift 建模只投"可被说服"群体，相同预算下增量转化最大化。这是 2026 年营销因果应用从"估计效应"走向"优化决策"的关键一跃。

参考：Gutierrez & Gérardy (2017) "Causal Inference and Uplift Modelling: A Review"; `scikit-uplift` 文档。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 Uplift 条目。

---

## 与前后 Day 的衔接

- **Day 2**：A/B 测试统计基础--今天升级为自适应实验（MAB）+ 规模化
- **Day 3**：观测因果（PSM/IV）--今天的综合案例在 RCT 基础上加 CATE
- **Day 4**：因果发现 + ML 因果--Day 4 的因果森林是今天 CATE 的技术基础
- **后续**：技能3 结业，进入技能4（AI 商业模式）/技能5（Agentic 系统），把因果思维用于商业决策与 Agent 评估

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 5 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：MAB vs 固定 A/B 在你的真实响应率数据上节省了多少实验成本？CATE 发现哪类用户响应最大？
- [ ] （可选）用 scikit-uplift 在 NSW 数据上画 Qini 曲线，识别"可被说服"用户群

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实数据 + TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 升级: 在 v5.0 真实数据 + TODO 脚手架基础上, 加 **学习科学层** 4 文件, 把"练习"升级为"刻意练习 (deliberate practice) + 间隔重复 (spaced retrieval) + 建构对齐 (constructive alignment) + 牛津 tutorial (Socratic) 仿真"。

### 1. 刻意练习 (Ericsson + MIT)
- `practice.md`: skill_target + 3 子技能 + 3 drills (Worked -> Faded -> Independent 三阶段, 即 Worked-Faded 渐退示例) + A1B1C1 交叉练习 (interleaving, 非块状) + weak_loop (连续 2 次失败回退上一 drill)
- feedback_rule 引用 NSW 真实响应率 / Thompson MAB 后验采样 / CausalForestDML 安慰剂检验 / Uplift 四类用户
- mastery_threshold: D1 >=80% / D2 >=70% / D3 能独立解 / M4 >=80%

### 2. 间隔重复 (FSRS-6 / SM-2)
- `schedule.json`: FSRS-6 (request_retention=0.9, 21 weights) + SM-2 备份 (EF0=2.5, I(1)=1, I(2)=6)
- 4 张卡片 (Thompson MAB / CATE / Uplift 四类 / 三陷阱), 间隔 [1, 3, 8, 21, 60, 180] 天
- 间隔重复 + 交叉 interleaving 强制检索切换, 避免块状假性掌握

### 3. 建构对齐 (Biggs)
- `alignment.md`: ILO ↔ TLA ↔ AT 矩阵 4 行 + mastery_threshold + 3 自检 (Feed Up / Feed Back / Feed Forward)
- 若不经 TLA 能过 AT = 对齐失败 (Biggs 建构对齐核心原则)

### 4. 牛津 Tutorial 仿真 (Oxford + Hattie)
- `tutorial.ipynb`: Oxford fellow persona (Socratic 追问 + 禁直接答案 + devil's advocate) + 4 轮静态 Socratic loop (>=5 问) + student_model.json + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避开 Self 级表扬) + 限频 1次/天防依赖
- 提取练习 (retrieval practice): pre-task 强制学生先写 300 字辩护, tutorial 时间用来挑战而非讲授

### 学习科学关键词命中
FSRS · SM-2 · 刻意练习 · deliberate practice · 建构对齐 · constructive alignment · 牛津 tutorial · Socratic · Hattie · 间隔重复 · spaced retrieval · 交叉 interleaving · mastery · Worked-Faded · 渐退 · 形成性反馈 · 提取练习

---

*v6.0 学习科学层由 v6.0 升级 agent 追加, 不动 v5.0 原文。研究依据: Ericsson 刻意练习 / FSRS-6 / Biggs 建构对齐 / Hattie (2007 RER 77(1):81-112) / MIT 6.5940 渐退示例 / Oxford tutorial / arxiv 2024-2025 Socratic LLM (2409.05511 / 2507.05795)。*

---

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
