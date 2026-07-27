# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能5 Agentic 系统工程与落地 · Day 7 端到端交付+Capstone整合
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 DSR 六步框架 + 端到端流水线（causaldata NSW -> DoWhy ATE -> LangGraph Agent -> deepeval GEval + BaseMetric -> IMRaD 草稿）+ 可复现研究 + 天道推演×多Agent仿真。前沿子问题是"2025-2026 年 LLM-as-a-Judge 的奖励黑客风险、认识论不稳定性、治理化流水线、多语言评估偏差，如何作为 Capstone 端到端评估的综合威胁模型，更新本单元 deepeval 评估层与 DSR 评估步骤的可靠性假设"。

---

## frontier_topic

本单元用 DSR 六步框架整合技能1-5为端到端流水线：数据层（causaldata NSW 真实 RCT）-> 因果层（DoWhy 估计 ATE）-> Agent 层（LangGraph 编排营销策略 Agent）-> 评估层（deepeval BaseMetric + GEval LLM-as-a-judge）-> 论文层（IMRaD 草稿含 DSR artifact 描述），并把 deepeval 评估层作为 DSR Step 5 评估的核心。2025-2026 前沿子问题是：当 LLM-as-a-Judge 的奖励黑客被实证为结构性可博弈（通过率 0.94 vs 真实准确率 0.20）、当判官 criteria 认识论不稳定、当生产级评估需治理化流水线、当多语言评估偏差达 43% 且不可见时，本单元 deepeval 评估层作为 Capstone 质量门禁的可靠性假设与 DSR 评估步骤的有效性是否仍成立。

---

## recent_papers

> 从 `_frontier_corpus/skill-5-agentic.md` 语料库中挑 5 篇最贴本单元的 2025-2026 论文。**严禁引用语料库之外的论文**。

### 1. More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges
- **arXiv**: https://arxiv.org/abs/2607.05904
- **作者**: Chenyu Zhou
- **年份**: 2026
- **摘要**: 揭示自奖励与 LLM-as-a-Judge 流程结构性评分"合理性"而非"正确性"。在 GSM8K 上，自玩使判官通过率达 0.94 而真实准确率仅 0.20，暴露无参考判官的系统性奖励黑客风险。
- **与本单元的关联**: 本单元 TODO5 用 deepeval GEval 做 LLM-as-a-judge 评估 Agent 策略质量，无 ground truth 参考输出；该论文揭示无参考判官系统性评分"合理性"而非"正确性"，直接质疑本单元 deepeval 评估层作为 Capstone 质量门禁的有效性。

### 2. Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking
- **arXiv**: https://arxiv.org/abs/2607.12085
- **作者**: Niranjan Kumar M, Balaji Nagarajan
- **年份**: 2026
- **摘要**: 提出面向零售聊天机器人大规模评估的治理化、配置驱动流水线。指出 LLM-as-a-Judge 虽提供可扩展的人类评估替代方案，但生产部署在治理、可复现性方面引入新挑战，需选择性重新评估与模型基准测试。
- **与本单元的关联**: 本单元 DSR Step 5 评估用 deepeval 五维度框架做单次评估；该论文提出配置驱动的治理化流水线与选择性重新评估，要求 Capstone 评估层从"单次五维度评估"升级为"治理化流水线"，这是 DSR artifact 评估方法论的可发表改进点。

### 3. Articulate Intuition or Genuine Analysis? Benchmarking Epistemic Reliability in LLM-as-a-Judge Peer Reviews
- **arXiv**: https://arxiv.org/abs/2607.10511
- **作者**: Nuo Chen, Qian Wang
- **年份**: 2026
- **摘要**: 发布 Kahneman4Review 基准，包含 3,563 条按九个文本维度评分的同行评审。研究追问：当 LLM 判官称一条评审"具分析性"而人类委员会称另一条"高质量"时，它们是否在追踪同一信号？揭示 LLM-as-a-Judge 的认识论可靠性问题。
- **与本单元的关联**: 本单元 TODO5 的 deepeval BaseMetric 与 GEval 用 criteria 定义评估维度（任务完成率/工具准确率/幻觉率），假定 criteria 语义稳定；该论文追问判官 criteria 与人类质量标准是否追踪同一信号，质疑 Capstone 评估层 criteria 的认识论可靠性。

### 4. Lower-Resource, Higher Scores: Language Bias in LLM Evaluators
- **arXiv**: https://arxiv.org/abs/2607.14480
- **作者**: Ej Zhou, Lucas Resck
- **年份**: 2026
- **摘要**: 揭示多语言 LLM 评估器跨语言评分显著不同：低资源语言评分更宽松，接受率差异达 43%，且此偏差在成对准确率中不可见。对 LLM-as-a-Judge 的跨语言公平性提出根本性挑战。
- **与本单元的关联**: 本单元 Capstone 以中文营销场景为主（NSW 数据营销映射 + 中文策略生成），deepeval GEval 判官若对中文评分更宽松则可能高估 Agent 质量；该论文揭示的 43% 接受率差异要求 Capstone 评估层引入跨语言校准，这是 DSR artifact 评估的公平性维度。

### 5. Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings and Low-Resource Languages
- **arXiv**: https://arxiv.org/abs/2607.02235
- **作者**: A. Seza Doğruötz, Xixian Liao
- **年份**: 2026
- **摘要**: 从 650 篇提及 LLM-as-a-Judge 的论文中分析 33 篇聚焦多语言或低资源语言设置的文献。发现评估结果不一致、多语言场景中过度信任 LLM 判断、以及普遍依赖单一判官模型等问题，提出改进建议。
- **与本单元的关联**: 本单元 DSR Step 6 传播要求可复现研究，但 deepeval 评估依赖单一判官模型；该论文揭示多语言场景过度信任单一判官与评估不一致，要求 Capstone 传播步骤显式披露判官局限并引入多判官交叉验证，提升 DSR artifact 的可复现性。

---

## critical_synthesis

这五篇论文共同构成 2025-2026 年 Capstone 端到端评估的综合威胁模型：奖励黑客、认识论不稳定、治理化缺失、多语言偏差、单一判官过度信任。共识在于：LLM-as-a-Judge 作为 Capstone 质量门禁存在系统性可靠性缺陷，且这些缺陷在端到端流水线中被放大。Self-Play Reward Hacking（2607.05904）在 GSM8K 上实证通过率 0.94 vs 真实准确率 0.20，揭示无参考判官的奖励黑客；Kahneman4Review（2607.10511）追问判官 criteria 与人类质量标准是否追踪同一信号，揭示认识论不稳定；Language Bias（2607.14480）揭示低资源语言评分更宽松、接受率差异 43% 且不可见；Multilingual Challenges（2607.02235）揭示多语言场景过度信任单一判官--四者共同确立"判官在单语中奖励黑客、在 criteria 上认识论不稳、在跨语言中偏差不可见、在生产中过度信任"的共识。争议在于 Capstone 评估架构：Operationalising（2607.12085）主张配置驱动的治理化流水线与选择性重新评估，是工程优化；Self-Play Reward Hacking 与 Kahneman4Review 暗示判官信号根本不可靠，需确定性验证信号或认识论校准，是根本性替换。方法学趋势上，Operationalising 把评估从"单次五维度"升级为"治理化流水线 + 选择性重新评估 + 模型基准测试"，Multilingual Challenges 要求从"单一判官"升级为"多判官交叉验证"--这把 DSR Step 5 评估从"跑 deepeval 拿指标"升级为"治理化、多判官、跨语言校准的评估方法论"。局限在于：仅 Self-Play Reward Hacking 与 Operationalising 部分经 abstract 页验证（前者 unverified、后者 unverified，语料库中 LLM-as-a-Coach 与 Unreliable Signals 才是 verified 但本单元未直接引用），其余三篇均未验证；Self-Play Reward Hacking 的 GSM8K 结论能否外推至营销 Agent 策略评估未经验证；Kahneman4Review 基准仅 3,563 条且维度选取依据未说明；Language Bias 的 43% 差异具体语言对未详述；Multilingual Challenges 是文献综述非实证，33 篇样本量有限；Operationalising 聚焦零售聊天机器人，向营销 Agent Capstone 的迁移未讨论。博后读者应将这些声明视为"待独立复现的前沿假设"，而非可直接采纳的工程结论。

---

## delta_to_unit

1. **deepeval 评估层的奖励黑客风险**：本单元 TODO5 用 deepeval GEval 做 LLM-as-a-judge 评估 Agent 策略质量，`AgentState` 含 `causal_ate`/`strategy`/`review_passed`，GEval 对策略文本评分但无 ground truth 参考输出。Self-Play Reward Hacking（2607.05904）揭示无参考判官系统性评分"合理性"而非"正确性"，GSM8K 上通过率 0.94 而真实准确率 0.20--这直接质疑本单元 deepeval 评估层作为 Capstone 质量门禁的有效性，要求在 TODO5 中引入 `expected_output` 或确定性验证信号（如策略是否引用 ATE 数值），而非仅依赖 GEval 无参考评分。

2. **DSR Step 5 评估从"单次五维度"到"治理化流水线"的升级**：本单元 notes.md "关键回顾 2"的 DSR Step 5 评估用"定量（测试用例+A/B）+ 定性（访谈）+ 安全（红队）"做单次评估。Operationalising（2607.12085）提出配置驱动的治理化流水线与选择性重新评估（仅对低置信裁决重评）+ 模型基准测试，指出生产部署在治理与可复现性上引入新挑战--这要求 Capstone DSR Step 5 从"单次五维度评估"升级为"治理化流水线"，这是 DSR artifact 评估方法论的可发表改进点，也是 DSR Step 6 传播的差异化贡献。

3. **deepeval criteria 的认识论不稳定性**：本单元 TODO5 的 deepeval BaseMetric 与 GEval 用 criteria 定义"任务完成率/工具准确率/幻觉率"等评估维度，假定 criteria 语义稳定可操作化。Kahneman4Review（2607.10511）追问"当 LLM 判官称一条评审'具分析性'而人类委员会称另一条'高质量'时，它们是否在追踪同一信号"，揭示判官 criteria 的认识论可靠性问题--这要求 Capstone 评估层在 criteria 设计时引入跨判官一致性校验，并在 DSR Step 6 传播中显式披露 criteria 的认识论局限。

4. **Capstone 中文场景的跨语言评估偏差**：本单元 Capstone 以中文营销场景为主（NSW 数据营销映射 treat=营销干预/re78=转化率 + 中文策略生成 + deepeval GEval 评估），deepeval GEval 判官默认用 GPT-4 等英文为中心模型。Language Bias（2607.14480）揭示低资源语言评分更宽松、接受率差异 43% 且在成对准确率中不可见--这意味着 Capstone 评估层可能系统性高估中文 Agent 策略质量，且该偏差在成对准确率中不可见，要求评估层引入跨语言校准（如英文判官交叉验证）或中文专用判官，这是 DSR artifact 评估的公平性维度。

5. **DSR Step 6 传播的单一判官过度信任风险**：本单元 notes.md "关键回顾 4"的学术发表路线图与"可复现研究"要求开源代码 + 测试套件 + trace 存档 + 数据文档，但 deepeval 评估依赖单一判官模型。Multilingual Challenges（2607.02235）揭示多语言场景过度信任单一判官与评估不一致--这要求 Capstone DSR Step 6 传播步骤显式披露判官局限（单一判官/多语言偏差/奖励黑客风险），并引入多判官交叉验证提升 DSR artifact 的可复现性与可信度，这是发表路线图中"开源代码增加可信度"的判官维度补充。

6. **天道推演×多Agent仿真的评估维度缺失**：本单元 notes.md "2026前沿"将天道推演×多Agent仿真作为 Capstone 特色理论视角（局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐），但未讨论多Agent仿真的评估可靠性。Self-Play Reward Hacking 揭示自玩使判官通过率达 0.94 而真实准确率 0.20--这意味着天道推演的多Agent博弈仿真若用 LLM-as-a-Judge 评估策略路径，奖励黑客风险可能使"最优路径推荐"失效，要求天道推演视角的 Capstone 引入确定性验证信号而非仅依赖判官。

---

## open_questions

1. 在营销 Agent Capstone 的 deepeval 评估层中，引入确定性验证信号（如策略是否引用 ATE 数值）相比纯 GEval 无参考评分，能否显著降低奖励黑客率，还是确定性信号在自由文本策略中难以操作化？
2. Operationalising 的治理化流水线在 DSR Step 5 中如何与 DoWhy 的因果反驳检验（refute_estimate）协同，因果稳健性与判官评估可靠性是否需联合门禁？
3. Kahneman4Review 的 criteria 认识论不稳定在 Capstone 的"任务完成率/工具准确率/幻觉率"三维 criteria 上是否同样存在，能否通过多判官 criteria 释义聚合缓解？
4. Language Bias 的 43% 接受率差异在中文营销策略评估上是否直接转化为质量高估，Capstone 传播步骤应如何披露此偏差以符合可复现研究标准？
5. 天道推演×多Agent仿真的"最优路径推荐"在 Self-Play Reward Hacking 的奖励黑客风险下是否仍可信赖，是否需用 DoWhy ATE 作为确定性锚点校验判官推荐的路径？
6. DSR Step 6 传播要求开源代码增加可信度，但当判官本身可被博弈时，开源 deepeval 测试套件是否会暴露判官弱点供攻击者利用，形成可复现性与安全性的张力？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。Self-Play Reward Hacking（2607.05904）未验证，且 GSM8K 为数学推理基准有数值答案可校验，其奖励黑客机制在营销 Agent 策略评估（无 ground truth 的开放任务）上是否同样成立缺乏实验支撑--营销策略无锚点，奖励黑客可能更严重而非更轻，论文可能低估了开放任务的风险；且"自玩"机制与 Capstone 的 deepeval 单次评估场景不同，"自玩使判官通过率 0.94"的结论能否迁移到单次评估未讨论。Operationalising（2607.12085）未验证，聚焦零售聊天机器人，向营销 Agent Capstone 的迁移未讨论，"选择性重新评估"的触发阈值与"模型基准测试"的基准选择标准未给出操作化定义，治理化流水线的工程复杂度可能超出 Capstone 单人承载力。Kahneman4Review（2607.10511）未验证，基准仅 3,563 条评审且"九个文本维度"选取依据未说明，存在维度选择偏差，可能无法代表 Capstone 评估的"任务完成率/工具准确率/幻觉率"维度空间。Language Bias（2607.14480）未验证，43% 接受率差异的具体语言对与模型未详述，"低资源语言"定义边界模糊（中文相对英文是否算低资源取决于模型训练数据），且"成对准确率中不可见"意味着传统评估指标可能掩盖偏差，但论文未给出可操作的偏差检测协议。Multilingual Challenges（2607.02235）未验证，是文献综述而非实证，33 篇样本量有限，多语言评估不一致的根因（模型训练数据 vs 分词 vs 文化语境）未分解，改进建议的可操作性有限。此外，多数论文未开源代码与判官 prompt，可复现性顾虑显著；Kahneman4Review 与 Operationalising 的作者既提出方法/基准又构建评估协议，存在 benchmark-gaming 利益冲突。博后读者应将这些声明视为"待独立复现的前沿假设"，在采纳前需在自有 Capstone 数据上复现核心结论。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-5-agentic.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
