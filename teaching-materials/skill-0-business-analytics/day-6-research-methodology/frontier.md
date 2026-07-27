# frontier.md

> **所属**：skill-0-business-analytics · day-6-research-methodology
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 AI coding agent 在 many-analysts 基线上的方法论多样性与裁决脆弱性、AI scientist 的证据天花板消融、多 agent 视角辩论的定性分析如何更新本单元"可复现研究+文献综述+研究范式"的教学。

---

## frontier_topic

本单元教 arxiv API 查询真实论文元数据、pandas 文献计量(年份趋势/高产作者)、networkx 作者合作网络(度中心性/社区检测)、OSF 预注册、FAIR 原则、ASReview AI 辅助文献综述、IMRaD 格式、可复现研究三大支柱。前沿子问题是: 当 AI coding agent 在 many-analysts 基线上匹配人类方法论多样性但裁决层可被提示翻转、AI scientist 的证据质量设定决策天花板(0.96 vs 0.25-0.38)、多 agent 视角辩论逼近人类定性编码时, 本单元"文献综述+预注册+IMRaD"的研究方法论教学如何被更新。

---

## recent_papers

### 1. AI Scientists Are Only as Good as Their Evidence: A Stratified Ablation of Proprietary Data and Reasoning Skills in Drug-Asset Valuation
- **arXiv**: https://arxiv.org/abs/2606.09556
- **作者**: Yinan Wang
- **年份**: 2026
- **摘要**: 在生产级药物资产估值 agent 上进行受控三臂消融实验, 表明专有证据设定 AI 决策质量上限. 完整系统 (含专有语料) 恢复 0.96 的 gold competitive records, 而非专有变体仅 0.25-0.38. 推理支架改善校准但无法突破事实天花板.
- **与本单元的关联**: 本单元 notes.md 教可复现研究三大支柱(OSF 预注册/FAIR/环境锁定), 该论文的"证据天花板"消融表明推理支架(预注册/方法论规范)无法弥补证据质量上限--呼应本单元 FAIR 原则中"可复用(Reusable)"的证据质量维度。

### 2. AI Coding Agents in Social Science: Methodologically Diverse, Empirically Consistent, Interpretively Vulnerable
- **arXiv**: https://arxiv.org/abs/2606.11456
- **作者**: Meysam Alizadeh, Fabrizio Gilardi
- **年份**: 2026
- **摘要**: 在移民/社会政策研究的 many-analysts 人类基线上测试 LLM 编码 agent (Claude Code, Codex). 在设计层 agent 匹配或超越人类方法论多样性; 在裁决层, 显式确认性提示将 Claude Code 的裁决从 10% 翻转至 90% 支持, 揭示解释层为 AI 偏见所在.
- **与本单元的关联**: 本单元 TODO1-2 用 arxiv API+pandas 做文献计量, 该论文测试的 Claude Code/Codex 正是自动执行文献编码的 agent, 其"设计层强、裁决层脆弱"的发现直接影响本单元"LLM 辅助文献综述"的可靠性边界。

### 3. Agent-as-Peer-Debriefer: A Multi-Agent Framework with Perspective-Based Refinement for Qualitative Analysis
- **arXiv**: https://arxiv.org/abs/2605.24600
- **作者**: Zhimin Lin, Kun Cheng
- **年份**: 2026
- **摘要**: 多 agent 定性数据分析框架, 引入同行辩论, 三个 Peer-Debriefing Agent 分别采用理论驱动、数据驱动、应用视角. 在三个数据集和三个 LLM 上, 基于视角的精化比单 LLM 基线更贴近人类编码, 各视角产生不同的权衡.
- **与本单元的关联**: 本单元 notes.md 教"实证/解释/实用主义"三研究范式, 该论文的三视角辩论(理论/数据/应用)提供了一个可操作的多 agent 定性分析框架, 更新了本单元"研究范式选择"的教学。

---

## critical_synthesis

这三篇论文共同揭示了一个正在形成的共识: AI agent 在研究方法论中的角色是"设计层协作者"而非"裁决层裁判"--它能匹配人类的方法论多样性(写代码/检索文献/编码), 但在判断结果含义时存在可被提示词系统性翻转的偏见。AI Coding Agents(2606.11456)的"10%->90% 裁决翻转"是最直接的证据, AI Scientists(2606.09556)的"0.96 vs 0.25-0.38 证据天花板"表明推理支架无法弥补数据质量上限, Agent-as-Peer-Debriefer(2605.24600)的三视角虽更贴近人类编码但各视角产生不同权衡(无单一正确答案)。然而三者之间存在明显争议: AI Coding Agents 主张 agent 在设计层可靠, 而 Agent-as-Peer-Debriefer 表明即便在设计层(定性编码), 单一 LLM 也不如多视角辩论--设计层的可靠性是否需要多 agent 保障尚无定论。更关键的 limitation: AI Coding Agents 的 many-analysts 基线是社会科学文本编码, 不是本单元的 arxiv 文献计量或 networkx 网络分析, 结论不能直接外推; AI Scientists 的消融仅限药物资产估值, "证据天花板"是否在所有研究领域成立存疑; Agent-as-Peer-Debriefer 的"人类编码"金标准本身有噪声(编码者间 kappa<0.7)。趋势上, 本单元教的 OSF 预注册与 FAIR 原则仍是不可放弃的底线, 但需新增"AI agent 介入层"的治理: 哪些环节可委托 agent, 哪些环节必须人类裁决。

---

## delta_to_unit

1. **文献计量的 agent 可委托性**: 本单元 TODO1-2 用 `arxiv.Search(query="marketing analytics")` 查询真实 arXiv API, 用 pandas 按年份统计论文增长趋势。AI Coding Agents(2606.11456)发现 Claude Code 在设计层(写检索代码)匹配人类多样性, 但在裁决层(判断论文是否支持假设)可被确认性提示翻转(10%->90%)。这意味着本单元的文献计量(检索+统计)可委托 agent, 但"哪些论文真正相关"的判断不可委托--notes.md 教的 arxiv API 检索是可自动化的, 但文献筛选(ASReview 的标注环节)仍需人类把关。

2. **FAIR 原则的证据质量维度**: 本单元 notes.md 教 FAIR 原则(Findable/Accessible/Interoperable/Reusable), 强调可复用性。AI Scientists(2606.09556)的消融(0.96 vs 0.25-0.38)表明证据质量设定决策天花板--这意味着 FAIR 的"Reusable"维度需要新增"证据质量分级"(专有 vs 公开/经验证 vs 未验证), 本单元 notes.md 的 FAIR 四字母框架未覆盖证据质量层级, 这是 v9.0 的关键更新。

3. **三研究范式 vs 三视角辩论**: 本单元 notes.md 教"实证/解释/实用主义"三研究范式(本体论层面)。Agent-as-Peer-Debriefer(2605.24600)的三视角辩论(理论驱动/数据驱动/应用视角)是方法论层面的可操作框架--理论驱动对应解释主义, 数据驱动对应实证主义, 应用视角对应实用主义, 但多 agent 辩论使范式选择从"单选"变为"多视角并行+权衡"。这更新了本单元的教学: 研究范式不必是预先选择的单一立场, 可用多 agent 并行实现三方视角再合成。

---

## open_questions

1. AI Coding Agents 发现确认性提示翻转裁决(10%->90%), 那么本单元教的 arxiv API 文献检索+networkx 共现网络是否能被 LLM agent 的"确认性偏见"系统性污染--若检索查询本身含方向性词汇(如 "LLM marketing success"), 检索结果是否已被偏见锁定?
2. AI Scientists 的证据天花板(0.96 vs 0.25-0.38)是否意味着本单元教的 FAIR 原则(Findable/Accessible)还不够--需要新增"证据质量分级"作为 FAIR+ 的第五维度, 还是将其纳入 Reusable 的子标准?
3. Agent-as-Peer-Debriefer 的三视角辩论(理论/数据/应用)比本单元的"三研究范式"更可操作, 但在营销 AI 文献综述中, 三视角是否覆盖了"因果推断"这一第四范式(干预而非关联)--若不覆盖, 是否需要四 agent 辩论?
4. 本单元教 ASReview 主动学习筛选文献, 但 AI Coding Agents 表明 LLM agent 在裁决层脆弱--ASReview+LLM 的混合管道中, 哪个环节(主动学习采样/LLM 初筛/人类终审)最容易被偏见污染, 如何设计对抗性审计?

---

## methodological_critique

这三篇论文的局限性需审慎对待。AI Scientists(2606.09556)标注 unverified, 其三臂消融仅在药物资产估值这一垂直领域进行, "0.96 vs 0.25-0.38"的差距可能反映该领域专有数据库(如医药审批记录)的特殊性而非普适规律; 且"推理支架无法突破事实天花板"的结论可能低估了推理方法在中等证据质量下的边际价值--在证据质量不是极端(非 0.25 也非 0.96)时, 推理支架可能仍有显著增益, 论文未探索这一区间。AI Coding Agents(2606.11456)同样 unverified, 其 many-analysts 基线是社会政策文本编码而非结构化数据研究, "设计层匹配人类"的结论不能外推到本单元的 arxiv 文献计量; 更严重的是, 10%->90% 的裁决翻转虽揭示了偏见, 但该实验仅用单一主题(移民政策), 未测试营销研究中的效应量方向性偏见, 且"确认性提示"的设计可能有人为夸大偏见效果的 cherry-picking 风险。Agent-as-Peer-Debriefer(2605.24600)的"三视角更贴近人类编码"基于三个数据集, 但"人类编码"本身是否金标准存疑--定性研究中人类编码者间信度(kappa)常低于 0.7, 以有噪声的人类编码为 ground truth 可能误导; 且三视角(理论/数据/应用)的完备性未论证, 是否存在第四视角(如批判性/伦理)未讨论。三者均存在 domain-specific benchmark-gaming 风险: 在自选领域展示 agent 优势, 未在统一的研究方法论基准上验证。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
