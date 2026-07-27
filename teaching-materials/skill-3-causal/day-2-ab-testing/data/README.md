# Day 2 真实数据集说明

> v5.0 核心升级：用**真实 RCT 数据**做 A/B 测试统计分析。Day 1 把 NSW 当观测数据，今天把它当本来的面目--真实随机对照试验。

---

## 主数据集：Lalonde / NSW 职业培训实验（真实 RCT，已验证可运行）

**这是什么**：NSW（National Supported Work）职业培训示范实验的真实数据。NSW 本身就是**随机对照试验**（RCT）--处理组随机分配接受职业培训，对照组不接受。是因果推断/A/B 测试教学最经典的真实实验数据集。

**为什么用它**：Day 1 把 NSW 当观测数据（处理组 vs 观测对照组，混杂严重）。今天用 NSW 的**实验对照**（随机化），让你直观对比"随机化消除混杂"的威力--同数据集两视角，Day 1 均值差有偏，今天均值差无偏 = ATE。

**加载方式**（需先 `pip install causaldata`）：

```python
from causaldata import nsw
df = nsw.load_pandas().data
```

**字段与营销映射**：

| 字段 | 含义 | Day 2 角色 | 营销映射 |
|------|------|----------|---------|
| `treat` | 是否参加培训（1=实验组，0=对照组，随机分配） | 处理 T | 是否看到新广告/收到优惠券 |
| `re78` | 1978 年真实收入（实验后） | 结果 Y（连续） | 转化率/GMV/客单价 |
| `re78 > 0`（衍生） | 是否有收入（0/1） | 结果 Y（二值） | 是否转化（比例 Z 检验） |
| `re75` | 1975 年收入（实验前） | CUPED 协变量 | 实验前历史消费/活跃度 |
| `age`,`education`,`black`,`hispanic`,`married`,`nodegree`,`re74` | 用户画像 | 均衡性检验协变量 | 用户画像特征 |

**来源与验证**：
- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （v0.1.5, 2024-11, Nick Huntington-Klein 维护，MIT License，已验证存在）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费 Bookdown，已验证，2025-10-17 构建，含 NSW 数据 + DiD/RDD 章节）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线，因果推断经典，含 NSW + DiD）
- DoWhy 官方文档：https://py-why.github.io/dowhy/ （四步因果分析流程，用真实数据演示）
- 原始论文：Dehejia, R. & Wahba, S. (1999). "Causal Effects in Nonexperimental Studies." *JASA*.

---

## 营销延伸数据集（自行下载，URL 需验证）

主数据集是职业培训，用于学**方法**。若你想在**真实营销 A/B 测试数据**上练习，推荐：

- **Cookie Cats A/B 测试数据集**：知名移动游戏 A/B 测试（gate 30 vs gate 40），真实留存数据。原始分析见 Rasmus Bååth "A Bayesian approach to A/B testing"。Kaggle 上有多个镜像，**请在 Kaggle 搜索 "cookie cats" 自行下载并验证 URL**（Kaggle slug 历次变动，不硬编码固定链接）。
- **Kaggle Marketing Analytics / marketing A/B test**：在 Kaggle 搜索 "marketing A/B test" / "marketing campaign"，选 star 数高、有明确 A/B 分组列的数据集。

> ⚠️ 使用任何自行下载的数据集前，先做 `starter.ipynb` TODO2 的均衡性检验，确认处理/对照分组列与结果列存在、样本量充足、随机化均衡。

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实 RCT 数据（v5.0） |
|------|----------------|----------------|
| 均衡性 | 你设定的，必然均衡 | 需真实检验，体会随机化的近似性 |
| 样本量 | 任意大 | 真实有限，体会功效不足 |
| 方差结构 | 你造的，CUPED 效果可控 | 真实相关，CUPED 效果未知需探索 |
| 显著性 | 你设的效应，必然显著 | 真实效应可能不显著，学会解读"不显著" |
| 结论可信 | 自欺欺人 | 可复现、可质疑 |

**真实即严谨**--这是 v5.0 的哲学增量。
