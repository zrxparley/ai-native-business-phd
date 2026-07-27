# frontier.md (v9.0 学术前沿注入层)

> **所属**：module-r-research-methodology · day-r6-research-ethics-ai-governance
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 LLM 辅助系统综述工具的可复现性危机如何重新定义 Belmont Report 善行原则的履行--当 LLM 即使温度=0 仍有残余非确定性、已发表 AI 论文错误率逐年上升、LLM 使用透明度存在系统性缺口时，研究伦理的底线在哪里？

---

## frontier_topic

本单元教 Belmont Report 三原则（尊重个人/善行/公平正义）、NIST AI RMF 四步循环、EU AI Act 风险分级、garak/PyRIT 红队测试、天道推演伦理风险预判。前沿子问题是：2025-2026 年 LLM 辅助综述工具揭示的可复现性危机（残余非确定性 + 错误率上升 + 透明度缺口）如何具体更新 Belmont 善行原则的履行方式，以及 ROBoto2 等 LLM 辅助偏倚评估工具如何成为 Belmont 公平正义原则的新操作化手段？

---

## recent_papers

### 1. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis
- **arXiv**: https://arxiv.org/abs/2512.05925
- **作者**: Federico Bianchi, Yongchan Kwon
- **年份**: 2025
- **摘要**: 使用 GPT-5 检查器识别已发表 AI 论文中的客观错误。NeurIPS 论文平均错误数从 2021 的 3.8 升至 2025 的 5.9，对 LLM 辅助科研的可复现性与质量保障提出警示。
- **与本单元的关联**: 直接对应 Belmont 善行原则（maximize benefits, minimize harms）--错误率上升意味着"最小化伤害"不再仅是研究设计问题，而是研究产出质量保障问题，伦理审查须引入错误审计。

### 2. ROBoto2: An Interactive System and Dataset for LLM-assisted Clinical Trial Risk of Bias Assessment
- **arXiv**: https://arxiv.org/abs/2511.03048
- **作者**: Anthony Hevia, Sanjana Chintalapati
- **年份**: 2025
- **摘要**: 开源平台用于 LLM 辅助临床试验偏倚风险评估，包含 521 篇儿科临床试验报告数据集（8954 个信号问题与 1202 条证据段落）。为 LLM 辅助综述的质量评估阶段提供可复现的工具与基准数据。
- **与本单元的关联**: 直接对应 Belmont 公平正义原则--RoB 评估是公平分配研究风险与收益的前置条件，ROBoto2 把这一定量操作化，是 NIST AI RMF Measure 步骤的 LLM 工具化实现。

### 3. Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs
- **arXiv**: https://arxiv.org/abs/2604.27006
- **作者**: Gilberto Sussumu Hida, Danilo Monteiro Ribeiro
- **年份**: 2026
- **摘要**: 评估 12 个 LLM 与 4 个经典模型在 SLR 证据筛选中的表现与变异性。发现 LLM 即使在温度为零时仍表现出显著异质性与残余非确定性。
- **与本单元的关联**: 直接挑战 Belmont 尊重个人原则--如果 LLM 介入的研究证据筛选非确定，基于该筛选的研究决策可能损害参与者自主权，伦理审查须引入"LLM 调用确定性等级"。

### 4. LLM-Assisted Empirical Software Engineering: Systematic Literature Review and Research Agenda
- **arXiv**: https://arxiv.org/abs/2604.26192
- **作者**: Victoria Gomes, Delaney Selb
- **年份**: 2026
- **摘要**: 对 50 篇 LLM 在实证软件工程中使用的主要研究进行系统综述。发现 LLM 使用正在增长但仍以自动化为导向，在以人为中心的整合与透明度方面存在缺口，提出研究议程。
- **与本单元的关联**: 对应 NIST AI RMF Govern 步骤--50 篇研究的透明度缺口意味着 LLM 介入研究的治理框架尚未建立，伦理委员会须强制报告 LLM 使用详情。

---

## critical_synthesis

这 4 篇论文共同揭示了 2025-2026 年 LLM 辅助科研的可复现性危机如何从技术问题升级为研究伦理问题。**共识**正在形成：LLM 介入研究必须透明报告（LLM-Assisted Empirical SE SLR 揭示 50 篇研究的透明度缺口），且 LLM 的残余非确定性（Beyond Accuracy 证明温度=0 仍非确定）构成新的伦理风险来源。**争议**在于伦理审查的强度：To Err Is Human 量化错误率 3.8->5.9 上升暗示当前伦理审查不足以保障研究产出质量，但是否应把"LLM 错误检查器自检"作为强制伦理审查项仍存分歧--LLM 检查 LLM 的自我偏好偏差可能引入新的伦理风险。**趋势**是 Belmont 三原则在 LLM 时代的操作化升级：善行原则从"风险-收益评估"升级为"风险-收益-错误率三轴评估"，公平正义原则从"负担收益公平分配"升级为"LLM 偏倚评估 + RoB 工具化"（ROBoto2），尊重个人原则从"知情同意"升级为"知情同意 + LLM 调用确定性等级披露"。**局限**关键：To Err Is Human 使用 GPT-5 作为错误检查器，存在 LLM-as-judge 自我偏好偏差--AI 检查 AI 论文错误可能系统性低估 LLM 习惯性错误，且"3.8->5.9"上升趋势可能反映 GPT-5 检查能力变化而非论文错误率真实上升；ROBoto2 仅在儿科临床试验验证，521 篇数据集可能携带"儿科试验特殊性"，跨域泛化未测；Beyond Accuracy 的"12 个 LLM + 4 个经典模型"样本不足以泛化。整体判断：前沿证据要求把可复现性危机显式纳入 Belmont 善行原则的履行，本单元所教的"风险-收益评估"须升级为"风险-收益-错误率-非确定性四轴评估"。

---

## delta_to_unit

1. **本单元 notes.md 关键回顾 1"Belmont Report 三原则（尊重个人/善行/公平正义）"，To Err Is Human（2512.05925）量化错误率 3.8->5.9 上升要求善行原则的操作化升级**--本单元教的"最大化收益、最小化伤害"是定性叙述，前沿证据要求新增"错误率审计"作为定量维度。建议在 solution.ipynb 的 Belmont 评分器中新增"error_audit_evidence"字段，更新 IRB 伦理审查清单 schema。

2. **本单元 notes.md TODO4"NIST AI RMF 研究伦理映射 + EU AI Act 研究合规判定"，LLM-Assisted Empirical SE SLR（2604.26192）揭示的 50 篇研究透明度缺口要求 NIST AI RMF Govern 步骤的具体化**--本单元教的"IRB 审批、伦理委员会监督、研究者问责"是抽象描述，前沿证据要求新增"LLM 使用详情强制报告"作为 Govern 步骤的具体操作化项（模型版本/提示词/温度/调用次数/变异性）。

3. **本单元 notes.md 关键回顾 4"算法偏见评估（Barocas & Selbst 2016）+ Model Cards + Fairlearn + AIF360"，ROBoto2（2511.03048）的 521 篇儿科临床试验 RoB 数据集是公平正义原则的新操作化工具**--本单元教的偏见评估工具（Fairlearn/AIF360）聚焦算法输出公平性，ROBoto2 把 RoB 评估前置为公平分配研究风险与收益的条件。建议在 NIST AI RMF Measure 步骤中新增"LLM-assisted RoB"路径。

4. **本单元 notes.md TODO6"AI 红队测试伦理验证（garak/PyRIT 概念）+ 天道推演预判伦理风险路径"，Beyond Accuracy（2604.27006）证明温度=0 时 LLM 仍有残余非确定性要求红队测试的伦理角色扩展**--本单元教的红队测试聚焦"发现系统漏洞"，前沿证据要求红队测试扩展为"发现 LLM 调用非确定性 + 错误率审计"双重验证，更新 Belmont 善行原则的履行手段。

---

## open_questions

1. 当 To Err Is Human 显示 AI 论文错误率逐年上升，研究伦理是否应把"LLM 错误检查器自检报告"作为 IRB 审批的强制材料，还是这会引入新的 LLM-as-judge 自我偏好伦理风险？
2. ROBoto2 的 LLM 辅助 RoB 评估在儿科临床试验场景验证，其 521 篇基准数据集是否存在"儿科试验特殊性"，导致在其他临床或非临床领域的 RoB 评估泛化失败，从而违反 Belmont 公平正义原则的普适性要求？
3. Beyond Accuracy 证明 LLM 在温度=0 仍非确定，这是否意味着 Belmont 尊重个人原则的"知情同意"须升级为"知情同意 + LLM 调用确定性等级披露"--即参与者有权知道研究决策基于非确定性 LLM 调用？
4. LLM-Assisted Empirical SE SLR 揭示的 50 篇研究透明度缺口是否构成 Belmont 善行原则的系统性违反--即不透明报告 LLM 使用是否本身就是"伤害"？

---

## methodological_critique

这 4 篇论文在研究伦理视角下可信度顾虑显著。To Err Is Human（2512.05925，unverified）是本单元关键引用，但使用 GPT-5 作为错误检查器存在严重的 LLM-as-judge 自我偏好风险--AI 检查 AI 论文错误可能系统性低估 LLM 习惯性错误，且"3.8->5.9"上升趋势可能反映 GPT-5 检查能力的变化而非论文错误率的真实上升，作者未报告检查器自身的 test-retest reliability，其"错误计数"的可复现性存疑。ROBoto2（2511.03048，unverified）的 521 篇儿科临床试验数据集可能携带"儿科试验特殊性"（如儿科知情同意的特殊程序），导致跨域泛化未测，且 8954 个信号问题的标注一致性（人工标注 kappa）未报告，标注质量本身可能成为新的偏倚来源。LLM-Assisted Empirical SE SLR（2604.26192，unverified）的"50 篇研究透明度缺口"声明依赖作者对"透明度"的操作化定义，该定义可能偏向软件工程领域的特定关注点，跨域泛化未测，且 50 篇样本规模不足以泛化到所有 LLM 辅助研究。Beyond Accuracy（2604.27006，unverified）的"12 个 LLM + 4 个经典模型"样本不足以泛化，且未区分残余非确定性的来源（数值精度、采样机制、框架实现、缓存命中）。整体而言，这批论文都未充分讨论"LLM 检查 LLM"或"LLM 评估 LLM"的自我偏好伦理风险，博后引用时必须交叉验证并标注验证缺口。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
