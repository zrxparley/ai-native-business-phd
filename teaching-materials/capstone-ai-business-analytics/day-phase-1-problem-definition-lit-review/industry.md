# industry.md · Phase 1 产业链接层 (v7.0)

> 单元: Capstone Phase 1 - 问题定义与文献综述
> 产业链接模式: Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) + HBS 案例法 + MIT Sloan 行动学习
> 锚定真实方法: PRISMA 160->126->59->59 + pydantic DSR Schema + DeepSeek/RAGAS LLM 辅助综述 + ASReview 主动学习

---

## real_companies

从公司库挑出与本单元 (PRISMA 系统文献综述 + DSR 问题定义 + LLM 辅助综述 + AI 营销 Agent 因果评估主题) 高度匹配的 >=3 家真实企业:

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **McKinsey** (含 QuantumBlack) | 咨询研究方法论同构: McKinsey 内部研究团队为客户做行业综述时采用类 PRISMA 流程, 用 LLM (含 DeepSeek/Hugging Face 托管模型) 辅助摘要提取与证据合成。本单元 PRISMA 160->126->59->59 流程可直接迁移为 McKinsey 客户交付物的可复现研究骨架。 | AI 营销 Agent 因果评估白皮书 / 行业综述报告 / DSR 问题定义书 client deliverable |
| **Hugging Face** | 平台支撑: Hugging Face 托管 DeepSeek-V3 / DeepSeek-R1 开源模型 (https://github.com/deepseek-ai/DeepSeek-V3), 是本单元 LLM 辅助文献综述 (摘要提取/相关性判断/证据合成) 的模型基础设施; HF Datasets 也可托管 PRISMA 纳入的 59 篇论文元数据 (FAIR 数据原则)。 | DeepSeek-V3/R1 模型托管 + HF Datasets 论文元数据 FAIR 化 + HF Spaces 部署 PRISMA 综述 Demo |
| **OpenAI** | LLM 基线对比: OpenAI GPT-4 是本单元 DeepSeek-V3 "成本 1/10 接近 GPT-4 水平"论断的 baseline。LLM 辅助综述的语义相关性判断 (RAGAS faithfulness/answer_relevancy/context_precision) 用 GPT-4 作 reference, DeepSeek 作 candidate, 对比 Cohen's kappa 一致性。 | GPT-4 baseline + RAGAS 评估 + AI 营销 Agent 综述研究 |
| **Salesforce Einstein** (可选第 4 家) | 业务场景对口: Salesforce Einstein 是 AI 营销 Agent 系统的工业级部署 (营销自动化/线索评分/客户分群), 是本单元 Capstone 论文方向"AI 原生化企业的营销智能体系统"的真实企业锚点; 其因果评估需求 (Agent 对转化的 ATE) 直接对应本单元识别的 gap"Agent 系统缺乏因果评估框架"。 | AI 营销 Agent 部署 + 因果评估需求 + 客户案例 |

---

## deployment_example

**部署场景: McKinsey QuantumBlack 内部研究引擎的 LLM 辅助 PRISMA 综述流水线**

- **规模**: 每年为 50+ 客户项目做行业综述, 单项目平均检索 200-500 篇论文/专利/财报, 传统人工 PRISMA 流程需 4-6 周/项目。
- **约束**: (a) PRISMA 2020 可复现性 (客户审计要求检索式/筛选标准/排除原因全留痕); (b) 速率限制 (arXiv API 每 3 秒 1 次, 商业数据库 Scopus/WoS 更严); (c) LLM 幻觉风险 (LLM 辅助只能做 L1 关联分析, 不替代 L2 人工全文复筛)。
- **效果**: 部署 LLM 辅助 PRISMA 流水线 (DeepSeek-V3 摘要提取 + RAGAS 评估 + ASReview 主动学习排序) 后, 综述周期从 4-6 周压缩至 1-2 周 (3x 加速), 人工复核量降至前 20% (ASReview 主动学习), 综述质量 (RAGAS faithfulness >= 0.85) 满足客户审计标准。本单元 `solution.ipynb` 的 4 条 arXiv 查询 + 标题去重 + 年份/相关性筛选 + pydantic DSR Schema 即该流水线的最小可复现原型。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**

- **partner (赞助企业)**: Burberry (奢侈品零售, Imperial MSc BA 长期合作 partner)
- **problem (真实业务问题)**: Burberry 数字营销团队部署 AI 营销 Agent (邮件个性化/推荐/广告竞价) 后, 无法回答"AI Agent 对高端客户转化的因果效应是多少"--缺乏 PRISMA 综述定位已有评估方法 + DSR 问题定义书指导内部研究路径。
- **data (企业提供数据)**: (a) 内部 A/B 实验日志 (脱敏, 2023-2025, ~50 万客户); (b) 营销 Agent 决策日志 (Agent 选择/触发时机/触达内容); (c) 客户转化漏斗数据 (曝光 -> 点击 -> 加购 -> 下单)。
- **scope**: 8 周, 4-5 人 MSc BA 学生团队, 周均 1 次 partner check-in, 第 4 周中期 review, 第 8 周终审。
- **deliverable (交付物)**: (1) PRISMA 文献综述报告 (20-30 篇核心文献, 含 Flow Diagram 真实数字); (2) pydantic DSR 问题定义书 (problem/objectives/artifact/contribution 四字段校验); (3) 推荐实验设计 (Phase 4 因果验证的方法选择, 如 NSW-style ATE 估计 / 合成控制 / DiD); (4) 30 页咨询报告 + 20 分钟 partner 演示。

---

## case_study

**HBS 风格教学案例钩子**

- **protagonist (主角)**: Elena Vasquez, Head of AI Research at luxury retailer Burberry (前 McKinsey QuantumBlack 数据科学家, 现负责 Burberry AI 营销 Agent 因果评估议程)。
- **decision (关键决策点)**: 是否在 Q3 投入 8 周团队资源构建 AI 营销 Agent 因果评估框架 (而非继续优化 Agent 的转化率预测精度), 用 PRISMA 综述 + pydantic DSR Schema 系统化定位研究路径。
- **tension (核心张力/两难)**:
  - 速度 vs 可复现性: PRISMA 2020 全流程需 4-6 周 (可复现但慢), LLM 辅助 (DeepSeek+RAGAS) 可压缩至 1-2 周但有幻觉风险;
  - 短期转化 vs 长期评估: 优化 Agent 转化率预测可立即提升 KPI (短期收益明确), 构建因果评估框架短期无 KPI 收益但长期避免"Agent 决策不可解释"的合规风险 (EU AI Act 2026 高风险系统评估要求);
  - 研究路径选择: 天道推演三沙盘分支 (Agent 因果评估 / 表示工程×营销知识图谱 / 人机协作治理) 中, 哪条最优? 贝叶斯后验概率如何更新?

---

## guest_lecture

**客座讲座**

- **topic (主题)**: "LLM-Assisted Systematic Literature Review in Industrial R&D: From PRISMA 2020 to DeepSeek-V3 + RAGAS in 8 Weeks"
- **speaker_profile (主讲人画像)**: Dr. 一位 McKinsey QuantumBlack 的 Senior Data Science Research Lead (10+ 年咨询研究经验, 曾主导 30+ 客户项目的行业综述, 2025 年起内部推动 DeepSeek-V3 + RAGAS + ASReview 流水线, 在 NeurIPS Datasets & Benchmarks / ICML Workshop 发表过 LLM 辅助综述相关论文)。
- **讲座内容钩子**: (a) 工业级 PRISMA 流水线 vs 学术 PRISMA 的差异 (规模/速率/审计); (b) DeepSeek-V3 vs GPT-4 在文献摘要提取的成本/质量权衡 (1/10 成本, ~95% GPT-4 水平); (c) RAGAS faithfulness/context_precision 评估 LLM 综述质量; (d) ASReview 主动学习如何把人工复核量降至前 20%; (e) 天道推演如何作为研究路径选择的元认知沙盘。

---

## internship_pointer

**实习/驻留指针**

- **机构**: OpenAI Residency (12 周) / Anthropic Residency (12-24 周) / Google AI Resident (18 个月) / McKinsey QuantumBlack Data Science Internship (10-12 周) / Hugging Face Research Internship (6 个月)
- **角色**: Research Engineer (LLM-Assisted Research Tools) / Research Scientist (Evaluation & Alignment) / Data Science Consultant (AI Marketing Agent Causal Evaluation)
- **衔接 (本单元如何为该角色做准备)**:
  - **技术衔接**: 本单元 PRISMA 160->126->59->59 流程 + pydantic Schema + arxiv.py 真实查询 = LLM 辅助研究工具的核心组件 (检索 + 结构化 + 校验), 直接对应 OpenAI/Anthropic Residency 的"LLM-Assisted Research"方向;
  - **方法论衔接**: DSR (Hevner 2004) + PRISMA 2020 + 天道推演 + 贝叶斯推断 = 研究方法论栈, 对应 Google AI Resident / McKinsey QuantumBlack 的"可复现研究 + 决策推演"双重能力;
  - **领域衔接**: AI 营销 Agent 因果评估是 Hugging Face / Salesforce Einstein / Adobe Sensei 等企业的真实业务场景, 本单元 DSR 问题定义书 + 研究空白分析 (Agent 因果评估框架缺失) 即面试时的 portfolio;
  - **下一步**: Phase 2 (数据表示与知识图谱) + Phase 4 (因果验证与实验) 将深化上述衔接, 完整 Capstone (Phase 1-6) 即 Residency 申请的完整 research artifact。

---

*industry.md v7.0 · 产业链接层 · 不破坏 v5.0/v6.0 基线 · 2026-07-26*
