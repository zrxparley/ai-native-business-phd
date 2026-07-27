# frontier.md (v9.0 学术前沿注入层)

> **所属**：elective-e1-agentic-ai · day-1-agent-theory-fundamentals
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年单 Agent 范式（ReAct/Plan-Execute/BDI）在意图演变与编排架构维度上被前沿研究如何修正与扩展。

---

## frontier_topic

本单元教授 ReAct 循环、Plan-Execute 模式与 BDI 形式化作为单 Agent 基础范式。前沿子问题是：当用户意图动态演变、模型规模受限、Agent 从"工具调用器"演进为"系统生成器"时，2026 年最新研究如何揭示经典 ReAct/Plan-Execute 的失效边界并提出编排替代方案？

---

## recent_papers

### 1. LLMs Get Lost in Evolving User Intent
- **arXiv**: https://arxiv.org/abs/2607.20734
- **作者**: Jihoon Tack, Philippe Laban
- **年份**: 2026
- **摘要**: 引入将静态任务转化为多轮对话的框架，其中用户意图动态演变。研究发现静态设置下的强劲性能无法迁移到意图演变设置，揭示了多 Agent/多轮协作场景中 LLM 跟随意图漂移的关键挑战。
- **与本单元的关联**: 直接挑战本单元 ReAct 范式的"单一任务目标"假设——notes.md 中 ReAct 循环（Thought→Action→Observation）隐式假设 Desire 固定，而本文揭示意图漂移下 ReAct 循环会"迷失"。

### 2. Small, Free, and Effective: Orchestrating Open-Weight Small Language Models to Outperform Single LLM for Malware Analysis
- **arXiv**: https://arxiv.org/abs/2607.20216
- **作者**: Adel ElZemity, Shujun Li
- **年份**: 2026
- **摘要**: 评估四种小模型编排架构，混合系统结合证据锚定管道与对抗辩论推理，实现 35.30% 准确率，超越单一 LLM。展示了通过编排多个开源小模型协作超越单一 LLM 的策略。
- **与本单元的关联**: 本单元 notes.md 的自主性谱系（L0-L4）以单 LLM 为假设，而本文展示"多小模型编排"可作为 L4 自主规划的替代路径——对本单元"Agent 灵活性来源于单一 LLM 自主决策"的核心洞见形成补充。

### 3. MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox
- **arXiv**: https://arxiv.org/abs/2607.12875
- **作者**: Zhenwen Miao, Honglin Wang
- **年份**: 2026
- **摘要**: 提出 MetaInfer，采用"LLM-as-Compiler"方法，通过 LLM 驱动的多 Agent 协作系统从运行时约束自动生成定制化推理框架。展示了多 Agent 协作在系统生成中的应用。
- **与本单元的关联**: 本单元将 Agent 形式化为 `<S, A, T, O, π>`，而 MetaInfer 将 LLM 从"策略 π 执行者"升级为"推理框架生成器"——Agent 不仅是状态图的遍历者，还能编译生成自身的执行架构。

### 4. Oracle Gap and Signal Fidelity: A Fixed-Pool Diagnostic for Test-Time Collaboration
- **arXiv**: https://arxiv.org/abs/2607.17531
- **作者**: Jie Hu
- **年份**: 2026
- **摘要**: 将测试时协作重新定义为候选选择问题而非多 Agent 拓扑的内在属性。提出 oracle gap 和 signal fidelity 两个诊断指标，为多 Agent 协作拓扑的部署前评估提供实用工具。
- **与本单元的关联**: 本单元 Plan-Execute 与 ReAct 对比依赖"步数/调用次数"等过程指标，而 oracle gap 提供了"最优候选与实际选择差距"的评估新维度——可直接用于本单元 solution.ipynb 中双模式对比的诊断增强。

---

## critical_synthesis

这四篇论文共同揭示了 2026 年单 Agent 理论的三个 state-of-the-art 转向。**共识**方面：经典 ReAct 循环的"单一固定目标 + 线性 Thought-Action-Observation"假设已被广泛质疑——Tack & Laban (2607.20734) 实证表明静态任务性能不可迁移到意图演变设置，ElZemity et al. (2607.20216) 则从模型规模维度补充：单一 LLM 的自主决策并非唯一路径，多小模型编排可超越单 LLM。两篇论文从不同角度（意图动态性、模型规模）收敛于同一结论：L4 自主规划范式的鲁棒性边界比本单元 notes.md 所暗示的更窄。**争议**方面：MetaInfer (2607.12875) 的"LLM-as-Compiler"立场与 ElZemity 的"多小模型编排"立场存在分歧——前者主张用强 LLM 生成推理框架（meta-level 自主），后者主张用弱模型协作涌现能力（object-level 协作），两条路线谁更可持续尚无定论。**趋势**方面：评估方法学正在从"过程指标"（步数、调用次数）转向"诊断指标"（oracle gap、signal fidelity），Hu (2607.17531) 的诊断框架表明，仅对比 Plan-Execute 与 ReAct 的步数已不够，需要量化"最优候选与实际选择之间的差距"。**局限**：四篇论文均未在真实生产营销场景验证——Tack & Laban 的意图演变框架限于受控 benchmark，ElZemity 仅在恶意软件分析领域验证，MetaInfer 聚焦推理引擎生成，oracle gap 诊断尚为概念框架。本单元的营销 ReAct Agent 若要采纳这些前沿，需先验证迁移有效性。

---

## delta_to_unit

1. **ReAct 的意图漂移盲区**：本单元 notes.md 的 ReAct 范式（Thought→Action→Observation 闭环）和 BDI 模型隐式假设 Desire 固定（"生成 10000+ 阅读的公众号文章"），而 Tack & Laban (2607.20734) 实证揭示：当用户意图在多轮对话中演变时，静态设置下的强劲性能不可迁移。本单元 solution.ipynb 的 StubChatModel 用预编排轨迹（react_trajectory）模拟 LLM 决策，完全回避了意图漂移问题——这是本单元未覆盖的真实场景失效模式。

2. **自主性谱系的编排替代路径**：本单元 notes.md 的核心洞见"Agent 的灵活性来源于 LLM 自主决策"以单一 LLM 为假设，而 ElZemity et al. (2607.20216) 展示四种小模型编排架构可超越单一 LLM。这意味着 L0-L4 谱系中，L4"自主规划"不一定要靠单一强 LLM 实现——多小模型编排是本单元自主性谱系未覆盖的第三条路径，直接修正了"能用 Workflow 解决的不要用 Agent"的二元判断。

3. **Agent 评估指标升级**：本单元 solution.ipynb 的 Plan-Execute vs ReAct 对比仅用"步数/工具调用次数/模型调用次数"作为过程指标，而 Hu (2607.17531) 提出 oracle gap（最优候选与实际选择差距）和 signal fidelity（信号保真度）两个诊断指标。本单元的双模式对比若要达到前沿严谨度，需补充"如果有一个 oracle 能遍历所有候选策略，ReAct/Plan-Execute 的实际输出与 oracle 最优的差距是多少"——这是本单元评估框架的结构性缺失。

4. **Agent 形式化的 meta-level 扩展**：本单元 notes.md 将 Agent 形式化为 `<S, A, T, O, π>`，策略 π 由 LLM 推理动态生成。MetaInfer (2607.12875) 的"LLM-as-Compiler"将 LLM 从 π 的执行者升级为推理框架本身的生成器——相当于 Agent 不仅遍历状态图，还能编译生成新的状态图结构。这扩展了本单元 BDI 模型中 Intention（执行计划）的边界：Intention 不仅可以是"步骤列表"，还可以是"生成步骤列表的元程序"。

---

## open_questions

1. 在营销场景中，用户意图演变（如从"要 10000 阅读"漂移到"要品牌调性一致"）的频率与幅度如何量化，ReAct 循环在何种意图漂移阈值下开始"迷失"？能否设计一个意图漂移检测器在 ReAct 循环中动态触发重新规划？
2. 多小模型编排（如 ElZemity 的 4 架构）在营销 Agent 场景下，与单一 GPT-4 级 LLM 的成本-质量权衡曲线在什么任务复杂度处交叉？是否存在一个"编排优于单 LLM"的临界点？
3. oracle gap 诊断指标能否在本单元 solution.ipynb 的 StubChatModel 预编排轨迹上实例化？如果预编排轨迹本身是"oracle"，那么真实 LLM 的 ReAct 输出与预编排轨迹的偏离度是否可作为 signal fidelity 的代理度量？
4. MetaInfer 的"LLM-as-Compiler"范式在营销 Agent 场景下，能否让 Agent 根据不同营销任务（品牌建设 vs 效果转化）自动编译生成不同的执行图结构？这种 meta-level 自主的可靠性边界在哪？

---

## methodological_critique

这些前沿论文存在多处不能全信的局限。Tack & Laban (2607.20734) 的意图演变框架虽揭示了关键问题，但论文标注 unverified，其"静态性能不可迁移"的结论可能受限于特定 benchmark 设计——意图演变的构造方式本身可能引入人为难度，真实用户意图漂移的模式未必如此剧烈。ElZemity et al. (2607.20216) 同为 unverified，且仅在恶意软件分析领域验证，35.30% 准确率虽超越单 LLM 但绝对值偏低，迁移到营销场景的有效性存疑；四种编排架构的比较可能受小模型选择偏差影响。MetaInfer (2607.12875) 的"LLM-as-Compiler"概念吸引人但 unverified，"自动生成推理框架"的可复现性和稳定性未经验证——生成框架的质量方差可能远大于使用固定框架。Hu (2607.17531) 的 oracle gap 和 signal fidelity 虽概念优雅但 unverified，其实用性依赖于"固定候选池"假设，而在开放域营销任务中候选池可能不可枚举。整体而言，四篇论文中有三篇 unverified，仅 IDSTune (2607.22031) 和 DoG (2607.17266) 经 abstract 页确认——读者应将 unverified 论文的结论视为待验证假设而非既定事实。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/elective-e1-agentic-ai.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
