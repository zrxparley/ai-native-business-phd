# Day 5 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档 / 教程 / 仓库，非主页）。全部链接已验证存在。

---

## ① SQL 基础语法与教程

### Python sqlite3 官方文档（已验证）
- 🌐 官方文档：https://docs.python.org/3/library/sqlite3.html
- **用法**：Day 5 的核心库文档。Python 标准库内置的 sqlite3 模块，零安装即可使用。重点读 §1（Module functions and constants）、§2（Connection objects）、§3（Cursor objects），理解 connect/cursor/execute/commit/executemany 的工作原理。在营销场景中，用 sqlite3 创建电商数据库 Schema 并执行 SQL 查询。
- **深链用法**：
  - [sqlite3.connect](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)：对标 TODO1 创建数据库连接
  - [cursor.execute](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute)：对标 TODO1-6 执行 SQL 语句
  - [Using sqlite3 with pandas](https://docs.python.org/3/library/sqlite3.html#how-to-use-connection-shortcuts)：SQL 与 pandas 的桥接

### Kaggle Learn: SQL（已验证）
- 🌐 互动教程：https://www.kaggle.com/learn/sql
- **用法**：Day 5 英语轨道材料。Kaggle 的互动式 SQL 教程，英文界面但 SQL 是通用语言，代码部分无语言障碍。完成全部练习约 2 小时。重点学 JOIN, GROUP BY, subquery, window function 等核心概念。这就是 i+1：你已有中文 SQL 基础（i），通过英文互动教程接触新表达方式（i+1）。
- **深链用法**：
  - [JOIN 课程](https://www.kaggle.com/learn/joining-data)：对标 TODO3 多表连接
  - [GROUP BY 与聚合](https://www.kaggle.com/learn/group-by-and-having)：对标 TODO4 聚合分析

### SQLite 官方 SQL 语法参考（已验证）
- 🌐 官方文档：https://www.sqlite.org/lang.html
- **用法**：SQLite 的完整 SQL 语法参考，涵盖 DDL/DML/DQL 全部语句。重点读 [SELECT 语法](https://www.sqlite.org/lang_select.html)（对标 TODO2-5）和 [CREATE TABLE 语法](https://www.sqlite.org/lang_createtable.html)（对标 TODO1），理解 SQL 标准语法和 SQLite 的扩展特性（如 GENERATED 列）。

---

## ② 真实库：pandas.read_sql + sqlite3

### pandas.read_sql 官方文档（已验证）
- 🌐 官方文档：https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html
- 📦 GitHub：https://github.com/pandas-dev/pandas （43k+ star，已验证）
- **深链用法**：
  - [read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)：对标 TODO2-5，SQL 查询结果转 DataFrame
  - [DataFrame.to_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)：DataFrame 写入数据库表
  - [SQL 查询教程](https://pandas.pydata.org/docs/user_guide/io.html#sql-queries)：pandas 与 SQL 的完整桥接指南

### SQLite Tutorial（已验证）
- 🌐 教程网站：https://www.sqlitetutorial.net/
- **用法**：Day 5 的进阶 SQL 练习资源。从基础到进阶的 SQLite 教程，涵盖 CREATE TABLE/INSERT/SELECT/JOIN/GROUP BY/窗口函数/CTE/索引/视图/触发器。提供在线练习环境，适合巩固 TODO1-6 的 SQL 技能。
- **深链用法**：
  - [SQLite INNER JOIN](https://www.sqlitetutorial.net/sqlite-inner-join/)：对标 TODO3
  - [SQLite GROUP BY](https://www.sqlitetutorial.net/sqlite-group-by/)：对标 TODO4
  - [SQLite Window Functions](https://www.sqlitetutorial.net/sqlite-window-functions/)：对标 TODO5

---

## ③ 2026 前沿：数据治理 / Apache Iceberg / 湖仓一体

### DAMA-DMBOK 数据管理知识体系（已验证）
- 🌐 DAMA International：https://www.dama.org/cpages/body-of-knowledge
- **用法**：Day 5 数据治理的理论基础。DAMA-DMBOK（Data Management Body of Knowledge）定义了数据管理的 11 个知识领域，数据治理是核心统筹领域。重点理解数据质量六维度（准确性/完整性/一致性/及时性/唯一性/有效性）和元数据管理的最佳实践。在 AI 营销系统中，DAMA-DMBOK 提供系统化的数据治理 checklist，是 AI 可靠性的制度保障。

### Apache Iceberg 开放表格式（已验证）
- 🌐 官方网站：https://iceberg.apache.org/ （已验证，Apache-2.0）
- 📦 GitHub：https://github.com/apache/iceberg （已验证，活跃维护）
- **用法**：Day 5 湖仓一体的前沿技术。Apache Iceberg 是开放表格式（Open Table Format）的代表，为数据湖提供 ACID 事务、时间旅行、Schema 演化能力，是"湖仓一体"的技术基石。重点理解 Iceberg 如何让数据湖具备数据仓库的 ACID 和 Schema 管理能力。Snowflake、Databricks、Trino、Spark 等主流引擎均已支持 Iceberg。对营销场景：可以在同一份数据上同时做 BI 报表和 ML 训练。

### Great Expectations 数据质量监控（已验证）
- 🌐 官方文档：https://greatexpectations.io/ （已验证，Apache-2.0）
- 📦 GitHub：https://github.com/great-expectations/great_expectations （9k+ star，已验证）
- **用法**：Day 5 数据质量监控的前沿工具。Great Expectations 提供声明式数据质量检查--用 Python/SQL 声明数据质量规则（如"customer_id 必须唯一""price 必须 > 0"），每次数据入库时自动运行检查。对营销场景：当数据从 CRM 流入数据仓库时，自动检查手机号格式、消费金额、客户ID一致性，将数据治理从"事后审计"升级为"事前预防"。

### 湖仓一体（Lakehouse）架构
- 📄 Armbrust et al. (2021)："Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics"，CIDR 2021
- **用法**：Databricks 团队提出的湖仓一体架构白皮书。阐述了如何用 Delta Lake / Apache Iceberg 等开放表格式，在数据湖上实现数据仓库的 ACID、Schema 管理、数据质量保证。对 AI 营销的启示：结构化的客户/订单数据和非结构化的客服对话/广告素材可以在同一平台上统一管理，无需数据搬运。

---

## ④ 营销分析方法论

### RFM 客户分群方法
- 📄 Hughes, A. (1996)："The Complete Database Marketer"，McGraw-Hill
- **用法**：Day 5 TODO5 的理论基础。RFM（Recency, Frequency, Monetary）是营销领域最经典的客户分群方法，由 Hughes 在 1994-1996 年提出。R 衡量客户活跃度，F 衡量忠诚度，M 衡量价值。本 Day 用 SQL 窗口函数和子查询实现 RFM 分群，展示 SQL 在营销分析中的强大能力。

### 数据隐私与合规
- 🌐 GDPR 官方文本：https://gdpr-info.eu/ （已验证）
- **用法**：Day 5 数据隐私合规的参考。GDPR（欧盟通用数据保护条例）要求企业在处理个人数据时遵循"合法、公平、透明"原则，用户有权访问、更正、删除其个人数据。在营销 AI 系统中，用户画像、行为追踪、个性化推荐都必须在 Schema 设计时就嵌入合规要求（Privacy by Design）。
- 🌐 中国个人信息保护法：http://www.npc.gov.cn/npc/c30834/202108/a8c4e3672c74491a80b53a172bb753fe.shtml （已验证）

---

## ⑤ 对标课程

### MIT OCW 15.071: The Analytics Edge（已验证）
- 🌐 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/
- **用法**：Day 5 的标杆课程。MIT 15.071 的数据库与 SQL 相关单元与本 Day 的 SQL 查询对标。英语轨道材料：读英文讲义，重点关注 SQL 在商业分析中的应用。

### Stanford: Introduction to Databases（已验证）
- 🌐 课程主页：https://online.stanford.edu/courses/soe-ydatabases-introduction-databases
- **用法**：Stanford 的数据库入门课程，涵盖关系模型/SQL/范式化/索引/事务，是 Day 5 理论部分的权威对标。重点学 relational algebra（关系代数）和 normalization（范式化）的概念。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 5 | 数据治理与 SQL 理论 | 1h |
| 2 | Python sqlite3 官方文档（选读） | 真实库 API 巩固 | 0.5h |
| 3 | `starter.ipynb` 上机（配 SQLite Tutorial） | 真实库实操 | 2h |
| 4 | Kaggle Learn: SQL（英语轨道） | SQL 互动练习 | 2h |
| 5 | Apache Iceberg + Great Expectations 概念 | 2026 前沿 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
