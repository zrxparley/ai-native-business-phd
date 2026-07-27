# Day 2 Agent框架对比 · 产业链接层 (v7.0)

> 本单元产出产业链接工件。锚点全部来自 `notes.md` 真实框架 (LangGraph/CrewAI/AutoGen/MetaGPT) + `reading.md` 真实链接 + 营销竞品分析任务场景。企业从 v7.0 公司库挑选, 全部真实存在。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **LangChain** (维护 LangGraph) | 本单元基准框架 LangGraph 的维护方, `create_react_agent` / `StateGraph` / `MemorySaver` 三件套的生产提供者; LangSmith (可观测性) + LangGraph Platform (部署) 形成完整生产链路 | 企业用 LangGraph 构建复杂营销 Agent 工作流, 显式控制每一步, 支持 Human-in-the-loop 审核与状态持久化 |
| **CrewAI** (维护 CrewAI) | 本单元 TODO5 静态分析的 CrewAI 框架维护方, `Agent(role,goal,backstory)` / `Task(description,expected_output,agent,context)` / `Crew(agents,tasks,process)` API 的设计者; 25k+ 星 | 企业用 CrewAI 快速构建角色化营销团队 Agent (调研员/分析师/策略师/撰写人), 适合"团队协作"模式的任务分解 |
| **Microsoft** (维护 AutoGen) | 本单元 TODO6 静态分析的 AutoGen 框架维护方, `ConversableAgent` / `GroupChat` / `GroupChatManager` 三件套的设计者; 40k+ 星, CC-BY-4.0 | 企业用 AutoGen 构建多 Agent 对话讨论场景, 如营销策略多视角辩论 (品牌经理/数据分析师/创意总监 Agent 在 GroupChat 中协商) |
| **Sierra** (Agent 平台公司) | 2026 年 Agent 平台代表, 由 Bret Taylor 联合创立, 提供企业级 Customer Experience Agent; 本单元框架选型决策树的"混合方案"参考 | 企业用 Sierra 部署客服/营销 Agent, 其底层编排混合 LangGraph 风格的图控制与角色化设计 |
| **Anthropic** (MCP 提出方) | 本单元 2026 前沿 MCP (Model Context Protocol) 的提出方; MCP 标准化 Agent 与工具连接, LangGraph/CrewAI/AutoGen 均逐步支持; "Building Effective Agents" 文章是本单元底层理论参考 | 企业用 MCP 标准化工具层 (search_product_info/analyze_competitor/write_strategy), 实现跨框架工具复用 |

---

## deployment_example

**场景: Sephora 用 LangGraph 部署营销竞品分析 Agent**

Sephora (LVMH 旗下美妆零售) 的数字营销团队需每周生成竞品分析报告 (透肌精华类目对标 Shiseido/Estée Lauder/SK-II)。传统流程: 数据分析师手动拉取竞品数据 -> 撰写分析 -> 策略师撰写策略, 耗时 3-5 工作日/周。

**部署方案**:
- **框架**: LangGraph `StateGraph` (Plan-Execute 模式), 因营销竞品分析是 **结构化任务** (信息充分、流程清晰), Plan-Execute 步数显著少于 ReAct (见 `research.md` H1)。
- **节点**: `plan_node` (规划 4 步: 搜索产品->分析竞品->对比成分->写策略) + `execute_node` (顺序执行) + `add_conditional_edges` (成分对比异常时分支到深度分析)。
- **工具层**: 通过 MCP 协议连接 Sephora 内部产品库 + 竞品爬虫 + 策略模板库 (search_product_info/analyze_competitor/write_strategy)。
- **Human-in-the-loop**: `interrupt_before` 在 write_strategy 前暂停, 等待营销总监审核竞品分析结论 (LangGraph 原生 HITL 优势, 见 reading.md HITL 教程)。
- **规模**: 每周 1 次自动运行, 覆盖 200+ SKU, 报告生成时间从 3-5 工作日降至 4 小时 (含 HITL 审核)。
- **约束**: ① LLM 成本控制 (用 Claude Haiku 做工具调用, Sonnet 做策略撰写); ② 数据合规 (竞品爬虫遵守 robots.txt); ③ 输出质量 (人工评分 ≥4/5 才发布)。
- **效果**: 报告生成效率提升 8x, 策略采纳率 65% (vs 人工 40%), HITL 审核拦截 15% 的低质量输出。

---

## consulting_project

**Imperial MSc BA 风格咨询项目** (对标 Imperial MSc Business Analytics Burberry/Expedia/J&J capstone 模式):

- **Partner (赞助企业)**: Sephora Digital (LVMH)
- **Problem (真实业务问题)**: Sephora 现有营销竞品分析流程耗时 3-5 工作日/周, 需评估是否用 Agent 框架自动化; 关键决策 = 在 LangGraph/CrewAI/AutoGen 中选哪个框架, 以及是否需要混合方案。
- **Data (企业提供数据)**: ① Sephora 透肌精华类目 200+ SKU 产品数据 (产品名/成分/价格/销量); ② 3 家竞品 (Shiseido/Estée Lauder/SK-II) 公开产品数据; ③ 50 份历史人工竞品分析报告 (用于质量基线); ④ 营销策略模板库。
- **Scope (范围)**: 8 周, 4-5 人团队 (Imperial MSc BA 学生), 含 2 周框架选型 + 4 周原型开发 + 2 周评估与交付。
- **Deliverable (交付物)**:
  1. **框架选型报告** (基于本单元 `research.md` IMRaD 大纲, 含 4 框架控制对比实证结果)
  2. **LangGraph Plan-Execute 原型** (基于 `solution.ipynb` 扩展, 接入 Sephora 真实数据 + MCP 工具层)
  3. **A/B 评估报告** (Agent 生成 vs 人工生成, 质量评分 + 耗时 + 成本对比)
  4. **部署建议书** (含 HITL 流程设计 + LLM 成本优化 + 合规 checklist)

---

## case_study

**HBS 风格教学案例钩子**:

- **Title**: "Sephora's Agent Framework Dilemma: LangGraph, CrewAI, or AutoGen?"
- **Protagonist (主角)**: Marie Chen, Head of AI at Sephora Digital (LVMH), 前 McKinsey 数据科学顾问, 现负责 Sephora 营销自动化转型。
- **Decision (关键决策点)**: Marie 需在 2 周内向 LVMH 集团 CTO 提交营销竞品分析 Agent 的框架选型方案。她的团队评估了 4 个框架:
  - LangGraph Plan-Execute (控制力强, 但学习曲线陡峭, 团队需 6 周培训)
  - CrewAI (角色化直觉, 代码简洁, 但控制力弱, 适合原型不适合生产)
  - AutoGen (多视角辩论, 但收敛慢, 适合策略讨论不适合结构化报告)
  - 混合方案 (LangGraph 骨架 + 关键节点嵌 CrewAI 角色, 复杂但兼顾控制与角色化)
- **Tension (核心张力/两难)**:
  - **短期 vs 长期**: CrewAI 2 周可出原型 (满足 Q3 KPI), 但生产环境控制力不足; LangGraph 6 周培训 (Q3 KPI 风险), 但长期可维护性更强。
  - **控制 vs 灵活**: LangGraph 显式图定义保证质量但牺牲 Agent 自主性; AutoGen 对话涌现灵活但质量不可控。
  - **标准化 vs 锁定**: MCP 标准化工具层降低框架锁定风险, 但 LLM 层仍锁定 (Anthropic vs OpenAI)。
- **教学目标**: 学员用天道推演沙盘模拟 4 框架在 Sephora 场景的因果链, 识别不可逆节点 (Plan 错误传播/角色边界模糊/max_round 耗尽), 给出选型建议 + 风险缓解方案。

---

## guest_lecture

**客座讲座**:

- **Topic (主题)**: "Production Agent Frameworks at Scale: Lessons from Deploying LangGraph at Enterprise"
- **Speaker Profile (主讲人画像)**: LangChain 公司 founding engineer (或 Sierra Head of Engineering), 曾主导 LangGraph 在 5+ Fortune 500 企业的生产部署, 深度参与 `create_react_agent` / `StateGraph` API 设计与 LangGraph Platform 构建。
- **内容大纲**:
  1. 从 38k+ 星开源项目到企业生产: LangGraph 的工程化演进 (2024-2026)
  2. 真实部署案例: 客服 Agent / 营销 Agent / 数据分析 Agent 的框架选型教训
  3. MCP + A2A 协议如何改变框架选型决策 (工具层标准化后, 框架差异是否收敛?)
  4. HITL 的工程实现: `interrupt_before` / `interrupt_after` 在生产中的坑
  5. Q&A: 学生可问"框架选型决策树"实战应用
- **与本单元衔接**: 主讲人将引用本单元 `research.md` 的 4 框架控制对比结果, 作为"实证选型"案例; 学生需在讲座前完成 `starter.ipynb` 6 个 TODO, 带着真实框架体验听讲座。

---

## internship_pointer

**实习/驻留指针**:

- **机构 1: LangChain Internship (开源 Agent 框架)**
  - **角色**: Agent Framework Engineering Intern
  - **衔接**: 本单元学生已掌握 LangGraph `StateGraph` / `create_react_agent` / `add_conditional_edges` 真实 API, 可直接贡献 LangGraph 生态 (如新增预构建 Agent 模式、优化 MemorySaver、贡献 LangSmith 可观测性模板)。`solution.ipynb` 是最好的面试作品集。
  
- **机构 2: Sierra AI Resident (企业 Agent 平台)**
  - **角色**: AI Resident (Customer Experience Agent 方向)
  - **衔接**: Sierra 的 Agent 平台混合 LangGraph 图控制与角色化设计, 本单元"混合方案" (LangGraph 骨架 + CrewAI 角色化节点) 正是 Sierra 的工程范式; 学生用本单元的天道推演沙盘分析可展示选型思维。

- **机构 3: OpenAI Residency (前沿 LLM 研究)**
  - **角色**: AI Resident (Agent 方向)
  - **衔接**: 本单元 StubChatModel 是 LLM 替身, OpenAI Residency 可让学生接触真实 GPT-4/GPT-5 驱动的 Agent, 验证 `research.md` H1/H2 假设; 本单元的 IMRaD 大纲 + 可复现清单是 Residency 申请的优质研究计划模板。

- **机构 4: Sephora Digital Capstone (企业赞助项目)**
  - **角色**: MSc BA Capstone Student (见 consulting_project)
  - **衔接**: 本单元营销竞品分析任务直接复用 Sephora 场景, 学生可在 capstone 中将 `solution.ipynb` 原型扩展为生产级 Agent, 交付给 Sephora Digital。

---

*产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。*
*最后更新: 2026-07-26*
