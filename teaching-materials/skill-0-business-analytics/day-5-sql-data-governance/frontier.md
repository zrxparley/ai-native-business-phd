# frontier.md

> **所属**：skill-0-business-analytics · day-5-sql-data-governance
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 agent 直读 Iceberg/Parquet 对象存储、LLM 将信息需求具体化为关系规范、多 agent 分离计算与解读如何更新本单元"Schema 设计->SQL 查询->数据质量审计"的治理链路。

---

## frontier_topic

本单元教 sqlite3 六表 Schema 设计(customers/products/categories/orders/order_items/campaigns, 1NF/2NF/3NF)、SQL DQL(JOIN/GROUP BY/窗口函数/CTE/RFM 子查询)、数据治理六维度(DAMA-DMBOK)、Apache Iceberg 湖仓一体(ACID/time-travel/schema-evolution)、Great Expectations 数据质量监控。前沿子问题是: 当 agent 能直接从对象存储读 Iceberg/Parquet、LLM 将信息需求自动具体化为关系规范、多 agent 分离计算脚本生成与结果解读时, 本单元"人工设计 Schema->手写 SQL->约束审计"的治理链路如何被重构。

---

## recent_papers

### 1. A Query Engine for the Agents
- **arXiv**: https://arxiv.org/abs/2605.27785
- **作者**: Kenny Daniel
- **年份**: 2026
- **摘要**: 提出 Hyperparam, 三个开源 JavaScript 库 (under 70 KB), 可在 AI-native 客户端应用中直接从对象存储读取 Parquet 和 Apache Iceberg. Squirreling 在 filter-bounded 查询上比 DuckDB-WASM 快 300 倍以上, 以更低成本支持 agent analyst 套件.
- **与本单元的关联**: 本单元 notes.md 教 Apache Iceberg 的 ACID 事务与 schema 演化, 该论文的 Hyperparam 让 agent 直读 Iceberg/Parquet 对象存储, 300x DuckDB-WASM, 是本单元"Iceberg 湖仓一体"前沿补充的 agent-native 落地。

### 2. Demonstration of Pneuma-Seeker: Agentic System for Reifying and Fulfilling Information Needs on Tabular Data
- **arXiv**: https://arxiv.org/abs/2604.14422
- **作者**: Muhammad Imam Luthfi Balaka, Raul Castro Fernandez
- **年份**: 2026
- **摘要**: 演示 Pneuma-Seeker 系统, 将用户信息需求具体化为可检视的关系规范 (relational specifications), 支持迭代精化. 通过两个采购用例, 将 LLM 作为透明、交互式的分析协作者而非黑盒答案引擎.
- **与本单元的关联**: 本单元 TODO1 用 sqlite3 CREATE TABLE 手动设计 Schema, 该论文将"我想要某客户买了什么产品"这类需求自动具体化为关系规范(SQL 级别的可检视规范), 挑战了人工 Schema 设计与 SQL 编写的必要性。

### 3. PMAx: An Agentic Framework for AI-Driven Process Mining
- **arXiv**: https://arxiv.org/abs/2603.15351
- **作者**: Anton Antonov, Humam Kourani
- **年份**: 2026
- **摘要**: 自主 agentic 框架, 作为虚拟流程分析师运行, 采用隐私保护多 agent 架构. Engineer agent 生成本地脚本运行流程挖掘算法, Analyst agent 解读结果, 通过分离计算与解读确保数学准确性与数据隐私.
- **与本单元的关联**: 本单元 TODO6 教数据治理实操(约束/索引/缺失值/数据质量六维度), 该论文的 Engineer/Analyst 双 agent 分离(计算脚本生成 vs 结果解读)对应本单元"数据查询(计算)与数据治理审计(解读)"的职责分离。

---

## critical_synthesis

这三篇论文共同揭示了一个正在形成的共识: 数据治理链路正从"人工设计 Schema->手写 SQL->人工审计"走向"agent 直读列式存储->LLM 自动具体化关系规范->多 agent 分离计算与解读"。Hyperparam(2605.27785)解决了 agent 直读 Iceberg/Parquet 的工程瓶颈, Pneuma-Seeker(2604.14422)解决了信息需求到关系规范的自动生成, PMAx(2603.15351)解决了计算与解读的职责分离。然而三者之间存在明显争议: Hyperparam 主张查询引擎下沉到客户端(70KB JS), Pneuma-Seeker 仍依赖服务端 LLM 迭代精化, PMAx 则用多 agent 架构在服务端分离职责--三种架构路径(客户端轻量/服务端 LLM/多 agent)尚无定论。更关键的 limitation: Hyperparam 的"300x DuckDB-WASM"仅在 filter-bounded 查询上测得, 未覆盖本单元教的 JOIN/GROUP BY/窗口函数等复杂 DQL; Pneuma-Seeker 仅用两个采购用例, 其"关系规范"能否表达窗口函数+CTE 的复杂 RFM 子查询存疑; PMAx 的"隐私保护"宣称缺乏对抗性评估, Engineer 生成的本地脚本是否泄露数据模式未验证。趋势上, 本单元教的 1NF/2NF/3NF 范式化与 sqlite3 约束(PK/FK/CHECK)仍是数据治理的基础, 但 Iceberg schema evolution 与 agent 自动化正在改变"何时范式化"的决策--在 schema 可演化的湖仓中, 适度反范式化的代价降低了。

---

## delta_to_unit

1. **Apache Iceberg 的 agent-native 落地**: 本单元 notes.md 教 Apache Iceberg 的 ACID 事务、time-travel、schema evolution, 称"Snowflake/Databricks/Trino/Spark 均已支持 Iceberg"。Hyperparam(2605.27785)将这一趋势推到 agent 层--70KB JS 库让 agent 直读 Iceberg/Parquet, filter-bounded 查询比 DuckDB-WASM 快 300x。这意味着本单元教的 `sqlite3.connect()` + `cursor.execute()` 在 agent-native 湖仓架构中可能被客户端直读取代, 但 sqlite3 的 CHECK/NOT NULL/UNIQUE 约束在 Parquet 中无等价物, 数据完整性保障需迁移到 schema 层。

2. **Schema 设计的自动化边界**: 本单元 TODO1(solution.ipynb)用 `CREATE TABLE customers(...PRIMARY KEY...FOREIGN KEY...)` 手动设计六表 Schema, notes.md 教 1NF/2NF/3NF 范式化评估。Pneuma-Seeker(2604.14422)将信息需求自动具体化为关系规范--但"关系规范"是否等价于范式化的 Schema 存疑, Pneuma-Seeker 的两个采购用例未展示复杂 JOIN/窗口函数的规范生成。这更新了本单元的教学重心: 从"手写 CREATE TABLE"转向"定义可检视的分析规范并验证其范式化质量"。

3. **数据治理的职责分离**: 本单元 TODO6 教"主键外键/索引/缺失值/数据质量六维度检查"一站式审计, notes.md 的 DAMA-DMBOK 六维度是单一分析师职责。PMAx(2603.15351)的 Engineer/Analyst 双 agent 分离(生成计算脚本 vs 解读结果)提供了一个新范式: 数据治理审计可拆分为"计算准确性(Engineer 生成本地脚本验证约束)"与"解读隐私(Analyst 评估数据泄露风险)"两个独立职责。这更新了本单元的教学: 数据治理不必是单人全栈, 可拆分为计算层与解读层, 但拆分引入了 agent 间通信的可治理性新问题。

---

## open_questions

1. Hyperparam 在客户端直读 Iceberg 300x DuckDB-WASM, 但本单元教的 sqlite3 CHECK/NOT NULL/UNIQUE 约束在 Parquet 列式格式中如何执行--是 Iceberg schema 层强制还是仍需查询层运行时检查, 约束缺失是否使 3NF 范式化失效?
2. Pneuma-Seeker 将信息需求自动具体化为关系规范, 但本单元 TODO5 的窗口函数(RANK/累计求和)+CTE+RFM 子查询是复杂 SQL--LLM 能否生成等价的窗口函数, 还是退化为多步简单查询(性能与可读性的权衡)?
3. PMAx 分离 Engineer(生成本地脚本)与 Analyst(解读结果), 但本单元教的 `pandas.read_sql()` 打通 SQL 与 Python 是单链路--agent 分离架构在数据治理上是否比单链路更可审计(两份日志 vs 一份)?
4. 本单元教 1NF/2NF/3NF 范式化原则, 但 Iceberg 的 schema evolution 支持无痛增删列--在 schema 可频繁演化的湖仓中, 范式化的迁移成本是否使其变得不必要, 适度反范式化是否成为新常态?

---

## methodological_critique

这三篇论文的局限性需审慎对待。Hyperparam(2605.27785)的"300x DuckDB-WASM"仅在 filter-bounded 查询(带过滤谓词的范围扫描)上测得, 未覆盖本单元教的 JOIN/GROUP BY/窗口函数等聚合 DQL, 其 70KB JS 体积优势可能以牺牲查询优化器通用性为代价; 且仅开源 JS 库未开源完整基准脚本, 可复现性存疑, "under 70 KB"的宣称可能排除了依赖项。Pneuma-Seeker(2604.14422)虽标注 verified, 但仅用两个采购用例演示, 样本量极小; 其"关系规范"的表达能力未与 SQL 标准对比--能否表达窗口函数、递归 CTE、物化视图等复杂 DQL 未验证; "透明协作者"的宣称缺乏对抗性评估, 若用户需求含歧义, 迭代精化是否收敛无证明。PMAx(2603.15351)标注 unverified, 其"隐私保护多 agent 架构"的宣称缺乏正式的安全分析, Engineer 生成的本地脚本可能通过侧信道(脚本结构/执行时间)泄露数据模式; "分离计算与解读确保数学准确性"的结论未与单 agent 基线在相同任务上对比, 存在 weak baseline 风险。三者均存在 domain-specific benchmark-gaming 风险: 在自选用例上展示治理优势, 未在统一的数据治理基准(如 DAMA-DMBOK 审计清单)上验证。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
