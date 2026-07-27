# frontier.md (v9.0 学术前沿注入层)

> **所属**：module-r-research-methodology · day-r4-systematic-review-prisma
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 LLM 辅助系统综述工具如何直接扩展 PRISMA 2020 的 27 条清单--L-PRISMA 提出 GenAI 时代的 PRISMA 扩展，meta-pipe 提供端到端 LLM-agent 流水线，ROBoto2 自动化 Phase 3 偏倚评估，而 Beyond Accuracy 揭示的 LLM 残余非确定性如何动摇 PRISMA 的可复现性根基？

---

## frontier_topic

本单元教 PRISMA 2020 四阶段（Identification/Screening/Quality Assessment/Synthesis）+ 27 条清单 + Kitchenham 五维质量评估 + Cohen's kappa + ASReview 主动学习 + scikit-learn 模拟。前沿子问题是：2025-2026 年 L-PRISMA、meta-pipe、Multi-Agentic SLR、ROBoto2 等工具如何具体扩展或挑战 PRISMA 2020 各阶段的可重复方法论，以及 Beyond Accuracy 揭示的"温度=0 仍非确定"对 PRISMA Item 5-8（检索策略与筛选流程）的可复现性要求构成何种根本挑战？

---

## recent_papers

### 1. L-PRISMA: An Extension of PRISMA in the Era of Generative Artificial Intelligence (GenAI)
- **arXiv**: https://arxiv.org/abs/2603.19236
- **作者**: Samar Shailendra, Rajan Kadel
- **年份**: 2026
- **摘要**: 提出在 PRISMA 框架中整合人工主导综合与 GenAI 辅助统计预筛选，应对 LLM 非确定性带来的可复现性、透明度与可审计性挑战。统计层的确定性增强了可复现性，为负责任地将 GenAI 纳入系统综述工作流提供路径。
- **与本单元的关联**: 直接对应本单元 PRISMA 2020 四阶段--提出 GenAI 时代的 PRISMA 扩展（L-PRISMA），更新本单元教的"27 条清单"为"27 + GenAI 透明度条款"。

### 2. Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop
- **arXiv**: https://arxiv.org/abs/2607.21920
- **作者**: Zexin Ren, Zixuan Zhao
- **年份**: 2026
- **摘要**: 提出两个带人在回路的 multi-agentic 系统用于临床试验系统文献综述，含异构人设 LLM 代理进行筛选与迭代纠错提取，恢复了原始研究所有试验并发现人工评审遗漏的额外合格试验。
- **与本单元的关联**: 对应本单元 PRISMA Phase 2（Screening）+ Phase 4（Synthesis）的 multi-agent 化--异构人设代理执行筛选，人在回路做迭代纠错，是 ASReview 主动学习的高级形态。

### 3. meta-pipe: An LLM-agent pipeline for end-to-end automated systematic review and meta-analysis
- **arXiv**: https://arxiv.org/abs/2606.28363
- **作者**: Hsieh-Ting Lin, Jiunn-Tyng Yeh
- **年份**: 2026
- **摘要**: 开源 LLM-agent 流水线，集成完整系统综述/荟萃分析工作流并强制人工监督。作者明确声明为"系统描述而非验证研究"，无验证数据报告，体现了 LLM 辅助综述工具从原型到验证的方法论缺口。
- **与本单元的关联**: 对应本单元 PRISMA 全四阶段的端到端自动化尝试，但作者自述无验证数据--是本单元教"PRISMA 可重复性"的反面教材，提示学生区分"系统描述"与"验证研究"。

### 4. Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs
- **arXiv**: https://arxiv.org/abs/2604.27006
- **作者**: Gilberto Sussumu Hida, Danilo Monteiro Ribeiro
- **年份**: 2026
- **摘要**: 评估 12 个 LLM 与 4 个经典模型在 SLR 证据筛选中的表现与变异性。发现 LLM 即使在温度为零时仍表现出显著异质性与残余非确定性，对 LLM 辅助综述的可复现性提出根本性挑战。
- **与本单元的关联**: 直接挑战本单元 PRISMA Item 7-8（筛选流程与筛选者）的"可重复性"假设--如果 LLM 筛选器在温度=0 仍非确定，Cohen's kappa 的 test-retest 假设不成立。

### 5. ROBoto2: An Interactive System and Dataset for LLM-assisted Clinical Trial Risk of Bias Assessment
- **arXiv**: https://arxiv.org/abs/2511.03048
- **作者**: Anthony Hevia, Sanjana Chintalapati
- **年份**: 2025
- **摘要**: 开源平台用于 LLM 辅助临床试验偏倚风险评估，包含 521 篇儿科临床试验报告数据集（8954 个信号问题与 1202 条证据段落）。为 LLM 辅助综述的质量评估阶段提供可复现的工具与基准数据。
- **与本单元的关联**: 直接对应本单元 PRISMA Phase 3（Quality Assessment）+ Kitchenham 五维 + Risk of Bias 三级分级--ROBoto2 是 RoB 评估的 LLM 辅助工具化实现。

---

## critical_synthesis

这 5 篇论文共同构成 2025-2026 年 LLM 辅助系统综述方法论的最完整前沿图景，且与本单元 PRISMA 四阶段形成精确映射。**共识**已形成：PRISMA 2020 需要 GenAI 时代扩展（L-PRISMA 直接提出），扩展方向是"人工主导综合 + GenAI 辅助预筛选"分工 + 统计层确定性强化可复现性。**争议**在于 LLM 在 PRISMA 流程中的角色定位：meta-pipe 追求端到端自动化（强 LLM 角色），Multi-Agentic SLR 把 LLM 作为异构代理 + 人在回路纠错（中 LLM 角色），L-PRISMA 把 LLM 限制在预筛选（弱 LLM 角色）--三种角色强度反映了"自动化 vs 可审计性"的方法论张力。**趋势**是 PRISMA 各阶段被 LLM 工具化：Phase 1（Identification）由 arxiv API + LLM 查询扩展自动化，Phase 2（Screening）由 multi-agent 异构人设 + ASReview 主动学习加速，Phase 3（Quality Assessment）由 ROBoto2 等 LLM 辅助 RoB 工具化，Phase 4（Synthesis）由人在回路综合 + GenAI 预筛选分工。**局限**尖锐且根本：Beyond Accuracy（2604.27006）证明 LLM 即使温度=0 仍有残余非确定性，这直接动摇 PRISMA Item 7-8 的"筛选流程可重复"假设--如果同一 LLM 筛选器对同一文献集多次运行结果不同，PRISMA flow diagram 中的数字不再是确定值而是分布。meta-pipe 自述无验证数据，是"系统描述"而非"验证研究"，其端到端自动化声明缺乏外部验证。ROBoto2 仅在儿科临床试验场景验证，跨域泛化未测。整体判断：前沿工具正在快速工具化 PRISMA 各阶段，但 PRISMA 2020 的可复现性根基（Item 5-8）正被 LLM 残余非确定性侵蚀，需要新的"LLM 调用确定性等级"报告标准。

---

## delta_to_unit

1. **本单元 notes.md TODO3"用 scikit-learn 计算两位筛选者的 Cohen's kappa"，Beyond Accuracy（2604.27006）证明温度=0 时 LLM 仍有残余非确定性**--这意味着本单元教的"两位筛选者 kappa"在 LLM 作为筛选者时假设不成立。建议在 solution.ipynb 的 kappa 计算后新增"LLM 筛选者变异性报告"：同一 LLM 筛选器对同一文献集运行 K 次，计算 kappa 的分布与置信区间，而非单一值。

2. **本单元 notes.md TODO4"实现 Kitchenham & Charters 五维质量评估 + Risk of Bias 三级分级"，ROBoto2（2511.03048）提供了 LLM 辅助 RoB 评估的工具化实现 + 521 篇儿科临床试验基准数据集**--这更新了本单元 Phase 3 的方法论：RoB 评估不再仅靠人工逐条打分，可引入 LLM 辅助信号问题标注。建议在 notes.md Phase 3 表中新增"LLM-assisted RoB"路径。

3. **本单元 notes.md TODO5"模拟 ASReview 主动学习筛选机制（种子集 -> TF-IDF+LogReg -> 迭代查询 -> 效率计算）"，Multi-Agentic SLR（2607.21920）的"异构人设 LLM 代理 + 人在回路迭代纠错"是 ASReview 的高级形态**--ASReview 用单一分类器排序，Multi-Agentic SLR 用多代理三角验证 + 人在回路纠错。这更新了本单元 ASReview TODO：从"单一分类器主动学习"走向"多代理 + HITL 协同主动学习"。

4. **本单元 notes.md 关键回顾 1"PRISMA 2020 27 条清单"，L-PRISMA（2603.19236）直接提出 GenAI 时代的 PRISMA 扩展**--这要求本单元 27 条清单教学新增"GenAI 透明度条款"：当使用 LLM 辅助任一阶段时，必须报告 LLM 模型版本、提示词、温度、调用次数、变异性度量。这是对本单元 Item 5-8 的实质性扩展。

5. **本单元 notes.md TODO6"用 matplotlib 画 PRISMA 2020 流程图（识别->去重->筛选->纳入各阶段真实数字）"，meta-pipe（2606.28363）的端到端自动化尝试 + 自述无验证数据提示流程图数字的可信度问题**--当流程图数字由 LLM 工具产生时，应附加"确定性等级标注"（如"Phase 1 数字来自 arxiv API 确定性调用 / Phase 2 数字来自 LLM 非确定调用，变异性 ±N%"），更新本单元流程图绘制规范。

---

## open_questions

1. 当 LLM 筛选器在温度=0 仍表现出残余非确定性时，PRISMA Item 7-8 的"筛选者一致性"是否应从单一 Cohen's kappa 升级为"K 次运行的 kappa 分布 + 置信区间"，并作为新的清单条目？
2. L-PRISMA 的"统计层确定性增强可复现性"声明在跨域（如营销、教育、软件工程）综述中是否仍成立，还是临床领域的逻辑结构特殊性使其难以迁移？
3. ROBoto2 的 LLM 辅助 RoB 评估在儿科临床试验场景验证，其 521 篇基准数据集是否存在"儿科试验特殊性"，导致在其他临床或非临床领域的 RoB 评估泛化失败？
4. Multi-Agentic SLR 的"发现人工评审遗漏的额外合格试验"是否揭示了 PRISMA 双盲筛选的系统性盲点--即两位人工筛选者可能共享同一种"领域偏见"，而异构人设 LLM 代理能识别这种盲点？
5. meta-pipe 自述"系统描述而非验证研究"却已发表，PRISMA 方法论是否应引入新的"工具验证等级"标准（如 Level 0 系统描述 / Level 1 内部验证 / Level 2 外部独立验证），以区分 LLM 综述工具的成熟度？

---

## methodological_critique

这 5 篇论文在 PRISMA 方法论视角下可信度差异显著，博后引用需谨慎。L-PRISMA（2603.19236，verified）是本单元最直接的引用，但其"统计层确定性增强可复现性"声明强依赖统计层与 GenAI 层接口的清洁性，作者未报告接口处的错误传播，且扩展条款的强制性等级（must vs should vs may）未明确。Multi-Agentic SLR（2607.21920，verified）的"发现人工遗漏试验"是强声明，但缺乏对遗漏试验是否影响原荟萃分析结论的敏感性分析，且异构人设代理的人设选择本身可能引入研究者偏见。meta-pipe（2606.28363，unverified）作者自述无验证数据，属"系统描述"，引用时不应作为"已验证方法"，其端到端自动化声明的实际可用性未经第三方独立复现。Beyond Accuracy（2604.27006，unverified）是本单元关键引用，但"12 个 LLM + 4 个经典模型"样本规模不足以泛化，且未区分残余非确定性的来源（数值精度、采样机制、框架实现、缓存命中）。ROBoto2（2511.03048，unverified）仅在儿科临床试验验证，521 篇数据集可能携带"儿科试验特殊性"，跨域泛化未测，且 8954 个信号问题的标注一致性（人工标注 kappa）未报告。整体而言，这批论文的 benchmark-gaming 风险中等偏高，PRISMA 流程图数字的可信度需结合 LLM 调用确定性等级交叉判断。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
