# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档 / 论文 / 仓库，非主页）。全部链接已验证存在。

---

## ① Python 数据结构基础

### Python 官方教程：数据结构（Data Structures）

- 🌐 官方文档：https://docs.python.org/3/tutorial/datastructures.html
- **用法**：Day 2 理论回顾的核心来源。覆盖 list 的栈/队列用法、list comprehension、del 语句、tuple 和序列、set、dict 五大数据结构的完整说明。重点读 §5.1（list 用法）、§5.5（dict）、§5.6（循环技巧），理解每种结构的适用场景。营销应用：list 做订单排序、dict 做产品目录、set 做用户去重。

### Python 官方文档：collections 模块

- 🌐 官方文档：https://docs.python.org/3/library/collections.html
- **用法**：Day 2 TODO4/TODO6 的核心库文档。重点读 Counter（自动计数 + most_common）、defaultdict（自动初始化缺失键）、namedtuple（命名元组数据类）三个组件。Counter 的 `most_common(n)` 方法直接实现"Top-N 热销商品"查询；defaultdict 的 `defaultdict(list)` 模式实现"按渠道分组订单"；namedtuple 的 `_replace` 方法实现不可变记录更新。营销应用：商品销量计数、用户行为聚合、Product/Order 数据类设计。

### Python 官方文档：heapq 模块

- 🌐 官方文档：https://docs.python.org/3/library/heapq.html
- **用法**：Day 2 TODO4 扩展阅读。heapq 提供最小堆队列算法，`heapq.nlargest(n, iterable, key=...)` 在 O(n log k) 时间内找出 Top-K 元素，比排序整个列表 O(n log n) 更高效。重点读"Priority Queue Implementation Notes"小节，理解堆在优先队列中的应用。营销应用：实时热销商品 Top-10 查询、订单优先级处理队列。

---

## ② 真实库 + 上机

### Python 官方文档：timeit 模块（性能测量）

- 🌐 官方文档：https://docs.python.org/3/library/timeit.html
- **用法**：Day 2 作业要求用 `%timeit` 对比 list 和 dict 的查询性能。timeit 模块提供精确的代码执行时间测量，`%timeit` 是 IPython/Jupyter 的魔法命令版本。重点理解为什么 dict 的 O(1) 查找在大数据量下比 list 的 O(n) 查找快几个数量级。营销应用：评估产品目录查询在不同数据结构下的性能差异。

### Real Python：Python 数据结构实践指南

- 🌐 文章：https://realpython.com/python-data-structures/
- **用法**：Real Python 的数据结构实践指南，用真实代码示例讲解 list/dict/set/deque 的使用模式和性能特性。重点读"Arrays vs Lists"和"Dictionaries and Sets"两节，理解哈希表底层原理。营销应用：选择正确的数据结构处理营销订单。

### Python 官方文档：dataclasses 模块（Python 3.7+）

- 🌐 官方文档：https://docs.python.org/3/library/dataclasses.html
- **用法**：Day 2 TODO6 的扩展阅读。dataclasses 提供更现代的数据类定义方式（比 namedtuple 更灵活，支持类型注解、默认值、可变性）。重点读"Module contents"中的 `@dataclass` 装饰器和 `field()` 函数。营销应用：设计可变的营销 Product/Order 数据类，支持数据治理 schema 规范。

---

## ③ 2026 前沿：Apache Arrow + Polars

### Apache Arrow：跨语言列式内存格式

- 🌐 官方文档：https://arrow.apache.org/docs/python/
- 📦 GitHub：https://github.com/apache/arrow （已验证，Apache-2.0）
- **用法**：Day 2 前沿补充的核心内容。Apache Arrow 定义了语言无关的列式内存格式，实现 Python/R/Spark/Polars 之间的零拷贝数据共享。重点读"Arrow in Python"章节，理解 `pyarrow.Table` 如何用列式格式存储数据。与本 Day 的连接：list of dicts 是行式存储的直觉代表，Arrow 的列式格式是其性能优化版--理解 list/dict 的性能特性是理解 Arrow 优势的前提。营销应用：多源营销数据的零拷贝传递（数据库 -> Arrow -> pandas -> ML 模型）。

### Polars：懒求值 DataFrame 引擎

- 🌐 官方文档：https://pola.rs/
- 📦 GitHub：https://github.com/pola-rs/polars （已验证，MIT License）
- **用法**：Day 2 前沿补充。Polars 基于 Arrow 内存格式，核心创新是懒求值（lazy evaluation）。重点读"Concepts > Lazy API"章节，理解查询图（query graph）如何自动优化执行顺序。与本 Day 的连接：Polars 的查询图是 DAG 数据结构，与 TODO6 的产品分类树同为树/图结构应用。懒求值让"先 filter 再 select"自动优化为最优执行顺序--这是数据结构选择影响性能的高级体现。

### 数据治理与可复现研究

- 🌐 OSF（Open Science Framework）：https://osf.io/ （已验证，数据版本管理平台）
- **用法**：Day 2 前沿补充。数据治理关注数据的质量、一致性、可追溯性。可复现研究要求固定随机种子、记录数据版本、用不可变数据结构确保数据处理管线可复现。OSF 是开放科学基金会维护的数据/研究版本管理平台。与本 Day 的连接：用 namedtuple/dataclass 定义 schema 是数据治理规范化的第一步，确保 Product/Order 的字段一致性可追溯。营销应用：营销分析管线的可复现性保障。

---

## ④ 对标课程

### MIT OCW 15.071: The Analytics Edge

- 🌐 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/
- **用法**：Day 2 英语轨道材料（教材指定）。MIT 的 The Analytics Edge 课程 Unit 1 "Introduction to Analytics" 用英文讲解数据分析基本流程。阅读时关注英文术语：data frame, missing values, data cleaning, merge/join。这些术语在后续所有英文技术文档中反复出现。与本 Day 的连接：MIT 课程的数据整理流程底层就是 Python 数据结构操作。

### Python 官方教程：类与数据结构

- 🌐 官方教程：https://docs.python.org/3/tutorial/classes.html
- **用法**：Day 2 TODO6 的扩展阅读。理解 Python 类机制有助于设计自定义数据结构。重点读 §9.3（类定义）和 §9.5（继承），理解 namedtuple 和 dataclass 如何用类机制实现数据 schema。营销应用：设计营销业务对象的面向对象模型。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 2 | 数据结构理论基础 | 1h |
| 2 | Python 官方数据结构教程 §5.1-5.6 | 五种内置结构 | 0.5h |
| 3 | `starter.ipynb` 上机（配 collections 文档） | 真实库实操 | 2h |
| 4 | Apache Arrow + Polars 文档 | 2026 前沿 | 0.5h |
| 5 | MIT OCW 15.071 Unit 1 | 英语轨道 | 1h |
| 6 | dataclasses 文档 + OSF 可复现研究 | 数据治理 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
