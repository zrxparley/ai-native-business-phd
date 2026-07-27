# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档 / 教程 / 仓库，非主页）。全部链接已验证存在。

---

## ① Python 基础语法

### Python Official Tutorial（已验证）
- 🌐 官方教程：https://docs.python.org/3/tutorial/introduction.html
- **用法**：Day 1 英语轨道材料。重点读 Chapter 3（An Informal Introduction to Python）和 Chapter 4（More Control Flow Tools），理解变量/表达式/控制流/函数的英文术语。这就是 i+1：你已有中文编程基础（i），通过英文官方文档接触新表达方式（i+1）。
- **深链用法**：
  - [Chapter 3.1: Numbers, strings, lists](https://docs.python.org/3/tutorial/introduction.html#lists)：对标 TODO2 数据类型
  - [Chapter 4.1: if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)：对标 TODO3 控制流
  - [Chapter 4.6: Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)：对标 TODO3 函数定义

### Python Official Tutorial: Classes（已验证）
- 🌐 官方教程：https://docs.python.org/3/tutorial/classes.html
- **用法**：Day 1 TODO4 的核心阅读。Python 面向对象编程的官方指南，重点读 §9.2（Python Scopes and Namespaces）和 §9.3（A First Look at Classes），理解 `class`/`__init__`/`self`/属性/方法的概念。在营销场景中，Product 和 Customer 类的设计需要理解构造函数和实例方法。

---

## ② 真实库：pandas + numpy

### pandas 官方文档与教程（已验证）
- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD-3-Clause）
- 📦 GitHub：https://github.com/pandas-dev/pandas （43k+ star，已验证存在）
- **深链用法**：
  - [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)：对标 TODO1/TODO2，快速上手 DataFrame 操作
  - [DataFrame.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)：对标 TODO2，理解数据类型检查
  - [groupby 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)：对标 TODO6，分组聚合计算营销指标
  - [pandas 2.0 release notes](https://pandas.pydata.org/docs/whatsnew/v2.0.0.html)：2026 前沿--Apache Arrow 后端

### numpy 官方文档（已验证）
- 🌐 官方文档：https://numpy.org/doc/stable/ （已验证，BSD-3-Clause）
- 📦 GitHub：https://github.com/numpy/numpy （27k+ star，已验证）
- **深链用法**：
  - [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)：对标 TODO6，理解 ndarray 数值计算
  - [numpy.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)：计算平均消费金额

---

## ③ 2026 前沿：pandas 2.x + Apache Arrow + Polars

### Apache Arrow 项目（已验证）
- 🌐 官方网站：https://arrow.apache.org/ （已验证，Apache-2.0）
- 📦 GitHub：https://github.com/apache/arrow （已验证，活跃维护）
- **用法**：pandas 2.0 引入的 Arrow 后端是 Day 1 的前沿补充。Apache Arrow 是跨语言的列式内存格式，让 pandas 与 Polars/DuckDB/Spark 之间零拷贝交换数据。重点理解 Arrow 的列式存储和字典编码如何节省 30-50% 内存。对营销数据处理的启示：处理千万级用户行为日志时，Arrow 后端可以让内存占用减半。

### Polars：高性能 DataFrame 替代（已验证）
- 🌐 官方文档：https://pola.rs/ （已验证，MIT License）
- 📦 GitHub：https://github.com/pola-rs/polars （28k+ star，已验证）
- **用法**：Polars 是用 Rust 编写的 DataFrame 库，API 设计参考 pandas 但性能提升 5-30 倍。重点理解 LazyFrame（惰性执行）和查询优化器的概念。何时用 Polars 替代 pandas：当营销数据超过 1GB（如全量用户行为日志）时，Polars 的性能优势显著。但 pandas 仍是学习首选，因为生态更完整。

### pandas 2.x 与可复现研究
- 📄 McKinney et al. (2024)："Apache Arrow and the Future of Data Frames"，PyData
- **用法**：Wes McKinney（pandas 创始人）关于 Arrow 后端的设计理念。可复现研究要求用 `random_state` 固定随机种子、用 `requirements.txt` 锁定版本。pandas 2.x 的严格类型系统（`int64` vs `Int64` 可空整数）帮助在数据加载阶段就发现类型问题，是数据治理的基础。

---

## ④ 营销分析方法论

### RFM 客户分群方法
- 📄 Hughes, A. (1996)："The Complete Database Marketer"，McGraw-Hill
- **用法**：Day 1 TODO3 的理论基础。RFM（Recency, Frequency, Monetary）是营销领域最经典的客户分群方法，由 Hughes 在 1994-1996 年提出。R 衡量客户活跃度，F 衡量忠诚度，M 衡量价值。在 AI 时代，RFM 的三个维度可以被 embedding 替代（后续技能1），但理解 RFM 是理解 embedding 优势的基础。

### 营销指标定义
- 🌐 Shopify: Average Order Value (AOV)：https://www.shopify.com/blog/average-order-value
- **用法**：Day 1 TODO6 中营销指标计算的参考。AOV（客单价）= 总收入 / 订单数，是电商营销的核心 KPI。ROI（投资回报率）= (收益 - 成本) / 成本，衡量营销活动盈利能力。复购率 = 复购客户数 / 总客户数，衡量客户忠诚度。

---

## ⑤ 对标课程

### MIT OCW 15.071: The Analytics Edge（已验证）
- 🌐 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/
- **用法**：Day 1 的标杆课程。MIT 15.071 的 Unit 1 从描述性统计和数据分析开始，与本 Day 的 pandas 数据探索对标。英语轨道材料：读 Unit 1 的英文讲义，重点关注数据结构和基础统计的概念。

### Khan Academy: Statistics and Probability（已验证）
- 🌐 课程主页：https://www.khanacademy.org/math/statistics-probability
- **用法**：Day 1 统计基础的英语轨道补充。重点复习 Descriptive Statistics（均值/中位数/标准差），为 Day 3-4 的统计推断打基础。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 1 | Python 基础理论 | 1h |
| 2 | Python Official Tutorial Ch.3-4（选读） | 英语轨道 + 语法巩固 | 0.5h |
| 3 | `starter.ipynb` 上机（配 pandas 10min 教程） | 真实库实操 | 2h |
| 4 | pandas 2.0 release notes + Apache Arrow 概念 | 2026 前沿 | 0.5h |
| 5 | MIT OCW 15.071 Unit 1（选读） | 英语轨道 + 对标课程 | 1h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
