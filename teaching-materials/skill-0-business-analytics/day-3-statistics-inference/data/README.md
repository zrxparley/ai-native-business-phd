# Day 3 真实数据与库说明

> v5.0 核心升级：用**真实统计科学库**（numpy + pandas + scipy.stats + matplotlib/seaborn）+ **真实营销 A/B 测试数据**替代手写统计公式。手写公式只能演示概念，scipy.stats 是经过严格测试的科学计算库，结果可直接用于业务决策。

---

## 主库：scipy.stats（已验证，可运行）

**这是什么**：SciPy（Scientific Python）是 Python 科学计算的基石库，`scipy.stats` 是其统计模块，提供 100+ 概率分布和假设检验方法。它由 SciPy 社区维护（BSD License），是统计学教科书和科研论文的标准工具。

**为什么用它**：
- **权威性**：所有假设检验方法（t 检验、卡方检验、正态性检验）经过严格数值验证，结果与 R/Stata/SAS 等商业软件一致
- **完整性**：覆盖连续分布（正态/Beta/t/F/卡方）、离散分布（二项/泊松/超几何）、假设检验（ttest_ind/chi2_contingency/shapiro/anderson）
- **工业标准**：A/B 测试平台（如 Optimizely、Google Optimize 的开源替代品）底层均使用 scipy.stats
- **与 pandas 无缝集成**：`scipy.stats.ttest_ind(df[df.group=='A'].converted, df[df.group=='B'].converted)` 一行完成检验

**安装方式**：

```bash
pip install scipy
# 通常已随 conda/venv 安装
# scipy 依赖 numpy，会自动安装
```

**核心 API 速查**：

| 组件 | 导入 | Day 3 用途 |
|------|------|-----------|
| ttest_ind | `from scipy.stats import ttest_ind` | 两独立样本 t 检验（TODO3） |
| chi2_contingency | `from scipy.stats import chi2_contingency` | 卡方独立性检验（TODO5） |
| norm | `from scipy.stats import norm` | 正态分布分位数/CI（TODO4） |
| beta | `from scipy.stats import beta` | Beta 分布后验推断（TODO6） |
| shapiro | `from scipy.stats import shapiro` | 正态性检验（TODO2 可选） |
| describe | `from scipy.stats import describe` | 描述统计（偏度/峰度） |

**来源与验证**：
- 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）
- GitHub：https://github.com/scipy/scipy （已验证，13k+★，2026-07 活跃维护）
- PyPI：https://pypi.org/project/scipy/ （已验证，持续发布）

---

## 辅助库：numpy + pandas + matplotlib + seaborn

### numpy（数值计算基础）

**安装**：`pip install numpy`（scipy 依赖，自动安装）

| 组件 | 导入 | Day 3 用途 |
|------|------|-----------|
| np.mean / np.median | `import numpy as np` | 均值/中位数（TODO1） |
| np.var / np.std | | 方差/标准差（TODO1） |
| np.quantile | | 分位数（TODO1） |
| np.random.binomial | | 模拟伯努利/二项数据 |
| np.sqrt | | 标准误计算（TODO4） |

- 官方文档：https://numpy.org/doc/ （已验证，BSD License）

### pandas（数据框操作）

**安装**：`pip install pandas`

| 组件 | 导入 | Day 3 用途 |
|------|------|-----------|
| DataFrame | `import pandas as pd` | 营销数据表（TODO1-6） |
| df.describe() | | 一键描述统计（TODO1） |
| df.groupby() | | 分组统计 A/B 两组（TODO1） |
| pd.crosstab() | | 列联表（TODO5） |

- 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）

### matplotlib + seaborn（可视化）

**安装**：`pip install matplotlib seaborn`

| 组件 | 导入 | Day 3 用途 |
|------|------|-----------|
| plt.subplots | `import matplotlib.pyplot as plt` | 多子图布局（TODO2） |
| plt.hist | | 直方图（TODO2） |
| plt.boxplot | | 箱线图（TODO2） |
| sns.histplot | `import seaborn as sns` | 增强直方图（TODO2） |
| sns.heatmap | | 列联表热力图（TODO5） |

- matplotlib 官方文档：https://matplotlib.org/stable/contents.html （已验证，PSF License）
- seaborn 官方文档：https://seaborn.pydata.org/ （已验证，BSD License）

---

## 数据：营销 A/B 测试数据（内嵌于 notebook）

本 Day 使用 1000 条模拟真实营销场景的 A/B 测试数据，直接内嵌在 `starter.ipynb` 和 `solution.ipynb` 中，无需外部下载：

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| user_id | int | 用户唯一标识 | 1-1000 |
| group | str | 实验分组（A=旧版落地页，B=新版落地页） | 'A' / 'B' |
| converted | int | 是否转化（1=购买，0=未购买） | 0 / 1 |
| spend | float | 消费金额（元，未转化为 0） | 0.0 / 89.50 |
| segment | str | 用户分群（new=新客，returning=回客，vip=VIP） | 'new' |
| category | str | 购买品类（beauty/electronics/fitness/home） | 'beauty' |

**数据生成逻辑**（模拟真实 A/B 测试）：
- A 组（旧版）：真实转化率约 3.0%，客单价均值约 33 元（lognormal）
- B 组（新版）：真实转化率约 6.0%，客单价均值约 45 元（lognormal）
- 用户分群与品类随机分配，用于卡方独立性检验

> 💡 **数据来源说明**：这些数据用 `np.random` 模拟真实电商 A/B 测试，转化率和客单价参数参考行业基准。在实际项目中，数据来自业务数据库（SQL 查询）或 A/B 测试平台 API。本上机用内嵌数据确保开箱即用。

---

## 可选扩展：seaborn 内置数据集

如果需要更大规模的真实数据集，可以用 seaborn 内置数据集练习：

```python
import seaborn as sns
# tips 数据集：餐厅小费数据（常用于描述统计和回归练习）
tips = sns.load_dataset("tips")
# mpg 数据集：汽车油耗数据（常用于分布分析）
mpg = sns.load_dataset("mpg")
```

- seaborn 内置数据集列表：https://github.com/mwaskom/seaborn-data （已验证）

> 本 Day 上机使用内嵌 A/B 测试数据即可完成所有 TODO，seaborn 内置数据集属于扩展选项。

---

## 可选扩展：statsmodels（统计建模）

如果需要更专业的统计建模（如功效分析、回归诊断）：

```bash
pip install statsmodels
```

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
# 功效分析：计算 A/B 测试所需样本量
power_analysis = NormalIndPower()
required_n = power_analysis.solve_power(effect_size=0.2, power=0.8, alpha=0.05)
```

- statsmodels 官方文档：https://www.statsmodels.org/ （已验证，BSD License）

> 本 Day TODO4 的置信区间用 scipy.stats.norm 手动计算，statsmodels 属于扩展选项。

---

## 为什么不用手写统计公式（v4.0 做法）

| 维度 | 手写公式（v4.0） | scipy.stats（v5.0） |
|------|-----------------|---------------------|
| 正确性 | 手写易出错（如 t 值查表、自由度计算） | 经过严格数值验证 |
| 覆盖面 | 仅能实现基础公式 | 100+ 分布和检验方法 |
| 可复现性 | 手写脚本难以复现 | 标准 API，结果可复现 |
| 工业标准 | ❌ 定制方案 | ✅ A/B 测试平台标准工具 |
| 扩展性 | 每个检验需重新实现 | 统一接口，学习成本低 |

**真实即严谨**--用工业级科学计算库替代手写公式，是 v5.0 的哲学增量。
