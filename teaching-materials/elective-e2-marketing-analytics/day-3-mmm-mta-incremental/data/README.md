# Day 3 真实数据与库说明

> v5.0 核心升级：用**真实统计/ML 库**（statsmodels + sklearn + scipy + causaldata）+ **真实 RCT 数据**（NSW）+ **真实快消品 MMM 参数结构**替代模拟数据和手写公式。真实数据即严谨，工业级库即可信。

---

## 主库 1：statsmodels（已验证，可运行）

**这是什么**：statsmodels 是 Python 统计建模的工业标准库（BSD License），提供 OLS / Ridge / WLS / GLM / 时间序列 / 因果推断等完整统计建模工具链。本 Day 用它做 MMM 的回归建模。

**为什么用它**：
- **统计推断完整**：相比 sklearn 的 Ridge，statsmodels 提供 R² / t 检验 / F 检验 / 置信区间完整推断
- **MMM 工业实现**：`OLS` 拟合 `Sales ~ Adstock_Spend + Controls` 是业界 MMM 标准做法
- **贡献分解基础**：`model.predict()` 与系数矩阵乘法支持完整的渠道贡献分解

**安装方式**：

```bash
pip install statsmodels
# 依赖 numpy + scipy + pandas，自动安装
```

**核心 API 速查**：

| 组件 | 导入 | Day 3 用途 |
|------|------|-----------|
| OLS | `import statsmodels.api as sm` | MMM 拟合（TODO1） |
| add_constant | `sm.add_constant(X)` | 添加基线截距（TODO1） |
| Ridge | `from sklearn.linear_model import Ridge` | MMM 共线性稳健（TODO1） |
| fit().summary() | | 完整统计推断（TODO1） |

**来源与验证**：
- statsmodels 官方文档：https://www.statsmodels.org/ （已验证，BSD License）
- statsmodels GitHub：https://github.com/statsmodels/statsmodels/ （已验证，10k+ star，2026-07 活跃维护）

---

## 主库 2：scikit-learn + scipy（已验证，可运行）

**scikit-learn**：机器学习工业标准库（BSD License）。本 Day TODO1 用 Ridge 回归做 MMM（处理共线性），TODO5 用 RandomForest 实现 DML。

**scipy**：科学计算基础（BSD License）。本 Day TODO6 用 `scipy.optimize.minimize` 做预算分配优化。

**核心 API 速查**：

| 组件 | 导入 | Day 3 用途 |
|------|------|-----------|
| Ridge | `from sklearn.linear_model import Ridge` | MMM 共线性稳健（TODO1） |
| StandardScaler | `from sklearn.preprocessing import StandardScaler` | 特征标准化（TODO1） |
| RandomForestRegressor | `from sklearn.ensemble import RandomForestRegressor` | DML 拟合 m(x) 和 g(x)（TODO5） |
| KFold | `from sklearn.model_selection import KFold` | DML 交叉拟合（TODO5） |
| minimize | `from scipy.optimize import minimize` | 预算优化（TODO6） |

**来源与验证**：
- sklearn 官方文档：https://scikit-learn.org/stable/ （已验证，BSD License）
- scipy 官方文档：https://docs.scipy.org/doc/scipy/reference/optimize.html （已验证，BSD License）

---

## 主库 3：causaldata（已验证，可运行）

**这是什么**：causaldata 是 Scott Cunningham《Causal Inference: The Mixtape》教材的配套 R/Python 数据包，提供多个真实因果推断数据集。MIT License。

**为什么用它**：
- **真实 RCT 数据**：NSW (National Supported Work) 是 1970 年代美国真实随机对照实验，445 条真实样本
- **增量测量金标准**：RCT 的随机化使均值差等于真实处理效应，是验证合成控制 / DML 等观测方法的基准
- **Day 3 营销映射价值**：treat = 营销曝光，re78 = 投放后销售，re74/re75 = pre-period 基线（合成控制 + DML 用）

**安装方式**：

```bash
pip install causaldata
```

**核心 API**：

```python
from causaldata.nsw_mixtape import load_pandas
df = load_pandas().data  # 返回 pandas DataFrame，445 行
```

**NSW 数据集字段说明**（Day 3 增量测量视角）：

| 字段 | 类型 | 原始含义 | Day 3 营销映射含义 |
|------|------|---------|-------------|
| treat | int8 | 是否参加培训(0/1) | 是否收到广告曝光(0/1) -- 处理变量 T |
| age | int8 | 年龄 | 客户年龄 -- 混杂协变量 |
| educ | int8 | 教育年限 | 消费能力代理 -- 混杂协变量 |
| black / hisp | int8 | 人口统计学 | 客户画像 -- 协变量 |
| marr | int8 | 是否已婚 | 家庭消费代理 -- 协变量 |
| nodegree | int8 | 是否无学位 | 价格敏感度代理 -- 协变量 |
| re74 | float32 | 1974年收入 | 投放前 2 年消费基线 -- pre-period matching |
| re75 | float32 | 1975年收入 | 投放前 1 年消费基线 -- pre-period matching |
| re78 | float32 | 1978年收入 | 投放后销售 -- 结果变量 Y |

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- causaldata GitHub：https://github.com/NickCH-K/causaldata （已验证）
- LaLonde (1986) 原始论文：https://www.jstor.org/stable/1806062 （已验证，AER 经典论文）
- Cunningham《Causal Inference: The Mixtape》：https://mixtape.scunning.com/ （已验证，免费在线教材）

---

## 真实数据 1：NSW RCT 数据集（增量测量）

**数据来源**：National Supported Work (NSW) Demonstration，1970 年代美国联邦政府资助的真实就业培训随机对照实验。实验将符合条件的失业人员随机分配到培训组（treat=1）和对照组（treat=0），追踪其后续收入变化。

**Day 3 视角**：本 Day 将 NSW 数据映射为营销增量测量场景。treat=1 代表收到广告曝光的客户，re78 代表投放后销售。RCT 的随机化使均值差等于真实增量。

### 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | NSW 真实 RCT 数据（v5.0） |
|------|-----------------|----------------------|
| 数据真实性 | np.random 生成的理想分布 | 真实实验收集的真实人数据 |
| 分布特征 | 正态/均匀等规则分布 | 右偏/长尾/零膨胀等真实分布 |
| 因果效应真值 | 你造数据时设定的"答案" | RCT 随机化 -> 均值差即真值 |
| 增量率 | 任意设定（如 30%） | 真实计算：treated vs control 的 re78 差距 |
| 合成控制验证 | 模拟数据无验证价值 | NSW 控制组可构造"合成实验组"对照 |
| DML 验证 | 模拟混杂已知 | 真实协变量混杂（age/educ/re74/re75） |
| 教学价值 | 演示概念 | 建立对真实因果测量质感和方法局限的直觉 |
| 严谨性 | 仅供演示 | 可用于学术研究和业务决策 |

**关键教学价值**：用 NSW 真实 RCT 数据，学生将看到朴素均值差、合成控制、DML 三种方法在真实数据上的差异--这恰恰反映了因果测量的复杂性。在真实营销场景中，RCT 不可行时，合成控制 / DML 是实操方案。

**数据规模**：445 行 x 11 列（185 treated + 260 control）

**关键统计量**（Day 3 用 pandas 验证）：

| 指标 | Control (treat=0) | Treated (treat=1) |
|------|:-----------------:|:-----------------:|
| 样本量 | 260 | 185 |
| re78 均值（投放后销售） | $4,554.80 | $6,349.14 |
| re74 均值（投放前 2 年） | $2,107.03 | $2,095.57 |
| re75 均值（投放前 1 年） | $1,266.91 | $1,532.06 |
| 朴素均值差（增量） | -- | $1,794.34 |
| 增量率 | -- | 28.26% |

> **关键观察**：re74/re75（pre-period）两组相近（RCT 随机化），但 re78（post-period）有显著差异。这就是 RCT 的力量--基线均衡使得均值差等于真实因果效应。

---

## 真实数据 2：基于真实快消品 MMM 案例参数的周度营销数据

**数据来源**：本 Day TODO1 的 MMM 数据并非凭空捏造，而是基于公开的真实快消品 MMM 案例参数结构生成（包括 Google Meridian 文档、Meta Robyn 案例库、Chan & Perry 2017 论文披露的典型参数范围）。生成器在 starter 中提供，确保可复现。

**渠道参数结构**（来自真实快消品 MMM 案例的典型范围）：

| 渠道 | 衰减率 λ（真实范围） | 响应系数 β（真实范围） | 业务含义 |
|------|:------------------:|:------------------:|---------|
| search_ads | 0.20（0.1-0.3 即时） | 1.5（高，强转化） | 搜索广告：用户主动搜索，转化率高 |
| social_ads | 0.40（0.3-0.5 中期） | 1.0（中，品牌+转化） | 社交广告：内容传播，中周期效果 |
| display_ads | 0.60（0.5-0.7 长尾） | 0.6（低，品牌为主） | 展示广告：品牌曝光，长尾效应 |
| email_marketing | 0.15（0.1-0.2 触发） | 1.2（较高，触发式） | 邮件营销：触发式，效果即时 |

**控制变量**（真实 MMM 标准控制）：
- `seasonality`：周度季节性指数（用 sin/cos 构造，模拟年末/节假日高峰）
- `holiday_flag`：节假日 0/1 标记
- `competitor_promo`：竞品促销 0/1 标记

**生成器**：见 `solution.ipynb` TODO1 的数据生成代码。用固定 `random_state=42` 确保可复现。104 周（2 年）数据，符合真实 MMM 的最小数据量要求。

---

## 辅助库：pandas + numpy（已验证）

**pandas + numpy**：本 Day 全程使用，提供 DataFrame 操作、向量化运算、矩阵分解等基础。已在 Day 1/2 介绍，此处不重复。

- pandas 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- numpy 官方文档：https://numpy.org/doc/ （已验证，BSD License）

---

## 真实库 + 真实数据总结

| 库 | 版本 | License | Day 3 角色 |
|---|------|---------|-----------|
| statsmodels | 0.14.2 | BSD | MMM 回归建模 + 统计推断 |
| scikit-learn | 1.5.1 | BSD | Ridge/MMM + RandomForest/DML + StandardScaler |
| scipy | 1.13.1 | BSD | 预算优化（minimize） |
| pandas | 2.2.2 | BSD | 数据处理 + MTA 路径分析 |
| numpy | 1.26.4 | BSD | Adstock 计算 + 矩阵运算 |
| causaldata | - | MIT | NSW 真实 RCT 数据 |

**真实即严谨**--用真实 RCT 数据替代模拟数据，用工业级统计/ML 库替代手写公式，用真实快消品 MMM 参数结构替代任意设定，是 v5.0 的核心哲学。
