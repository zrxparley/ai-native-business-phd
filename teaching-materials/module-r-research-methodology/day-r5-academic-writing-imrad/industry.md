# R5 产业链接层 (v7.0)

> 本单元 IMRaD 学术写作方法论的产业落地。从公司库挑 >=3 真实企业，锚定 LLM-as-a-judge 自动评审 / IMRaD 写作规范 / A/B 测试报告 APA 格式三条主线。遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

>=3 家真实企业锚点 (从公司库挑，与本单元 IMRaD 写作 + LLM-as-a-judge 主题匹配)：

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **OpenAI** | LLM-as-a-judge 技术来源 (GPT-4 评审)；本单元 notes.md §2026 前沿核心引用 | 提供 GPT-4 API 作为 IMRaD 写作评审 judge；企业用 OpenAI API 构建投稿前自检工具，CI/CD 集成论文结构完整性检查 |
| **Anthropic** | Claude 作为异构 judge (缓解同源偏差)；Constitutional AI 与写作伦理对齐 | Claude 评估学术论文 Discussion 节的局限性诚实度与伦理声明合规性；企业用 Claude 做 LLM-as-a-judge 多 judge 投票的异构成员 |
| **McKinsey** | 咨询报告 IMRaD 化 (Introduction 漏斗结构 / Methods 可复现性) | 内部研究写作规范白皮书；将 IMRaD 方法论迁移到咨询报告 (problem -> approach -> findings -> implications 四段式) |
| **DeepSeek** | 开源写作评估模型 (成本 1/10)，本单元 notes.md 明确引用 DeepSeek-V3/R1 | 大批量论文写作自检 (CI/CD 集成)；多 judge 投票的低成本成员 |
| **Booking.com** | A/B 测试实验报告 APA 格式 (与 NSW RCT 结构同构) | 实验报告写作规范：t 检验 + Cohen's d + 95% CI 按 APA 第7版报告；LLM-as-a-judge 自动评估实验报告 IMRaD 合规性 |

---

## deployment_example

**真实部署场景：Booking.com 实验报告 LLM-as-a-judge 自动评审流水线**

- **公司**: Booking.com ( experimentation 文化知名，与 Microsoft ExP / Netflix 类似)
- **业务场景**: Booking.com 每年运行 >1000 个 A/B 测试，每个实验需撰写 IMRaD 风格实验报告 (Introduction 漏斗 -> Methods 实验设计 -> Results 统计报告 -> Discussion 业务启示)。人工评审每份报告需 2-3 小时，且评审质量不一致。
- **部署规模**: 1000+ 报告/年，50+ 数据科学家提交报告。
- **约束**:
  - 评审需符合 APA 第7版统计报告格式 (t/df/p/d/CI 全报告)。
  - LLM-as-a-judge 已知偏差 (位置/冗长/自我偏好, arXiv 2504.18703) 必须缓解。
  - 实验数据含 PII (用户预订信息)，不能直接发给 LLM API。
- **效果 (合理估计)**:
  - 评审周期从 2-3 小时降至 15-20 分钟 (LLM 初筛 + 人工 1 小时校准)。
  - position bias 通过段落顺序随机化 (ABC/BCA/CAB 三组) + 3 judge (GPT-4 + DeepSeek-V3 × 2) 多数投票降至 < 15%。
  - APA 格式合规率从 72% 提升至 96% (LLM 自动检测缺失的 d / CI 报告)。
- **关键设计**: LLM 评审定位为"投稿前/内部评审前自检工具"，对应因果阶梯 L1 (关联)，不替代人工评审 (L2 干预: 修改后重新提交)。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (参考 Imperial MSc BA 与 Burberry/Expedia/J&J 合作模式)：

- **Partner (赞助企业)**: Booking.com (Experimentation Team)
- **Problem (真实业务问题)**: Booking.com 内部 A/B 测试实验报告质量参差--部分数据科学家未按 APA 第7版报告效应量与 CI，Introduction 漏斗结构不连贯，Discussion 局限性不诚实。需要一个自动化评审工具提升报告质量一致性。
- **Data (企业提供数据)**: Booking.com 提供 200 份脱敏历史实验报告 (含人工评审评分作为 ground truth) + 50 份新报告 (用于 LLM 评审验证)。所有 PII 已脱敏，符合 GDPR。
- **Scope (项目周期与团队)**: 8 周，4-5 人 Imperial MSc BA 学生团队。
- **Deliverable (交付物)**:
  1. **原型**: LLM-as-a-judge 评审原型 (Python + OpenAI/DeepSeek API)，按 IMRaD checklist (Introduction 清晰度 / Methods 可复现性 / Results 统计严谨 / Discussion 诚实度) 自动打分。
  2. **模型**: 3 judge 多数投票 + 段落顺序随机化的偏差缓解模型；评估指标: 与人工评分 Spearman ρ ≥ 0.7。
  3. **策略**: 内部实验报告写作规范白皮书 (基于本单元 notes.md 的 IMRaD 四要素 + APA 第7版)。
  4. **报告**: Imperial MSc BA capstone 报告 (IMRaD 格式，20 页) + Booking.com 内部 presentation。
- **衔接**: 本单元 starter.ipynb TODO1-6 (arxiv 下载论文 + NSW t 检验 + LLM-as-a-judge checklist) 直接为该项目提供代码起点。

---

## case_study

**HBS 风格教学案例钩子** (参考 HBS case method "protagonist + decision + tension" 三要素)：

- **Title (钩子)**: *"Should Booking.com Trust LLM-as-a-Judge for Experiment Report Quality?"*
- **Protagonist (主角)**: Dr. Lena Müller, Head of AI Research at Booking.com (前学术界实验经济学家，转型工业界 5 年)。
- **Decision (关键决策点)**: 是否将 LLM-as-a-judge 评审流水线 (3 judge 投票 + 段落随机化) 从"投稿前自检工具"升级为"实验报告强制评审关卡"--所有数据科学家提交报告前必须通过 LLM 评审，否则无法进入人工评审队列。
- **Tension (核心张力/两难)**:
  - **效率侧**: 评审周期从 2-3 小时降至 20 分钟，释放 2 名资深数据科学家做更高价值工作；APA 格式合规率从 72% 升至 96%。
  - **风险侧**: LLM-as-a-judge 已知偏差 (arXiv 2504.18703) 可能系统性低估某些创新性论证路径 (如非标准漏斗结构的 Introduction)；过度依赖 LLM 评审可能让数据科学家"为 LLM 写作"而非"为人类读者写作"；GDPR 合规风险 (脱敏数据仍可能被 LLM 记忆)。
  - **认知侧**: Lena 在学术界的经验告诉她，最好的论文常常打破格式规范 (如 ReAct arXiv 2210.03629 的 Methods 节占比异常高 42%)。强制 LLM 评审可能扼杀创新。
- **教学目标**: 让学生理解 LLM-as-a-judge 的能力边界 (L1 关联 vs L2 干预)、IMRaD 规范的弹性、以及 AI 评审工具的组织采纳决策。
- **配套数据**: 本单元 NSW 数据 (N=445) + ReAct/LLM-as-a-judge/GraphRAG 三篇 arXiv 论文作为案例附录。

---

## guest_lecture

**客座讲座** (与本单元 IMRaD 写作 + LLM-as-a-judge 主题匹配)：

- **Topic (主题)**: *"LLM-as-a-Judge in Production: Biases, Mitigations, and the Limits of Automated Peer Review"*
- **Speaker Profile (主讲人画像)**: Dr. Lianhui Zheng (或同级人物), Senior Research Scientist at OpenAI (或 Anthropic)，LLM-as-a-judge 原论文 (arXiv 2306.05685) 共同作者，现任 OpenAI/Anthropic 内部"AI 评审系统"团队负责人。
- **讲座大纲** (90 分钟):
  1. (20 min) LLM-as-a-judge 范式回顾: MT-Bench / Chatbot Arena 到学术写作的迁移。
  2. (20 min) 三类已知偏差 (位置/冗长/自我偏好) 的实证证据 (arXiv 2504.18703)。
  3. (25 min) 缓解策略: 多 judge 投票 + 段落随机化 + 人工校准 (本单元 research.md H1 的工业实践)。
  4. (15 min) 因果阶梯定位: LLM-as-a-judge 是 L1 关联工具，不替代 L2 真实同行评审。
  5. (10 min) Q&A: 学生提问 (结合本单元 TODO6 的 LLM-as-a-judge 模拟器)。
- **衔接**: 讲座前学生需完成 starter.ipynb TODO6 (构建 LLM-as-a-judge checklist) + 阅读 arXiv 2306.05685 §3, §5。

---

## internship_pointer

**实习/驻留指针** (为本单元学生指明产业衔接路径)：

- **机构 1: OpenAI Residency (1 年)**
  - **角色**: AI Research Resident, Evaluation & Alignment 团队
  - **衔接**: 本单元的 LLM-as-a-judge checklist 构建 + 偏差分析 (TODO6) + NSW 数据统计报告 (TODO4) 为 Residency 的"评估方法论"核心技能做准备。Residency 申请材料可用本单元 research.md 的 IMRaD 大纲作为写作样本。
- **机构 2: Anthropic Alignment Residency**
  - **角色**: Alignment Researcher, Constitutional AI 团队
  - **衔接**: 本单元 Discussion 节的"伦理声明"写作 + LLM-as-a-judge 偏差分析直接对应 Anthropic 的 Constitutional AI 对齐研究。学生可基于本单元 research.md 的 H1 (多 judge 投票降偏差) 作为 Anthropic Residency 研究提案起点。
- **机构 3: McKinsey Analytics (Capstone Sponsor)**
  - **角色**: Analytics Summer Associate / Capstone Sponsor
  - **衔接**: 本单元的 IMRaD 写作规范 + 咨询项目 (industry.md §consulting_project) 为 McKinsey 内部"研究白皮书"写作做准备。McKinsey 内部白皮书遵循类似的 problem -> approach -> findings -> implications 四段式 (与 IMRaD 同构)。
- **机构 4: DeepSeek (开源 LLM 团队)**
  - **角色**: Research Intern, Evaluation Team
  - **衔接**: 本单元 notes.md 明确引用 DeepSeek-V3/R1 作为低成本写作评估模型；学生可申请 DeepSeek 实习，参与"开源 LLM 作为学术写作 judge"的开源项目。
- **机构 5: Hugging Face (开源 ML 平台)**
  - **角色**: ML Engineer Intern, Evaluation & Leaderboards
  - **衔接**: Hugging Face Open LLM Leaderboard 使用 LLM-as-a-judge 评估模型质量；本单元的 IMRaD 评估 checklist 可迁移到 Leaderboard 评估方法论。

---

## 与本单元教学目标的衔接

本产业链接层与本单元 5 个学习目标 (notes.md §学习目标) 衔接：
- **LO1** (arxiv 下载 + IMRaD 分类) -> industry.md §real_companies 的 OpenAI / arXiv 论文分析
- **LO3** (NSW t 检验 + APA 第7版) -> industry.md §consulting_project 的 Booking.com 实验报告
- **LO5** (LLM-as-a-judge 同行评审) -> industry.md §deployment_example 的自动评审流水线
- **LO2/LO4** (Introduction 漏斗 + Title/Abstract) -> industry.md §case_study 的 HBS 教学案例

产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。研究产出详见 `research.md`。
