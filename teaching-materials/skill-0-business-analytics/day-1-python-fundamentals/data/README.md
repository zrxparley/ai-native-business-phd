# Day 1 真实数据与库说明

> v5.0 核心升级：用**真实数据分析库**（pandas + numpy）+ **真实营销数据**（产品/客户/订单）替代纯手写脚本。手写脚本只能演示语法概念，pandas 能处理百万行级别的商业数据，是工业标准工具链。

---

## 主库：pandas（已验证，可运行）

**这是什么**：pandas 是 Python 数据分析的核心库（pandas-dev/pandas，43k+ star，BSD-3-Clause），提供 Series（一维）和 DataFrame（二维）两种数据结构。DataFrame 可以理解为 Excel 表格的程序化版本，但能处理百万行级别数据，且支持复杂的筛选、分组、聚合操作。

**为什么用它**：
- **工业标准**：几乎所有 Python 数据分析项目都以 pandas 为基础，与 NumPy/scikit-learn/matplotlib 无缝衔接
- **数据 IO 全覆盖**：`read_csv()`/`read_json()`/`read_sql()`/`read_excel()` -- 支持所有常见数据格式
- **向量化操作**：`df.apply()` / `df.groupby()` 比原生 Python `for` 循环快 10-100 倍
- **pandas 2.x 新特性**：基于 Apache Arrow 的后端（`dtype_backend="pyarrow"`），内存效率提升 30-50%

**安装方式**：

```bash
pip install pandas
# pandas 会自动安装 numpy 作为依赖
# 验证安装：
python -c "import pandas as pd; print(pd.__version__)"
# 预期输出: 2.x.x
```

**核心 API 速查**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| DataFrame | `import pandas as pd; pd.DataFrame(dict)` | 从字典创建营销数据表（TODO1） |
| dtypes | `df.dtypes` / `df.info()` | 检查数据类型（TODO2） |
| describe | `df.describe()` | 描述性统计（TODO2） |
| apply | `df['col'].apply(func)` | 向量化清洗/分类（TODO3） |
| groupby | `df.groupby('col').agg(...)` | 分组聚合（TODO6） |
| to_csv | `df.to_csv('file.csv', index=False)` | 写入 CSV（TODO5） |
| to_json | `df.to_json('file.json', orient='records', force_ascii=False)` | 写入 JSON（TODO5） |

**来源与验证**：
- GitHub：https://github.com/pandas-dev/pandas （43k+ star，BSD-3-Clause，已验证存在，2026-07 活跃维护）
- 官方文档：https://pandas.pydata.org/docs/ （已验证，含完整教程和 API 参考）
- PyPI：https://pypi.org/project/pandas/ （已验证，持续发布）

---

## 辅助库：numpy

**这是什么**：NumPy 是 Python 数值计算的基石（numpy/numpy，27k+ star，BSD-3-Clause），提供 ndarray（N维数组），比 Python 原生列表快 10-100 倍，因为底层数据连续存储且用 C 实现。pandas 底层依赖 NumPy。

**安装**：通常随 pandas 自动安装。如需单独安装：`pip install numpy`

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| mean | `np.mean(arr)` | 计算平均消费金额（TODO6） |
| sum | `np.sum(arr)` | 计算总销售额（TODO6） |
| where | `np.where(condition, x, y)` | 条件赋值（TODO3） |

- 官方文档：https://numpy.org/doc/stable/ （已验证，BSD-3-Clause）
- GitHub：https://github.com/numpy/numpy （已验证）

---

## 数据：营销产品/客户/订单数据（内嵌于 notebook）

本 Day 使用真实营销场景的产品/客户/订单数据，直接内嵌在 `starter.ipynb` 和 `solution.ipynb` 中，无需外部下载：

### 产品数据（8 个产品，3 个类别）

| product_id | product_name | category | unit_price | unit_cost |
|-----------|-------------|----------|-----------|----------|
| P001 | 烟酰胺精华液 | skincare | 299 | 120 |
| P002 | 保湿面霜 | skincare | 159 | 65 |
| P003 | 防晒霜SPF50 | skincare | 129 | 55 |
| P004 | 跑步手表 | electronics | 899 | 450 |
| P005 | 蓝牙耳机 | electronics | 499 | 220 |
| P006 | 智能体脂秤 | electronics | 169 | 75 |
| P007 | 瑜伽垫 | fitness | 89 | 35 |
| P008 | 阻力带套装 | fitness | 69 | 28 |

### 客户数据（15 个客户）

| customer_id | age | gender | registration_date | channel |
|------------|-----|--------|-------------------|---------|
| C0001 | 28 | F | 2024-01-15 | wechat |
| C0002 | 35 | M | 2024-02-20 | douyin |
| ... | ... | ... | ... | ... |

### 订单数据（30 笔订单）

| order_id | customer_id | product_id | quantity | order_date | channel | discount |
|---------|-----------|-----------|---------|-----------|---------|---------|
| ORD001 | C0001 | P001 | 2 | 2024-03-10 | wechat | 0.10 |
| ORD002 | C0002 | P004 | 1 | 2024-03-15 | douyin | 0.05 |
| ... | ... | ... | ... | ... | ... | ... |

> 💡 **数据来源说明**：这些数据模拟真实电商平台的营销数据（产品/客户/订单三表关联）。在实际项目中，你可以从业务数据库提取真实数据（用 `pd.read_sql()`），或使用公开数据集。本上机用内嵌数据确保开箱即用。

---

## 可选扩展：公开营销数据集

如果需要更大规模的真实营销数据，可以用以下公开数据集：

### 1. Kaggle: E-Commerce Data（已验证）
- URL：https://www.kaggle.com/datasets/carrie1/ecommerce-data
- **描述**：英国在线零售商 2010-2011 年交易数据（约 54 万条），包含产品/客户/订单字段，适合营销分析练习
- **用法**：下载 CSV 后用 `pd.read_csv('data.csv', encoding='latin1')` 加载

### 2. UCI: Online Retail II 数据集（已验证）
- URL：https://archive.ics.uci.edu/dataset/502/online+retail+ii
- **描述**：UCI Machine Learning Repository 的经典电商数据集，包含 2010-2011 年交易记录
- **用法**：适合练习 RFM 分析、客户分群、复购率计算

### 3. seaborn 内置 tips 数据集（已验证）
- URL：https://github.com/mwaskom/seaborn-data/blob/master/tips.csv
- **描述**：餐饮消费小费数据集（244 条），包含消费金额、小费、性别等字段，适合快速练习 pandas 操作
- **用法**：`import seaborn as sns; df = sns.load_dataset('tips')`

---

## 为什么不用手写脚本（v4.0 做法）

| 维度 | 手写脚本（v4.0） | pandas（v5.0） |
|------|-----------------|----------------|
| 数据加载 | 手动解析 CSV 行 | `pd.read_csv()` 一行搞定 |
| 类型安全 | 手动检查类型 | `dtypes` 自动推断 |
| 分组聚合 | 手写 for 循环 | `groupby().agg()` 向量化 |
| 缺失值 | 手动遍历填充 | `fillna()` / `dropna()` |
| 文件 IO | 手动 open/write | `to_csv()` / `to_json()` |
| 性能 | Python 循环 | C 后端，快 10-100 倍 |

**真实即严谨**--用工业级 pandas 替代手写脚本，是 v5.0 的哲学增量。
