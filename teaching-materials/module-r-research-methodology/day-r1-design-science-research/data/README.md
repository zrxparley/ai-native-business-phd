# R1 真实数据与库说明

> v5.0 核心升级：用**真实库**（pydantic + pandas）+ **真实DSR案例评估数据**（NSW真实RCT的ATE）替代手写文档。DSR方法论不是"写在Word里的研究计划"，而是"用代码结构化的可验证artifact规格"。

---

## 主库：pydantic（已验证，可运行）

**这是什么**：pydantic 是 Python 数据验证库（pydantic/pydantic，13k+ star，MIT License），用 Python 类型注解定义数据模型，自动进行类型验证和序列化。它是 FastAPI、LangChain 等框架的底层依赖。

**为什么用它**：
- **类型安全**：用 `BaseModel` 定义DSR artifact规格schema，每个字段都有类型约束和描述
- **自动验证**：实例化artifact时自动验证字段完整性，避免遗漏关键步骤
- **结构化方法论**：把DSR六步从"文档中的文字"变成"代码中的数据结构"，更严谨
- **JSON序列化**：artifact规格可直接导出为JSON，支持可复现研究

**安装方式**：

```bash
pip install pydantic
# 验证安装：
python -c "import pydantic; print(pydantic.__version__)"
# 预期输出: 2.x.x
```

**核心API速查**：

| 组件 | 导入 | R1 用途 |
|------|------|---------|
| BaseModel | `from pydantic import BaseModel` | 定义DSR六步子模型（TODO1） |
| Field | `from pydantic import Field` | 为字段添加描述和约束 |
| Enum | `from enum import Enum` | 定义ArtifactType四种类型 |
| model_fields | `DSRArtifact.model_fields` | 检查schema字段（验证） |

**来源与验证**：
- GitHub：https://github.com/pydantic/pydantic （13k+ star，MIT License，已验证存在，2026-07 活跃维护）
- 官方文档：https://docs.pydantic.dev/ （已验证，含完整教程和API参考）
- PyPI：https://pypi.org/project/pydantic/ （已验证，持续发布）

---

## 辅助库：pandas（已验证，可运行）

**这是什么**：pandas 是 Python 数据分析核心库（pandas-dev/pandas，43k+ star，BSD-3-Clause），提供 DataFrame 二维数据结构。本单元用 DataFrame 结构化Hevner七准则评估。

**安装**：通常已随数据分析环境安装。如需单独安装：`pip install pandas`

| 组件 | 导入 | R1 用途 |
|------|------|---------|
| DataFrame | `import pandas as pd; pd.DataFrame(list)` | 定义七准则评估表（TODO3/4） |
| mean | `df['score'].mean()` | 计算七准则平均分（TODO4） |
| iterrows | `df.iterrows()` | 遍历每条准则打印评分（TODO4） |
| to_string | `df.to_string(index=False)` | 格式化输出映射表（TODO6） |

**来源与验证**：
- GitHub：https://github.com/pandas-dev/pandas （43k+ star，BSD-3-Clause，已验证存在）
- 官方文档：https://pandas.pydata.org/docs/ （已验证，含完整教程）

---

## 真实DSR案例评估数据：NSW职业培训实验（真实RCT）

**这是什么**：NSW（National Supported Work）职业培训实验是因果推断领域的经典真实RCT数据集。1970年代在美国随机分配失业人员到职业培训组（treatment）和对照组（control），追踪后续收入变化。LaLonde (1986) 用它挑战了当时计量经济学方法的可靠性，此后成为因果推断方法论的benchmark数据集。

**在本单元中的角色**：本单元不直接运行因果分析（那是技能3/技能5 Day7的内容），而是**引用NSW真实RCT的评估结果**作为DSR artifact的evaluation数据。具体引用数据：

| 评估指标 | 真实值 | 来源 |
|---------|--------|------|
| 样本总量 | 445 | causaldata nsw_mixtape |
| 处理组样本量 | 185 | causaldata nsw_mixtape |
| 对照组样本量 | 260 | causaldata nsw_mixtape |
| ATE（简单差分） | 1794.34 | re78处理组均值(6349.14) - 对照组均值(4554.80) |
| 策略质量评分 | 0.80 | 技能5 Day7 deepeval BaseMetric评估 |

**营销映射**：

| NSW变量 | 含义 | 营销映射 | 角色 |
|---------|------|---------|------|
| `treat` | 是否接受职业培训 | 是否收到个性化营销 | 处理 T |
| `re78` | 1978年收入（实验后） | 营销后转化率/GMV | 结果 Y |
| `re75` | 1975年收入（实验前） | 实验前历史消费 | 协变量 |
| `age`,`educ`,... | 人口统计 | 用户画像 | 协变量 X |

**数据来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License，Nick Huntington-Klein维护）
- causaldata GitHub：https://github.com/NickCH-K/causaldata （已验证，含NSW/LaLonde等数据集）
- 原始论文：LaLonde, R. J. (1986). "Evaluating the Econometric Evaluations of Training Programs". American Economic Review, 76(4), 604-620.
- 技能5 Day7 data/README.md：https://github.com/ （本项目的技能5 Day7使用同一数据集做端到端因果分析）

> 注意：本单元引用NSW评估数据作为DSR artifact的evaluation结果，但不重复因果分析代码。因果分析的完整实现见技能5 Day7。

---

## DSR方法论参考论文

**Hevner et al. (2004)** "Design Science in Information Systems Research", MIS Quarterly 28(1), 75-105.
- JSTOR：https://www.jstor.org/stable/25148625 （DSR七准则经典论文，引用超30,000次）

**Peffers et al. (2007)** "A Design Science Research Methodology for Information Systems Research", Journal of Management Information Systems 24(3), 45-78.
- 论文PDF：https://desrist.org/desrist/files/peffers2007.pdf （DSR六步方法论）

**March & Smith (1995)** "Design and Natural Science Research on Information Technology", Decision Support Systems 15(4), 251-266.
- artifact四种类型：constructs / models / methods / instantiations

---

## 为什么不用模拟数据/手写文档（v4.0做法）

| 维度 | 手写文档/模拟数据（v4.0） | 真实库+真实评估数据（v5.0） |
|------|-------------------------|--------------------------|
| artifact规格 | Word文档描述，无验证 | pydantic schema，类型安全+自动验证 |
| 七准则评估 | 表格手填，无聚合统计 | pandas DataFrame，可计算平均分/分布 |
| 评估数据 | 编造的ATE/评分 | NSW真实RCT的ATE(1794.34)+真实评估评分(0.80) |
| 可复现性 | 不可复现（文档无代码） | 可复现（schema+评估代码可运行） |
| 学术可信度 | 低（无方法论工具支撑） | 高（DSR artifact可验证+可开源） |
| 方法论严谨性 | 主观描述 | 结构化评估（pydantic Field + pandas统计） |

**真实即严谨**--用真实库（pydantic + pandas）结构化DSR方法论，用真实评估数据（NSW RCT）填充artifact的evaluation，是v5.0的哲学增量，也是DSR方法论教学的基本要求。
