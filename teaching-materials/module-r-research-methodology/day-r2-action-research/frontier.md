# frontier.md (v9.0 学术前沿注入层)

> **所属**：module-r-research-methodology · day-r2-action-research
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 LLM 辅助系统综述中的"人在回路 + 迭代纠错"工作流如何映射到行动研究的 Plan-Act-Observe-Reflect 螺旋，以及 LLM 残余非确定性对 AR trustworthiness 四准则的挑战？

---

## frontier_topic

本单元教 Lewin/Kemmis 四阶段螺旋、PAR 利益相关方共创、Lincoln & Guba trustworthiness 四准则（可信性/可迁移性/可靠性/可确认性）+ 贝叶斯干预更新。前沿子问题是：2025-2026 年 LLM 辅助系统综述工具引入的"异构人设 LLM 代理 + 人在回路迭代纠错"工作流，本质是一种计算化的 AR 螺旋，但它对 AR 的 trustworthiness 准则构成何种新挑战--特别是当 LLM 即使在温度为零时仍表现出残余非确定性时？

---

## recent_papers

### 1. Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop
- **arXiv**: https://arxiv.org/abs/2607.21920
- **作者**: Zexin Ren, Zixuan Zhao
- **年份**: 2026
- **摘要**: 提出两个带人在回路的 multi-agentic 系统用于临床试验系统文献综述，含异构人设 LLM 代理进行筛选与迭代纠错提取。系统恢复了原始研究所有试验并发现人工评审遗漏的额外合格试验。
- **与本单元的关联**: 异构人设代理 + 人在回路迭代纠错 = 计算化 PAR（利益相关方以 agent 人设形式参与共创），迭代纠错直接映射 AR 的 Plan-Act-Observe-Reflect 螺旋。

### 2. L-PRISMA: An Extension of PRISMA in the Era of Generative Artificial Intelligence (GenAI)
- **arXiv**: https://arxiv.org/abs/2603.19236
- **作者**: Samar Shailendra, Rajan Kadel
- **年份**: 2026
- **摘要**: 提出在 PRISMA 框架中整合人工主导综合与 GenAI 辅助统计预筛选，应对 LLM 非确定性带来的可复现性、透明度与可审计性挑战。统计层的确定性增强了可复现性。
- **与本单元的关联**: "人工主导综合 + GenAI 辅助预筛选"对应 AR 的"研究者主导干预 + 工具辅助观察"--明确分工是 AR trustworthiness 可靠性（audit trail）的新操作化方式。

### 3. Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs
- **arXiv**: https://arxiv.org/abs/2604.27006
- **作者**: Gilberto Sussumu Hida, Danilo Monteiro Ribeiro
- **年份**: 2026
- **摘要**: 评估 12 个 LLM 与 4 个经典模型在 SLR 证据筛选中的表现与变异性。发现 LLM 即使在温度为零时仍表现出显著异质性与残余非确定性，对 LLM 辅助综述的可复现性提出根本性挑战。
- **与本单元的关联**: 直接挑战 AR trustworthiness 的"可靠性（dependability）"准则--即使干预方案固定（温度=0），观察数据仍非确定，audit trail 无法完全复现。

### 4. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis
- **arXiv**: https://arxiv.org/abs/2512.05925
- **作者**: Federico Bianchi, Yongchan Kwon
- **年份**: 2025
- **摘要**: 使用 GPT-5 检查器识别已发表 AI 论文中的客观错误。NeurIPS 论文平均错误数从 2021 的 3.8 升至 2025 的 5.9，对 LLM 辅助科研的可复现性与质量保障提出警示。
- **与本单元的关联**: 对应 AR 的"反思性（reflexivity）"准则--研究者须主动量化自身产出的错误率，而非依赖"我感觉没错"的内省。

---

## critical_synthesis

这 4 篇论文共同揭示了 2025-2026 年 LLM 辅助综述工作流与行动研究认识论的一个深层共振与张力。**共识**正在形成：纯 LLM 自动化综述不可接受，人在回路（HITL）是必需--L-PRISMA 的"人工主导综合 + GenAI 辅助预筛选"分工、Multi-Agentic SLR 的"异构人设代理 + 人在回路迭代纠错"都印证了 AR 的"研究者作为变革推动者"原则不能被 LLM 取代。**争议**在于 HITL 的强度与位置：L-PRISMA 把人工放在综合层（高干预），Multi-Agentic SLR 把人工放在纠错回路（中干预），两者代表了 PAR"共创深度"光谱的不同位置。**趋势**是 LLM 代理承担"推演"角色（异构人设 = 多利益相关方视角模拟），人工承担"裁决"角色--这恰好映射 AR 的 Plan（推演）-Act（实施）-Observe（收集）-Reflect（裁决）循环。**局限**尖锐：Beyond Accuracy（2604.27006）证明 LLM 即使温度为零仍有残余非确定性，这直接动摇 AR trustworthiness 的"可靠性（dependability/audit trail）"准则--如果同一干预在同一状态下产生不同观察，audit trail 无法复现，AR 的可确认性（confirmability）也受波及。To Err Is Human 进一步量化了"AI 论文错误率 3.8→5.9"的上升趋势，意味着用 LLM 辅助 AR 循环时，反思性（reflexivity）必须从"定性内省"升级为"定量错误审计"。整体判断：前沿工作流强化了 AR 的"双重目标"合法性，但要求 trustworthiness 操作化方式升级，本单元所教的三角验证 + 成员校验 + 反思性评分需引入 LLM 非确定性度量。

---

## delta_to_unit

1. **本单元 notes.md TODO3"AR 效度评估--三角验证（数据源数量）+ 成员校验率 + 反思性评分"，Beyond Accuracy（2604.27006）证明温度=0 时 LLM 仍有残余非确定性**--这意味着本单元教的"audit trail 完整度"作为 dependability 量化指标已不够，需新增"LLM 调用变异性指标"（如同提示多次运行的结果方差），更新 solution.ipynb 中效度评估 DataFrame 的列结构。

2. **本单元 notes.md TODO4"PAR 利益相关方分析--权力-利益矩阵 + 共创度演化"，Multi-Agentic SLR（2607.21920）的"异构人设 LLM 代理"实质上把利益相关方以 agent 人设形式参与共创**--这扩展了本单元 PAR 的"共创"定义：共创不再仅限于人类利益相关方，LLM 代理作为"模拟利益相关方"也可参与共创。建议在权力-利益矩阵中新增一列"agent_proxy_eligible"。

3. **本单元 notes.md TODO7"贝叶斯干预有效性更新--用观察数据更新干预有效后验概率"，L-PRISMA（2603.19236）的"统计层确定性 + GenAI 辅助预筛选"分工提供了一个混合架构范例**--确定性统计层提供可复现的似然函数，GenAI 层提供先验信息。这更新了本单元贝叶斯更新 TODO：先验不应仅来自"理论框架或经验"，还可来自 LLM 辅助预筛选的结构化判断。

4. **本单元 notes.md 关键回顾 5"AR vs DSR vs 案例研究"对比表把 AR 的效度标准定为 trustworthiness，To Err Is Human（2512.05925）量化错误率 3.8→5.9 上升**--这要求本单元在"反思性（reflexivity）"准则的操作化中引入"LLM 错误审计"作为新维度，而非仅靠"反思日记"定性记录。本单元 solution.ipynb 中 reflexivity 评分应增加"error_audit_evidence"字段。

---

## open_questions

1. 当 LLM 代理以异构人设参与 PAR 共创时，"成员校验（member checking）"是否仍能成立--LLM 代理的"人设反馈"是否能替代真实利益相关方的校验，还是会引入"模拟校验偏差"？
2. Beyond Accuracy 证明温度=0 时 LLM 仍有残余非确定性，这是否意味着 AR 的 audit trail 准则需要引入"LLM 调用确定性等级"作为新的可信度维度，而非仅记录干预描述与数据收集？
3. L-PRISMA 的"人工主导综合 + GenAI 辅助预筛选"分工在 AR 多轮螺旋中是否稳定--当 GenAI 预筛选在第 N 轮引入系统性偏差时，人工主导综合层能否检测并修正？
4. To Err Is Human 显示 AI 论文错误率逐年上升，AR 研究者用 LLM 辅助反思时，是否需要预注册一个"LLM 辅助反思错误率上限"作为可确认性（confirmability）的门槛？

---

## methodological_critique

这 4 篇论文在 AR 方法论视角下各有可信度顾虑。Multi-Agentic SLR（2607.21920）虽经验证（2 篇 verified 之一），但其"发现人工评审遗漏的额外合格试验"是单一场景声明，未报告遗漏试验对原荟萃分析结论的方向性影响，且异构人设代理的"人设设计偏差"未讨论--人设选择本身可能引入研究者偏见。L-PRISMA（2603.19236，verified）的"统计层确定性增强可复现性"是强声明，但作者未报告统计层与 GenAI 层接口处的错误传播，确定性层可能被上游 GenAI 偏差污染。Beyond Accuracy（2604.27006，unverified）的"温度=0 仍有残余非确定性"是核心发现，但作者仅测试 12 个 LLM 与 4 个经典模型，样本规模不足以泛化到所有 LLM 架构，且未区分非确定性的来源（数值精度 vs 采样机制 vs 框架实现）。To Err Is Human（2512.05925，unverified）使用 GPT-5 作为检查器，存在严重的 LLM-as-judge 自我偏好风险--AI 检查 AI 论文错误可能系统性低估 LLM 习惯性错误，且"错误计数"的 test-retest reliability 未报告。整体而言，这批论文在 AR 多轮螺旋的"反思性"层面都缺乏对自身方法局限的充分讨论，博后引用时必须交叉验证。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
