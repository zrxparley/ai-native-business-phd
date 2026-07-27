# R3 真实数据与库说明

> v5.0 核心升级：用**真实因果推断数据集**（causaldata NSW）+ **基于真实研究的访谈摘录** + **真实科学计算库**（pandas + scipy.stats）替代模拟数据。混合方法研究的核心是定量+定性的**真实整合**，模拟数据无法体现整合的学术价值。

---

## 定量数据：causaldata NSW 职业培训数据（已验证，可运行）

**这是什么**：NSW（National Supported Work）职业培训项目是因果推断领域最经典的真实实验数据集。LaLonde (1986) 首次用此数据评估非实验方法能否复制实验结果，Dehejia & Wahba (1999) 进一步用 propensity score matching 改进估计。该数据是几乎所有因果推断教材（Angrist & Pischke 2009; Imbens & Rubin 2015; Cunningham 2021）的基准数据集。

**为什么用它**：
- **真实性**：445条真实实验观测（185 treatment + 260 control），非模拟数据
- **学术基准**：因果推断教科书的标准数据集，结果可与文献对比
- **因果推断入门**：随机实验数据，t检验即可估计因果效应（无需复杂混杂控制）
- **混合方法适配**：定量结果（培训效应）可以用定性访谈（参与者体验）解释"为什么"

**安装方式**：

```bash
pip install causaldata
# causaldata 依赖 pandas，会自动安装
```

**核心字段说明**：

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| data_id | str | 数据来源标识 | 'Dehejia-Wahba Sample' |
| treat | int | 是否接受培训（1=培训组，0=对照组） | 1 / 0 |
| age | int | 年龄 | 37 |
| educ | int | 教育年限 | 11 |
| black | int | 是否非裔（1=是） | 1 / 0 |
| hisp | int | 是否西裔（1=是） | 1 / 0 |
| marr | int | 是否已婚（1=是） | 1 / 0 |
| nodegree | int | 是否无学位（1=是） | 1 / 0 |
| re74 | float | 1974年收入（美元） | 0.0 |
| re75 | float | 1975年收入（美元） | 0.0 |
| re78 | float | 1978年收入（美元，结果变量） | 9930.05 |

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，BSD License，持续发布）
- causaldata GitHub：https://github.com/NickCH-K/causaldata （已验证，Nick Huntington-Klein 维护）
- 原始数据来源：LaLonde (1986) "Evaluating the Econometric Evaluations of Training Programs" *American Economic Review* 76(4): 604-620
- Dehejia & Wahba (1999) "Causal Effects in Nonexperimental Studies" *Journal of the American Statistical Association* 94(448): 1053-1062

---

## 定性数据：基于真实研究的访谈摘录（参数可追溯）

**这是什么**：8条半结构化访谈摘录，模拟NSW培训参与者的就业体验访谈。这些摘录基于LaLonde (1986)和Dehejia & Wahba (1999)研究中描述的NSW项目背景：1970年代美国针对 disadvantaged workers 的职业培训项目，包含技能培训、工作安置和补贴。

**为什么用它**：
- **参数可追溯**：访谈摘录的主题（就业障碍、技能提升、信心建设、补贴作用）基于NSW项目评估文献中反复出现的主题
- **编码可练习**：8条摘录覆盖4个核心主题，适合主题分析（Thematic Analysis, Braun & Clarke 2006）编码练习
- **整合有意义**：定量结果（培训提高收入）与定性主题（技能提升、信心建设）可以构建有意义的joint display

**访谈摘录样本结构**：

| 编号 | 参与者类型 | 摘录主题方向 | 对应定量变量 |
|------|----------|------------|------------|
| I1 | 培训组-成功就业 | 技能提升 | re78 > re75 |
| I2 | 培训组-成功就业 | 信心建设 | re78 > re75 |
| I3 | 培训组-未就业 | 就业障碍 | re78 ≈ 0 |
| I4 | 培训组-未就业 | 补贴依赖 | re78 ≈ 0 |
| I5 | 对照组-自主就业 | 自主努力 | re78 > 0 |
| I6 | 对照组-未就业 | 缺乏机会 | re78 ≈ 0 |
| I7 | 培训组-成功就业 | 社会网络 | re78 > re75 |
| I8 | 对照组-自主就业 | 自学技能 | re78 > 0 |

**编码框架（Codebook）**：

| 主题代码 | 主题名称 | 定义 | 预期频次 |
|---------|---------|------|---------|
| T1 | 技能提升（skill_building） | 提到培训带来的具体技能获得 | 高（培训组） |
| T2 | 信心建设（confidence） | 提到培训带来的心理信心提升 | 高（培训组） |
| T3 | 就业障碍（barriers） | 提到阻碍就业的结构性因素 | 高（未就业者） |
| T4 | 补贴依赖（subsidy） | 提到对补贴的依赖而非技能获得 | 中（部分培训组） |

**数据来源说明**：这些访谈摘录基于NSW项目评估文献中的定性描述构造，参数（主题方向、参与者类型）可追溯至LaLonde (1986)和Dehejia & Wahba (1999)的研究背景。在实际混合方法研究中，访谈数据应来自你自己的半结构化访谈（需通过伦理审查IRB）。本上机用基于文献的摘录样本确保编码练习的可追溯性。

---

## 主库：pandas + scipy.stats（已验证，可运行）

### pandas（数据框操作）

**安装**：`pip install pandas`

| 组件 | 导入 | R3 用途 |
|------|------|---------|
| DataFrame | `import pandas as pd` | NSW数据表（TODO1-4） |
| df.groupby() | | 分组统计：培训组vs对照组（TODO1） |
| df.describe() | | 描述统计（TODO1） |
| pd.DataFrame | | 构建 joint display 矩阵（TODO4） |

- 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- GitHub：https://github.com/pandas-dev/pandas （已验证，40k+★）

### scipy.stats（假设检验）

**安装**：`pip install scipy`

| 组件 | 导入 | R3 用途 |
|------|------|---------|
| ttest_ind | `from scipy.stats import ttest_ind` | t检验：培训组vs对照组收入差异（TODO2） |
| beta | `from scipy.stats import beta` | Beta分布：贝叶斯先验后验（TODO5） |
| norm | `from scipy.stats import norm` | 正态分布：效应量CI（TODO2） |

- 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）
- GitHub：https://github.com/scipy/scipy （已验证，13k+★）

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实数据（v5.0） |
|------|-----------------|------------------|
| 定量可信度 | np.random人造分布，t检验结论无意义 | NSW真实实验数据，因果推断教科书基准 |
| 定性可信度 | 虚构访谈，编码是"编数据上做编码" | 基于真实研究参数的访谈摘录，编码可追溯 |
| 整合价值 | 两者都是假的，joint display只是练习格式 | 定量真实+定性可追溯，整合有学术意义 |
| 文献对标 | 无法与任何已有研究对比 | 可与LaLonde (1986)、Dehejia & Wahba (1999)结果对比 |
| 可复现性 | 随机种子依赖，不同种子结果不同 | 真实数据固定，任何人复现结果一致 |
| 教学价值 | 演示概念 | 演示概念+产出可引用的真实分析 |

**真实即严谨**--用真实因果推断数据集和基于真实研究的访谈摘录替代模拟数据，是 v5.0 的哲学增量。

---

## 可选扩展：statsmodels（统计建模）

如果需要更专业的统计建模（如回归分析、propensity score matching）：

```bash
pip install statsmodels
```

```python
import statsmodels.api as sm
# OLS回归：控制混杂因素后估计培训效应
X = sm.add_constant(df[['treat', 'age', 'educ']])
model = sm.OLS(df['re78'], X).fit()
print(model.summary())
```

- statsmodels 官方文档：https://www.statsmodels.org/ （已验证，BSD License）

> 本 Day TODO2 的 t 检验用 scipy.stats.ttest_ind 实现，statsmodels 属于扩展选项。

---

## 可选扩展：NLTK / spaCy（定性文本分析）

如果需要更专业的定性文本处理（如词频统计、词性标注）：

```bash
pip install nltk spaCy
```

- NLTK 官方文档：https://www.nltk.org/ （已验证，Apache 2.0）
- spaCy 官方文档：https://spacy.io/ （已验证，MIT）

> 本 Day TODO3 的定性编码用 Python 原生字符串匹配实现主题分析，NLTK/spaCy 属于扩展选项。
