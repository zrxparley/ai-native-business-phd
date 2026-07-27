# Day 4 真实数据集说明

> v5.0 核心升级：用**真实数据集**替代模拟数据。模拟数据预设了答案，真实数据才能让你学会"算法在真实数据上会发现什么、哪些发现可信"。

---

## 数据集 1：sklearn 糖尿病数据集（因果发现用）

**这是什么**：scikit-learn 内置的真实医学数据集，442 个糖尿病患者的 10 个生理指标，是因果发现算法的标准测试数据。

**为什么用它**：教材 4.1 节的因果发现代码用模拟数据（预设了 `user_interest -> search -> page_view` 的因果结构）--模拟数据预设了答案。改用真实糖尿病数据，算法发现的因果结构可能与医学常识相符也可能不符，才能学到"真实不确定性"。

**加载方式**（需先 `pip install scikit-learn`）：

```python
from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
```

**字段**：

| 字段 | 含义 | 营销映射 |
|------|------|---------|
| `age` | 年龄（标准化） | 用户年龄段 |
| `sex` | 性别 | 用户性别 |
| `bmi` | 体质指数 | 用户健康画像 |
| `bp` | 平均血压 | 用户健康指标 |
| `s1` | 总胆固醇 | 用户特征 |
| `s2` | 低密度脂蛋白 | 用户特征 |
| `s3` | 高密度脂蛋白 | 用户特征 |
| `s4` | 总胆固醇/高密度脂蛋白 | 用户特征 |
| `s5` | 血清甘油三酯对数 | 用户特征 |
| `s6` | 血糖水平 | 用户特征 |

**来源与验证**：
- scikit-learn 官方文档：https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset （已验证，scikit-learn 内置数据集，BSD License）
- 原始数据：Bradley Efron et al. (2004). "Least Angle Regression." *Annals of Statistics*

---

## 数据集 2：Lalonde / NSW（ML 因果推断用）

**这是什么**：NSW（National Supported Work）职业培训示范实验的真实数据，由 Dehejia & Wahba (1999) 整理，因果推断领域**最经典的真实教学数据集**。Day 1 已用于后门调整 ATE 估计；Day 4 用它做**因果森林 CATE 估计**（异质处理效应）。

**为什么用它**：真实存在严重混杂，且样本量足够（445 样本）做因果森林。Day 1 估的是平均效应（ATE），Day 4 估的是**不同特征用户的差异化效应（CATE）**--同一份数据，不同问题。

**加载方式**（需先 `pip install causaldata`）：

```python
from causaldata import nsw
df = nsw.load_pandas().data
```

**字段**（同 Day 1）：

| 字段 | 含义 | 营销映射 | Day 4 角色 |
|------|------|---------|-----------|
| `treat` | 是否参加培训（1=是，0=否） | 是否收到优惠券 | 处理 T |
| `re78` | 1978年收入 | 转化率/GMV | 结果 Y |
| `age` | 年龄 | 用户年龄 | 异质性特征 X |
| `education` | 受教育年限 | 用户特征 | 异质性特征 X |
| `black`/`hispanic`/`married`/`nodegree` | 人口统计 | 用户分群 | 异质性特征 X |
| `re74`/`re75` | 1974/1975年收入 | 历史消费 | 异质性特征 X（关键） |

**来源与验证**：
- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （v0.1.5, 2024-11, Nick Huntington-Klein 维护，MIT License，已验证存在）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费 Bookdown 版，已验证，本书代码用 `causaldata` 包，含 NSW 数据）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线版，因果推断经典开源教材，同样使用 NSW 数据）
- DoWhy 官方文档（四步因果分析流程）：https://py-why.github.io/dowhy/

---

## 库依赖说明

| 库 | 用途 | 安装 | 验证链接 |
|----|------|------|---------|
| `causal-learn` | PC/FCI 因果发现算法 | `pip install causal-learn` | https://pypi.org/project/causal-learn/ （TCU Zhongheng Zheng 等，MIT License，已验证） |
| `econml` | 因果森林 CausalForestDML | `pip install econml` | https://github.com/py-why/EconML （微软研究院，MIT License，已验证） |
| `causaldata` | NSW 真实数据 | `pip install causaldata` | https://pypi.org/project/causaldata/ （已验证） |
| `scikit-learn` | 糖尿病数据 + 随机森林 | `pip install scikit-learn` | https://scikit-learn.org/ （已验证） |

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0 教材） | 真实数据（v5.0） |
|------|----------------|----------------|
| 因果结构 | 你造的，预设已知 | 未知的，需发现 |
| 因果发现 | 算法"发现"的就是你造的结构 | 算法可能发现意外结构，需判断可信度 |
| 混杂 | 你设定的，干净 | 真实存在的，脏，可能有隐混杂 |
| CATE 异质性 | 你设定的线性 CATE | 真实异质性未知，需探索 |
| 教学价值 | 验证代码能跑 | 学会面对真实不确定性 |

**真实即严谨**--这是 v5.0 的哲学增量。
