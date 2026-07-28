# 技能0 · Day 5：数据治理与 SQL · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能0 AI商业分析基础（预科层）· Day 5
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：企业数据资产如何管理？--从关系型数据库 Schema 设计到 SQL 查询与数据治理的完整闭环
> **v5.0 升级点**：① 真实库上机（sqlite3 + pandas.read_sql，替代纯理论讲解）② TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（DAMA-DMBOK 数据治理框架 / Apache Iceberg 表格式 / 湖仓一体 / 数据质量监控）

---

## 学习目标（学完你能做到）

1. 能解释数据治理（Data Governance）的六个核心维度（数据质量、元数据管理、数据架构、数据安全与隐私、数据生命周期、数据标准与主数据管理），并说明为什么 AI 系统的质量取决于数据质量（"Garbage In, Garbage Out"），在营销 AI 场景中识别常见数据质量问题（客户信息重复、手机号格式不统一、消费金额缺失、数据更新不及时）
2. 能用 **sqlite3**（Python 内置库）创建电商企业营销数据库 Schema（customers/products/categories/orders/order_items/campaigns 六表），理解主键（PRIMARY KEY）、外键（FOREIGN KEY）、CHECK 约束、DEFAULT 值、GENERATED 列的设计原理，并用范式化（1NF/2NF/3NF）原则评估 Schema 质量
3. 能用 **SQL DQL**（SELECT/WHERE/JOIN/GROUP BY/HAVING/窗口函数/子查询）完成营销数据分析任务，包括按品类/渠道/月份聚合销量 GMV、多表连接查询"某客户买了什么产品"、RANK 排名热销商品、RFM 客户分群子查询，并用 `pandas.read_sql()` 将查询结果转为 DataFrame 做进一步分析
4. 能执行数据治理实操：创建索引（INDEX）提升查询性能、用约束（CHECK/NOT NULL/UNIQUE）保障数据完整性、检测缺失值与重复记录、评估数据质量六维度（准确性/完整性/一致性/及时性/唯一性/有效性），理解数据仓库 vs 数据湖 vs 湖仓一体的选型差异
5. 能解释 GDPR（欧盟通用数据保护条例）、中国数据安全法、个人信息保护法对企业营销数据处理的影响，理解 Privacy by Design 原则，并在数据库 Schema 设计中嵌入合规要求

---

## 理论部分：精炼索引（详见独立教材）

> Day 5 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md` § Day 5](../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md)（997-1357 行，已包含数据治理六维度/关系型数据库与SQL/范式化/数据仓库vs数据湖vs湖仓一体/数据隐私合规/电商企业数据库Schema设计完整案例/英语轨道说明）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：数据治理 -- 企业数据资产的管理框架

数据治理（Data Governance）是 AI 时代数据资产管理的制度基础。DAMA International（Data Management Association）在 DAMA-DMBOK 中定义了数据治理的六个核心维度：

| 维度 | 核心内容 | 营销场景示例 |
|------|---------|------------|
| 数据质量 | 准确性/完整性/一致性/及时性/唯一性/有效性 | 客户信息重复录入、手机号格式不统一、消费金额缺失 |
| 元数据管理 | 数据字典/业务术语表/数据血缘 | "这个字段是什么意思、从哪来、被谁用" |
| 数据架构 | 数据仓库/数据湖/湖仓一体选型 | 结构化订单存仓库，非结构化客服对话存湖泊 |
| 数据安全与隐私 | GDPR/数据安全法/个保法 | 用户画像、行为追踪、个性化推荐的合规边界 |
| 数据生命周期 | 创建/存储/使用/归档/销毁 | 营销活动数据的保留期限与销毁策略 |
| 数据标准与主数据 | 统一数据定义/单一真相源 | 客户ID跨系统统一、产品编码标准化 |

**AI 时代的核心命题**：AI 系统的输入是数据，如果数据质量差，AI 的输出就会不可靠。NIST AI RMF 框架中的"Map"步骤就要求企业识别 AI 系统的数据来源和质量。数据治理不是可选项，是 AI 可靠性的前提。

### 关键回顾 2：关系型数据库与 SQL 四类操作

| 操作类型 | 缩写 | 关键语句 | 营销场景 |
|---------|------|---------|---------|
| 数据定义语言 | DDL | CREATE TABLE / ALTER TABLE / DROP TABLE | 设计营销数据库 Schema |
| 数据操作语言 | DML | INSERT / UPDATE / DELETE | 插入客户/订单/商品数据 |
| 数据查询语言 | DQL | SELECT | 分析销量/GMV/客户分群（最常用） |
| 数据控制语言 | DCL | GRANT / REVOKE | 控制营销团队的数据访问权限 |

### 关键回顾 3：数据库范式化（Normalization）

| 范式 | 要求 | 营销示例 |
|------|------|---------|
| 第一范式 1NF | 每个字段不可再分 | 订单不能把"商品列表"塞进一个字段 |
| 第二范式 2NF | 非主键字段完全依赖主键 | 订单明细中的商品名应关联到商品表，不冗余存于订单 |
| 第三范式 3NF | 非主键字段直接依赖主键 | 客户等级不冗余存于订单表，通过客户ID关联 |

实际企业中常做适度反范式化（Denormalization），在范式和查询性能间取平衡。

### 关键回顾 4：数据仓库 vs 数据湖 vs 湖仓一体

| 维度 | 数据仓库 | 数据湖 | 湖仓一体 |
|------|---------|--------|---------|
| 数据类型 | 结构化 | 结构化+非结构化 | 结构化+非结构化 |
| 处理方式 | 写时模式 Schema-on-Write | 读时模式 Schema-on-Read | 两者兼有 |
| 典型工具 | Snowflake, Redshift, BigQuery | S3, HDFS | Databricks, Delta Lake, Apache Iceberg |
| 适用场景 | BI报表、分析查询 | 数据探索、ML训练 | 统一分析和ML |

在 AI 营销场景中：结构化的客户/订单数据存数据仓库，非结构化的客服对话/广告素材/用户评论存数据湖，湖仓一体提供统一的数据底座。

---

## 上机部分：用真实库构建电商营销数据库

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（sqlite3 + pandas.read_sql + 电商数据库Schema）

### 为什么用真实库而非纯理论讲解

v4.0 的代码用伪代码演示 SQL 概念。v5.0 改用 Python 内置的真实数据库引擎：

- **sqlite3**（Python 标准库，无需安装）：`sqlite3.connect()` / `cursor.execute()` / `conn.commit()` -- 轻量级关系型数据库引擎，Python 内置，零安装即可运行完整的 SQL DDL/DML/DQL
- **pandas.read_sql**（pandas-dev/pandas，43k+ star）：`pd.read_sql_query(sql, conn)` -- 将 SQL 查询结果直接转为 DataFrame，打通 SQL 与 Python 数据分析的闭环

### 营销映射（关键桥接）

本 Day 处理一个"电商企业营销数据库"场景：6张表（类目/客户/商品/订单/订单明细/营销活动），用 SQL 完成从 Schema 设计到营销分析的完整闭环：

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| 建库建表 | 设计电商营销数据库 Schema | sqlite3 CREATE TABLE + 约束 |
| 基础查询 | 按品类/价格/时间筛选产品订单 | SELECT-WHERE-ORDER BY |
| 多表连接 | 查"某客户买了什么产品" | JOIN（INNER/LEFT） |
| 聚合分析 | 按品类/月份聚合销量GMV，找TOP品类 | GROUP BY-HAVING |
| 窗口函数 | RANK排名/累计求和/RFM子查询 | 窗口函数 + CTE + 子查询 |
| 数据治理 | 主键外键/索引/缺失值/数据质量检查 | 约束/INDEX/数据质量审计 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 sqlite3 创建电商营销数据库 Schema（customers/products/categories/orders/order_items/campaigns 六表），插入营销数据（200客户/50商品/500订单/营销活动）
2. **TODO2**：用 SELECT-WHERE-ORDER BY 按品类/价格/时间筛选产品和订单
3. **TODO3**：用 JOIN 多表连接查询"某客户买了什么产品"，关联订单-客户-商品三表
4. **TODO4**：用 GROUP BY-HAVING 按品类/月份聚合销量 GMV，找 TOP 品类和渠道
5. **TODO5**：用窗口函数（RANK/累计求和）和子查询实现 RFM 客户分群分析
6. **TODO6**：数据治理实操--主键外键约束/索引创建/缺失值检测/数据质量六维度检查/范式化评估

---

## 2026 前沿补充：DAMA-DMBOK + Apache Iceberg + 湖仓一体

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① DAMA-DMBOK 数据治理框架 ② Apache Iceberg 开放表格式 ③ 数据质量监控与湖仓一体。

### DAMA-DMBOK：数据治理的国际标准框架

DAMA International（Data Management Association）发布的 **DAMA-DMBOK**（Data Management Body of Knowledge）是数据治理领域的国际标准参考框架。DMBOK 定义了数据管理的 11 个知识领域，数据治理是其中的核心--它为其他 10 个领域（数据架构、数据建模、数据存储、数据安全、数据集成、文档与内容、参考数据与主数据、数据仓库与BI、元数据、数据质量）提供统筹和协调。

**对营销 AI 的启示**：在构建 AI 营销系统时，DAMA-DMBOK 提供了系统化的数据治理 checklist--从数据架构设计（Schema 规范化）到数据质量监控（六维度审计）到元数据管理（数据字典维护），每个环节都有明确的标准和最佳实践。这正是 AI 系统可靠性的制度保障。

### Apache Iceberg：开放表格式与湖仓一体的基石

**Apache Iceberg**（apache/iceberg，Apache-2.0）是开放表格式（Open Table Format）的代表，正在重塑数据湖架构：

- **ACID 事务**：为数据湖提供事务保证，解决传统数据湖"最终一致"导致的数据质量问题
- **时间旅行（Time Travel）**：支持查询历史版本数据，对营销数据的版本审计和回溯分析至关重要
- **Schema 演化**：支持无痛增删列，不需要重写整个表--对频繁变化的营销数据模型极为友好
- **分区演化**：自动管理分区策略，查询时自动裁剪分区，提升性能

**与 Day 5 SQL 的关系**：Apache Iceberg 让数据湖具备数据仓库的 ACID 和 Schema 管理能力，是"湖仓一体"的技术基石。Snowflake、Databricks、Trino、Spark 等主流引擎均已支持 Iceberg。在 AI 营销场景中，Iceberg 让你可以在同一份数据上同时做 BI 报表和 ML 训练，无需数据搬运。

### 数据质量监控与可观测性

数据质量监控（Data Quality Monitoring）是数据治理的执行层。前沿工具如 **Great Expectations**（great-expectations/great_expectations，9k+ star）和 **Soda Core** 提供声明式数据质量检查：

- **期望（Expectations）**：用 Python/SQL 声明数据质量规则（如"customer_id 必须唯一""price 必须 > 0"）
- **自动化测试**：每次数据入库时自动运行质量检查，失败则阻断流水线
- **数据可观测性**：监控数据分布漂移、体量异常、Schema 变更，提前预警

**营销场景**：当营销数据从 CRM 流入数据仓库时，Great Expectations 可以自动检查"手机号格式是否统一""消费金额是否为正""客户ID是否跨系统一致"，将数据治理从"事后审计"升级为"事前预防"。

> ⚠️ 数据治理不是一次性的项目，而是持续运营。在后续技能中，你将学习如何用 AI 自动化数据质量检查（如用 LLM 识别数据异常、用 embedding 做实体对齐）。

---

## 与后续 Day 的衔接

- **Day 1-4**：Python 基础/数据结构/统计/回归 -- 今天的 SQL 查询结果可以用 pandas 加载，用统计方法分析
- **Day 6**：研究方法论入门 -- 今天的数据治理原则（可复现性、数据质量）是学术研究方法的基础
- **技能1**：营销 AI Agent -- 今天的数据库 Schema 将扩展为知识图谱（Neo4j）和向量数据库
- **技能2**：RAG 知识引擎 -- 今天的数据质量治理原则直接适用于 RAG 的知识库管理

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 5 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的电商营销数据库 Schema 设计遵循了哪些范式化原则？RFM 分群后各层级客户的消费特征有何差异？数据质量检查发现了哪些问题？
- [ ] （可选）将本 Day 的电商数据库 Schema 扩展为支持"营销活动效果分析"的完整 Schema（增加广告投放表、渠道归因表），并写出 3 个业务分析 SQL 查询

---

## 英语轨道（i+1）

打开 [Kaggle Learn: SQL](https://www.kaggle.com/learn/sql)，完成互动式 SQL 练习。SQL 是通用语言，代码部分没有语言障碍。阅读英文解释时，关注 JOIN, GROUP BY, subquery, window function, CTE (Common Table Expression) 等术语。完成全部练习大约需要 2 小时。这就是 i+1：你已有中文 SQL 基础（i），通过英文互动教程接触新表达方式（i+1）。

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（sqlite3 + pandas.read_sql）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 升级: 在 v5.0 真实库上机基础上, 注入学习科学四件套 - 刻意练习 (deliberate practice, Ericsson) / 间隔重复 (spaced retrieval, FSRS-6 + SM-2 backup) / 建构对齐 (constructive alignment, Biggs ILO↔TLA↔AT) / 牛津tutorial Socratic 仿真 (Hattie 四级形成性反馈 formative feedback).

### 1. 刻意练习 (Ericsson + MIT Worked-Faded)
本单元 3 个 drill (Schema 设计 / DQL 查询 / 数据治理审计) 各含 difficulty / reps_required / feedback_rule, 采用 Worked-Faded 三阶段 (完整示范 -> 部分填空 -> 独立解, 渐退式脚手架). 连续 2 次失败触发 weak_loop - 回退上一 drill + 补充 worked example. A1B1C1 交叉 interleaving 排布 (不块状).

### 2. 间隔重复 (FSRS-6 / SM-2)
4 张 card (数据治理六维度 / sqlite3 约束四件套 / RFM 52/49/31/45 / 数据仓库vs数据湖vs湖仓一体) 按 FSRS-6 间隔 [1, 3, 8, 21, 60, 180] 天复习, request_retention=0.9, EF₀=2.5 (SM-2 备份). 强制 retrieval practice (提取练习) - Butler 2010 证据: 检索 68% vs 重学 44%.

### 3. 建构对齐 (Biggs ILO↔TLA↔AT)
4 行矩阵对齐 ILO/TLA/AT + mastery_threshold (掌握阈值), 3 自检 (Feed Up: TLA 训练 ILO? Feed Back: AT 测量 ILO? Feed Forward: 不经 TLA 能过 AT?). 不经 worked-faded 不能过 milestone.

### 4. 牛津tutorial Socratic 仿真 (Hattie 四级)
Oxford tutorial fellow persona, 禁直接答案, 4+ 轮 Socratic 追问 (为什么 / 若 / 反例 / 凭什么 / 假设变). Hattie 四级反馈 [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD] - 避免 Self 级表扬. student_model.json 跨单元复用. 限频 1次/天 防依赖.

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM-as-data-analyst × Polars/duckdb 列式引擎。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 sqlite3 + pandas.read_sql（SQL DQL）形成对照。
> - **从零构建主题**：手写关系代数 select/project/join + 数据质量度量
> - **核心算法**：关系代数 $\sigma_\theta(R) \cdot \pi_L(R) \cdot R \bowtie S$ + 数据质量距离度量（含数学推导 + LaTeX）
> - **code_artifact**：手写 collections 骨架，imports ⊆ {collections}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P0/09 Data Management + P1/14 Norms and Distances
> - **手写实现要点**：用 from-scratch list-of-dicts + defaultdict 而非 sqlite3，理解到金属层
> - **verification_property**：select 筛选正确；project 去重；hash_join 匹配嵌套循环；聚合金额正确
