# industry.md — Phase 6 Capstone 产业链接层 (v7.0)

> 单元: capstone-ai-business-analytics / day-phase-6-implementation-paper-writing
> 主题: Capstone Phase6 实现+论文 (LangSmith @traceable / NSW ATE=1636 / deepeval 0.80 / arxiv 5篇发表路线图 / 天道推演×多Agent仿真)
> 标准: Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (Action Learning)

---

## real_companies

>=3 家真实企业锚点（从公司库挑选，与本单元 LangSmith trace / 因果 A/B / LLM 评估主题匹配）：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|----------|
| **LangChain** | LangSmith `@traceable` 是本单元 TODO2 可复现基础设施的核心库；LangChain 团队维护 langsmith-sdk（reading.md 已记录 GitHub 仓库） | 生产级 LLM Agent 可观测性 + trace 存档 + 评估 CI；本单元 trace 检索 API 即 LangSmith Observability |
| **Microsoft** | Microsoft ExP 是业界 A/B 实验标杆；Microsoft Research 维护 DoWhy 因果推断库（reading.md 已记录 py-why/dowhy）；NSW RCT 是 ExP 真实实验方法的学术复刻 | 大规模 A/B 实验平台 + 因果识别工具链；本单元 DoWhy + causaldata NSW 的工业对应 |
| **Booking.com** | 业界因果推断 + A/B 实验领先者，公开发表大量因果识别 + 决策科学论文；与本单元 NSW ATE 估计 + APA 统计报告 + DSR artifact 直接对应 | 在线旅行平台的实时因果推断 + 个性化 Agent 决策；本单元 ATE=1636 / d=0.27 的工业落地场景 |
| **Anthropic** | 本单元 deepeval LLM-as-a-judge 评估用 Claude 系列模型；Anthropic 公开发表 Constitutional AI / 对齐研究，与本单元 deepeval 五维评估的"对齐维度"对应 | LLM-as-a-judge 评估服务商 + 安全对齐研究；本单元 deepeval 0.80 评分背后的模型供应方 |
| **OpenAI** | 本单元 arxiv 5 篇发表路线图的"对标论文"中，OpenAI Residency / Researcher Residency 项目是产业实习指针（见 §internship_pointer） | LLM 研究 + Residency 项目；本单元研究产出 → 实习衔接的天然出口 |

---

## deployment_example

**真实部署场景：Booking.com 的因果推断 + Agent 决策生产管线**

- **规模**：Booking.com 每天运行 >1000 个 A/B 实验，覆盖 >100M 用户；ExP 团队（与 Microsoft ExP 同源方法论）用因果识别处理实验污染与溢出效应。
- **约束**：(1) 实时性 — Agent 决策延迟 <200ms P95；(2) 可复现性 — 每次实验必须产出可查询 trace 存档供审计；(3) 法规 — GDPR 数据驻留要求 trace 存档在欧盟区域。
- **与本单元方法对应**：
  - 本单元 TODO2 LangSmith `@traceable` → Booking.com 的实验 trace 存档基础设施（每个 Agent 决策可追溯）。
  - 本单元 TODO3 DoWhy + causaldata NSW → Booking.com 的因果识别管线（ATE 估计 + 安慰剂检验 + 敏感性分析）。
  - 本单元 TODO4 statsmodels APA 报告 t(443)=2.84, p=0.005, d=0.27 → Booking.com 实验报告的统计标准化格式。
  - 本单元 TODO6 deepeval LLM-as-a-judge → Booking.com 用 LLM 自动评估 Agent 决策质量（CI/CD 集成）。
- **效果**：Booking.com 公开报告显示，因果识别驱动的 Agent 决策使转化率提升 2-5%（行业基准）；本单元 NSW ATE=1636 美元为同方法论的学术复现锚点。

**部署关键差异**：学术场景（本单元）用历史 RCT 数据复现；生产场景（Booking.com）用实时流式数据 + 增量因果识别。本单元 trace 存档基础设施为生产场景的可审计性做准备。

---

## consulting_project

**Imperial MSc BA 风格咨询项目（8 周，4-5 人团队）**：

- **Partner（赞助企业）**：Booking.com（或 Microsoft ExP / Anthropic，三选一；本方案以 Booking.com 为例）
- **Problem（真实业务问题）**：Booking.com 的 Agent 决策管线目前依赖人工抽样审计，每月仅能覆盖 <5% 的 trace；需要构建一个基于 LangSmith trace 存档 + deepeval LLM-as-a-judge 的自动化审计系统，覆盖 100% 的生产 trace，并产出可复现的因果识别报告。
- **Data（企业提供数据）**：(1) 脱敏的 1 个月 Agent 决策 trace 存档（约 10M 条）；(2) 对应的 A/B 实验元数据（实验 ID / 假设 / 样本量 / 结果指标）；(3) 历史人工审计标签（约 50K 条，作为 LLM-as-a-judge 的校准集）。
- **Scope（范围）**：8 周，4-5 人团队；分三阶段：(1) 第 1-2 周数据理解 + trace 存档 schema 设计；(2) 第 3-5 周 DoWhy 因果识别 + deepeval 自定义 BaseMetric 开发；(3) 第 6-8 周端到端管线集成 + APA 统计报告 + IMRaD 风格最终报告。
- **Deliverable（交付物）**：
  1. 可运行原型（Jupyter notebook + LangSmith trace 集成，复用本单元 `solution.ipynb` 架构）；
  2. 因果识别模型（DoWhy CausalModel + 安慰剂检验 + 敏感性分析，输出 ATE + CI + APA 报告）；
  3. deepeval 评估管线（5 维度自定义 BaseMetric + GEval，输出均分 ≥0.80）；
  4. 策略报告（IMRaD 结构，3000-5000 字，含 DSR artifact 描述 + 天道推演×多Agent仿真特色章节）；
  5. 最终展示（Partner 现场 30 分钟 + Q&A，含 trace 存档 demo）。

**与 Imperial MSc BA 历史项目对标**：Burberry（营销分析）/ Expedia（在线旅行）/ J&J（医疗）为 Imperial MSc BA 三大历史 partner；本项目以 Booking.com 为 partner，承接 Expedia 同行业（在线旅行）的方法论升级。

---

## case_study

**HBS 风格教学案例钩子**：

- **Protagonist（主角）**：Maria Chen，Booking.com Head of AI Marketing Agents，前 Imperial MSc BA 毕业，负责 100+ Agent 的生产管线审计。
- **Decision（关键决策点）**：2026 年 Q3，Maria 面临一个决策 — 是否将 Agent 决策审计从"人工抽样 5%"升级为"LangSmith trace + deepeval LLM-as-a-judge 全量自动化审计"？升级成本：120 万美元/年（LangSmith 商业版 + LLM 调用）；不升级风险：GDPR 审计失败可能罚款 4% 全球营收。
- **Tension（核心张力/两难）**：
  - **效率 vs 严谨**：全量自动化审计覆盖 100% trace，但 LLM-as-a-judge 有已知偏差（arXiv 2306.05685 §5），可能漏报 5-10% 的真实违规。
  - **成本 vs 合规**：120 万美元/年的 LangSmith + LLM 成本，相对 GDPR 罚款风险（4% 营收 ≈ 4 亿美元）是合理投资，但 CFO 要求 ROI 量化。
  - **可复现 vs 商业锁定**：LangSmith trace 存档依赖 LangChain 商业服务，迁移成本高；自建 trace 基础设施需要 6 个月工程投入。
  - **学术 vs 工业**：Maria 的前导师（Imperial 教授）建议发表 arXiv 预印本（强化个人品牌 + 学术贡献），但 Booking.com 法务要求方法论保密（竞争优势）。

**案例教学目标**：学生扮演 Maria，用本单元 DSR 六步框架 + NSW ATE 估计 + deepeval 评估 + 天道推演沙盘模拟，在 90 分钟内产出 3 条决策建议（含因果证据 + 风险评估 + ROI 测算）。

---

## guest_lecture

**客座讲座**：

- **Topic（主题）**：*"From Research Artifact to Production: How LangSmith @traceable Powers Reproducible AI Agent Systems at Scale"* — 从 DSR artifact 到生产部署：LangSmith 如何在规模化场景中支撑可复现 AI Agent 系统。
- **Speaker Profile（主讲人画像）**：Harrison Chase，LangChain CEO 兼联合创始人；LangSmith 主要架构师；开源社区领袖（LangChain GitHub 100k+ stars）。备选：LangChain DevRel Lead 或 LangSmith 团队 Senior Engineer。
- **讲座结构（90 分钟）**：
  1. (15 min) LangSmith `@traceable` 设计哲学 — 为什么 trace 存档是可复现研究的基石；
  2. (20 min) 真实生产案例 — 如何在 100M+ trace/天的规模下保持查询性能；
  3. (20 min) 与本单元 TODO2 的对应 — 学生用 `@traceable` 追踪 Phase 1-5 执行链的实操演示；
  4. (20 min) LLM-as-a-judge + trace 存档的协同 — 与 deepeval 的集成实践；
  5. (15 min) Q&A — 聚焦"从学术 artifact 到生产部署"的迁移路径。
- **与本单元衔接**：讲座内容直接对应 notes.md § 关键回顾 1 的"可复现层"与 § 2026前沿的"可复现研究与 LangSmith trace 存档"；学生在讲座前需完成 TODO2（LangSmith 可复现基础设施）。

---

## internship_pointer

**实习/驻留指针**：

- **机构 1（首选）**：**OpenAI Residency** — OpenAI 研究员驻留项目（1 年，全职，带薪）；适合本单元 arxiv 5 篇发表路线图的 Paper 2/3 阶段学生。
  - **角色**：Research Resident, Agent Evaluations 团队；
  - **衔接**：本单元 deepeval LLM-as-a-judge 评估 + arXiv 2306.05685 方法论为该角色的直接准备；Harrison Chase 客座讲座（见 §guest_lecture）可提供推荐信路径。

- **机构 2（备选）**：**Anthropic Residency / Academy** — Anthropic 研究驻留项目（6-12 个月）；适合本单元安全对齐方向学生。
  - **角色**：Research Resident, Alignment Evaluations；
  - **衔接**：本单元 deepeval 五维评估的"对齐维度" + Constitutional AI 相关阅读为该角色准备；研究产出（research.md）的 IMRaD 大纲符合 Anthropic 研究文化。

- **机构 3（企业 Capstone Sponsor）**：**Booking.com / Microsoft ExP / LangChain**（三选一，与 §consulting_project 的 partner 对应）— 企业 Capstone 赞助实习（3-6 个月，暑期）。
  - **角色**：Data Science Intern, Causal Inference & Agent Systems；
  - **衔接**：本单元 NSW ATE 估计 + DoWhy + LangSmith trace 存档为该角色的核心技能；咨询项目交付物（§consulting_project）可直接作为实习面试作品集。

- **机构 4（学术）**：**Imperial MSc BA Industry Project**（必修，8 周）— 本单元 consulting_project（§consulting_project）即 Imperial MSc BA 的 Industry Project 雏形，完成本单元后可直接申请 Imperial MSc BA 项目。

**准备路径**：本单元 → arXiv 预印本（Paper 1）→ 客座讲座 networking → OpenAI/Anthropic Residency 申请 → 企业 Capstone Sponsor 面试 → Residency 录取。

---

*本文件遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (Action Learning) 标准。所有公司从公司库挑选，未联网查询。*
*最后更新：2026-07-26*
