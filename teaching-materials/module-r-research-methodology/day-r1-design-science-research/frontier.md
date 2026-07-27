# frontier.md (v9.0 学术前沿注入层)

> **所属**：module-r-research-methodology · day-r1-design-science-research
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 LLM 辅助系统综述工具作为 DSR artifact 的评估严谨性缺口--当综述工具本身被当作 DSR 贡献发表时，Hevner 准则 3（设计评估）与准则 5（研究严谨性）如何被回避？

---

## frontier_topic

本单元教 Peffers 六步 + Hevner 七准则 + pydantic artifact schema，并以"营销 Agent 系统"作为 DSR artifact 实例。前沿子问题是：2025-2026 年涌现的 LLM 辅助系统综述流水线（meta-pipe、Eligibility-Aware、Multi-Agentic SLR）本身就被作者作为 DSR artifact 发表，它们对 Hevner 准则 3（设计评估）和准则 5（严谨性）的履行程度如何更新本单元所教的"DSR 评估不是自夸而是诚实学术自我审视"原则？

---

## recent_papers

### 1. meta-pipe: An LLM-agent pipeline for end-to-end automated systematic review and meta-analysis
- **arXiv**: https://arxiv.org/abs/2606.28363
- **作者**: Hsieh-Ting Lin, Jiunn-Tyng Yeh
- **年份**: 2026
- **摘要**: 开源 LLM-agent 流水线，集成完整系统综述/荟萃分析工作流并强制人工监督。作者明确声明为"系统描述而非验证研究"，无验证数据报告，体现了 LLM 辅助综述工具从原型到验证的方法论缺口。
- **与本单元的关联**: 直接对应本单元 Hevner 准则 3（设计评估）--作者自述无验证数据，是 DSR artifact 评估缺失的活教材。

### 2. Eligibility-Aware Evidence Synthesis: An Agentic Framework for Clinical Trial Meta-Analysis
- **arXiv**: https://arxiv.org/abs/2604.02678
- **作者**: Yao Zhao, Zhiyue Zhang
- **年份**: 2026
- **摘要**: 提出整合自动试验发现与资格感知荟萃分析的代理框架。LLM 从自然语言查询生成可解释规则，而逻辑操作确定性地执行以确保可复现性，展示了 LLM 与确定性方法混合的综述范式。
- **与本单元的关联**: 对应本单元 March & Smith 四类 artifact 中的 method/instantiation 混合，以及 DSR 准则 6（设计即搜索）的"理论依据 + 确定性约束"路径。

### 3. Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop
- **arXiv**: https://arxiv.org/abs/2607.21920
- **作者**: Zexin Ren, Zixuan Zhao
- **年份**: 2026
- **摘要**: 提出两个带人在回路的 multi-agentic 系统用于临床试验系统文献综述，含异构人设 LLM 代理进行筛选与迭代纠错提取。应用于已发表的网络荟萃分析，系统恢复了原始研究所有试验并发现人工评审遗漏的额外合格试验。
- **与本单元的关联**: 一个 instantiation 类 artifact 的范例，且作者用"恢复原研究 + 发现遗漏试验"作为评估证据，对应 DSR Step 5 评估的定量+定性双路径。

### 4. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis
- **arXiv**: https://arxiv.org/abs/2512.05925
- **作者**: Federico Bianchi, Yongchan Kwon
- **年份**: 2025
- **摘要**: 使用 GPT-5 检查器识别已发表 AI 论文中的客观错误。发现每篇论文平均错误数随时间增长--从 NeurIPS 2021 的 3.8 个增至 NeurIPS 2025 的 5.9 个，对 LLM 辅助科研的可复现性与质量保障提出警示。
- **与本单元的关联**: 对应 DSR 准则 7（研究交流）与 NeurIPS 可复现清单--"发表"不等于"可靠"，DSR artifact 的 Communication 阶段需引入错误量化机制。

---

## critical_synthesis

这 4 篇 2025-2026 论文共同勾勒出 LLM 辅助系统综述工具作为 DSR artifact 发表时的一个核心张力：artifact 被快速产出，但评估（Hevner 准则 3）和严谨性（准则 5）的履行参差不齐。**领域共识**正在形成--LLM 辅助综述工具应采用"LLM + 确定性"混合架构（Eligibility-Aware 的逻辑操作 + Multi-Agentic 的异构人设代理），单一 LLM 调用不足以满足可复现性。**争议**在于人在回路（HITL）的强度：meta-pipe 强制人工监督但无验证数据，而 Multi-Agentic SLR 用"恢复原研究 + 发现遗漏试验"作为验证证据，两者代表了"系统描述"与"验证研究"的方法论分野。**趋势**是综述工具从单 Agent 走向 multi-agent + HITL，并引入确定性约束层以保证可审计性。**局限**也很明显：meta-pipe 自述无验证数据，Eligibility-Aware 仅在临床荟萃分析场景验证，跨域泛化未测；To Err Is Human 则揭示 AI 论文错误率从 3.8 升至 5.9，意味着这些综述工具发表的 artifact 本身可能就携带错误。本单元所教"DSR 评估不是自夸"原则，被前沿证据强化为更尖锐的判断：相当一部分 2026 年发表的 LLM 综述 artifact 在 Hevner 准则 3 上是不达标的。

---

## delta_to_unit

1. **本单元 notes.md TODO5 评分"营销 Agent 系统在 Hevner 准则 3（设计评估）得 5 分"，前沿论文 meta-pipe（2606.28363）作者自述为"系统描述而非验证研究、无验证数据"**--这表明本单元教学生在准则 3 自评 5 分前，必须要求"验证数据报告"作为证据，否则与 2026 年发表的 meta-pipe 同样落入 DSR 评估缺口。建议在 solution.ipynb 的 evaluation_results DataFrame 增加一列"validation_evidence"，强制学生说明是否有外部验证。

2. **本单元 notes.md 教 March & Smith 四类 artifact（constructs/models/methods/instantiations）并用 pydantic ArtifactType 枚举，Eligibility-Aware（2604.02678）展示了一种本单元未覆盖的混合类型**--它是 method（资格感知荟萃分析方法）+ instantiation（代理框架）的组合，且通过"LLM 生成可解释规则 + 逻辑操作确定性执行"双层级设计满足可复现性。这是对本单元"单一 artifact 类型"建模的扩展，建议在 pydantic schema 中支持 `composite_types: List[ArtifactType]`。

3. **本单元 notes.md 的 2026 前沿节提到"可复现研究（artifact 开源 + trace 存档 + 数据文档 + 评估可复现）"，To Err Is Human（2512.05925）量化了这条原则的紧迫性**--NeurIPS 2025 论文平均 5.9 个客观错误，比 2021 年增长 55%。这要求本单元 DSR Step 6（传播）不能只教"发表 + 开源"，还要引入"LLM 错误检查器作为投稿前自检"的步骤，更新本单元 NeurIPS 可复现清单。

4. **本单元 notes.md TODO6"天道推演作为 DSR 设计推演工具"构建同构映射，Multi-Agentic SLR（2607.21920）的"异构人设 LLM 代理 + 迭代纠错"实质上是一种计算化的天道推演沙盘**--多个 LLM 代理扮演不同视角（如天道推演的"多维视角"），迭代纠错对应"反馈学习"。这是对本单元天道推演同构表的第三列"并行世界树"从概念到实现的补充证据。

---

## open_questions

1. 当 LLM 辅助综述工具的作者自述"系统描述而非验证研究"时，DSR 框架是否应引入新的 artifact 子类（如"prototype artifact"）并附强制验证时间窗，以区分于经过外部验证的 instantiation？
2. Eligibility-Aware 的"LLM 生成规则 + 确定性执行"双层架构在非临床领域（如营销、教育）是否仍能保证可复现性，还是临床领域的逻辑结构特殊性使其难以迁移？
3. To Err Is Human 显示 AI 论文错误率逐年上升，那么用 LLM 检查器审查 LLM 辅助综述工具产出的 artifact 是否会引入"LLM 自我偏好盲点"--即检查器与被检查工具共享同类错误模式？
4. Multi-Agentic SLR 用"恢复原研究所有试验 + 发现人工遗漏"作为评估证据，这种"回溯验证"是否能推广为 DSR artifact 评估的通用范式，还是仅适用于有已发表基准的系统综述场景？

---

## methodological_critique

这 4 篇论文的可复现性与可信度存在显著差异，博后级读者需警惕。meta-pipe（2606.28363）作者自述无验证数据，属"系统描述"，引用时不应作为"已验证方法"使用，且其开源代码的实际可用性未经第三方独立复现报告。Eligibility-Aware（2604.02678）仅在临床荟萃分析场景验证，跨域泛化未测，且"确定性逻辑操作"的可复现性强依赖其规则生成层的稳定性，作者未报告规则冲突时的回退行为。Multi-Agentic SLR（2607.21920）的"发现人工评审遗漏的额外合格试验"是强声明，但缺乏对遗漏试验是否真正影响原荟萃分析结论的敏感性分析。To Err Is Human（2512.05925）使用 GPT-5 作为错误检查器，存在 LLM-as-judge 的自我偏好偏差--AI 检查 AI 论文错误，可能系统性低估某些 LLM 习惯性错误，且其"错误计数"依赖 GPT-5 的判断一致性，作者未报告检查器自身的 test-retest reliability。整体而言，这些论文的 benchmark-gaming 风险中等偏高，引用时必须标注其验证缺口。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
