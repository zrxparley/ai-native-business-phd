# AI原生化商业博士 · 独立教材：选修E6 应用统计与优化方法

> **修读者**：aha.gare
> **导师系统**：Claude / 天道推演 + 系统觉醒 + 学位对标融合 + 牛津自然学习法 + 全球七校对标
> **版本**：v4.2 | **日期**：2026-07-30
> **学时**：6h | 建议节奏：3天集中学习
> **对标课程**：MIT Sloan 15.071 The Analytics Edge + Stanford GSB Optimization Methods + Harvard HBS DDA + Imperial Statistics for Data Science
> **AEFS对标**：Phase 1 (Math Foundations) + Phase 2 (ML Fundamentals) 部分课节
> **前置条件**：完成技能0（AI商业分析基础），具备Python基础和描述统计知识
> **定位**：从"理解统计概念"升级到"能用统计与优化方法解决营销决策问题"，覆盖时间序列预测、蒙特卡洛模拟、数学优化和R语言分析全链路

---

## 课程概述

### 核心命题

**如何用统计模型和优化算法将营销决策从"凭经验判断"升级为"数据驱动最优"？**

应用统计与优化方法是数据驱动决策的核心数学引擎。技能0让你掌握了描述统计和基础回归，技能3让你理解了因果推断的框架。本选修课进一步深入两个方向：一是**时间序列预测**——从历史数据中提取趋势和季节性规律来预测未来；二是**优化方法**——在约束条件下寻找最优决策方案。这两个方向合在一起，构成了"预测+决策"的完整闭环。

对于售前解决方案产品经理而言，统计与优化能力直接决定了AI营销方案的"技术深度"。客户经常面临这样的问题：下个季度的销售额会怎样？1000万营销预算怎么在5个渠道之间分配才能ROI最高？产品定价定在多少利润最大？这些问题的答案，都需要时间序列预测和数学优化方法来回答。

### 学习目标

完成本课程后，你将能够：

1. **预测层**：掌握时间序列分解、平稳性检验、ARIMA/SARIMA/Prophet模型，能对营销销售额进行月度/季度预测
2. **模拟层**：理解蒙特卡洛模拟原理，能用10000次随机采样评估营销ROI的风险分布
3. **优化层**：掌握线性规划、非线性优化和启发式算法，能用scipy求解多渠道预算最优分配和定价优化问题
4. **工具层**：掌握R语言基础（dplyr/ggplot2/lm/glm），能用R完成完整的营销数据分析报告
5. **实践层**：理解Python与R的协作模式，能根据场景选择合适的工具链

### 前置条件

- 完成技能0核心课程，掌握Python数据分析（pandas/numpy/matplotlib）和描述统计基础
- 理解线性回归和逻辑回归的基本概念
- 对企业营销场景有实战经验（理解销售额周期波动、预算分配、定价策略）

---

## 学习计划表（3天）

| 天次 | 主题 | 时长 | 核心产出 | AEFS引用 |
|:---:|------|:----:|---------|---------|
| **Day 1** | 时间序列预测 | 2h | ARIMA预测代码 + Prophet预测代码 + 模型评估报告 | P2-15, P1-22, P1-16 |
| **Day 2** | 蒙特卡洛模拟与优化方法 | 2h | 蒙特卡洛模拟代码 + 线性规划代码 + 非线性优化代码 | P1-08, P1-18, P1-16 |
| **Day 3** | R语言基础与统计应用 | 2h | R营销分析报告代码 + Python-R协作方案 | P1-15 |

---

## 详细学习内容

---

### Day 1：时间序列预测

#### 一、时间序列分解

时间序列（Time Series）是按时间顺序排列的数据点序列。在营销领域，月度销售额、日UV、季度广告支出都是典型的时间序列。时间序列分解的核心思想是将一个序列拆解为多个可解释的组成部分。

**加法模型**：$Y_t = T_t + S_t + R_t$

其中 $T_t$ 是趋势成分（Trend），反映长期上升或下降方向；$S_t$ 是季节性成分（Seasonality），反映固定周期内的重复模式；$R_t$ 是残差成分（Residual），包含无法被趋势和季节性解释的随机波动。加法模型适用于季节性波动幅度不随趋势变化的情况。

**乘法模型**：$Y_t = T_t \times S_t \times R_t$

乘法模型适用于季节性波动幅度随趋势增大而增大的情况——这在营销数据中非常常见，因为销售额越高，季节性波动的绝对值也越大。

**STL分解**（Seasonal and Trend decomposition using Loess）是一种灵活的分解方法，使用局部加权回归（LOESS）来估计趋势和季节性成分。STL的优势在于可以处理任意频率的季节性、允许季节性成分随时间变化、对异常值具有鲁棒性。

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

# 生成模拟的月度营销销售额数据（3年，36个月）
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=36, freq='MS')
trend = np.linspace(100, 200, 36)  # 线性上升趋势
seasonality = 20 * np.sin(2 * np.pi * np.arange(36) / 12)  # 年度季节性
noise = np.random.normal(0, 5, 36)
sales = trend + seasonality + noise

ts = pd.Series(sales, index=dates, name='monthly_sales')

# STL分解
stl = STL(ts, period=12)
result = stl.fit()

# 可视化
fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
axes[0].plot(ts, label='原始数据'); axes[0].set_title('月度销售额'); axes[0].legend()
axes[1].plot(result.trend, color='orange', label='趋势'); axes[1].legend()
axes[2].plot(result.seasonal, color='green', label='季节性'); axes[2].legend()
axes[3].plot(result.resid, color='red', label='残差'); axes[3].legend()
plt.tight_layout(); plt.savefig('stl_decomposition.png', dpi=150)
plt.show()

print(f"趋势范围: {result.trend.min():.1f} - {result.trend.max():.1f}")
print(f"季节性范围: {result.seasonal.min():.1f} - {result.seasonal.max():.1f}")
# 输出示例：
# 趋势范围: 102.3 - 197.8
# 季节性范围: -19.8 - 19.8
```

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 22: [Stochastic Processes](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/22-stochastic-processes)
> 预计时长：~60 min

#### 二、平稳性检验

平稳性（Stationarity）是时间序列建模的核心假设。一个平稳序列的统计特性（均值、方差、自相关结构）不随时间变化。ARIMA模型要求输入序列是平稳的，因此需要先检验并必要时通过差分使其平稳。

**ADF检验**（Augmented Dickey-Fuller Test）：
- 原假设 $H_0$：序列存在单位根（非平稳）
- 备择假设 $H_1$：序列平稳
- 若 p-value < 0.05，拒绝原假设，认为序列平稳

**KPSS检验**（Kwatkowski-Phillips-Schmidt-Shin Test）：
- 原假设 $H_0$：序列平稳
- 备择假设 $H_1$：序列非平稳
- 若 p-value < 0.05，拒绝原假设，认为序列非平稳

ADF和KPSS的假设方向相反，实践中常同时使用以交叉验证。

**差分**（Differencing）是将非平稳序列转化为平稳序列的常用方法。一阶差分：$\Delta Y_t = Y_t - Y_{t-1}$。如果一阶差分后仍不平稳，可以进行二阶差分。

```python
from statsmodels.tsa.stattools import adfuller, kpss

def check_stationarity(series, name='series'):
    """执行ADF和KPSS检验"""
    # ADF检验
    adf_result = adfuller(series.dropna())
    print(f"=== {name} ADF检验 ===")
    print(f"ADF统计量: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}")
    print(f"结论: {'平稳' if adf_result[1] < 0.05 else '非平稳'}")

    # KPSS检验
    kpss_result = kpss(series.dropna(), regression='c')
    print(f"\n=== {name} KPSS检验 ===")
    print(f"KPSS统计量: {kpss_result[0]:.4f}, p-value: {kpss_result[1]:.4f}")
    print(f"结论: {'非平稳' if kpss_result[1] < 0.05 else '平稳'}")

# 检验原始序列
check_stationarity(ts, '原始销售额')

# 一阶差分
ts_diff1 = ts.diff()
check_stationarity(ts_diff1, '一阶差分')
```

> 🔗 **延伸实践**：详见 AEFS Phase 2 · Lesson 15: [Time Series Fundamentals](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/15-time-series)
> 预计时长：~90 min

#### 三、自相关分析

自相关函数（ACF, Autocorrelation Function）度量序列与其自身滞后版本之间的相关性。偏自相关函数（PACF, Partial Autocorrelation Function）度量在控制中间滞后项影响后的纯相关。

ACF和PACF图是选择ARIMA模型参数的关键工具：

| 模式 | ACF | PACF | 适用模型 |
|------|-----|------|---------|
| AR(p) | 逐渐衰减 | p步后截尾 | ARIMA(p, d, 0) |
| MA(q) | q步后截尾 | 逐渐衰减 | ARIMA(0, d, q) |
| ARMA(p,q) | 逐渐衰减 | 逐渐衰减 | ARIMA(p, d, q) |

"截尾"指自相关值在某个滞后阶数后突然降至置信区间内（通常为 $\pm 1.96/\sqrt{n}$）；"衰减"指自相关值逐渐减小。

```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig, axes = plt.subplots(1, 2, figsize=(14, 4))
plot_acf(ts_diff1.dropna(), lags=20, ax=axes[0])
axes[0].set_title('ACF（自相关函数）')
plot_pacf(ts_diff1.dropna(), lags=20, ax=axes[1])
axes[1].set_title('PACF（偏自相关函数）')
plt.tight_layout(); plt.savefig('acf_pacf.png', dpi=150)
plt.show()
```

#### 四、ARIMA模型详解

ARIMA（AutoRegressive Integrated Moving Average）模型是时间序列预测的经典方法，由三个部分组成：

**AR(p) - 自回归部分**：
$$Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + ... + \phi_p Y_{t-p} + \epsilon_t$$

当前值是过去p个值的线性组合加上随机误差。$\phi_i$ 是自回归系数，$p$ 是阶数。

**I(d) - 差分部分**：
对序列进行d阶差分使其平稳。$d=0$ 表示序列已平稳，$d=1$ 表示一阶差分后平稳。

**MA(q) - 移动平均部分**：
$$Y_t = c + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + ... + \theta_q \epsilon_{t-q}$$

当前值是当前和过去q个随机误差的线性组合。$\theta_j$ 是移动平均系数。

完整的ARIMA(p, d, q)模型：先对序列做d阶差分，然后对差分后的序列建立ARMA(p, q)模型。

**参数选择策略**：
1. 通过ADF/KPSS检验确定d（差分阶数）
2. 通过ACF/PACF图的截尾/衰减模式初步判断p和q
3. 使用AIC/BIC信息准则在候选模型中选优：$AIC = 2k - 2\ln(L)$，其中k是参数个数，L是似然函数值。AIC越小模型越好，同时惩罚过拟合

```python
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# 自动选择最优ARIMA参数（基于AIC）
best_aic = float('inf')
best_order = None
best_model = None

for p in range(4):
    for q in range(4):
        try:
            model = ARIMA(ts, order=(p, 1, q))  # d=1因为原始序列需要一阶差分
            result = model.fit()
            if result.aic < best_aic:
                best_aic = result.aic
                best_order = (p, 1, q)
                best_model = result
        except:
            continue

print(f"最优ARIMA参数: {best_order}, AIC: {best_aic:.2f}")
print(best_model.summary())

# 预测未来6个月
forecast = best_model.forecast(steps=6)
print("\n未来6个月销售额预测:")
for date, value in zip(pd.date_range('2026-01-01', periods=6, freq='MS'), forecast):
    print(f"  {date.strftime('%Y-%m')}: {value:.1f}万元")
# 输出示例：
#   2026-01: 205.3万元
#   2026-02: 198.7万元
#   2026-03: 212.1万元
#   2026-04: 208.5万元
#   2026-05: 221.3万元
#   2026-06: 215.8万元
```

**模型诊断**：拟合后需要检查残差是否为白噪声。如果残差仍包含未被提取的信息（ACF有显著项），说明模型不够充分。

```python
# 残差诊断
residuals = best_model.resid
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(residuals)
axes[0].set_title('残差时序图')
plot_acf(residuals, lags=20, ax=axes[1])
axes[1].set_title('残差ACF')
plt.tight_layout(); plt.savefig('residual_diagnostics.png', dpi=150)
plt.show()

# Ljung-Box检验：残差是否为白噪声
from statsmodels.stats.diagnostic import acorr_ljungbox
lb_test = acorr_ljungbox(residuals, lags=10, return_df=True)
print(f"Ljung-Box检验p-value: {lb_test['lb_pvalue'].iloc[-1]:.4f}")
print(f"结论: {'残差是白噪声（模型充分）' if lb_test['lb_pvalue'].iloc[-1] > 0.05 else '残差非白噪声（模型不充分）'}")
```

#### 五、Seasonal ARIMA (SARIMA)

SARIMA在ARIMA基础上增加季节性成分：$ARIMA(p, d, q) \times (P, D, Q, s)$

其中 $(P, D, Q)$ 是季节性自回归、差分和移动平均阶数，$s$ 是季节周期（月度数据$s=12$，季度数据$s=4$）。

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# SARIMA(1,1,1)(1,1,1,12) 模型
sarima_model = SARIMAX(ts, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_result = sarima_model.fit(disp=False)
print(f"SARIMA AIC: {sarima_result.aic:.2f}")

# 与ARIMA比较
print(f"ARIMA AIC: {best_model.aic:.2f}")
print(f"SARIMA {'更优' if sarima_result.aic < best_model.aic else '不如ARIMA'}")
```

#### 六、Prophet模型

Prophet是Facebook开源的时间序列预测工具，特别适合包含强季节性和节假日效应的商业数据。

Prophet使用加法模型：$y(t) = g(t) + s(t) + h(t) + \epsilon_t$

- $g(t)$：趋势项，支持线性趋势和饱和增长趋势（基于逻辑函数）
- $s(t)$：季节性项，使用傅里叶级数建模：$s(t) = \sum_{n=1}^{N}(a_n \cos(\frac{2\pi n t}{P}) + b_n \sin(\frac{2\pi n t}{P}))$
- $h(t)$：节假日效应，为每个节假日分配一个冲击变量
- $\epsilon_t$：噪声项

**变点（Changepoint）检测**：Prophet自动检测趋势变化点，允许趋势在特定时间点发生方向变化。这对营销数据尤其重要——一次营销策略调整或市场环境变化可能导致趋势突变。

```python
from prophet import Prophet
import pandas as pd

# 准备Prophet格式数据（列名必须为ds和y）
prophet_df = pd.DataFrame({
    'ds': dates,
    'y': sales
})

# 添加中国电商节日
holidays = pd.DataFrame({
    'holiday': ['618大促', '双11', '双12'],
    'ds': pd.to_datetime(['2023-06-18', '2023-11-11', '2023-12-12']),
    'lower_window': [-7, -7, -7],  # 节日前7天开始影响
    'upper_window': [3, 3, 3],      # 节日后3天仍有影响
})

# 创建并训练Prophet模型
model = Prophet(
    growth='linear',        # 线性趋势
    seasonality_mode='additive',  # 加法季节性
    changepoint_prior_scale=0.05,  # 变点灵活度（越大越灵活）
    holidays=holidays,
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)
model.fit(prophet_df)

# 预测未来6个月
future = model.make_future_dataframe(periods=6, freq='MS')
forecast = model.predict(future)

# 可视化
fig1 = model.plot(forecast)
plt.title('Prophet销售额预测（含节日效应）')
plt.savefig('prophet_forecast.png', dpi=150)

fig2 = model.plot_components(forecast)
plt.savefig('prophet_components.png', dpi=150)
plt.show()

# 查看节日效应
holiday_effects = forecast[forecast['holidays'].abs() > 0.1][['ds', 'holidays']]
print("节日效应:")
print(holiday_effects)
```

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 16: [Sampling Methods](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/16-sampling-methods)
> 预计时长：~75 min

#### 七、模型评估

时间序列模型评估不能使用普通的K折交叉验证（因为时间序列有时序依赖性），而应使用**时间序列交叉验证**（Time Series Cross-Validation, TSCV）：训练集始终在测试集之前。

常用评估指标：

- **MAPE**（Mean Absolute Percentage Error）：$\text{MAPE} = \frac{100\%}{n}\sum_{t=1}^{n}\left|\frac{Y_t - \hat{Y}_t}{Y_t}\right|$

  MAPE表示预测值偏离实际值的平均百分比，直观易懂，适合向业务方汇报。缺点是当实际值为0时无定义。

- **RMSE**（Root Mean Squared Error）：$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{t=1}^{n}(Y_t - \hat{Y}_t)^2}$

  RMSE对大误差更敏感（平方惩罚），单位与原始数据一致。适合关注极端偏差的场景。

- **MASE**（Mean Absolute Scaled Error）：$\text{MASE} = \frac{\text{MAE}}{\frac{1}{n-1}\sum_{t=2}^{n}|Y_t - Y_{t-1}|}$

  MASE将MAE除以朴素预测法（用上一期值预测下一期）的MAE。MASE < 1 表示模型优于朴素预测，MASE > 1 表示模型不如朴素预测。MASE对不同尺度的时间序列具有可比性，是学术界推荐的标准指标。

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 时间序列交叉验证
def tscv_evaluate(series, order=(1,1,1), h=6, n_splits=3):
    """时间序列交叉验证"""
    n = len(series)
    results = []
    for i in range(n_splits):
        train_end = n - (n_splits - i) * h
        train = series[:train_end]
        test = series[train_end:train_end + h]

        model = ARIMA(train, order=order)
        result = model.fit()
        forecast = result.forecast(steps=h)

        mape = np.mean(np.abs((test - forecast) / test)) * 100
        rmse = np.sqrt(mean_squared_error(test, forecast))
        naive_mae = np.mean(np.abs(test - series[train_end-1:train_end+h-1].values))
        mae = mean_absolute_error(test, forecast)
        mase = mae / naive_mae if naive_mae > 0 else float('inf')

        results.append({'split': i+1, 'MAPE': mape, 'RMSE': rmse, 'MASE': mase})

    return pd.DataFrame(results)

eval_results = tscv_evaluate(ts, order=best_order)
print("ARIMA时间序列交叉验证结果:")
print(eval_results)
print(f"\n平均MAPE: {eval_results['MAPE'].mean():.2f}%")
print(f"平均RMSE: {eval_results['RMSE'].mean():.2f}")
print(f"平均MASE: {eval_results['MASE'].mean():.2f} ({'优于' if eval_results['MASE'].mean() < 1 else '劣于'}朴素预测)")
```

> 💡 **售前洞察**：当客户要求"销售预测"时，不要只给一个预测值。用Prophet同时输出预测区间（置信区间）、趋势分解图和节日效应分析，展示出"预测+归因"的综合能力，方案含金量立刻提升。

---

### Day 2：蒙特卡洛模拟与优化方法

#### 一、蒙特卡洛模拟原理

蒙特卡洛模拟（Monte Carlo Simulation）是一种通过大量随机采样来近似求解复杂问题的数值方法。其理论基础是**大数定律**：当采样次数足够多时，样本均值的期望收敛于总体均值。

**核心步骤**：
1. 定义输入变量的概率分布（如营销转化率服从Beta分布，客单价服从对数正态分布）
2. 从每个分布中随机采样
3. 计算目标输出值（如ROI）
4. 重复步骤2-3数千次
5. 统计输出的分布特征（均值、标准差、分位数）

**大数定律**：$\bar{X}_n = \frac{1}{n}\sum_{i=1}^{n}X_i \xrightarrow{P} \mu$，当 $n \to \infty$

这意味着采样次数越多，模拟结果越接近真实分布。实践中10000次采样通常足够稳定。

**方差缩减技术**：当直接随机采样效率不够高时，可以使用重要性采样（Importance Sampling）、分层采样（Stratified Sampling）或对立变量法（Antithetic Variates）来减少估计方差，从而在相同采样次数下获得更高精度。

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 16: [Sampling Methods](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/16-sampling-methods)
> 预计时长：~75 min

#### 二、蒙特卡洛模拟：营销预算风险评估

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 10000  # 采样次数

# === 定义营销漏斗各环节的概率分布 ===

# 1. 广告曝光量（正态分布）
impressions = np.random.normal(500000, 50000, N)

# 2. 点击率 CTR（Beta分布，均值约2%，标准差0.5%）
ctr = np.random.beta(8, 392, N)  # Beta(8, 392) 均值≈0.02

# 3. 落地页转化率（正态分布，截断到[0,1]）
landing_rate = np.random.normal(0.35, 0.05, N)
landing_rate = np.clip(landing_rate, 0, 1)

# 4. 注册转化率（Beta分布）
signup_rate = np.random.beta(15, 35, N)  # 均值≈0.30

# 5. 购买转化率（Beta分布）
purchase_rate = np.random.beta(5, 45, N)  # 均值≈0.10

# 6. 客单价（对数正态分布，反映右偏分布）
avg_order_value = np.random.lognormal(mean=5.3, sigma=0.3, N)  # 均值≈200元

# 7. 营销成本（固定+随机）
ad_cost = 500000  # 广告投放成本固定50万
variable_cost = np.random.normal(50000, 5000, N)  # 变动成本

# === 计算每次模拟的ROI ===

clicks = impressions * ctr
landings = clicks * landing_rate
signups = landings * signup_rate
purchases = signups * purchase_rate
revenue = purchases * avg_order_value
total_cost = ad_cost + variable_cost
roi = (revenue - total_cost) / total_cost

# === 结果分析 ===

print("=== 营销预算蒙特卡洛模拟结果（10000次）===")
print(f"预期收入: {revenue.mean():,.0f}元 (±{revenue.std():,.0f})")
print(f"预期ROI: {roi.mean():.1%} (±{roi.std():.1%})")
print(f"ROI中位数: {np.median(roi):.1%}")
print(f"\n风险分析:")
print(f"  亏损概率 (ROI<0): {(roi < 0).mean():.1%}")
print(f"  低收益概率 (ROI<10%): {(roi < 0.10).mean():.1%}")
print(f"  高收益概率 (ROI>50%): {(roi > 0.50).mean():.1%}")
print(f"\n分位数分析:")
print(f"  5%分位 (悲观): ROI = {np.percentile(roi, 5):.1%}")
print(f"  50%分位 (中位): ROI = {np.percentile(roi, 50):.1%}")
print(f"  95%分位 (乐观): ROI = {np.percentile(roi, 95):.1%}")

# 可视化ROI分布
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(roi, bins=50, density=True, alpha=0.7, color='steelblue', edgecolor='white')
axes[0].axvline(x=0, color='red', linestyle='--', label='盈亏平衡线')
axes[0].axvline(x=roi.mean(), color='orange', linestyle='-', label=f'均值: {roi.mean():.1%}')
axes[0].set_xlabel('ROI'); axes[0].set_ylabel('密度')
axes[0].set_title('ROI概率分布'); axes[0].legend()

# 累积分布函数
sorted_roi = np.sort(roi)
cdf = np.arange(1, N+1) / N
axes[1].plot(sorted_roi, cdf, color='steelblue')
axes[1].axhline(y=0.05, color='red', linestyle='--', label='5%分位')
axes[1].axvline(x=0, color='gray', linestyle=':', label='盈亏平衡')
axes[1].set_xlabel('ROI'); axes[1].set_ylabel('累积概率')
axes[1].set_title('ROI累积分布函数（CDF）'); axes[1].legend()
plt.tight_layout(); plt.savefig('monte_carlo_roi.png', dpi=150)
plt.show()
```

> 💡 **售前洞察**：蒙特卡洛模拟的核心价值不是给出一个精确数字，而是给出一个**概率分布**。当你告诉客户"这个营销方案有85%的概率ROI超过20%，但有5%的概率亏损"，比给出"预期ROI是25%"有价值得多——因为客户真正关心的是风险，而不仅仅是期望收益。

#### 三、线性规划

线性规划（Linear Programming, LP）是在线性约束条件下最大化或最小化线性目标函数的优化方法。

**标准形式**：

$$\min \mathbf{c}^T \mathbf{x}$$

$$\text{s.t.} \quad A\mathbf{x} \leq \mathbf{b}$$

$$\mathbf{x} \geq 0$$

其中 $\mathbf{x}$ 是决策变量向量，$\mathbf{c}$ 是成本系数向量，$A$ 是约束矩阵，$\mathbf{b}$ 是约束上限向量。

**单纯形法**（Simplex Method）是求解线性规划的经典算法，通过在可行域的顶点之间移动来寻找最优解。**对偶理论**（Duality）指出每个线性规划问题都有一个对偶问题，对偶变量的经济学含义是**影子价格**——即放宽某个约束条件所带来的目标函数改善量。

**营销应用：多渠道预算最优分配**

假设有5个营销渠道（搜索广告、信息流广告、社交媒体、邮件营销、KOL合作），总预算1000万，如何分配才能最大化总转化数？

```python
from scipy.optimize import linprog

# 5个渠道：搜索广告、信息流广告、社交媒体、邮件营销、KOL合作
channels = ['搜索广告', '信息流广告', '社交媒体', '邮件营销', 'KOL合作']

# 每万元投入的转化数（基于历史数据估算）
conversions_per_10k = [15, 12, 8, 25, 10]

# 线性规划求最大化 -> 转为最小化负值
c = [-conv for conv in conversions_per_10k]  # 取负因为linprog默认最小化

# 约束条件
# 1. 总预算 <= 1000万（即1000个"万元"单位）
# 2. 每个渠道最低投入 >= 50万
# 3. 搜索广告+信息流广告 <= 500万（数字广告总预算上限）
# 4. KOL合作 <= 200万（KOL合作预算上限）

A_ub = [
    [1, 1, 1, 1, 1],       # 总预算约束
    [1, 1, 0, 0, 0],       # 数字广告上限
    [0, 0, 0, 0, 1],       # KOL上限
]
b_ub = [1000, 500, 200]  # 对应上限值（万元单位）

# 变量下界：每个渠道至少50万
bounds = [(50, None), (50, None), (50, None), (50, None), (50, None)]

# 求解
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.success:
    budget = result.x
    total_conversions = -result.fun

    print("=== 多渠道预算最优分配方案 ===")
    print(f"总预算: {sum(budget):.0f}万元")
    print(f"总转化数: {total_conversions:.0f}")
    print()
    for ch, b in zip(channels, budget):
        conv = b * conversions_per_10k[channels.index(ch)]
        print(f"  {ch}: {b:.0f}万元 -> {conv:.0f}转化 (效率: {conv/b:.1f}转化/万元)")

    # 对偶变量（影子价格）分析
    print(f"\n=== 影子价格分析 ===")
    print(f"总预算约束的影子价格: {-result.ineqlin.marginals[0]:.2f} 转化/万元")
    print("  含义: 每增加1万元总预算，可增加{-result.ineqlin.marginals[0]:.2f}个转化")
    print(f"数字广告上限的影子价格: {-result.ineqlin.marginals[1]:.2f} 转化/万元")
    print(f"KOL上限的影子价格: {-result.ineqlin.marginals[2]:.2f} 转化/万元")
else:
    print(f"求解失败: {result.message}")
```

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 18: [Convex Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/18-convex-optimization)
> 预计时长：~90 min

#### 四、非线性优化

当目标函数或约束条件是非线性的，需要使用非线性优化方法。

**梯度下降法**（Gradient Descent）：沿目标函数的负梯度方向迭代更新：

$$\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha \nabla f(\mathbf{x}_k)$$

其中 $\alpha$ 是学习率，$\nabla f(\mathbf{x}_k)$ 是梯度。梯度下降简单但收敛慢，且可能陷入局部最优。

**牛顿法**（Newton's Method）：利用二阶导数（Hessian矩阵）加速收敛：

$$\mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$$

牛顿法收敛速度快（二次收敛），但需要计算和存储Hessian矩阵，在高维问题中计算代价高。

**拉格朗日乘子法**（Lagrange Multipliers）：用于求解等式约束优化问题。构造拉格朗日函数：

$$\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_i \lambda_i g_i(\mathbf{x})$$

其中 $g_i(\mathbf{x}) = 0$ 是等式约束，$\lambda_i$ 是拉格朗日乘子。最优解满足 $\nabla \mathcal{L} = 0$。

**KKT条件**（Karush-Kuhn-Tucker Conditions）是拉格朗日乘子法在不等式约束下的推广，是非线性优化最优性的必要条件（在凸优化条件下也是充分条件）。

**营销应用：定价优化**

假设需求量与价格的关系为：$Q = a - b \times P$（线性需求曲线）。利润函数为：

$$\pi(P) = (P - C) \times Q = (P - C) \times (a - b \times P)$$

其中 $C$ 是单位成本。最优价格 $P^* = \frac{a + b \times C}{2b}$。但当需求函数更复杂（如考虑价格弹性随价格变化、竞争对手反应等），解析解不可行，需要数值优化。

```python
from scipy.optimize import minimize
import numpy as np

# 定价优化：最大化利润
# 需求模型: Q = 10000 * P^(-1.5) * (1 + 0.3*seasonality)  (非线性需求曲线)
# 成本模型: C = 30 + 0.001 * Q  (规模效应降低单位成本)
# 利润: profit = (P - C) * Q

def negative_profit(price, seasonality=1.0):
    """计算负利润（用于最小化）"""
    P = price[0]
    Q = 10000 * (P ** (-1.5)) * (1 + 0.3 * seasonality)
    C = 30 + 0.001 * Q
    profit = (P - C) * Q
    return -profit

# 不同季节的最优定价
seasons = {'淡季': 0.5, '平季': 1.0, '旺季': 1.5}

print("=== 定价优化结果 ===")
for season_name, seasonality in seasons.items():
    result = minimize(
        negative_profit,
        x0=[80],  # 初始价格
        args=(seasonality,),
        method='Nelder-Mead',
        bounds=[(20, 300)]
    )
    optimal_price = result.x[0]
    optimal_Q = 10000 * (optimal_price ** (-1.5)) * (1 + 0.3 * seasonality)
    optimal_C = 30 + 0.001 * optimal_Q
    optimal_profit = (optimal_price - optimal_C) * optimal_Q

    print(f"\n{season_name} (seasonality={seasonality}):")
    print(f"  最优价格: {optimal_price:.2f}元")
    print(f"  预期销量: {optimal_Q:.0f}件")
    print(f"  单位成本: {optimal_C:.2f}元")
    print(f"  最大利润: {optimal_profit:,.0f}元")
    print(f"  利润率: {optimal_profit/(optimal_price*optimal_Q):.1%}")
```

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 08: [Optimization: Gradient Descent Family](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/08-optimization)
> 预计时长：~75 min

#### 五、整数规划与启发式算法简介

**整数规划**（Integer Programming）要求决策变量取整数值。营销中的典型场景是广告位购买——你不能买3.7个广告位。混合整数规划（MIP）允许部分变量为实数、部分为整数。

**遗传算法**（Genetic Algorithm）模拟生物进化过程：通过选择（Selection）、交叉（Crossover）和变异（Mutation）在解空间中搜索全局最优。适合目标函数不可导、解空间不规则的复杂优化问题。

**模拟退火**（Simulated Annealing）受金属退火过程启发：以一定概率接受比当前解更差的解，从而跳出局部最优。温度参数随迭代降低，搜索从全局探索逐渐收敛到局部精细搜索。

```python
# 用scipy的差分进化（一种进化算法）求解非线性优化
from scipy.optimize import differential_evolution

def multi_channel_roi(budget_allocation):
    """多渠道ROI的非线性优化目标函数
    考虑边际递减效应：投入越多，边际转化越低
    """
    total_budget = 1000
    # 非线性转化函数：conv_i = a_i * x_i^0.7 (边际递减)
    a = [15, 12, 8, 25, 10]
    conversions = sum(a[i] * (b ** 0.7) for i, b in enumerate(budget_allocation))

    # 惩罚项：总预算偏离约束
    penalty = abs(sum(budget_allocation) - total_budget) * 100
    return -(conversions - penalty)

bounds = [(50, 400)] * 5  # 每个渠道50-400万
result = differential_evolution(multi_channel_roi, bounds, seed=42, maxiter=200)

print("=== 差分进化算法求解（考虑边际递减）===")
for ch, b in zip(channels, result.x):
    print(f"  {ch}: {b:.0f}万元")
print(f"总转化数: {-result.fun:.0f}")
print(f"总预算: {sum(result.x):.0f}万元")
```

#### 六、营销案例：全年营销预算优化方案

综合蒙特卡洛模拟和优化方法，构建一个完整的全年营销预算优化方案：

```python
"""
全年营销预算优化Pipeline
输入：年度预算、历史转化数据、季节性系数
输出：月度x渠道的最优预算分配矩阵
"""
import numpy as np
from scipy.optimize import linprog

# === 输入参数 ===
annual_budget = 1200  # 全年1200万
channels = ['搜索广告', '信息流广告', '社交媒体', '邮件营销', 'KOL合作']
n_channels = len(channels)
n_months = 12

# 月度季节性系数（1.0为平均水平）
seasonality = [0.8, 0.7, 0.9, 1.0, 1.2, 1.5,  # 上半年：春节低、618高
               0.9, 0.8, 1.0, 1.1, 1.8, 1.6]  # 下半年：双11最高

# 各渠道基础转化效率（转化/万元）
base_efficiency = [15, 12, 8, 25, 10]

# === 构建线性规划 ===
# 决策变量：12个月 x 5个渠道 = 60个变量
# x[i*n_channels + j] = 第i月渠道j的预算（万元）

c = []  # 目标函数系数（负转化数）
for i in range(n_months):
    for j in range(n_channels):
        # 转化数 = 效率 * 预算 * 季节性
        c.append(-base_efficiency[j] * seasonality[i])

# 约束
A_ub = []
b_ub = []

# 约束1：总预算 <= 1200万
row = [1] * (n_months * n_channels)
A_ub.append(row); b_ub.append(annual_budget)

# 约束2：每月总预算 >= 月度最低（50万）
for i in range(n_months):
    row = [0] * (n_months * n_channels)
    for j in range(n_channels):
        row[i * n_channels + j] = 1
    A_ub.append([-x for x in row])  # -sum >= -50 => sum <= 50的反向
    b_ub.append(-50)

# 约束3：每个渠道全年预算 >= 100万
for j in range(n_channels):
    row = [0] * (n_months * n_channels)
    for i in range(n_months):
        row[i * n_channels + j] = 1
    A_ub.append([-x for x in row])
    b_ub.append(-100)

# 变量下界
bounds = [(0, None)] * (n_months * n_channels)

# 求解
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.success:
    budget_matrix = result.x.reshape(n_months, n_channels)
    total_conversions = -result.fun

    print("=== 全年营销预算最优分配方案 ===")
    print(f"年度总预算: {annual_budget}万元")
    print(f"预期总转化: {total_conversions:.0f}")
    print()

    # 打印月度x渠道矩阵
    header = "月份  " + "  ".join(f"{ch:>8s}" for ch in channels) + "  |  合计"
    print(header)
    print("-" * len(header))
    for i in range(n_months):
        row_str = f"{i+1:2d}月  "
        for j in range(n_channels):
            row_str += f"{budget_matrix[i,j]:8.0f}"
        row_str += f"  |  {budget_matrix[i].sum():.0f}"
        print(row_str)

    print("-" * len(header))
    col_str = "合计  "
    for j in range(n_channels):
        col_str += f"{budget_matrix[:,j].sum():8.0f}"
    col_str += f"  |  {budget_matrix.sum():.0f}"
    print(col_str)
else:
    print(f"求解失败: {result.message}")
```

#### 七、LLM辅助统计推断与AI优化

> **2026前沿补丁**：本节探索LLM如何增强传统统计推断和优化方法，从"自动化计算"升级为"智能辅助决策"。

**1. LLM辅助贝叶斯推断**

贝叶斯推断的核心是先验分布（Prior）的选择，这通常依赖领域专家的经验。LLM在三个方面增强贝叶斯推断：

**用LLM设定先验**：将领域知识转化为先验分布是贝叶斯建模中最主观也最困难的步骤。LLM可以阅读领域文献、分析历史数据，自动建议合理的先验分布。例如，在预测某新品类产品的转化率时，LLM可以基于行业常识建议"电商新品类的转化率通常在1%-5%之间，符合Beta(2, 50)分布"。

**LLM辅助MCMC**：马尔可夫链蒙特卡洛（MCMC）的效率高度依赖提议分布（Proposal Distribution）的选择。LLM可以根据目标分布的特征，智能建议提议分布的参数，加速收敛。虽然LLM不能直接替代MCMC算法，但可以在初始化阶段提供更好的起点。

**用LLM解释统计结果**：将p值、置信区间、后验分布等统计概念转化为业务语言。例如，LLM将"p=0.03，95% CI: [0.02, 0.15]"翻译为"有97%的置信度认为这个广告渠道带来了2%-15%的增量转化，最可能在8%左右"。

**2. AI驱动的优化**

**LLM作为优化器**：对于离散优化问题（如排班、路径规划），LLM可以通过推理直接生成候选解。虽然LLM不擅长精确数值优化，但在组合优化中可以快速生成合理方案，再用传统算法精调。

**Bayesian Optimization + LLM**：贝叶斯优化（BO）用于黑盒函数优化，需要定义搜索空间。LLM可以根据问题描述建议搜索空间的范围和关键参数。例如，在超参数优化中，LLM建议"学习率应在0.0001-0.01之间，batch size应为2的幂次"。

**演化算法 + LLM**：在遗传算法中，LLM可以替代随机变异操作，进行"智能变异"--根据当前解的特征，LLM生成有方向性的变异，加速收敛。这在代码优化和创意生成场景中特别有效。

**3. 营销预算分配的AI增强**

传统预算分配依赖线性规划或梯度下降，需要预先固定约束条件。AI增强的预算分配可以动态调整：

| 方法 | 优势 | 局限 |
|------|------|------|
| 传统线性规划 | 精确、可解释 | 约束固定，无法适应市场变化 |
| LLM增强 | 理解市场环境，动态调整约束 | 结果非确定性，需要验证 |
| 强化学习 | 实时优化，从反馈中学习 | 需要大量交互数据，冷启动难 |

LLM增强的预算分配流程：LLM分析市场环境（竞品动态、季节性、经济指标）-> 建议调整约束条件（如"双11前应增加社交渠道预算上限"）-> 线性规划求解 -> LLM验证结果合理性 -> 如不合理则调整约束重新求解。

**4. Python实战：LLM辅助贝叶斯先验设定**

```python
from openai import OpenAI
import numpy as np
import pymc as pm
import json

client = OpenAI()

def llm_suggest_prior(product_category, historical_data_summary):
    """用LLM根据领域知识建议贝叶斯先验分布"""

    prompt = f"""
    你是一位营销分析专家。请根据以下信息，为一个贝叶斯模型建议先验分布。

    产品类别：{product_category}
    历史数据摘要：{json.dumps(historical_data_summary, ensure_ascii=False)}

    我们要预测的参数是：该产品的转化率（conversion rate）

    请建议：
    1. prior_distribution: 先验分布类型（如Beta、Normal等）
    2. parameters: 分布参数（如Beta的alpha和beta值）
    3. reasoning: 选择这个先验的理由
    4. expected_range: 预期转化率的合理范围

    以JSON格式输出。
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)


def compare_bayesian_inference(observed_data, llm_prior, default_prior=(1, 1)):
    """对比有/无LLM先验的贝叶斯推断效果"""

    # 方法1：使用LLM建议的先验
    alpha_llm, beta_llm = llm_prior
    with pm.Model() as model_llm:
        p = pm.Beta('conversion_rate', alpha=alpha_llm, beta=beta_llm)
        obs = pm.Binomial('obs', n=len(observed_data), p=p,
                          observed=np.sum(observed_data))
        trace_llm = pm.sample(2000, tune=1000, chains=2, progressbar=False)

    # 方法2：使用无信息先验 Beta(1,1) = Uniform(0,1)
    alpha_default, beta_default = default_prior
    with pm.Model() as model_default:
        p = pm.Beta('conversion_rate', alpha=alpha_default, beta=beta_default)
        obs = pm.Binomial('obs', n=len(observed_data), p=p,
                          observed=np.sum(observed_data))
        trace_default = pm.sample(2000, tune=1000, chains=2, progressbar=False)

    # 对比结果
    llm_mean = trace_llm.posterior['conversion_rate'].mean().values
    llm_hdi = pm.hdi(trace_llm, hdi_prob=0.95)['conversion_rate'].values
    default_mean = trace_default.posterior['conversion_rate'].mean().values
    default_hdi = pm.hdi(trace_default, hdi_prob=0.95)['conversion_rate'].values

    print("=== 贝叶斯推断对比 ===")
    print(f"观测数据: {len(observed_data)}次曝光, {np.sum(observed_data)}次转化")
    print(f"观测转化率: {np.mean(observed_data):.4f}")
    print(f"\nLLM先验 Beta({alpha_llm}, {beta_llm}):")
    print(f"  后验均值: {llm_mean:.4f}")
    print(f"  95% HDI: [{llm_hdi[0]:.4f}, {llm_hdi[1]:.4f}]")
    print(f"  区间宽度: {llm_hdi[1] - llm_hdi[0]:.4f}")
    print(f"\n无信息先验 Beta({alpha_default}, {beta_default}):")
    print(f"  后验均值: {default_mean:.4f}")
    print(f"  95% HDI: [{default_hdi[0]:.4f}, {default_hdi[1]:.4f}]")
    print(f"  区间宽度: {default_hdi[1] - default_hdi[0]:.4f}")
    print(f"\nHDI宽度缩减: {(1 - (llm_hdi[1]-llm_hdi[0])/(default_hdi[1]-default_hdi[0])):.1%}")
    print("（LLM先验通过引入领域知识，缩小了不确定性区间）")

    return trace_llm, trace_default


# ===== 示例使用 =====
# 模拟历史数据摘要
historical_summary = {
    "category": "电商美妆类",
    "avg_conversion_rate_history": 0.035,
    "std_conversion_rate": 0.012,
    "sample_size": "约5000次曝光",
    "seasonality": "Q4转化率较高"
}

# Step 1: 用LLM建议先验
prior_suggestion = llm_suggest_prior("美妆产品", historical_summary)
print("LLM建议的先验分布:")
print(json.dumps(prior_suggestion, ensure_ascii=False, indent=2))

# Step 2: 生成模拟观测数据
np.random.seed(42)
n_exposures = 200
true_rate = 0.04  # 真实转化率4%
observed = np.random.binomial(1, true_rate, n_exposures)

# Step 3: 对比有/无LLM先验的推断效果
# 从LLM建议中提取先验参数
llm_alpha = prior_suggestion.get('parameters', {}).get('alpha', 3)
llm_beta = prior_suggestion.get('parameters', {}).get('beta', 80)

trace_llm, trace_default = compare_bayesian_inference(
    observed, (llm_alpha, llm_beta)
)
```

**代码解读**：这段代码展示了LLM如何增强贝叶斯推断。核心逻辑：(1)`llm_suggest_prior`让LLM基于领域知识建议先验分布参数；(2)`compare_bayesian_inference`对比LLM先验和无信息先验的推断结果。关键发现：当观测数据量有限时（如200次曝光），有信息的LLM先验能显著缩小后验的置信区间（HDI），提供更精确的估计。当数据量充足时，先验的影响减弱（数据"覆盖"了先验）。这正是贝叶斯方法的核心思想：小数据时先验重要，大数据时数据主导。

#### 八、跨学科桥梁：医疗统计与政策优化

**医疗统计：临床试验的自适应设计**

临床试验是贝叶斯方法的重要应用领域。传统临床试验使用固定设计（预先确定样本量和停止规则），而自适应设计（Adaptive Design）允许根据中期分析结果调整试验参数。LLM增强的自适应设计可以：(1)分析历史临床试验数据，建议合理的先验分布；(2)在中期分析时，LLM解释统计结果并建议是否调整样本量或停止试验；(3)自动生成临床试验报告的统计部分。FDA和NMPA都已发布自适应设计的指导原则。

**政策优化：政策参数的贝叶斯优化**

公共政策制定中，政策参数（如税率、补贴额度、准入门槛）的优化是一个黑盒优化问题--政策效果需要时间显现且受多重混杂因素影响。贝叶斯优化适合这类昂贵的黑盒优化：(1)用高斯过程建模政策参数与社会效果的关系；(2)用采集函数（Acquisition Function）建议下一个"最有信息量"的政策参数组合；(3)LLM分析政策环境和历史数据，为贝叶斯优化提供搜索空间建议和约束条件。典型应用：城市交通限行政策的参数优化、教育资源分配优化。

> 💡 **售前洞察**：LLM辅助统计推断是面向学术型客户（高校、研究机构、政府智库）的差异化能力。当客户看到你不仅会跑统计模型，还能用LLM将领域知识转化为先验分布、自动解释统计结果，方案的可信度显著提升。关键卖点：从"纯数据驱动"到"数据+知识双轮驱动"，在小数据场景下利用领域知识弥补数据不足。

---

### Day 3：R语言基础与统计应用

#### 一、R环境搭建

R是统计分析和数据科学领域的经典工具，在学术界（尤其是统计学院和生物统计领域）占据主导地位。对于商业博士学习者，掌握R语言有两个价值：一是能阅读和复现大量使用R编写的统计研究论文；二是R的某些统计包（如时间序列、生存分析、计量经济学）在功能上领先于Python。

**核心工具链**：
- **RStudio**：R的集成开发环境（IDE），提供代码编辑、控制台、变量浏览、可视化面板
- **tidyverse**：R的数据科学工具包集合，包含dplyr（数据操作）、ggplot2（可视化）、tidyr（数据整理）、readr（数据读取）等
- **R Markdown**：将R代码、分析文本和可视化结果整合为可重现的研究报告

```r
# R环境安装（在RStudio Console中执行）
# install.packages("tidyverse")  # 核心数据科学包
# install.packages("lubridate")  # 日期时间处理
# install.packages("forecast")   # 时间序列预测
# install.packages("car")        # 回归诊断

# 加载核心包
library(tidyverse)
library(lubridate)
library(forecast)
```

#### 二、R数据操作：dplyr与tidyr

dplyr是R中最强大的数据操作包，其核心动词（verbs）构成了数据操作的语法体系：

| 函数 | 功能 | Python等效 |
|------|------|-----------|
| `filter()` | 按条件筛选行 | `df[df.col > x]` |
| `mutate()` | 创建或修改列 | `df['new'] = ...` |
| `summarise()` | 汇总统计 | `df.groupby().agg()` |
| `arrange()` | 排序 | `df.sort_values()` |
| `select()` | 选择列 | `df[['col1','col2']]` |
| `group_by()` | 分组 | `df.groupby()` |
| `left_join()` | 合并 | `pd.merge()` |

```r
# === 营销数据分析示例 ===

# 创建模拟营销数据
set.seed(42)
marketing_data <- tibble(
  date = seq(as.Date('2024-01-01'), as.Date('2024-12-31'), by='day'),
  channel = sample(c('搜索广告', '信息流广告', '社交媒体', '邮件营销'), 366, replace=TRUE),
  impressions = round(runif(366, 1000, 50000)),
  clicks = round(runif(366, 50, 2000)),
  conversions = round(runif(366, 1, 80)),
  spend = round(runif(366, 100, 5000), 2)
)

# dplyr数据操作链
channel_summary <- marketing_data %>%
  mutate(
    ctr = clicks / impressions,           # 点击率
    cvr = conversions / clicks,            # 转化率
    cpa = spend / conversions,             # 每转化成本
    month = month(date, label=TRUE)        # 提取月份
  ) %>%
  group_by(channel, month) %>%
  summarise(
    total_spend = sum(spend),
    total_conversions = sum(conversions),
    avg_ctr = mean(ctr),
    avg_cpa = mean(cpa, na.rm=TRUE),
    .groups = 'drop'
  ) %>%
  mutate(
    roi = total_conversions / total_spend * 100  # 简化ROI
  ) %>%
  arrange(desc(roi))  # 按ROI降序排列

print(channel_summary)
```

#### 三、R数据可视化：ggplot2

ggplot2基于**图层语法**（Grammar of Graphics），通过叠加图层来构建图表。核心组件：

1. **数据**（data）：数据框
2. **美学映射**（aesthetic mapping）：将数据列映射到视觉属性（x/y轴、颜色、大小、形状）
3. **几何对象**（geom）：图表类型（geom_point散点图、geom_line折线图、geom_bar柱状图）
4. **标度**（scale）：控制视觉属性的映射方式（颜色标度、坐标轴范围）
5. **主题**（theme）：控制非数据元素（标题、网格线、字体）

```r
# ggplot2可视化
library(ggplot2)

# 图1：月度x渠道的CPA热力图
p1 <- ggplot(channel_summary, aes(x=month, y=channel, fill=avg_cpa)) +
  geom_tile(color='white', linewidth=0.5) +
  scale_fill_gradient(low='#2ecc71', high='#e74c3c') +
  labs(title='各渠道月度CPA热力图',
       x='月份', y='渠道', fill='平均CPA(元)') +
  theme_minimal(base_size=12) +
  theme(axis.text.x = element_text(angle=45, hjust=1))

# 图2：ROI趋势折线图
p2 <- ggplot(channel_summary, aes(x=month, y=roi, group=channel, color=channel)) +
  geom_line(linewidth=1) +
  geom_point(size=2) +
  labs(title='各渠道月度ROI趋势',
       x='月份', y='ROI(转化/支出×100)', color='渠道') +
  theme_minimal(base_size=12) +
  theme(legend.position='bottom')

# 保存图表
ggsave('r_cpa_heatmap.png', p1, width=10, height=5, dpi=150)
ggsave('r_roi_trend.png', p2, width=10, height=5, dpi=150)
print(p1)
print(p2)
```

#### 四、R统计建模

R的统计建模函数简洁而强大：

```r
# === 线性回归：营销支出对转化的影响 ===
model_lm <- lm(conversions ~ spend + channel, data=marketing_data)
summary(model_lm)

# 回归诊断
par(mfrow=c(2,2))
plot(model_lm)  # 残差图、QQ图、杠杆图
par(mfrow=c(1,1))

# === 广义线性模型：泊松回归（计数数据） ===
model_glm <- glm(conversions ~ spend + channel, data=marketing_data, family=poisson)
summary(model_glm)

# === 时间序列建模 ===
# 创建月度时间序列
monthly_sales <- marketing_data %>%
  mutate(month = floor_date(date, 'month')) %>%
  group_by(month) %>%
  summarise(total_spend = sum(spend), total_conv = sum(conversions)) %>%
  pull(total_conv)

ts_data <- ts(monthly_sales, frequency=12, start=c(2024,1))

# ARIMA自动建模
auto_model <- auto.arima(ts_data)
summary(auto_model)

# 预测未来3个月
forecast_result <- forecast(auto_model, h=3)
print(forecast_result)
plot(forecast_result, main='R ARIMA月度转化预测')

# === t检验：A/B测试 ===
# 假设有两组广告创意的转化数据
group_a <- c(45, 52, 48, 55, 50, 47, 53, 49, 51, 46)
group_b <- c(58, 61, 55, 63, 59, 57, 62, 60, 56, 58)

t_test_result <- t.test(group_a, group_b, alternative='two.sided')
print(t_test_result)
cat("\n结论: ", if(t_test_result$p.value < 0.05) "两组差异显著" else "无显著差异", "\n")
```

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 15: [Statistics for ML](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/15-statistics-for-ml)
> 预计时长：~75 min

#### 五、R vs Python对比与协作

| 维度 | Python | R |
|------|--------|---|
| **设计哲学** | 通用编程语言 | 统计分析专用语言 |
| **数据操作** | pandas | dplyr/tidyverse |
| **可视化** | matplotlib/seaborn | ggplot2（更优雅） |
| **统计建模** | statsmodels/scikit-learn | 内置lm/glm + 专业包 |
| **机器学习** | scikit-learn/PyTorch（生态强） | caret/mlr3（较弱） |
| **深度学习** | PyTorch/TensorFlow | reticulate调用Python |
| **研究报告** | Jupyter Notebook | R Markdown（更强大） |
| **学术统计** | 较少专业包 | 生存分析/计量经济学/贝叶斯（领先） |

**协作策略**：在同一个分析项目中，可以用Python做数据获取和机器学习建模，用R做统计检验和可视化，用R Markdown生成最终报告。

#### 六、Python调用R（rpy2）

```python
# 使用rpy2在Python中调用R
# pip install rpy2

import os
os.environ['R_HOME'] = '/usr/local/lib/R'  # 设置R安装路径

import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr

# 激活pandas-R转换
pandas2ri.activate()

# 导入R的base和stats包
base = importr('base')
stats = importr('stats')

# 在Python中创建数据，传给R做统计检验
import numpy as np
group_a = ro.FloatVector([45, 52, 48, 55, 50, 47, 53, 49, 51, 46])
group_b = ro.FloatVector([58, 61, 55, 63, 59, 57, 62, 60, 56, 58])

# 调用R的t.test
t_test = stats.t_test(group_a, group_b, alternative='two.sided')
print(f"R t检验结果:")
print(f"  t统计量: {t_test.rx2('statistic')[0]:.4f}")
print(f"  p-value: {t_test.rx2('p.value')[0]:.4f}")
print(f"  均值差: {t_test.rx2('estimate')[0] - t_test.rx2('estimate')[1]:.2f}")

# 调用R的lm线性回归
import pandas as pd
df = pd.DataFrame({
    'spend': np.random.uniform(100, 5000, 100),
    'channel': np.random.choice(['A', 'B', 'C'], 100)
})
df['conversions'] = df['spend'] * 0.01 + np.random.normal(0, 5, 100)

r_df = pandas2ri.py2rpy(df)
r_formula = ro.Formula('conversions ~ spend + channel')
r_model = stats.lm(formula=r_formula, data=r_df)
print(ro.r('summary')(r_model))
```

#### 七、综合案例：用R完成营销数据分析报告

```r
# === R Markdown营销分析报告模板 ===
# 将以下代码保存为 marketing_report.Rmd 文件
# 在RStudio中点击"Knit"生成HTML/PDF报告

---
title: "2024年度营销数据分析报告"
author: "数据团队"
date: "`r Sys.Date()`"
output: html_document
---

```{r setup, include=FALSE}
library(tidyverse)
library(ggplot2)
library(knitr)
knitr::opts_chunk$set(echo=TRUE, warning=FALSE, message=FALSE)
```

## 1. 数据概览

```{r data-overview}
# 加载数据
data <- read_csv('marketing_data.csv')

# 基本统计
data %>%
  summarise(
    记录数 = n(),
    总支出 = sum(spend),
    总转化 = sum(conversions),
    平均CPA = sum(spend)/sum(conversions)
  ) %>%
  kable(digits=2)
```

## 2. 渠道效率分析

```{r channel-analysis}
channel_stats <- data %>%
  group_by(channel) %>%
  summarise(
    支出 = sum(spend),
    转化 = sum(conversions),
    CPA = sum(spend)/sum(conversions),
    CTR = mean(clicks/impressions)
  ) %>%
  arrange(CPA)

kable(channel_stats, digits=4)

ggplot(channel_stats, aes(x=reorder(channel, -CPA), y=CPA, fill=channel)) +
  geom_bar(stat='identity') +
  labs(title='各渠道CPA对比', x='渠道', y='CPA(元)') +
  theme_minimal()
```

## 3. 回归分析

```{r regression}
model <- lm(conversions ~ spend + channel, data=data)
summary(model)
```

## 4. 结论与建议

基于以上分析，建议将预算从CPA最高的渠道向CPA最低的渠道倾斜，
同时持续监控转化率的季节性波动。
```

> 💡 **售前洞察**：在面向学术型客户（如高校、研究机构）的方案中，展示R Markdown报告能力可以显著提升方案的可信度。R Markdown能将代码、分析、图表和结论整合为一份可复现的研究报告，这正是学术研究的核心要求。

---

## 知识问答（10题）

**Q1**：时间序列的加法模型和乘法模型有什么区别？如何选择？

> **答案要点**：加法模型 $Y_t = T_t + S_t + R_t$ 适用于季节性波动幅度不随趋势变化的情况；乘法模型 $Y_t = T_t \times S_t \times R_t$ 适用于季节性波动幅度随趋势增大而增大的情况。选择方法：观察分解图——如果季节性波动的绝对幅度随时间增大，选乘法模型；如果幅度稳定，选加法模型。营销销售额数据通常适用乘法模型。

**Q2**：ADF检验和KPSS检验的假设方向有何不同？为什么要同时使用？

> **答案要点**：ADF的原假设是"序列非平稳"（存在单位根），KPSS的原假设是"序列平稳"。两者假设方向相反。同时使用可以交叉验证：如果ADF拒绝原假设且KPSS不拒绝原假设，则强证据表明序列平稳。如果两者结论矛盾，说明序列处于平稳/非平稳的边界，需要谨慎判断。

**Q3**：ARIMA(p,d,q)中的p、d、q分别代表什么？如何确定它们的值？

> **答案要点**：p是自回归阶数（AR部分），d是差分阶数（I部分），q是移动平均阶数（MA部分）。确定方法：d通过ADF/KPSS检验确定（差分到平稳为止）；p通过PACF图的截尾点确定；q通过ACF图的截尾点确定。最终用AIC/BIC在候选组合中选优。

**Q4**：Prophet模型相比ARIMA有哪些优势？适合什么场景？

> **答案要点**：Prophet的优势：(1) 自动处理节假日效应（通过holidays参数）；(2) 自动检测变点（趋势突变）；(3) 不要求序列平稳；(4) 可以处理缺失值和异常值；(5) 预测结果自带置信区间。适合包含强季节性、受节假日影响大、趋势可能突变的商业时间序列数据（如电商销售额）。

**Q5**：MAPE、RMSE和MASE三个评估指标各有什么优缺点？

> **答案要点**：MAPE直观（百分比），但对零值无定义且对高值偏差不敏感。RMSE对大误差敏感（平方惩罚），单位与原始数据一致，但不同序列间不可比。MASE将MAE除以朴素预测的MAE，无量纲，不同序列间可比，MASE<1表示优于朴素预测，是学术界推荐的标准指标。

**Q6**：蒙特卡洛模拟的基本原理是什么？采样次数如何确定？

> **答案要点**：原理基于大数定律：通过大量随机采样，用样本分布近似总体分布。采样次数取决于所需精度——通常10000次足够稳定。可以用不同种子重复运行，检查结果是否收敛。方差缩减技术（重要性采样、分层采样）可以在较少采样次数下达到相同精度。

**Q7**：线性规划中影子价格（对偶变量）的经济学含义是什么？

> **答案要点**：影子价格表示放宽某个约束条件一单位时目标函数的改善量。例如，总预算约束的影子价格为5转化/万元，意味着每增加1万元预算可以多获得5个转化。影子价格为0的约束是非紧约束（有松弛），影子价格为正的约束是紧约束（已耗尽）。这对资源分配决策有直接指导意义。

**Q8**：梯度下降法和牛顿法的主要区别是什么？

> **答案要点**：梯度下降只用一阶导数（梯度），每步计算量小但收敛慢（线性收敛），需要调学习率。牛顿法用二阶导数（Hessian矩阵），每步计算量大但收敛快（二次收敛），不需要学习率但需要Hessian可逆。在高维问题中，拟牛顿法（如BFGS）用近似Hessian来平衡计算效率和收敛速度。

**Q9**：R语言中的dplyr管道操作符 %>% 的工作原理是什么？

> **答案要点**：`%>%` 将左边的结果作为右边函数的第一个参数。例如 `data %>% filter(x > 0) %>% select(y, z)` 等价于 `select(filter(data, x > 0), y, z)`。管道操作符使代码从内向外嵌套的函数调用变为从左到右的线性流程，显著提升可读性。R 4.1+ 也支持原生管道 `|>`，功能类似但语法更简洁。

**Q10**：在什么场景下应该选择R而不是Python进行统计分析？

> **答案要点**：(1) 需要使用R独有的统计包（如survival生存分析、plm面板数据、lme4混合效应模型）；(2) 需要生成可复现的研究报告（R Markdown）；(3) 面向学术发表（统计/计量经济学领域R更主流）；(4) 需要高质量统计可视化（ggplot2的图层语法更灵活）；(5) 需要复现使用R编写的论文代码。如果涉及深度学习或大规模数据处理，Python仍是首选。

---

## 作业设计

### 必做作业：月度销售额预测与预算优化

**任务描述**：

使用给定的月度营销销售额数据（36个月），完成以下任务：

1. **时间序列分析**（30分）
   - 对数据进行STL分解，解读趋势和季节性模式
   - 进行平稳性检验（ADF + KPSS），确定差分阶数
   - 绘制ACF/PACF图，初步判断ARIMA参数

2. **模型构建**（30分）
   - 用AIC选择最优ARIMA模型，报告参数和AIC值
   - 用Prophet构建预测模型，加入双11和618节日效应
   - 用时间序列交叉验证比较两个模型的MAPE和MASE

3. **预算优化**（25分）
   - 基于预测的销售额，用线性规划求解下一年5个渠道的预算分配
   - 用蒙特卡洛模拟（5000次）评估最优方案的ROI风险分布
   - 报告ROI的5%、50%和95%分位数

4. **报告撰写**（15分）
   - 将分析过程整理为R Markdown报告，包含代码、图表和结论
   - 给出3条可执行的业务建议

**评估量表**（5分制）：

| 维度 | 5分（优秀） | 3分（合格） | 1分（不合格） |
|------|------------|------------|-------------|
| 技术正确性 | 模型选择有据，诊断完整，优化求解正确 | 模型基本正确，诊断不全 | 模型错误或未做诊断 |
| 代码质量 | 代码完整可运行，注释清晰 | 代码可运行，注释不全 | 代码无法运行 |
| 分析深度 | 多模型比较+风险评估+敏感性分析 | 单模型分析 | 仅描述性分析 |
| 业务洞察 | 建议具体可执行，量化支撑 | 建议方向正确 | 无业务建议 |

### 挑战作业：动态定价优化系统

**任务描述**：

设计一个考虑竞争对手反应的动态定价优化系统：

1. 构建需求函数：$Q_i = f(P_i, P_{comp}, \text{season}, \text{ad\_spend})$，其中 $P_{comp}$ 是竞争对手价格
2. 用scipy.optimize.minimize求解最优定价（考虑约束：$P_i \in [50, 300]$）
3. 用蒙特卡洛模拟评估竞争对手3种定价策略下（降价10%/不变/涨价10%）的利润分布
4. 撰写一页技术方案，说明如何将此系统部署为实时定价引擎

**加分项**：
- 使用差分进化算法求解全局最优
- 考虑库存约束
- 用R Markdown生成双语（中英）报告

---

## 推荐资源清单

### 教材与在线课程

| 资源 | 类型 | 说明 |
|------|------|------|
| Forecasting: Principles and Practice (Hyndman & Athanasopoulos) | 免费在线教材 | 时间序列预测权威教材，R代码，3rd edition |
| Introduction to Statistical Learning (ISLP) | 免费在线教材 | 统计学习经典，Python/R双版本 |
| MIT OCW 15.071 The Analytics Edge | 公开课 | MIT Sloan数据分析课程，含真实案例 |
| Stanford EE364A Convex Optimization (Boyd) | 公开课 | 凸优化理论与应用，Boyd教授授课 |
| R for Data Science (Wickham & Grolemund) | 免费在线教材 | tidyverse官方教材 |

### Python库文档

| 库 | 用途 | 链接 |
|------|------|------|
| statsmodels | 时间序列/统计建模 | https://www.statsmodels.org/ |
| prophet | 时间序列预测 | https://facebook.github.io/prophet/ |
| scipy.optimize | 优化求解 | https://docs.scipy.org/doc/scipy/reference/optimize.html |
| PuLP | 线性/整数规划 | https://coin-or.github.io/pulp/ |

### R包文档

| 包 | 用途 |
|------|------|
| tidyverse (dplyr/ggplot2/tidyr) | 数据操作与可视化 |
| forecast | 时间序列预测（auto.arima） |
| rmarkdown | 可复现研究报告 |
| caret / mlr3 | 机器学习框架 |
| survival | 生存分析 |

### AEFS延伸实践

| AEFS课节 | 课节名称 | 对应本教材内容 |
|---------|---------|-------------|
| P1-08 | Optimization: Gradient Descent Family | Day 2 非线性优化 |
| P1-15 | Statistics for ML | Day 3 R统计建模 |
| P1-16 | Sampling Methods | Day 1/2 采样与蒙特卡洛 |
| P1-18 | Convex Optimization | Day 2 线性规划与凸优化 |
| P1-22 | Stochastic Processes | Day 1 时间序列基础 |
| P2-15 | Time Series Fundamentals | Day 1 时间序列预测 |

---

*本教材将应用统计与优化方法系统融入营销决策场景，从时间序列预测到蒙特卡洛模拟到数学优化，构建了"预测-评估-优化"的完整方法论闭环。通过AEFS的from-scratch延伸实践，学习者可以深入理解每个方法背后的数学原理和实现细节。*
