# industry.md · Day 6 IMRaD 论文写作 · 产业链接层 (v7.0)

> 本单元产出产业链接：把 IMRaD 论文写作 (arxiv 拆解 + statsmodels 统计 + LLM-as-a-judge 评估) 与真实企业 / 咨询项目 / 教学案例 / 客座讲座 / 实习指针连接。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **OpenAI** | LLM-as-a-judge (arXiv 2306.05685) 默认 judge = GPT-4；Day 6 写作评估的闭源基线。其 API 被 starter.ipynb 用于评分 IMRaD 各部分。 | GPT-4 作 judge 评估营销研究报告写作质量；Evals 平台可托管自定义 IMRaD criteria。 |
| **Anthropic** | 三 judge 投票配置中的第二 judge (Claude)；其 Constitutional AI 方法论与"偏差缓解"主题强相关。 | Claude 评估 Discussion 部分局限性诚实度；Constitutional AI 用于审稿 prompt 对齐。 |
| **DeepSeek** | 开源 judge (DeepSeek-V3 / R1) 的提供方；Day 6 前沿点：成本仅 GPT-4 的 1/10，使 CI/CD 集成可行。 | 开源 judge 大批量论文写作自检；多 judge 投票缓解单模型偏差。 |
| **Salesforce Einstein** | 营销 Agent vs 人工策略 A/B 测试 (N=400) 的产业对应--其 Einstein Marketing Cloud 部署营销 Agent。 | 营销 Agent 效果评估的 IMRaD 报告由 LLM-as-a-judge 自动审稿，加速内部 R&D 报告流转。 |
| **McKinsey** | 企业架构 / 咨询 partner：把"自动 IMRaD 写作 + 评审"打包成企业内部研究方法论服务。 | 为 CPG / 零售客户出"AI 辅助研究报告写作"白皮书 + 部署方案。 |
| **Hugging Face** | 开源 judge 模型托管 (DeepSeek-V3 / Llama) + 评估 leaderboard；本单元可复用其 evaluation-harness。 | IMRaD 写作评估 leaderboard；FAIR 数据集托管。 |

---

## deployment_example

**部署场景：Salesforce Einstein Marketing Cloud 内部研究报告流水线 (合理场景)**

- **规模**：营销 Agent 团队每月产出 ~200 份 A/B 测试 IMRaD 报告 (营销 Agent vs 人工策略)；人工审稿 SLA = 5 工作日 / 份，积压严重。
- **约束**：① 隐私合规 (客户数据脱敏后才能送 judge)；② 成本上限 (单月 judge API 预算 < $5k)；③ 偏差可控 (人工抽检 10% 校准)。
- **方法**：starter.ipynb 的 pipeline 部署为内部 Airflow DAG--研究员用 statsmodels 跑 t / Cohen's d / χ²，自动生成 APA 第 7 版 Results 段；LLM-as-a-judge (GPT-4 + DeepSeek-V3 + Claude 三 judge 投票) 按四部分 criteria 评分；评分 <3 分的段自动回退人工审稿。
- **效果 (预期)**：审稿 SLA 从 5 天 -> 8 小时；judge API 月成本 ~$3.2k (DeepSeek-V3 占 70% 用量，1/10 成本压低总成本)；位置偏差通过段落顺序随机化降低 ~40%；人工抽检一致率 ρ≈0.78。

---

## consulting_project

**Imperial MSc BA 风格咨询项目 (8 周, 4-5 人)**

- **Partner (赞助企业)**：Salesforce Einstein Marketing Cloud (营销 Agent 团队)。
- **Problem (真实业务问题)**：营销 Agent vs 人工策略的 A/B 测试报告 (N=400 量级) 每月积压，人工审稿慢且不一致；需建一个自动 IMRaD 写作评估 pipeline，并量化 LLM-as-a-judge 的偏差与成本权衡。
- **Data (企业提供数据)**：脱敏的 200 份历史 A/B 测试报告 (含实验组 / 对照组转化率 + 已有的 IMRaD 文本)；3 位 senior 审稿人历史评分 (作为 ground truth)。
- **Scope**：8 周, 4-5 名 MSc BA 学生。
  - W1-2：用 arxiv 包拆解 ReAct (2210.03629) + LLM-as-a-judge (2306.05685) 文献，建立 IMRaD criteria 评分 rubric。
  - W3-4：用 statsmodels + scipy 重跑历史报告统计检验，验证 APA 第 7 版文本可复现。
  - W5-6：接入 GPT-4 + DeepSeek-V3 + Claude 三 judge，跑 200 份报告，计算 Spearman ρ + 偏差指标。
  - W7-8：偏差缓解 (随机化 + 多 judge 投票 + 人工校准)，写 IMRaD 最终报告。
- **Deliverable**：① 可复现 pipeline (Python notebook + Airflow DAG)；② 偏差分析报告 (APA 第 7 版)；③ 成本-一致性权衡仪表板 (Tableau)；④ 给 Salesforce 的部署建议书。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**：Maya Chen, Head of Marketing Analytics at a DTC brand (虚构), 曾在 McKinsey 做过 5 年数据科学顾问，刚读完 Day 6 IMRaD 课程。
- **Decision (关键决策点)**：公司每月产出 50+ 份营销 Agent A/B 测试报告 (类似 N=400 那种)，她要决定是否把内部审稿流程从"3 位 senior 周级人工审"切换为"LLM-as-a-judge 自动评分 + 人工抽检"--三选一：① 单 GPT-4 judge；② 单 DeepSeek-V3 (1/10 成本)；③ 三 judge 投票 (GPT-4 + DeepSeek-V3 + Claude)。
- **Tension (核心张力 / 两难)**：
  - 成本 vs 一致性：DeepSeek-V3 单 judge 最便宜但偏差未知；三 judge 最稳但 API 月成本翻 3 倍。
  - 速度 vs 可问责性：自动审稿快但 senior 团队担心"AI 评审 AI 写的报告"形成回音壁 (自我偏好偏差)。
  - 开源 vs 闭源：开源 (DeepSeek) 可自部署保隐私但运维重；闭源 (GPT-4 / Claude) API 简单但数据出域。
  - 教学钩子：学生需用 Day 6 的 statsmodels 重跑统计 + 用 LLM-as-a-judge 量化偏差，给出数据驱动的建议。

---

## guest_lecture

**客座讲座**

- **Topic (主题)**："LLM-as-a-Judge in Production: Bias, Cost, and the Open-Source Frontier"--基于 ReAct (2210.03629) 的 IMRaD 拆解 + 在 Salesforce Einstein 部署自动审稿 pipeline 的经验。
- **Speaker Profile (主讲人画像)**：Dr. Lianmin Zheng (LLM-as-a-judge 原论文一作, NeurIPS 2023) 或同等画像的工业界 leader (e.g., Salesforce Einstein Head of AI / DeepSeek 研究员)。背景：做过 LLM 评估 (MT-Bench / Chatbot Arena) 且在工业界部署过自动评审 pipeline；能讲 §5 已知偏差 (位置 / 冗长 / 自我偏好) 的实战缓解 + 开源模型 1/10 成本权衡。
- **衔接本单元**：主讲人 30 min 讲工业部署，30 min 用 Day 6 starter.ipynb 现场演示"用三 judge 评估一份营销 IMRaD 论文"，最后 15 min Q&A。

---

## internship_pointer

**实习 / 驻留指针**

- **机构**：OpenAI Residency (1 年) / Google DeepMind AI Safety Residency / Salesforce Einstein AI Capstone Sponsor / Hugging Face Open Science Resident。
- **角色**：Research Resident - LLM Evaluation & Alignment；具体方向 = LLM-as-a-judge 偏差量化 + 多 judge 投票缓解 + 学术写作评估 benchmark。
- **衔接 (本单元如何为该角色做准备)**：
  - ① Day 6 的 ReAct IMRaD 拆解训练"用代码理解论文结构"--Residency 面试常考 paper reading。
  - ② statsmodels + scipy 的统计检验 (t / Cohen's d / χ²) 是评估 judge 一致性 (Spearman ρ) 的基础。
  - ③ LLM-as-a-judge (2306.05685) 的偏差分析 (位置 / 冗长 / 自我偏好) 直接对应 Residency 项目--本单元 starter.ipynb 是最小可行原型。
  - ④ APA 第 7 版 + 可复现 checklist 训练"研究产出符合 NeurIPS 标准"--Residency 终期需投顶会。
  - ⑤ 三 judge 投票 + DeepSeek 开源 judge 部署经验，衔接 Hugging Face Open Science Resident 的"开源 evaluation harness"工作。

---

## 备注

产业链接遵循 Imperial MSc BA 咨询项目模式 (Burberry / Expedia / J&J 等 partner) + HBS 案例法 + MIT Sloan 行动学习模式。全部企业从公司库挑，真实存在。详见 `notes.md` § 研究产出与产业链接层 (v7.0) 与 `research.md`。
