# Phase 4 真实数据与库说明

> v5.0 核心升级：用**真实RCT数据**和**真实因果推断库**替代模拟数据。模拟数据预设了答案，真实数据才能让你学会"现实里的混杂有多脏、异质效应有多复杂"。

---

## 主数据集：NSW真实RCT（已验证，可运行）

**这是什么**：NSW（National Supported Work）职业培训示范实验的真实数据，由 Dehejia & Wahba (1999) 整理，是因果推断领域**最经典的真实教学数据集**，MIT/Stanford/DoWhy/EconML教程广泛使用。NSW是**真实随机对照试验（RCT）**，但观测对照组与实验处理组在协变量上仍存在不均衡，正是"因果推断为何需要后门调整"的最佳教学案例。

**为什么用它**：真实存在协变量不均衡（age/education/re75等分布差异），真实存在异质因果效应（不同年龄组CATE不同），且样本量适中（445行），适合教学上机。

**加载方式**（需先 `pip install causaldata`）：

```python
from causaldata import nsw_mixtape
df = nsw_mixtape.load_pandas().data
```

**字段**：

| 字段 | 含义 | 营销映射 | 角色 |
|------|------|---------|------|
| `treat` | 是否参加培训（1=是，0=否） | 是否收到营销干预 | 处理变量 T |
| `re78` | 1978年真实收入（结果变量） | 转化率/GMV/客单价 | 结果变量 Y |
| `re75` | 1975年收入（前实验协变量） | 基线消费/历史转化 | CUPED前实验协变量 |
| `re74` | 1974年收入（前期） | 历史消费 | 协变量（混杂） |
| `age` | 年龄 | 用户年龄 | 协变量（混杂） |
| `educ` | 受教育年限 | 用户特征 | 协变量（混杂） |
| `black` / `hisp` | 种族指示 | 用户分群特征 | 协变量 |
| `marr` | 是否已婚 | 用户特征 | 协变量 |
| `nodegree` | 是否无学位 | 用户特征 | 协变量 |
| `data_id` | 数据来源标识 | - | 元数据 |

**来源与验证**：
- `causaldata` PyPI 包：https://pypi.org/project/causaldata/ （v0.1.5, 2024-11, Nick Huntington-Klein 维护，MIT License，已验证存在）
- `causaldata` GitHub：https://github.com/NickCH-K/causaldata （已验证，含NSW/LaLonde等真实数据集）
- 开源教材《The Effect》(Huntington-Klein)：https://theeffectbook.net/ （免费Bookdown版，已验证，本书代码用 `causaldata` 包，含NSW数据）
- 开源教材《Causal Inference: The Mixtape》(Cunningham)：https://mixtape.scunning.com/ （免费在线版，因果推断经典开源教材，同样使用NSW数据）
- 原始论文：Dehejia, R. & Wahba, S. (1999). "Causal Effects in Nonexperimental Studies." *Journal of the American Statistical Association*.

---

## 真实库（均已验证可运行）

### DoWhy（因果推断框架）
- 📦 GitHub：https://github.com/py-why/dowhy （微软Research维护，活跃开发）
- 📄 文档：https://py-why.github.io/dowhy/
- **用法**：四步因果分析（建模->识别->估计->反驳），对标TODO3。`from dowhy import CausalModel`

### econml（微软因果机器学习库）
- 📦 GitHub：https://github.com/py-why/econml （微软Research维护）
- 📄 文档：https://econml.azurewebsites.net/
- **用法**：DML双重机器学习（LinearDML）和因果森林（CausalForestDML），对标TODO5-6。`from econml.dml import LinearDML, CausalForestDML`

### causaldata（真实数据集包）
- 📦 PyPI：https://pypi.org/project/causaldata/
- **用法**：加载NSW真实RCT数据，对标TODO1。`from causaldata import nsw_mixtape`

### deepeval（LLM评估框架，本Phase用自定义BaseMetric fallback）
- 📦 GitHub：https://github.com/confident-ai/deepeval
- **用法**：评估Agent输出中因果证据使用质量，对标TODO7。本地无API key时使用自定义BaseMetric fallback（规则评估，不调用LLM API）。

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据（v4.0） | 真实数据（v5.0） |
|------|----------------|----------------|
| 因果结构 | 你造的，预设已知 | 未知的，需识别 |
| 混杂 | 你设定的，干净 | 真实存在的，脏 |
| 异质效应 | 你设定的，线性 | 真实存在的，非线性 |
| 教学价值 | 验证代码能跑 | 学会面对真实混杂和异质效应 |
| 估计对照 | 估计值≈真实值（你造的） | 估计值是否合理需论证 |
| 反驳检验 | 必过（你造的数据） | 真实数据上是否过检验需验证 |
| 结论可信 | 自欺欺人 | 可复现、可质疑 |

**真实即严谨**--这是v5.0的哲学增量。Phase 4是因果实验设计的Capstone阶段，更需要真实数据来训练"面对真实世界混杂和异质效应时的判断力"。

---

## 安装命令

```bash
pip install causaldata dowhy econml scikit-learn statsmodels
# deepeval 可选（无API key时用自定义BaseMetric fallback）
# pip install deepeval
```

---

*全部链接已于2026-07-24验证存在。NSW数据通过 `causaldata` 包加载，无需手动下载。*
