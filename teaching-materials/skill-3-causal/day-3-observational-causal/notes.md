# 技能3 · Day 3：观测数据的因果推断 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能3 因果推断与规模实验 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：没有 A/B 测试时，如何从观测数据中提取因果效应？
> **v5.0 升级点**：① 新增真实数据上机（NSW+CPS 观测对照 + close_college IV 数据）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（双重机器学习 DML）

---

## 学习目标（学完你能做到）

1. 能区分 PSM / DiD / IV / RDD 四大准实验方法的适用条件，并为一个营销观测数据问题选择合适的方法
2. 能在**真实观测数据**（NSW+CPS 观测对照）上用倾向得分匹配（PSM）消除自选择偏差，并与朴素估计对比
3. 能在**真实 IV 数据**（close_college 教育回报）上用两阶段最小二乘（2SLS）估计因果效应，并解释 LATE 的含义
4. 能用 DoWhy/statsmodels 完成从建模到估计到检验的完整观测因果分析流程
5. 能用"何时用哪个"的决策框架，为一个营销场景设计观测因果推断方案

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md` § Day 3](../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md)（3.1-3.4 节，已包含 PSM/IV/DiD/合成控制/DoWhy 实战）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：四大准实验方法对比

| 方法 | 核心假设 | 适用场景 | 营销映射 |
|------|---------|---------|---------|
| PSM 倾向得分匹配 | 可忽略性（无未观测混杂） | 横截面数据，处理/对照自选择 | 收到优惠券用户 vs 相似未收到用户 |
| DiD 双重差分 | 平行趋势 | 面板数据，有前后时间点 | 活动前后处理组 vs 对照组 |
| IV 工具变量 | 相关性+独立性+排他性 | 存在未观测混杂，有好工具 | "是否有门店"作"是否收到促销"的工具 |
| RDD 断点回归 | 断点处局部随机 | 处理由某阈值决定 | 消费满 500 元送会员，分析 500 元附近 |

### 关键回顾 2：PSM 倾向得分匹配

倾向得分 $e(X) = P(T=1|X)$。Rosenbaum & Rubin (1983) 证明：若可忽略性成立，则 $(Y(1),Y(0)) \perp T | e(X)$。

**步骤**：① 估计倾向得分（Logistic 回归）② 匹配 ③ 检查平衡（标准化均值差<0.1）④ 估计效应

**关键局限**：只能消除**可观测**混杂。若有未观测混杂（如"个人购买意向"），PSM 仍然有偏。此时需要 IV。

### 关键回顾 3：IV 工具变量法

当存在未观测混杂时，PSM 失效。IV 提供出路：找一个工具变量 Z，满足：
1. **相关性（Relevance）**：Z 与 T 相关，Cov(Z, T) ≠ 0
2. **独立性（Independence）**：Z 与潜在结果独立，Z ⊥ (Y(1), Y(0))
3. **排他性约束（Exclusion Restriction）**：Z 只通过 T 影响 Y，没有其他路径

用 2SLS 估计：第一阶段 $T = \gamma_0 + \gamma_1 Z + \epsilon_1$，第二阶段 $Y = \beta_0 + \beta_1 \hat{T} + \epsilon_2$。

**注意**：IV 估计的是 **LATE**（局部平均处理效应）--只对 compliers（因 Z 变化而改变 T 的那部分人）有效，不是全局 ATE。

### 关键回顾 4：DiD 双重差分

$$Y_{it} = \alpha + \beta \cdot \text{Treat}_i + \gamma \cdot \text{Post}_t + \delta \cdot (\text{Treat}_i \times \text{Post}_t) + \epsilon_{it}$$

$\delta$ 就是因果效应。**关键假设**：平行趋势（若无干预，处理组和对照组的变化趋势相同）。

### 关键回顾 5：RDD 断点回归

处理由某连续变量的阈值决定（如消费≥500 送会员）。在断点附近，处理分配近似随机，可估计局部因果效应。

---

## 上机部分：在真实观测数据上做 PSM 与 IV

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据集**：[`data/README.md`](./data/README.md)（NSW+CPS 观测对照 + close_college 教育回报数据）

### 为什么用真实数据而非模拟数据

v4.0 的 PSM/IV 代码用"模拟数据"--模拟数据预设了答案（你造的数据就有已知因果效应）。v5.0 改用两个经典真实数据集：
- **NSW + CPS 观测对照**：NSW 实验处理组 + CPS 观测对照组（非实验），**混杂远比实验对照严重**--正是 PSM 的用武之地
- **close_college (Card 1995)**：用"是否住近四年制大学"作"受教育年限"的工具变量，估计教育对工资的因果效应--IV 最经典的真实数据

### 为什么 Day 3 不用 Day 1 的 NSW 实验对照

Day 1 用 `causaldata.nsw_mixtape` 的实验对照组（随机化，协变量基本均衡），后门调整即可。Day 3 换用 **NSW 处理组 + CPS 观测对照组**（`causaldata.cps_mixtape`），**观测对照意味着严重自选择偏差**--朴素估计严重有偏，必须用 PSM 匹配。

### 营销映射（关键桥接）

| 数据变量 | 营销对应 | 含义 |
|---------|---------|------|
| `treat`（NSW 培训） | 是否收到优惠券 | 处理变量 T（PSM） |
| `re78`（1978 收入） | 转化率 / GMV | 结果变量 Y（PSM） |
| `age`,`educ`,`re74`,`re75`,... | 用户画像 / 历史消费 | 协变量 X（PSM 匹配用） |
| `educ`（受教育年限） | 用户被推荐次数/曝光深度 | 内生处理 T（IV） |
| `lwage`（对数工资） | 转化率 / GMV | 结果变量 Y（IV） |
| `nearc4`（住近大学） | 是否有线下门店/是否在覆盖区域 | 工具变量 Z（IV） |

**PSM 因果问题**：收到优惠券（培训）对转化（收入）的真实效应？观测对照组下朴素估计偏多少？PSM 修正多少？
**IV 因果问题**：被推荐次数（教育）对转化（工资）的因果效应？用"是否有门店"（近大学）作工具变量，消除未观测混杂（如购买意向/上进心）。

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：加载真实 NSW+CPS 观测对照数据（`causaldata.nsw_mixtape` + `cps_mixtape`），做公共支撑限制后合并
2. **TODO2**：探索数据--观测对照组 vs 实验处理组的协变量失衡有多严重
3. **TODO3**：朴素估计--直接算均值差（观测对照下严重有偏）
4. **TODO4**：用 DoWhy + PSM 估计（倾向得分匹配消除自选择偏差）
5. **TODO5**：后门回归对比 + 反驳检验（安慰剂处理）--验证估计稳健性
6. **TODO6**：加载 close_college 数据，用 2SLS 估计教育回报的 IV 估计

---

## 2026 前沿补充：双重机器学习（Double Machine Learning, DML）

> v5.0 新增前沿点。传统 PSM/IV 用参数模型（Logistic/线性回归）估计倾向得分和结果模型。DML（Chernozhukov et al. 2018, arXiv 1705.07626）用**机器学习**估计这些 nuisance 参数，同时通过"正交化"保持因果可解释性。

**核心思想**：
1. 用 ML 估计 $E[T|X]$（处理模型）和 $E[Y|X]$（结果模型）
2. 取残差 $\tilde{T} = T - \hat{E}[T|X]$，$\tilde{Y} = Y - \hat{E}[Y|X]$
3. 在残差上回归 $\tilde{Y} \sim \tilde{T}$，得到因果效应

**优势**：ML 能捕捉高维非线性混杂关系，比 Logistic/线性回归更灵活。**关键**：通过交叉拟合（cross-fitting）避免过拟合偏差，通过正交化保证 $\sqrt{n}$ 一致性。

**实现**：`econml.dml`（微软因果 ML 库）或 `DoubleML`（Python 包）。2026 年 DML 仍是观测因果推断的前沿工具，在数字广告归因、价格弹性估计等营销场景中被越来越多地采用。

**注意**：DML 仍依赖可忽略性假设（无未观测混杂）--它用 ML 放松了**函数形式**假设，但不放松**可忽略性**假设。若有未观测混杂，仍需 IV。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 DML 条目。

---

## 与前后 Day 的衔接

- **Day 1**：因果推断基础（因果阶梯、DAG、后门调整）--今天是观测数据的进阶方法
- **Day 2**：实验设计（A/B 测试统计基础、准实验 DiD/RDD）--DiD/RDD 的统计细节在 Day 2
- **Day 3**（今天）：观测数据的因果推断（PSM、IV，真实数据上机）
- **Day 4**：因果发现 + ML 因果推断（DML 的进阶、因果森林、PC/FCI 算法）

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：PSM 估计 vs 朴素估计的差异来自哪些混杂？IV 估计 vs OLS 估计的差异说明了什么？
- [ ] （可选）用 econml 的 DML 在 NSW+CPS 数据上再估一次，对比 PSM 与 DML 的估计差异

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实数据 + TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 真实数据 + TODO 脚手架之上, 加 4 个学习科学文件, 把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津tutorial仿真"。v5.0 内容不动, 本节仅追加。

### 设计依据 (4 agent 调研合成)

- **Ericsson 刻意练习** (deliberate practice): 5 要素 -- 具体目标 / 专注 / 反馈 / 重复 / 难度递增. practice.md 的 3 个 drill (D1 PSM / D2 IV / D3 DML) 各含 difficulty + reps_required=3 + feedback_rule + Worked-Faded 三阶段 (完整示范 -> 部分填空 -> 独立解).
- **FSRS-6 / SM-2 间隔重复**: schedule.json 5 张卡片 (PSM/IV/DML/决策树/营销映射), 间隔 [1,3,8,21,60,180] 天, EF₀=2.5. request_retention=0.9. 间隔重复 (spaced retrieval) 比块状练习多保留 24% (Butler 2010).
- **Biggs 建构对齐** (constructive alignment): alignment.md ILO↔TLA↔AT 4 行矩阵 + mastery_threshold + 3 自检 (Feed Up / Feed Back / Feed Forward). 检验 "不经 TLA 能过 AT 吗? 若能 = 对齐失败".
- **牛津 tutorial LLM 仿真**: tutorial.ipynb 用 Oxford fellow persona + Socratic 追问 (禁直接答案) + devil's advocate + 5 轮脚手架渐退 + student_model.json 跨单元记忆 + Hattie (2007) 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + 限频防依赖 (Vygotsky 共构 -> 内化).
- **MIT 交叉练习** (interleaving): practice.md A1B1C1 -> B2C2A2 -> C3A3B3 明文交叉排布, 禁块状. 提取练习 (retrieval practice) 强制 pre-task.
- **Mastery 阈值**: 4 drill 全部 reps_required=3 + progressive_project Week 3 报告 >=80% + schedule.json 首次复习 100% + exit artifact >=2 盲点.

### 4 个新增文件

1. `practice.md` - 刻意练习 (skill_target + 3 subskills + 3 drills D1/D2/D3 + progressive_project + A1B1C1 interleaving + retry_policy + weak_loop)
2. `schedule.json` - FSRS-6 间隔重复 (5 cards: PSM/IV/DML/决策树/营销映射)
3. `alignment.md` - Biggs ILO↔TLA↔AT 4 行 + mastery_threshold + 3 自检
4. `tutorial.ipynb` - 牛津 Tutorial LLM 仿真 (persona + 5 轮 Socratic + student_model + Hattie 四级 + 限频 + exit)

### v5.0 -> v6.0 哲学增量

v5.0: 真实即严谨 · 练习即掌握
v6.0: **科学即高效 · 反馈即成长** -- 用学习科学把"练习"升级为"刻意练习+间隔重复+建构对齐+牛津tutorial仿真"

### 与本单元 NSW+CPS / close_college / DML 的锚点

- D1 (PSM) feedback_rule 引用 LaLonde 1986 + NSW+CPS 观测对照自选择偏差
- D2 (IV) feedback_rule 引用 Card 1995 + close_college nearc4 + LATE vs ATE
- D3 (DML) feedback_rule 引用 Chernozhukov 2018 (arXiv 1705.07626) + "放松函数形式但不放松可忽略性"
- tutorial.ipynb 5 轮 Socratic 追问分别锚定 PSM 自选择 / IV 排他性 / LATE 外推 / DML 边界 / 方法决策

---

*v6.0 学习科学层 · Ericsson + FSRS-6/SM-2 + Biggs + Oxford Tutorial + Hattie + MIT Interleaving*
*最后更新：2026-07-25*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。linked_paper锚定Chernozhukov 2018 (arXiv 1705.07626) DML论文与Card 1995 close_college IV数据源头; real_companies从公司库挑(Microsoft ExP/Netflix/Uber/Booking.com/Google, 因果推断/A-B领域)。详见 research.md 与 industry.md。

*v7.0 研究产出与产业链接层 · IMRaD + DSR(Hevner) + OSF preregistration + FAIR + Imperial MSc BA + HBS Case*
*最后更新：2026-07-26*
