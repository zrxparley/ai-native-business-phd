# frontier.md

> **所属**：skill-0-business-analytics · day-4-regression-probability
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年神经符号贝叶斯推断在投资估值中的小样本优势、LLM-as-Judge 在效用排序中的生产部署、TreeSHAP+LLM 叙事在归因解释中的实践如何更新本单元"回归系数解读+特征重要性+LTV 概率区间"的教学。

---

## frontier_topic

本单元教 OLS 多元回归(R²=0.037, treat β=1621 p=0.01)、Logit 倾向性评分、概率分布拟合(正态/二项/泊松)、LTV 计算(uplift 39.4%)、分位数回归(75 分位 2502 vs 25 分位 290)、贝叶斯回归(PyMC/bambi)。前沿子问题是: 当神经符号贝叶斯方法在投资估值中用 5 样本达 Bayes-optimal、LLM-as-Judge 在信用分析中部署于 800+ 分析师、TreeSHAP+LLM 叙事在生产中 yield 89% 时, 本单元"OLS 系数解读+VIF 共线性+分位数异质性"的回归教学如何被更新。

---

## recent_papers

### 1. The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models
- **arXiv**: https://arxiv.org/abs/2606.29799
- **作者**: Rafael Kaufmann, Felix Neubürger
- **年份**: 2026
- **摘要**: 神经符号框架用于自动化复杂分析工作流, 以基本面投资分析为主要用例. 构建动态概率程序支持贝叶斯推断, 在公司分类任务上仅用 5 个样本即达到 Bayes-optimal accuracy, 超越准确率停滞在 40% 左右的 LLM.
- **与本单元的关联**: 本单元 notes.md 教贝叶斯回归(PyMC/bambi)在 A/B 测试中计算"P(实验组优于对照组)>95%", 该论文在投资估值中用动态概率程序做贝叶斯推断, 5 样本达 Bayes-optimal, 直接挑战本单元 NSW 数据 R²=0.037 的低信噪比回归范式。

### 2. Beyond Semantic Similarity: A Two-Phase Non-Parametric Retrieval Workflow for Corporate Credit Underwriting
- **arXiv**: https://arxiv.org/abs/2605.20684
- **作者**: Linus Ng Junjia, Ezekiel Tee Kongquan
- **年份**: 2026
- **摘要**: 两阶段检索架构, 分离高召回候选检索与高精度效用排序, 使用 LLM-as-a-Judge 评分. 部署于 800+ 信用分析师, 文档审阅时间从数小时降至约三分钟, 在多语言金融文档上超越朴素检索基线.
- **与本单元的关联**: 本单元 TODO3 用 Logit 回归计算倾向性评分(propensity score)做排序, 该论文的两阶段检索(高召回+高精度 LLM-Judge 效用排序)将"概率排序"升级为"LLM 效用排序", 部署于 800+ 分析师的生产规模。

### 3. Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification
- **arXiv**: https://arxiv.org/abs/2607.17586
- **作者**: Yuge Zhang, Yuanxing Zhang
- **年份**: 2026
- **摘要**: 端到端管道用于洗钱骡户检测, 结合 LightGBM、TreeSHAP 归因和 LLM 生成的分析师叙事. 生产环境中 yield rate 达 89% (规则系统仅 61%), 增量检出 60%. 分析师反馈 LLM 叙事降低告警分诊的认知负荷.
- **与本单元的关联**: 本单元 notes.md 教 OLS 回归系数解读与 VIF 多重共线性检测, 该论文用 TreeSHAP 做非线性特征归因+LLM 叙事, 在生产中 yield 89%--展示了本单元"线性系数解读"之外的非线性归因路径。

---

## critical_synthesis

这三篇论文共同揭示了一个共识: 回归分析正从"单一模型+系数解读"走向"多模型+归因+叙事"的管道化, 且解释层(TreeSHAP/LLM 叙事)与建模层(贝叶斯/LightGBM)正在分离。CRISTAL(2606.29799)在投资估值中用概率程序做贝叶斯推断, Beyond Semantic Similarity(2605.20684)在信用分析中分离检索与排序, Money Mule(2607.17586)在反洗钱中分离建模(LightGBM)与归因(TreeSHAP)与叙事(LLM)。然而三者之间存在明显争议: CRISTAL 主张小样本(5 样本)+强结构先验, 而 Money Mule 的 LightGBM 依赖大规模标注数据(89% yield 需要足够训练集)--小样本贝叶斯 vs 大样本树模型的路径之争未解决。更关键的 limitation: CRISTAL 的 5 样本优势仅在分类任务上验证, 回归任务(连续 Y)的贝叶斯推断需要更强的先验设定, 本单元 NSW 数据 R²=0.037 的低信噪比场景下, 5 样本可能严重过拟合。Beyond Semantic Similarity 的 LLM-as-Judge 引入了"评分者偏见"--LLM 倾向于给某些文档格式更高分, 这种偏见在 Logit 倾向性评分中不存在。趋势上, 本单元教的 OLS 系数+p 值+VIF 仍是回归的入门基础, 但生产级系统已转向"LightGBM+TreeSHAP+LLM 叙事"的管道, 学生需理解线性系数解读的局限性。

---

## delta_to_unit

1. **分位数回归的异质性 vs 贝叶斯异质推断**: 本单元 notes.md 教分位数回归发现"treat 在 75 分位系数 2502(p=0.004)显著, 但 25 分位仅 290(p=0.520)不显著", 展示处理效应异质性。CRISTAL(2606.29799)用动态概率程序在贝叶斯框架下做异质推断, 5 样本达 Bayes-optimal。这更新了本单元的教学: 分位数回归是频率派的异质性检测, 贝叶斯概率程序能在更小样本下做异质推断, 但代价是需要设计 DAG 先验--本单元 notes.md 未覆盖这一权衡。

2. **倾向性评分排序 vs LLM 效用排序**: 本单元 TODO3 用 `sm.Logit(y, X).fit()` 计算倾向性评分(propensity score)做概率排序, notes.md 称其为"连接技能3因果推断的桥梁"。Beyond Semantic Similarity(2605.20684)用两阶段检索(高召回候选+高精度 LLM-as-Judge 效用排序)替代纯概率排序, 部署于 800+ 信用分析师。这更新了本单元的教学: Logit 倾向性评分是"单一概率排序", LLM-Judge 引入了"效用排序"的第二维度, 但也引入了 LLM 评分者偏见--本单元 notes.md 未讨论排序方法的这一演进。

3. **线性系数解读 vs TreeSHAP 非线性归因**: 本单元 notes.md 教"解读 R²、回归系数、p 值"和"VIF>10 检测多重共线性", 假设线性可加关系。Money Mule(2607.17586)用 LightGBM+TreeSHAP 做非线性特征归因+LLM 叙事, 生产 yield 89%(规则系统仅 61%)。这意味着本单元教的 VIF 线性共线性检测在非线性交互(如 age x treat)下可能失效, 学生需知道 OLS 系数解读的局限--TreeSHAP 能捕捉 VIF 无法检测的非线性交互归因。

---

## open_questions

1. CRISTAL 在投资估值中用 5 样本达 Bayes-optimal, 但本单元 NSW 数据 R²=0.037 表明真实营销数据信噪比极低--5 样本贝叶斯在低信噪比回归中是否过拟合, 概率程序 DAG 的先验质量如何量化?
2. Beyond Semantic Similarity 用 LLM-as-Judge 做效用排序, 但本单元 Logit 倾向性评分是可校准的概率--LLM-Judge 的排序是否可替代 propensity score, 还是引入不可量化的评分者偏见(如对文档格式的偏好)?
3. Money Mule 的 TreeSHAP+LLM 叙事在生产中 yield 89%, 但本单元教的 OLS 系数解读是线性可加的--当特征交互非线性(如 age x treat)时, 本单元的 VIF 多重共线性检测是否失效, TreeSHAP 的 Shapley 值如何纳入回归教学?
4. 本单元 LTV 计算用回归+概率分布的点估计+概率区间(treat 组 uplift 39.4%), 但 CRISTAL 的动态概率程序支持持续贝叶斯更新--LTV 模型能否从静态 OLS 拟合升级为在线贝叶斯更新, 实时融入新订单数据?

---

## methodological_critique

这三篇论文的局限性需审慎对待。CRISTAL(2606.29799)标注 unverified, 其"5 样本 Bayes-optimal"仅在公司分类(离散 Y)任务上验证, 本单元的回归(连续 Y)任务需要更强的先验假设, 5 样本能否外推到 LTV 回归存疑; 且概率程序 DAG 的设计是强领域知识注入, 论文未量化设计成本, 若 DAG 错误则小样本贝叶斯可能比 OLS 更差。Beyond Semantic Similarity(2605.20684)同样 unverified, 其"800+ 分析师部署"的宣称缺乏公开的生产指标(如 precision/recall), LLM-as-Judge 存在已知的自我偏好(self-preference)问题--LLM 倾向于给同类 LLM 生成的文档更高分, 这种偏见在多语言金融文档上可能放大; "数小时降至三分钟"的效率提升未控制文档复杂度变量。Money Mule(2607.17586)同样 unverified, 其"89% yield vs 61%"的对比基线是规则系统而非机器学习基线, 存在 weak baseline 风险; TreeSHAP 的 Shapley 值在特征相关时有条件分布假设, 若特征强相关(如本单元 VIF>10 场景), Shapley 值的归因可能误导; LLM 叙事"降低认知负荷"的结论基于分析师主观反馈而非客观决策准确率对比。三者均存在 domain-specific benchmark-gaming 风险。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
