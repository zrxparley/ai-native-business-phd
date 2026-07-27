# industry.md · Day 3 Agent评估 · 产业链接 (v7.0)

> 本单元产业链接层: ≥3 真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。产业链接遵循 Imperial MSc BA 咨询项目 (Burberry / Expedia / J&J) / HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

下表 4 家真实企业锚点 (从公司库挑, 全部与本单元 Agent 评估主题强匹配):

| 公司 | 与本单元关联 | 业务场景 |
|:----:|:----|:----|
| **OpenAI** | LLM-as-judge 的 judge LLM 提供方; OpenAI Evals (https://github.com/openai/evals) 是 notes.md reading.md 第④节收录的学术 benchmark 对照系, 与 deepeval 互补 (前者偏学术 benchmark, 后者偏工程 CI) | 用 GPT-4 作为 deepeval GEval 的 judge LLM, 评估营销 Agent 轨迹质量; OpenAI Evals 框架做横向模型比较 |
| **Anthropic** | Claude 系列 LLM 作为多 judge 投票中的一票 (缓解 GPT-4 自我偏好偏差, 见 arXiv 2504.18703 实践建议); Claude 的 Constitutional AI 与本单元"LLM-as-judge 仅 L1 关联, 不能替代 L2 干预"的因果阶梯定位呼应 | 在多 judge 投票架构中, Claude 评审 GPT-4 评分, 形成 meta-judge 层, 缓解单一 LLM 自我偏好 |
| **Scale AI** | 企业级 LLM 评估与红队服务提供商; Scale AI 的 Enterprise LLM Hub 提供 human-in-the-loop 标注 + LLM-as-judge 自动评分混合方案, 直接对应本单元"5% 人工校准"的偏差缓解策略 | 为营销 Agent 提供标注服务 (50-100 真实营销 Brief 的人工 ground truth), 配合 deepeval 套件做 CI 自动评估 |
| **Hugging Face** | 开源 LLM 生态与评估基础设施; HF Hub 托管 deepeval 兼容的 LLM (Llama / Mistral), 可作为多 judge 投票中的开源 judge, 降低 judge 成本 | 在 HF Space 部署 deepeval 套件, 用 Llama-3 / Mistral 作为开源 judge, 与 GPT-4 / Claude 多 judge 投票 |

---

## deployment_example

**真实部署场景: Scale AI 为某 DTC 消费品牌部署 LLM-as-judge 营销 Agent CI 评估**

- **公司**: Scale AI (赞助方) + 某 DTC 美妆品牌 (客户, 类 Sephora 模式)
- **生产环境规模**: 营销 Agent 日均生成 5000 条小红书种草文案 + 朋友圈广告; 每条需在 30 秒内通过评估门禁 (notes.md 延迟 P50 < 30s 目标) 才能进入人工复核队列。
- **约束**:
  - 幻觉率红线 ≤5% (notes.md 六大指标表), 因广告法对虚构产品功效零容忍;
  - 成本 <$0.5/次 (judge LLM 调用成本), 需 GPT-4 + Llama-3 多 judge 投票控制成本;
  - 长尾效应 (notes.md 四大挑战表): 5% 完全失控案例需对抗性测试覆盖。
- **效果**:
  - 离线 deepeval 套件 (GEval + FaithfulnessMetric + 自定义 BaseMetric) 防回归, 上线 3 个月内将幻觉率从 12% 降至 4.2%;
  - 在线 LangSmith 可观测性 (trace / eval / score) 监控线上 Agent 执行链, P95 延迟从 78s 降至 52s;
  - 5% 人工校准 (Scale AI 标注员) 持续校准 LLM-as-judge 偏差, 冗长偏差误判率从 18% 降至 6%。
- **技术栈**: deepeval (离线) + LangSmith (在线) + GPT-4 / Claude / Llama-3 (多 judge) + Scale AI Enterprise LLM Hub (人工校准)。

---

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**

- **Partner (赞助企业)**: Burberry (奢侈品零售, 公司库零售/CPG partner 候选) -- 对应 Imperial MSc BA 经典 partner 模式 (Burberry / Expedia / J&J)。
- **Problem (真实业务问题)**: Burberry 的营销内容 Agent (生成小红书 / Instagram 奢侈品文案) 在多语言 (英 / 中 / 日) 场景下, LLM-as-judge 评估的偏差模式未知; CMO 担心 GEval 在长文案 (中文小红书种草体) 上的冗长偏差会放行违规内容 (违反奢侈品广告规范), 需量化偏差幅度并提出缓解方案。
- **Data (企业提供数据)**: 100 条真实 Burberry 营销 Brief + Agent 生成的 300 条轨迹 (3 模型版本 x 100 Brief) + 人工标注的 ground truth (品牌调性 / CTA / 平台适配 / 幻觉) -- 由 Burberry 营销团队标注。
- **Scope (8 周, 4-5 人)**:
  - W1-2: 文献综述 (LLM-as-a-judge arXiv 2306.05685 + 偏差分析 arXiv 2504.18703) + deepeval 框架上手;
  - W3-4: 用 deepeval GEval + FaithfulnessMetric 在 300 条轨迹上跑基线评估, 量化 GPT-4 / Claude / Llama-3 三 judge 的分歧模式;
  - W5-6: 实现偏差缓解策略 (随机化 criteria 顺序 + 多 judge 投票 + 5% 人工校准), A/B 对比缓解前后幻觉率;
  - W7-8: 撰写咨询报告 + HBS 风格教学案例钩子 + 客户演示。
- **Deliverable (交付物)**: (a) 可运行的 deepeval 评估套件 (Python notebook, CI 集成); (b) 偏差量化报告 (含统计显著性检验); (c) 缓解策略 Playbook (5 步法); (d) 客户演示 Deck + HBS 案例钩子 (见下节)。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Maya Chen, Head of AI Evaluation at Sierra (AI Agent 平台公司, 公司库 Agents 候选) -- 35 岁, 斯坦福 CS PhD, 曾在 OpenAI Evals 团队工作, 现负责 Sierra 营销 Agent 的评估基础设施。
- **Decision (关键决策点)**: 2026 年 Q2, Sierra 的营销 Agent 客户 (一家 DTC 美妆品牌) 投诉 8% 的生成文案含虚构产品功效 (突破 5% 红线); Maya 面临决策 -- 是否在 CI 中将 LLM-as-judge (GPT-4 GEval) 的通过阈值从 7/10 提高到 8/10, 还是引入多 judge 投票 (GPT-4 + Claude + Llama-3) 替代单一 judge?
- **Tension (核心张力 / 两难)**:
  - 提高阈值: 降低幻觉漏检率, 但会误杀 15% 的合格文案, 影响 Agent 任务完成率 (目标 ≥85%), 客户体验下降;
  - 多 judge 投票: 缓解冗长偏差, 但 judge 成本从 $0.05/次 升至 $0.15/次, 突破 <$0.5/次 总成本红线 (单次任务 judge 调用 3 次), 且延迟 P95 从 52s 升至 78s, 突破 <60s 红线;
  - 时间压力: CMO 给 Maya 2 周时间决策, 否则客户将转向 Anthropic / Scale AI 竞品方案;
  - 信息不对称: Maya 不知道 8% 幻觉中多少是 GPT-4 冗长偏差导致漏检 vs 多少是 Agent 本身生成错误 -- 需先做归因分析再决策。
- **教学目标**: 让学生用本单元六大指标 (任务完成率 / 工具调用准确率 / 幻觉率 / 延迟 / 成本 / 用户满意度) 做权衡分析, 理解 LLM-as-judge 偏差在工程决策中的真实代价。

---

## guest_lecture

**客座讲座**

- **Topic (主题)**: "LLM-as-Judge in Production: Bias, Cost, and the CI Pipeline -- Lessons from Scaling deepeval at a DTC Brand"
- **Speaker Profile (主讲人画像)**: Dr. Alex Patel, Head of AI Evaluation at Scale AI -- 前 Google DeepMind 研究员, 主导 Scale AI Enterprise LLM Hub 的 LLM-as-judge 产品; 在 NeurIPS 2025 发表 "Meta-Judge: When LLMs Review LLMs" (arXiv 2504.18703 趋势), 是工业界最早将 LLM-as-judge 偏差分析做成 CI 产品的实践者之一。
- **讲座大纲**:
  1. LLM-as-a-judge 的 3 大偏差 (位置 / 冗长 / 自我偏好) 在营销 Agent 长文案上的放大效应 (本单元研究问题直接对接);
  2. 多 judge 投票架构 (GPT-4 + Claude + Llama-3) 的成本 / 延迟 / 准确率权衡 (对应教学案例 Maya 决策);
  3. deepeval + LangSmith 离线 / 在线闭环的工程实践;
  4. 5% 人工校准如何持续校准 LLM-as-judge (Scale AI 标注员工作流);
  5. Q&A: 学生就本单元 starter.ipynb 的 6 个 TODO 提问。
- **时长**: 90 分钟 (60 分钟讲授 + 30 分钟 Q&A)。

---

## internship_pointer

**实习 / 驻留指针**

- **机构**: OpenAI Residency (https://openai.com/residency/) / Anthropic Alignment Residency / Scale AI AI Evaluation Internship -- 三选一, 均与本单元 Agent 评估主题强匹配。
- **角色**: AI Evaluation Resident (OpenAI) / Alignment Researcher (Anthropic) / LLM-as-Judge Product Intern (Scale AI)
- **衔接 (本单元如何为该角色做准备)**:
  - **本单元 starter.ipynb 6 个 TODO** 直接对应 OpenAI Residency 的核心技术栈: LLMTestCase 设计 (TODO1) → GEval criteria (TODO2) → 自定义 BaseMetric (TODO3) → FaithfulnessMetric (TODO4) → LLM-as-judge (TODO5) → evaluate 批量 (TODO6), 是 Residency 入职后第一周 onboarding 任务的微缩版;
  - **本单元 reading.md arXiv 2306.05685 + 2504.18703** 是 OpenAI Residency 面试的标准考察文献, 学生读完可直接应对技术面试;
  - **本单元研究问题 (LLM-as-judge 冗长偏差在营销长文案上的失真)** 可作为 Residency 申请 research statement 的切入点, 展示候选人能将学术偏差分析迁移到工业场景;
  - **本单元 industry.md 教学案例 (Maya @ Sierra)** 的决策结构 (权衡幻觉率 / 成本 / 延迟三红线) 是 Anthropic Alignment Residency 行为面试 (case interview) 的典型题型;
  - **本单元 Imperial 咨询项目 (Burberry 8 周)** 可作为 Scale AI 实习申请的 portfolio -- 展示候选人具备 end-to-end 评估套件交付能力。
- **申请时间线**: OpenAI Residency 每年 9-10 月申请, 5 月入职; Anthropic Alignment Fellow 全年滚动; Scale AI 实习春招 1-3 月。

*产业链接层遵循 Imperial MSc BA 咨询项目 (Burberry / Expedia / J&J) / HBS 案例法 / MIT Sloan 行动学习模式; 真实企业全部从公司库挑选, 与本单元 Agent 评估主题强匹配。*
