# Day 5 产业链接层 (v7.0) - 数据治理与 SQL

> 本单元产出产业链接 (industry linkage): >=3 真实企业锚点 + 部署场景 + Imperial MSc BA 风格咨询项目 + HBS 教学案例钩子 + 客座讲座 + 实习指针。所有企业从公司库挑, 与本单元主题 (数据治理 / SQL / 电商营销数据库 / RFM 52/49/31/45 / 六维数据治理审计 / sqlite3 + pandas.read_sql / DAMA-DMBOK / Apache Iceberg / 湖仓一体) 匹配。

---

## real_companies

>=3 家真实企业锚点, 均与本单元数据治理 + SQL + 电商营销主题匹配:

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Booking.com** | SQL 重度用户 / 数据治理六维审计 / A/B 实验数据质量 | Booking.com 每天运行数千个 A/B 实验, 实验数据质量直接影响决策。其数据团队用 SQL (BigQuery/Snowflake) 做客户分群与实验分析, 数据治理 (唯一性/完整性/及时性) 是实验可信度的前提。与本单元 RFM 分群 + 六维审计直接对标。 |
| **Sephora** | 零售营销数据库 / RFM 客户分群 / Beauty Insider 会员体系 | Sephora 的 Beauty Insider 会员体系覆盖数千万客户, 用 RFM 类方法做客户分层与个性化营销。其营销数据库 Schema (客户/订单/商品/营销活动) 与本单元电商 6 表 Schema 高度同构, 数据治理 (主数据管理 / 客户ID 跨系统统一) 是核心挑战。 |
| **Walmart** | 超大规模电商营销数据库 / 数据仓库 vs 数据湖 vs 湖仓一体 / Apache Iceberg | Walmart 全球最大零售商之一, 营销与供应链数据规模极大, 用湖仓一体 (Apache Iceberg on S3/Spark) 统一结构化订单与非结构化客服对话。与本单元"湖仓一体选型"与"Iceberg Time Travel 审计"前沿点直接对标。 |
| **Amazon (AWS)** | 数据仓库 Redshift / 湖仓一体 (Iceberg on S3 + Athena) / 营销数据治理 | Amazon 自身用 Redshift + S3 + Iceberg 做营销与推荐数据底座; AWS 是 Iceberg 的主要企业推动者之一。与本单元"数据仓库 vs 数据湖 vs 湖仓一体"选型决策直接对标。 |

---

## deployment_example

**部署场景: Walmart 营销数据湖仓一体的 RFM 客户分群与治理审计**

Walmart 在生产中用湖仓一体架构 (Apache Iceberg on S3 + Spark/Trino 查询引擎) 统一营销数据, 规模与约束如下:

- **规模**: 数亿客户 / 数十亿订单 / 数万 SKU / 跨 20+ 国家; 每日新增订单 TB 级。
- **技术栈**: S3 数据湖 (Iceberg 表格式, ACID + Time Travel) + Spark ETL + Trino/Presto 即席 SQL 查询 + Great Expectations 数据质量门禁 + pandas/Spark DataFrame 下游分析。
- **治理约束**: 数据入库时自动跑六维审计 (唯一性: 客户ID 跨系统去重 / 完整性: 手机号邮箱非空率 / 一致性: 订单客户ID 外键 / 及时性: order_date 滞后检测 / 有效性: amount > 0 CHECK / 准确性: 跨源对账), 失败则阻断流水线 (Great Expectations 声明式规则)。
- **RFM 分群**: 用 Spark SQL 窗口函数 `RANK() OVER (ORDER BY recency)` + CTE 在 Iceberg 表上跑 RFM 分箱, 输出 52/49/31/45 四组 (核心/新客/流失风险/流失), 每周刷新; Iceberg Time Travel 支持回溯任意历史版本的分群结果, 做客户迁移率分析。
- **效果**: 湖仓一体让 BI 报表 (Trino SQL) 与 ML 训练 (Spark MLlib) 在同一份数据上运行, 无需数据搬运; 六维审计将"事后审计"升级为"事前预防", 数据质量事故下降 (与本单元 notes.md "Great Expectations 将治理从事后审计升级为事前预防"一致)。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目**

- **Partner (赞助企业)**: Burberry (零售/CPG 咨询项目 partner, 公司库)
- **Problem (真实业务问题)**: Burberry 的奢侈品客户分群 (VIP/Aspirational/New/At-risk) 当前用各区域团队即席 SQL 跑, 数据质量参差 (客户ID 跨系统不统一 / 消费金额缺失 / 数据更新滞后), 导致分群结果区域间不可比, 个性化营销 ROI 波动大。需要一套统一的客户数据治理与分群框架。
- **Data (企业提供数据)**: Burberry 提供 18 个月脱敏客户/订单/营销活动数据 (约 50 万客户 / 200 万订单), 含线上线下多渠道; 数据 Schema 与本单元电商 6 表 Schema 同构 (customers/products/categories/orders/order_items/campaigns)。
- **Scope (8 周, 4-5 人)**: 周 1-2 现状诊断 (跑六维审计 SQL, 量化数据质量基线) / 周 3-4 Schema 规范化与主数据统一 (3NF + 客户ID 跨系统映射) / 周 5-6 RFM 分群迁移 (52/49/31/45 四组 + Bootstrap 稳定性验证) / 周 7 报告与可视化 / 周 8 交付与培训。
- **Deliverable (交付物)**: (1) 数据治理成熟度评估报告 (六维评分卡 + 6 条 SQL 审计脚本) (2) 统一客户营销数据库 Schema 设计文档 (3NF + 主数据) (3) RFM 分群原型 (SQL + pandas.read_sql + 可视化 Dashboard) (4) 数据质量监控规则集 (Great Expectations 格式, 接入 Burberry 数据流水线) (5) 策略建议书 (向 CMO/Head of Data 汇报)。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Maria Chen, 某全球零售品牌 Head of Customer Data (前 McKinsey 数据咨询合伙人, 现任企业内数据负责人)。
- **Decision (关键决策点)**: Maria 面临决策 - 是否将六维数据治理审计 (6 条 SQL + Great Expectations 规则) 嵌入每周 RFM 客户分群刷新流水线? 嵌入会增加每周 4 小时计算成本与 0.5 FTE 数据工程运维, 但预期将分群迁移率 (52↔49 / 31↔45 误移) 降低 30%+, 提升个性化营销 ROI。
- **Tension (核心张力/两难)**:
  - **短期成本 vs 长期收益**: 治理审计的 4 小时 + 0.5 FTE 成本本季度可见, 而分群稳定性收益需 2-3 个季度才能在营销 ROI 中显现。
  - **工程团队 vs 营销团队**: 工程团队主张"先治理再分析" (数据质量是前提), 营销团队主张"先分析再治理" (业务不等人)。Maria 需在两条路线间取舍。
  - **Lakehouse 投资 vs 现有数据仓库**: 治理审计在现有 Snowflake 数据仓库上可跑, 但迁移到 Lakehouse (Iceberg) 能获得 Time Travel 回溯能力 - 投资规模 vs 能力跃升。
- **教学目标**: 学员用本单元六维数据治理框架 + RFM 52/49/31/45 分群方法, 量化 Maria 的决策选项, 给出 2-3 个差异化策略建议 (含收益/风险/成本权衡)。

---

## guest_lecture

**客座讲座**

- **Topic (主题)**: *"From Schema to Segments: How [Company] Governs Customer Data for AI Marketing at Scale"* (从 Schema 到分群: [公司] 如何治理客户数据以支撑规模化 AI 营销)
- **Speaker Profile (主讲人画像)**: 某全球零售/电商平台 (Walmart/Sephora/Booking.com 级) Head of Data Engineering 或 Head of Customer Analytics, 10+ 年数据治理与营销分析经验, 熟悉 DAMA-DMBOK 框架与 Lakehouse 架构, 曾主导企业级数据治理项目落地。
- **内容大纲**:
  1. (15 min) 企业营销数据治理现状 - 六维度挑战 (唯一性/完整性/一致性/及时性/有效性/准确性) 与本单元笔记的对应
  2. (15 min) Lakehouse 架构选型 - 数据仓库 vs 数据湖 vs 湖仓一体, Apache Iceberg 在生产中的角色
  3. (15 min) RFM 客户分群生产化 - SQL 窗口函数 + CTE 在万亿级数据上的工程实践, Great Expectations 数据质量门禁
  4. (15 min) Q&A - 与学员讨论本单元 starter.ipynb 的 6 个 TODO 在企业生产中的对应
- **与本单元衔接**: 主讲人用本单元电商 6 表 Schema 做开场类比, 让学员理解"教学版 sqlite3"与"生产版 Lakehouse"的工程差异, 衔接 Day 6 研究方法论与技能1 营销 AI Agent。

---

## internship_pointer

**实习/驻留指针**

- **机构 (3 个候选, 均与本单元数据治理 + SQL + 营销分析匹配)**:
  1. **Google AI Resident / Google Data Engineering Intern** - Google Ads 团队用 SQL + 数据治理支撑广告投放分群与归因; 本单元 SQL DQL + pandas.read_sql + 六维审计为该角色的直接前置。
  2. **Walmart Global Tech - Data Engineering Internship** - Walmart 营销与供应链 Lakehouse (Iceberg on S3 + Spark/Trino) 团队, 实习生参与数据质量门禁与客户分群工程化; 本单元 Apache Iceberg 前沿点 + 六维审计为该角色的概念前置。
  3. **Booking.com Data Science Internship** - Booking.com 数据驱动实验文化, 实习生用 SQL + A/B 实验做客户分群与效果评估; 本单元 RFM 52/49/31/45 + 数据治理为该角色的方法论前置。
- **角色**: Data Engineering Intern / Data Science Intern / Analytics Engineer Intern (8-12 周)
- **衔接 (本单元如何为该角色做准备)**:
  - sqlite3 + pandas.read_sql 打通 SQL 与 Python 数据分析的闭环, 是 Analytics Engineer 角色的核心技能栈。
  - 六维数据治理审计 + DAMA-DMBOK 框架, 让实习生能在企业数据流水线中识别质量问题, 是 Data Engineering 角色的差异化能力。
  - RFM 52/49/31/45 分群 + 窗口函数/CTE/子查询, 是 Data Science/Marketing Analytics 角色的方法论基础, 直接可迁移到企业客户分群项目。
  - Apache Iceberg + Lakehouse 前沿点, 让实习生能在面试中展示对现代数据架构的理解, 是 Walmart/Booking.com 级企业的加分项。
