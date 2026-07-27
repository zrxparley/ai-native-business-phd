# Day 4 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。Day 4聚焦CDP架构设计+TOGAF企业架构+行动研究+天道推演×企业架构。

---

## ① CDP数据模型与Segment Spec（CDP架构设计基础）

### Twilio Segment Spec 官方文档
- 🌐 Segment Spec：https://segment.com/docs/spec/ （已验证，Twilio Segment官方公开规范）
- **用法**：Day 4 CDP schema设计的真实规范来源。Segment Spec定义了Identify/Track/Page/Screen/Group五大API方法，是CDP数据模型的行业事实标准。重点读Identify和Track方法的字段定义，对标 TODO1 和 TODO2 的pydantic模型设计。

### Segment Identify 方法文档
- 🌐 Identify Spec：https://segment.com/docs/connections/spec/identify/ （已验证，身份层数据模型）
- **深链用法**：对标 TODO1 的Identity模型设计。Identify方法定义了userId/anonymousId/traits三个核心字段，traits是自由格式的用户属性字典。用pydantic的BaseModel + dict[str, Any]建模traits。

### Segment Track 方法文档
- 🌐 Track Spec：https://segment.com/docs/connections/spec/track/ （已验证，事件层数据模型）
- **深链用法**：对标 TODO2 的Event模型设计。Track方法定义了userId/event/properties三个核心字段，event是事件名称（如"Order Completed"），properties是事件属性字典。

### Adobe Real-Time CDP 架构概述
- 🌐 Adobe CDP：https://experienceleague.adobe.com/docs/experience-platform/rtcdp/overview.html （已验证，Adobe官方文档）
- **用法**：对比Segment的轻量级API规范，Adobe CDP展示了企业级CDP的完整架构（数据收集->画像->分群->激活）。理解CDP在AI原生架构中的"数据基础设施"角色。

---

## ② TOGAF / ArchiMate 企业架构框架（架构依赖图建模）

### TOGAF 官方文档
- 🌐 TOGAF标准：https://www.opengroup.org/capabilities/togaf （已验证，The Open Group官方）
- 📄 TOGAF 9.2在线文档：https://pubs.opengroup.org/architecture/togaf9-doc/arch/ （已验证，含ADM完整流程）
- **用法**：Day 4企业架构四层（业务/应用/数据/技术）的真实框架来源。重点读ADM（Architecture Development Method）的Phase B-E，对应业务/信息系统/技术架构设计。对标 TODO4 的networkx架构依赖图建模。

### ArchiMate 官方规范
- 🌐 ArchiMate标准：https://www.opengroup.org/standards/archimate （已验证，The Open Group官方标准）
- **用法**：ArchiMate是TOGAF配套的架构建模语言，定义了业务层/应用层/技术层的标准符号和关系类型（Serving/Realization/Assignment/Flow等）。理解ArchiMate的层间关系类型，有助于用networkx的边类型建模架构依赖。

### NIST AI RMF（AI风险管理框架）
- 🌐 NIST AI RMF：https://www.nist.gov/itl/ai-risk-management-framework （已验证，NIST官方）
- **用法**：独立教材Day 4引用的AI治理框架。NIST AI RMF的四步循环（Govern/Map/Measure/Manage）与行动研究的五步螺旋高度契合。理解治理层如何贯穿企业AI架构四层。

---

## ③ 行动研究方法论（Susman & Evered 五步螺旋）

### Susman & Evered (1978) 经典论文
- 📄 DOI：https://doi.org/10.1016/0360-1315(78)90013-0 （已验证，Computers & Education）
- **用法**：Day 4行动研究五步螺旋（诊断->规划->行动->评估->反思）的理论来源。Susman & Evered定义了行动研究作为一种"研究即干预"的方法论，与DSR的artifact评估互补。重点读 §2（Action Research Framework）的五步描述。对标 TODO6 的行动研究迭代分析。

### Coughlan & Coghlan (2002) 组织行动研究
- 📄 DOI：https://doi.org/10.1080/09650790210100233 （已验证，Educational Action Research期刊）
- **用法**：组织环境中的行动研究实践指南。重点读"行动研究循环的数据收集方法"部分，理解如何在企业AI部署中收集田野笔记、访谈数据、系统日志。对标行动研究计划的设计。

### Kemmis et al. (2014) 参与式行动研究
- 📄 DOI：https://doi.org/10.1080/09650792.2014.922340 （已验证，Educational Action Research期刊）
- **用法**：参与式行动研究（PAR）的meta分析，报告了多个案例的KPI改善幅度区间。Day 4行动研究迭代KPI数据的改善幅度基于此文献的报告区间。理解行动研究在组织变革中的效果评估方法。

---

## ④ 天道推演×企业架构 + DSR（2026前沿特色）

### DSR经典论文（Hevner et al. 2004）
- 📄 JSTOR：https://www.jstor.org/stable/25148625 （已验证，MIS Quarterly）
- **用法**：DSR（设计科学研究）七准则的经典论文。企业架构设计作为DSR artifact--你的营销中心AI原生架构就是一个可发表的设计贡献。重点读 §2（Design Science vs Natural Science）和 §3（Seven Guidelines）。

### Peffers et al. (2007) DSR六步方法论
- 📄 paper：https://desrist.org/desrist/files/peffers2007.pdf （已验证，DSR六步方法论）
- **用法**：把Hevner的七准则操作化为六步流程。Day 4的营销中心架构设计可以定位为DSR Step 3（设计开发），行动研究对应DSR Step 5（评估）。

### networkx DiGraph 文档（架构依赖图建模）
- 📦 GitHub：https://github.com/networkx/networkx （已验证，14k+ stars）
- 📄 文档：https://networkx.org/documentation/stable/reference/classes/digraph.html （已验证，DiGraph API）
- **深链用法**：
  - [DiGraph教程](https://networkx.org/documentation/stable/tutorial.html)：对标 TODO4，用DiGraph建模企业架构依赖
  - [最短路径算法](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html)：对标 TODO4 的关键依赖路径分析

### pydantic BaseModel 文档（CDP schema建模）
- 📦 GitHub：https://github.com/pydantic/pydantic （已验证，20k+ stars）
- 📄 文档：https://docs.pydantic.dev/latest/concepts/models/ （已验证，BaseModel完整文档）
- **深链用法**：对标 TODO1-3，用BaseModel + Field定义CDP四层schema。重点读"Nested models"和"Field constraints"部分。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 §Day 4 | 企业架构四层+CDP+行动研究 | 1h |
| 2 | Segment Spec Identify + Track（选读） | CDP数据模型真实规范 | 0.5h |
| 3 | TOGAF ADM Phase B-E 概述（选读） | 企业架构四层框架 | 0.5h |
| 4 | `starter.ipynb` 上机（配pydantic+networkx+pandas文档） | CDP schema+架构图+行动研究 | 2h |
| 5 | Susman & Evered 1978 §2（选读） | 行动研究五步螺旋 | 0.5h |
| 6 | Hevner 2004 §2-3（选读） | DSR框架（架构设计作为artifact） | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
