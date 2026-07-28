# 技能3 · Day 4：因果发现与 ML 因果推断 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能3 因果推断与规模实验 · Day 4
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何让算法自动发现因果结构？如何用 ML 估计"对不同用户效果不同"的异质处理效应？
> **v5.0 升级点**：① 新增真实数据集上机（sklearn 糖尿病 + NSW）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM 辅助因果发现）

---

## 学习目标（学完你能做到）

1. 能区分**因果发现**（从数据自动学因果图）与**因果推断**（已知因果图估效应），并说明各自的输入/输出/前提
2. 能用 **PC 算法**在真实数据上自动发现因果图结构，解读有向边/无向边，并指出 PC 的因果充分性假设何时会被违背
3. 能用**因果森林**（CausalForestDML）在真实数据上估计**异质处理效应（CATE）**，找出"对哪类用户处理效应最大"，并解读特征重要性
4. 能解释 **DML**（双重机器学习）的去偏原理（交叉拟合 + 双残差），说明它为何比传统线性回归更适合高维协变量场景
5. 能将因果发现与因果森林映射到营销场景：自动发现"什么影响转化" + 精准识别"哪类用户对优惠券响应最大"

---

## 理论部分：精炼索引（详见独立教材）

> Day 4 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md` § Day 4](../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md)（4.1–4.4 节，已包含 PC/FCI 算法、DML、因果森林、Athey & Imbens 方法论）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：因果发现 vs 因果推断

| 维度 | 因果推断（Day 1） | 因果发现（Day 4） |
|------|----------------|----------------|
| 输入 | 已知因果图 + 数据 | 仅数据 |
| 输出 | 因果效应大小 | 因果图结构本身 |
| 问题 | "X对Y的效应有多大？" | "X和Y之间有没有因果关系？方向是什么？" |
| 前提 | 已知因果图（领域知识） | 数据中的条件独立性关系 |

Day 1 你**人工画** DAG；Day 4 你让**算法学** DAG。这是从"假设因果结构"到"发现因果结构"的跃迁。

### 关键回顾 2：PC 算法

**核心思想**：从完全连接图开始，通过条件独立性检验逐步删除边，再用 v-结构检测定向。

```
PC 算法流程：
1. 骨架学习：对每对 (X,Y)，若存在条件集 S 使 X ⊥ Y | S，则删除 X-Y 边
   从 |S|=0 开始，逐步增加 |S|=1, 2, ...
2. 方向定向：对 X-Z-Y（X,Y不相邻），若 Z 不在 S 中 -> v-结构 X->Z<-Y
3. 方向传播：避免产生新 v-结构和有向环
```

**三大假设**：因果马尔可夫 + **因果充分性（无隐混杂）** + 忠实性

### 关键回顾 3：FCI 算法

FCI（Fast Causal Inference）放宽了 PC 的**因果充分性假设**，允许隐混杂因素存在。输出 PAG（Partial Ancestral Graph），用更丰富的边类型：

| 边类型 | 含义 |
|-------|------|
| X -> Y | X 是 Y 的原因（确定） |
| X <-> Y | 存在隐混杂因素同时影响 X 和 Y |
| X o-o Y | 方向不确定 |
| X o-> Y | X 可能是 Y 的原因，但不完全确定 |

**营销意义**：用 FCI 可以发现"用户购买意向"等不可观测变量同时影响搜索和购买（用 <-> 表示），而 PC 会错误地把这种关系归因为直接因果。

### 关键回顾 4：NOTEARS（连续优化因果发现）

NOTEARS（Zheng et al. 2018, arXiv 1803.02122）将因果发现**从组合优化转化为连续优化**：

- 核心 trick：用矩阵指数 trace 约束 `tr(e^{W∘W}) - d = 0` 替代离散的 DAG 约束
- 优势：可梯度下降求解，支持大规模变量集合
- 局限：假设线性关系（非线性扩展见 NoTEARS-MLP）

### 关键回顾 5：DML（双重机器学习）

Chernozhukov et al. (2018) 提出的 DML 同时解决两个问题：

1. **去偏（Debiased）**：交叉拟合（cross-fitting）消除过拟合偏差
2. **双重（Double）**：同时建模 Y|X 和 T|X，用双残差消除混杂偏差

$$\hat{\theta} = \frac{\sum_i \tilde{T}_i \tilde{Y}_i}{\sum_i \tilde{T}_i^2}$$

其中 $\tilde{Y} = Y - \hat{Y}$（Y 残差），$\tilde{T} = T - \hat{T}$（T 残差）。

**直觉**：先用 ML "扣掉"协变量对结果和处理的影响，再看"剩下的"处理和结果之间是否还有关系。

### 关键回顾 6：因果森林（Causal Forests）

Athey & Wager 提出的因果森林，专攻**异质处理效应（CATE）**估计：

- **分裂标准**：最大化子节点间处理效应的差异（而非最小化 Y 的预测误差）
- **CausalForestDML**：结合 DML 去偏 + 因果森林分裂

$$\hat{\tau}(x) = \frac{1}{|S(x)|} \sum_{i \in S(x)} \hat{\tau}_i$$

**营销应用**：传统 A/B 测试告诉你"优惠券平均有效5%"；因果森林告诉你"对高活跃用户有效8%，对低活跃用户无效"--直接指导精准投放。

---

## 上机部分：在真实数据上做因果发现与 ML 因果推断

> 配套笔记本：`starter.ipynb`（TODO 填空版）｜ `solution.ipynb`（参考答案，gated）
> 真实数据集：`data/README.md`（sklearn 糖尿病 + NSW 真实数据）

### 为什么用真实数据而非模拟数据

教材 4.1 节的因果发现代码用的是**模拟数据**（预设了 `user_interest -> search -> page_view` 的因果结构）--模拟数据预设了答案，学不到"算法在真实数据上会发现什么、哪些发现可信、哪些是伪相关"。v5.0 改用 **sklearn 糖尿病真实数据集**做因果发现：10 个真实生理变量，算法发现的因果结构可能与医学常识相符也可能不符，正是教学需要的"真实不确定性"。

ML 因果部分继续用 **NSW 真实数据**（同 Day 1），但这次不是估 ATE，而是估 **CATE**（异质处理效应）--找哪类用户对培训响应最大。

### 营销映射（关键桥接）

| Day 4 上机内容 | NSW/糖尿病对应 | 营销对应 |
|-------------|-------------|---------|
| PC 因果发现 | 糖尿病 10 个生理变量间的因果结构 | 从营销行为日志自动发现"什么影响转化" |
| 因果森林 CATE | NSW 不同特征用户的培训效应差异 | 哪类用户对优惠券响应最大（HTE） |
| 特征重要性 | 哪个特征最驱动 CATE 异质性 | 哪个用户标签最区分"券敏感用户" |

### 上机任务（6 个 TODO，见 starter.ipynb）

**Part 1 因果发现**：
1. **TODO1**：加载真实糖尿病数据（`load_diabetes()`）
2. **TODO2**：运行 PC 算法（`pc()`）
3. **TODO3**：提取并解读发现的因果结构（有向边/无向边）

**Part 2 ML 因果推断**：
4. **TODO4**：加载 NSW 真实数据（`causaldata.nsw`）
5. **TODO5**：用因果森林（`CausalForestDML`）估计异质处理效应
6. **TODO6**：分析 CATE 异质性 + 特征重要性（哪类用户响应最大）

---

## 2026 前沿补充：LLM 辅助因果发现

> v5.0 新增前沿点。传统因果发现（PC/FCI/NOTEARS）纯靠数据驱动，不利用领域知识。2026 年的新趋势是用 **LLM 辅助因果发现**。

**核心思路**：用 LLM 从领域知识/文献/文本中提取因果图候选（"什么可能导致什么"），再与数据驱动的因果发现结果**融合**。

- LLM 提供先验因果方向（如"BMI 影响血压"而非反过来），数据驱动方法验证/修正这些先验
- Kiciman et al. (2023) "Causal Reasoning and Large Language Models"（arXiv 2305.00050）--微软研究院发现 LLM 在因果图构建、反事实推理等任务上达到或超过人类专家水平
- 后续工作（如 Willig et al. 2024, "KGP Prompting"）探索用知识图谱约束 LLM 的因果图输出，减少幻觉

**营销应用场景**：把品牌经理的领域知识（"促销影响销量，但天气也影响"）输入 LLM，让它生成候选因果图，再用 PC/FCI 在真实营销数据上验证。LLM 提供"人类先验"，数据驱动方法提供"统计验证"，两者交叉校验。

**注意**：LLM 辅助因果发现仍处于研究阶段。LLM 可能产生"幻觉因果边"（编造不存在的因果关系），必须与数据驱动方法交叉验证。把它定位为"提供候选因果图的助手"，最终因果结构需数据验证。

> 深入阅读见 `reading.md` 的 LLM 辅助因果发现条目。

---

## 与前后 Day 的衔接

- **Day 1**：因果推断基础（你**人工画** DAG，用后门调整估 ATE）-- Day 4 用**算法学** DAG
- **Day 2**：实验设计（A/B 测试、DiD/RDD/IV）-- Day 4 的因果森林是观测数据的 HTE 估计
- **Day 3**：营销归因与增量度量 -- Day 4 的因果发现可用于验证归因模型的因果路径
- **Day 5**：规模实验与营销应用 -- Day 4 的方法在大规模营销实验中应用

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 4 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：PC 算法发现的因果图中，哪条边最符合医学常识？哪条最反直觉？为什么？
- [ ] 一段 300 字分析：因果森林发现哪类用户对培训响应最大？`feature_importances_` 排第一的特征是什么？在营销场景中这意味着什么？
- [ ] （可选）用 LLM 辅助因果发现：把糖尿病 10 个变量名输入 LLM，让它画出候选因果图，再与 PC 算法的结果对比，记录 1 个 LLM 发现了但 PC 没发现的边（或反过来）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实数据 + TODO 脚手架。*
*最后更新：2026-07-23*

---

## 学习科学层 (v6.0)

本单元在 v5.0 基线上增加学习科学层，基于 4 个研究方向升级（科学即高效 · 反馈即成长）：

1. **刻意练习 (deliberate practice)**: `practice.md` 将 Day 4 上机拆解为 3 个 drills（PC / NOTEARS / 因果森林+LLM），每 drill 含 difficulty / reps_required / feedback_rule / worked-faded 三阶段（完整示范 -> 部分填空 -> 独立解），并设 weak_loop 弱项循环（连续 2 次失败回退上一 drill + 补充 worked example）。
2. **间隔重复 (spaced retrieval)**: `schedule.json` 用 FSRS-6 算法（SM-2 备份，EF₀=2.5）排程 4 张复习卡（PC / NOTEARS / 因果森林 / LLM 融合），间隔 [1,3,8,21,60,180] 天，request_retention=0.9。
3. **建构对齐 (constructive alignment)**: `alignment.md` 按 Biggs 框架对齐 ILO ↔ TLA ↔ AT（3 行矩阵 + mastery_threshold + 3 自检问题 Feed Up / Feed Back / Feed Forward）。
4. **牛津 tutorial (Oxford tutorial)**: `tutorial.ipynb` 仿真 Oxford fellow 的 Socratic 追问（禁直接答案，devil's advocate），5 轮脚手架渐退，配 student_model.json 跨单元追踪盲点 + Hattie 四级 formative feedback [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD] + 限频防依赖。
5. **交叉练习 (interleaving)**: practice.md 按 A1B1C1...B2C2A2...C3A3B3 模式交叉排布 PC / NOTEARS / 因果森林，不块状，强化长期保持（Butler 2010 检索练习证据 + 提取练习 / retrieval practice）。

> v6.0 哲学：科学即高效 · 反馈即成长。不动 v5.0 原文，只追加本节。mastery 阈值详见 alignment.md。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

- **linked_paper (arXiv 已验证)**: Kiciman et al. 2023 (arXiv 2305.00050, LLM 因果推理) / Wager & Athey 2018 (arXiv 1802.05480, 因果森林) / Chernozhukov et al. 2018 (arXiv 1608.00060, DML) / Zheng et al. 2018 (arXiv 1803.02122, NOTEARS) / Willig et al. 2024 (arXiv 2402.15602, KGP Prompting)。
- **研究产出 (research output)**: research_question 锚定 LLM × PC 在糖尿病数据上的交叉验证 + NSW CATE 异质性; contribution 声明 delta vs 5 篇 prior work; IMRaD 大纲含真实数字 (NSW ATE≈1794); reproducibility_checklist >=6 项 (code/data/seeds/environment/preregistration/FAIR)。
- **产业链接 (industry linkage)**: real_companies 含 Microsoft ExP / Netflix / Booking.com / Uber / Salesforce Einstein; consulting_project partner=Booking.com (8周4-5人); case_study protagonist=Sephora Head of AI; guest_lecture=Booking.com experimentation Director; internship_pointer=Microsoft ExP / OpenAI Residency / Uber-Netflix-Booking.com DS Intern。
- **deployment**: Netflix 用 CausalForestDML 做推荐算法改动的 CATE 异质性分析 (2.6 亿用户, 1000+ A/B/天)。
- **咨询 (consulting)** / **案例 (case study)** / **客座 (guest lecture)** / **实习 (internship)**: 详见 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：因果推断 × LLM（因果发现/推理/反事实）。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 causal-learn/gcastle 库实现形成"from-scratch vs 库"对照。
> - **从零构建主题**：手写 PC 算法骨架 + 条件独立性检验（因果发现 from scratch）
> - **核心算法**：$\rho(i,j\mid S)=-P_{ij}/\sqrt{P_{ii}P_{jj}}$ + $z=\frac12\ln\frac{1+r}{1-r}\sqrt{n-|S|-3}$ + v-结构定向（含数学推导 + LaTeX，精度矩阵偏相关 + Fisher Z + collider 检测）
> - **code_artifact**：手写 numpy 骨架（≤50行），imports ⊆ {numpy, math, itertools}，附 verification_property（链 X->Z->Y 删 X-Y 边、不触发 v-结构）
> - **延伸阅读**：rohitg00 AI工程 from scratch P1/21 Graph Theory + P2/07 Unsupervised Learning
> - **手写实现要点**：用 from-scratch numpy 写 CI 检验 + 骨架学习 + v-结构而非 causal-learn `pc()` 黑箱，理解"删边/定向"到金属层
> - **verification_property**：链 $X\to Z\to Y$ 上 PC 删除 $X$-$Y$ 边（sepset={Z}）且不触发 v-结构定向（$Z\in$ sepset）
