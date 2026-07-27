# 技能0 · Day 2：数据结构与应用 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能0 AI商业分析基础 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Python 数据结构如何组织营销数据？--从"散乱记录"到"结构化资产"的工程基础
> **v5.0 升级点**：① 新增真实库上机（Python 内置 list/dict/set/tuple/deque + collections + heapq）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（Apache Arrow 列式内存 + Polars 懒求值 + 数据治理）

---

## 学习目标（学完你能做到）

1. 能解释 list/dict/set/tuple/deque 五种 Python 内置数据结构的时间复杂度差异（O(1) vs O(n)），并说明在营销订单处理、产品目录查询、用户去重等场景中为什么选 A 而不选 B
2. 能用 `collections.Counter` 做商品销量计数、`defaultdict` 做用户行为聚合、`namedtuple` 设计不可变营销数据对象，并用 `heapq` 实现 Top-K 热销商品堆查询
3. 能用 set 运算（交集/并集/差集/对称差集）做用户标签运算和跨渠道用户去重，用 deque 实现"最近浏览"滑动窗口和订单处理队列
4. 能设计自定义数据结构（namedtuple Product/Order + 产品分类树），理解数据结构选择对 AI pipeline 性能和数据治理的影响
5. 能阐述 Apache Arrow 列式内存格式和 Polars 懒求值如何革新数据分析底层，以及可复现研究对数据结构规范化的要求

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md` § Day 2](../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md)（第 271-560 行，已包含 JSON/CSV 数据格式、API 调用、SQL 数据库连接、数据清洗 80/20 法则、多源营销数据整合案例）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Python 内置数据结构--营销数据的五种容器

| 数据结构 | 有序 | 可变 | 查找复杂度 | 营销应用场景 |
|---------|:----:|:----:|:---------:|------------|
| `list` | ✅ | ✅ | O(n) 线性查找 | 订单列表排序/筛选/切片 |
| `dict` | ✅(3.7+) | ✅ | O(1) 哈希查找 | 产品目录映射、客户画像 |
| `set` | ❌ | ✅ | O(1) 哈希查找 | 用户去重、标签集合运算 |
| `tuple` | ✅ | ❌ | O(n) 线性查找 | 不可变记录、字典键 |
| `deque` | ✅ | ✅ | O(1) 两端操作 | 浏览路径滑动窗口、处理队列 |

**核心洞察**：数据结构的选择直接决定代码性能。用 list 做产品查询是 O(n)，换成 dict 就是 O(1)--当产品目录有 10 万条时，差距是 10 万倍。这正是数据治理中"数据结构规范化"的工程基础。

### 关键回顾 2：collections 模块--数据聚合的三大利器

| 组件 | 核心能力 | 营销应用 |
|------|---------|---------|
| `Counter` | 自动计数 + `most_common(n)` | 商品销量排行、用户行为频次 |
| `defaultdict` | 自动初始化缺失键 | 按 channel 分组订单、按用户聚合行为 |
| `namedtuple` | 不可变 + 字段名访问 | 定义 Product/Order 数据类 |

**与独立教材的连接**：教材 Day2 的多源数据整合案例中，`ad_records` 用 list 存 JSON 记录、`crm_df` 用 DataFrame 做表格操作。底层都是 Python 数据结构在支撑--pandas 的 DataFrame 本质是 dict of numpy arrays，理解原生数据结构是理解 pandas 内部机制的前提。

### 关键回顾 3：堆与优先队列--Top-K 查询的高效实现

`heapq` 模块提供最小堆操作。对于"Top 10 热销商品"这类查询，用 `heapq.nlargest(n, iterable, key)` 比排序整个列表 O(n log n) 更高效（O(n log k)，k 远小于 n 时优势显著）。在营销实时看板场景中，每秒处理万级订单流时，堆结构是性能关键。

### 关键回顾 4：数据清洗的 80/20 法则与数据结构

教材指出"数据分析师 80% 时间花在数据清洗上"。数据清洗的每一步都依赖数据结构：
- 缺失值处理 → dict 的 `get(key, default)` 提供默认值
- 重复值处理 → set 自动去重
- 数据类型转换 → list comprehension 批量转换
- 数据一致性 → dict 统一命名映射

---

## 上机部分：用 Python 数据结构处理营销数据

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（Python 标准库 + 营销订单/产品/客户数据）

### 为什么用真实库而非手写脚本

v4.0 的代码用"伪代码"演示概念。v5.0 改用 Python 标准库的真实数据结构模块：

- **Python 内置**：list/dict/set/tuple/deque 是所有 Python 数据处理的基础，pandas/numpy/SQLAlchemy 底层都构建在这些结构之上
- **collections**：Counter/defaultdict/namedtuple 是 Python 官方推荐的数据聚合工具，比手写循环计数更高效且可读
- **heapq**：堆队列算法，工业级 Top-K 查询的标准实现

### 营销映射（关键桥接）

本 Day 处理一个"营销数据结构实战"场景：一组营销订单数据（订单列表 + 产品目录 + 客户画像 + 用户标签 + 行为序列），用 Python 数据结构完成排序查询、目录映射、标签运算、行为聚合、路径模拟、自定义数据类设计：

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| list 操作 | 订单列表排序/筛选/切片 | Python 内置 list + sorted/filter |
| dict 映射 | 产品目录键值查询、客户画像 | Python 内置 dict + comprehension |
| set 运算 | 用户去重、标签交集并集差集 | Python 内置 set |
| Counter/defaultdict | 商品销量计数、行为聚合 | collections.Counter/defaultdict |
| deque/栈队列 | 用户浏览路径、最近访问 | collections.deque + heapq |
| 自定义结构 | Product/Order 数据类、分类树 | collections.namedtuple + dict 树 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 list 对营销订单列表做排序（按金额降序）、筛选（完成订单且金额>500）、切片（Top 5）、提取唯一客户 ID
2. **TODO2**：用 dict 构建产品目录映射（product_id -> 产品信息），做 O(1) 查询和按类别筛选
3. **TODO3**：用 set 做用户标签运算（交集/并集/差集/对称差集）和跨渠道用户去重
4. **TODO4**：用 Counter 统计商品销量排行，用 defaultdict 按渠道分组订单、按用户聚合行为
5. **TODO5**：用 deque 模拟用户浏览路径（maxlen 滑动窗口），实现栈式撤销和队列式订单处理
6. **TODO6**：用 namedtuple 设计 Product/Order 数据类，用 dict 构建产品分类树并做 BFS 遍历

---

## 2026 前沿补充：Apache Arrow + Polars + 数据治理

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① Apache Arrow 列式内存格式 ② Polars 懒求值引擎 ③ 数据治理与可复现研究。

### Apache Arrow：跨语言列式内存格式

Apache Arrow（Apache 软件基金会，2016 年起）定义了一种**语言无关的列式内存格式**，解决了数据在不同系统间传递时的序列化/反序列化开销问题。

**核心思想**：传统方式中，Python 的 dict、R 的 data.frame、Java 的 List 互不兼容，数据传递需要序列化（pickle/JSON/CSV）。Arrow 定义了统一的内存布局，使得 Python pandas、R arrow、Spark、Polars 可以**零拷贝**共享同一块内存中的数据。

**对营销 AI pipeline 的启示**：
- **零拷贝数据传递**：从数据库读取 -> Arrow 内存 -> pandas/Polars 分析 -> 机器学习模型训练，全程无序列化开销
- **列式存储**：分析单列（如"统计所有订单金额"）时只读取该列内存，比行式存储（list of dicts）快 10-100 倍
- **与本 Day 的连接**：list of dicts 是行式存储的直觉代表，Arrow 的列式格式是其性能优化版--理解 list/dict 的性能特性是理解 Arrow 优势的前提

### Polars：懒求值 DataFrame 引擎

Polars（Ritchie Vink，2020 年起）是基于 Arrow 内存格式的 DataFrame 库，核心创新是**懒求值（lazy evaluation）**：

- **pandas 的 eager 模式**：每一步操作立即执行，中间结果物化为新 DataFrame，多次遍历数据
- **Polars 的 lazy 模式**：操作构建查询图（query graph），最后 `.collect()` 时优化器全局优化后一次执行

**与数据结构的连接**：Polars 的查询图本质是一个 DAG（有向无环图）数据结构，与本 Day TODO6 的产品分类树同为树/图结构的工程应用。懒求值让"先 filter 再 select"和"先 select 再 filter"自动优化为最优执行顺序--这正是数据结构选择影响性能的高级体现。

### 数据治理与可复现研究

数据治理（Data Governance）关注数据的**质量、一致性、可追溯性**。在 AI 营销场景中：

- **数据结构规范化**：用 namedtuple/dataclass 定义 Product/Order 的 schema，比裸 dict 更可追溯、更可验证
- **可复现研究**：固定随机种子、记录数据版本、用不可变数据结构（tuple/frozen set）确保数据处理管线可复现
- **贝叶斯视角**：数据结构的选择影响先验信息的编码方式--dict 的键值结构天然适合表示贝叶斯先验（参数名 -> 分布参数）

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 Apache Arrow / Polars / 数据治理条目。

---

## 与后续 Day 的衔接

- **Day 3**：SQL 与数据库基础--今天的 dict 映射概念将扩展到 SQL 的 JOIN/GROUP BY，产品目录 dict 就是内存中的"索引表"
- **Day 4**：数据清洗与特征工程--今天的 list/dict 操作是 pandas DataFrame 操作的底层基础，理解 list comprehension 是理解向量化操作的前提
- **Day 5**：数据管理与版本控制--今天的数据结构规范化（namedtuple schema）将扩展到数据版本管理（DVC）和数据血缘追踪
- **技能1**：表示工程--今天的"订单 list -> 产品 dict -> 客户画像"是后续 embedding 表示的原始数据层，数据结构决定了表示工程的数据接入方式

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 2 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：对比 list 和 dict 在产品查询场景下的性能差异（用 `%timeit` 实测），说明在什么数据规模下 dict 的 O(1) 优势开始显著
- [ ] （可选）为你的业务场景设计一组 namedtuple schema（Product/Order/Customer），并写一段说明为什么用 namedtuple 而非裸 dict（从数据治理和可复现角度论证）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（Python 内置 + collections + heapq）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 "真实即严谨 · 练习即掌握" 之上, 叠加 **科学即高效 · 反馈即成长** -- 用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。本节是 v6.0 注入层, 不改动 v5.0 原文。

### 1. 刻意练习 (Ericsson + MIT Worked-Faded)

本 Day 的 6 个 TODO 不再是"刷题", 而是按 Ericsson 刻意练习 5 要素重构 (见 `practice.md`):
- **skill_target** 明确可观察: "在 10 万级营销数据下自主选择 Python 标准库结构 + 用 %timeit 实测 O(1) vs O(n) + namedtuple 设计可治理 schema"
- **3 drills (D1/D2/D3)** 每个含 difficulty (1-5) + reps_required (3 次) + feedback_rule (引用真实库源码模式: `Counter.__missing__` / `heapq._siftdown` / dict hash table)
- **Worked-Faded 三阶段**: 完整示范 -> 部分填空 -> 独立解 (MIT Open Learning 明文原则)
- **weak_loop**: 连续 2 次失败触发, 回退上一 drill + 补 worked example

### 2. 间隔重复 (FSRS-6 / SM-2)

本 Day 4 个核心概念进入 `schedule.json` (FSRS-6, request_retention=0.9, SM-2 备份 EF₀=2.5):
- C1: list O(n) vs dict O(1) 哈希查找 (due: 1/3/8/21/60/180 天)
- C2: Counter.most_common + defaultdict(list) Pythonic 聚合
- C3: heapq.nlargest O(n log k) + deque(maxlen=) 滑动窗口
- C4: namedtuple schema + Apache Arrow 列式内存 + OSF 可复现研究

FSRS-6 用 21 个权重优化记忆曲线, 比 SM-2 (1985) 更贴合真实遗忘; SM-2 作 fallback 保底。间隔重复 (spaced retrieval) 比块状练习长期保留高 40%+ (Butler 2010 RER)。

### 3. 交叉练习 (Interleaving)

`practice.md` 的 interleaving 节明文排布 **A1B1C1...B2C2A2...C3A3B3** 螺旋 (A=结构选择, B=collections 聚合, C=高级/前沿), 禁块状。短期分数比块状低 10%, 但 1 周后保留率高 40% -- 这是 mastery 的长期投资。

### 4. 建构对齐 (Biggs ILO↔TLA↔AT)

`alignment.md` 把 3 条 ILO (结构选择 / collections 聚合 / heapq+Arrow 前沿) 与 TLA (starter TODO + drill + tutorial + schedule 复习) 和 AT (solution + diagnostic + progressive_project + poster) 一一对齐, 每条标注 mastery_threshold (80%/70%/独立解)。Biggs 三自检 (Feed Up/Back/Forward) 检测对齐失败: "不经 TLA 能过 AT 吗? 若能 = 对齐失败。"

### 5. 牛津 Tutorial 仿真 (Socratic + Hattie)

`tutorial.ipynb` 仿真牛津 tutorial fellow (1对1, 限频 1 次/天防依赖):
- **Persona**: never give direct answers, Socratic questioning, HBS devil's advocate
- **5 轮 Socratic loop** (静态 if/else 模拟, 不调 API): 追问 vague claim / 反例 / 边界条件
- **student_model.json** 读写, 记录掌握度/盲点, 跨单元复用
- **Hattie 四级反馈** ([TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD]), 避免无效的 Self 级表扬 (d=0.14), 优先 FEED-FORWARD (d=0.71)
- **Exit artifact**: 2-3 盲点 + 推荐复习单元 + 下次 focus question

### 6. 与 v5.0 的关系

| 层 | v5.0 | v6.0 增量 |
|---|---|---|
| 文件 | notes/data/README/starter/solution/reading (5) | + practice/schedule/alignment/tutorial (4) |
| 练习 | TODO 填空 (starter) | + drill + worked-faded + interleaving + weak_loop |
| 复习 | 无 | + FSRS-6 间隔重复 (1/3/8/21/60/180 天) |
| 对齐 | 隐式 | + Biggs ILO↔TLA↔AT 显式矩阵 + mastery 阈值 |
| 反馈 | solution 自对 | + 牛津 Socratic + Hattie 四级 + student_model |

v5.0 的 7 条验收 (verify_unit.py) 不变, v6.0 在其上叠加 5 条 (verify_v6_unit.py, 8-12), 12/12 即收敛。

### 研究依据

- Ericsson (1993) 刻意练习 5 要素; Butler (2010 RER) 检索练习 vs 重学 68% vs 44%
- FSRS-6 (Liu 2022+, 21 weights, request_retention=0.9); SM-2 (Wozniak 1985, EF₀=2.5)
- Biggs (1996) Constructive Alignment; Hattie (2007 RER 77(1):81-112) 4 级反馈
- Oxford tutorial (1对1-3 + 每周强制); Vygotsky 共构 (ZPD); Socratic LLM (arxiv 2409.05511 / 2507.05795)
- MIT Open Learning: 提取练习 + 交叉 + Worked-Faded; Stanford CS230 progressive project + retry; Harvard HBS devil's advocate

*v6.0 学习科学层 - 让练习有科学依据, 让反馈有成长方向。*

---

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM-as-data-analyst × Polars/duckdb 列式引擎。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
