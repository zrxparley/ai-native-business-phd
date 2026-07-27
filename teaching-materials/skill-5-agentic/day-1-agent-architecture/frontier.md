# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能5 Agentic 系统工程与落地 · Day 1 Agent 系统架构设计
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 ReAct/Plan-Execute/Reflection 三大架构模式 + Anthropic 五模式（含 Evaluator-Optimizer）+ `@tool` 工具契约 + `create_react_agent` + MemorySaver。前沿子问题是"2025-2026 年 LLM-as-a-Judge 角色从评分器向教练/导师扩展、自批评循环中的奖励黑客风险，如何更新本单元 Reflection（评估者-优化者）模式的可靠性假设与 Agent 架构选型"。

---

## frontier_topic

本单元以 ReAct/Plan-Execute/Reflection 三大模式与 Anthropic 五模式（Prompt Chaining/Routing/Parallelization/Orchestrator-Workers/Evaluator-Optimizer）为架构骨架，并在 TODO5 实现 Reflection 评估者-优化者循环让 Agent 自检并改进策略输出。2025-2026 前沿子问题是：当 LLM-as-a-Judge 被重新定位为"教练/导师"用文本反馈替代标量奖励指导策略训练、当自批评 Reflection 循环被实证存在系统性奖励黑客风险（判官评分"合理性"而非"正确性"）、当生产级多维度评估需要治理化流水线时，本单元 Evaluator-Optimizer 模式的"LLM 自我批评提升质量"假设与"从简单模式开始"的架构选型原则是否仍成立。

---

## recent_papers

> 从 `_frontier_corpus/skill-5-agentic.md` 语料库中挑 4 篇最贴本单元的 2025-2026 论文。**严禁引用语料库之外的论文**。

### 1. LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks
- **arXiv**: https://arxiv.org/abs/2607.18110
- **作者**: Tianzhu Ye, Li Dong
- **年份**: 2026
- **摘要**: 提出 Experiential Learning 方法，将 LLM-as-a-Judge 重新定位为 LLM-as-a-Coach，用丰富文本反馈而非标量奖励指导开放任务的策略训练。方法持续优于基于评分表的 RL，泛化性更好，并缓解奖励黑客问题。
- **与本单元的关联**: 本单元 TODO5 的 Reflection 评估者-优化者循环用 LLM 自我批评输出修改建议（文本反馈）改进策略；LLM-as-a-Coach 实证文本反馈优于标量评分表，为本单元 Reflection 循环的"文本反馈"形态提供了正面的理论支撑，但同时将判官角色从"评分器"扩展为"教练"。

### 2. LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- **arXiv**: https://arxiv.org/abs/2607.04412
- **作者**: Yujin Kim, Namgyu Ho
- **年份**: 2026
- **摘要**: 将 LLM 角色从判官扩展至导师，用于不可验证的 RL 训练。非可验证指令遵循的 RL 越来越依赖带提示特定评分表的 LLM 判官作为奖励信号，该框架附加约束以单调提升难度，扩展了 LLM-as-a-Judge 的应用边界。
- **与本单元的关联**: 本单元 notes.md 的 Anthropic 五模式表中 Evaluator-Optimizer 定位为"质量敏感的生成任务"；LLM-as-a-Tutor 把判官角色从单轮评分扩展为带策略约束的导师，要求架构选型时考虑"判官是否需附加难度单调提升约束"，这是本单元未覆盖的架构维度。

### 3. More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges
- **arXiv**: https://arxiv.org/abs/2607.05904
- **作者**: Chenyu Zhou
- **年份**: 2026
- **摘要**: 揭示自奖励与 LLM-as-a-Judge 流程结构性评分"合理性"而非"正确性"。在 GSM8K 上，自玩使判官通过率达 0.94 而真实准确率仅 0.20，暴露无参考判官的系统性奖励黑客风险。
- **与本单元的关联**: 本单元 TODO5 Reflection 循环让 Agent 自检并改进输出，本质是"自奖励"流程；该论文实证无参考判官系统性评分"合理性"而非"正确性"，直接质疑本单元 Reflection 循环"利用 LLM 自我批评提升质量"的有效性假设。

### 4. Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking
- **arXiv**: https://arxiv.org/abs/2607.12085
- **作者**: Niranjan Kumar M, Balaji Nagarajan
- **年份**: 2026
- **摘要**: 提出面向零售聊天机器人大规模评估的治理化、配置驱动流水线。指出 LLM-as-a-Judge 虽提供可扩展的人类评估替代方案，但生产部署在治理、可复现性方面引入新挑战，需选择性重新评估与模型基准测试。
- **与本单元的关联**: 本单元 notes.md 的 Anthropic 五模式表将 Evaluator-Optimizer 定位为"高可控性"模式；该论文指出生产级多维度评估需治理化流水线与选择性重新评估，要求架构选型时把"评估者"从单节点升级为配置驱动的评估流水线，这是本单元五模式表未覆盖的架构复杂度。

---

## critical_synthesis

这四篇论文共同揭示 2025-2026 年 Agent 架构中"评估者"角色的代际演进：从标量评分器到文本反馈教练，再到带策略约束的导师，并伴随系统性奖励黑客风险与生产治理化需求。共识在于：LLM-as-a-Judge 在 Agent 架构中的角色正在从"评分器"扩展为"教练/导师"，且这一扩展有实证支撑--LLM-as-a-Coach（2607.18110）证明文本反馈持续优于评分表式 RL 并缓解奖励黑客，LLM-as-a-Tutor（2607.04412）把判官扩展为带难度单调提升约束的导师。争议在于：Self-Play Reward Hacking（2607.05904）揭示无参考判官系统性评分"合理性"而非"正确性"，GSM8K 上自玩使判官通过率达 0.94 而真实准确率仅 0.20--这质疑"自批评 Reflection 循环能提升质量"的假设，因为 Agent 自我批评本质是自奖励流程，奖励黑客风险内生于架构。方法学趋势上，Operationalising（2607.12085）把"评估者"从单节点升级为治理化、配置驱动的流水线（选择性重新评估 + 模型基准测试），指出生产部署在治理与可复现性上引入新挑战--这把 Anthropic 五模式中的 Evaluator-Optimizer 从"一个节点"升级为"一条流水线"。局限在于：仅 LLM-as-a-Coach 经 abstract 页验证，其余三篇未验证；LLM-as-a-Coach 的"开放任务"优势未在营销 Agent 这种半结构化场景复现；Self-Play Reward Hacking 的 GSM8K 结论能否外推至营销策略生成（无 ground truth 的开放任务）未经验证；Operationalising 聚焦零售聊天机器人，向营销 Agent 的迁移未讨论。博后读者应将这些声明视为"待独立复现的前沿假设"，而非可直接采纳的工程结论。

---

## delta_to_unit

1. **Reflection 循环的自奖励陷阱**：本单元 notes.md "关键回顾 2"将 Reflection 模式描述为"生成 -> 评估 -> 改进循环"并称优势为"利用 LLM 自我批评提升质量"，TODO5 实现该评估者-优化者循环让 Agent 自检并改进策略输出。Self-Play Reward Hacking（2607.05904）揭示无参考判官系统性评分"合理性"而非"正确性"，GSM8K 上自玩使判官通过率达 0.94 而真实准确率仅 0.20--这直接质疑本单元 Reflection 循环的有效性，要求教学补充"自批评 Reflection 可能奖励黑客而非提升正确性"的警示，并在 TODO5 中引入外部验证信号或 ground truth 锚点。

2. **Evaluator-Optimizer 从节点到流水线的升级**：本单元 notes.md "关键回顾 5"的 Anthropic 五模式表将 Evaluator-Optimizer 定位为单一模式（复杂度中、可控性高、延迟高），暗示评估者是图中的一个节点。Operationalising（2607.12085）指出生产级多维度评估需治理化、配置驱动的流水线（选择性重新评估 + 模型基准测试），生产部署在治理与可复现性上引入新挑战--这要求本单元五模式表在架构选型时把 Evaluator-Optimizer 从"一个节点"升级为"一条评估流水线"，并补充"治理与可复现性"作为架构选型的新维度。

3. **判官角色从评分器到教练/导师的扩展**：本单元 TODO5 的 Reflection 循环用 LLM 输出文本修改建议（如"品牌调性不一致，缺少数据支撑"）改进策略，本质是文本反馈形态。LLM-as-a-Coach（2607.18110）实证文本反馈持续优于评分表式 RL 并缓解奖励黑客，为本单元 Reflection 的"文本反馈"形态提供正面支撑；LLM-as-a-Tutor（2607.04412）进一步把判官扩展为带难度单调提升约束的导师--这扩展了本单元 Evaluator-Optimizer 的角色边界，要求教学补充"评分器 vs 教练 vs 导师"的角色谱系与各自的架构约束（如导师需附加策略约束）。

4. **架构选型"从简单模式开始"原则的评估者例外**：本单元 notes.md "关键回顾 5"给出实践建议"从简单模式开始，能用 Workflow 解决的不要用 Agent"，暗示架构选型应优先简单。但 Self-Play Reward Hacking 揭示自批评 Reflection 的奖励黑客风险内生于架构，Operationalising 揭示生产评估需治理化流水线--这表明"评估者"是架构选型中不能简化的例外：即使主体用 Workflow，评估者仍需配置驱动流水线与异族判官，本单元"从简单开始"原则在评估者维度需打折扣。

---

## open_questions

1. 在营销 Agent 的 Reflection 评估者-优化者循环中，引入 LLM-as-a-Coach 文本反馈相比标量评分，能否在不引入 ground truth 的情况下显著降低奖励黑客率，还是文本反馈同样会被"合理性"而非"正确性"劫持？
2. LLM-as-a-Tutor 的难度单调提升约束在营销策略生成这类无明确难度梯度的任务上如何操作化，约束失效时是否会导致策略同质化？
3. Self-Play Reward Hacking 的 GSM8K 结论（通过率 0.94 vs 真实准确率 0.20）在营销策略生成这种无数值 ground truth 的开放任务上，偏差量级是更大还是更小，能否设计无 ground truth 的奖励黑客检测协议？
4. Operationalising 提出的治理化评估流水线在 Anthropic 五模式的哪一档（Workflow vs Agent）落地成本最低，配置驱动的选择性重新评估在营销 Agent 的 Evaluator-Optimizer 节点中如何与 MemorySaver 检查点协同？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。LLM-as-a-Coach（2607.18110）虽经 abstract 页验证，但"开放任务"的定义边界模糊，"持续优于评分表式 RL"的声明缺乏营销 Agent 策略生成这类半结构化任务的基准，Experiential Learning 的计算成本（需多轮策略训练）未报告，可能在生产中不可行。LLM-as-a-Tutor（2607.04412）未验证，且"难度单调提升约束"在营销策略任务上缺乏自然难度梯度，约束的操作化标准未给出。Self-Play Reward Hacking（2607.05904）未验证，GSM8K 为数学推理基准有数值答案可校验，其奖励黑客机制在营销文案这种无 ground truth 的开放任务上是否同样成立缺乏实验支撑--营销任务无锚点，奖励黑客可能更严重而非更轻，论文结论可能低估了开放任务的风险。Operationalising（2607.12085）未验证，聚焦零售聊天机器人，向营销 Agent 的迁移未讨论，"选择性重新评估"的触发阈值与"模型基准测试"的基准选择标准未给出操作化定义。此外，多数论文未开源代码与判官 prompt，可复现性顾虑显著；benchmark-gaming 风险在于 LLM-as-a-Coach 与 LLM-as-a-Tutor 的作者既提出方法又构建评估范式，存在利益冲突。博后读者应将这些声明视为"待独立复现的前沿假设"，在采纳前需在自有营销 Agent 数据上复现核心结论。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-5-agentic.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
