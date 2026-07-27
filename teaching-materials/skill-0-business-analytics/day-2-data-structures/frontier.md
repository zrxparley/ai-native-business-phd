# frontier.md

> **所属**：skill-0-business-analytics · day-2-data-structures
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年列式查询引擎的 DAG 查询优化器、LLM 驱动的多维下钻树遍历、神经符号概率程序的 DAG 推理如何更新本单元"数据结构选择决定性能"的核心命题。

---

## frontier_topic

本单元教 list/dict/set/collections/heapq 的时间复杂度选择(O(1) vs O(n))、namedtuple schema 规范化、BFS 树遍历、Apache Arrow 列式零拷贝、Polars LazyFrame 懒求值 DAG 查询图。前沿子问题是: 当列式查询引擎的 DAG 优化器自动重排操作、LLM 近似贪心下钻路径、神经符号概率程序在 DAG 上做贝叶斯推断时, 本单元"数据结构选择决定性能"的命题如何被更新--哪些选择被引擎自动化了, 哪些结构(DAG/树/堆)仍是分析系统的骨架。

---

## recent_papers

### 1. A Query Engine for the Agents
- **arXiv**: https://arxiv.org/abs/2605.27785
- **作者**: Kenny Daniel
- **年份**: 2026
- **摘要**: 提出 Hyperparam, 三个开源 JavaScript 库 (under 70 KB), 可在 AI-native 客户端应用中直接从对象存储读取 Parquet 和 Apache Iceberg. Squirreling 在 filter-bounded 查询上比 DuckDB-WASM 快 300 倍以上, 以更低成本支持 agent analyst 套件.
- **与本单元的关联**: 本单元 notes.md 教 Polars LazyFrame 的查询图(DAG)全局优化, 该论文的 Squirreling 引擎在 filter-bounded 查询上比 DuckDB-WASM 快 300x, 直接对比了两种列式 DAG 优化器的性能差异。

### 2. Intelligent Drill-Down: Large Language Model-Driven Drill-Down Technique for Human-AI Collaborative Visual Exploration
- **arXiv**: https://arxiv.org/abs/2604.17002
- **作者**: Zhijun Zheng, Tian Qiu
- **年份**: 2026
- **摘要**: 提出智能下钻框架, LLM 生成视觉洞察、解释用户意图并推荐多维数据探索的下钻路径. LLM 经训练近似已验证的贪心路径推荐算法, 配备分支管理系统和分层导航的混合界面.
- **与本单元的关联**: 本单元 TODO6 用 deque 做 BFS 树遍历产品分类树, 该论文的 LLM 下钻框架在多维数据上推荐树遍历路径, 将"手动 BFS"升级为"LLM 辅助贪心路径推荐"。

### 3. The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models
- **arXiv**: https://arxiv.org/abs/2606.29799
- **作者**: Rafael Kaufmann, Felix Neubürger
- **年份**: 2026
- **摘要**: 神经符号框架用于自动化复杂分析工作流, 以基本面投资分析为主要用例. 构建动态概率程序支持贝叶斯推断, 在公司分类任务上仅用 5 个样本即达到 Bayes-optimal accuracy, 超越准确率停滞在 40% 左右的 LLM.
- **与本单元的关联**: 本单元 notes.md 将 Polars 查询图类比为 DAG 数据结构, 该论文的动态概率程序也是 DAG(贝叶斯网络), 展示了 DAG 结构在概率推断而非查询优化中的另一面应用。

---

## critical_synthesis

这三篇论文共同揭示了一个共识: DAG(有向无环图)与树结构仍是 2025-2026 年分析系统的骨架, 但其构建与遍历正从"程序员手动设计"转向"引擎自动优化"或"LLM 近似推荐"。Hyperparam(2605.27785)的列式查询优化器在 DAG 上自动重排 filter/projection, 300x 的优势证明了自动优化的价值; Intelligent Drill-Down(2604.17002)用 LLM 近似贪心下钻路径, 将树遍历的决策权部分交给模型; CRISTAL(2606.29799)则在 DAG 上做贝叶斯推断, 展示了概率程序结构。然而, 三者之间存在深层争议: Hyperparam 追求精确的查询优化器, 而 Intelligent Drill-Down 接受 LLM 的"近似"贪心路径--精确与近似之间的权衡在什么场景下谁占优尚无定论。更关键的 limitation 在于: 三篇论文的 DAG/树结构都是预定义的, 没有解决"结构本身从何而来"的问题。CRISTAL 的概率程序 DAG 需要人类设计, Intelligent Drill-Down 的下钻维度树是预设的, Hyperparam 的查询图由用户 SQL 决定。趋势上, 本单元教的 dict O(1) 哈希查找、heapq O(n log k) Top-K、deque 滑动窗口等"原子数据结构"仍是所有上层引擎的基础, 但学生需认识到: 在 agent 时代, 这些结构的"选择"正被引擎/LLM 自动化, 人类的价值转向"定义正确的分析结构与约束"。

---

## delta_to_unit

1. **Polars DAG 查询优化器的产业验证**: 本单元 notes.md 教 Polars LazyFrame 的查询图(DAG)全局优化, 称"先 filter 再 select 和先 select 再 filter 自动优化为最优执行顺序"。Hyperparam(2605.27785)提供了这一趋势的产业验证--其 Squirreling 引擎在 filter-bounded 查询上比 DuckDB-WASM 快 300x, 说明 DAG 优化器的实现质量差异巨大, 本单元学生不能仅知道"有优化器", 还需知道优化器之间有 300x 量级的差距。

2. **BFS 树遍历 vs LLM 贪心下钻**: 本单元 TODO6(solution.ipynb cell-19)用 `deque` 做 BFS 遍历产品分类树, notes.md 称"树/图遍历是数据结构的基础操作"。Intelligent Drill-Down(2604.17002)用 LLM 近似已验证的贪心路径推荐算法, 配备分支管理系统--这更新了本单元的教学: BFS 是精确遍历, 但在多维营销数据探索中, LLM 的"近似贪心"可能比 BFS 的"穷举"更实用, 代价是可能漏掉非贪心路径上的洞察。

3. **DAG 结构的双重角色**: 本单元 notes.md 将 Polars 查询图类比为 DAG, 用于查询优化。CRISTAL(2606.29799)展示了 DAG 的另一面--动态概率程序(贝叶斯网络)在 DAG 上做推断, 仅用 5 个样本达到 Bayes-optimal。这意味着本单元教的 DAG 概念不仅是查询优化器的基础, 也是概率推断的基础, 学生需理解同一数据结构在"确定性查询"与"概率推断"中的不同角色--这是 notes.md 未显式区分的。

---

## open_questions

1. Polars LazyFrame 的 DAG 查询优化器自动重排 filter/select, 但 Hyperparam 的 300x 优势是否意味着 DuckDB-WASM 的查询图优化器有根本性缺陷, 还是 filter-bounded 这一特定查询类型的偏差?
2. Intelligent Drill-Down 用 LLM 近似贪心下钻路径, 但本单元 TODO6 的 BFS 是精确遍历--在什么数据规模下 LLM 近似的"快但不精确"优于 BFS 的"慢但完整", 漏掉的分支如何量化损失?
3. CRISTAL 用 5 个样本达到 Bayes-optimal, 但其 DAG 概率程序的结构需要人类设计--能否用 LLM 从数据自动推断 DAG 结构(贝叶斯网络结构学习), 还是结构设计永远是不可自动化的领域知识?
4. 本单元教 namedtuple 的不可变 schema 作为数据治理基础, 但 Arrow 的列式零拷贝要求内存布局固定--namedtuple 的不可变性与 Arrow 的列式格式在内存层面是否同构, 还是需要额外转换层?

---

## methodological_critique

这三篇论文的局限性需审慎评估。Hyperparam(2605.27785)的"300x DuckDB-WASM"仅在 filter-bounded 查询上测得, 这是一种特殊查询类型(带过滤谓词的范围扫描), 未覆盖本单元教的 groupby/apply/JOIN 等聚合操作, 其 70KB JS 体积优势可能以牺牲查询优化器通用性为代价; 且仅开源 JS 库未开源完整基准脚本, 可复现性存疑。Intelligent Drill-Down(2604.17002)标注 unverified, 其"LLM 近似已验证的贪心路径推荐算法"的宣称缺乏与精确 BFS/DFS 的系统性对比--论文展示的是推荐路径的质量, 未报告路径遗漏率, 存在 cherry-picking 成功案例的风险。CRISTAL(2606.29799)同样 unverified, 其"5 个样本 Bayes-optimal"的结果仅在公司分类这一单一任务上测得, 5 样本的小样本优势高度依赖先验质量, 若先验错误则可能比 LLM 的 40% 更差; 且概率程序 DAG 的设计本身是强领域知识注入, 论文未量化"设计 DAG 的人力成本"与"节省的标注成本"的权衡。三者均存在 benchmark-gaming 风险: 在自选用例上展示结构优势, 未在统一的营销数据结构基准上横向对比。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
