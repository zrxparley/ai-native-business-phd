# frontier.md (v9.0 学术前沿注入层)

> **所属**：module-r-research-methodology · day-r3-mixed-methods-research
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 LLM 辅助系统综述工具如何重新定义混合方法研究的"整合"策略--从"并排展示"（joint display）走向"LLM 生成规则 + 确定性执行"的概率-逻辑混合，以及 LLM 残余非确定性对定性编码 Cohen's kappa 的根本挑战？

---

## frontier_topic

本单元教 Creswell & Plano Clark 三种设计、Morse 三种整合策略（合并/解释/构建）、joint display 联合展示矩阵、Beta-Binomial 贝叶斯整合、LLM-as-a-judge 定性编码。前沿子问题是：2025-2026 年 LLM 辅助综述工具展示的"异构人设代理三角验证"与"LLM 规则 + 确定性逻辑混合架构"如何更新 Morse 的三整合策略，以及 Beyond Accuracy 揭示的"温度=0 仍非确定"如何动摇本单元 TODO6 的 LLM-as-a-judge 编码一致性假设？

---

## recent_papers

### 1. Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs
- **arXiv**: https://arxiv.org/abs/2604.27006
- **作者**: Gilberto Sussumu Hida, Danilo Monteiro Ribeiro
- **年份**: 2026
- **摘要**: 评估 12 个 LLM 与 4 个经典模型在 SLR 证据筛选中的表现与变异性。发现 LLM 即使在温度为零时仍表现出显著异质性与残余非确定性，对 LLM 辅助综述的可复现性提出根本性挑战。
- **与本单元的关联**: 直接挑战本单元 TODO6"LLM-as-a-judge 编码 + Cohen's kappa 一致性"--如果 LLM 在温度=0 仍非确定，kappa 的 test-retest 假设不成立。

### 2. Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop
- **arXiv**: https://arxiv.org/abs/2607.21920
- **作者**: Zexin Ren, Zixuan Zhao
- **年份**: 2026
- **摘要**: 提出两个带人在回路的 multi-agentic 系统用于临床试验系统文献综述，含异构人设 LLM 代理进行筛选与迭代纠错提取，恢复了原始研究所有试验并发现人工评审遗漏的额外合格试验。
- **与本单元的关联**: 异构人设 LLM 代理 = 计算化三角验证（多视角交叉验证），是 Morse"合并（Merging）"策略的 multi-agent 实现范例。

### 3. Eligibility-Aware Evidence Synthesis: An Agentic Framework for Clinical Trial Meta-Analysis
- **arXiv**: https://arxiv.org/abs/2604.02678
- **作者**: Yao Zhao, Zhiyue Zhang
- **年份**: 2026
- **摘要**: 提出整合自动试验发现与资格感知荟萃分析的代理框架。LLM 从自然语言查询生成可解释规则，而逻辑操作确定性地执行以确保可复现性，展示了 LLM 与确定性方法混合的综述范式。
- **与本单元的关联**: "LLM 生成规则（定性层）+ 确定性逻辑执行（定量层）"是 Morse"构建（Building）"策略的混合方法新范式--用定性发现构建定量执行框架。

### 4. L-PRISMA: An Extension of PRISMA in the Era of Generative Artificial Intelligence (GenAI)
- **arXiv**: https://arxiv.org/abs/2603.19236
- **作者**: Samar Shailendra, Rajan Kadel
- **年份**: 2026
- **摘要**: 提出在 PRISMA 框架中整合人工主导综合与 GenAI 辅助统计预筛选，应对 LLM 非确定性带来的可复现性、透明度与可审计性挑战。统计层的确定性增强了可复现性。
- **与本单元的关联**: "GenAI 辅助预筛选（定性层）+ 人工主导综合（解释层）"对应 Morse"解释（Explaining）"策略--用 LLM 预筛选结果解释人工综合的焦点。

---

## critical_synthesis

这 4 篇论文共同指向一个对混合方法研究方法论的根本更新：Morse 三整合策略（合并/解释/构建）在 LLM 时代获得了计算化实现，但同时也暴露了"整合"的新认识论问题。**共识**正在形成--单一 LLM 调用不足以承担整合，必须采用"LLM + 确定性"或"异构 LLM + 人在回路"的混合架构（Eligibility-Aware、Multi-Agentic SLR、L-PRISMA 三者一致）。**争议**在于"整合"的认识论地位：Eligibility-Aware 把 LLM 生成的规则交给确定性逻辑执行，实质是把定性层"硬约束"为定量层，这与传统 MMR"定性发现构建定量框架"（Building 策略）的方向一致但更严格；Multi-Agentic SLR 的异构人设代理则是"Merging"的 multi-agent 化，每个代理代表一个视角，通过迭代纠错实现三角验证。**趋势**是 MMR 整合从"并排展示"走向"概率-逻辑混合"--LLM 提供概率判断，确定性逻辑提供可复现执行。**局限**关键：Beyond Accuracy（2604.27006）证明 LLM 即使温度=0 仍有残余非确定性，这意味着以 LLM 作为"定性编码器"的混合方法（如本单元 TODO6 的 LLM-as-a-judge 编码）其 Cohen's kappa 的 test-retest 假设不成立--同一编码器对同一文本的多次编码可能不同。这要求 MMR 引入"LLM 调用变异性"作为新的整合不确定性来源，而非仅报告单一 kappa 值。整体判断：前沿工作流强化了"整合是 MMR 核心难点"的共识，但要求把"LLM 非确定性"显式纳入整合的不确定性预算。

---

## delta_to_unit

1. **本单元 notes.md TODO6"LLM 辅助定性编码模拟--设计 LLM-as-a-judge 编码提示词模板，对比人工编码与 LLM 编码的一致性"，Beyond Accuracy（2604.27006）证明温度=0 时 LLM 仍有残余非确定性**--这要求本单元 TODO6 不能只报告单一 kappa 值，必须新增"LLM 编码变异性度量"：同一文本同一提示运行 K 次，计算编码分布的熵或多数投票一致率。这是对本单元 solution.ipynb 中 kappa 计算的扩展。

2. **本单元 notes.md 关键回顾 3"Morse 三种整合策略（合并/解释/构建）"，Eligibility-Aware（2604.02678）的"LLM 生成规则 + 确定性逻辑执行"是 Building 策略的新范式**--传统 Building 是"用定性发现构建定量研究的理论框架和测量工具"，而 Eligibility-Aware 把定性层（LLM 规则）硬约束为定量执行层（确定性逻辑），这是一种更严格的"可执行 Building"。建议在 notes.md 整合策略表中新增"LLM-augmented Building"子类。

3. **本单元 notes.md TODO4"构建 joint display 联合展示矩阵"把定量统计与定性主题并排对照，Multi-Agentic SLR（2607.21920）的异构人设代理提供了"动态 joint display"的实现路径**--每个代理代表一个视角，通过迭代纠错在矩阵中填充交叉证据，而非静态并排。这更新了本单元 joint display TODO：从"静态并排"走向"多 agent 迭代填充"。

4. **本单元 notes.md TODO5"贝叶斯整合--将定性编码的主题置信度转化为先验分布，用 Beta-Binomial 模型更新培训效应后验"，L-PRISMA（2603.19236）的"GenAI 辅助预筛选 + 人工主导综合"分工为贝叶斯整合提供了新的先验来源**--GenAI 预筛选的结构化判断可作为先验，人工主导综合的结果作为似然，这比本单元教的"定性编码置信度作为先验"更系统化。

---

## open_questions

1. 当 LLM 在温度=0 仍表现出残余非确定性时，混合方法中"LLM 编码一致性"是否应从单一 Cohen's kappa 升级为"K 次运行的一致性分布"，并报告其置信区间？
2. Eligibility-Aware 的"LLM 生成规则 + 确定性逻辑执行"架构中，如果 LLM 生成的规则本身有偏差，确定性执行层会放大还是抑制这种偏差--即 Building 策略的"硬约束"是否会成为"硬错误"？
3. Multi-Agentic SLR 的异构人设代理作为"计算化三角验证"，其人设设计的多样性（agent 数量与人设差异度）是否存在一个"三角验证收益递减点"，超过后增加代理不再显著提升验证质量？
4. 在混合方法的贝叶斯整合中，LLM 预筛选提供的先验与人工综合提供的似然之间的"信息重叠"如何量化--是否会因 LLM 与人工基于相同原始数据而违反贝叶斯更新的独立性假设？

---

## methodological_critique

这 4 篇论文在 MMR 方法论视角下可信度参差。Beyond Accuracy（2604.27006，unverified）是本单元最关键的引用，但其"12 个 LLM + 4 个经典模型"样本规模不足以泛化到所有 LLM 架构，且未区分残余非确定性的来源（数值精度、采样机制、框架实现、缓存命中），其"温度=0 仍非确定"声明需更细粒度的归因分析。Multi-Agentic SLR（2607.21920，verified）的"发现人工遗漏试验"是强声明，但未报告遗漏试验对原荟萃分析结论的方向性影响，且异构人设代理的人设选择本身可能引入研究者偏见--人设设计是"研究者构建的视角"，并非真正的利益相关方多样性。Eligibility-Aware（2604.02678，unverified）的"LLM 规则 + 确定性执行"在临床场景验证，但作者未报告 LLM 规则冲突时的回退行为，跨域泛化未测，其"可复现性"强依赖规则生成层的稳定性。L-PRISMA（2603.19236，verified）的"统计层确定性增强可复现性"是强声明，但统计层与 GenAI 层接口处的错误传播未讨论。整体而言，这批论文都未充分讨论"LLM 与人工基于相同原始数据"导致的贝叶斯独立性假设违反，这是 MMR 整合方法论的隐性漏洞，博后引用时必须标注。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
