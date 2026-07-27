# Day 1 真实数据集说明

> v5.0 核心升级：用**真实数据集**替代模拟数据。模拟数据预设了答案，真实数据才能让你学会"现实里的混杂有多脏"。

---

## 主数据集：Lalonde / NSW（已验证，可运行）

**这是什么**：NSW（National Supported Work）职业培训示范实验的真实数据，由 Dehejia & Wahba (1999) 整理，是因果推断领域**最经典的真实教学数据集**，MIT/Stanford/DoWhy/EconML 教程广泛使用。

**为什么用它**：真实存在严重混杂——观测对照组与实验处理组在年龄、教育、种族、前期收入等协变量上分布严重不均，正是"混杂偏差"的最佳教学案例。

**加载方式**（需先 `pip install causaldata`）：

```python
from causaldata import nsw
df = nsw.load_pandas().data
```

**字段**：

| 字段 | 含义 | 营销映射 |
|------|------|---------|
| `treat` | 是否参加培训（1=是，0=否） | 是否收到优惠券/看到广告 |
| `re78` | 1978年真实收入（结果变量） | 转化率/GMV/客单价 |
| `age` | 年龄 | 用户年龄 |
| `education` | 受教育年限 | 用户特征 |
| `black` / `hispanic` | 种族指示 | 用户分群特征 |
| `married` | 是否已婚 | 用户特征 |
| `nodegree` | 是否无学位 | 用户特征 |
| `re74` / `re75` | 1974/1975年收入（前期） | 历史消费（关键混杂） |

**来源与验证**：
- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （v0.1.5, 2024-11, Nick Huntington-Klein 维护，MIT License，已验证存在）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费 Bookdown 版，已验证，2025-10-17 构建，本书代码用 `causaldata` 包，含 NSW 数据）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线版，因果推断经典开源教材，同样使用 NSW 数据）
- DoWhy 官方文档（四步因果分析流程，用真实数据演示）：https://py-why.github.io/dowhy/
- 原始论文：Dehejia, R. & Wahba, S. (1999). "Causal Effects in Nonexperimental Studies." *Journal of the American Statistical Association*.

---

## 营销延伸数据集（自行下载，URL 需验证）

主数据集是职业培训，用于学**方法**。若你想在**真实营销 A/B 测试数据**上练习，推荐：

- **Cookie Cats A/B 测试数据集**：知名移动游戏 A/B 测试（gate 30 vs gate 40），真实留存数据（`retention_1`, `retention_7`, `sum_gamerounds`, `version`）。原始分析见 Rasmus Bååth "A Bayesian approach to A/B testing"。Kaggle 上有多个镜像，**请在 Kaggle 搜索 "cookie cats" 自行下载并验证 URL**（Kaggle slug 历次变动，不在此硬编码固定链接以免失效）。
- **Kaggle Marketing Analytics 数据集**：在 Kaggle 搜索 "marketing A/B test" / "marketing campaign"，选 star 数高、有明确 A/B 分组列的数据集。

> ⚠️ 使用任何自行下载的数据集前，先做 `starter.ipynb` TODO2 的数据探索，确认处理/对照分组列与结果列存在、样本量充足。

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实数据（v5.0） |
|------|----------------|----------------|
| 因果结构 | 你造的，预设已知 | 未知的，需识别 |
| 混杂 | 你设定的，干净 | 真实存在的，脏 |
| 教学价值 | 验证代码能跑 | 学会面对真实混杂 |
| 估计对照 | 估计值≈真实值（你造的） | 估计值是否合理需论证 |
| 结论可信 | 自欺欺人 | 可复现、可质疑 |

**真实即严谨**——这是 v5.0 的哲学增量。
