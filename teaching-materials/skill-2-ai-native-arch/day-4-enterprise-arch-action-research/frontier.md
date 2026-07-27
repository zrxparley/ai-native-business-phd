# frontier.md (v9.0 学术前沿注入层)

> **所属**：skill-2-ai-native-arch · day-4-enterprise-arch-action-research
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年企业 Agent 系统的规格驱动工程化、编排分类决策框架、agent 程序静态依赖分析（Agent BOM）、延迟感知架构优化、验证器驱动研究框架，如何更新本单元所教的 CDP 四层 schema + TOGAF 四层架构依赖图 + Susman 行动研究五步螺旋 + DSR artifact 设计。

---

## frontier_topic

本单元教 CDP 四层 schema（pydantic 对标 Segment Spec）+ TOGAF 四层架构依赖图（networkx DiGraph）+ Susman 行动研究五步螺旋（pandas KPI 分析）+ DSR artifact 设计 + 天道推演×企业架构同构。前沿子问题是：2025-2026 年的规格驱动 MAS 工程化（MAS-Lab 三层）、编排分类决策框架（四属性）、agent 程序静态依赖分析（AgentFlow ADG + Agent BOM）、延迟感知架构优化（LAMaS）、验证器驱动研究框架（Glite ARF），如何把"手工画架构依赖图 + pandas KPI 统计"升级为"规格驱动工程化 + 静态依赖分析 + 学习优化 + 验证器驱动评估"的可复现架构研究范式。

---

## recent_papers

### 1. MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems
- **arXiv**: https://arxiv.org/abs/2606.30546
- **作者**: Jordan Augé, Giovanna Carofiglio
- **年份**: 2026
- **摘要**: 规格驱动框架，包含三层：声明式 agentic 规格层、有状态 MAS 操作系统、带可观测性工具的 lab overlay。旨在将 MAS 从脚本集合转变为工程化分布式系统，将语义意图与运维关注点分离。
- **与本单元的关联**: 本单元 TOGAF 四层架构（业务/应用/数据/技术）是通用企业架构框架；MAS-Lab 的"规格层 + 操作系统 + lab overlay"三层是 agent 专用工程化架构，为本单元 `solution.ipynb` TODO4 的 networkx 架构依赖图提供 agent 专用分层替代方案。

### 2. AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs
- **arXiv**: https://arxiv.org/abs/2607.01640
- **作者**: Shenao Wang, Xinyi Hou
- **年份**: 2026
- **摘要**: 首个从 agent 程序中恢复和分析 agent 依赖关系的静态分析框架，构建 Agent Dependency Graph (ADG) 作为框架无关表示。在 5399 个真实 agent 程序上评估，发现 238 个污点式 prompt-to-tool 风险并生成 Agent Bills of Materials。
- **与本单元的关联**: 本单元 `solution.ipynb` TODO4 的 networkx DiGraph 是手工 `add_node` + `add_edge` 建模 TOGAF 四层；AgentFlow 的 ADG 从 agent 程序自动恢复依赖图 + 生成 Agent BOM，把"手工画架构图"升级为"自动恢复依赖图 + 物料清单"，直接对应本单元 DSR artifact 的可复现性要求。

### 3. Design and Implementation of Agentic Orchestrations and Orchestration of Agents
- **arXiv**: https://arxiv.org/abs/2606.31518
- **作者**: Stefanie Rinderle-Ma, Juergen Mangler
- **年份**: 2026
- **摘要**: 提供 agentic orchestration 选项的分类框架，沿任务特异性、可追溯性、自主性、正确性保证等属性分类。给出不同场景的定性决策标准和通过预测光感场景 agentic 实现评估的定量指标。
- **与本单元的关联**: 本单元天道推演×企业架构的"多架构方案并行模拟"是概念推演；该论文的"任务特异性 × 可追溯性 × 自主性 × 正确性保证"四属性分类为架构选型提供可量化的决策标准，把天道推演的"概率评估"从主观判断升级为属性驱动的定性+定量决策。

### 4. Learning Latency-Aware Orchestration for Multi-Agent Systems
- **arXiv**: https://arxiv.org/abs/2607.13359
- **作者**: Xi Shi, Mengxin Zheng
- **年份**: 2026
- **摘要**: 提出延迟感知编排框架 LAMaS，通过约束优化和关键路径感知信用分配学习执行图。端到端延迟降低 50% 以上且保持竞争性准确率，轻量推理时控制器消除冗余 agent 交互。
- **与本单元的关联**: 本单元 `notes.md` 第 201-205 行"多 Agent 仿真×架构验证"是概念性架构验证；LAMaS 的"关键路径感知信用分配"为架构验证提供量化方法--可模拟本单元架构依赖图（TODO4）中"如果 LLMService 故障，关键路径如何变化"。

### 5. Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents
- **arXiv**: https://arxiv.org/abs/2606.27416
- **作者**: Vassili Philippov, Pavel Katunin
- **年份**: 2026
- **摘要**: 开源 Python 框架，在研究仓库上并行运行多个 LLM 编码 agent，使用确定性验证器脚本强制任务隔离与不可变性。用于开发 BEA 2026 共享任务提交，在 closed track 获得第一名，包含 273 个跟踪任务。
- **与本单元的关联**: 本单元 DSR artifact + 行动研究（Susman 五步螺旋）是研究方法论；Glite ARF 的"验证器驱动 + 任务隔离 + 不可变性 + 273 个跟踪任务"是 DSR 的具体工程化实现，为本单元行动研究的"评估"步骤提供可复现的验证器范式。

---

## critical_synthesis

这 5 篇论文共同揭示了 2025-2026 年企业 Agent 架构研究的**共识**：架构正从"手工画 TOGAF 四层依赖图 + pandas KPI 统计"（本单元范式）走向"规格驱动工程化 + 自动依赖恢复 + 学习优化 + 验证器驱动评估"的可复现研究范式。领域共识是：企业 Agent 架构作为 DSR artifact，必须从"PPT 架构图"升级为"可自动分析 + 可学习优化 + 可验证器评估"的工程化 artifact。**争议**在于架构验证路径：MAS-Lab (2606.30546) 主张"规格驱动 + lab overlay"（声明式验证），AgentFlow (2607.01640) 主张"静态 ADG 分析 + Agent BOM"（事前静态分析），LAMaS (2607.13359) 主张"学习优化执行图"（运行时优化），Glite ARF (2606.27416) 主张"验证器脚本 + 任务隔离"（事后验证）--四条路径尚未统一。方法学趋势是从"手工建模"走向"自动恢复 + 学习优化 + 验证器闭环"。**局限**：MAS-Lab 和 LAMaS 均标注 unverified，定量评估缺失；AgentFlow 的 ADG 聚焦 agent 程序内部依赖，未覆盖本单元 CDP 四层 schema（Identity/Event/Segment/Profile）的数据架构维度--CDP 的 Segment Spec 数据模型不在 agent 程序依赖图范围内；Glite ARF 的验证器脚本假设任务可形式化（编码任务），本单元行动研究的"团队满意度"KPI（solution.ipynb TODO6）不可形式化验证。所有论文均未涉及本单元 Susman 行动研究五步螺旋的组织变革方法论，也未覆盖天道推演×企业架构的同构映射--管理咨询与人文学科方法论在 agent 架构学术论文中仍是空白。

---

## delta_to_unit

1. **架构依赖图从手工到自动恢复**：本单元 `solution.ipynb` TODO4 的 `G = nx.DiGraph()` + 手工 `G.add_node` + `G.add_edge` 建模 TOGAF 四层 17 节点 27 边；AgentFlow (2607.01640) 从 agent 程序自动恢复 Agent Dependency Graph + 生成 Agent Bills of Materials，把"手工画架构图"升级为"程序自动恢复依赖图 + 物料清单"，本单元 DSR artifact 的可复现性可借此从"手工 networkx"升级为"自动 ADG"。

2. **架构分层从通用 TOGAF 到 agent 专用三层**：本单元 `notes.md` 第 27-43 行的 TOGAF 四层（业务/应用/数据/技术）是通用企业架构；MAS-Lab (2606.30546) 的"声明式规格层 + 有状态 MAS 操作系统 + 可观测性 lab overlay"三层是 agent 专用工程化架构，为本单元 `solution.ipynb` TODO4 的 networkx 四层分区提供 agent 专用替代--"规格层"对应本单元 CDP schema，"操作系统层"对应 Agent 编排，"lab overlay"对应行动研究评估。

3. **架构选型从天道推演主观到属性驱动决策**：本单元 `notes.md` 第 192-197 行天道推演"方案 A vs B vs C 各推演 3 层未来走向"是主观推演；论文 3 (2606.31518) 的"任务特异性 × 可追溯性 × 自主性 × 正确性保证"四属性分类为架构选型提供可量化的定性+定量决策标准，把天道推演的"概率评估"从"主观贝叶斯"升级为"属性驱动决策"。

4. **架构验证从概念到关键路径优化**：本单元 `notes.md` 第 201-205 行"多 Agent 仿真×架构验证"是概念性"模拟故障传播"；LAMaS (2607.13359) 的"关键路径感知信用分配 + 50% 延迟降低"为架构验证提供量化方法，可模拟本单元架构依赖图中"LLMService 故障时关键路径如何重路由"。

5. **行动研究评估从 pandas KPI 到验证器驱动**：本单元 `solution.ipynb` TODO6 的 pandas 4 轮 KPI 分析（决策时间/决策质量/团队满意度/AI 使用率）是事后统计；Glite ARF (2606.27416) 的"确定性验证器脚本 + 任务隔离 + 273 个跟踪任务"把行动研究的"评估"步骤从"pandas 统计"升级为"验证器驱动 + 不可变性跟踪"，为本单元 DSR artifact 的可复现性提供工程化范式。

---

## open_questions

1. AgentFlow 的 ADG 从 agent 程序自动恢复依赖图，但本单元 CDP 四层 schema（Identity/Event/Segment/Profile）是数据架构而非 agent 程序，ADG 如何扩展覆盖数据架构依赖--CDP 的 Segment Spec 数据模型不在 agent 程序依赖图范围内？
2. MAS-Lab 的"声明式 agentic 规格层"与本单元 `solution.ipynb` TODO1-3 的 pydantic CDP schema 如何对接--pydantic schema 是数据规格，MAS-Lab 的 agentic 规格是行为规格，两者在架构 artifact 中如何统一表达？
3. LAMaS 的关键路径感知信用分配假设执行图可学习优化，但本单元 `notes.md` 第 192-197 行天道推演的"方案 A/B/C 3 层未来走向"涉及不可量化的组织变量（团队接受度/合规风险），学习优化器如何处理混合量化-定性变量？
4. Glite ARF 的验证器脚本在 BEA 2026 编码任务上有效，但本单元行动研究的"团队满意度"KPI（solution.ipynb TODO6）不可形式化验证，如何设计"概率性验证器"以处理主观 KPI 的验证？
5. 本单元 DSR artifact 遵循 Hevner 2004 框架，但 AgentFlow 的 Agent BOM（物料清单）和 MAS-Lab 的三层架构是 2026 年新提出的 agent 专用 artifact 形态，DSR 框架是否需要扩展以容纳这些新 artifact 类型？

---

## methodological_critique

这些论文的局限性需博后级读者警惕：MAS-Lab (2606.30546) 标注 unverified，三层架构的定量评估在摘要中未给出，"将 MAS 从脚本集合转变为工程化分布式系统"的宣称缺乏与现有 agent 框架（LangGraph/AutoGen/CrewAI）的基准对比，可能存在"为工程化而工程化"风险。AgentFlow (2607.01640) 的 5399 个 agent 程序数据集来源未公开，可能存在框架偏向，且"238 个污点式风险"未与真实攻击事件对照，false positive 率不可知；Agent BOM 的"物料清单"概念借用自软件供应链（SBOM），但 agent 的动态工具加载（MCP 运行时加载）使 BOM 在运行时可能不完整。论文 3 (2606.31518) 的"预测光感场景"是单一领域评估，四属性分类框架的通用性需更多场景验证，且"定量指标"未公开计算方式。LAMaS (2607.13359) 标注 unverified，50% 延迟降低的"竞争性准确率"表述模糊，延迟-准确率权衡曲线未公开，可能存在隐藏权衡。Glite ARF (2606.27416) 标注 unverified，BEA 2026 第一名是单一 benchmark，验证器脚本的有效性强依赖于任务可形式化（编码任务可形式化，本单元行动研究 KPI 不可完全形式化），泛化性需更多场景验证；273 个跟踪任务的"不可变性"假设在真实行动研究中常被打破（组织会中途调整 KPI 定义）。所有论文均未覆盖本单元 Susman 行动研究五步螺旋和天道推演×企业架构同构，管理学研究方法论在 agent 架构学术论文中是空白。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-2-ai-native-arch.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
