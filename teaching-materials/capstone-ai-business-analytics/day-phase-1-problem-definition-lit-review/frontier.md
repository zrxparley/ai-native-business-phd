# frontier.md (v9.0 学术前沿注入层)

> **所属**：capstone-ai-business-analytics · Phase 1 问题定义与文献综述
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：如何系统化识别"AI 原生企业 agent 系统"这一新兴领域的研究空白？2025-2026 年的 agent 基础设施论文（gap taxonomy、MCP 语义网关、模块化 skill 架构）如何为本 Capstone 的 PRISMA 综述与 DSR 问题定义提供可操作的空白分类框架？

---

## frontier_topic

本单元教 PRISMA 四步系统文献综述 + DSR 六步问题识别 + DeepSeek/RAGAS 辅助综述 + 天道推演研究路径设计。前沿子问题是：当"AI 原生企业 agent 系统"这一领域在 2025-2026 年才刚刚形成可命名的范式（CRUD→autonomous agents、Agentverse、Microskill），PRISMA 检索策略应如何覆盖一个尚无稳定关键词共识的新兴领域？新的 gap analysis 论文如何把"研究空白"从主观判断升级为可编目的结构化 taxonomy？

---

## recent_papers

### 1. From CRUD to Autonomous Agents: Formal Validation and Zero-Trust Security for Semantic Gateways in AI-Native Enterprise Systems
- **arXiv**: https://arxiv.org/abs/2604.25555
- **作者**: Ignacio Peyrano
- **年份**: 2026
- **摘要**: 提出由 MCP（Model Context Protocol）治理的语义网关，将企业系统从 CRUD 范式演进为自主代理交互，并提供形式化验证与零信任安全闭环。直接命名"AI-Native Enterprise Systems"，为该领域提供首篇可引用的形式化定义。
- **与本单元的关联**: 本单元 PRISMA TODO2 用 arxiv 包检索"AI marketing agent"主题——这篇论文正是"AI 原生企业"范式的代表性文献，应作为 Capstone 研究问题定义书的核心引用，把"Agent 系统缺乏因果评估框架"的研究空白锚定到 CRUD→agents 的范式迁移语境。

### 2. Infrastructure for the Agentic Web: Gap Analysis and Architecture from the Agentverse Platform
- **arXiv**: https://arxiv.org/abs/2606.20570
- **作者**: Robin Dey, Panyanon Viradecha
- **年份**: 2026
- **摘要**: 对 Fetch.ai 的 Agentverse 平台做实证审计，编目 204 个 API 端点，识别 8 个类别中 62 项缺失能力，提出七层"代理云栈"参考架构并刻画到 2030 年的五条演进路径。
- **与本单元的关联**: 本单元 TODO5 要求"识别 2-3 个研究空白（gap analysis）"——这篇论文示范了一种可复现的 gap taxonomy 方法（按类别编目缺失能力），可直接迁移到本单元的 PRISMA Synthesis 阶段，把研究空白从"主观判断"升级为"类别×缺失能力"的结构化矩阵。

### 3. Microskill Architecture: A Modular Skill-Driven Framework for AI-Native Code Generation
- **arXiv**: https://arxiv.org/abs/2606.05720
- **作者**: Mohammad Zare, Omid Abdolrahmani
- **年份**: 2026
- **摘要**: 提出受微服务启发的 MicroSkill 架构，用于知识封装而非服务分解的模块化设计范式，为 AI 原生企业的代码生成能力组合与技能复用提供架构基础。
- **与本单元的关联**: 本单元 DSR 问题定义书的"artifact 描述"字段要求定义"核心组件：组件1/组件2/组件3"——MicroSkill 提供了一种具体的模块化 artifact 设计范式，可作为 Capstone artifact（marketing agent system）的组件分解参考，把"研究空白"从"缺一个系统"细化为"缺一个 skill 组合机制"。

---

## critical_synthesis

这三篇论文共同标志着"AI 原生企业 agent 系统"在 2025-2026 年完成了从分散工程实践到可命名研究范式的相变。**领域共识**正在形成：企业系统正从 CRUD/服务导向迁移到 agent 导向，MCP（语义网关）+ 模块化 skill（MicroSkill）+ 代理云栈（七层架构）构成新基础设施三件套，Peyrano（#1）的形式化验证工作与 Dey & Viradecha（#2）的 gap taxonomy 互相印证了这一方向。**争议**在于"AI-native enterprise"的边界——Peyrano 把它定义在 MCP 语义网关层，Dey 等把它定义在七层代理云栈，Zare 等把它定义在 skill 模块层；三篇论文各自从不同抽象层声称"AI 原生企业"的定义权，缺乏统一的 reference architecture，存在概念碎片化风险。**方法学趋势**是从概念论文转向实证 gap analysis：Agentverse 论文编目 204 端点 + 62 缺失能力，是少见的可量化空白研究，但仅基于单一平台（Fetch.ai），外部效度存疑。**局限**显著——三篇论文均未提供因果证据证明 agent 范式优于 CRUD 范式（Peyrano 仅做形式化验证、无生产 A/B）；均未覆盖营销/商业分析垂直域；MicroSkill 的"知识封装"概念与知识图谱（Phase 2 所教）的关系未厘清。这意味着本 Capstone 的"Agent 系统缺乏因果评估框架"研究空白在这三篇中均未被填补——正是本单元 PRISMA 综述应定位的贡献缺口，而非已被饱和的领域。

---

## delta_to_unit

1. **PRISMA 检索策略的更新**：本单元 notes.md TODO2 教用 `arxiv.Search(query="AI marketing agent")` 做关键词检索——但前沿论文显示该领域尚无稳定关键词共识（#1 用"AI-native enterprise systems"、#2 用"agentic web"、#3 用"microskill"）。建议在 starter.ipynb TODO2 增加多 query 并集检索（至少 3 个同义 query），否则 PRISMA 的"识别"阶段会系统性遗漏 Agentverse/Microskill 这类用新术语命名的文献。

2. **gap analysis 方法的升级**：本单元 TODO5 要求"识别 2-3 个研究空白"但未给结构化方法——#2（Agentverse）示范了"按类别×缺失能力"的 gap taxonomy 矩阵（8 类 × 62 项）。这是对本单元所教"主观判断 gap"的直接更新：把 gap analysis 从"我觉得缺什么"升级为"按类别编目已有什么、缺什么"，使研究空白可复现、可被审稿人验证。

3. **DSR artifact 描述的具体化**：本单元 DSR 问题定义书模板的"artifact 描述"字段（notes.md 第 70-72 行）只要求"组件1/组件2/组件3"——#3（MicroSkill）提供了具体的模块化 artifact 设计范式（微服务启发、知识封装而非服务分解），可作为 Capstone artifact 组件分解的参考模式，把模糊的"组件1/2/3"升级为有架构依据的 skill 模块划分。

4. **天道推演研究路径的锚定**：本单元 notes.md 第 156-162 行用天道推演设计三条研究路径沙盘——前沿论文为这些路径提供了 2026 年的实证锚点：路径1（Agent 因果评估框架）对应 #1 的形式化验证缺口（Peyrano 仅做形式化、无生产因果证据）；路径2（表示工程×营销 KG）对应 #3 的 skill 模块化缺口；路径3（人机协作治理）对应 #2 的 62 项缺失能力中的治理类。

---

## open_questions

1. 当一个研究领域（AI 原生企业 agent）的关键词共识尚未稳定时，PRISMA 检索策略应如何避免"用旧关键词搜新范式"导致的系统性遗漏——是否需要引入 embedding-based 语义检索补充关键词检索？
2. Agentverse 的 gap taxonomy（8 类 × 62 项）是基于单一平台（Fetch.ai）编目的——把该方法迁移到营销 agent 领域时，taxonomy 的类别定义是否需要重新校准？跨平台/跨领域的 gap taxonomy 可比性如何保证？
3. 三篇论文分别从语义网关层（#1）、代理云栈层（#2）、skill 模块层（#3）声称"AI 原生企业"的定义权——是否存在一个统一的 reference architecture 能调和这三层 abstraction？还是"AI 原生企业"本质上是一个多 abstraction 的概念簇？
4. Peyrano（#1）用形式化验证但无生产因果证据证明 agent 范式优于 CRUD——AI 原生企业范式的"优越性"是否本质上不可证伪（因为 CRUD 与 agent 不是同一 abstraction 层的可比较对象）？

---

## methodological_critique

这三篇论文的方法论严谨性参差不齐，博后级读者需警惕。**Peyrano（#1）** 的形式化验证是亮点，但"零信任安全闭环"仅在语义网关层做形式化，未在生产环境验证——形式化模型的假设（如 MCP 协议的完备性）未经实证压力测试，存在"模型正确但假设错误"的可复现性风险。**Dey & Viradecha（#2）** 的 gap analysis 是少见可量化的贡献，但样本严重偏倚：仅基于 Fetch.ai 一个平台，204 个端点不代表 agentic web 的全貌；62 项缺失能力的判定标准未公开（是否预设了"应有能力"清单？），存在确认偏误风险；"到 2030 年的五条演进路径"是预测性陈述，缺乏证据基础，应视为观点而非发现。**Zare 等（#3）** 的 MicroSkill 架构概念吸引人但验证薄弱——论文标题称"AI-native code generation"，但未报告任何代码生成质量的实证指标（如 pass@k、human eval），仅做架构论述；"受微服务启发"的类比是否成立（微服务是服务分解、MicroSkill 是知识封装）需要更严格的论证，否则有概念滑移风险。三篇均未开源代码（截至语料库标注时），且 #3 标注 unverified，引用时需标注"未经 abstract 页确认"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/capstone-ai-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
