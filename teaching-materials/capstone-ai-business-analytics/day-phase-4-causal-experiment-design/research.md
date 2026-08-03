# research.md -- Capstone Phase 4 因果实验设计与验证 · 研究产出层 (v7.0)

> 质量契约：CQ-C4-1。

> 本文件是 v7.0 升级新增的**研究产出层**：把 Phase 4 在真实 NSW RCT 数据 (445 行) 上做的 DoWhy 四步 + DML + 因果森林 + CUPED + 安慰剂检验工作，重构为一篇可发表/可复现的研究工件。所有数字、arXiv 链接、数据集均来自 `notes.md` 与 `reading.md`，不联网查证。

---

## research_question

**核心研究问题**：在 NSW 职业培训真实 RCT (445 行) 上，DML 双重机器学习、因果森林、CUPED 三种 2026 前沿因果推断方法在 ATE/CATE 估计上是否比朴素均值差与 DoWhy 线性后门调整更稳健，且异质效应 (CATE) 是否能识别出"年长组获益更大"的可解释子群体？

可实证拆解为三个子问题：(RQ1) 朴素 ATE 与 DML ATE=1940 (95% CI [608, 3271]) 的差异是否来自混杂偏差而非随机波动？(RQ2) 因果森林 CATE=1811 与 DML CATE 是否一致识别出 age 子群体的异质效应？(RQ3) CUPED 用 re75 调整 re78 后，方差缩减后的等效样本量提升能否让安慰剂检验 p=0.98 仍不拒绝零效应？

---

## contribution

相对已有文献，本研究工件的增量贡献声明如下：

1. **相对 Chernozhukov et al. 2018 (DML 原论文, arXiv 1608.00060)**：原论文用模拟数据与半合成数据演示 double/debiased 性质；本文用**真实 NSW RCT** (`causaldata.nsw_mixtape`, 445 行) 验证 LinearDML 在小样本+真实协变量不均衡下的 ATE 估计是否仍保持标称覆盖率，给出 ATE=1940 CI[608, 3271] 的实证区间。
2. **相对 Wager & Athey 2018 (因果森林, arXiv 1510.04342)**：原论文强调 honest splitting 的理论保证；本文进一步用 econml `CausalForestDML` 在同一 NSW 数据上对比 DML 的 CATE，检验两种方法在"年长组获益更大"这一可解释子群体上是否给出一致排序 (因果森林 CATE=1811)。
3. **相对 Deng et al. 2013 (CUPED, KDD)**：原 CUPED 论文在 Microsoft 大样本 A/B 上验证方差缩减；本文在**小样本 (n=445) RCT** 上检验 CUPED 用 re75 作前实验协变量调整 re78 后，方差缩减比例是否接近理论 ρ²，以及 CUPED ATE=1747 与未调整 ATE 的相对效率。
4. **相对 Gutierrez & Gérardy 2017 (Uplift 综述, arXiv 1702.05675)**：综述讨论 T/S/X-learner；本文把 DML 与因果森林的 CATE 直接用作 Uplift 排序信号，验证在 NSW 营销映射场景下两种 CATE 估计的子群体优先级一致性。
5. **方法学整合**：首次在同一真实数据集上同时跑通 DoWhy 四步 (建模→识别→估计→反驳) + DML + 因果森林 + CUPED + 安慰剂检验 (p=0.98) + deepeval 自定义 BaseMetric 评估 Agent 因果证据使用质量，形成可复现的"因果实验设计+Agent 评估"双闭环工件。

---

## linked_paper

本研究工件锚定以下 5 篇真实论文 (链接全部来自 `reading.md` 已验证深链)：

| # | 论文 | 作者/年份/venue | 链接 | 关联说明 |
|---|------|----------------|------|---------|
| 1 | Double/Debiased Machine Learning | Chernozhukov et al. 2018, Econometrics Journal | https://arxiv.org/abs/1608.00060 | TODO5 LinearDML 的理论基础；§2 double/debiased 框架、§3 cross-fitting 直接对应 solution.ipynb 的 `econml.dml.LinearDML` 调用，产出 ATE=1940 CI[608, 3271] |
| 2 | Estimation and Inference of Heterogeneous Treatment Effects using Random Forests (因果森林) | Wager & Athey 2018, JASA | https://arxiv.org/abs/1510.04342 | TODO6 `CausalForestDML` 的理论基础；§2 honest splitting 避免 adaptive bias，§4 因果森林算法，对应 CATE=1811 与"年长组获益更大"的子群体发现 |
| 3 | Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED) | Deng et al. 2013, KDD | https://dl.acm.org/doi/10.1145/2487575.2488215 | TODO4 CUPED 方差缩减的理论基础；§3 方差缩减公式推导 θ=Cov(Y,X_pre)/Var(X_pre)，对应 re75 调整 re78 后 CUPED ATE=1747 |
| 4 | Causal Inference and Uplift Modeling: A review of the approaches | Gutierrez & Gérardy 2017 | https://arxiv.org/abs/1702.05675 | Uplift/增量建模综述，对比 T-learner/S-learner/X-learner；DML 与因果森林的 CATE 估计可直接用于 Uplift 排序，对应"哪些用户可被说服"的营销映射 |
| 5 | LLM-as-a-judge | Zheng et al. NeurIPS 2023 | https://arxiv.org/abs/2306.05685 | TODO7 自定义 BaseMetric (deepeval fallback) 评估 Agent 输出中因果证据使用质量的理论基础；§3 评估方法、§5 已知偏差对应规则化简化版 LLM-judge |

辅助参考：贝叶斯因果森林 (BCF, https://projecteuclid.org/journals/bayesian-analysis/volume-15/issue-3/Bayesian-Causal-Forest-Assessing-the-Mechanisms-through-which-a-High/10.1214/19-BA1195.full) 在 n=445 小样本下提供后验分布，是频率方法 (DML/因果森林) 的互补不确定性量化。

---

## imrad_outline

**IMRaD 四段大纲** (引用 `starter.ipynb`/`solution.ipynb` 真实方法与本单元真实数字)：

### Introduction (引言)
- **动机**：营销 Agent 的干预是否真的有效？朴素均值差有偏 (混杂偏差)，观测数据需因果推断；2026 前沿方法 (DML/CUPED/因果森林) 在小样本真实 RCT 上的稳健性尚缺统一实证。
- **Gap**：DML/因果森林/CUPED 三者原论文分别用模拟/半合成/大样本数据，缺少在同一**真实小样本 RCT (NSW, n=445)** 上的横向对比与可解释子群体 (CATE) 一致性检验。
- **贡献**：(1) 在 NSW 上同时跑通 DoWhy 四步 + DML + 因果森林 + CUPED + 安慰剂检验；(2) 给出 ATE=1940 CI[608, 3271]、因果森林 CATE=1811、CUPED ATE=1747、安慰剂 p=0.98 的可复现数字；(3) 用 deepeval 自定义 BaseMetric 闭环评估 Agent 因果证据使用质量。

### Methods (方法)
- **协议与 estimand**：正式研究先冻结 `protocol.md`；primary estimand 为 ATE = E[Y(1)-Y(0)]，secondary estimand 为按 age/nodegree/marr 等预声明子群体的 CATE。处理、结果窗口、目标人群、SUTVA 和业务决策阈值必须预声明。
- **数据**：`causaldata.nsw_mixtape` 真实 RCT (Dehejia & Wahba 1999)，n=445；处理 `treat`，结果 `re78`，前实验协变量 `re75` (CUPED 用)，协变量 age/educ/black/hisp/marr/nodegree/re74。报告需补缺失数据、处理/对照样本数、重叠性/正值性和协变量平衡。
- **识别策略**：DoWhy `CausalModel` 声明 DAG → `identify_effect` 后门准则 → `estimate_effect` 后门调整/PSM/DML → `refute_estimate`。发表级报告必须给 DAG 边、调整集、不可观测混杂威胁和至少 placebo/random_common_cause/data_subset 三类 sensitivity/refutation。
- **估计方法**：(1) 朴素均值差 (有偏基线)；(2) DoWhy 线性后门调整；(3) `econml.dml.LinearDML`；(4) `econml.dml.CausalForestDML`；(5) CUPED 调整 Y_adj=Y−θ(X_pre−X̄_pre)。二值处理的 DML `model_t` 应使用分类器，若 notebook 使用回归器则必须标注为教学实现差异。
- **统计计划**：报告 95% 置信区间、power/MDE、多重检验控制、bootstrap 次数、cross-fitting 折数、missingness 处理和业务显著阈值；p 值不能单独作为上线依据。
- **Agent 评估**：自定义 `BaseMetric` (deepeval fallback)，规则化检验 Agent 输出是否引用 ATE/CI/CATE/反驳检验结果。

### Results (结果)
- **RQ1 (ATE 比较)**：朴素 ATE 偏高 (混杂未调整)；DoWhy 后门 ATE 居中；DML ATE=1940, 95% CI [608, 3271] 不含零，最可信 (double/debiased + cross-fitting)。
- **RQ2 (CATE 一致性)**：因果森林 CATE=1811，DML CATE 与之在 age 子群体上排序一致——**年长组获益更大**，两种方法互相印证。
- **RQ3 (CUPED 方差缩减)**：CUPED ATE=1747 与未调整 ATE 点估计接近，但置信区间更窄 (等效提升样本量≈1/(1−ρ²))；安慰剂检验 p=0.98 不拒绝零效应，证明原估计非伪相关。
- **Agent 评估**：自定义 BaseMetric 在 Phase 3 Agent 输出上给出因果证据使用质量分数，识别"Agent 是否正确引用 CI 与反驳检验"。

### Discussion (讨论)
- **贡献边界**：NSW 是职业培训数据，营销映射是同构而非同质；n=445 小样本下 DML 的 cross-fitting 折数需谨慎 (建议 cv=5)；CATE 子群体发现需后续访谈定性验证 (解释性序列设计阶段 2)。
- **局限**：(1) 单一数据集，外部效度有限；(2) 安慰剂检验 p=0.98 仅证伪伪相关，不证因果方向；(3) Agent 评估的 BaseMetric 是规则化简化版，未跑完整 LLM-as-a-judge。
- **未来工作**：(1) 在 LaLonde/CPS/PSID 配对数据上复现；(2) 引入 BCF 贝叶斯因果森林做不确定性量化；(3) 把 CATE 接入 Uplift 在线排序 + MAB (arXiv 1904.01580) explore-exploit 闭环。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (≥6 项勾选)：

- [x] **Code (代码)**：完整代码在 `solution.ipynb` (9 个 code cells，与 starter.ipynb 9 cells 一一对应，scaffold=0, TODO 残留=0)；`starter.ipynb` 为 TODO 填空版 (7 个 TODO 脚手架)。
- [x] **Data (数据)**：真实 RCT 数据集 `causaldata.nsw_mixtape` (Dehejia & Wahba 1999)，n=445 行；来源 https://github.com/NickCH-K/causaldata ，PyPI https://pypi.org/project/causaldata/ ；许可见 `data/README.md` (NSW 公共领域 + causaldata MIT)。
- [x] **Seeds (随机种子)**：`random_state=42` 全程固定 (LinearDML/CausalForestDML/RandomForest model_y/model_t/PSM 匹配)；cross-fitting cv=5 固定。
- [x] **Environment (环境)**：Python 3.11 + econml 0.15 + dowhy 0.8 + causaldata 0.1 + scikit-learn 1.4 + deepeval 1.4；`data/README.md` 列出完整依赖与版本。
- [x] **Preregistration (预注册)**：`protocol.md` 提供可审计预分析模板；notes.md 学习目标只能算教学预声明，正式研究必须在查看结果前冻结 estimand、DAG、primary/secondary endpoints、power/MDE、多重检验、缺失数据和 sensitivity 计划。
- [x] **FAIR (数据可发现/可访问/可互操作/可重用)**：数据 Findable (causaldata GitHub+PyPI 可搜索)、Accessible (pip install 一行获取)、Interoperable (DataFrame 标准格式，列名 treat/re74/re75/re78/age/educ 跨研究通用)、Reusable (MIT 许可 + Dehejia-Wahba 1999 文档完整)。
- [x] **Reproduction script (复现脚本)**：`solution.ipynb` 从 `from causaldata import nsw_mixtape` 到 `refute_estimate` 全链路可一键 Run All；`verify_unit.py` 7/7 + `verify_v6_unit.py` 5/5 + `verify_v7_unit.py` 3/3 = 15/15 自动验收。
- [x] **Statistical reporting (统计报告)**：所有 ATE/CATE 报告点估计 + 95% CI + p 值 (安慰剂 p=0.98)；DML CI [608, 3271] 不含零；CUPED 报告方差缩减比例。发表级版本还必须补 MDE/power、多重检验、缺失数据、重叠性/正值性、协变量平衡和敏感性分析矩阵。

---

## research_to_practice

本研究工件可沿三条路径翻译为实践工件：

1. **HBS Working Paper → HBR Article**：把"NSW 上 DML/CUPED/因果森林三方法对比 + 年长组 CATE 更大"重构为 HBS Working Paper (Methodology section 引用 Chernozhukov 2018 + Wager-Athey 2018 + Deng 2013)，再压缩为 Harvard Business Review 文章，标题如 *"Why Your A/B Test Is Lying to You: A Causal Toolkit for Marketing Agents"*，面向 CMO/Head of Growth 讲"朴素 ATE 有偏、DML 最可信、CUPED 提灵敏度、因果森林找可被说服群体"。
2. **MIT Sloan Teaching Case**：把 Phase 4 的"营销 Agent 干预是否有效"作为教学案例钩子，protagonist 是 Head of AI Marketing，决策点是"是否把 DML ATE=1940 作为 Agent 上线的 go/no-go 门槛"，tension 是"统计显著但 CI 下限 608 是否业务显著"。本单元 `industry.md` 的 case_study 段落给出完整钩子。
3. **企业白皮书 + Imperial MSc BA 咨询项目**：把 DoWhy 四步 + DML + CUPED + 因果森林封装为"因果实验设计 SOP"白皮书，赞助企业 (如 Booking.com/Microsoft ExP/Netflix) 提供 A/B 平台日志数据，Imperial MSc BA 4-5 人团队 8 周交付原型 (详见 `industry.md` consulting_project 段落)。研究产出遵循 IMRaD (本文件 §imrad_outline) + DSR (Hevner 设计科学) + OSF 预注册 + FAIR + 可复现研究标准；产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。
