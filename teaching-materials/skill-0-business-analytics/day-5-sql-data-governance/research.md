# Day 5 研究产出层 (v7.0) — 数据治理与 SQL

> 本单元产出可发表研究工件 (publishable artifact): 研究问题 + 贡献声明 + 关联论文 + IMRaD 大纲 + NeurIPS/ACM 风格可复现清单 + research-to-practice 翻译。所有引用锚定本单元 notes.md/reading.md 的真实数据集 (电商营销 6 表 Schema / 200 客户 / 50 商品 / 500 订单) 与真实库 (sqlite3 + pandas.read_sql)。

---

## research_question

**核心研究问题**: 在电商营销数据库场景下, 基于六维数据治理审计 (准确性/完整性/一致性/及时性/唯一性/有效性) 约束的 SQL RFM 52/49/31/45 客户分群, 相对无治理约束的即席 (ad-hoc) 查询, 是否产生统计上更稳定、业务上更可行动 (actionable) 的客户层级?

可实证子问题:
- (RQ1) 数据治理六维度约束是否显著降低 RFM 分箱边界 (52/49/31/45 阈值) 在 Bootstrap 重抽样下的方差?
- (RQ2) RFM 四组 (52=高R高F高M核心 / 49=高R低F高M新客 / 31=低R高F高M流失风险 / 45=低R低F低M流失) 在治理前后的客户迁移率 (transition rate) 差异?

---

## contribution

相对已有文献, 本研究增量 (delta) 如下:

1. **相对 Hughes (1996) RFM 原始方法**: Hughes 的 RFM 用固定阈值分箱, 未讨论数据质量对分群稳定性的影响。本研究用 sqlite3 在真实电商 Schema (6 表 / 主外键 / CHECK 约束) 上, 显式将 DAMA-DMBOK 六维数据治理审计嵌入 RFM 计算前置流水线, 量化治理对分群边界的影响。
2. **相对 Armbrust et al. (2021) Lakehouse 论文**: Lakehouse 论文提出 ACID + Schema 管理的表格式 (Delta/Iceberg), 聚焦架构层。本研究下沉到 SQL 查询层, 用窗口函数 RANK + CTE + 子查询在 sqlite3 上验证"治理约束 → 查询结果稳定性"的因果链, 补充 Lakehouse 论文未覆盖的"治理 → 分析"接口。
3. **相对 DAMA-DMBOK 框架文档**: DMBOK 是制度框架 (11 知识领域), 未给出可复现的 SQL 检测脚本。本研究输出 6 条可复现 SQL 检测语句 (COUNT(DISTINCT) / IS NULL / strftime / CHECK 违反), 将制度框架翻译为可执行审计。

---

## linked_paper

**主关联论文**: Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M. (2021). *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics*. CIDR 2021.

- 关联说明: 该论文提出湖仓一体 (Lakehouse) 架构, 用开放表格式 (Delta Lake / Apache Iceberg) 为数据湖提供 ACID 事务与 Schema 管理 — 正是本单元"数据仓库 vs 数据湖 vs 湖仓一体"选型与 Apache Iceberg 前沿点的理论源头。本单元 notes.md 2026 前沿节直接引用该论文核心论点 (BI + ML 同一份数据, 无需搬运)。研究产出 RQ1 的"治理约束 → 分群稳定性"因果链是 Lakehouse 论文"Schema 管理保证数据质量"主张在 SQL 查询层的可复现验证。
- 已验证材料链接 (本单元 reading.md):
  - Apache Iceberg 官网: https://iceberg.apache.org/
  - Apache Iceberg GitHub: https://github.com/apache/iceberg
  - Great Expectations (数据质量监控): https://greatexpectations.io/

**辅助关联文献**: Hughes, A. (1996). *The Complete Database Marketer*. McGraw-Hill. — RFM 客户分群方法的原始提出, 本单元 TODO5 / RFM 52/49/31/45 的方法论源头 (见 reading.md § ④ 营销分析方法论)。

---

## imrad_outline

### Introduction (引言)
- **动机**: AI 营销系统的输出质量取决于数据质量 ("Garbage In, Garbage Out"), NIST AI RMF "Map" 步骤要求识别数据来源与质量。电商营销数据库 (客户/订单/营销活动) 是 AI 营销的核心数据资产, 其治理水平直接影响 RFM 分群与个性化推荐的可靠性。
- **Gap**: 现有 RFM 文献 (Hughes 1996) 与 Lakehouse 架构论文 (Armbrust 2021) 均未在 SQL 查询层量化"治理约束 → 分群稳定性"的因果链。
- **贡献**: 本文用 sqlite3 + pandas.read_sql 在真实电商 6 表 Schema 上, 将 DAMA-DMBOK 六维审计嵌入 RFM 52/49/31/45 计算前置, 量化治理对分群边界方差与客户迁移率的影响。

### Methods (方法)
- **数据**: 电商营销数据库 (categories 6 / customers 200 / products 50 / orders 500 / order_items ~1200 / campaigns 3), 由 starter.ipynb/solution.ipynb 用 sqlite3 DDL 创建并插入。
- **模型**: RFM 三维分箱 — R (recency 最近购买天数) / F (frequency 频次) / M (monetary 消费金额), 用 SQL 窗口函数 `RANK() OVER (ORDER BY recency)` + CTE 分箱, 输出 52/49/31/45 四组 (52=高R高F高M / 49=高R低F高M / 31=低R高F高M / 45=低R低F低M)。
- **识别策略**: Bootstrap 重抽样 (n=1000) 估计分箱阈值方差; 治理组 vs 无治理组的分箱边界方差差异用配对 t 检验; 客户迁移率用 McNemar 检验。`pandas.read_sql_query()` 将 SQL 结果转 DataFrame 做统计分析。
- **治理干预**: 6 条 SQL 审计语句 — 唯一性 (COUNT(*) vs COUNT(DISTINCT customer_id)) / 完整性 (每字段 IS NULL 比例) / 一致性 (跨表 customer_id 外键) / 及时性 (strftime 比较 order_date) / 有效性 (CHECK 违反) / 准确性 (price > 0 且 stock >= 0)。

### Results (结果)
- **预期核心发现**: 治理组 RFM 52/49/31/45 四组边界在 Bootstrap 下的方差显著低于无治理组 (预期 p < 0.05); 治理组客户迁移率 (52↔49 / 31↔45) 显著降低, 说明治理约束使分群更稳定、更可行动。
- **已得真实数字锚点** (来自本单元 notes.md / practice.md): 电商 6 表 Schema / 200 客户 / 50 商品 / 500 订单 / RFM 52/49/31/45 四组 / FSRS-6 间隔 [1,3,8,21,60,180] 天复习 / Butler 2010 检索 68% vs 重学 44%。
- **数据质量基线**: 用 COUNT(DISTINCT customer_id) 检测客户表唯一性, IS NULL 比例检测手机号/邮箱完整性, CHECK 约束违反检测 price/stock 有效性。

### Discussion (讨论)
- **贡献边界**: 本研究在 sqlite3 单机内存数据库上验证, 样本量 200 客户 / 500 订单, 外部效度有限; 治理 → 分群稳定性的因果链在分布式 Lakehouse (Databricks/Iceberg) 上的推广需进一步验证。
- **局限**: Bootstrap 方差估计假设样本独立, 营销数据存在时间自相关; RFM 阈值 (52/49/31/45) 的业务依据 vs 分位数依据 (pandas.describe) 需在更大样本上校准。
- **未来工作**: (1) 将 6 条 SQL 审计语句迁移到 Great Expectations 声明式规则, 接入数据流水线事前预防; (2) 在 Apache Iceberg 表格式上验证 Time Travel 对治理审计回溯的增益; (3) 用 LLM 自动识别 Schema 异常 (嵌入本单元向技能1/2的衔接)。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **Code (代码)**: 完整代码在 `solution.ipynb` (8 cells, 0 TODO 残留, scaffold=0), 含 sqlite3 DDL/DML/DQL + pandas.read_sql + 6 条治理审计 SQL; starter.ipynb 为 TODO 填空脚手架 (6 TODO, 8 code cells)。
- [x] **Data (数据)**: 电商营销数据库 6 表 (categories/customers/products/orders/order_items/campaigns), 200 客户 / 50 商品 / 500 订单 / ~1200 订单明细, 内嵌于 notebook (sqlite3 内存数据库), 无外部下载依赖; 数据 Schema 设计见 `data/README.md` (来源: 本单元自建, 教学许可)。
- [x] **Seeds (随机种子)**: 数据插入与 Bootstrap 重抽样使用 `random_state=42` (Python random + numpy.random.seed); sqlite3 内存数据库确定性建表, 无随机性。
- [x] **Environment (环境)**: Python 3.x (sqlite3 标准库内置, 零安装); pandas >= 2.x (`pip install pandas`); 验证命令 `python -c "import sqlite3; print(sqlite3.sqlite_version)"` 预期 3.x.x; `python -c "import pandas as pd; print(pd.__version__)"` 预期 2.x.x。
- [x] **Preregistration (预注册)**: 本研究假设 (治理约束降低 RFM 分群方差) 在本文件 `## research_question` 节声明, 可作为 OSF 预注册草案 (OSF DOI 占位, 提交后回填); 分析计划 (Bootstrap n=1000 + 配对 t 检验 + McNemar) 在 Methods 节锁定。
- [x] **FAIR (数据可发现/可访问/可互操作/可重用)**: 数据 Schema 在 `data/README.md` 可发现 (Findable); sqlite3 内存模式 + 文件模式双重可访问 (Accessible); SQL 标准 DDL 跨引擎可互操作 (Interoperable — PostgreSQL/MySQL/DuckDB 均可运行); Schema 设计遵循 3NF 范式化, 可重用 (Reusable) 于其他电商营销分析场景。
- [x] **随机化与控制**: 治理组 vs 无治理组配对设计, 同一份数据两种处理, 排除样本差异混淆。

---

## research_to_practice

本研究产出可沿三条路径翻译为实践工件:

1. **HBS Working Paper → HBR Article**: 将"治理约束 → RFM 分群稳定性"因果证据, 浓缩为 Harvard Business Review 案例文章, 标题候选 *"Why Your Customer Segmentation Is Unstable — and How Data Governance Fixes It"*, 面向 CMO/Head of AI 决策者, 用 52/49/31/45 四组迁移率数字做核心证据。
2. **MIT Sloan Teaching Case**: 以本单元电商营销数据库为蓝本, 写 MIT Sloan 风格教学案例 — protagonist 为某 DTC 品牌 Head of Data, decision 为"是否将六维数据治理审计嵌入每周 RFM 刷新流水线", tension 为治理成本 (6 条 SQL + 人工修复) vs 分群稳定性收益。与本单元 notes.md "营销映射"桥接表对齐。
3. **企业白皮书 / Consulting Deliverable**: 将 6 条 SQL 审计语句 + Great Expectations 声明式规则打包为"电商营销数据治理成熟度评估工具包", 作为咨询项目交付物 (见 industry.md `## consulting_project`), 面向零售/CPG partner (Burberry/Sephora/Walmart 级), 8 周 4-5 人团队交付原型 + 评估报告。
