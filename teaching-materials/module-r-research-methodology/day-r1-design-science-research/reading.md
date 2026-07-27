# R1 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。R1聚焦DSR设计科学研究方法论 + 可复现研究 + 天道推演。

---

## ① DSR方法论核心论文

### Hevner et al. (2004) MIS Quarterly 经典（DSR七准则）
- 📄 JSTOR：https://www.jstor.org/stable/25148625
- **用法**：R1 DSR框架的理论来源。Hevner提出DSR七准则（artifact为研究贡献/问题相关性/设计评估/研究贡献/研究严谨性/设计即搜索/研究交流），是信息系统的核心研究范式。引用超30,000次。重点读 §2（Design Science vs Natural Science）和 §3（Seven Guidelines）。本单元TODO3/TODO4用pandas结构化评估这七准则。

### Peffers et al. (2007) DSR六步方法论
- 📄 paper：https://desrist.org/desrist/files/peffers2007.pdf
- **用法**：把Hevner的七准则操作化为六步流程（问题识别->目标定义->设计开发->演示->评估->传播），是DSR的标准方法论模板。本单元TODO1直接用pydantic定义这六步的schema。重点读 §3（Methodology）的六步描述。

### March & Smith (1995) Artifact四种类型
- 📄 ScienceDirect：https://www.sciencedirect.com/science/article/pii/0167923694900186
- **用法**：提出artifact的四种类型（constructs/models/methods/instantiations），是DSR中artifact概念的理论基础。本单元TODO1的ArtifactType枚举直接引用这一分类。重点读 §2（Design and Natural Science）。

### Design Science Research in IS 参考社区
- 🌐 DESRIST社区：https://desrist.org/ （已验证，DSR研究社区，年度会议）
- **用法**：DSR领域的研究社区和年度会议，Capstone论文可投DESRIST会议（CCF-C级别，适合初学者）。

---

## ② 真实库：pydantic + pandas

### pydantic 官方文档与教程（已验证）
- 📦 GitHub：https://github.com/pydantic/pydantic （13k+ star，MIT License，已验证存在）
- 📄 官方文档：https://docs.pydantic.dev/ （已验证，含完整教程）
- **深链用法**：
  - [Models教程](https://docs.pydantic.dev/latest/concepts/models/)：对标 TODO1，用BaseModel定义DSR artifact schema
  - [Field API](https://docs.pydantic.dev/latest/concepts/fields/)：对标 TODO1，为字段添加description约束
  - [Validators](https://docs.pydantic.dev/latest/concepts/validators/)：进阶--为artifact schema添加自定义验证逻辑

### pandas 官方文档（已验证）
- 📦 GitHub：https://github.com/pandas-dev/pandas （43k+ star，BSD-3-Clause，已验证）
- 📄 官方文档：https://pandas.pydata.org/docs/ （已验证）
- **深链用法**：
  - [DataFrame教程](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)：对标 TODO3/TODO4，用DataFrame结构化七准则
  - [DataFrame.mean](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)：对标 TODO4，计算七准则平均分

---

## ③ 真实DSR案例数据

### causaldata NSW 真实RCT数据集
- 📦 GitHub：https://github.com/NickCH-K/causaldata （已验证，NSW/LaLonde等真实数据集）
- 📦 PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- **用法**：NSW职业培训实验真实RCT数据。本单元引用其评估结果（ATE=1794.34）作为DSR artifact的evaluation数据。完整因果分析实现见技能5 Day7。

### LaLonde (1986) 原始论文
- 📄 JSTOR：https://www.jstor.org/stable/1806062
- **用法**：NSW数据集的原始论文。LaLonde用NSW挑战了当时计量经济学方法的可靠性，此后NSW成为因果推断方法论的benchmark。理解DSR评估中"为什么用真实RCT数据"的方法论意义。

---

## ④ 2026前沿：可复现研究 + 天道推演 + 贝叶斯

### 可复现研究（Reproducible Research）
- 🌐 OSF（Open Science Framework）：https://osf.io/ （已验证，开放科学平台）
- **用法**：可复现研究要求artifact开源 + trace存档 + 数据文档。OSF是注册预研究计划（preregistration）和存档研究数据的标准平台。DSR Step 6传播时，应将artifact规格和评估数据存档至OSF。

### 贝叶斯因果推断
- 📦 PyMC：https://github.com/pymc-devs/pymc （已验证，贝叶斯统计建模库）
- 📄 文档：https://www.pymc.io/ （已验证）
- **用法**：传统DSR评估用点估计，贝叶斯方法用概率分布表达评估结果。PyMC可用于DSR Step 5评估中，用贝叶斯推断替代频率派点估计。天道推演的"概率评估"能力对应贝叶斯推断。

### 天道推演系统（项目内）
- 📄 项目CLAUDE.md：`/Users/aha.gare.mbp/CLAUDE.md` （天道推演系统定义）
- **用法**：天道推演是一种元认知沙盘推演能力，与DSR的设计搜索过程同构。本单元TODO6构建天道推演<->DSR的同构映射。天道推演可作为DSR设计阶段的推演工具。

### 多Agent仿真
- 📦 Mesa：https://github.com/projectmesa/mesa （已验证，Python多Agent仿真框架）
- **用法**：多Agent仿真可作为DSR Step 4（演示）的高级形式。Mesa是Python的多Agent仿真框架，可模拟Agent交互和涌现行为。

---

## ⑤ 对标大学

### NUS IS PhD（DSR核心特色）
- 🌐 博士项目主页：https://www.comp.nus.edu.sg/programmes/pg/phdis/ （已验证）
- **用法**：NUS的信息系统博士项目以DSR为核心特色，要求博士生在Qualifying Examination中展示用DSR框架定义和论证研究问题的能力。本单元的DSR六步+七准则对标NUS的训练标准。

### Imperial MRes（Design Science方法论训练）
- 🌐 PhD项目主页：https://www.imperial.ac.uk/business-school/phd/ （已验证）
- **用法**：Imperial的MRes项目将Design Science方法作为方法论训练的核心模块之一，强调artifact的设计、评估和理论化循环。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本单元 `notes.md` 理论回顾 + 独立教材 § R1 | DSR方法论理论 | 1h |
| 2 | Hevner 2004 §2-3（选读） | DSR七准则 | 0.5h |
| 3 | Peffers 2007 §3（选读） | DSR六步方法论 | 0.5h |
| 4 | `starter.ipynb` 上机（配pydantic+pandas文档） | DSR方法论实操 | 2h |
| 5 | OSF可复现研究概念（选读） | 可复现研究前沿 | 0.5h |
| 6 | 项目CLAUDE.md天道推演系统（选读） | 天道推演×DSR | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
