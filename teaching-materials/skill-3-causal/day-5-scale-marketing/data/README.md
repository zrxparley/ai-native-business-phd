# Day 5 真实数据集说明

> v5.0 核心升级：用**真实数据**驱动规模实验综合案例。MAB 用真实响应率、CATE 用真实协变量，MMM 因需时序媒体数据在 reading.md 给真实数据集指引。

---

## 主数据集：Lalonde / NSW（综合案例 + CATE + MAB 驱动，已验证可运行）

**这是什么**：NSW 职业培训实验真实数据（Dehejia & Wahba 1999）。Day 1 当观测数据做后门调整，Day 2 当 RCT 做 A/B 统计，Day 5 当**综合案例**做 CATE 异质效应 + MAB 自适应实验。

**为什么用它**：
- **CATE**：NSW 有丰富协变量（age/education/re74/re75/...），适合用 CausalForestDML 估计"哪类用户对培训响应最大"--直接对应营销"哪类用户对优惠券响应最大"
- **MAB**：用 NSW 处理组/对照组的真实"响应率"（`re78>0` 比例）作为多臂老虎机的真实 CTR，对比固定 A/B 与 Thompson Sampling 的累计转化损失--用真实统计量驱动 bandit，比纯模拟更贴近现实

**加载方式**（需先 `pip install causaldata`）：

```python
from causaldata import nsw
df = nsw.load_pandas().data
```

**字段与营销映射**：

| 字段 | 含义 | Day 5 角色 | 营销映射 |
|------|------|----------|---------|
| `treat` | 是否参加培训 | 处理 T（CATE + MAB） | 是否收到优惠券/AI推荐 |
| `re78` | 1978 年真实收入 | 结果 Y（CATE） | GMV/转化 |
| `re78 > 0`（衍生） | 是否有收入 | MAB 响应率 | 是否转化（MAB 的 CTR） |
| `age`,`education`,`black`,`hispanic`,`married`,`nodegree`,`re74`,`re75` | 用户画像 | 协变量 X（CATE） | 用户画像/历史消费 |

**来源与验证**：
- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （v0.1.5, 2024-11, MIT License，已验证）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费 Bookdown，已验证，含归因/MMM 章节）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线，含 NSW + 异质效应）
- DoWhy 官方文档：https://py-why.github.io/dowhy/
- econml 官方（CausalForestDML）：https://github.com/py-why/EconML （微软因果ML库，已验证，含 CATE 估计器）

---

## 营销延伸数据集（自行下载，URL 需验证）

### 真实营销 A/B 测试（MAB 回放 + 增量测试）
- **Kaggle marketing A/B test**：在 Kaggle 搜索 "marketing A/B test" / "marketing campaign"，选 star 高、有明确 A/B 分组列的数据集。用于在真实营销 A/B 数据上做 MAB 回放（把分组结果序列回放给 bandit）。
- **Cookie Cats A/B 测试**：知名移动游戏 A/B（gate 30 vs 40），真实留存。Kaggle 搜 "cookie cats" 自行下载验证 URL。

### 真实媒体混合建模数据（MMM）
- **Kaggle Marketing Mix Modeling 数据集**：Kaggle 搜 "marketing mix modeling" / "media mix"，选含多渠道周花费 + 销售的时间序列数据集。用于在真实媒体数据上建 adstock + 饱和回归。
- **谷歌 LightweightMMM**：https://github.com/google/lightweight_mmm （谷歌开源 MMM 库，已验证，含真实样例数据 + 贝叶斯 MMM 实现）--MMM 的工业级工具。

> ⚠️ 使用自行下载的数据前，先做数据探索，确认处理/对照分组列、时序频率、结果列存在。

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实数据（v5.0） |
|------|----------------|----------------|
| MAB 响应率 | 你设的 true CTR | 真实 NSW 估计的响应率 |
| CATE 结构 | 你造的异质效应 | 真实协变量驱动的未知 HTE |
| MMM 时序 | 你造的 adstock | 真实媒体周花费（需下载） |
| 决策可信 | 自欺欺人 | 可复现、可质疑 |

**真实即严谨**--这是 v5.0 的哲学增量。
