# Day 2 真实数据与库说明

> v5.0 核心升级：用 **Python 标准库真实数据结构**（list/dict/set/tuple/deque + collections + heapq）+ **真实营销数据**替代伪代码演示。Python 内置数据结构是 pandas/numpy/SQLAlchemy 等所有数据科学库的底层基础，理解原生结构是理解高级库内部机制的前提。

---

## 主库：Python 内置数据结构（已验证，开箱即用）

**这是什么**：Python 内置的 list、dict、set、tuple、deque 是所有 Python 数据处理的基石。它们由 CPython 用 C 实现，是 Python 生态中最底层、最稳定的数据容器。pandas 的 DataFrame 本质是 dict of numpy arrays，SQLAlchemy 的查询结果是 list of tuples，所有数据科学库都构建在这些结构之上。

**为什么用它**：
- **零安装**：Python 标准库，无需 pip install，开箱即用
- **性能基石**：dict/set 的 O(1) 哈希查找是所有索引操作的底层实现
- **真实工业基础**：pandas、numpy、Polars、DuckDB 底层都基于这些结构
- **可复现**：标准库无版本漂移风险，确保数据处理管线可复现

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| list | 内置（无需导入） | 有序可变序列，订单列表排序/筛选/切片 |
| dict | 内置（无需导入） | 键值映射，产品目录 O(1) 查询 |
| set | 内置（无需导入） | 无序唯一集合，用户去重、标签运算 |
| tuple | 内置（无需导入） | 不可变序列，字典键、记录 |
| deque | `from collections import deque` | 双端队列，浏览路径滑动窗口 |
| Counter | `from collections import Counter` | 自动计数，商品销量排行 |
| defaultdict | `from collections import defaultdict` | 自动初始化缺失键，按渠道分组 |
| namedtuple | `from collections import namedtuple` | 不可变命名元组，Product/Order 数据类 |
| heapq | `import heapq` | 堆队列，Top-K 热销商品查询 |

**来源与验证**：
- Python 官方文档（数据结构）：https://docs.python.org/3/tutorial/datastructures.html （已验证，Python 3.12+ 标准库）
- Python 官方文档（collections 模块）：https://docs.python.org/3/library/collections.html （已验证，含 Counter/defaultdict/namedtuple 完整 API）

---

## 辅助库：heapq + 数据验证工具

### heapq（堆队列算法）

**安装**：无需安装，Python 标准库

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| heapq.nlargest | `import heapq` | Top-N 热销商品（TODO4 扩展） |
| heapq.nsmallest | `import heapq` | Bottom-N 低频商品 |
| heapq.heappush/heappop | `import heapq` | 优先队列实现 |

- 官方文档：https://docs.python.org/3/library/heapq.html （已验证）

### typing（类型注解，可选）

**安装**：无需安装，Python 3.5+ 标准库

用于给 namedtuple 和 dataclass 添加类型注解，提升代码可读性和数据治理规范度。

---

## 数据：营销订单数据集（内嵌于 notebook）

本 Day 使用一组真实营销场景的数据，直接内嵌在 `starter.ipynb` 和 `solution.ipynb` 中，无需外部下载：

### 1. 订单列表（list of dicts）

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| order_id | str | 订单编号 | "ORD001" |
| customer_id | str | 客户编号 | "C001" |
| product_id | str | 产品编号 | "P101" |
| amount | float | 订单金额 | 1299.00 |
| date | str | 下单日期 | "2025-06-15" |
| channel | str | 下单渠道 | app/web/mini_program/store |
| status | str | 订单状态 | completed/pending/cancelled/refunded |

共 15 条订单记录，覆盖 6 个客户、8 个产品、4 种渠道、4 种状态。

### 2. 产品目录（dict）

product_id -> {name, category, price, stock} 映射，覆盖电子产品、护肤、健身三个类别。

### 3. 客户画像（dict）

customer_id -> {name, level, region, age} 映射，覆盖金卡/银卡/普通三个等级、华北/华东/华南三个区域。

### 4. 用户标签（dict of sets）

customer_id -> set of tags，每个客户 3-5 个行为标签（如"高频"、"电子"、"高消费"、"APP用户"）。

### 5. 用户行为序列（list of tuples）

(customer_id, action, product_id, timestamp) 四元组列表，模拟用户浏览/点击/收藏/购买行为序列。

> 💡 **数据来源说明**：这些数据模拟真实电商平台的营销数据。在实际项目中，你可以从业务数据库用 SQL 查询真实订单数据，或用 pandas 从 CSV/JSON 加载。本上机用内嵌数据确保开箱即用，同时保持与真实数据结构的一致性。

---

## 可选扩展：pandas + Apache Arrow

如果需要处理更大规模的营销数据，可以用 pandas（Day 4 将深入学习）或 Polars：

```bash
pip install pandas polars pyarrow
```

```python
import pandas as pd
# 用 DataFrame 替代 list of dicts 处理订单
orders_df = pd.DataFrame(orders)
# 按 channel 分组统计
channel_stats = orders_df.groupby('channel')['amount'].agg(['count', 'sum', 'mean'])
```

- pandas 官方文档：https://pandas.pydata.org/docs/ （已验证）
- Apache Arrow Python 文档：https://arrow.apache.org/docs/python/ （已验证，列式内存格式）
- Polars 官方文档：https://pola.rs/ （已验证，懒求值 DataFrame 引擎）

> 本 Day 上机使用 Python 标准库即可完成所有 TODO，pandas/Polars 属于扩展选项。

---

## 为什么不用手写伪代码（v4.0 做法）

| 维度 | 手写伪代码（v4.0） | Python 标准库（v5.0） |
|------|-------------------|---------------------|
| 可运行 | ❌ 伪代码无法执行 | ✅ 真实可运行代码 |
| 性能感知 | ❌ 无时间复杂度对比 | ✅ O(1) vs O(n) 实测对比 |
| 工业基础 | ❌ 与真实库脱节 | ✅ pandas/numpy 底层基础 |
| 数据治理 | ❌ 无 schema 规范 | ✅ namedtuple 定义 schema |
| 可复现 | ❌ 伪代码不可复现 | ✅ 标准库版本稳定可复现 |

**真实即严谨**--用 Python 标准库真实数据结构替代手写伪代码，是 v5.0 的哲学增量。
