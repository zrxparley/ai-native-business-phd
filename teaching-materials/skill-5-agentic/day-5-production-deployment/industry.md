# industry.md · 产业链接层 (v7.0)

> **单元**：技能5 · Day 5 生产部署与运维（LangSmith @traceable + wrap_openai / tiktoken / vLLM / 投机解码 / MoE）
> **定位**：本单元学习材料与真实企业、咨询项目、教学案例、客座讲座、实习指针的产业链接。

---

## real_companies

本单元主题（生产部署运维 + 推理成本优化 + 可观测性 + 灾备降级）匹配的真实企业锚点（全部来自公司库，真实存在）：

| 公司 | 与本单元关联 | 业务场景 |
|:----:|:------------|:---------|
| **Together AI** | vLLM 推理服务的商业化旗舰 | 基于 vLLM PagedAttention 与连续批处理提供高吞吐 LLM 推理 API，对标本单元 notes.md "vLLM 在相同硬件上吞吐量达原生 HuggingFace 14-24 倍"的工程落地；企业客户在 Together 上自建 Agent 推理后端以替代商业 API，实现日均万次请求的降本目标。 |
| **OpenAI** | tiktoken 的出品方 + 生产级 LLM API 标杆 | tiktoken 是本单元 token 计数与成本计算的事实标准（notes.md "成本计算基础"）；OpenAI API 的 gpt-4o / gpt-4o-mini 是本单元 ResilientLLM 多级 fallback 链中的主模型与备用模型；OpenAI 自身在生产部署上对 P50/P95/P99 延迟、token 计费、限流的工程实践直接映射本单元 TODO2/TODO3/TODO6。 |
| **AWS Bedrock** | 生产级多模型 fallback 部署平台 | Bedrock 支持 OpenAI/Anthropic/Meta 等多模型路由与灾备，与本单元 ResilientLLM 多级 fallback（主模型 -> 备用模型 -> 缓存 -> 默认模板）架构同构；企业客户在 Bedrock 上实现本单元 TODO4 的灾备降级策略，配合 CloudWatch 做本单元"三层可观测性"中的第一层（基础设施监控）。 |

补充候选（如需扩展）：Replicate（生产 LLM 部署平台，与 Together AI 同类）、Anthropic（生产 LLM API + 对齐安全，与本单元安全合规检查呼应）、NVIDIA（vLLM 在 NVIDIA GPU 上的硬件层优化，PagedAttention 的物理底座）。

---

## deployment_example

**部署场景：某 DTC 美妆品牌（年 GMV 5 亿）在 AWS Bedrock + Together AI 上生产化营销内容生成 Agent**

- **规模**：日均 12,000 次小红书种草文案 + 朋友圈广告生成请求，峰值 QPS 50（双十一大促期间 QPS 200）。
- **架构**：主模型 gpt-4o（OpenAI API）-> 备用 gpt-4o-mini（AWS Bedrock 路由）-> draft model gpt-4o-mini-real（Together AI vLLM 自建服务，启用投机解码）-> 默认模板（本地 Redis 缓存）。三层 fallback 对应本单元 solution.ipynb TODO4 的 ResilientLLM 实现。
- **可观测性**：LangSmith `@traceable` 装饰 Agent 主函数，`wrap_openai` 自动 instrument 所有 LLM 调用，trace 数据流入 LangSmith Dashboard；CloudWatch 监控基础设施（CPU/内存/网络）；自建 BI Dashboard 监控业务指标（CTR/转化率/人工修改率）。三层对应 notes.md "三层可观测性设计"。
- **约束**：P95 延迟 ≤5s（生产要求），日均 token 成本 ≤300 美元，任务完成率 ≥90%，幻觉率 ≤5%，安全违规率 =0%。
- **效果**：vLLM PagedAttention 使 Together AI 自建推理吞吐量达原生 HuggingFace 的 18x（notes.md 记录区间 14-24x 中位）；投机解码将 P95 延迟从基线 28s 降至 4.2s（2-3x 区间内）；MoE 路由（Mixtral 8x7B 激活 2/8 专家）在简单文案任务上单次推理成本下降约 42%；ResilientLLM 多级 fallback 将月度可用性从 95.3% 提升至 99.94%。日均总成本约 220 美元，低于 300 美元预算。

---

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目**

- **Partner（赞助企业）**：Burberry（奢侈品零售，公司库中标注的咨询项目 partner）
- **Problem（真实业务问题）**：Burberry 的全球社媒营销团队日均生成约 8,000 条多语言文案（小红书/Instagram/TikTok），目前用第三方 SaaS 工具成本不可控且 P95 延迟波动大（5-45s），影响营销活动上线节奏。需评估"自建 vLLM 推理服务 vs 继续用 SaaS"的 TCO（总拥有成本）与延迟可靠性 trade-off。
- **Data（企业提供数据）**：Burberry 提供 6 个月脱敏营销文案生成日志（含请求时间戳/输入 prompt/输出文案/用户采纳率/人工修改率/延迟），约 120 万条；以及当前 SaaS 供应商的月度账单与 SLA 报告。
- **Scope（8 周，4-5 人团队）**：
  - W1-2：用 LangSmith `@traceable` + `wrap_openai` 对现有 SaaS 调用链做 instrumentation，建立 baseline P50/P95/P99 与 token 成本曲线。
  - W3-4：在 Together AI 上搭建 vLLM 推理服务原型，复现本单元 notes.md 14-24x 吞吐量与投机解码 2-3x 延迟降低。
  - W5-6：用 tiktoken 精确测算 MoE 路由（Mixtral 8x7B）在多语言文案上的 token 成本对比；用本单元 ThreadPoolExecutor 压测模拟双十一 QPS 200。
  - W7-8：交付 TCO 模型 + 推荐架构 + CI/CD 评估门禁设计（任务完成率 ≥90%、幻觉率 ≤5%、P95 ≤5s 阻止部署规则）。
- **Deliverable（交付物）**：① 可运行原型（vLLM + LangSmith trace Dashboard）；② TCO 对比报告（3 年期 NPV）；③ 推荐架构图与 ResilientLLM fallback 设计；④ CI/CD YAML 与 pytest 评估门禁；⑤ 高管汇报 deck（面向 Burberry CMO 与 CTO）。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：Lin Wei，某 DTC 美妆品牌 Head of AI（前 Meta Ads 工程师，加入品牌 18 个月，主导营销 Agent 从 PoC 走向生产）。
- **Decision（关键决策点）**：双十一前 6 周，OpenAI API 连续两次区域性故障导致营销 Agent 不可用 47 分钟，CMO 要求"48 小时内给出可靠性方案"。Lin Wei 面临三个选项：
  - A. 继续单押 OpenAI API，加本地缓存层（成本最低，但 SLA 仍受制于供应商）。
  - B. 接入 AWS Bedrock 做多模型 fallback（成本中，需重新签企业合同，2-3 周）。
  - C. 自建 Together AI vLLM 推理服务 + 投机解码 + MoE 路由（成本最高但可控，需招 2 名 ML 工程师，4-6 周，但长期 TCO 最优且 P95 可压到 ≤5s）。
- **Tension（核心张力）**：
  - **短期 vs 长期**：A/B 能在 48 小时决策窗口内缓解 CMO 压力，C 需 4-6 周但长期成本降 40%+。
  - **可控性 vs 复杂度**：C 把推理栈握在自己手里（vLLM PagedAttention + 投机解码 + MoE 三件套全可控），但运维复杂度上升，团队需学本单元 LangSmith 可观测性 + ResilientLLM fallback + CI/CD 评估门禁整套技能。
  - **PoC 思维 vs 生产思维**：CEO 倾向 A（"先跑起来"），CTO 倾向 C（"生产可用"），Lin Wei 需用本单元 notes.md "PoC 能跑 ≠ 生产能用"的五大挑战框架做决策说服。
- **教学目标**：让学生用本单元学到的 vLLM / 投机解码 / MoE / LangSmith / ResilientLLM 知识，量化三个选项的 P95/成本/可用性/TCO，做出推荐并辩护。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**：*From PoC to 99.9%: Productionizing LLM Agents with vLLM, Speculative Decoding, and MoE at Scale*（从 PoC 到 99.9% 可用性：vLLM、投机解码与 MoE 在大规模 Agent 生产化中的实践）
- **Speaker Profile（主讲人画像）**：Together AI Head of AI Infrastructure（或 AWS Bedrock 首席解决方案架构师），10+ 年分布式系统经验，主导过日均亿级请求的 LLM 推理服务，是 vLLM PagedAttention 论文的早期生产验证者之一，曾在 NeurIPS / ICML 工业track 做 invited talk。
- **内容大纲（50 分钟 + 10 分钟 Q&A）**：
  1. （10 分钟）生产化五大挑战的真实数字：可靠性 99.9% / 成本 / 延迟 / 可观测性 / 安全合规在 Together AI 客户案例中的实测。
  2. （15 分钟）vLLM PagedAttention 内部机制 + 14-24x 吞吐量在生产环境的复现条件（batch size / KV Cache / 硬件）。
  3. （10 分钟）投机解码（arXiv 2211.17192）的 draft model 选择策略与接受率实测，何时 2-3x 加速有效、何时失效。
  4. （10 分钟）MoE 路由（Mixtral 8x7B / DeepSeek-MoE arXiv 2401.04088）在 Agent 多步调用链上的成本建模。
  5. （5 分钟）LangSmith `@traceable` + CI/CD 评估门禁的工程实践。
- **与本单元衔接**：讲座内容直接对应 notes.md "2026 前沿补充"三件套与 reading.md ③④ 的深链材料，学生听完讲座后可在 solution.ipynb TODO6 压测中复现主讲人提到的数字。

---

## internship_pointer

**实习/驻留指针**

- **Institution（机构）**：OpenAI Residency（或 Together AI ML Engineer Internship / AWS Bedrock Solutions Architect Internship）
- **Role（角色）**：OpenAI Residency -- LLM Systems & Inference track（6 个月驻留，面向有 ML/系统工程背景的应届生或博士生）；或 Together AI Inference Engineer Intern（12 周暑期实习，专注 vLLM 与投机解码生产优化）。
- **衔接（本单元如何为该角色做准备）**：
  1. **LangSmith `@traceable` + `wrap_openai` + Client API**：本单元 TODO1 训练的可观测性技能直接对应 OpenAI Residency 中"用 trace 数据诊断生产 Agent 故障"的日常工作流。
  2. **tiktoken + 成本建模**：TODO2 的 token 计数与定价表组合，对应 OpenAI 内部对模型定价与 token 经济学的量化分析能力。
  3. **vLLM PagedAttention + 投机解码 + MoE**：notes.md "2026 前沿补充"三件套正是 Together AI Inference Engineer 的核心面试考点；reading.md ③ 的 arXiv 2211.17192 与 2401.04088 是驻留面试必读论文。
  4. **ResilientLLM 多级 fallback + CI/CD 评估门禁**：TODO4/TODO5 训练的灾备降级与评估门禁设计，对应 AWS Bedrock Solutions Architect 为企业客户设计生产 Agent 架构的核心交付能力。
- **申请建议**：用本单元 solution.ipynb 作为申请材料中的"productionization work sample"；research.md 的 IMRaD 大纲可作为 research statement 雏形；industry.md 的 consulting_project（Burberry）可作为 case interview 准备材料。
