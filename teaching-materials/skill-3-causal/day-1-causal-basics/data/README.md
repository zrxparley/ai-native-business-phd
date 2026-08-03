# Day 1 真实数据集说明

> v5.0 核心升级：用**真实数据集**替代模拟数据。模拟数据预设了答案，真实数据才能让你学会"现实里的混杂有多脏"。

---

## 主数据集：Lalonde / NSW（公开教学数据；运行性需在锁定环境中复核）

**这是什么**：NSW（National Supported Work）职业培训示范实验的真实数据，由 Dehejia & Wahba (1999) 整理，是因果推断领域**最经典的真实教学数据集**，MIT/Stanford/DoWhy/EconML 教程广泛使用。

**为什么用它**：`nsw_mixtape` 提供随机实验基准，`cps_mixtape` 提供观测对照。把 NSW 处理组与 CPS 对照组合并后，会出现年龄、教育、种族、前期收入等选择差异；这才是本单元要诊断的观测偏差。不要把 NSW 随机实验本身说成“严重混杂”。

**加载方式**（需先 `pip install causaldata`）：

```python
import pandas as pd
from causaldata import nsw_mixtape, cps_mixtape

nsw_df = nsw_mixtape.load_pandas().data
cps_df = cps_mixtape.load_pandas().data
df = pd.concat([
    nsw_df.loc[nsw_df["treat"] == 1],
    cps_df.loc[cps_df["treat"] == 0],
], ignore_index=True)
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

**来源与验证**：
- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （需在课程锁定环境中记录实际安装版本与 license）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费 Bookdown 版；用于核对 `causaldata` 包和 NSW 示例）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线版；用于核对 Lalonde/NSW 教学背景）
- DoWhy 官方文档（四步因果分析流程，用真实数据演示）：https://py-why.github.io/dowhy/
- 原始论文：Dehejia, R. & Wahba, S. (1999). "Causal Effects in Nonexperimental Studies." *Journal of the American Statistical Association*.

证据复核日期：2026-08-03。复核范围：确认本单元使用的是公开教学数据源路径；不等同于证明当前仓库 notebook 已在干净环境中 clean run。

---

## CQ-S3-1 数据质量检查

提交 `starter.ipynb` 前必须记录：

1. **数据版本**：`causaldata` 实际版本、Python 版本、加载出的 `df.shape` 与字段列表。
2. **positivity/overlap**：处理组与对照组样本量；倾向得分共同支撑区；共同支撑区外样本占比。
3. **协变量平衡**：对 `age/educ/black/hisp/marr/nodegree/re74/re75` 报告均值、标准化均值差（SMD）和缺失率。
4. **负对照候选**：说明哪个结果或处理理论上不应受 `treat` 影响；若当前数据缺少合适负对照，必须写明“不具备直接负对照字段”，并转为概念设计。
5. **估计边界**：NSW 到营销场景只是因果结构类比，不自动证明任何真实优惠券/广告业务的外部有效性。

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
