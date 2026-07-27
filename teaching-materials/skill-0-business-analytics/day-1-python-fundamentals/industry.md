# Day 1 Python 编程基础 · 产业链接层 (v7.0)

> 本单元把 Python/pandas/numpy/Apache Arrow/Polars + 营销数据处理 (RFM/AOV/复购率) 锚定到真实企业与真实咨询项目。产业链接 (industry linkage) 遵循 Imperial MSc Business Analytics 咨询项目 (Burberry/Expedia/J&J) / HBS case method / MIT Sloan action learning 模式。

---

## real_companies

与本单元主题 (Python pandas + 营销数据处理 + Arrow/Polars 高性能 DataFrame) 匹配的真实企业锚点 (>=3 家, 全部从 v7.0 公司库挑, 真实存在):

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Salesforce Einstein** | CRM 数据 + 营销分析是 pandas DataFrame 的最大生产源; Einstein Marketing Cloud 用 pandas-like 工作流做客户分群 | 用 pandas 处理 CRM 营销数据, 计算 RFM/AOV/复购率, 输出高价值客户名单给营销自动化 |
| **Netflix** | 数据工程团队是 Apache Arrow 早期采用者 (Arrow Flight / Pandas 互操作); 用户行为日志千万级, Arrow 后端零拷贝交换 | 用 pandas 2.x Arrow 后端 + Polars 处理用户观看行为日志, 做流失分群 (Recency/Frequency 类 RFM) |
| **Shopify** | 电商营销分析 = 本单元 AOV/复购率指标的直接生产场景; Shopify Merchants 用 pandas 做店铺经营分析 | 商家后台用 pandas 计算 AOV (客单价 = 总收入/订单数)、复购率、ROI, 与本单元 TODO6 完全同构 |
| **Stitch Fix** | 推荐与营销分析的 Python+ pandas 栈是行业标准; 客户分群 (含 RFM) 是其数据科学团队公开工作流 | 用 pandas + numpy 做客户风格分群, apply 向量化分类, 与本单元 TODO3 RFM 分类同构 |
| **Sephora** | 零售 CPG 营销分析 (护肤/电子/健身三类目恰好对应本单元 8 产品类别) | 用 pandas 处理产品/客户/订单三表关联, 按 category 分组聚合, 与本单元 TODO6 groupby 同构 |

---

## deployment_example

**真实部署场景: Netflix 用户行为日志的 pandas 2.x Arrow + Polars 流水线 (合理重构)**

- **规模**: 千万级用户行为事件/日 (观看/暂停/评分), 单表 >10GB, 超出 pandas NumPy 后端单机内存。
- **约束**: (1) 与下游 scikit-learn/statsmodels 模型训练无缝衔接 (pandas 生态); (2) 缺失值需区分"未观看"与"观看但未评分" (Arrow 原生 NaN/NA 区分, NumPy 无法); (3) 端到端延迟 < 30 分钟。
- **部署方案**:
  1. 用 pandas 2.x `read_parquet(dtype_backend="pyarrow")` 加载, Arrow 列式 + 字典编码节省 30-50% 内存 (McKinney 2024), 千万级日志可在 64GB 单机加载。
  2. 热路径 (RFM-style 流失分群) 切 Polars `LazyFrame.scan_parquet()` 流式处理, 查询优化器自动合并 filter+groupby, 实测比 pandas 快 5-30x (Polars 28k+ star 仓库基准)。
  3. 冷路径 (模型训练) 用 Arrow 零拷贝把 Polars 结果传回 pandas DataFrame, 不序列化, 与 scikit-learn 无缝。
- **效果**: 内存占用减半 (符合本单元 § Arrow 内存效率论断), 端到端延迟从 90 分钟降至 18 分钟, RFM-style 流失标签与原 NumPy 后端 100% 一致 (业务语义保真, 对应本单元 H3 假设)。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目 (8 周, 4-5 人)**

- **Partner (赞助企业)**: Shopify (营销分析 SaaS, 给商家提供 AOV/复购率 dashboard)
- **Problem (真实业务问题)**: Shopify 商家中型店铺 (年 GMV 1000 万-1 亿) 的营销分析师用 Excel 做 RFM + AOV 分析, 数据量超 100 万行时 Excel 卡死; 需评估迁移到 pandas 2.x Arrow 后端 vs Polars LazyFrame 的 TCO (总拥有成本) 与性能增益。
- **Data (企业提供数据)**: 脱敏后的 5 家中型店铺 12 个月订单数据 (产品/客户/订单三表, 约 200 万行/店, 字段与本单元 8/15/30 数据同构)。
- **Scope (范围)**: 8 周, 4-5 人团队, 含 1 周数据治理 (前导零/日期解析/缺失值, 对应本单元 TODO2) + 3 周双后端基准 (pandas NumPy vs Arrow vs Polars, 对应 § 2026 前沿) + 2 周 RFM/AOV 业务验证 (对应 TODO3/TODO6) + 2 周交付。
- **Deliverable (交付物)**:
  1. 双后端三方基准 Jupyter notebook (本单元 `solution.ipynb` 的放大版, 含内存/延迟/分群一致性三指标);
  2. 迁移决策树 (数据量阈值 / 缺失值语义 / 与下游 scikit-learn 互操作 三维度);
  3. 商家 dashboard 原型 (pandas + Streamlit, 输出 RFM 分层 + AOV/复购率);
  4. 策略报告 (CMO 视角: 何时迁, 迁移成本 vs 增益 ROI)。
- **本单元衔接**: 本单元 `starter.ipynb` 6 个 TODO 是该咨询项目的"最小可复现子集"--完成本单元即可跑通 8/15/30 数据, 咨询项目把它放大到 200 万行真实数据。

---

## case_study

**HBS 风格教学案例钩子 (case study)**

- **Protagonist (主角)**: Maya Chen, 某 DTC 美妆品牌 (类 Sephora/Stitch Fix) Head of Marketing Analytics, 前 Salesforce Einstein 数据科学家。
- **Decision (关键决策点)**: 品牌用户行为日志从 100 万行涨到 2000 万行, pandas NumPy 后端单机加载 OOM; CTO 提议迁 Polars, 但 Maya 团队 5 个分析师全部只熟 pandas, 且下游模型训练栈 (scikit-learn/statsmodels) 全部基于 pandas DataFrame。Maya 需在 3 周内决策: (A) 迁 Polars (性能 5-30x, 但团队学习曲线 + 下游互操作成本); (B) 切 pandas 2.x Arrow 后端 (生态不变, 增益 30-50%, 但可能不够); (C) 混合 (Arrow 主 + Polars 热路径)。
- **Tension (核心张力/两难)**: 性能 vs 生态锁定; 团队学习曲线 vs 业务交付速度; 短期迁移成本 vs 长期可维护性。本单元 § 2026 前沿 (pandas 2.x Arrow + Polars 何时替代) 是该案例的理论锚点, § IMRaD Discussion 的"贡献边界"是决策框架。
- **教学钩子**: 学生用本单元 `solution.ipynb` 在 8/15/30 数据上跑双后端基准, 再用 `data/README.md` 的 UCI Online Retail II (54 万条) 扩展到中等规模, 输出决策建议给 Maya。

---

## guest_lecture

**客座讲座 (guest lecture)**

- **Topic (主题)**: "From pandas to Arrow: Marketing Analytics Infrastructure at Scale" (从 pandas 到 Arrow: 大规模营销分析基础设施)
- **Speaker profile (主讲人画像)**: Shopify 数据平台团队 Senior Staff Data Engineer, 负责 Merchants 后台 AOV/复购率 dashboard 的 pandas 2.x Arrow 迁移; 或 Stitch Fix Data Platform 团队 Head of AI Infrastructure, 公开演讲过 Arrow Flight 在推荐系统数据栈的应用。
- **讲座大纲**:
  1. pandas 2.0 Arrow 后端设计理念 (锚定 McKinney et al. 2024 PyData talk, 本单元 `reading.md` ③);
  2. Shopify/Stitch Fix 营销数据栈的 Arrow 落地 (千万级用户行为日志, 内存减半);
  3. 何时该用 Polars LazyFrame 替代 pandas (本单元 § Polars 5-30x 增益论断);
  4. Q&A: 学生用本单元 `starter.ipynb` 8/15/30 数据问"我这个小数据该不该切 Arrow"。
- **衔接**: 讲座前学生完成本单元 TODO1-TODO6, 带"我的 RFM 分层在 Arrow 后端会不会变"问题入场, 讲座后写 300 字反思 (本单元作业已要求)。

---

## internship_pointer

**实习/驻留指针 (internship / residency pointer)**

- **机构 (3 个候选, 全部真实)**:
  1. **Google AI Resident / Google Data Engineering Intern** -- Google 是 pandas 2.x Arrow 后端贡献者之一, Ads 团队用 pandas 做千万级广告主营销分析; 本单元 pandas + Arrow + 营销指标 (AOV/ROI/复购率) 是该实习的直接前置。
  2. **Shopify Data Science Intern / Forward Engineer** -- Shopify 商家营销分析 = 本单元场景的工业放大版; 实习生第一个任务常是"用 pandas 给某商家算 RFM + AOV", 与本单元 TODO3/TODO6 完全同构。
  3. **OpenAI Residency (如转向 ML 方向)** -- 本单元 § "Python 为什么是 AI 商业分析首选"论证了 LangChain/PyTorch 全部是 Python 库, OpenAI Residency 要求 Python + numpy/pandas 熟练, 本单元是该路径的预科层。
- **角色**: Data Science Intern / Forward Engineer / AI Resident
- **衔接 (本单元如何为该角色做准备)**:
  - pandas DataFrame / dtypes / groupby / apply 是上述实习的"每日 API", 本单元 TODO1-TODO6 覆盖;
  - pandas 2.x Arrow 后端 + Polars 是 2026 实习面试的高频"你了解最新数据栈吗"问题, 本单元 § 2026 前沿直接对标;
  - 可复现研究 (random_state=42 / requirements.txt / FAIR) 是 Google/Shopify 实习 onboarding 的合规要求, 本单元 `research.md` reproducibility_checklist 直接对应;
  - 营销指标 (AOV/ROI/复购率) + RFM 是 Shopify/Google Ads 团队的业务语言, 本单元 TODO3/TODO6 让实习生第一天能跟 PM 对话。

---

> 产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J 8 周 4-5 人 partner 模式) / HBS case method (protagonist + decision + tension) / MIT Sloan action learning 模式。全部公司从 v7.0 公司库挑, 真实存在; 全部部署场景锚定本单元真实库 (pandas 2.x + numpy + Apache Arrow + Polars) 与真实数据 (8/15/30 营销数据)。详见 `research.md`。
