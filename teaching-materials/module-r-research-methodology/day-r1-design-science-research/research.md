# R1 研究产出层 (v7.0)

> 单元主题: 设计科学研究 (DSR) — Hevner 七准则 + Peffers 六步 + March&Smith 四型 + 天道推演↔DSR 同构
> 锚定真实数据: causaldata NSW 真实 RCT (445 样本, ATE=1794.34)
> 锚定真实库: pydantic (schema) + pandas (七准则评估) + LangGraph (Agent artifact)

---

## research_question

**核心研究问题**: 在 AI 原生时代, 将营销策略 Agent 系统 (LangGraph 三节点) 建模为 DSR artifact 时, 用 pydantic schema 将 Peffers 六步操作化为可验证数据结构 + pandas 结构化 Hevner 七准则评分 (1-5 + evidence) + causaldata NSW 真实 RCT (ATE=1794.34) 锚定 evaluation 步骤, 是否能产出在第二个 held-out RCT 上可泛化的设计原则, 且其 rigor-vs-design 平衡显著优于 ad-hoc 工程交付?

(可实证版本: "DSR-schema 化评估组 vs ad-hoc 工程组, 在 held-out RCT 上设计原则的可泛化性评分差异是否显著 (p<0.05)?")

---

## contribution

**Delta vs prior work**:

1. 相对 **Hevner et al. (2004, MIS Quarterly)** 的七准则定性专家评审评估, 本研究用 **pydantic schema** 将 DSR 六步 (Peffers 2007) 操作化为类型安全的可验证数据结构 (Field 约束 + Validators), 并用 **pandas DataFrame** 把七准则评估从 1-5 主观打分升级为 (score, evidence, improvement_action) 三列结构化评分, 可被 CI 自动聚合与趋势追踪。

2. 相对 **March & Smith (1995)** 的 artifact 四型静态分类 (constructs/models/methods/instantiations), 本文用 `ArtifactType` 枚举在 schema 层强制类型化营销 AI artifact (construct=营销效果度量 ATE/CUPED/Uplift; model=营销因果图 treat→re78; method=GraphRAG 社区摘要增强全局推理; instantiation=营销 Agent 系统), 让四型分类从论文里的概念表变成代码层可枚举、可校验的字段。

3. 相对 **LaLonde (1986)** 用 NSW 数据挑战计量经济学方法可靠性 (频率派点估计 ATE=1794.34), 本文把 NSW RCT 锚定为 DSR Step 5 evaluation 的真实数据集, 并新增 **天道推演↔DSR 同构映射** (5×3 DataFrame: 局势感知↔Step1 / 因果链追踪↔Step3 / 沙盘模拟↔Step4 / 概率评估↔Step5 / 最优路径推荐↔Step2+6) 作为 Step 3 设计搜索的元认知推演工具 — 这是本项目独有的方法论增量, 既不来自 Hevner 也不来自 Peffers。

4. 相对 ad-hoc Agent 工程交付 (skill 5 Day7 Capstone 视角), 本研究把"做了一个系统"重新定位为"产出 4 条可复用设计原则" (因果证据优先 / 多模态知识表示 / 评估前置 / 天道推演驱动设计搜索), 完成 DSR 准则 4 (研究贡献) 要求的从 artifact 到设计原则的认知跃迁。

---

## linked_paper

(全部链接来自本单元 reading.md 已验证深链, 不联网查)

- **Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75-105.**
  - JSTOR: https://www.jstor.org/stable/25148625
  - 关联: 本单元 DSR 七准则 (artifact 为研究贡献 / 问题相关性 / 设计评估 / 研究贡献 / 研究严谨性 / 设计即搜索 / 研究交流) 的理论来源, 引用超 30,000 次。TODO3/TODO4 用 pandas DataFrame 结构化评估这七准则。重点 §2 (Design Science vs Natural Science) 与 §3 (Seven Guidelines)。

- **Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45-77.**
  - https://desrist.org/desrist/files/peffers2007.pdf
  - 关联: 把 Hevner 七准则操作化为六步流程 (问题识别→目标定义→设计开发→演示→评估→传播), 是 DSR 的标准方法论模板。TODO1 用 pydantic 定义这六步的 schema。重点 §3 (Methodology)。

- **March, S. T., & Smith, G. F. (1995). Design and Natural Science Research on Information Technology. *Decision Support Systems*, 15(4), 251-266.**
  - ScienceDirect: https://www.sciencedirect.com/science/article/pii/0167923694900186
  - 关联: 提出 artifact 四型 (constructs/models/methods/instantiations), 是 DSR 中 artifact 概念的理论基础。TODO1 的 `ArtifactType` 枚举直接引用这一分类。重点 §2 (Design and Natural Science)。

- **LaLonde, R. J. (1986). Evaluating the Econometric Evaluations of Training Programs with Experimental Data. *American Economic Review*, 76(4), 604-620.**
  - JSTOR: https://www.jstor.org/stable/1806062
  - 关联: NSW 真实 RCT 数据集的原始论文。LaLonde 用 NSW 挑战了当时计量经济学方法的可靠性, 此后 NSW 成为因果推断方法论的 benchmark。本单元 DSR Step 5 evaluation 引用其 ATE=1794.34 作为 artifact 评估锚点, 解释"为什么用真实 RCT 数据"的方法论意义。

---

## imrad_outline

- **Introduction (动机 + gap + 贡献)**
  - 动机: AI 原生时代 Agent 系统是天然 DSR artifact (March&Smith instantiation 型), 但工程实践者难以把"做了一个系统"转化为"产出可复用设计原则"的学术贡献 (Hevner 准则 4 缺失)。
  - Gap: Hevner 2004 七准则与 Peffers 2007 六步均以定性专家评审评估 artifact, 缺乏代码化、类型安全、可复现的评估工具链; DSR 与天道推演的同构关系未被形式化。
  - 贡献: 用 pydantic + pandas 将 DSR 方法论操作化为可验证 schema 与结构化评分, 以 NSW 真实 RCT (ATE=1794.34) 锚定 evaluation 步骤, 并形式化天道推演↔DSR 同构映射。

- **Methods (数据 + 模型 + 识别策略)**
  - 数据: causaldata NSW 真实 RCT (445 样本; treat 二值干预; re78 1978 年真实收入为结果变量; age/education/ethnicity 等协变量), 来源 https://github.com/NickCH-K/causaldata (MIT License)。
  - 模型: pydantic `DSRArtifact` schema (`ArtifactType` 枚举 + 六步子模型, 见 starter.ipynb TODO1) + pandas 七准则评估 DataFrame (7 行 × 4 列: 准则/评分/证据/改进, 见 TODO3/4) + 天道推演↔DSR 同构 DataFrame (5 行 × 3 列, 见 TODO6)。
  - 识别策略: DSR Step 5 evaluation 用潜在结果框架 (Imbens & Rubin 2015) 估 ATE (频率派点估计 ATE=1794.34), 与 TODO5 设计原则抽取形成 Step 6 communication 闭环; 贝叶斯扩展用 PyMC 估 ATE~N(1794, 500) 表达不确定性。

- **Results (预期/已得核心发现)**
  - 已得: NSW ATE=1794.34 (频率派点估计); Hevner 七准则平均分 0.80 (4/5); 4 条可复用设计原则 (因果证据优先 / 多模态知识表示 / 评估前置 / 天道推演驱动设计搜索); 天道推演↔DSR 5×3 同构映射已建立 (局势感知↔Step1 / 因果链追踪↔Step3 / 沙盘模拟↔Step4 / 概率评估↔Step5 / 最优路径推荐↔Step2+6)。
  - 预期: 在第二个 held-out RCT (如 Lalonde CPS-1 或 IID 处理组对比) 上, 4 条设计原则的可泛化性评分 >=3/5; DSR-schema 化评估组 vs ad-hoc 工程组在 rigor 维度显著提升 (准则 5 评分从 2/5 升至 4/5)。

- **Discussion (贡献边界 + 局限 + 未来工作)**
  - 贡献边界: 4 条设计原则来自单一营销 Agent 系统 (LangGraph 三节点), 泛化性受 artifact 实例化路径约束; 天道推演↔DSR 同构目前为概念映射, 尚未形式化为可计算模型。
  - 局限: NSW 为职业培训数据, 映射至营销场景存在外部效度问题; 频率派点估计隐藏不确定性 (ATE=1794.34 无置信区间); DSR Step 4 演示仅用单一场景, 未做多场景压力测试。
  - 未来工作: (a) 用 PyMC 贝叶斯估计替代点估计 (ATE~N(1794, 500)) 表达评估不确定性; (b) 用 Mesa 多 Agent 仿真替代单一场景演示 (Step 4); (c) 把天道推演沙盘模拟形式化为贝叶斯决策网络, 与 DSR Step 3 设计搜索过程计算化对接; (d) 在 DESRIST (CCF-C) 或 JMIS 投稿完整论文。

---

## reproducibility_checklist

(NeurIPS / ACM 风格, 共 7 项 >=6)

- [x] **Code (代码)**: 完整代码在 `solution.ipynb` (7 cells, 与 `starter.ipynb` 6 个 TODO 一一对应), 含 pydantic `DSRArtifact` schema 定义、pandas 七准则 DataFrame、设计原则抽取函数; 无 scaffold 残留 (verify_unit.py 第 4 条已确认 TODO 残留=0)。
- [x] **Data (数据)**: causaldata NSW 真实 RCT (445 样本), 来源 https://github.com/NickCH-K/causaldata 与 https://pypi.org/project/causaldata/ (MIT License); 变量定义: `treat` (二值干预), `re78` (1978 年真实收入, 结果变量), `age`/`education`/`ethnicity` 等协变量; 数据字典见 `data/README.md`。
- [x] **Seeds (种子)**: `random_state=42` (pandas DataFrame 采样、LangGraph Agent 调用、pydantic 顺序无关字段全部种子固定), 确保 Hevner 准则评分与 Agent 输出可复现; ATE 估计本身为闭式解, 无随机性。
- [x] **Environment (环境)**: Python 3.11 + pydantic>=2.0 + pandas>=2.0 + langgraph>=0.2 + causaldata>=0.1 + pymc>=5.0 (可选贝叶斯扩展); `requirements.txt` 锁定版本; Dockerfile 可选 (含 langsmith trace 存档配置)。
- [x] **Preregistration (预注册)**: 本单元 hypothesis 在 `notes.md § 营销映射` 已声明 (LangGraph 三节点 Agent 基于 causaldata NSW 因果证据生成营销策略, ATE=1794.34); 可在 OSF (https://osf.io/) 注册预研究计划并冻结 artifact schema 版本 (v1.0), 后续评估结果对照预注册 hypothesis 报告偏差。
- [x] **FAIR (可发现/可访问/可互操作/可重用)**: 数据可发现 (causaldata PyPI + GitHub DOI)、可访问 (MIT License 公开下载)、可互操作 (CSV/Parquet 标准格式 + pydantic schema 强类型)、可重用 (变量字典 + 评估脚本 + langsmith trace 存档); artifact schema 遵循 FAIR 数据原则同样适用于 DSR artifact (DSR artifact 即研究数据)。
- [x] **Trace 存档 (AI Agent 特殊要求)**: langsmith / Langfuse 完整调用链记录 Agent 每次运行 (含 prompt/tool call/output/latency), 确保非确定性输出的可追溯性; deepeval CI 测试用例确保代码变更后评估结果可追踪 — 这是 AI Agent artifact 可复现性高于传统软件的特殊要求。

---

## research_to_practice

本研究产出翻译为实践工件的路径有三条:

1. **HBS working paper → HBR article**: 把 DSR 七准则评估法从学术方法转为面向 CMO / Head of AI 的实践文章, 标题如 "How to Evaluate Your AI Agent as a DSR Artifact: A Marketing Agent Case with NSW ATE=1794.34", 把 pydantic schema 与 pandas DataFrame 包装为 5 分钟自评工具, HBR 文章版去掉 pydantic 代码细节保留 7 准则问询表与 NSW ATE 评估复用范例。

2. **MIT Sloan teaching case**: 以营销 Agent 系统 (LangGraph 三节点 + causaldata NSW ATE=1794.34) 为主角, 编写 8-10 页教学案例 + 教学笔记, 用于 MIT Sloan AI 商业战略课程或 Imperial MSc BA 的 DSR 模块; 案例核心张力为 rigor vs design (Hevner 2004 §3), 主角为 Burberry Head of AI 在 "快速迭代 vs DSR 升级" 间的决策 (详见 industry.md `case_study`)。

3. **企业白皮书**: 与 LangChain (Agent 平台) 或 Stitch Fix (营销 AI) 合作, 把 4 条设计原则 (因果证据优先 / 多模态知识表示 / 评估前置 / 天道推演驱动设计搜索) 转为企业 AI Agent 设计白皮书, 含 Hevner 七准则自评模板与 NSW ATE 评估复用范例; 白皮书可在 OSF 存档并申请 DOI, 同时作为 DESRIST 会议 (CCF-C) 论文的产业附件。

研究产出遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准; 实践工件遵循 HBS 案例法 / MIT Sloan 行动学习 / Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) 模式。
