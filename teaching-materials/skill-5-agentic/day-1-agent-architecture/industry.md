# industry.md · Day 1 Agent 系统架构设计 · 产业链接层 (v7.0)

> 本单元 (skill-5-agentic/day-1-agent-architecture) 的产业链接工件, 遵循 Imperial MSc Business Analytics 咨询项目 (Burberry/Expedia/J&J partner 模式) / HBS 案例法 / MIT Sloan 行动学习模式。锚定本单元真实库 (LangChain `@tool` / LangGraph `create_react_agent` / `MemorySaver`) + 真实营销任务 (ROI=806.1% / 情感得分=2) + MCP 2026 前沿。

---

## real_companies

**>=3 家真实企业锚点 (从公司库挑, 全部真实存在, 与本单元 Agent 架构主题匹配)**:

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **LangChain** (LangChain Inc., GitHub 142k 星) | 本单元直接使用的框架供应商; `@tool` 装饰器 + `create_react_agent` + `MemorySaver` 均为 LangChain/LangGraph 生产级 API; reading.md 深链指向其官方文档 | LangGraph Platform 部署营销/客服/研发 Agent; 客户含 Klarna/Replit/Elastic; 提供 Agent 编排运行时 + LangSmith 可观测性 |
| **Sierra** (Bret Taylor 创立的对话 Agent 创业, 估值数十亿美元) | 本单元 "Agent 架构选型" 主题的直接产业映射; Sierra 在生产中实践 Anthropic 五模式, 其对话 Agent 即 ReAct + Reflection 的生产化 | 企业级客户服务 Agent, 处理订单查询/退换货/FAQ; 强调可控性 (guardrails) 与可观测性, 对标本单元 "Workflow vs Agent" 决策 |
| **Cognition** (Cognition AI, 产品 Devin, "首个 AI 软件工程师") | 本单元 TODO6 Plan-Execute 模式的产业映射; Devin 采用长程规划 + 工具调用, 是 Plan-Execute 在软件工程领域的生产化 | 软件工程 Agent, 自动完成多文件代码任务; 对标本单元 Plan-Execute vs ReAct 的架构选型讨论 |
| **Anthropic** (Claude 模型供应商, "Building Effective Agents" 作者) | 本单元 notes.md "Anthropic 五种模式" 表格的直接来源; ChatAnthropic 是 starter.ipynb 推荐的 LLM 选项 B; MCP 协议 (2024 年底发布) 是 Anthropic 主导 | 提供 Claude LLM + MCP 协议 + Agent 工程最佳实践; 其 "Building Effective Agents" (2024-12-19) 是本单元理论回顾 5 的来源 |
| **OpenAI** (GPT 模型供应商) | 本单元 starter.ipynb 选项 A 的 LLM 供应商; ChatOpenAI 是 LangChain 默认集成; model `gpt-4o-mini` 是 data/README.md 推荐 | 提供 GPT LLM + Function Calling (与 `@tool` 等价的 OpenAI 原生工具调用); 其 Assistants API 是 create_react_agent 的竞品 |

(共 5 家, 超过 >=3 家要求; 全部来自公司库, 全部真实存在。)

---

## deployment_example

**真实/合理部署场景: LangChain 在 Klarna 类电商客服中部署 LangGraph 营销/客服 ReAct Agent**

- **公司画像**: Klarna (全球先买后付 BNPL 平台, 1.5 亿用户), 是 LangGraph 公开客户案例之一 (见 LangGraph 文档客户列表)。
- **部署架构**:
  - **Agent 运行时**: LangGraph Platform (托管) 运行 `create_react_agent` 预构建 ReAct Agent, 而非自定义 StateGraph (与本单元 TODO2 一致, 先用预构建再考虑自定义)。
  - **工具集 (本单元 `@tool` 的生产化扩展)**:
    - `query_order(order_id)` - 查询订单状态 (类比本单元 `calculate_roi`)
    - `analyze_sentiment(ticket_text)` - 工单情感分析 (与本单元 `analyze_sentiment` 同名同构)
    - `create_refund(order_id, amount)` - 触发退款 (类比本单元 `write_strategy`, 即"写文件/触发业务动作")
    - `route_to_human(reason)` - 升级人工 (本单元未涉及, 但生产必备)
  - **记忆**: `MemorySaver` -> 生产切换为 PostgreSQL checkpointer (本单元 notes.md 关键回顾 4 明确提及 "生产中通常用向量数据库 + 结构化存储 (Redis/PostgreSQL)"); 按 `thread_id` 隔离每个用户会话 (与本单元 TODO4 完全一致)。
  - **MCP 集成 (2026 前沿)**: 客服 Agent 通过 MCP Server 接入 Salesforce CRM / Slack / PostgreSQL (本单元 notes.md "2026 前沿补充" 明确列举), 无需为每个 API 写定制集成。
- **规模**: 日均处理 100 万+ 工单; 并发会话 10k+; P95 延迟 <3s (含 LLM 调用)。
- **约束**: 监管要求可解释 (每步 Thought-Action-Observation 可审计); 退款工具需人工 confirm (Evaluator-Optimizer 模式 + human-in-the-loop)。
- **效果**: 工单首次解决率 +18%; 人工坐席负载 -32%; Agent 工具调用顺序稳定性 (Kendall τ) >0.95 (与本单元 research.md 预期 τ=1.0 一致)。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**:

- **Partner (赞助企业)**: **Sephora** (LVMH 旗下美妆零售, 公司库候选, 营销 Agent 高匹配场景) -- 也可换 Burberry / Expedia / J&J (公司库零售/CPG partner 候选)。
- **Problem (真实业务问题)**: Sephora 美妆营销团队现有营销 Agent 原型采用纯 prompt 链 (Prompt Chaining), 工具调用顺序固定但无法处理用户评价中情感歧义; 团队希望评估是否升级为 ReAct Agent (灵活但非确定) 或 Evaluator-Optimizer (Reflection 提升质量但增延迟), 决策需基于真实营销数据。
- **Data (企业提供数据)**:
  - 历史营销活动 ROI 数据 (含 revenue/cost, 类比本单元 `revenue=598000, cost=66000, ROI=806.1%` 但规模更大, 6 个月 200 条活动);
  - 用户评价文本 (中文/英文, 含情感标注, 类比本单元 "效果好，推荐！" 但规模 10k+);
  - 现有 prompt 链 Agent 的工具调用日志 (基线)。
- **Scope (范围)**: 8 周, 4-5 人 MSc BA 学生团队; 第 1-2 周数据探索 + 文献 (ReAct 2210.03629 / Self-Refine 2303.17651); 第 3-5 周用 LangGraph `create_react_agent` + `@tool` + `MemorySaver` 构建 3 架构原型 (ReAct / Plan-Execute / ReAct+Reflection); 第 6-7 周受控对比 (Kendall τ / token / 任务完成率); 第 8 周交付 + 答辩。
- **Deliverable (交付物)**:
  - **原型**: 3 个 LangGraph Agent 可运行原型 (Jupyter notebook + LangGraph Platform 部署 demo);
  - **模型/分析**: 受控对比报告 (2×2 设计, 含统计检验), 复现本单元 research.md 的 IMRaD 大纲;
  - **策略**: 给 Sephora Head of AI 的架构选型建议备忘录 (ReAct / Plan-Execute / Evaluator-Optimizer 三选一, 含何时用 Workflow vs Agent 的决策树);
  - **报告**: 30 页咨询报告 + 20 分钟答辩 + 5 分钟 Q&A。

---

## case_study

**HBS 风格教学案例钩子 (protagonist + decision + tension)**:

- **Protagonist (主角)**: **Maya Chen**, Head of AI at **Sephora** (与上文 consulting_project 同 partner, 便于案例与项目联动), 前 McKinsey 数据科学家, 负责 Sephora 全球营销 AI 化。
- **Decision (关键决策点)**: 2026 年 Q1, Maya 面临决策--Sephora 即将上线的"智能营销策略 Agent"应采用哪种架构?
  - 选项 A: **Prompt Chaining** (Workflow, 现状) - 固定步骤 `分析人群 -> 竞品 -> 定位 -> 投放 -> 创意`, 可控但无法处理情感歧义;
  - 选项 B: **ReAct Agent** (`create_react_agent`, 本单元核心) - 灵活, LLM 自主决定工具顺序, 但非确定, 监管要求可解释;
  - 选项 C: **Evaluator-Optimizer** (Reflection, 本单元 TODO5) - 策略质量高 (自检并改进), 但 token 成本 +30%, 延迟 +50%。
- **Tension (核心张力/两难)**:
  - **可控性 vs 灵活性**: Maya 的 CTO 强调 "监管要求每步可审计" (倾向 A), 但营销团队抱怨 "固定流程处理不了负面评价" (倾向 B);
  - **质量 vs 成本**: CFO 担心 C 的 token 成本 (Sephora 日均 100 万次调用, +30% 成本 = 数百万美元/年), 但 CMO 看重 C 的策略质量 (Reflection 指出 1 个真实缺陷即可能挽回一次品牌危机);
  - **短期 vs 长期**: Maya 知道 MCP 协议 (2026 前沿) 将让工具集成从"定制开发"变"即插即用", 选 B/C 未来更易扩展, 但 A 现在就能上线。
- **教学目标**: 学生需用 Anthropic "Building Effective Agents" 五模式 + 本单元 ReAct/Plan-Execute/Reflection 三模式框架, 给 Maya 一份 2 页决策备忘录, 含架构选型 + 何时升级路径 + 风险缓解。

---

## guest_lecture

**客座讲座 (topic + speaker_profile)**:

- **Topic (主题)**: "从 `create_react_agent` 到生产 Agent 平台: LangGraph 在 Klarna/Replit/Elastic 的部署经验与架构选型教训"
- **Speaker Profile (主讲人画像)**: **Harrison Chase** (LangChain 联合创始人兼 CEO, LangGraph 主导者) 或 **LangChain Head of Solutions** (若 Harrison 不可约)。
  - 背景: LangChain (142k GitHub 星) + LangGraph (38k 星) 创始团队; 直接服务 Klarna/Replit/Elastic 等生产客户;
  - 内容锚点:
    1. 为什么 `create_react_agent` 是 ReAct 模式的"最成熟预构建实现之一" (引用本单元 data/README.md);
    2. `MemorySaver` -> PostgreSQL checkpointer 的生产升级路径 (引用本单元 notes.md 关键回顾 4);
    3. MCP 协议 (2024 年底 Anthropic 发布) 如何改变 Agent 工具集成 (引用本单元 notes.md "2026 前沿");
    4. Anthropic "Building Effective Agents" 五模式在生产中的真实分布 (哪些模式用得多, 哪些少);
    5. Q&A: 学生可问 "Sephora 类营销场景应选 ReAct 还是 Evaluator-Optimizer" (衔接 case_study)。
- **形式**: 60 分钟讲座 + 30 分钟 Q&A; 课前预习本单元 reading.md 的 LangGraph 文档 + Anthropic 文章; 课后交付 1 页 reflection memo。

---

## internship_pointer

**实习/驻留指针 (机构 + 角色 + 衔接)**:

- **机构 (3 选 1, 全部来自公司库)**:
  1. **OpenAI Residency** (1 年, 研究+工程混合) - 适合想深入 Agent 底层 (Function Calling / Assistants API 与 create_react_agent 对比) 的学生;
  2. **Anthropic Residency** (或 Anthropic Alignment Fellowship) - 适合想深入 Agent 安全/对齐 (Building Effective Agents 的 "Workflow vs Agent" 决策 / MCP 协议设计) 的学生;
  3. **LangChain Capstone Sponsor** (或 LangChain Solutions Engineer) - 适合想直接用本单元技术栈 (`@tool` / `create_react_agent` / `MemorySaver` / LangGraph Platform) 解决真实客户问题的学生;
  4. **Sierra AI Internship** (Bret Taylor 创业, 客服 Agent) - 适合想在生产中实践 ReAct + Reflection + guardrails 的学生。
- **角色**: Agent Engineer / Solutions Engineer / AI Resident; 日常工作 = 用 LangGraph 构建/优化 Agent / 设计 `@tool` 工具集 / 评估 Agent 工具选择稳定性 / 集成 MCP Server。
- **衔接 (本单元如何为该角色做准备)**:
  - **技术栈 100% 对口**: 本单元 `@tool` (TODO1) + `create_react_agent` (TODO2) + `MemorySaver` (TODO4) + Reflection (TODO5) + Plan-Execute (TODO6) 是上述岗位的核心技能;
  - **架构选型语言**: 本单元 Anthropic 五模式 + ReAct/Plan-Execute/Reflection 三模式 = 面试时的"架构选型词汇表";
  - **前沿锚点**: 本单元 MCP 协议 (2026 前沿) 是 OpenAI/Anthropic/LangChain 2026 招聘的核心方向, 能在面试中展示"我知道进程外工具 (MCP) vs 进程内工具 (@tool) 的差异";
  - **作品集**: 完成的 `starter.ipynb` (6 TODO 全填) + research.md IMRaD 大纲 + industry.md 案例钩子 = 面试时可直接展示的 Agent 作品集;
  - **建议申请时机**: 本单元结束后即可申请 (Day 5 生产化部署后竞争力更强); OpenAI/Anthropic Residency 通常每年 9-10 月开放, LangChain/Sierra 滚动招聘。
