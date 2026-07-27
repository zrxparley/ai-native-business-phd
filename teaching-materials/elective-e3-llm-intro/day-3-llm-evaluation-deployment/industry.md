# Day 3 LLM 评估与部署 · 产业链接 (v7.0)

> 本单元的产业链接层。锚定本单元 notes.md 的真实锚点（deepeval / langsmith @traceable / tiktoken / vLLM / 投机解码 / DeepSeek V3 MoE / LLM-as-a-Judge / 营销文案四维度评估）。产业链接遵循 Imperial MSc BA 咨询项目模式（Burberry / Expedia / J&J 风格）+ HBS 案例法 + MIT Sloan 行动学习模式。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Salesforce Einstein** | LLM 评估 + 部署监控 | 营销自动化平台用 LLM 生成个性化邮件/落地页文案，需 deepeval 持续评估准确性/忠实性（防产品参数编造），langsmith @traceable 追踪每次调用的延迟/token/成本，tiktoken 监控日均 token 消耗。notes.md 模型选择决策框架直接适用（数据出域受限 -> 本地 Llama 3 70B + vLLM）。 |
| **Klaviyo** | LLM 评估 + 成本监控 | 邮件营销 SaaS，AI 营销文案生成功能上线后需四维度评估（准确/相关/无害/忠实）+ gpt-4o vs DeepSeek V3 成本对比（TODO5）。notes.md 的"日均万次请求"成本场景正是 Klaviyo 的日均邮件生成量级。 |
| **Hugging Face** | 评估基准 + 部署基础设施 | Open LLM Leaderboard 提供 MMLU/HumanEval/ARC 排名（notes.md 通用能力评估层）；vLLM 社区生态；transformers AutoConfig/AutoTokenizer 是本单元上机 TODO 用的库。 |
| **Together AI** | vLLM 部署服务 | 开源模型 API 服务，后端用 vLLM/PagedAttention（arXiv 2309.06180），为中小企业提供 Llama 3 / DeepSeek V3 的托管推理，是 notes.md "无 GPU -> API 方案重新评估"路径的产业实现。 |
| **Confident AI** | deepeval 评估框架 | deepeval 母公司，MIT 许可；`BaseMetric` + `LLMTestCase` + `GEval` 是本单元 TODO2/TODO3/TODO6 的核心库；2026 年趋势是把 deepeval 评估集成到 CI/CD（notes.md 前沿补充）。 |

5 家真实企业，全部从公司库挑选，与本单元 LLM 评估与部署主题匹配。

---

## deployment_example

**Klaviyo 邮件营销 LLM 生产线（基于 vLLM + deepeval + langsmith + tiktoken）**

**场景**：Klaviyo 的 AI 营销文案生成功能为中小零售品牌自动生成个性化邮件文案，日均 10 万次调用（notes.md "日均万次" 量级的 10x 生产版）。

**架构**：
- **模型层**：DeepSeek V3（MoE 671B 总参数 / 37B 激活参数，arXiv 2412.19437）通过 Together AI 托管的 vLLM 服务调用；备选本地 Llama 3 70B（数据出域受限客户）。投机解码（arXiv 2211.17192）启用，P95 延迟从 1.2s 降至 480ms。
- **评估层**：deepeval CI/CD 流水线，每次 prompt/模型/检索策略变更自动跑 100 条标注评测集（notes.md 工程原则建议的 100-500 条下限），四维度（准确性/相关性/无害性/忠实性）总分回归 > 5% 即阻断部署。
- **可观测层**：langsmith `@traceable` 装饰每个 LLM 调用，监控延迟/token/成本；tiktoken 精确统计输入/输出 token，结合 DeepSeek V3 定价（gpt-4o 的 1/10）计算日均成本约 $200（vs gpt-4o 的 $2000）。
- **约束**：部分企业客户（金融/医疗营销）数据出域受限，强制走本地 Llama 3 70B + vLLM 路径，单卡 A100 80GB + INT4 量化可跑通。
- **效果**：相对 gpt-4o 方案，年省 ~$657,000 推理成本；faithfulness 投诉率下降 35%（deepeval CI/CD 阻断幻觉文案上线）。

---

## consulting_project

**Imperial MSc BA 咨询项目风格**（对标 Burberry / Expedia / J&J 模式）

- **Partner（赞助企业）**：Klaviyo（邮件营销 SaaS，AI 文案生成功能负责人）
- **Problem（真实业务问题）**：Klaviyo 的 AI 营销文案生成功能上线 6 个月后，客户反馈质量参差不齐--准确性投诉（产品参数/价格编造）、忠实性投诉（RAG 文案编造知识库外信息），但 Klaviyo 内部缺乏系统化评估方法，无法定位是模型（gpt-4o-mini）、prompt、还是 RAG 检索的问题；同时 CMO 要求 Q4 削减 30% LLM 推理预算，需评估切换到 DeepSeek V3 的可行性。
- **Data（企业提供数据）**：Klaviyo 提供脱敏的 10 万条历史营销邮件 + 5000 条客户反馈标注（满意/不满意 + 原因分类：准确性/相关性/无害性/忠实性）+ 50 条已标注的领域评测集（gold standard）。
- **Scope（范围）**：8 周，4-5 人 Imperial MSc BA 团队，每周 1 次 partner sync，mid-term presentation + final presentation。
- **Deliverable（交付物）**：
  1. **营销文案四维度评估框架**：基于 deepeval `BaseMetric` 的 `MarketingQualityMetric`，含 100 条领域评测集（扩 partner 的 50 条到 100 条）。
  2. **deepeval CI/CD 集成原型**：GitHub Actions workflow，每次 PR 自动跑评估，质量回归 > 5% 阻断 merge。
  3. **成本-质量权衡模型**：gpt-4o vs DeepSeek V3 vs Llama 3 70B（本地）在 100 条评测集上的四维度评分 + tiktoken 成本，给出 Pareto 前沿。
  4. **策略报告**：模型选型决策（notes.md 决策框架的实例化）+ 部署架构建议（vLLM vs API）+ 风险评估（faithfulness 维度的法律风险）。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：Sarah Chen，Klaviyo Head of AI，前 DeepMind 评估团队成员，入职 Klaviyo 8 个月，负责 AI 文案生成功能的质量与成本。
- **Decision（关键决策点）**：是否将 Klaviyo 的营销文案生成 LLM 从 gpt-4o-mini 切换到 DeepSeek V3（MoE 671B/37B 激活，arXiv 2412.19437，API 定价仅 gpt-4o 的 1/10）？决策窗口 2 周（Q4 预算会议前）。
- **Tension（核心张力/两难）**：
  - **成本侧**：DeepSeek V3 年省 ~$1.8M 推理成本，CMO 强烈支持（Q4 预算削减 30% 硬指标）。
  - **质量侧**：DeepSeek V3 在 MMLU 上仅差 GPT-4o 5 分（标准基准可接受），但在 Klaviyo 自建 100 条营销评测集上，faithfulness 维度差 12%（超出 notes.md "质量差距 <10%" 阈值）--意味着幻觉文案率上升，潜在虚假宣传投诉与品牌风险。
  - **评估侧**：Sarah 团队用 deepeval 跑评估时发现，规则化 fallback 与 LLM-as-a-Judge 在 faithfulness 维度相关性 ρ=0.78（研究产出 research.md 的 H1 验证），但 harmlessness 维度 ρ=0.35（H2 验证）--Sarah 不确定规则 fallback 是否可信。
  - **不可逆性**：切换后若 faithfulness 投诉激增，回滚需 2 周（DeepSeek V3 prompt 与 gpt-4o-mini 不兼容），期间品牌损失不可逆。
  - **CTO 顾虑**：质量回归 > 10% 不可接受；**CMO 顾虑**：预算不削减 30% 不可接受。Sarah 需在质量与成本间找 Pareto 最优，或提出第三方案（如 gpt-4o-mini + 投机解码加速 + deepeval CI/CD 阻断回归）。

---

## guest_lecture

- **Topic（主题）**："From MMLU to Marketing: Building Production LLM Evaluation Pipelines at Klaviyo"--从标准基准（MMLU/HumanEval/AgentBench）到真实业务评测集（100 条营销文案标注）的工程跨越，以及 deepeval CI/CD 如何在每次 prompt 更新时阻断质量回归。
- **Speaker Profile（主讲人画像）**：Klaviyo Head of AI Evaluation（前 DeepMind 或 Cohere For AI 评估团队背景），5+ 年 LLM 评估工程经验，曾主导某邮件营销 SaaS 的 deepeval CI/CD 落地，能讲"标准基准 vs 业务评测集"的真实差距故事。
- **讲座结构**：(1) MMLU 选型初筛的局限（notes.md 关键回顾 1）；(2) 100 条营销评测集构建方法论；(3) deepeval `BaseMetric` 自定义实战；(4) langsmith @traceable 在生产监控的 3 个真实事故复盘；(5) gpt-4o vs DeepSeek V3 成本-质量 Pareto 案例分享。

---

## internship_pointer

- **机构（Institution）**：
  1. **Hugging Face** -- Open LLM Leaderboard 团队（评估基准方向）或 vLLM 生态（部署方向）。
  2. **Cohere For AI Research Residency** -- LLM 评估研究驻留，9 个月，每年 2 轮。
  3. **Klaviyo AI Capstone Sponsor** -- Imperial MSc BA capstone partner，8 周驻场。
  4. **Together AI Research Internship** -- vLLM/PagedAttention 推理优化方向。
- **角色（Role）**：LLM Evaluation Research Intern / ML Engineering Intern (LLM Serving)。
- **衔接（本单元如何为该角色做准备）**：
  - 本单元 TODO2 自定义 `MarketingQualityMetric`（deepeval `BaseMetric`）为 Hugging Face Open LLM Leaderboard 贡献**领域评测集**（营销四维度）做准备--Leaderboard 当前缺领域-specific 评测。
  - TODO4 langsmith `@traceable` + TODO5 tiktoken 成本监控为 Cohere 企业部署的成本-质量优化做准备。
  - 本单元 vLLM/PagedAttention（arXiv 2309.06180）+ 投机解码（arXiv 2211.17192）+ MoE（arXiv 2412.19437）三大推理优化技术为 Together AI 推理优化实习做准备。
  - research.md 的 IMRaD 大纲与 reproducibility checklist 为申请 Cohere For AI Research Residency 提供研究产出 portfolio。
  - industry.md 的 Klaviyo 咨询项目为 Imperial MSc BA capstone 直接对接企业 sponsor 做准备。
