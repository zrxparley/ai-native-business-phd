# frontier.md

> **所属**：skill-0-business-analytics · day-1-python-fundamentals
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 LLM-as-data-analyst 工作流与列式查询引擎(DuckDB-WASM/Parquet 直读对象存储)如何重构"从原始数据到营销指标"的加载-探索-计算链路。

---

## frontier_topic

本单元教 pandas DataFrame 加载营销数据、dtype 治理(客户ID 前导零)、RFM apply 向量化分类、Product/Customer 面向对象设计、ROI/AOV/复购率指标计算，并前瞻 pandas 2.x Arrow 后端与 Polars LazyFrame。前沿子问题是: 当 LLM-as-data-analyst 能直接从对象存储读取 Parquet/Iceberg 并迭代精化分析意图时, 本单元所教的"pandas 手动加载→dtype 检查→apply 分类→聚合指标"链路中, 哪些环节被自动化、哪些环节仍是不可替代的人类判断。

---

## recent_papers

### 1. A Query Engine for the Agents
- **arXiv**: https://arxiv.org/abs/2605.27785
- **作者**: Kenny Daniel
- **年份**: 2026
- **摘要**: 提出 Hyperparam, 三个开源 JavaScript 库 (under 70 KB), 可在 AI-native 客户端应用中直接从对象存储读取 Parquet 和 Apache Iceberg. Squirreling 在 filter-bounded 查询上比 DuckDB-WASM 快 300 倍以上, 以更低成本支持 agent analyst 套件.
- **与本单元的关联**: 本单元 solution.ipynb 用 pandas `pd.DataFrame(dict)` 从内存字典加载, 该论文展示 agent 直读 Parquet/Iceberg 列式格式, 对应本单元 notes.md "pandas 2.x Arrow 后端"前沿补充的产业落地。

### 2. Demonstration of Pneuma-Seeker: Agentic System for Reifying and Fulfilling Information Needs on Tabular Data
- **arXiv**: https://arxiv.org/abs/2604.14422
- **作者**: Muhammad Imam Luthfi Balaka, Raul Castro Fernandez
- **年份**: 2026
- **摘要**: 演示 Pneuma-Seeker 系统, 将用户信息需求具体化为可检视的关系规范 (relational specifications), 支持迭代精化. 通过两个采购用例, 将 LLM 作为透明、交互式的分析协作者而非黑盒答案引擎.
- **与本单元的关联**: 本单元 TODO3 用 `apply` 手动实现 RFM 分类逻辑, 该论文的 LLM 将"我想要高价值客户"这类信息需求自动具体化为关系规范, 挑战了手动 apply 分类的必要性。

### 3. AI Coding Agents in Social Science: Methodologically Diverse, Empirically Consistent, Interpretively Vulnerable
- **arXiv**: https://arxiv.org/abs/2606.11456
- **作者**: Meysam Alizadeh, Fabrizio Gilardi
- **年份**: 2026
- **摘要**: 在移民/社会政策研究的 many-analysts 人类基线上测试 LLM 编码 agent (Claude Code, Codex). 在设计层 agent 匹配或超越人类方法论多样性; 在裁决层, 显式确认性提示将 Claude Code 的裁决从 10% 翻转至 90% 支持, 揭示解释层为 AI 偏见所在.
- **与本单元的关联**: 本单元教 Python+pandas 数据处理代码, 该论文测试的 Claude Code 正是自动生成这类代码的 agent, 其"设计层强、裁决层脆弱"的发现直接影响本单元"apply 向量化 vs for 循环"等代码决策的可委托性。

---

## critical_synthesis

这三篇论文共同揭示了一个正在形成的共识: LLM-as-data-analyst 不再是"生成一段 SQL/Python 就结束"的代码生成器, 而是嵌入数据加载-意图精化-结果解读全链路的协作者。Hyperparam(2605.27785)解决了 agent 直读列式存储的工程瓶颈, Pneuma-Seeker(2604.14422)解决了意图到关系规范的自动具体化, AI Coding Agents(2606.11456)则揭示了 agent 在"写代码"层可靠但在"判断结果含义"层存在可被提示词翻转的系统性偏见。然而三者之间存在明显争议: Hyperparam 主张将查询引擎下沉到客户端(70KB JS 库), 而 Pneuma-Seeker 仍依赖服务端 LLM 迭代精化——两种架构路径尚无定论。更关键的局限在于: 三篇论文均未在百万行级真实营销数据上验证, Pneuma-Seeker 仅用两个采购用例, AI Coding Agents 的 many-analysts 基线限于社会政策文本编码而非结构化营销指标计算。趋势上, 列式引擎(Parquet/Iceberg)+LLM 协作正在取代"pandas 手动加载 CSV"的旧范式, 但本单元所教的 dtype 治理(前导零)、RFM 业务逻辑阈值定义、指标口径(ROI/AOV)仍是 agent 无法自动化的领域知识, 这正是 limitation 所在。

---

## delta_to_unit

1. **数据加载环节的更新**: 本单元 solution.ipynb cell-6 用 `pd.DataFrame(dict)` 从内存字典加载, notes.md 前沿补充提到 pandas 2.x Arrow 后端零拷贝交换可省 30-50% 内存。Hyperparam(2605.27785)将这一趋势推到极致——agent 直接从对象存储读 Parquet/Iceberg, 跳过 pandas 加载步骤, 在 filter-bounded 查询上比 DuckDB-WASM 快 300x。这意味着本单元教的 `pd.read_csv()`/`pd.DataFrame()` 在 agent-native 工作流中可能沦为中间过渡层。

2. **RFM 分类逻辑的自动化边界**: 本单元 TODO3 用 `classify_customer(row)` 函数 + `rfm.apply(classify_customer, axis=1)` 手动实现 R≤30/F≥3/M≥¥1000 的高价值客户规则。Pneuma-Seeker(2604.14422)表明 LLM 能将"我想要高价值客户"自动具体化为关系规范并迭代精化。但本单元的 RFM 阈值(R≤30天、M≥¥1000)是业务领域知识, Pneuma-Seeker 的透明规范仍需人类定义阈值——这更新了本单元的教学重心: 从"写 apply 代码"转向"定义可检视的分析规范"。

3. **代码生成的可委托性与偏见**: 本单元 notes.md 强调"apply 比 for 循环快 10-100 倍"的向量化原理。AI Coding Agents(2606.11456)发现 Claude Code 在设计层(写 apply 代码)匹配甚至超越人类方法论多样性, 但在裁决层(判断结果是否支持假设)会被确认性提示从 10% 翻转到 90%。这意味着本单元学生不能仅学"怎么写 apply", 还须学"怎么批判性审查 agent 生成的 apply 代码及其结论"——这是本单元 notes.md 未覆盖的更新。

---

## open_questions

1. 当 Hyperparam 式列式直读(300x DuckDB-WASM)普及后, pandas DataFrame 作为"中间内存格式"的角色是否会被 Arrow 零拷贝直接取代, 本单元教的 `pd.read_csv`/`df.describe` API 还有教学价值吗?
2. Pneuma-Seeker 将信息需求具体化为"可检视的关系规范", 但本单元 RFM 的阈值(R≤30/F≥3/M≥¥1000)本身是经验性的营销领域知识——LLM 能否从历史数据自动推断这些阈值, 还是永远依赖人类先验?
3. AI Coding Agents 发现确认性提示可翻转裁决(10%→90%), 那么在营销 ROI 计算场景中, 如果分析师用 LLM 生成指标代码并附带"预期实验组更优"的提示, 会在多大程度上系统性扭曲营销决策?
4. Hyperparam 的 70KB JS 库在客户端直读 Parquet, 但本单元强调的客户ID前导零(dtype 治理)问题在 Parquet 列式格式中如何保证——是 schema 层面强制还是仍需运行时检查?

---

## methodological_critique

这三篇论文的局限性需谨慎对待。Hyperparam(2605.27785)的"300x DuckDB-WASM"仅在 filter-bounded 查询上测得, 未覆盖本单元 groupby/apply 等聚合操作, 其 70KB 体积优势可能以牺牲查询优化器复杂度为代价, 可复现性存疑(未开源完整基准脚本)。Pneuma-Seeker(2604.14422)仅用两个采购用例演示, 样本量极小, "透明协作者"的宣称缺乏对抗性评估——若用户信息需求本身含歧义, 系统的迭代精化是否收敛无证明。AI Coding Agents(2606.11456)的 many-analysts 基线是社会科学文本编码而非结构化营销数据, 其"设计层匹配人类"的结论不能直接外推到本单元的 pandas/RFM 场景; 更严重的是, 10%→90% 的裁决翻转虽揭示了偏见, 但该实验仅用单一主题(移民政策), 未测试营销决策中的效应量方向性偏见。三者均存在 benchmark-gaming 风险: 在自选用例上展示优势, 未在统一的营销分析基准上横向对比。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
