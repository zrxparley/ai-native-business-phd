# Day 1 真实数据与库说明

> v5.0 核心升级：用**真实统计科学库**（pandas + scipy.stats + statsmodels）+ **真实 RCT 数据**（causaldata / NSW）替代模拟数据和手写公式。真实数据即严谨，工业级库即可信。

---

## 主库 1：pandas（已验证，可运行）

**这是什么**：pandas 是 Python 数据分析的工业标准库，提供 DataFrame 数据结构和丰富的数据操作方法。BSD License，由 PyData 社区维护。

**为什么用它**：
- **工业标准**：几乎所有 Python 数据分析项目的基础--从数据加载到清洗到分组聚合
- **与 SQL 的对应**：pandas 的 `groupby`/`agg`/`merge` 在逻辑上等价于 SQL 的 `GROUP BY`/聚合函数/`JOIN`，是 SQL 到 Python 的自然桥梁
- **描述统计核心**：`df.describe()` 一行生成均值/标准差/分位数/极值，`df.groupby('col').agg(...)` 一行完成分组统计
- **RFM 分析基础**：`groupby` + `agg` 组合可快速计算 R/F/M 三个维度

**安装方式**：

```bash
pip install pandas
# 通常已随 conda/venv 安装
# pandas 依赖 numpy，会自动安装
```

**核心 API 速查**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| DataFrame | `import pandas as pd` | NSW 数据表（TODO1-6） |
| df.describe() | | 一键描述统计（TODO1） |
| df.groupby() | | 分组统计 treated vs control（TODO1） |
| pd.crosstab() | | 列联表（TODO5） |
| df.corr() | | 相关矩阵（TODO6） |
| pd.cut() / pd.qcut() | | RFM 分桶（TODO3） |

**来源与验证**：
- 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- GitHub：https://github.com/pandas-dev/pandas （已验证，40k+ star，2026-07 活跃维护）

---

## 主库 2：scipy.stats（已验证，可运行）

**这是什么**：SciPy（Scientific Python）的统计模块，提供 100+ 概率分布和假设检验方法。BSD License，科学计算基石。

**为什么用它**：
- **权威性**：所有假设检验方法（t 检验、卡方检验、正态性检验）经过严格数值验证，结果与 R/Stata/SAS 一致
- **工业标准**：A/B 测试平台底层均使用 scipy.stats
- **与 pandas 无缝集成**：`scipy.stats.ttest_ind(df[df.treat==1].re78, df[df.treat==0].re78)` 一行完成检验

**安装方式**：

```bash
pip install scipy
# scipy 依赖 numpy，会自动安装
```

**核心 API 速查**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| ttest_ind | `from scipy.stats import ttest_ind` | 两独立样本 t 检验（TODO4） |
| chi2_contingency | `from scipy.stats import chi2_contingency` | 卡方独立性检验（TODO5） |
| pearsonr | `from scipy.stats import pearsonr` | 皮尔逊相关系数（TODO6） |

**来源与验证**：
- 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）
- GitHub：https://github.com/scipy/scipy （已验证，13k+ star，2026-07 活跃维护）

---

## 主库 3：statsmodels（已验证，可运行）

**这是什么**：statsmodels 是 Python 统计建模的专业库，提供回归分析、时间序列分析、方差分析等完整的统计模型和诊断工具。BSD License。

**为什么用它**：
- **专业建模**：提供 OLS / Logit / Probit / GLM 等完整模型，比 sklearn 更适合统计推断
- **完整诊断**：`model.summary()` 一键输出 R-squared / t 检验 / F 检验 / 置信区间 / AIC / BIC
- **控制混杂**：OLS 回归可以控制协变量（如 re75, age, educ），估计干预的净效应--这是诊断性分析的核心

**安装方式**：

```bash
pip install statsmodels
```

**核心 API 速查**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| OLS | `import statsmodels.api as sm` | 普通最小二乘回归（TODO6） |
| add_constant | `sm.add_constant(X)` | 添加截距项（TODO6） |
| model.summary() | | 完整回归诊断报告（TODO6） |

**来源与验证**：
- 官方文档：https://www.statsmodels.org/ （已验证，BSD License）
- GitHub：https://github.com/statsmodels/statsmodels/ （已验证，10k+ star）

---

## 主库 4：causaldata（已验证，可运行）

**这是什么**：causaldata 是 Scott Cunningham 的《Causal Inference: The Mixtape》教材配套 R/Python 数据包，提供多个真实因果推断数据集。MIT License。

**为什么用它**：
- **真实 RCT 数据**：NSW (National Supported Work) 是 1970 年代美国真实随机对照实验，445 条真实样本
- **因果推断标准数据**：NSW 是 LaLonde (1986) 论文使用的经典数据集，因果推断教材的标杆案例
- **营销映射价值**：RCT 数据天然适合映射为"营销干预"场景（treat = 营销活动，re78 = 活动后效果）

**安装方式**：

```bash
pip install causaldata
```

**核心 API**：

```python
from causaldata.nsw_mixtape import load_pandas
df = load_pandas().data  # 返回 pandas DataFrame
```

**NSW 数据集字段说明**：

| 字段 | 类型 | 原始含义 | 营销映射含义 |
|------|------|---------|-------------|
| data_id | str | 数据来源标识 | 数据来源标识 |
| treat | int8 | 是否参加培训(0/1) | 是否收到营销干预(0/1) |
| age | int8 | 年龄 | 客户年龄 |
| educ | int8 | 教育年限 | 消费能力代理 |
| black | int8 | 是否非裔 | 人口统计学特征 |
| hisp | int8 | 是否西裔 | 人口统计学特征 |
| marr | int8 | 是否已婚 | 家庭消费代理 |
| nodegree | int8 | 是否无学位 | 价格敏感度代理 |
| re74 | float32 | 1974年收入 | 历史消费基线（活动前2年） |
| re75 | float32 | 1975年收入 | 近期消费（活动前1年） |
| re78 | float32 | 1978年收入 | 活动后消费（效果指标） |

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- causaldata GitHub：https://github.com/NickCH-K/causaldata （已验证）
- LaLonde (1986) 原始论文：https://www.jstor.org/stable/1806062 （已验证，AER 经典论文）
- Dehejia & Wahba (1999) NSW 子样本说明：https://www.uh.edu/~adkugler/DehejiaWahba.pdf （已验证）

---

## 真实数据：NSW RCT 数据集

**数据来源**：National Supported Work (NSW) Demonstration，1970 年代美国联邦政府资助的真实就业培训随机对照实验。实验将符合条件的失业人员随机分配到培训组（treat=1）和对照组（treat=0），追踪其后续收入变化。

**为什么用 NSW 而非模拟数据**：

| 维度 | 模拟数据 | NSW 真实 RCT 数据 |
|------|---------|------------------|
| 真实性 | np.random 生成的理想分布 | 真实人的真实收入，含偏态/异常值/缺失 |
| 基线平衡 | 完美平衡（设计使然） | 存在基线不平衡（真实实验常见） |
| 效应大小 | 任意设定 | 真实效果（treat 效应约 $1,800） |
| 教学价值 | 演示概念 | 建立对真实数据质感的直觉 |
| 因果推断基础 | 无 | RCT 是因果推断金标准，Day 2/3 的基础 |

**数据规模**：445 行 x 11 列（185 treated + 260 control）

**关键统计量**（已用 pandas 验证）：

| 指标 | Control (treat=0) | Treated (treat=1) |
|------|:-----------------:|:-----------------:|
| 样本量 | 260 | 185 |
| re78 均值 | $4,554.80 | $6,349.14 |
| re78 中位数 | $3,138.80 | $4,232.31 |
| age 均值 | 25.05 | 25.82 |

> **数据来源说明**：NSW 数据通过 causaldata 库加载，无需外部下载。该数据是公开的真实实验数据，广泛用于因果推断教学和研究。在营销场景中，我们将其映射为"营销干预效果评估"--treat=1 代表收到促销活动的客户，re78 代表活动后的消费金额。

---

## 辅助库：numpy + matplotlib

### numpy（数值计算基础）

**安装**：`pip install numpy`（scipy/pandas 依赖，自动安装）

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| np.mean / np.median | `import numpy as np` | 均值/中位数（TODO1） |
| np.sqrt | | 标准误计算（TODO4） |

- 官方文档：https://numpy.org/doc/ （已验证，BSD License）

### matplotlib（可视化）

**安装**：`pip install matplotlib`

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| plt.subplots | `import matplotlib.pyplot as plt` | 多子图布局（TODO2 可选） |
| plt.hist | | 直方图（TODO2 可选） |

- matplotlib 官方文档：https://matplotlib.org/stable/contents.html （已验证，PSF License）

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实 RCT 数据（v5.0） |
|------|-----------------|----------------------|
| 数据真实性 | np.random 生成的理想分布 | 真实实验收集的真实人数据 |
| 分布特征 | 正态/均匀等规则分布 | 右偏/长尾/零膨胀等真实分布 |
| 基线平衡 | 完美平衡（设计使然） | 存在基线不平衡（真实实验常见） |
| 分析挑战 | 预设的"干净"结果 | 需要处理真实数据的不完美 |
| 教学价值 | 演示概念 | 建立对真实数据质感的直觉 |
| 因果推断基础 | 无 | RCT 是因果推断金标准 |
| 严谨性 | 仅供演示 | 可用于学术研究和业务决策 |

**真实即严谨**--用真实 RCT 数据替代模拟数据，用工业级科学计算库替代手写公式，是 v5.0 的核心哲学。
