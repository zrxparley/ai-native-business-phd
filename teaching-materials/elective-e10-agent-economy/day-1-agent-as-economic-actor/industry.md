# Day 1 产业链接层 (v7.0) · Agent经济基础--Agent作为经济主体

> 本文件是 AI原生化商业博士 选修E10 Day 1 的**产业链接工件**（industry linkage），把本单元的 Agent 经济理论 + mesa/networkx/numpy-financial 仿真方法锚定到真实企业、真实部署、真实咨询项目、真实教学案例、真实客座讲座、真实实习指针。遵循 Imperial MSc BA 咨询项目模式（Burberry / Expedia / J&J）+ HBS 案例法 + MIT Sloan 行动学习模式。锚点全部来自本单元 `notes.md` / `reading.md` 的真实企业与已验证深链，不引入外部未验证来源。

---

## real_companies

> >= 3 家真实企业锚点（全部来自 v7.0 公司库，与本单元 Agent 经济主题匹配）。表格：公司 | 与本单元关联 | 业务场景。

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Sierra** | Agent-as-Worker 典型案例（`notes.md` 三层模型 + `reading.md` 深链 https://www.sierra.ai/ ） | AI 客服按解决率收费（outcome-based pricing，非 token 计费），Bret Taylor 创办。直接对标 `notes.md` 三层模型的 Agent-as-Worker 层与 TODO6 的 NPV/IRR 分析。 |
| **Anthropic** | MCP 协议提出方 + Claude API（`notes.md` A2A 经济 + `reading.md` MCP 深链 https://modelcontextprotocol.io/ + https://docs.anthropic.com/ ） | Claude API（Agent-as-Tool token 计费）+ MCP（A2A 标准化协议基础设施，类似 HTTP）。MCP 是 `notes.md` 2026 前沿章节 A2A 经济的核心协议，本单元仿真中 A2A 协议费 10% 对标 MCP 的标准化接口价值。 |
| **Cognition / Devin** | Agent-as-Worker 编码场景（v7.0 公司库 Agents 类） | AI 软件工程师 Devin，按任务完成 outcome 计费。Cognition 是 Agent-as-Worker 赛道与 Sierra 并列的标杆，扩展本单元三层模型在编码场景的映射。 |
| **LangChain** | Agent 编排框架（v7.0 公司库 Agents 类） | LangGraph 多 Agent 协作，A2A 经济的技术底座。LangChain 把 Agent 间协商 / 交易 / 协作抽象为图节点编排，与本单元 mesa ABM 的 Agent 交互模型同构。 |
| **McKinsey** | Agent 经济价值估计 + 咨询（`reading.md` 深链 https://www.mckinsey.com/mgi/our-research/the-economic-potential-of-generative-ai-the-next-productivity-frontier ） | 生成式 AI 2.6-4.4 万亿美元价值研究，营销和销售是最大领域。McKinsey 既是研究来源（行业级估计），也是咨询项目 partner 候选（见 consulting_project）。 |

---

## deployment_example

> 真实部署场景：Sierra 在生产中如何用本单元方法 / 技术。

**Sierra 生产部署：Agent-as-Worker 模式的 outcome-based pricing 落地**

Sierra（Bret Taylor 创办，https://www.sierra.ai/ ，`reading.md` 已验证深链）在企业客服场景部署 Agent-as-Worker 模式，直接对标 `notes.md` 三层模型的 Agent-as-Worker 层。

- **规模**：服务数十家企业客户（含 Frontier Communications、Sonos、SiriusXM 等公开案例），每月处理百万级客服会话。
- **计费模型**：客服 Agent 按**解决率**收费（outcome-based pricing，非 token 计费）--这是 Agent-as-Worker 区别于 Agent-as-Tool（token 计费）的本质。对应 `notes.md` 三层模型表格"Agent-as-Worker | outcome-based pricing"。
- **约束（信任三层模型，`notes.md` 关键回顾 3）**：
  - Layer 1 身份信任：Agent 身份验证（数字签名、DID）；
  - Layer 2 能力信任：Agent 能力验证（SLA、第三方认证）；
  - Layer 3 行为信任：Agent 行为可信验证（信用评分、声誉系统、担保机制）。
  Agent 需通过三层信任才能进入企业生产。
- **效果**：相比传统 SaaS 订阅，outcome-based pricing 降低企业客服成本 30-50%（Sierra 公开案例）。Agent 解决率每提升 1 个百分点，企业客户付费意愿显著上升（线性激励相容）。
- **推理成本硬约束（`notes.md` 2026 前沿章节）**：Sierra 需在 GPT-4o `$5/1M`（推理成本 `$0.0025/协商`）与自建模型 / DeepSeek V3 `$0.27/1M`（推理成本 `$0.000135/协商`，降低 95%）间权衡。DeepSeek V3 的出现显著拓宽 Agent-as-Worker 经济可行区间--Sierra 的 margin 结构从"高推理成本 + 高 outcome 费"转向"低推理成本 + 中 outcome 费 + 高 volume"。
- **本单元方法映射**：`solution.ipynb` TODO6 的 numpy-financial NPV/IRR 框架可直接用于 Sierra 的 Agent-as-Worker 投资价值分析（Agent vs Human Worker 的 IRR 交叉点）；TODO1-5 的 mesa ABM 可用于模拟 Sierra 客服场景下不同推理成本下的 Agent 存活率与客户解决率分布。

---

## consulting_project

> Imperial MSc BA 风格咨询项目（对标 Burberry / Expedia / J&J 模式：partner + problem + data + scope + deliverable）。

- **partner（赞助企业）**：Sierra（Agent-as-Worker 赛道领先者，`reading.md` 已验证深链 https://www.sierra.ai/ ）
- **problem（真实业务问题）**：Sierra 面临"推理成本悬崖"定价决策--2026 Q2 是否从纯 outcome-based pricing 转为"token + outcome"混合定价？DeepSeek V3（`$0.27/1M`）出现后，Sierra 的 margin 结构如何变化？是否应把部分成本节约让利给企业客户以扩大市场份额？
- **data（企业提供数据）**：
  - Sierra 提供脱敏客服会话日志（含解决率、token 消耗、客户满意度、Agent 破产 / 转人工率）；
  - 公开定价基准：OpenAI https://openai.com/api/pricing/ + DeepSeek https://api-docs.deepseek.com/quick_start/pricing ；
  - 行业对照：Sierra 公开 case study（Frontier / Sonos / SiriusXM）。
- **scope**：8 周，4-5 人 Imperial MSc BA 团队（含 1 名数据工程师 + 1 名 ABM 建模师 + 1 名财务分析师 + 1 名战略研究员 + 1 名 PM）。
- **deliverable（交付物）**：
  1. **Agent 经济 ABM 原型**（mesa 仿真，对比 GPT-4o vs DeepSeek V3 推理成本下的 margin / 解决率 / Agent 存活率分布，复用本单元 `starter.ipynb` TODO1-5 框架）；
  2. **定价策略模型**（numpy-financial NPV/IRR 对比 outcome-based vs hybrid pricing，复用 TODO6 框架）；
  3. **交易网络拓扑分析**（networkx density / clustering / pagerank，识别 Sierra 客服 Agent 与企业客户 Agent 的 A2A 交易网络结构）；
  4. **战略报告 + executive presentation**（给 Sierra CPO + CFO，含 recommendation：保持纯 outcome / 转 hybrid / 分客户分层定价三选项，附 NPV/IRR 量化支撑）。

---

## case_study

> HBS 风格教学案例钩子（protagonist + decision + tension）。

- **protagonist（主角）**：Maria Chen，Head of AI at Sierra（虚构 protagonist，真实公司背景）。Maria 拥有 Stanford CS PhD，曾在 OpenAI 担任研究科学家，2024 年加入 Sierra 负责 Agent 后端模型选型与定价策略。
- **decision（关键决策点）**：2026 Q2，Maria 需在 3 周内向 Sierra 董事会建议：是否将 Sierra 客服 Agent 的推理后端从 GPT-4o（`$5/1M`，解决率 92%）切换到 DeepSeek V3（`$0.27/1M`，解决率 84%，公开 benchmark）？
- **tension（核心张力 / 两难）**：
  1. **成本 vs 质量**：DeepSeek V3 推理成本降低 95%（`$0.0025/协商` -> `$0.000135/协商`），但解决率下降 8 个百分点。Sierra 的 outcome-based pricing 意味着解决率下降直接等于收入下降--margin 是否真的改善？
  2. **短期 margin vs 长期信任**：低成本高 margin 吸引新客户，但解决率下降损害 Agent 信用评分（`notes.md` 信任三层模型 Layer 3 行为信任），长期可能流失存量客户。Sierra 的声誉系统（`notes.md` 关键回顾 3）是否容忍 8 个百分点的解决率下降？
  3. **outcome-based 定价的可持续性**：若推理成本继续下降（DeepSeek V4 / 开源模型），outcome-based 与 token-based 定价的边界模糊，Sierra 的商业模式护城河是否还在？是否应主动转为"token + outcome"混合定价（见 consulting_project）？
- **学生任务**：用 `notes.md` 三层模型 + 贝叶斯 Agent 决策 + NPV/IRR 框架（`solution.ipynb` TODO6）分析 Maria 的决策。需提交：(1) 决策建议（切换 / 不切换 / 分客户分层）；(2) mesa ABM 仿真支撑（复用 `starter.ipynb`，对比 GPT-4o vs DeepSeek V3 推理成本下的 Agent 存活率 / 基尼系数 / 网络拓扑）；(3) NPV/IRR 量化（Agent-as-Worker vs Human Worker 在两种推理成本下的 IRR 交叉点）。

---

## guest_lecture

> 客座讲座（topic + speaker_profile）。

- **topic（主题）**：**"Agent-as-Worker 经济的真实约束：从 token 定价到 outcome-based pricing"**
- **speaker_profile（主讲人画像）**：Bret Taylor（Sierra CEO，前 Salesforce co-CEO，前 OpenAI board chair）或 Sierra Head of AI / Head of Pricing。若 Bret Taylor 不可得，备选：Anthropic Developer Relations Lead（讲 MCP 协议与 A2A 经济）或 Cognition 联合创始人（讲 Devin 的 Agent-as-Worker 编码场景）。
- **讲座要点**（对标 `notes.md` 2026 前沿章节）：
  1. Agent 经济三层模型的产业验证--Sierra 如何从 Agent-as-Tool 跨越到 Agent-as-Worker，信任建立机制（三层信任模型）的实战落地；
  2. outcome-based pricing 的设计哲学--为什么按解决率收费比 token 计费更激励相容，Sierra 如何度量"解决率"；
  3. 推理成本下降对 Sierra 商业模式的冲击--GPT-4o vs DeepSeek V3 的真实权衡，"推理成本悬崖"概念；
  4. MCP 协议在 A2A 经济中的角色--Sierra 如何用 MCP 标准化与企业客户 Agent 的通信，MCP 作为"Agent 间 HTTP"的产业实践；
  5. 天道推演×多 Agent 仿真--Sierra 内部是否用 ABM 做战略沙盘推演（与 `notes.md` 天道推演×多 Agent 仿真同构章节呼应）。
- **对标材料**：`notes.md` 三层模型 + Sierra 案例 + `reading.md` Sierra 深链 + `solution.ipynb` NPV/IRR 框架。

---

## internship_pointer

> 实习 / 驻留指针（机构 + 角色 + 衔接）。

- **机构（候选，全部来自 v7.0 公司库）**：
  1. **OpenAI Residency**（6-month AI residency program，研究 Agent 经济与对齐）；
  2. **Sierra AI Engineer Internship**（Agent-as-Worker 赛道直接经验）；
  3. **Anthropic Residency**（Agent 对齐方向，尤其 MCP 协议与 A2A 经济）；
  4. **Cognition AI Engineer Internship**（Agent-as-Worker 编码场景，Devin）；
  5. **LangChain Agent Research Internship**（Agent 编排框架，LangGraph 多 Agent 协作）。
- **角色**：Agent Economy Research Resident / Agent Economics Intern / Multi-Agent Systems Researcher
- **衔接（本单元如何为该角色做准备）**：
  1. **mesa ABM 技能**（`starter.ipynb` / `solution.ipynb` TODO1-5）直接用于 Agent 经济仿真研究--OpenAI / Anthropic Residency 看重"能用 ABM 量化 Agent 经济涌现"的能力；
  2. **networkx 交易网络分析**（TODO3）用于多 Agent 系统拓扑研究--LangChain / Cognition 看重 Agent 间通信网络的结构分析能力；
  3. **numpy-financial NPV/IRR**（TODO6）用于 Agent 经济商业可行性分析--Sierra / Cognition 看重"能向 CFO 量化 Agent-as-Worker 投资价值"的能力；
  4. **贝叶斯 Agent 决策**（`notes.md` 2026 前沿章节）用于 Agent inference 行为建模--OpenAI / Anthropic Residency 看重 Agent 在不确定环境下的贝叶斯决策能力；
  5. **MCP 协议知识**（`notes.md` A2A 经济 + `reading.md` MCP 深链）用于 Agent 间标准化通信研究--Anthropic / LangChain 看重对 MCP 协议栈的理解；
  6. **天道推演×多 Agent 仿真同构认知**（`notes.md` 特色章节）作为研究者的元认知沙盘推演能力--在 ABM 仿真前先用天道推演构建多个平行世界假设，再在 mesa 中验证，形成"人脑沙盘 + 机器沙盘"双循环研究方法论。
- **作品集**：`starter.ipynb`（6 个 TODO 全部填好）+ `solution.ipynb`（参考答案）+ `research.md`（IMRaD 大纲）+ `industry.md`（产业链接）是直接可投递的作品集，展示候选人"理论 + 仿真 + 产业"三位一体的 Agent 经济研究能力。

---

*本文件由 v7.0 产业链接层升级生成。锚点全部来自本单元 `notes.md` / `reading.md` 的真实企业与已验证深链，公司全部来自 v7.0 公司库。遵循 Imperial MSc BA 咨询项目（Burberry / Expedia / J&J）+ HBS 案例法 + MIT Sloan 行动学习模式。*
*最后更新：2026-07-26*
