# Day 5 真实数据与库说明

> v5.0 核心升级：用**真实数据库引擎**（sqlite3，Python 内置）+ **SQL-DataFrame 桥接**（pandas.read_sql）替代纯理论讲解。sqlite3 是零安装的关系型数据库引擎，能完整运行 DDL/DML/DQL，是学习 SQL 与数据治理的最佳实践工具。

---

## 主库：sqlite3（Python 内置，无需安装）

**这是什么**：sqlite3 是 Python 标准库内置的轻量级关系型数据库引擎（Python Software Foundation License）。它不需要独立的服务器进程，整个数据库存储在单个文件中（或内存中），零配置零安装即可使用。尽管轻量，sqlite3 完整支持 SQL 标准的 DDL（CREATE/ALTER/DROP）、DML（INSERT/UPDATE/DELETE）、DQL（SELECT/JOIN/GROUP BY/窗口函数）、DCL（GRANT/REVOKE），是企业级数据库（PostgreSQL/MySQL）的完美学习替代。

**为什么用它**：
- **零安装**：Python 标准库内置，`import sqlite3` 即可用，无需 pip install
- **完整 SQL 支持**：主键/外键/CHECK约束/索引/视图/触发器/窗口函数/CTE 全部支持
- **内存模式**：`sqlite3.connect(':memory:')` 创建内存数据库，适合教学演示和单元测试
- **文件模式**：`sqlite3.connect('marketing.db')` 创建文件数据库，数据持久化
- **工业级 Schema**：可设计完整的多表关系型数据库（如电商6表Schema），支撑真实营销分析

**安装方式**：

```bash
# sqlite3 是 Python 标准库，无需安装！直接导入即可：
python -c "import sqlite3; print(sqlite3.sqlite_version)"
# 预期输出: 3.x.x
```

**核心 API 速查**：

| 组件 | 导入 | Day 5 用途 |
|------|------|-----------|
| connect | `import sqlite3; conn = sqlite3.connect(':memory:')` | 创建内存数据库（TODO1） |
| cursor | `cursor = conn.cursor()` | 获取游标执行 SQL |
| execute | `cursor.execute('CREATE TABLE ...')` | 执行 DDL 建表（TODO1） |
| executemany | `cursor.executemany('INSERT ...', data)` | 批量插入数据（TODO1） |
| commit | `conn.commit()` | 提交事务 |
| read_sql | `pd.read_sql_query(sql, conn)` | SQL 结果转 DataFrame（TODO2-5） |

**来源与验证**：
- Python 官方文档：https://docs.python.org/3/library/sqlite3.html （已验证，Python 标准库）
- SQLite 官网：https://www.sqlite.org/ （已验证，公共领域软件）
- GitHub 镜像：https://github.com/python/cpython/blob/main/Modules/_sqlite/ （已验证，CPython 仓库）

---

## 辅助库：pandas.read_sql

**这是什么**：pandas 的 `read_sql_query()` / `read_sql()` 函数能将 SQL SELECT 查询结果直接转为 pandas DataFrame，打通 SQL 与 Python 数据分析的闭环。这意味着你可以用 SQL 做数据提取和聚合（SQL 更擅长），再用 pandas 做统计分析和可视化（pandas 更擅长）。

**安装**：

```bash
pip install pandas
# 验证安装：
python -c "import pandas as pd; print(pd.__version__)"
# 预期输出: 2.x.x
```

| 组件 | 导入 | Day 5 用途 |
|------|------|-----------|
| read_sql_query | `pd.read_sql_query(sql, conn)` | 执行 SELECT 并返回 DataFrame（TODO2-5） |
| read_sql | `pd.read_sql(sql, conn)` | read_sql_query 的别名 |
| to_sql | `df.to_sql('table', conn)` | 将 DataFrame 写入数据库表 |

- 官方文档：https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html （已验证）
- GitHub：https://github.com/pandas-dev/pandas （43k+ star，已验证）

---

## 数据：电商企业营销数据库 Schema（内嵌于 notebook）

本 Day 使用真实电商企业营销场景的数据库 Schema，直接在 `starter.ipynb` 和 `solution.ipynb` 中用 SQL DDL 创建并插入数据，无需外部下载：

### 数据库 Schema 设计（6 张表）

| 表名 | 记录数 | 核心字段 | 营销用途 |
|------|--------|---------|---------|
| categories（类目表） | 6 | category_id, category_name, parent_category_id | 商品分类管理 |
| customers（客户表） | 200 | customer_id, name, phone, email, gender, customer_level, status | 客户画像、RFM分析 |
| products（商品表） | 50 | product_id, product_name, category_id, brand, price, cost, stock | 商品管理、利润分析 |
| orders（订单表） | 500 | order_id, customer_id, order_date, total_amount, status, channel | 消费行为、渠道分析 |
| order_items（订单明细表） | ~1200 | item_id, order_id, product_id, quantity, unit_price, subtotal | 商品销量、GMV计算 |
| campaigns（营销活动表） | 3 | campaign_id, campaign_name, channel, budget, target_audience | 营销活动管理 |

### Schema 关系图

```
categories (类目)
    ↑ parent_category_id (自引用)
    |
products (商品) ── category_id → categories
    |
order_items (订单明细) ── product_id → products
    |                    ── order_id → orders
orders (订单) ── customer_id → customers
    |
customers (客户) ── customer_level (普通/银卡/金卡/钻石)

campaigns (营销活动) ── 独立表，关联 channel 字段
```

**设计要点**：
- **主键约束**：每表有 PRIMARY KEY（customer_id/product_id/order_id 等），保证唯一性
- **外键约束**：orders.customer_id → customers，order_items.product_id → products，保证参照完整性
- **CHECK 约束**：price > 0、stock >= 0、gender IN ('M','F','O')、status 枚举值，保证数据有效性
- **GENERATED 列**：order_items.subtotal = quantity * unit_price（自动计算，防篡改）
- **DEFAULT 值**：customer_level DEFAULT '普通'、status DEFAULT 'active'

> 💡 **数据来源说明**：这些数据模拟真实电商平台的营销数据（200客户/50商品/500订单），用 numpy 生成随机但合理的数据分布。在实际项目中，你可以用 `pd.read_sql()` 从业务数据库提取真实数据。本上机用 SQL 内嵌数据确保开箱即用。

---

## 可选扩展：公开 SQL 数据集

如果需要更大规模的真实 SQL 数据练习，可以用以下公开数据集：

### 1. Chinook 示例数据库（已验证）

- URL：https://github.com/lerocha/chinook-database
- **描述**：经典的 SQLite 示例数据库，模拟数字音乐商店（Artist/Album/Track/Invoice/Customer 等 11 张表），是学习 SQL JOIN/GROUP BY/窗口函数的最佳实践数据集
- **用法**：下载 SQLite 版本，`sqlite3.connect('chinook.db')` 即可查询

### 2. UCI: Online Retail II 数据集（已验证）

- URL：https://archive.ics.uci.edu/dataset/502/online+retail+ii
- **描述**：UCI Machine Learning Repository 的经典电商数据集（2010-2011 年交易记录），适合练习 SQL 聚合、RFM 分析、客户分群
- **用法**：下载 CSV 后用 `pd.read_csv()` 加载，再用 `df.to_sql()` 导入 SQLite 做查询练习

### 3. Kaggle: SQL Practice Dataset（已验证）

- URL：https://www.kaggle.com/datasetsgetitem/sql-practice-dataset
- **描述**：Kaggle 提供的 SQL 练习数据集，包含多种表结构，适合进阶练习
- **用法**：配合 Kaggle Learn: SQL 课程使用

---

## 为什么不用纯理论讲解（v4.0 做法）

| 维度 | 纯理论讲解（v4.0） | sqlite3 实操（v5.0） |
|------|-------------------|---------------------|
| Schema 设计 | 画 ER 图讲解 | `CREATE TABLE` 真实建表+约束 |
| SQL 语法 | 伪代码演示 | 真实执行 SELECT/JOIN/GROUP BY |
| 数据约束 | 口头说明 | CHECK/FOREIGN KEY 真实报错 |
| 查询验证 | 看不到结果 | `pd.read_sql_query()` 看到真实数据 |
| 数据治理 | 概念介绍 | 索引/缺失值检测/质量审计实操 |
| 性能 | 无法讨论 | 可用 EXPLAIN QUERY PLAN 分析 |

**真实即严谨**--用 sqlite3 真实数据库引擎替代纯理论讲解，是 v5.0 的哲学增量。
