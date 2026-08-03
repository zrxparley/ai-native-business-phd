# Capstone Phase 4 因果实验设计 Protocol（CQ-C4-1）

> 状态：可审计模板。正式研究必须在查看结果前冻结本文件；任何分析后改动都记录为 amendment。

## 1. 研究问题与 estimand

- Primary question：营销干预是否对目标结果产生正向因果效应？
- Teaching data：NSW `causaldata.nsw_mixtape`。
- Primary estimand：ATE = E[Y(1)-Y(0)]，其中 T=`treat`，Y=`re78`。
- Secondary estimands：按 age、nodegree、marr 等预声明子群体的 CATE。
- 业务迁移必须补充目标人群、处理版本、结果窗口、干预成本和 SUTVA 假设。

## 2. DAG 与识别

- 核心节点：T=`treat`，Y=`re78`，X=`age/educ/black/hisp/marr/nodegree/re74/re75`。
- 后门调整集：`age, educ, black, hisp, marr, nodegree, re74, re75`。
- 不可观测混杂：动机、地区劳动力市场、项目可及性等无法完全观测；报告必须说明这限制外部效度。
- DAG amendment：任何新增/删除边或协变量，都必须记录原因和对估计量的影响。

## 3. 数据质量、重叠性与协变量平衡

- 报告处理组/对照组样本数、缺失率和删除/插补策略。
- 重叠性/正值性：报告倾向得分分布和共同支持区间；无共同支持的样本不得用于 CATE 外推。
- 协变量平衡：报告处理前、匹配/IPW/DML 后的 SMD；关键协变量 |SMD| > 0.1 时必须解释。

## 4. 统计分析计划

- 主分析：DoWhy 后门调整与 DML ATE。
- 次分析：CUPED 方差缩减、因果森林 CATE、Agent 因果证据 BaseMetric。
- 置信区间：所有 ATE/CATE/CUPED 报告 95% CI。
- power/MDE：报告样本量、结果方差、alpha、目标 power、minimum detectable effect；NSW 小样本只作教学证据。
- 多重检验：预声明 primary outcome；secondary outcomes 和 CATE 子群体使用 Holm 或 Benjamini-Hochberg FDR。
- Missingness：报告缺失数据表；不得静默 dropna。

## 5. 敏感性分析

最低矩阵：

| 检验 | 通过标准 |
|---|---|
| placebo_treatment_refuter | 估计接近 0，且不改变主结论 |
| random_common_cause | 主估计符号稳定，偏离不超过预设阈值 |
| data_subset_refuter | 子样本估计方向稳定 |
| bootstrap / Rosenbaum bounds | 量化小样本不确定性或隐藏混杂敏感性 |

## 6. 业务决策阈值

- Go：主 estimand 的 CI 下限超过实施成本或最低业务收益阈值。
- No-go：CI 跨越负向业务阈值，或关键子群体存在显著负效应且无保护策略。
- Hold：统计显著但业务阈值未达标，或 power/MDE 显示样本不足。

## 7. 环境锁与审计链

- 必须附环境锁文件或 run manifest：Python、dowhy、econml、causaldata、scikit-learn、numpy、pandas、statsmodels、deepeval 版本。
- 记录 random_state、cross-fitting cv、bootstrap 次数、notebook hash、protocol hash、输出表 hash。
- 二值 treatment 的 DML `model_t` 推荐分类器；若使用回归器，必须作为教学实现差异披露。

## 8. 可发表报告清单

- Methods：estimand、DAG、识别假设、overlap/balance、缺失数据、估计器、CI、power/MDE、多重检验。
- Results：ATE/CATE/CUPED、置信区间、敏感性分析、业务阈值判定。
- Discussion：外部效度、不可观测混杂、小样本限制、Agent 评估局限。
- Appendix：protocol amendment、环境锁文件、审计 manifest。
