# Capstone · Phase 4：因果实验设计与验证 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · Capstone AI和商业分析项目 · Phase 4
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：营销Agent的干预真的有效吗？--用因果推断给出科学回答
> **v5.0 升级点**：① 整合技能3(因果推断Day1-5)+技能5(Day3评估) ② 真实NSW RCT数据上机 ③ TODO填空脚手架 ④ Notebook化 ⑤ 深链阅读 ⑥ 2026前沿（DML双重机器学习/CUPED/因果森林/Uplift增量建模）

---

## 学习目标（学完你能做到）

1. 能用**解释性序列设计**（Explanatory Sequential Design）规划一个营销Agent系统的因果评估方案：先定量（A/B+因果推断），再定性（访谈+案例），最后整合
2. 能在**真实RCT数据**（NSW职业培训实验）上完成DoWhy四步因果分析（假设->识别->估计->反驳），估计ATE并用安慰剂检验/随机混杂检验验证稳健性
3. 能用**DML双重机器学习**（econml）和**因果森林**估计异质因果效应（CATE），识别"哪些用户群体从营销干预中获益最大"
4. 能用**CUPED**（Controlled-Experiment Using Pre-Experiment Data）利用前实验协变量降低实验方差、提升检测灵敏度
5. 能用**自定义BaseMetric**（deepeval fallback）评估Phase 3 Agent输出中因果证据的使用质量，回答"Agent是否正确使用因果证据做决策"

---

## 理论部分：精炼索引（详见独立教材）

> Phase 4 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md` § Phase 4](../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md)（4.1-4.6节，已包含混合方法评估设计/A/B测试设计/因果推断分析/定性评估设计/交付物清单）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：解释性序列设计（混合方法）

```
阶段1: 定量评估（先）
  ├─ A/B测试 + 因果推断（DoWhy四步）
  └─ 产出：ATE/CATE/稳健性检验

        ↓ （解释"为什么"）

阶段2: 定性评估（后）
  ├─ 用户访谈 + 案例分析
  └─ 产出：对定量结果的深度解释

        ↓ （整合）

阶段3: 综合结论
  └─ 定量+定性 -> 设计原则
```

### 关键回顾 2：DoWhy四步因果分析

| 步骤 | 操作 | 本Phase实现 |
|:----:|------|------------|
| 1 建模 | 声明因果图（DAG），定义处理/结果/混杂 | `CausalModel(data, treatment, outcome, common_causes)` |
| 2 识别 | 用后门准则找到可识别的估计策略 | `model.identify_effect()` |
| 3 估计 | 用后门调整/PSM/DML估计因果效应 | `model.estimate_effect(method_name=...)` |
| 4 反驳 | 安慰剂/随机混杂/子集检验，验证稳健性 | `model.refute_estimate(...)` |

### 关键回顾 3：为什么朴素均值差有偏

$$\hat{\text{ATE}}_{naive} = \bar{Y}_{treated} - \bar{Y}_{control} = \text{ATE} + \text{Bias}$$

偏差来自混杂因素在处理组与对照组分布不均。**RCT通过随机化消除偏差**（NSW是真实RCT，但观测对照组仍有混杂）；**观测数据需后门调整/匹配/DML消除偏差**。

### 关键回顾 4：CUPED方差缩减

CUPED（Deng et al. 2013, Microsoft）利用前实验协变量 $X_{pre}$ 调整结果变量：

$$Y_{adj} = Y - \theta \cdot (X_{pre} - \bar{X}_{pre}), \quad \theta = \frac{\text{Cov}(Y, X_{pre})}{\text{Var}(X_{pre})}$$

调整后方差降低 $\approx \rho^2$（Y与X_pre的相关系数平方），等效提升样本量。在NSW数据中，用 `re75`（前一年收入）作为前实验协变量调整 `re78`（结果收入）。

---

## 上机部分：在真实RCT数据上做因果实验设计与验证

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（NSW真实RCT + DoWhy + econml + deepeval）

### 为什么用真实数据而非模拟数据

模拟数据预设了因果结构（你造的数据就是按某个DAG生成的），学不到"真实世界里混杂长什么样、有多脏"。v5.0改用**NSW真实RCT数据**（Dehejia & Wahba 1999），真实存在协变量不均衡，正是因果实验设计的最佳教学案例。

### 营销映射（关键桥接）

NSW数据是职业培训，但因果结构与营销问题同构：

| NSW变量 | 营销对应 | 角色 |
|---------|---------|------|
| `treat`（是否参加培训） | 是否收到营销干预（优惠券/广告/Agent系统） | 处理变量 T |
| `re78`（1978年收入） | 转化率/GMV/客单价 | 结果变量 Y |
| `re75`（1975年收入） | 基线消费/历史转化率 | 前实验协变量（CUPED用） |
| `age`, `educ`, `black`, `hisp`, `marr`, `nodegree`, `re74` | 用户画像特征 | 协变量 X（潜在混杂） |

**你要回答的因果问题**：营销干预（treat）对转化（re78）的**真实因果效应**是多少？哪些用户群体的因果效应更大（CATE）？估计是否稳健（反驳检验）？

### 上机任务（7个TODO，见starter.ipynb）

1. **TODO1**：加载真实NSW数据，检查协变量均衡性
2. **TODO2**：朴素估计--直接算处理组-对照组均值差（有偏）
3. **TODO3**：DoWhy四步因果分析（建模->识别->估计->反驳）
4. **TODO4**：CUPED方差缩减--用re75调整re78，对比方差
5. **TODO5**：DML双重机器学习--用econml估计ATE和CATE（异质效应）
6. **TODO6**：因果森林--用econml估计CATE，对比DML的异质效应发现
7. **TODO7**：Agent因果证据评估--自定义BaseMetric评估Agent输出中因果证据使用质量

---

## 2026前沿：DML/CUPED/因果森林/Uplift增量建模

> v5.0新增前沿点。Phase 4聚焦因果实验设计的2026前沿方法。

### DML双重机器学习（Double/Debiased Machine Learning）

DML（Chernozhukov et al. 2018, Econometrics Journal）用机器学习模型估计 nuisance functions（E[Y|X]和E[T|X]），再用残差化的Y和T估计因果效应。相比传统线性回归后门调整，DML在**高维协变量**和**非线性关系**下更稳健，且提供**无偏估计**（double/debiased）。

**怎么用**：用 `econml.dml.LinearDML`，`model_y`和`model_t`用随机森林（捕捉非线性），`discrete_treatment=True`（二值处理）。输出ATE和CATE。

### CUPED（Controlled-Experiment Using Pre-Experiment Data）

CUPED（Deng et al. 2013, KDD）是Microsoft发明的方差缩减技术，利用前实验协变量调整结果变量，等效提升实验灵敏度。在A/B测试中广泛使用（Microsoft/Netflix/LinkedIn）。CUPED不改变ATE估计，但缩小置信区间、提升统计功效。

### 因果森林（Causal Forest）

因果森林（Wager & Athey 2018, Journal of the American Statistical Association）用随机森林结构估计异质因果效应（CATE），能自动发现"哪些子群体效应最大"。相比DML的线性CATE，因果森林能捕捉**协变量交互效应**。

### Uplift建模与增量建模

Uplift建模（增量建模）是营销领域的因果推断应用：估计每个用户"被干预vs不被干预"的增量效应，按 uplift 排序优先干预"可被说服"的用户。DML和因果森林的CATE估计可直接用于Uplift排序。MAB（多臂老虎机）则用于在多干预方案中自适应选择最优方案。

### 贝叶斯因果推断

贝叶斯方法（如Bayesian Causal Forest, BART）在因果推断中提供不确定性量化：不仅给出ATE点估计，还给出后验分布。在小样本场景下贝叶斯方法比频率方法更稳健。NSW数据仅445个样本，贝叶斯方法有独特优势。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的DML/CUPED/因果森林条目。

---

## 整合性：Phase 3 Agent系统的因果评估

本Phase的**整合性**体现在：对Phase 3产出的营销Agent系统做因果评估。

| 整合层 | Phase 3产出 | Phase 4评估 |
|--------|------------|------------|
| Agent输出 | 营销策略文本+工具调用轨迹 | Agent是否正确使用因果证据做决策？ |
| 因果估计 | DoWhy ATE估计 | ATE是否稳健（反驳检验）？CATE是否有异质性？ |
| 实验设计 | 营销A/B测试方案 | CUPED能否提升检测灵敏度？DML能否发现非线性效应？ |
| Agent评估 | deepeval评估 | 自定义BaseMetric评估因果证据使用质量 |

**核心整合问题**：Phase 3的营销Agent系统是否真的有效？--Phase 4用因果推断回答"有效"，用Agent评估回答"Agent是否正确理解了这个有效性"。

---

## 与前后Phase的衔接

- **Phase 3**（Agent系统构建）：本Phase对Phase 3的Agent系统做因果评估，Agent输出的因果证据使用质量是TODO7的评估对象
- **Phase 5**（商业模式与价值评估）：本Phase的ATE/CATE估计是Phase 5 ROI分析的基础--"因果效应 x 用户规模 x 客单价 = 价值"

---

## 作业与评估

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（7个TODO全部填好，能跑通）
- [ ] 一段300字分析：朴素ATE vs DoWhy后门ATE vs DML ATE的差异来自哪里？哪个最可信？
- [ ] CATE分析：DML和因果森林发现的异质效应是否一致？哪个用户群体获益最大？
- [ ] Agent评估报告：用自定义BaseMetric评估Agent输出的因果证据使用质量，记录分数和改进建议

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材Phase 4节，上机部分用真实数据（NSW RCT）+ 真实库（DoWhy+econml+deepeval fallback）+ TODO脚手架，整合技能3因果推断与技能5 Agent评估。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习**（Ericsson deliberate practice：拆子技能 + 即时反馈 + 重复到自动化，见 `practice.md` 的 6 个 drill 与 Worked-Faded 三阶段示范-填空-独立解）/ **间隔重复**（FSRS-6 算法，SM-2 备份；`schedule.json` 8 张卡片，每张 due 间隔 [1,3,8,21,60,180]，request_retention=0.9）/ **建构对齐**（Biggs constructive alignment：ILO↔TLA↔AT 矩阵 5 行，mastery 阈值 ≥80%，3 自检问题 Feed Up/Feed Back/Feed Forward，见 `alignment.md`）/ **牛津 tutorial LLM 仿真**（Socratic 追问 5 轮，禁直接答案，Hattie 四级形成性反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]，见 `tutorial.ipynb`）。

**mastery 阈值**与 Worked-Faded 示例详见 `practice.md`（每个 drill 的 Independent 阶段 ≥80% + Poster ≥80% = Phase 4 通过）与 `alignment.md`（5 ILO 各自 mastery_threshold）。**交叉练习**（interleaving，A1B1C1B1A2C1A2B2A3B2C1A3C3A3B2 顺序，非块状）促进迁移；**提取练习**（retrieval practice，tutorial.ipynb cell2 强制 pre-tutorial essay）优于重读。

**弱项循环**（weak_loop）：连续 2 次 drill 失败触发回退上一 drill + Worked Example 重看 + schedule.json 间隔缩短为 [1,2,4,8]。**限频**：tutorial 每单元每天 1 次，防依赖。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

**研究产出关键词**：research output / IMRaD / 可复现 reproducibility / OSF preregistration 预注册 / FAIR / contribution 贡献 / linked_paper (arXiv 1608.00060 DML + 1510.04342 因果森林 + 1702.05675 Uplift + 2306.05685 LLM-as-judge) / research-to-practice / NeurIPS。

**产业链接关键词**：industry linkage / consulting 咨询项目 / case study 教学案例 / guest lecture 客座讲座 / internship 实习 / deployment 部署场景 (Microsoft ExP CUPED / Netflix DML / Booking.com Uplift / Uber / Amazon / LinkedIn)。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/capstone-ai-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：端到端AI原生企业闭环（综合）。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

本单元新增 `from_scratch.md`：手写 ATE/IPW 估计器 + DML 双重机器学习，从零构建 numpy 版因果估计器，不调 DoWhy、不调 econml、不调 sklearn。对应 rohitg00 P19/52 Experiment Runner + P19/53 Result Evaluator。core_algorithm 从第一性原理推导 IPW 逆倾向得分加权 $\hat{\text{ATE}}_{\text{IPW}} = \frac{1}{n}\sum[\frac{T_i Y_i}{\hat{e}(X_i)} - \frac{(1-T_i)Y_i}{1-\hat{e}(X_i)}]$ + DML 双重正交 $\hat{\theta} = \frac{\sum \tilde{T}_i \tilde{Y}_i}{\sum \tilde{T}_i^2}$，code_artifact 含手写 numpy 骨架（logistic_irls 倾向得分 -> ipw_ate 加权估计 -> ols nuisance -> dml_ate 残差正交），verification_property 验证 IPW/DML 收敛真实 ATE + 朴素有偏 + DML 优于朴素。与 notes.md 的 DoWhy+econml 库实现对比：库版用 CausalModel.estimate_effect + LinearDML 黑箱，from-scratch 版让因果估计可逐行审计。这是因果实验设计的可计算内核--ai-engineering-from-scratch 的工程底座。
