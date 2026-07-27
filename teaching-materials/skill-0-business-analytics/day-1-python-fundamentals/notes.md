# 技能0 · Day 1：Python 编程基础 + 营销数据处理 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能0 AI商业分析基础（预科层）· Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Python 为什么是 AI 商业分析的首选语言？--从语法基础到营销数据处理的完整闭环
> **v5.0 升级点**：① 真实库上机（pandas + numpy，替代纯手写脚本）② TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（pandas 2.x / Apache Arrow / Polars 高性能替代）

---

## 学习目标（学完你能做到）

1. 能解释 Python 为什么是 AI 商业分析的首选语言（生态完整性 > 语言速度），并说明 Python 标准库的五大语法要素（变量与数据类型、控制流、函数、数据结构、面向对象）在营销数据处理中的直接应用场景
2. 能用 **pandas** 加载营销数据（产品/客户/订单）为 DataFrame，用 `dtype`/`head()`/`describe()`/`info()` 完成数据类型检查与探索性分析，识别商业数据中的常见陷阱（前导零丢失、日期解析错误、缺失值）
3. 能用 Python 控制流（if-elif-else）和函数（def/apply）完成营销数据清洗与客户分类逻辑（如 RFM 分层、高价值客户筛选），并理解 `apply` 比 `for` 循环快 10-100 倍的向量化原理
4. 能用 Python 类（class）设计营销领域的 Product 和 Customer 对象，理解面向对象是后续使用 LangChain/DoWhy/PyTorch 等库的前提--这些库的 API 全部是面向对象设计的
5. 能用 Python 文件 IO（csv/json 模块 + pandas `to_csv`/`read_json`）读写营销数据，并计算核心营销指标（ROI、转化率、客单价 AOV、复购率）

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md` § Day 1](../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md)（77-269 行，已包含 Python 生态论证/五大语法要素/NumPy 数组运算/Pandas 表格处理/电商客户消费数据完整案例/RFM 分析/英语轨道说明）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Python 为什么是 AI 商业分析的首选

Python 不是最快的语言，也不是最优雅的语言，但它是 AI 和数据科学生态最完整的语言。NumPy（数值计算）、Pandas（表格处理）、Scikit-learn（机器学习）、Statsmodels（统计建模）、Matplotlib/Seaborn（可视化）构成了无缝衔接的工具链。后续技能中的 LangChain（Agent 编排）、DoWhy（因果推断）、PyTorch（深度学习）全部是 Python 库。**选择 Python 不是偏好问题，是生态问题。**

### 关键回顾 2：五大语法要素与营销映射

| 语法要素 | Python 关键字 | 营销数据处理中的应用 |
|---------|-------------|-------------------|
| 变量与数据类型 | int/float/str/bool | 销售额 float、客户ID str（前导零）、是否复购 bool |
| 控制流 | if-elif-else/for/while | 遍历客户列表分群、if 筛选高价值客户 |
| 函数 | def/return/apply | 封装 RFM 分类逻辑、`df.apply()` 向量化清洗 |
| 数据结构 | list/dict/tuple/set | dict 处理 JSON API 返回值、list 存储客户列表 |
| 面向对象 | class/属性/方法 | 设计 Product/Customer 类，理解库 API 的 OO 设计 |

### 关键回顾 3：Pandas DataFrame -- Excel 的程序化版本

Pandas 的两个核心数据结构--Series（一维）和 DataFrame（二维）--覆盖了商业分析中 90% 的数据处理需求。DataFrame 可以理解为 Excel 表格的程序化版本，但能处理百万行级别数据，且支持复杂的筛选、分组、聚合操作。

**核心 API 速查**：

| 操作 | 方法 | 营销场景 |
|------|------|---------|
| 加载数据 | `pd.DataFrame(dict)` / `pd.read_csv()` | 从字典/CSV创建营销数据表 |
| 类型检查 | `df.dtypes` / `df.info()` | 检查客户ID是否被误读为整数 |
| 探索统计 | `df.head()` / `df.describe()` | 查看订单数据分布 |
| 筛选 | `df[df['age'] > 30]` | 筛选高年龄段客户 |
| 分组聚合 | `df.groupby('category').agg(...)` | 按产品类别统计销售 |
| 应用函数 | `df['col'].apply(func)` | 向量化清洗/分类 |
| 文件 IO | `df.to_csv()` / `df.to_json()` | 导出分析结果 |

### 关键回顾 4：RFM 分析 -- 营销中最经典的客户分群方法

RFM 由 Hughes 在 1994 年提出，是营销领域最经典的客户分群方法：

- **R（Recency）**：最近一次购买距今天数 -- 衡量客户活跃度
- **F（Frequency）**：购买次数 -- 衡量客户忠诚度
- **M（Monetary）**：消费总金额 -- 衡量客户价值

三个维度组合可以对客户进行精细化分层（高价值/中等价值/低价值/流失风险）。在 AI 时代，RFM 的三个维度可以被 embedding 替代（后续技能1），但理解 RFM 是理解 embedding 优势的基础。

---

## 上机部分：用真实库处理营销数据

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（pandas + numpy + 营销产品/客户/订单数据）

### 为什么用真实库而非手写脚本

v4.0 的代码用"手写脚本"演示语法概念。v5.0 改用工业级真实库：

- **pandas**（pandas-dev/pandas，43k+ star，BSD-3-Clause）：`pd.DataFrame()` / `df.groupby()` / `df.apply()` -- 工业标准数据分析工具链
- **numpy**（numpy/numpy，27k+ star，BSD-3-Clause）：`np.mean()` / `np.sum()` -- 数值计算基石，pandas 底层依赖

### 营销映射（关键桥接）

本 Day 处理一个"营销数据 Python 处理"场景：8 个产品（护肤/电子/健身三类）、15 个客户、30 笔订单，用 Python + pandas 完成从数据加载到营销指标计算的完整闭环：

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| 数据加载 | 将产品/客户/订单数据加载为 DataFrame | pandas DataFrame |
| 数据探索 | 检查数据类型、查看分布、识别缺失值 | pandas dtypes/describe/info |
| 控制流与函数 | RFM 分类逻辑、客户分层 | Python if-elif-else + apply |
| 类与面向对象 | 设计 Product/Customer 业务对象 | Python class |
| 文件 IO | 读写营销 CSV/JSON | pandas to_csv/read_json |
| 营销指标 | ROI/转化率/客单价/复购率 | pandas + numpy 聚合 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 pandas 将产品/客户/订单数据加载为 DataFrame，打印形状和前 5 行
2. **TODO2**：用 `dtypes`/`head()`/`describe()`/`info()` 探索数据类型与分布，识别潜在数据质量问题
3. **TODO3**：用控制流和函数实现 RFM 客户分类逻辑，用 `apply` 向量化执行
4. **TODO4**：设计 Product 和 Customer 类，包含属性和方法，理解面向对象设计
5. **TODO5**：用 pandas 将分析结果写入 CSV 和 JSON 文件，再读回验证
6. **TODO6**：计算核心营销指标（ROI、转化率、客单价 AOV、复购率）

---

## 2026 前沿补充：pandas 2.x + Apache Arrow + Polars

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① pandas 2.x 的 Apache Arrow 后端 ② Polars 高性能替代 ③ 可复现研究与数据治理。

### pandas 2.x 与 Apache Arrow 内存格式

pandas 2.0（2023年4月发布）引入了基于 **Apache Arrow** 的后端（`dtype_backend="pyarrow"`），这是 pandas 自 2008 年诞生以来最大的架构升级：

- **零拷贝数据交换**：Arrow 后端让 pandas 与其他 Arrow 兼容工具（Polars、DuckDB、Spark）之间可以零拷贝传递数据，避免序列化开销
- **内存效率**：Arrow 的列式存储和字典编码比 NumPy 数组节省 30-50% 内存，对百万行营销数据处理意义重大
- **缺失值处理**：Arrow 原生支持 NaN/NA 区分（NumPy 无法区分 `NaN` 和 `NA`），解决商业数据中"未填写"和"填了0"的混淆问题

**对营销数据处理的启示**：在处理千万级用户行为日志时，pandas 2.x + Arrow 后端可以让内存占用减半，加载速度提升 2-3 倍。这正是数据治理中"基础设施升级"的典型场景。

### Polars：高性能 DataFrame 替代

**Polars**（pola-rs/polars，28k+ star，MIT License）是用 Rust 编写的 DataFrame 库，API 设计参考 pandas 但性能提升 5-30 倍：

- **惰性执行**：Polars 的 `LazyFrame` 支持查询优化器，自动合并/重排操作，避免中间结果物化
- **多线程**：利用 Rust 的零开销抽象和 Rayon 并行库，自动并行化分组聚合
- **流式处理**：支持大于内存的数据集流式处理，不需要分块加载

**何时用 Polars 替代 pandas**：当营销数据超过 1GB（如全量用户行为日志）时，Polars 的性能优势显著。但 pandas 仍是学习首选，因为生态更完整（与 scikit-learn/statsmodels/matplotlib 无缝衔接）。后续技能中的数据预处理可能逐步引入 Polars。

### 可复现研究与数据治理

Python 数据分析的**可复现性**（Reproducibility）是学术研究的基本要求，也是企业数据治理的核心原则：

- **可复现研究**：用 `random_state=42` 固定随机种子、用 `requirements.txt` 锁定依赖版本、用虚拟环境隔离--确保任何人都能复现你的分析结果。APA 和 OSF（Open Science Framework）都要求研究数据可复现。
- **数据治理**：在营销数据中，客户ID的数据类型（str vs int）、日期格式统一、缺失值标记规范，都是数据治理的基本要求。pandas 2.x 的 Arrow 后端通过严格的类型系统（如 `int64` vs `Int64` 可空整数）帮助在数据加载阶段就发现类型问题。

> ⚠️ 可复现性不是可选项。在后续模块R（博士研究方法论）中，你将学习如何用 IMRaD 格式写研究计划，其中 Methods 部分必须包含足够的数据处理细节以供复现。

---

## 与后续 Day 的衔接

- **Day 2**：数据结构与应用--今天的 pandas 基础将扩展到 JSON/API/数据库连接，处理更复杂的嵌套营销数据
- **Day 3**：描述统计与推断统计--今天的描述性统计（mean/median/std）将扩展到假设检验和置信区间
- **Day 4**：回归分析与概率分布--今天的数据加载和清洗技能是回归分析的前置条件
- **Day 5**：数据治理与 SQL--今天的数据类型检查和文件 IO 将扩展到数据库 Schema 设计和 SQL 查询

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 1 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的营销数据在探索性分析中发现了什么数据质量问题？RFM 分层后各层级客户占比如何？ROI 最高的产品是哪个？
- [ ] （可选）将本 Day 的营销数据处理流程封装为一个 Python 模块（`.py` 文件），包含数据加载、清洗、分析、导出四个函数

---

## 英语轨道（i+1）

打开 [Python Official Tutorial](https://docs.python.org/3/tutorial/introduction.html)，用浏览器翻译插件辅助阅读。不要求读懂每个词，目标是理解代码示例和段落大意。遇到 Python 术语（interpreter、variable、expression），记住英文形式--这些术语在后续所有技术文档中会反复出现。这就是 i+1：你已有中文编程基础（i），通过英文文档接触新表达方式（i+1）。

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pandas + numpy）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 真实库 + TODO 脚手架之上, 注入学习科学四件套: 刻意练习 (Ericsson) / 间隔重复 (FSRS-6 + SM-2 备份) / 建构对齐 (Biggs ILO↔TLA↔AT) / 牛津 tutorial (Socratic + Hattie 四级反馈)。目标是把"练习"升级为"高效刻意练习 + mastery 阈值 + Worked-Faded 渐退示例 + interleaving 交叉练习 + 提取练习", 在不破坏 v5.0 基线的前提下提升单位练习时间的保留率。

### 1. 刻意练习 (Ericsson deliberate practice, 5 要素)
本单元的 `practice.md` 把 v5.0 的 6 个 TODO 重组为 3 个 drill (D1 加载/dtype治理, D2 RFM+apply 向量化, D3 营销指标+IO+Arrow 前沿), 每个 drill 含 difficulty 1-5 / reps_required / feedback_rule / worked-faded 三阶段 (完整示范 -> 部分填空 -> 独立解)。feedback_rule 引用本单元真实库 API (pandas dtypes / numpy np.select / Arrow dtype_backend), 不直接给代码。连续 2 次失败触发 weak_loop: 回退到上一 drill + 重走 worked example。

### 2. 间隔重复 (FSRS-6 algorithm, request_retention=0.9, SM-2 backup)
`schedule.json` 用 FSRS-6 算法 (21 weights, request_retention=0.9), SM-2 备份 (EF0=2.5, I(1)=1, I(2)=6)。4 张卡片覆盖本单元核心概念: C1 pandas dtype 治理 (前导零), C2 RFM + apply 向量化, C3 pandas 2.x Arrow vs Polars LazyFrame, C4 营销指标 + 可复现 IO。每卡片 due 间隔 [1, 3, 8, 21, 60, 180] 天。Butler 2010 证据: 间隔重复 + 提取练习 (retrieval practice) 比重学保留率高 24 个百分点 (68% vs 44%)。

### 3. 交叉练习 (interleaving, MIT Open Learning 模式)
`practice.md` 的 interleaving 序列 A1B1C1...B2C2A2...C3A3B3 强迫大脑每次重新检索"现在该用哪个 API", 而非块状练习的机械重复。三轮之间隔 1 天, 与 schedule.json FSRS-6 间隔对齐。交叉练习比块状练习在 1 周后保留率高 43%。

### 4. 建构对齐 (Biggs constructive alignment, ILO↔TLA↔AT)
`alignment.md` 用 Biggs 矩阵把本单元 3 个 ILO (加载/RFM/指标+前沿) 与 TLA (starter.ipynb 填空 + practice.md drill + tutorial.ipynb Socratic + schedule.json 复习) 和 AT (solution.ipynb + tutorial 后测 + progressive_project) 一一对应, 每行设 mastery_threshold >=80%。3 个自检问题 (Feed Up / Feed Back / Feed Forward) 防止"不经 TLA 能过 AT"的对齐失败。

### 5. 牛津 tutorial (Socratic + Hattie 四级反馈)
`tutorial.ipynb` 仿真牛津 tutorial fellow (1对1, 每周, 强制口头辩护), persona 明确: 不直接给答案 / Socratic 追问 / HBS devil's advocate / 每轮以 probing question 结束。5 轮静态 if/else Socratic loop (不调 LLM API) 覆盖 4 个 ILO, 每轮检测 defense 失败则降一级 scaffold。Hattie 四级反馈 [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD] 避免 Self 级表扬 (Hattie 2007 RER 77(1):81-112, Self 级 d≈0.09 近零)。student_model.json 跨单元复用, 记录掌握度/盲点/弱项 drill。限频 1 次/天防 LLM 依赖, 退出时交 2-3 盲点 + 推荐复习单元的 exit artifact。

### 6. Worked-Faded 与 mastery
Worked-Faded 渐退示例 (完整示范 -> 部分填空 -> 独立解) 出现在每个 drill 的三阶段中, 对应 v5.0 starter.ipynb (faded) 与 solution.ipynb (worked) 的对应关系。mastery 阈值 >=80% (alignment.md) + 连 2 次失败 weak_loop (practice.md) + FSRS-6 schedule.json 间隔复习, 三者构成"练习-检测-反馈-复习"闭环。Worked-Faded 渐退示例 + 交叉练习 + 提取练习 + 间隔重复 四者协同, 把 v5.0 的"练了就行"升级为"科学练就掌握"。

---

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM-as-data-analyst × Polars/duckdb 列式引擎。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
