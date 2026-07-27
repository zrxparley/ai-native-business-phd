# Day 3 真实数据集说明

> v5.0 核心升级：用**真实数据集**替代模拟数据。Day 3 用两个经典观测因果数据集：NSW+CPS 观测对照（PSM）+ close_college 教育回报（IV）。

---

## 数据集 1：NSW + CPS 观测对照（PSM 用，已验证可运行）

**这是什么**：NSW 职业培训实验的真实处理组 + CPS（Current Population Survey）观测对照组，由 Dehejia & Wahba (1999) 整理。Day 1 用的是 NSW 实验对照组（随机化，均衡）；Day 3 换用 CPS 观测对照组（非随机，严重失衡）--正是 PSM 的用武之地。

**为什么用它**：观测对照组与实验处理组在协变量上**严重失衡**（CPS 是全美代表性样本，NSW 是低收入弱势群体），朴素估计严重有偏，PSM 匹配后才能恢复合理估计--这是 PSM 最经典的真实教学案例。

**加载方式**（需先 `pip install causaldata`）：

```python
from causaldata import nsw_mixtape, cps_mixtape
nsw = nsw_mixtape.load_pandas().data
nsw_treated = nsw[nsw['treat'] == 1]  # NSW 实验处理组
cps = cps_mixtape.load_pandas().data   # CPS 观测对照组（全部 treat=0）
```

**公共支撑限制**（Common Support Restriction）：CPS 全样本（15992 人）与 NSW 处理组（185 人）差异极大，直接匹配效果差。需限制 CPS 为与 NSW 处理组特征相似的子样本：

```python
cps_similar = cps[(cps['age'] <= 40) & (cps['re75'] <= 10000)]
df = pd.concat([nsw_treated, cps_similar], ignore_index=True)
```

**字段**：

| 字段 | 含义 | 营销映射 |
|------|------|---------|
| `treat` | 是否参加培训（1=是，0=否） | 是否收到优惠券/看到广告 |
| `re78` | 1978年真实收入（结果变量） | 转化率/GMV/客单价 |
| `age` | 年龄 | 用户年龄 |
| `educ` | 受教育年限 | 用户特征 |
| `black` / `hisp` | 种族指示 | 用户分群特征 |
| `marr` | 是否已婚 | 用户特征 |
| `nodegree` | 是否无学位 | 用户特征 |
| `re74` / `re75` | 1974/1975年收入（前期） | 历史消费（关键混杂） |

> **注意**：`causaldata` 包中 `nsw_mixtape` 的列名为 `educ`/`hisp`/`marr`（非 `education`/`hispanic`/`married`），与 Day 1 使用的 `nsw` 数据列名不同。

---

## 数据集 2：close_college (Card 1995) 教育回报（IV 用，已验证可运行）

**这是什么**：David Card (1995) 的经典数据，用"是否在四年制大学附近长大"（`nearc4`）作为"受教育年限"（`educ`）的工具变量，估计教育对工资的因果效应。IV 方法最经典的真实教学数据集。

**为什么用它**：教育年限与工资存在未观测混杂（如"个人能力"同时影响教育和工资），OLS 估计有偏。`nearc4` 满足 IV 三条件（相关性：住近大学->多上学；独立性：住址与能力无关；排他性：住址只通过教育影响工资），是 IV 的教科书级案例。

**加载方式**：

```python
from causaldata import close_college
df = close_college.load_pandas().data
```

**关键字段**：

| 字段 | 含义 | 营销映射 |
|------|------|---------|
| `educ` | 受教育年限（内生处理） | 推荐次数 / 曝光深度 |
| `lwage` | 对数工资（结果变量） | 转化率 / GMV |
| `nearc4` | 是否住近四年制大学（工具变量） | 是否有线下门店 / 是否在覆盖区域 |
| `exper` | 工作经验 | 用户生命周期 |
| `black` | 是否黑人 | 用户分群特征 |
| `smsa` | 是否住都市区 | 地域特征 |
| `south` | 是否住南方 | 地域特征 |
| `married` | 是否已婚 | 用户特征 |

---

## 来源与验证

- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （v0.1.5, 2024-11, Nick Huntington-Klein 维护，MIT License，已验证存在，含 `nsw_mixtape`、`cps_mixtape` 和 `close_college` 数据集）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费 Bookdown 版，已验证，本书代码用 `causaldata` 包，含 NSW/CPS 和 Card 数据）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线版，因果推断经典开源教材，含 IV 章节）
- DoWhy 官方文档（四步因果分析流程，支持 PSM 和 IV）：https://py-why.github.io/dowhy/
- 原始论文：
  - Dehejia, R. & Wahba, S. (1999). "Causal Effects in Nonexperimental Studies." *JASA*.
  - Card, D. (1995). "Using Geographic Variation in College Proximity to Estimate the Return to Schooling." *Aspects of Labour Economics*.

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实数据（v5.0） |
|------|----------------|----------------|
| 因果效应 | 你设定的，已知 | 未知的，需估计 |
| 混杂结构 | 你造的，干净 | 真实存在的，脏 |
| IV 有效性 | 你设计的，满足 | 需论证三个条件 |
| 教学价值 | 验证代码能跑 | 学会面对真实混杂 |

**真实即严谨**--这是 v5.0 的哲学增量。
