# industry.md - 产业链接层 (v7.0)

> 单元: skill-4-business-model / day-3-agent-economy-emerging-models
> 主题: Agent经济涌现模型 (mesa ABM / 三层模型 / A2A经济 / 推理成本约束 / 天道推演×多Agent仿真)
> 标准遵循: Imperial MSc BA 咨询项目模式 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习

---

## real_companies

下表从公司库挑选 >=3 家真实企业, 与本单元 Agent 经济主题精准匹配:

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Sierra** (sierra.ai) | Agent-as-Worker 层次典型案例, outcome-based pricing 标杆 | AI 客服 Agent 按解决率收费 (非 seat/token), 对应 notes.md 三层模型表中"Sierra"案例; 是本单元从 Tool->Worker 跨越挑战 (信任+度量) 的产业锚点 |
| **Cognition / Devin** | Agent-as-Worker 层次在软件工程领域的标杆 | Devin 是自主软件工程师 Agent, 按 PR/任务完成收费, 体现 outcome-based pricing 在高价值任务场景的可行性; 对应 notes.md "定价从 seat-based 转向 outcome-based" 论点 |
| **MultiOn** | Agent-as-Actor 层次早期形态, 浏览器内自主交易 | MultiOn Agent 在浏览器中代客完成购物/预订, 涉及 Agent 与电商网站的自主交互, 是 A2A 经济 (Agent-to-Agent) 的 C 端雏形; 对应 notes.md A2A 经济章节 |
| **Adept** | Agent-as-Worker 层次通用工作流 Agent | Adept (ACT-1 模型) 让 Agent 跨多个 SaaS 工具自主完成任务, 对应 notes.md "Agent 是新应用形态"的产业实例 |
| **OpenAI** (LLM 后端) | Agent-as-Tool 层次底层 LLM 供应商 | GPT-4o $5/1M input tokens 是本单元推理成本基准参数 (notes.md "真实经济参数"表), 对应仿真 AI 中介每次匹配 $0.0025 的硬约束 |
| **Anthropic** (MCP 提出方) | A2A 经济标准化基础设施供应商 | Anthropic 提出 MCP (Model Context Protocol) 协议, 是 Agent 间发现彼此能力的标准化接口, 对应 notes.md A2A 经济章节中"MCP 是 A2A 经济关键方向" |
| **DeepSeek** | 推理成本下降趋势的产业驱动力 | DeepSeek V3 $0.27/1M input tokens 比 GPT-4o 降 95%, 是本单元"推理成本下降 5-10 倍时 Agent 经济可行性发生质变"论点的真实成本数据来源 |

> 全部公司均来自公司库, 真实存在, 与 Agent 经济主题精准匹配 (Sierra/Devin/MultiOn/Adept 在 Agents 类别; OpenAI/Anthropic/DeepSeek 在 LLM 类别)。

---

## deployment_example

**部署场景: Sierra 在零售客服场景的 Agent-as-Worker 生产部署**

- **公司**: Sierra (Bret Taylor 创办, Agent-as-Worker 层次标杆)
- **场景**: 大型零售企业 (如 Sonos, SiriusXM 等真实 Sierra 客户) 部署 Sierra AI 客服 Agent 处理售后咨询/退换货/订单查询。
- **规模**: 单客户日均处理 10万+ 客服对话, Agent 自主完成 70%+ 一线咨询, 复杂案例转人工。
- **约束**:
  - 信任约束: Agent 决策需可解释 (knowledge graph + 引用源), 错误率 <2%, 安全兜底机制覆盖退款/取消等高风险动作。
  - 度量约束: 每次解决率可审计 (日志归因), outcome-based pricing 按"已解决工单"计费而非 seat。
  - 推理成本约束: 假设每次对话平均 5000 tokens 推理消耗, GPT-4o 基准下每次对话推理成本 ~$0.025, 日均 10万对话推理成本 ~$2500; 切换 DeepSeek V3 后推理成本降至 ~$135/日 (降 95%), 直接影响 Sierra 毛利。
- **效果**: 客户客服成本降 40-60%, 一线响应时间从分钟级降至秒级, 复杂案例人工专注度提升。
- **与本单元关联**: Sierra 部署是 notes.md 三层模型表 (Agent-as-Worker) + 真实经济参数表 (推理成本) + 信任机制章节的产业实例; mesa 仿真中 AI 中介 Agent 的 fee + 推理成本约束直接对应 Sierra 的 outcome-based pricing 模型。

---

## consulting_project

**Imperial College London MSc Business Analytics 咨询项目 (8 周, 4-5 人团队)**

- **Partner (赞助企业)**: Burberry (零售/CPG 类别, Imperial MSc BA 真实 partner 之一)
- **Problem (真实业务问题)**: Burberry 拟在其高端零售场景部署 AI 营销 Agent (代客比价/个性化推荐/库存匹配), 但面临两类商业模式设计两难: (a) Agent 是按 seat 收费 (Agent-as-Tool) 还是按 outcome 收费 (Agent-as-Worker)? (b) 在 GPT-4o 与 DeepSeek V3 之间选哪个 LLM 后端, 综合考虑推理成本、能力、合规?
- **Data (企业提供数据)**: (a) Burberry 过去 12 个月线上客服对话日志 (脱敏); (b) 商品目录与价格历史; (c) 客户分层数据 (VIP/regular); (d) 现有 LLM API 调用成本基线。
- **Scope (8 周 4-5 人)**:
  - W1-2: 文献综述 (a16z Agent Economy + McKinsey 报告) + Burberry 现状访谈
  - W3-4: 用 mesa 构建 Burberry 零售 Agent 经济仿真 (消费者Agent / 商家Agent=Burberry / AI中介Agent), 参数化 GPT-4o vs DeepSeek 推理成本
  - W5-6: batch_run 参数扫描 (抽成率 × 推理成本 × seed), 分析基尼系数/A2A交易量/Agent存活率
  - W7-8: 撰写咨询报告, 给出商业模式建议 (Tool vs Worker) + LLM 后端选择 + 风险评估
- **Deliverable (交付物)**:
  - 原型: mesa 仿真代码 (Burberry 定制版, 基于 starter.ipynb 扩展)
  - 模型: 参数扫描结果 dashboard (matplotlib + pandas)
  - 策略: 商业模式决策矩阵 (Tool/Worker × GPT-4o/DeepSeek, 含 ROI 估算)
  - 报告: 30 页咨询报告 + 1 页 Executive Summary + 20 分钟 presentation

> 与本单元关联: 该咨询项目直接复用 starter.ipynb 的 6 个 TODO 脚手架, 学生在 Day 3 学的 mesa 仿真 + 推理成本约束 + A2A 经济就是咨询项目的核心方法论。

---

## case_study

**HBS 风格教学案例钩子: Sierra 的 Agent-as-Worker 定价两难**

- **Protagonist (主角)**: Bret Taylor (Sierra 联合创始人, 前 Salesforce 联合 CEO, 前 Facebook CTO) -- 面临 Agent-as-Worker 商业模式的核心定价决策。
- **Decision (关键决策点)**: Sierra 应当 (A) 坚持 outcome-based pricing (按已解决工单收费, 单价高但客户采纳门槛高), 还是 (B) 转向 hybrid pricing (基础 seat 费 + 超量 outcome 费, 降低客户采纳门槛但可能稀释 Agent 价值主张), 还是 (C) 引入推理成本 pass-through (把 GPT-4o/DeepSeek 推理成本直接转嫁给客户, 自身只赚 margin)?
- **Tension (核心张力/两难)**:
  - 张力 1 (价值vs采纳): outcome-based 单价高但客户需重新设计 KPI 体系; seat-based 采纳门槛低但退化为传统 SaaS。
  - 张力 2 (毛利vs规模): GPT-4o 后端推理成本高 ($0.0025/匹配) 但能力强, 客户满意度高; 切换 DeepSeek V3 ($0.000135/匹配, 降 95%) 毛利大幅提升, 但部分复杂案例能力下降可能影响 outcome 解决率。
  - 张力 3 (Agent-as-Worker vs Agent-as-Actor): Sierra 当前是 Worker 层次 (人类监督), 但客户开始要求 Agent 间自主交易 (Agent-as-Actor), 是否过早投入 MCP 协议集成?
- **教学用途**: 案例可让学生用本单元 mesa 仿真跑参数扫描, 用 Gini/A2A/存活率数据支撑 Bret 的决策, 把"商业判断"转为"仿真支持的决策"。对应 notes.md 三层模型 + 推理成本 + A2A 经济三章节。

---

## guest_lecture

**客座讲座: "从 Agent-as-Tool 到 Agent-as-Actor: Sierra 的产业实践与未解挑战"**

- **Topic (主题)**: Agent 经济三层模型的产业落地--Sierra 在客服场景如何跨越 Tool->Worker 的信任与度量挑战, 以及 Worker->Actor 的标准化协议 (MCP) 探索。
- **Speaker Profile (主讲人画像)**: Sierra Head of AI 或 VP of Product (具备产业一线经验, 熟悉 outcome-based pricing 的客户谈判细节); 备选: Anthropic Developer Relations 负责人 (讲 MCP 协议在 A2A 经济的角色)。讲座 60 分钟 (40 分钟分享 + 20 分钟 Q&A), 配合 mesa 仿真 demo 展示推理成本对 Sierra 毛利的敏感性。
- **与本单元衔接**: 主讲人可在讲座中引用本单元的 mesa 仿真结果 (Gini 0.108->0.857 / 104 笔 A2A 交易 / DeepSeek 降 95% 推理成本) 作为产业决策的"沙盘工具", 强化"天道推演×多Agent仿真"的工程化价值。

---

## internship_pointer

**实习/驻留指针: AI Agent 公司 + 企业 capstone sponsor**

- **机构 1: OpenAI Residency / Anthropic Residency**
  - 角色: AI Safety / Agent Research Resident
  - 衔接: 本单元的推理成本约束 + Agent 行为规则设计 + A2A 经济章节为 Residency 做准备; 学生在 Residency 中可研究"推理成本下降如何改变 Agent 经济涌现模式", 直接扩展 Day 3 的 mesa 仿真。

- **机构 2: Sierra / Cognition / MultiOn (Agent 公司 capstone sponsor)**
  - 角色: AI Agent Strategy / Product intern
  - 衔接: 本单元三层模型 (Tool/Worker/Actor) + 信任机制 + outcome-based pricing 是这些公司的核心商业模式; 学生在实习中可参与"Agent 经济商业模式设计"项目, 用 mesa 仿真为客户做参数扫描决策支持。

- **机构 3: McKinsey / BCG (AI 咨询 capstone sponsor)**
  - 角色: AI Strategy Associate
  - 衔接: McKinsey 是 notes.md 引用的生成式 AI 价值创造报告来源, 也是本单元 research.md 的 research-to-practice 工件目标读者; 学生在咨询项目中可用 mesa 仿真方法论服务零售/金融客户的 Agent 经济战略评估。

- **机构 4: Hugging Face / Together AI (开源 LLM 平台)**
  - 角色: Developer Advocate / Solutions Engineer
  - 衔接: 本单元"推理成本下降 95% (DeepSeek)"章节直接关联开源 LLM 平台; 学生在实习中可构建"Agent 经济 LLM 后端选型沙盘", 用本单元仿真方法对比 OpenAI/DeepSeek/Llama 后端的涌现差异。

> 全部实习/驻留机构均在公司库内, 与 Agent 经济主题精准匹配。

---

*本文件遵循 Imperial MSc BA 咨询项目模式 (Burberry/Expedia/J&J sponsor) + HBS 案例法 (protagonist + decision + tension) + MIT Sloan 行动学习 (consulting project 8周4-5人) 标准。*
