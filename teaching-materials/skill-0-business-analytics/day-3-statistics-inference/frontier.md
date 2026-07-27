# frontier.md

> **所属**：skill-0-business-analytics · day-3-statistics-inference
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年神经符号贝叶斯推断(5 样本达 Bayes-optimal)、AI agent 的证据天花板消融、多 agent 视角辩论如何更新本单元"频率派 vs 贝叶斯派"与"可复现研究"的教学。

---

## frontier_topic

本单元教描述统计(均值/中位数/偏度)、假设检验(t-test/chi2)、置信区间、Beta-Binomial 贝叶斯推断(Beta(α+s, β+n-s))、ASA p 值六原则、p-hacking 与 OSF 预注册。前沿子问题是: 当神经符号贝叶斯方法用 5 个样本达到 Bayes-optimal、AI agent 的证据质量设定决策天花板(0.96 vs 0.25-0.38)、多 agent 视角辩论逼近人类编码时, 本单元"频率派 vs 贝叶斯派"的二元框架与"p 值+效应量+CI"的三件套如何被更新。

---

## recent_papers

### 1. The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models
- **arXiv**: https://arxiv.org/abs/2606.29799
- **作者**: Rafael Kaufmann, Felix Neubürger
- **年份**: 2026
- **摘要**: 神经符号框架用于自动化复杂分析工作流, 以基本面投资分析为主要用例. 构建动态概率程序支持贝叶斯推断, 在公司分类任务上仅用 5 个样本即达到 Bayes-optimal accuracy, 超越准确率停滞在 40% 左右的 LLM.
- **与本单元的关联**: 本单元 TODO6 用 scipy.stats.beta 手动实现 Beta-Binomial 后验估计, 该论文用动态概率程序做贝叶斯推断, 5 样本达 Bayes-optimal, 直接挑战本单元"小样本频率派 p 值不稳定"的论断。

### 2. AI Scientists Are Only as Good as Their Evidence: A Stratified Ablation of Proprietary Data and Reasoning Skills in Drug-Asset Valuation
- **arXiv**: https://arxiv.org/abs/2606.09556
- **作者**: Yinan Wang
- **年份**: 2026
- **摘要**: 在生产级药物资产估值 agent 上进行受控三臂消融实验, 表明专有证据设定 AI 决策质量上限. 完整系统 (含专有语料) 恢复 0.96 的 gold competitive records, 而非专有变体仅 0.25-0.38. 推理支架改善校准但无法突破事实天花板.
- **与本单元的关联**: 本单元 notes.md 教 ASA p 值六原则与 p-hacking 防范, 该论文的"证据天花板"(0.96 vs 0.25-0.38)表明推理方法(p 值/CI)本身也是"推理支架", 无法弥补数据质量上限--呼应本单元"Garbage In, Garbage Out"的数据治理命题。

### 3. Agent-as-Peer-Debriefer: A Multi-Agent Framework with Perspective-Based Refinement for Qualitative Analysis
- **arXiv**: https://arxiv.org/abs/2605.24600
- **作者**: Zhimin Lin, Kun Cheng
- **年份**: 2026
- **摘要**: 多 agent 定性数据分析框架, 引入同行辩论, 三个 Peer-Debriefing Agent 分别采用理论驱动、数据驱动、应用视角. 在三个数据集和三个 LLM 上, 基于视角的精化比单 LLM 基线更贴近人类编码, 各视角产生不同的权衡.
- **与本单元的关联**: 本单元 notes.md 教"频率派 vs 贝叶斯派"二元对比, 该论文的三视角辩论(理论/数据/应用)提供了一个第三认识论轴, 更新了本单元的统计范式对比框架。

---

## critical_synthesis

这三篇论文共同揭示了一个正在形成的共识: 在统计推断中, 证据质量(数据)设定决策天花板, 推理方法(p 值/贝叶斯/多视角)只能在天花板内优化校准, 无法突破它。AI Scientists(2606.09556)的消融实验(0.96 vs 0.25-0.38)是最直接的证据, CRISTAL(2606.29799)的"5 样本 Bayes-optimal"本质上也是强先验(高质量证据)弥补小样本, Agent-as-Peer-Debriefer(2605.24600)的三视角辩论则表明单一视角(无论频率派还是贝叶斯派)都有盲区。然而, 三者之间存在明显争议: CRISTAL 主张小样本+强先验+贝叶斯最优, 而 AI Scientists 的消融暗示没有专有证据再好的推理支架也只到 0.25-0.38--两种路径对小样本的乐观程度截然不同。更关键的 limitation: CRISTAL 的"5 样本 Bayes-optimal"仅在公司分类任务上验证, 分类任务的先验可由本体定义, 但本单元的营销 A/B 测试转化率估计中, 先验从何而来? Agent-as-Peer-Debriefer 的三视角虽贴近人类编码, 但其"视角"是预设的(理论/数据/应用), 未解决"视角本身是否完备"的元问题。趋势上, 本单元教的"频率派 vs 贝叶斯派"二元对比正被"证据质量 x 推理方法 x 视角多元"的三维框架取代, 但 ASA p 值六原则作为最低标准仍是不可放弃的底线。

---

## delta_to_unit

1. **小样本贝叶斯的再评估**: 本单元 notes.md 称"新产品上线初期只有几十次曝光, 频率派 p 值不稳定, 贝叶斯方法通过先验信息给出更合理的估计", TODO6 用 Beta(1+s, 1+n-s) 手动实现。CRISTAL(2606.29799)将这一论断推到极致--5 个样本即达 Bayes-optimal, 但前提是动态概率程序(强结构化先验)。这更新了本单元的教学: 小样本贝叶斯的优势不是"任意先验都行", 而是"结构化先验(概率程序 DAG)的质量决定上限"--本单元的 Beta(1,1) 均匀先验是最弱先验, 与 CRISTAL 的结构化先验有质的差距。

2. **p 值三件套作为"推理支架"的局限**: 本单元 notes.md 教"报告 p 值+效应量+CI"三件套对抗 p-hacking, 并引用 ASA p 值六原则。AI Scientists(2606.09556)发现"推理支架改善校准但无法突破事实天花板"(0.96 vs 0.25-0.38)。这意味着本单元的三件套本身也是"推理支架"--当营销数据质量差(如转化率测量有偏)时, 再规范的 p 值报告也无法弥补, 这是 notes.md 未显式讨论的局限。

3. **二元范式对比 vs 三视角辩论**: 本单元 notes.md 用"频率派 vs 贝叶斯派"表格做二元对比。Agent-as-Peer-Debriefer(2605.24600)的三视角辩论(理论驱动/数据驱动/应用视角)提供了一个更丰富的认识论框架--频率派对应"数据驱动", 贝叶斯派对应"理论驱动(先验)", 而"应用视角"是本单元未覆盖的第三轴(决策效用)。这更新了本单元的范式教学: 从二元对立走向三方权衡。

---

## open_questions

1. CRISTAL 用 5 个样本达到 Bayes-optimal, 但本单元 Beta-Binomial 的 Beta(1,1) 均匀先验需要多少样本后验才收敛--5 样本的优势是否仅限于强结构化先验(概率程序 DAG), 营销 A/B 测试的 Beta(1,1) 弱先验无法复现?
2. AI Scientists 发现推理支架无法突破事实天花板(0.96 vs 0.25-0.38), 那么本单元教的 ASA p 值六原则+效应量+CI 三件套是否也是"推理支架"--在营销数据存在选择偏倚时, 三件套能在多大程度上校准而非掩盖偏倚?
3. Agent-as-Peer-Debriefer 的三视角辩论(理论/数据/应用)是否可移植到本单元的"频率派 vs 贝叶斯派"对比, 形成三方认知对抗--"应用视角"(决策效用)在营销 A/B 测试中如何量化?
4. 本单元教 scipy.stats.ttest_ind 假设数据无测量误差, 但 AI Scientists 的消融表明专有证据 vs 公开证据差距 0.96 vs 0.25-0.38--营销 A/B 测试中的"证据质量"(日志完整性/归因窗口)如何量化并纳入假设检验?

---

## methodological_critique

这三篇论文的局限性需审慎对待。CRISTAL(2606.29799)标注 unverified, 其"5 样本 Bayes-optimal"仅在公司分类这一单一任务上测得, 分类任务有明确本体可编码为先验, 但本单元的营销转化率估计无此类本体, 5 样本优势能否外推存疑; 更严重的是, 概率程序 DAG 的设计本身是强领域知识注入, 论文未量化"设计 DAG 的人力成本", 若 DAG 设计错误, 5 样本可能比频率派更差。AI Scientists(2606.09556)同样 unverified, 其三臂消融仅在药物资产估值这一垂直领域进行, "0.96 vs 0.25-0.38"的差距可能反映该领域专有数据库的特殊性而非普适规律; 且"推理支架无法突破事实天花板"的结论可能低估了推理方法在中等证据质量下的边际价值。Agent-as-Peer-Debriefer(2605.24600)的"三视角更贴近人类编码"基于三个数据集, 但"人类编码"本身是否金标准存疑--定性研究中人类编码者间信度(kappa)常低于 0.7, 以有噪声的人类编码为 ground truth 可能误导。三者均存在 domain-specific 风险: 在自选领域展示优势, 未在统计推断的标准基准(如 ASA 推荐)上验证。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
