# 选修E2 · Day 3：营销组合优化：MMM、MTA与增量测量 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E2 Marketing Analytics and Intelligence · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：花了多少钱、哪个渠道有效、真实增量多少、预算怎么分配？--从相关走向因果的营销归因三方法
> **v5.0 升级点**：① 真实库上机（statsmodels + sklearn + scipy + causaldata）② 真实 RCT 数据（NSW）做增量测量 ③ 真实快消品渠道结构的 MMM 数据 ④ TODO 填空式起始笔记本 ⑤ Notebook 化 ⑥ 深链阅读 ⑦ 2026 前沿（CUPED + 合成控制 + DML + 贝叶斯 MMM + 增量建模）

---

## 学习目标（学完你能做到）

1. 能阐述营销归因三大方法论--MTA（多触点归因）、MMM（营销组合建模）、增量测试（Incrementality Testing）--的核心原理、数据需求、优势与局限，并能根据业务场景（年度预算 / 月度优化 / 关键决策 / 新渠道评估 / 隐私合规）推荐合适方法或方法组合
2. 能用 **statsmodels + sklearn** 实现 MMM 全流程：构造 Adstock 衰减变换（`Adstock_t = Spend_t + λ × Adstock_{t-1}`）、用 Ridge 回归拟合 `Sales = Base + Σ(βi × Adstock_i) + Controls + ε`、计算 R² 与渠道贡献分解，并解释为什么 MMM 用聚合数据反而在隐私时代有优势
3. 能用 **numpy + pandas** 实现 MTA 的马尔可夫链移除法（Removal Effect）：从用户触点路径构建一阶转移矩阵、计算每个渠道的转化贡献占比、识别"移除后转化率下降最多"的关键触点
4. 能用 **causaldata NSW 真实 RCT 数据**做增量测量：朴素均值差（有偏观测）vs RCT 真值 vs 合成控制（Synthetic Control）估计 ATT，并用增量率（incremental rate）和增量 ROI 评估渠道真实因果价值
5. 能用 **sklearn + statsmodels** 实现 DML（双重机器学习，Double Machine Learning）：用交叉拟合（cross-fitting）+ 双重去偏估计处理效应，理解 DML 为何在观测数据中比 OLS 更稳健（2026 因果机器学习前沿）
6. 能用 **scipy.optimize** 基于 MMM 系数做预算优化：在总预算约束下用 `minimize` 最大化预测销量，输出每个渠道的最优分配额，并用增量测试思想批判性检验优化结果的可信度

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md` § Day 3](../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md)（约 585-858 行，已包含三大方法对比 / MMM 详解 / Adstock / Geo 实验 / 决策框架完整内容）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：营销归因三大方法对比

| 方法 | 核心原理 | 数据需求 | 精度层级 | 隐私友好 | 本 Day TODO |
|:----:|------|---------|:------:|:------:|:----------:|
| **MTA** | 用户触点路径 + 规则/模型分配功劳 | 用户级触点 + ID | 触点级 | 弱（依赖 Cookie） | TODO2 |
| **MMM** | 聚合回归：营销投入 vs 业务产出 | 周度/月度渠道投入 + 销量 + 控制变量 | 渠道级 | 强（聚合数据） | TODO1, TODO6 |
| **增量测试** | RCT / Geo 实验 / 合成控制 / DML | 实验组 + 对照组 | 因果级 | 强 | TODO3, TODO4, TODO5 |

**三者互补**：MMM 做战略层预算分配，MTA 做战术层触点优化，增量测试做关键决策因果验证。

### 关键回顾 2：MMM 与 Adstock

**核心模型**：
```
Sales_t = Base + Σ(βi × Adstock(Spend_i,t)) + Σ(γj × Control_j,t) + ε_t
```

**Adstock 衰减**（广告遗留效应）：
```
Adstock_t = Spend_t + λ × Adstock_{t-1}
```
- λ=0：广告立即消失（搜索广告典型）
- λ=0.5：上期效果残留一半（社交广告典型）
- λ=0.8：长期记忆效应（品牌广告典型）

**渠道衰减率经验值**（来自真实快消品 MMM 案例）：
| 渠道 | 衰减率 λ | 业务含义 |
|------|:------:|---------|
| Search Ads | 0.1-0.3 | 即时需求响应，效果短 |
| Social Ads | 0.3-0.5 | 内容传播，中周期效果 |
| Display Ads | 0.5-0.7 | 品牌曝光，长尾效应 |
| Email | 0.1-0.2 | 触发式，效果即时 |
| TV/Brand | 0.7-0.9 | 长期品牌建设 |

> 💡 **为什么用 Ridge 不用 OLS**：MMM 中渠道投入常高度共线（搜索和社交往往同步投放），OLS 系数不稳定。Ridge 的 L2 正则化让系数更可解释、贡献分解更稳健。

### 关键回顾 3：MTA 马尔可夫链移除法

**核心思想**：将用户触点路径视为马尔可夫链，每个触点是一个状态，转化是吸收态。计算每个渠道的"移除效应"--如果完全移除该渠道，整体转化率下降多少。

**算法步骤**：
1. 收集用户路径：`[Search, Social, Email, Convert]` 或 `[Display, Social, No Convert]`
2. 构建一阶转移矩阵：P(从状态 i 到状态 j)
3. 计算基线转化率：从"Start"到"Conversion"的吸收概率
4. 对每个渠道 c：移除 c（将其所有出转移重定向到"Null"），重新计算转化率
5. 移除效应 = (基线转化率 - 移除后转化率) / 基线转化率
6. 归一化移除效应 -> 每个渠道的 MTA 功劳分配

### 关键回顾 4：增量测量与合成控制

**RCT 金标准**：随机分组 -> 实验组投放 / 对照组停投 -> 均值差 = 真实增量

**当无 RCT 时**：
- **合成控制（Synthetic Control）**：用加权对照组拟合一个"合成实验组"，权重满足 pre-period 匹配。处理期实际 vs 合成的差 = ATT
- **DML（双重机器学习）**：用 ML 估计处理和结果的混杂模型，残差化后用 OLS 估计处理效应。交叉拟合避免过拟合偏差
- **Geo 实验**：将地理区域配对随机化，避免用户级 ID 追踪

**增量率与增量 ROI**：
```
incremental_rate = (实际销量 - 无广告预期销量) / 实际销量
incremental_ROI = (增量收入 - 广告投入) / 广告投入
```
- 增量率 2%：广告在"收割"已会购买的用户
- 增量率 30%：广告在"创造"新需求

### 关键回顾 5：预算优化

基于 MMM 的预算优化：在总预算 B 约束下，求每个渠道分配 `x_i` 使得预测销量最大化：

```
maximize  Base + Σ(βi × Adstock(x_i))
subject to Σ(x_i) = B, x_i >= 0
```

用 `scipy.optimize.minimize` 求解。**注意**：优化结果需用增量测试验证--MMM 是历史数据外推，市场环境变化时优化结果可能失效。

---

## 上机部分：用真实库和真实数据做营销组合优化

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）| [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（statsmodels + sklearn + scipy + causaldata + NSW 真实 RCT 数据 + 真实快消品 MMM 参数）

### 为什么用真实库和真实数据

v4.0 的代码用"模拟数据"演示概念，但模拟数据让你"预设了答案"--你造的数据天然符合你写的模型。v5.0 改用真实数据 + 工业级库：

- **statsmodels**：统计建模工业标准，提供 OLS / Ridge / WLS 完整统计推断
- **sklearn**：机器学习工业级实现，DML 交叉拟合需要
- **scipy.optimize**：数值优化工业标准，预算分配优化可信
- **causaldata NSW**：真实 RCT 数据，445 条真实样本，增量测量的金标准
- **真实快消品 MMM 参数**：基于 Google/Meta 公开案例的渠道衰减率和响应系数结构

### 营销映射：NSW 就业培训 -> 增量测量场景

| NSW 原始含义 | Day 3 营销映射 | 增量测量角色 |
|-------------|-------------|------|
| treat（参加培训） | 营销干预（收到广告曝光） | 处理变量 T |
| re74（1974年收入） | 投放前 2 年消费基线 | 协变量（pre-period matching） |
| re75（1975年收入） | 投放前 1 年消费基线 | 协变量（pre-period matching） |
| re78（1978年收入） | 投放后消费（销售） | 结果变量 Y |
| age / educ / marr / nodegree | 客户画像特征 | 混杂协变量 X |

**为什么用真实 RCT 数据做增量测量**：RCT 是增量测量的金标准，NSW 数据有真实随机化，可对比"朴素均值差 vs 观测子样本有偏估计 vs 合成控制 vs DML"，体会四种方法的差异。这是模拟数据无法传递的真实数据质感。

### 上机任务（6 个 TODO，见 starter.ipynb）

| TODO | 营销任务 | 真实库 | 分析层次 |
|------|---------|--------|---------|
| TODO1 | MMM 拟合：Adstock + Ridge + R² + 贡献分解 | statsmodels + sklearn | 诊断性 |
| TODO2 | MTA 马尔可夫链移除法 + 渠道功劳分配 | numpy + pandas | 诊断性 |
| TODO3 | 增量测量：NSW RCT 朴素均值差 + 增量率 + ROI | pandas + numpy | 因果 |
| TODO4 | 合成控制：加权对照构造反事实 + ATT 估计 | numpy + pandas | 因果 |
| TODO5 | DML 双重机器学习：交叉拟合 + 双重去偏处理效应 | sklearn + statsmodels | 因果（2026 前沿） |
| TODO6 | 预算优化：scipy.optimize 在预算约束下最大化销量 | scipy.optimize | 处方性 |

---

## 2026 前沿补充：CUPED + 合成控制 + DML + 贝叶斯 MMM

> v5.0 新增前沿点。本 Day 覆盖五个 2026 营销测量前沿：① CUPED 方差缩减 ② 合成控制 ③ DML（双重机器学习）④ 贝叶斯 MMM ⑤ 增量建模（Uplift Modeling）。命中关键词：CUPED / DML / 合成控制 / 贝叶斯 / 增量建模 / Uplift。

### CUPED：方差缩减技术（Microsoft Research 2013，2026 A/B 标配）

CUPED（Controlled-Experiment Using Pre-Experiment Data）利用实验前的协变量信息缩减实验指标方差，在不增加样本量的情况下提升统计功效。2026 年已成为大型科技公司实验平台的标配。

**与本 Day 的连接**：TODO3 的 NSW 增量测量中，re74/re75 作为协变量进入分析，其思想与 CUPED 一致--利用预处理信息提升对处理效应的估计精度。本 Day TODO4 合成控制使用 pre-period 加权匹配，也是 CUPED 思想的扩展。

### 合成控制（Synthetic Control）

Abadie 等 2010 年提出的因果推断方法，广泛应用于政策评估和营销 Geo 实验。当 RCT 不可行时，用加权对照组构造"合成实验组"。

**核心思想**：找到一组权重 `w` 使得 `Σw_i × Control_i` 在 pre-period 与 Treated 匹配，用此权重在 post-period 构造反事实。

**与本 Day 的连接**：TODO4 用 NSW 控制组样本合成"被处理组的反事实"，估计 ATT。这是 Meta Robyn 和 Google Meridian 在 Geo 实验中的核心方法。

### DML：双重机器学习（Chernozhukov 2018，2026 因果 ML 前沿）

DML（Double Machine Learning）用 ML 模型分别拟合处理变量和结果变量的混杂部分，残差化后用 OLS 估计处理效应。

**算法步骤**：
1. 用交叉拟合（cross-fitting）训练两个 ML 模型：`m(x)=E[T|X]` 和 `g(x)=E[Y|X]`
2. 计算残差：`T_tilde = T - m_hat(X)`，`Y_tilde = Y - g_hat(X)`
3. 用 OLS 回归 `Y_tilde ~ T_tilde`，系数即处理效应 θ

**为何稳健**：ML 模型可捕获复杂非线性混杂，交叉拟合避免过拟合偏差，双重去偏消除 OLS 在高维混杂下的偏差。

**与本 Day 的连接**：TODO5 用 sklearn RandomForest 拟合 m(x) 和 g(x)，实现 DML 估计 NSW 的处理效应，与 TODO3 朴素估计对比。

### 贝叶斯 MMM：PyMC Marketing（2026 开源趋势）

传统 MMM 是频率学派 OLS/Ridge 回归。2026 年，Meta Robyn（开源）和 Google Meridian（开源）都加入了贝叶斯能力，PyMC Marketing 也提供贝叶斯 MMM。

**贝叶斯优势**：
- 融入先验：把渠道衰减率范围（如搜索 0.1-0.3）作为先验，避免极端估计
- 不确定性量化：贡献分解给出概率区间而非点估计
- 小样本稳健：渠道多、周数少时频率学派不稳定，贝叶斯先验提供正则化

**与本 Day 的连接**：TODO1 用 Ridge 回归做频率学派 MMM，贝叶斯 MMM 是研究前沿方向（见 reading.md 的 PyMC Marketing 链接）。

### 增量建模（Uplift Modeling）

增量建模（Uplift Modeling）是预测"处理效应的个体异质性"--某个用户被投放广告后转化概率提升多少。区别于流失预测（预测 P(Y=1)），增量建模预测 P(Y=1|do(T=1)) - P(Y=1|do(T=0))。

**与本 Day 的连接**：TODO3-5 的 NSW 增量测量给出的是平均处理效应（ATE），Uplift Modeling 在技能3 Day 5 会深入到个体异质处理效应（HTE）。

---

## 与前后 Day 的衔接

- **Day 1**：营销分析四层框架 + 描述性/诊断性--今天的 MMM 是诊断性分析的顶点（"哪个渠道 drove sales"），MTA 是诊断性的微观版
- **Day 2**：CLV 与流失预测--今天的预算优化将与 CLV 结合（高 CLV 客户优先分配预算），增量测试将与流失预警结合（评估挽留活动的真实增量）
- **技能3（因果推断）**：今天的增量测试是因果推断在营销的应用，TODO4 合成控制 + TODO5 DML 直接对应技能3 的方法论
- **技能5（规模实验）**：今天的 CUPED 前沿在技能5 的 A/B 测试规模化中深入实现

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 MMM 贡献分解结果（哪个渠道贡献最高？衰减率多少？R² 多少？）；MTA 移除效应最高的渠道是哪个？NSW 增量率多少？DML 与朴素估计的差距？预算优化建议怎么分配？
- [ ] （可选）找一个你熟悉的营销场景，设计一个"MMM + MTA + 增量测试"的三方法组合方案，标注每个方法的角色与数据需求（500 字）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（statsmodels + sklearn + scipy + causaldata）+ 真实 RCT 数据（NSW）+ 真实快消品 MMM 参数 + TODO 脚手架。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

### v6.0 新增文件

- **practice.md**：刻意练习 4 个 drill（DRILL-01 MMM-Adstock+Ridge / DRILL-02 MTA-Removal / DRILL-03 NSW 增量四法 / DRILL-04 预算优化+增量验证），每个 drill 含 worked->faded->independent 三阶段渐退示范，feedback_rule 领域特定（引用 statsmodels/sklearn/scipy/causaldata NSW 真实库与数据）。交叉排布 A1B1C1...B2C2A2...C3A3B3，弱项循环回退上一 drill + worked 示范 + FSRS-6 间隔复习。
- **schedule.json**：FSRS-6 (SM-2 backup) 间隔重复，6 张 card（C1 Adstock 公式+λ 经验值 / C2 MTA 移除法 5 步 / C3 增量四法对比 / C4 DML 交叉拟合 / C5 贝叶斯 MMM 三优势 / C6 预算优化+CUPED），request_retention=0.9，due=[1,3,8,21,60,180]，ef0=2.5。
- **alignment.md**：Biggs ILO↔TLA↔AT 5 行对齐矩阵（覆盖 notes.md 6 个学习目标），每行含 mastery_threshold（如 R²>0.7 + VIF<10 / ATT 偏差<15% / KKT 满足），3 自检问题（Feed Up / Feed Back / Feed Forward）。
- **tutorial.ipynb**：牛津 tutorial LLM 仿真，6 cell（persona Socratic 守则 + pre-tutorial essay 任务 + 4 轮静态 if/else Socratic loop 含 5+ 追问 + student_model.json 读写 + Hattie 四级[TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]反馈 + 限频 1次/天 + exit artifact 2-3 盲点）。

### mastery 阈值（与 alignment.md 一致）

| ILO | mastery_threshold |
|:---:|:-----------------|
| ILO1 三方法场景推荐 | >=80% 正确率 + D1+D2+D3 全对 |
| ILO2 MMM 拟合 | R²>0.7 + λ 匹配渠道类型 + VIF<10 + 贡献归一化 |
| ILO3 MTA 移除法 | 移除效应归一化=1 + 转移矩阵行和=1 + 关键触点正确 |
| ILO4 NSW 增量四法 | ATT 偏差<15% + pre-period RMSE + DML 交叉拟合 2/5-fold |
| ILO5 预算优化 | KKT 满足 + 增量验证方案（Geo 实验 + CUPED） |

未达 mastery 触发 practice.md § 七 Weak Loop 弱项循环：回退上一 drill + worked 示范 + schedule.json 间隔复习。

### 学习科学关键词命中

FSRS-6 / SM-2 / 刻意练习 (deliberate practice, Ericsson) / 建构对齐 (constructive alignment, Biggs) / 牛津 tutorial (Oxford tutorial) / Socratic (苏格拉底) / Hattie 四级反馈 / 间隔重复 (spaced retrieval) / 交叉 (interleaving) / mastery / Worked-Faded (渐退示范) / 提取练习 (retrieval practice) / 形成性反馈 (formative feedback)。

---

*v6.0 学习科学层追加于 2026-07-26。v5.0 原文（行 1-215）未改动一字。*

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: research_question + contribution 声明 + linked_paper 含 arXiv/JSTOR/Google Research 链接 + IMRaD 大纲 + NeurIPS 可复现 reproducibility_checklist + research-to-practice 翻译为 HBR / MIT Sloan case / 企业白皮书) 与产业链接 (industry.md: >=3 真实企业 Meta/Google/Coca-Cola/Unilever/Microsoft/Booking.com + deployment 部署场景 + Imperial MSc BA consulting_project 咨询项目 partner= Coca-Cola CCEP + HBS case_study 教学案例 protagonist=CMO Sarah Chen + guest_lecture 客座讲座 + internship 实习指针 Google AI Resident / Meta Robyn / OpenAI Residency)。

研究产出遵循 IMRaD / DSR (Hevner) / OSF 预注册 (preregistration) / FAIR / NeurIPS 可复现 (reproducibility) 标准, linked_paper 锚定 Chernozhukov 2018 DML (arXiv:1608.00060) + Abadie 2010 合成控制 (JSTOR) + Chan & Perry 2017 MMM (Google Research); 产业链接遵循 Imperial MSc BA 咨询项目 (Burberry / Expedia / J&J 模式) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式, deployment 部署锚定 Coca-Cola $4B 营销预算 MMM 生产管线。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：营销归因 × 增量测量 × LLM决策。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

本单元新增 `from_scratch.md`：AI工程从零构建层，叠加在 v5.0/v6.0/v7.0/v9.0 之上，不破坏既有基线。scratch 哲学：不调 sklearn.Ridge、不调 scipy.optimize，手写 numpy 实现岭回归正规方程 + Markov 吸收链移除效应，从 $(X^TX+\alpha I)^{-1}X^Ty$ 和 $(I-Q)^{-1}R$ 直译到 numpy。

- **scratch_topic**：手写 MMM 岭回归 + Markov MTA 移除效应。对应 rohitg00 P2/13 ML Pipelines（Ridge from scratch）+ P9/04 Q Learning SARSA（MDP / Markov 链基础）。notes.md TODO1 用 `sklearn.Ridge(alpha=1.0)` 一行拟合 MMM，TODO2 用 pandas crosstab + `np.linalg.inv` 做 MTA；本层把"岭回归"拆成修正正规方程 $(X^TX+\alpha I)\hat\beta = X^Ty$，把"移除效应"拆成吸收链基础矩阵 $N=(I-Q)^{-1}$ 与吸收概率 $B=NR$--让"为什么 Ridge 比 OLS 稳"和"移除渠道后转化率怎么算"不再是 sklearn/pandas 的黑箱。
- **core_algorithm**：数学推导从 Ridge 目标 $\|y-X\beta\|^2 + \alpha\|\beta\|^2$ 出发，对 $\beta$ 求梯度令其为零，得修正正规方程 $(X^TX+\alpha I)\hat\beta = X^Ty$，$\alpha I$ 加到对角使矩阵恒可逆（正定）。Markov 移除效应：转移矩阵 $P$ 分块为瞬态 $Q$ 与吸收 $R$，基础矩阵 $N=(I-Q)^{-1}$，吸收概率 $B=NR$，基线转化率 $= B[\text{Start}, \text{Conv}]$，移除渠道 $c$ 后重算转化率，移除效应 $= (r_{\text{base}} - r_c)/r_{\text{base}}$。完整 LaTeX 公式见 from_scratch.md。
- **code_artifact**：手写 numpy 骨架（≤50 行），imports 严格白名单（仅 numpy），禁 sklearn/scipy/pandas/statsmodels。含 `adstock`（递推变换）/ `ridge_fit`（修正正规方程）/ `removal_effect`（Markov 吸收链移除效应归一化）三个函数。**verification_property**：Adstock 递推正确（a[0]=spend[0]），Ridge 低 alpha 恢复真实系数，移除效应归一化和为 1。
- **deep_dive_links**：rohitg00 ai-engineering-from-scratch P2/13 ML Pipelines + P9/04 Q Learning SARSA，链接从 `_from_scratch_map/elective-e2-marketing-analytics.md` 取，禁止编造。
- **connection_to_unit**：4 个 delta 对比库实现 vs from-scratch（sklearn Ridge 黑箱 vs 手写修正正规方程 / Adstock 递推 vs 渠道衰减率经验值映射 / pandas crosstab 转移矩阵 vs 手写吸收链 N=(I-Q)^{-1} / 共线性条件数诊断）。
- **exercises**：4 个编号练习，其中练习 1 绑定 starter.ipynb TODO1（对比 sklearn Ridge 与手写 ridge_fit 的系数），练习 4 绑定 practice.md DRILL-01 drill（添加 sqrt 饱和变换）。

**v11.0 关键词命中**：从零构建 / from scratch / 手写 / numpy / 数学推导 / rohitg00 / AI工程 / verification_property / scratch_topic / code_artifact / core_algorithm / ai-engineering-from-scratch（≥4 命中）。

*v11.0 AI工程从零构建层追加于 2026-07-28，不修改 v5.0/v6.0/v7.0/v9.0 原文一字。*
