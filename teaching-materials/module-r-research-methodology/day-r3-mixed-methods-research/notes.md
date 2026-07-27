# 模块R · R3：混合方法研究（Mixed Methods Research） · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 模块R 博士研究方法论 · R3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：定量告诉你"是什么"，定性告诉你"为什么"--混合方法把两者整合成"既知道效果又理解机制"的完整证据链
> **v5.0 升级点**：① 新增真实库上机（pandas + scipy.stats + 贝叶斯整合）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM辅助定性编码 + 贝叶斯定量定性整合 + 天道推演推演层）

---

## 学习目标（学完你能做到）

1. 能阐述混合方法研究（Mixed Methods Research, MMR）的理论基础--实用主义（Pragmatism）--以及 Creswell & Plano Clark (2018) 的三种核心设计：收敛式（Convergent）、解释性序列（Explanatory Sequential）、探索性序列（Exploratory Sequential），并说明各设计的适用场景
2. 能解释 Morse (1991) 的三种整合策略--合并（Merging）、解释（Explaining）、构建（Building）--并指出"整合"是混合方法区别于"分别做定量和定性"的核心难点
3. 能用 **pandas + scipy.stats** 对真实因果推断数据集（causaldata NSW job training program）执行定量分析：描述统计、t 检验、效应量计算，识别 NSW 职业培训对收入的影响
4. 能用 Python 实现主题分析（Thematic Analysis）的定性编码框架，对基于真实研究的访谈摘录进行编码，计算主题频次并识别核心模式
5. 能构建 **joint display（联合展示矩阵）**，将定量统计结果与定性主题对照整合，识别一致性与差异，并理解如何用贝叶斯方法将定性先验融入定量估计

---

## 理论部分：精炼索引（详见独立教材）

> R3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md` § 四、R3 混合方法研究](../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md)（约 183-254 行，已包含核心概念/三种设计/整合策略/案例分析/博士论文关联）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：混合方法的理论基础

混合方法研究（Mixed Methods Research, MMR）将定量和定性方法系统整合。理论基础是**实用主义（Pragmatism）**：实证主义偏重定量，解释主义偏重定性，实用主义主张"方法应该服从于研究问题"--如果研究问题既需要"是什么"（what）也需要"为什么"（why），就应该使用混合方法（Tashakkori & Teddlie, 2010）。

### 关键回顾 2：Creswell & Plano Clark 三种核心设计

| 设计类型 | 逻辑 | 数据收集顺序 | 适用场景 |
|---------|------|------------|---------|
| **收敛式（Convergent）** | 三角验证 | 定量+定性同步收集 | 交叉验证结果，一致性增强可信度 |
| **解释性序列（Explanatory Sequential）** | 定量发现需要定性理解 | 先定量后定性 | 定量结果出乎意料，需要解释"为什么" |
| **探索性序列（Exploratory Sequential）** | 新领域先探索再验证 | 先定性后定量 | 研究领域新，缺乏理论框架 |

### 关键回顾 3：Morse 三种整合策略

- **合并（Merging）**：定量和定性结果并排比较，识别一致性和差异（收敛式常用）
- **解释（Explaining）**：用定性数据解释定量结果（解释性序列常用）
- **构建（Building）**：用定性发现构建定量研究的理论框架和测量工具（探索性序列常用）

**核心认知**（Creswell, 2015）："一个混合方法研究如果只是分别做了定量和定性分析但从未将两者整合，那它不是真正的混合方法研究。"

### 关键回顾 4：解释性序列设计案例（营销映射）

本 Day 上机采用**解释性序列设计**，场景映射到 NSW 职业培训项目评估（经典因果推断真实数据集）+ 营销AI效果评估类比：

1. **第一阶段（定量）**：用 causaldata NSW 真实数据，比较培训组（treat=1）与对照组（treat=0）的收入差异（re78），执行 t 检验
2. **第二阶段（定性）**：基于定量发现设计半结构化访谈，对基于真实研究（LaLonde 1986, Dehejia & Wahba 1999）的参与者访谈摘录做主题分析编码
3. **整合**：构建 joint display 联合展示矩阵，将定量统计结果与定性主题对照

### 营销映射（关键桥接）

混合方法评估营销AI效果的完整映射：

| 阶段 | NSW培训项目评估（本Day上机） | 营销AI效果评估（Capstone映射） |
|------|--------------------------|-------------------------------|
| 定量 | t检验：培训组vs对照组收入差异 | A/B测试：AI文案vs人工文案CTR差异 |
| 定性 | 访谈摘录：培训参与者的就业障碍/促进因素 | 用户访谈：用户对AI生成内容的信任/体验 |
| 整合 | joint display：收入统计+就业障碍主题对照 | joint display：CTR统计+用户体验主题对照 |
| 贝叶斯 | 定性编码置信度作为先验，更新收入效应估计 | 定性访谈置信度作为先验，更新CTR效应估计 |

---

## 上机部分：用真实库做混合方法分析

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（causaldata NSW + 基于真实研究的访谈摘录 + pandas + scipy.stats）

### 为什么用真实数据而非模拟数据

v5.0 的核心哲学是"真实即严谨"。本 Day 使用：
- **定量部分**：causaldata NSW 真实数据集（LaLonde 1986 经典因果推断数据，445条真实观测）
- **定性部分**：基于真实研究文献（LaLonde 1986, Dehejia & Wahba 1999）参数可追溯的访谈摘录样本

| 维度 | 模拟数据 | 真实数据（v5.0） |
|------|---------|----------------|
| 定量可信度 | 人造分布，结论无实际意义 | NSW真实实验数据，因果推断教科书基准 |
| 定性可信度 | 虚构访谈，编码结果无参考价值 | 基于真实研究参数的访谈摘录，编码可追溯 |
| 整合意义 | 两者都是假的，整合无意义 | 定量真实+定性可追溯，整合有学术价值 |
| 可复现性 | 随机种子依赖 | 真实数据固定，任何人复现结果一致 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：加载 causaldata NSW 真实数据，用 pandas 计算培训组与对照组的描述统计（样本量/均值/中位数/标准差）
2. **TODO2**：用 scipy.stats.ttest_ind 执行 t 检验，判断 NSW 培训对收入（re78）的因果效应是否显著，计算 Cohen's d 效应量
3. **TODO3**：实现主题分析编码框架，对8条基于真实研究的访谈摘录进行定性编码，计算各主题频次
4. **TODO4**：构建 joint display 联合展示矩阵，将定量统计结果与定性主题对照整合
5. **TODO5**：贝叶斯整合--将定性编码的主题置信度转化为先验分布，用 Beta-Binomial 模型更新培训效应的后验估计
6. **TODO6**：LLM辅助定性编码模拟--设计 LLM-as-a-judge 编码提示词模板，对比人工编码与LLM编码的一致性

---

## 2026 前沿补充：LLM辅助定性编码 + 贝叶斯整合 + 天道推演

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① LLM辅助定性编码（DeepSeek/RAGAS/LLM-as-a-judge做主题分析）② 贝叶斯定量定性整合 ③ 天道推演作为混合方法的推演层。

### LLM辅助定性编码（DeepSeek / LLM-as-a-judge）

传统定性编码依赖人工逐条标注，成本高、耗时长、编码者间一致性难以保证。2026 年的前沿趋势是用 **LLM-as-a-judge**（NeurIPS 2023, arXiv 2306.05685）辅助定性编码：

- **DeepSeek** 等开源大模型可充当"编码助手"：给定编码框架（codebook）和访谈文本，LLM 自动标注每条文本的主题归属
- **RAGAS**（Retrieval Augmented Generation Assessment）框架可评估 LLM 编码质量：faithfulness（是否忠于原文）、answer_relevancy（编码是否相关）
- **编码者间一致性**：人工编码 vs LLM编码的 Cohen's kappa 可量化 LLM 编码可靠性

**注意**：LLM辅助编码是"加速工具"而非"替代工具"--LLM有自身偏差（偏好某些主题、对模糊文本编码不稳定）。正确用法是 LLM 做初筛 + 人工复核不一致案例。本 Day TODO6 设计 LLM-as-a-judge 编码提示词模板。

### 贝叶斯定量定性整合

传统混合方法的整合是"并排展示"（joint display），但定量和定性仍是两个独立证据流。**贝叶斯方法**可以把定性证据转化为定量先验，实现真正的"概率整合"：

- 定性编码的主题频次和置信度 -> 转化为先验分布参数
- 定量数据（NSW t检验结果）-> 作为似然函数
- 贝叶斯更新 -> 后验分布融合了定性和定量证据

这是混合方法研究的前沿方向：从"展示整合"走向"概率整合"。本 Day TODO5 用 Beta-Binomial 模型实现这一整合。

### 天道推演作为混合方法的推演层

天道推演系统可以作为混合方法的"推演层"：在完成定量+定性分析后，用天道推演的沙盘模拟方法，推演不同政策干预下的未来走向。这对应混合方法的"构建"策略--用定性发现构建定量推演框架，再用推演结果指导决策。多Agent仿真（Multi-Agent Simulation）可进一步模拟多利益相关方博弈。

> 🔗 深入阅读见 [`reading.md`](./reading.md)。

---

## 与后续 R 模块的衔接

- **R1 设计科学研究（DSR）**：DSR 定义"应该是什么"，混合方法评估"实际是什么" --两者互补
- **R2 行动研究**：行动研究的螺旋循环中，每轮循环可用混合方法评估干预效果
- **R4 系统文献综述（PRISMA）**：混合方法的结果可以用 PRISMA 标准做系统综述
- **R5 学术写作（IMRaD）**：混合方法论文的 Methods 部分需同时报告定量和定性方法

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § R3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 joint display 中定量和定性结果是否一致？如果不一致，不一致本身揭示了什么？贝叶斯整合后后验与频率派结论有何差异？
- [ ] （可选）为你的 Capstone 设计一个混合方法评估方案（500字），包含设计类型选择、定量方法、定性方法和整合策略

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pandas + scipy.stats + 贝叶斯整合）+ 真实数据（causaldata NSW）+ TODO 脚手架。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)

本单元在 v5.0 基线（notes.md / data / README.md / starter.ipynb / solution.ipynb / reading.md，7/7 验收通过）之上，叠加 v6.0 学习科学层（4 个新文件 + 本节追加）：

- **刻意练习 (deliberate practice, Ericsson)**：见 `practice.md`。skill_target 为"独立完成 NSW t 检验 + 主题分析编码 + joint display + 贝叶斯整合 + 设计论证"，拆 3 子技能 (S1/S2/S3)，4 个 drill 各含 worked-faded 三阶段（完整示范 -> 部分填空 -> 独立解）、difficulty(1-5)、reps_required、领域特定 feedback_rule（引用 causaldata NSW 真实分布、Cohen's kappa、Beta-Binomial 后验、Creswell 2015 整合原则）。weak_loop 连续 2 次失败触发回退 worked + 补充 worked example。retry_policy 沿用 CS230 式 10 free late days + 失败重试不罚分。
- **间隔重复 (spaced retrieval, FSRS-6 / SM-2 backup)**：见 `schedule.json`。6 张卡片覆盖 Creswell 三设计、Morse 三整合策略、joint display、Beta-Binomial 贝叶斯整合、LLM-as-a-judge + Cohen's kappa、NSW causaldata 真实数据。request_retention=0.9，due=[1,3,8,21,60,180] 六点间隔，ef0=2.5。
- **建构对齐 (constructive alignment, Biggs ILO↔TLA↔AT)**：见 `alignment.md`。4 行 ILO↔TLA↔AT 矩阵（ILO1 设计+策略 / ILO2 NSW t 检验+d / ILO3 joint display+贝叶斯 / ILO4 LLM 编码+kappa），每行 TLA 引用 starter/practice/tutorial，AT 引用 solution/practice/tutorial，mastery_threshold >=80%。3 自检问题（Feed Up: TLA 是否训练 ILO / Feed Back: AT 是否测量 ILO / Feed Forward: 不经 TLA 能过 AT 吗）全部对齐成立。
- **牛津 Tutorial LLM 仿真 (Oxford tutorial + Socratic + Hattie 4 级反馈)**：见 `tutorial.ipynb`。Persona 设定为"Oxford tutorial fellow in 混合方法研究，禁直接答案，每轮以苏格拉底问结尾，兼 HBS devil's advocate"。4 轮静态 if/else Socratic loop（含 >=5 个苏格拉底问：为什么/凭什么/反例/若前提变/如何），针对 NSW d=0.22 解读、Explanatory vs Convergent 选择、Explaining vs Building 替代、Beta 先验强度 vs kappa 关系追问。Hattie 4 级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] 避免 Self 级表扬。student_model.json 记录 4 ILO mastery + 盲点 + weak_history。限频 1 次/天防依赖。

mastery 阈值与 Worked-Faded 示例见 `practice.md` 与 `alignment.md`。交叉练习 (interleaving) 排布 A1B1C1D1->B2C2A2D2->C3A3B3D3 促进迁移，提取练习 (retrieval practice) 优于重读。本层不修改 v5.0 原文一字，仅在末尾追加本节。

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
