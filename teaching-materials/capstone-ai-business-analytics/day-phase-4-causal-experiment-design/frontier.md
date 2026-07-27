# frontier.md (v9.0 学术前沿注入层)

> **所属**：capstone-ai-business-analytics · Phase 4 因果实验设计与验证
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：当本单元教 DoWhy 四步因果推断 + DML/CUPED/因果森林在 NSW RCT 上估计 ATE/CATE 时，2025-2026 年的 agent 系统评估论文如何暴露"准确率评估 vs 因果效应估计"的认识论鸿沟？agent 行为的可验证基础设施（proof-derived authorization、artifact provenance）如何为因果推断的可复现性提供新基础设施？

---

## frontier_topic

本单元教 DoWhy 四步因果分析（建模->识别->估计->反驳）+ DML 双重机器学习 + CUPED 方差缩减 + 因果森林 + deepeval 自定义 BaseMetric 评估 agent 因果证据使用质量，在 NSW 真实 RCT 数据上估计 ATE/CATE。前沿子问题是：2025-2026 年生产级 agent 系统的评估论文（AINTMA 报告 88.4% 准确率）普遍使用"准确率/周期缩减"等关联性指标，而非因果效应--这如何暴露 agent 系统评估的"准确率vs因果效应"认识论鸿沟？agent 行为的可验证基础设施（proof-derived authorization、artifact provenance）如何为 Phase 4 的因果反驳检验（安慰剂/随机混杂）提供可审计的 agent 决策链？

---

## recent_papers

### 1. AINTMA: Agentic AI Architecture for Autonomous Test Management with Generative Intelligence, Secure Cloud Communication and Adaptive Quality Analytics
- **arXiv**: https://arxiv.org/abs/2607.20452
- **作者**: Vinil Pasupuleti, Shyalendar Reddy Allala
- **年份**: 2026
- **摘要**: AINTMA 是多代理 AI 系统，使用六个专门代理在云环境中实现自主测试管理。在 12 个项目 18 个月的评估中达到 88.4% 测试优先级准确率与 43% 测试周期时间缩减。
- **与本单元的关联**: 本单元 notes.md TODO7 教用 deepeval 自定义 BaseMetric 评估 agent 输出中因果证据使用质量--AINTMA 的 88.4% 准确率是"关联性指标"而非"因果效应"，正好示范了本单元所批判的"准确率不等于因果有效"陷阱：AINTMA 证明 agent 准确排序测试，但未证明 agent 因果地减少了测试周期（可能有混杂）。

### 2. Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems
- **arXiv**: https://arxiv.org/abs/2605.15228
- **作者**: Jun He, Deying Yu
- **年份**: 2026
- **摘要**: 引入分布式信任框架（DTF），从结构化可验证制品计算执行授权的验证框架，用于受治理的变更系统。为 AI 原生企业的代理权限治理与可审计闭环提供基础设施层。
- **与本单元的关联**: 本单元 notes.md TODO3 教 DoWhy 反驳检验（安慰剂/随机混杂/子集检验）验证 ATE 稳健性--DTF 的"从可验证制品计算执行授权"为反驳检验提供了 agent 决策链的可审计基础设施：agent 的每次工具调用/状态变更都有可验证制品，使"随机混杂检验"能追溯到具体 agent 决策点。

### 3. MAIF: Enforcing AI Trust and Provenance with an Artifact-Centric Agentic Paradigm
- **arXiv**: https://arxiv.org/abs/2511.15097
- **作者**: Vineeth Sai Narajala, Manish Bhatt
- **年份**: 2025
- **摘要**: 提出以制品为中心的 AI 代理范式，行为由持久、可验证的数据制品而非临时任务驱动，从数据架构层解决可信任问题。
- **与本单元的关联**: 本单元 notes.md 第 142-144 行指出 Phase 3 的 HITL Checkpointing 为 Phase 4 提供可审计的决策链--MAIF 的"制品驱动+provenance"范式把"可审计决策链"从 LangGraph Checkpointing 升级为带密码学 provenance 的制品链，为因果反驳检验提供更强的可复现基础。

---

## critical_synthesis

这三篇论文从不同角度暴露了 agent 系统评估的"准确率vs因果效应"认识论鸿沟，并为因果可复现性提供了新基础设施。**领域共识**正在浮现：agent 系统评估需要可审计的决策链（不只是最终输出），且评估指标应区分"关联性"（准确率/周期缩减）与"因果效应"（ATE/CATE）。**AINTMA（#1）的 88.4% 准确率**是生产级 agent 系统的罕见量化证据，但**关键争议**在于：准确率是关联性指标，43% 周期缩减可能是 agent 因果所致，也可能是混杂（如项目复杂度分布变化）--AINTMA 未做反驳检验，无法排除混杂。这正是本单元 DoWhy 四步中"反驳"步骤（TODO3 安慰剂/随机混杂检验）要解决的问题，但前沿 agent 评估论文普遍跳过这一步。**DTF（#2）与 MAIF（#3）** 从基础设施层补充：DTF 的"proof-derived authorization"与 MAIF 的"artifact provenance"为因果推断的可复现性提供了新工具--agent 决策链的可验证制品使得"哪个 agent 决策导致了处理组与对照组的差异"可追溯，这是传统因果推断（仅观测变量级数据）做不到的。**方法学趋势**是从"输出级评估"转向"决策链级可验证评估"，但**局限**显著：DTF 与 MAIF 的"可验证"是密码学/制品级验证，不等于"因果正确"--可验证制品能证明 agent 执行了某操作，但不能证明该操作因果地导致某结果。三篇论文均未将因果推断（DoWhy/DML）纳入评估框架，"可验证性"与"因果有效性"之间存在未被填补的鸿沟--这是本 Capstone 的贡献机会。

---

## delta_to_unit

1. **"准确率vs因果效应"认识论鸿沟的显式化**：本单元 notes.md TODO2 教"朴素估计--直接算处理组-对照组均值差（有偏）"作为因果推断的反面教材--#1（AINTMA）的 88.4% 准确率正是这种"关联性指标伪装为因果证据"的生产级案例。本单元应增加讨论：AINTMA 的 43% 周期缩减在未做反驳检验的情况下，不能宣称"agent 因果地减少了测试周期"，这对应本单元 TODO3 的安慰剂检验缺失场景。

2. **反驳检验的 agent 决策链追溯**：本单元 notes.md TODO3 教 DoWhy 反驳检验（安慰剂处理/随机混杂/子集检验），但反驳检验在观测数据上是统计层面的--#2（DTF）的"proof-derived authorization"与 #3（MAIF）的"artifact provenance"提供了 agent 决策链级的可审计基础设施。这更新了本单元的反驳检验：在 agent 系统中，"随机混杂检验"可以升级为"agent 决策链追溯"--追溯哪个 agent 决策点引入了混杂。

3. **deepeval BaseMetric 的 provenance 增强**：本单元 notes.md TODO7 教用 deepeval 自定义 BaseMetric 评估 agent 输出中因果证据使用质量--#3（MAIF）的"制品驱动+provenance"范式暗示 deepeval 评估应增加 provenance 维度：不仅评估 agent 输出是否引用因果证据，还评估因果证据的 provenance 链是否完整可验证。

4. **NSW RCT 到 agent 系统评估的迁移 caveat**：本单元 notes.md 用 NSW RCT 数据（职业培训，N=445）教因果推断--但 NSW 是人类 RCT，agent 系统的"处理"是 agent 决策（非随机分配）。三篇前沿论文均未讨论"agent 决策作为处理变量"的因果识别策略，这暗示本单元的 NSW 教学应增加 caveat：agent 系统的因果评估需要处理变量是 agent 决策（非随机），需用 DML/工具变量等观测数据方法，而非 RCT。

---

## open_questions

1. AINTMA 的 88.4% 准确率与 43% 周期缩减是关联性指标--若用本单元的 DoWhy 反驳检验（安慰剂处理/随机混杂）重审 AINTMA 的 18 个月数据，多少比例的"周期缩减"能被归因为 agent 因果效应而非项目混杂？
2. DTF 的 proof-derived authorization 与 MAIF 的 artifact provenance 提供了 agent 决策链的可验证基础设施--但"可验证制品"能证明 agent 执行了某操作，不能证明该操作因果地导致某结果。可验证性（verifiability）与因果有效性（causal validity）之间的鸿沟如何弥合？
3. 本单元用 NSW RCT（人类随机分配）教因果推断，但 agent 系统的"处理"是 agent 决策（非随机分配）--当处理变量是 agent 自主决策时，DoWhy 的后门准则/DML 的 nuisance function 估计策略需要哪些修正？
4. deepeval 的 LLM-as-judge 评估 agent 因果证据使用质量（TODO7），但 LLM-judge 自身有偏差（position bias/length bias）--在 agent 系统的因果评估中，LLM-judge 的偏差是否会系统性地影响 ATE/CATE 估计的元评估（meta-evaluation）？

---

## methodological_critique

这三篇论文在因果推断语境下的方法论局限显著，博后级读者需审慎。**AINTMA（#1）** 是生产级实证的亮点，但评估指标设计有根本缺陷：88.4%"测试优先级准确率"的 ground truth 如何定义（人工标注？是否有标注者间信度？）论文未说明；43%"周期时间缩减"的基线不明确（vs 人工 vs 旧自动化？），存在基线操纵风险；最关键的是完全缺失因果设计--18 个月观察性数据中，项目复杂度/团队经验/工具链变化的混杂未被控制，"周期缩减"可能是混杂而非 agent 效应。这恰好印证本单元"朴素均值差有偏"的教学点。**He & Yu（#2）** 的 DTF 框架概念严谨但"proof-derived authorization"的 proof 本身的正确性如何保证存在递归信任问题--若 proof 链的根信任被污染，整个授权链失效；论文未报告 DTF 在生产 agent 系统上的性能开销（验证延迟/存储成本），可能存在"安全但不可用"的风险。**Narajala & Bhatt（#3）** 的 MAIF 范式最大软肋是"provenance 完整性"--制品的 provenance 链本身也可能被篡改（若 agent 被对抗攻击），MAIF 未讨论 provenance 链的对抗鲁棒性；且未与 DoWhy/econml 等因果推断工具做集成实验，"制品 provenance 辅助因果反驳"目前是概念而非已验证方法。三篇均标注 unverified 或仅生产评估，可复现性存疑。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/capstone-ai-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
