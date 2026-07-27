# Day 2 真实数据与库说明

> v5.0 核心升级：用**真实机器学习库**（pandas + numpy + sklearn）+ **真实 RCT 数据**（causaldata / NSW）替代模拟数据和手写公式。真实数据即严谨，工业级库即可信。

---

## 主库 1：pandas + numpy（已验证，可运行）

**这是什么**：pandas 是 Python 数据分析的工业标准库（BSD License，PyData 维护），numpy 是数值计算基础（BSD License）。两者构成 CLV 公式计算与 RFM 分群的基础工具链。

**为什么用它**：
- **工业标准**：几乎所有 Python 数据分析项目的基础--从数据加载到清洗到分组聚合
- **CLV 公式实现**：`df['re74'] + df['re75'] + df['re78']` 一行完成历史 CLV 计算
- **RFM 分群基础**：`groupby` + `pd.qcut()` 组合可快速计算 R/F/M 三个维度并自动分桶
- **BG/NBD 简化公式**：numpy 的向量化运算让 `F × retention^12 × AOV × 12 × discount` 一行应用于全量客户

**安装方式**：

```bash
pip install pandas numpy
# 通常已随 conda/venv 安装
```

**核心 API 速查**：

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| DataFrame | `import pandas as pd` | NSW 数据表（TODO1-6） |
| pd.qcut() | | RFM 分桶 + CLV 价值四分位（TODO2/3） |
| df.apply() | | RFM 分群规则函数（TODO2） |
| Series.replace() | | 缺失值与无穷值处理（TODO4） |
| np.where() | `import numpy as np` | 流失标签向量化构造（TODO4） |

**来源与验证**：
- pandas 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- pandas GitHub：https://github.com/pandas-dev/pandas （已验证，40k+ star，2026-07 活跃维护）
- numpy 官方文档：https://numpy.org/doc/ （已验证，BSD License）

---

## 主库 2：scikit-learn（已验证，可运行）

**这是什么**：scikit-learn 是 Python 机器学习的工业标准库（BSD License），由 INRIA / Google / 谷歌AI等多方贡献维护。提供分类、回归、聚类、降维、模型选择、预处理等完整机器学习工具链。

**为什么用它**：
- **工业标准**：所有 Python 机器学习项目的基础--LogisticRegression / RandomForest / GradientBoosting 经过严格测试
- **流失预测核心**：`LogisticRegression` 提供基线模型，`RandomForestClassifier` 提供非线性强模型，两者构成流失预测的标配组合
- **完整评估**：`roc_auc_score` / `precision_score` / `recall_score` / `classification_report` 一键输出 AUC-ROC + Precision/Recall + F1
- **工程化**：`train_test_split` 支持分层抽样，`StandardScaler` 处理特征尺度差异，`class_weight='balanced'` 处理类不平衡

**安装方式**：

```bash
pip install scikit-learn
# sklearn 依赖 numpy + scipy，会自动安装
```

**核心 API 速查**：

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| LogisticRegression | `from sklearn.linear_model import LogisticRegression` | 流失预测基线模型（TODO4） |
| RandomForestClassifier | `from sklearn.ensemble import RandomForestClassifier` | 流失预测强模型（TODO5） |
| train_test_split | `from sklearn.model_selection import train_test_split` | 分层抽样分割（TODO4） |
| StandardScaler | `from sklearn.preprocessing import StandardScaler` | 特征标准化（TODO4） |
| roc_auc_score | `from sklearn.metrics import roc_auc_score` | AUC-ROC 评估（TODO4/5） |
| precision_score / recall_score | `from sklearn.metrics import precision_score, recall_score` | Precision/Recall（TODO4/5） |
| classification_report | `from sklearn.metrics import classification_report` | 完整分类报告（TODO5） |

**来源与验证**：
- sklearn 官方文档：https://scikit-learn.org/stable/ （已验证，BSD License）
- sklearn GitHub：https://github.com/scikit-learn/scikit-learn （已验证，13k+ star，2026-07 活跃维护）
- ROC 曲线文档：https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics （已验证）

---

## 主库 3：causaldata（已验证，可运行）

**这是什么**：causaldata 是 Scott Cunningham 的《Causal Inference: The Mixtape》教材配套 R/Python 数据包，提供多个真实因果推断数据集。MIT License。

**为什么用它**：
- **真实 RCT 数据**：NSW (National Supported Work) 是 1970 年代美国真实随机对照实验，445 条真实样本
- **因果推断标准数据**：NSW 是 LaLonde (1986) 论文使用的经典数据集，因果推断教材的标杆案例
- **CLV/流失映射价值**：RCT 数据天然适合映射为"营销干预 + 流失/CLV"场景（treat = 营销活动，re78 = 活动后消费用于构造流失标签）

**安装方式**：

```bash
pip install causaldata
```

**核心 API**：

```python
from causaldata.nsw_mixtape import load_pandas
df = load_pandas().data  # 返回 pandas DataFrame
```

**NSW 数据集字段说明**（Day 2 营销映射）：

| 字段 | 类型 | 原始含义 | Day 2 营销映射含义 |
|------|------|---------|-------------|
| data_id | str | 数据来源标识 | 数据来源标识 |
| treat | int8 | 是否参加培训(0/1) | 是否收到营销干预(0/1) -- 流失预测特征 |
| age | int8 | 年龄 | 客户年龄 -- 流失协变量 |
| educ | int8 | 教育年限 | 消费能力代理 -- 流失协变量 |
| black | int8 | 是否非裔 | 人口统计学特征 |
| hisp | int8 | 是否西裔 | 人口统计学特征 |
| marr | int8 | 是否已婚 | 家庭消费代理 -- 流失协变量 |
| nodegree | int8 | 是否无学位 | 价格敏感度代理 -- 流失协变量 |
| re74 | float32 | 1974年收入 | 历史消费基线（活动前2年）-- 历史 CLV 组成 + 流失特征 |
| re75 | float32 | 1975年收入 | 近期消费（活动前1年）-- 历史 CLV 组成 + 趋势特征 |
| re78 | float32 | 1978年收入 | 活动后消费 -- 历史 CLV 组成 + **流失标签构造来源** |

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- causaldata GitHub：https://github.com/NickCH-K/causaldata （已验证）
- LaLonde (1986) 原始论文：https://www.jstor.org/stable/1806062 （已验证，AER 经典论文）

---

## 真实数据：NSW RCT 数据集（Day 2 视角）

**数据来源**：National Supported Work (NSW) Demonstration，1970 年代美国联邦政府资助的真实就业培训随机对照实验。实验将符合条件的失业人员随机分配到培训组（treat=1）和对照组（treat=0），追踪其后续收入变化。

**Day 2 视角**：本 Day 将 NSW 数据映射为营销 CLV/流失场景。re74/re75/re78 分别代表活动前 2 年 / 前 1 年 / 活动后消费。流失定义：re78 == 0（活动后无消费）。

### 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | NSW 真实 RCT 数据（v5.0） |
|------|-----------------|----------------------|
| 数据真实性 | np.random 生成的理想分布 | 真实实验收集的真实人数据 |
| 分布特征 | 正态/均匀等规则分布 | 右偏/长尾/零膨胀等真实分布 |
| 流失标签 | 任意设定（如随机 20%） | 真实业务定义（re78==0，30.79%） |
| 模型表现 | 任意调参到 AUC 0.95+ | 真实 AUC ~0.54，反映 RCT 随机化设计 |
| 教学价值 | 演示概念 | 建立对真实数据质感和模型局限的直觉 |
| 因果推断基础 | 无 | RCT 是因果推断金标准，Day 3 增量测量的基础 |
| 严谨性 | 仅供演示 | 可用于学术研究和业务决策 |

**关键教学价值**：用 NSW 真实 RCT 数据，学生将看到 AUC ~0.54（接近随机）的模型表现--这恰恰反映了 RCT 设计的精髓：随机化确保基线特征不应强烈预测结果。在真实营销场景中，需要更丰富的行为特征（登录频率、会话时长、客服投诉）才能达到 AUC > 0.80。这一对比是模拟数据无法传递的真实数据质感。

**数据规模**：445 行 x 11 列（185 treated + 260 control）

**关键统计量**（Day 2 用 pandas 验证）：

| 指标 | Control (treat=0) | Treated (treat=1) |
|------|:-----------------:|:-----------------:|
| 样本量 | 260 | 185 |
| re78 == 0 比例（流失率） | 35.38% | 24.32% |
| re78 均值 | $4,554.80 | $6,349.14 |
| 历史 CLV（re74+re75+re78）均值 | $7,654 | $10,290 |

> **数据来源说明**：NSW 数据通过 causaldata 库加载，无需外部下载。该数据是公开的真实实验数据，广泛用于因果推断教学和研究。在 Day 2 营销场景中，我们将其映射为"营销干预对客户 CLV 与流失的影响"--treat=1 代表收到促销活动的客户，re78 代表活动后的消费金额，re78==0 表示流失。

---

## 辅助库：scipy + statsmodels

### scipy（统计计算基础）

**安装**：`pip install scipy`（sklearn 依赖，自动安装）

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| scipy.stats | `from scipy import stats` | 留存率置信区间（TODO3 选做） |

- scipy 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）

### statsmodels（统计建模，Day 1 已用）

本 Day 不直接使用 statsmodels，但其 OLS 回归框架是 Day 1 TODO6 的核心，与 Day 2 的 CUPED 前沿思想连接。

- statsmodels 官方文档：https://www.statsmodels.org/ （已验证，BSD License）

---

## 真实库 + 真实数据总结

| 库 | 版本 | License | Day 2 角色 |
|---|------|---------|-----------|
| pandas | 2.2.2 | BSD | RFM 分群 + CLV 公式 |
| numpy | 1.26.4 | BSD | BG/NBD 简化公式数值计算 |
| scikit-learn | 1.5.1 | BSD | 流失预测模型 + 评估 |
| scipy | 1.13.1 | BSD | 统计计算辅助 |
| causaldata | - | MIT | NSW 真实 RCT 数据 |

**真实即严谨**--用真实 RCT 数据替代模拟数据，用工业级机器学习库替代手写公式，是 v5.0 的核心哲学。
