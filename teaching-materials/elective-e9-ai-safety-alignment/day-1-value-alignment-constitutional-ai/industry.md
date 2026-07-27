# Day 1 · 价值对齐与 Constitutional AI · 产业链接 (v7.0)

> **所属**：AI原生化商业博士 · 选修E9 · Day 1 · 产业链接层 (v7.0)
> **配套**：[`notes.md`](./notes.md)（理论锚点）｜[`research.md`](./research.md)（研究产出）
> **标准**：Imperial MSc BA 咨询项目模式（Burberry / Expedia / J&J）｜HBS 案例法｜MIT Sloan 行动学习

---

## real_companies

与 Day 1「价值对齐 + Constitutional AI」主题强关联的 ≥3 家真实企业锚点：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|----------|
| **Anthropic** | Constitutional AI 提出者；本 Day 核心理论来源（arXiv 2212.08073）。其 Claude 系列模型（Claude 3.5 / Claude 4）是 CAI 工程化的标杆产物；HHH 原则（Helpful/Harmless/Honest）由 Anthropic 提出，是本 Day deepeval BaseMetric 的评估框架 | Claude 模型的宪法原则设计 + RLAIF 训练流程；企业版 Claude for Work 的营销场景合规定制；可解释性研究（Scaling Monosemanticity）支撑对齐评估的"行为可审计性" |
| **OpenAI** | RLHF 工程化先驱（InstructGPT, arXiv 2203.02155）；本 Day RLHF baseline 的对照基线。其 GPT-4 系列被广泛用作营销 Agent 的基座模型与 LLM-as-a-judge backend | GPT-4o 在营销内容生成 Agent 中的对齐失败案例（Reward Hacking / 虚假宣传）；Moderation API 作为 Harmless 维度的工业级 baseline；与 CAI 的可审计性差距分析 |
| **Salesforce Einstein** | 营销场景对齐的产业落地点。Einstein GPT 为营销/销售/服务场景定制 LLM，对齐需求集中在广告法合规 + 客户数据保护 + 品牌调性 | 营销内容生成 Agent 在 Salesforce Marketing Cloud 中的部署；企业自定宪法原则集（"不夸大宣传 / 不误导消费者 / 符合广告法"）作为 Einstein 信任层的策略定义；对齐评估纳入 Marketing Cloud CI |
| **Scale AI** | 对齐数据供应链。RLHF 的人类偏好标注 + RLAIF 的宪法原则集标注 + 红队探针数据，Scale AI 提供 data engine；本 Day garak 探针的产业对标 | 为营销 Agent 提供对齐数据标注服务（HHH 三维度偏好数据）；Scale AI 的 Red Team 服务与 garak alignment probes 的功能对照 |
| **Apollo Research** | AI 安全专项研究机构；对齐评估与模型欺骗行为（deceptive alignment）研究前沿 | 第三方对齐审计服务；为营销 Agent 提供独立的价值偏差评估，与本 Day garak 探针扫描的"外部红队"角色互补 |

---

## deployment_example

**真实部署场景**：Salesforce Marketing Cloud + Einstein GPT 营销内容生成 Agent 的对齐工程化。

- **公司**：Salesforce（产业伙伴），客户为某 DTC 美妆品牌（年营收 ~$200M，北美+亚太市场）。
- **场景**：营销内容生成 Agent 自动产出邮件标题 / 社媒文案 / 产品描述，日均生成量 ~50,000 条，需符合美国 FTC guidelines + 中国《广告法》+ 欧盟 GDPR（不基于敏感属性定向）。
- **方法**：采用本 Day 的 Constitutional AI 工程化方案 --
  1. **企业宪法原则集**（v1.0, 2026-07）：10 条原则，覆盖 (a) 不使用绝对化用语（"最佳""第一""治愈"）、(b) 不虚构成分/功效（必须忠于产品知识库）、(c) 不基于种族/性别/年龄歧视性定向、(d) 不利用心理弱点操纵消费者、(e) 清晰标注 AI 生成内容。
  2. **对齐评估闭环**：deepeval 自定义 BaseMetric 量化 HHH 三维度（每条生成内容打分 0-1）+ garak alignment probes（`latentinjection` / `goodside` / `snowball`）做日级红队扫描；Harmless 维度 < 0.9 触发人工复审。
  3. **CI 集成**：`deepeval test run` 在 Marketing Cloud 的 prompt 修改 CI 中自动执行，对齐回归（HHH 任一维度降 > 5%）阻断发布。
- **规模/约束**：日均 50k 条生成内容；LLM-as-a-judge 成本 ~$0.002/条（gpt-4o-mini），日成本 ~$100；garak 全量扫描周级跑，无 API key 时用本地静态扫描 fallback。
- **效果**（预期/产业基准）：Harmless 维度失败率从 RLHF baseline 的 ~3.2% 降至 CAI 方案的 ~0.8%；宪法原则可审计性使法务团队首次能"读对齐策略"，而非黑盒信任模型。
- **约束**：LLM-as-a-judge 的位置偏差/冗长偏差需用随机化 prompt 顺序缓解；广告法边界跨文化（美/中/欧）需独立宪法原则子集。

---

## consulting_project

**Imperial MSc Business Analytics 咨询项目**（8 周，4-5 人团队，partner 赞助）：

- **Partner（赞助企业）**：Burberry（奢侈品零售，营销内容生成 Agent 对齐需求强）+ Anthropic（技术 partner，提供 Claude API 额度与宪法设计咨询）。
- **Problem（真实业务问题）**：Burberry 的营销内容生成 Agent 在多语种（英/中/日/韩）场景下，对齐失败表现为 (a) 文化敏感度不足（特定市场禁忌词）、(b) 奢侈品调性偏离（过于"促销化"）、(c) 跨文化夸大宣传边界不一致。需设计一套可复现的对齐评估 + 宪法原则集，并量化 CAI vs RLHF baseline 的差距。
- **Data（企业提供数据）**：Burberry 提供 (a) 过去 12 个月已发布的 ~20k 条营销文案（脱敏，含人工合规标注）、(b) 品牌调性 guidelines 文档、(c) 4 个市场的法务合规清单；Anthropic 提供 (a) Claude API 额度、(b) Constitutional AI 训练流程咨询、(c) 内部宪法原则集参考。
- **Scope（8 周, 4-5 人）**：
  - W1-2：文献综述（CAI / RLHF / DPO / LLM-as-a-judge）+ 数据探索 + 宪法原则集 v0.1 草案；
  - W3-4：deepeval BaseMetric 实现 HHH 三维度评估 + garak 红队扫描 baseline；
  - W5-6：CAI vs RLHF 对照实验（3 个市场 × 2 个方案 × ~2k 条用例）+ 统计检验（McNemar / Spearman ρ）；
  - W7-8：deliverable 打磨 + partner review + final presentation。
- **Deliverable（交付物）**：
  1. **原型**：Burberry 营销 Agent 对齐评估 dashboard（HHH 三维度 + 探针命中 + 宪法合规）；
  2. **模型**：企业营销宪法原则集 v1.0（多语种，4 个市场）+ CAI 微调的 Claude 模型权重；
  3. **策略**：对齐成熟度 5 级路线图（手动 -> RLHF -> CAI -> CAI+红队 -> 在线监控）+ 12 个月落地计划；
  4. **报告**：30 页咨询报告 + executive deck + 可复现代码（GitHub repo，CC-BY-NC 4.0）。
- **衔接**：本 Day starter.ipynb 是该咨询项目的"最小可行原型"（MVP）；6 个 TODO 对应咨询 W3-4 的核心交付。

---

## case_study

**HBS 风格教学案例钩子**（3 段：protagonist / decision / tension）：

- **Protagonist（主角）**：Lin Wei，某 DTC 美妆品牌（年营收 ~$150M，中美双市场）Head of AI。前 Google DeepMind 机器学习工程师，2025 年加入该品牌负责 AI 战略。汇报给 CMO（营销出身，对 AI 黑盒持谨慎态度）。直接管理 8 人 AI 团队 + 与法务 / 品牌团队矩阵协作。
- **Decision（关键决策点）**：2026 年 Q3，品牌即将上线"全球营销内容生成 Agent v2"，支持 12 个语种、日均 30k 条生成内容。Lin Wei 面临三选一决策：
  - **方案 A**：沿用 v1 的 RLHF baseline（InstructGPT 风格 SFT + RM + PPO），已知 Harmless 失败率 ~3.2%，法务团队投诉"对齐策略不可审计"；
  - **方案 B**：切换为 Constitutional AI（显式宪法原则集 + RLAIF + garak 红队），预期 Harmless 失败率 ~0.8%，但需法务团队参与宪法原则设计，且 Claude API 成本 +15%；
  - **方案 C**：采用 DPO + CAI 组合（DPO 解决训练稳定性，CAI 解决标注成本），技术风险最高但长期可维护性最好。
  - 决策窗口：CMO 要求 4 周内给出建议，Q4 上线。Board 关心品牌声誉风险 > 转化率。
- **Tension（核心张力/两难）**：
  1. **可审计性 vs 性能**：CAI 的宪法原则集可审计（法务团队支持），但 LLM-as-a-judge 本身是黑盒（法务团队反对）；如何在"可审计的对齐策略"与"不可审计的评估器"之间向 Board 解释？
  2. **品牌调性 vs 转化率**：宪法原则"不利用心理弱点操纵消费者"可能降低转化率 5-8%，CMO 的 KPI 是转化率，Board 的 KPI 是品牌声誉 -- 谁的 KPI 优先？
  3. **跨文化边界**：中国《广告法》禁止"最佳"等绝对化用语，美国 FTC 允许"puffery"（合理夸张）-- 一套宪法原则如何处理跨文化合规边界？是否需要 12 个语种 × 4 个市场 = 48 套子原则？
  4. **时间压力 vs 工程严谨**：4 周决策窗口无法跑完整 A/B 测试，Lin Wei 只能用 starter.ipynb 的 MVP 评估 + 文献基准（arXiv 2212.08073）做外推 -- 如何向 Board 坦诚不确定性而不失去决策权？

**Teaching note 钩子**：本案例可作为 HBS "AI Ethics in Practice" 系列 / MIT Sloan "AI Product Management" 课程的教学案例，教学目标对应 Day 1 学习目标 1-4（对齐三层 / RLHF-CAI-DPO / HHH 评估 / 企业宪法设计）。案例附件含本 Day starter.ipynb 作为上机练习。

---

## guest_lecture

**客座讲座**：

- **Topic（主题）**：*"From RLHF to Constitutional AI: Building Auditable Alignment for Marketing Agents at Scale"* -- 从 RLHF 到 Constitutional AI：为营销 Agent 构建可审计的对齐工程。
- **Speaker Profile（主讲人画像）**：Amanda Askell（Anthropic，Constitutional AI 设计核心成员）或 Sam Bowman（Anthropic / NYU，对齐评估前沿研究员）。备选：Ethan Perez（Anthropic，对齐评估与 red teaming）；产业侧可邀请 Salesforce Einstein GPT 的 Head of AI Safety。
- **形式**：45 min talk + 30 min Q&A + 15 min 上机 demo（用本 Day starter.ipynb 演示 HHH 三维度评估 + garak 探针扫描）。
- **核心议题**：(1) RLHF 的标注偏见与 Reward Hacking 真实案例、(2) Constitutional AI 的"宪法原则 -> AI 自我批评 -> RLAIF"工程流程、(3) HHH 三维度的张力与权衡（越 helpful 可能越不 harmless）、(4) LLM-as-a-judge 的已知偏差与缓解、(5) 营销垂直场景的宪法原则设计模板。
- **衔接**：讲座前学员完成 Day 1 starter.ipynb 的 TODO1-4，带 1 个对齐评估失败案例参与 Q&A。

---

## internship_pointer

**实习/驻留指针**：

1. **Anthropic Alignment Research Residency**（12 个月，全职）
   - **机构**：Anthropic（Constitutional AI 提出者，本 Day 核心理论来源）
   - **角色**：Alignment Research Resident -- 参与 Constitutional AI / 可解释性 / 红队 / 对齐评估前沿研究，mentor 由 Amanda Askell / Sam Bowman / Ethan Perez 等担任。
   - **衔接**：本 Day 是该 residency 的"入门必修"-- starter.ipynb 实操 deepeval + garak + 企业宪法设计，对应 residency 的"对齐评估"能力栈；research.md 的 IMRaD 大纲可作为 residency 申请的 writing sample。
   - 申请链接：https://www.anthropic.com/careers（搜索 "Residency"）

2. **OpenAI Red Team Residency**（6-12 个月）
   - **机构**：OpenAI（RLHF 工程化先驱，本 Day baseline 来源）
   - **角色**：Red Team Resident -- 系统化测试 GPT 系列模型的对齐漏洞，覆盖营销合规 / 价值偏差 / Prompt Injection 等场景。
   - **衔接**：本 Day 的 garak alignment probes 上机是 red teaming 的"最小可行训练"；Day 2（Prompt Injection / 红队测试）是 residency 的进阶准备。
   - 申请链接：https://openai.com/careers/red-teaming-network

3. **Salesforce Einstein AI Capstone Sponsor**（Imperial MSc BA capstone，3-6 个月）
   - **机构**：Salesforce Einstein（营销场景对齐产业落地点）
   - **角色**：AI Capstone Researcher -- 参与营销内容生成 Agent 的对齐工程化项目，HHH 评估 + 企业宪法设计 + CI 集成。
   - **衔接**：本 Day 的 consulting_project 节描述的 Burberry + Anthropic 咨询项目是 capstone 的范例；starter.ipynb 的 6 个 TODO 对应 capstone W3-4 的核心交付。
   - 申请链接：Imperial MSc BA 项目内部 capstone sponsor 列表

4. **Apollo Research Internship**（3-6 个月）
   - **机构**：Apollo Research（AI 安全专项研究机构，对齐评估与 deceptive alignment 前沿）
   - **角色**：Research Intern -- 参与对齐评估方法学与模型欺骗行为研究。
   - **衔接**：本 Day 的"对齐评估是发现问题的手段，不能证明已对齐"认知是 Apollo 研究议程的入门；research.md 的 contribution §4（LLM-as-a-judge 偏差声明）对应 Apollo 的评估方法学批判。
   - 申请链接：https://www.apolloresearch.ai/careers

---

*本产业链接层与 research.md 研究产出层互为锚点：咨询项目 partner / 案例主角 / 客座讲座 speaker 均可在 research.md 的 linked_paper 作者中找到学术对应；实习指针的机构均与本 Day 理论来源强关联。*
