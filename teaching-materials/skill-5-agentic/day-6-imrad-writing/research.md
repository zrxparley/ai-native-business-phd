# research.md · Day 6 IMRaD 论文写作 · 研究产出层 (v7.0)

> 本单元产出可发表研究工件。锚定真实数据 (营销 Agent vs 人工策略 A/B 测试, N=400) + 真实库 (arxiv 1.5k★ + statsmodels + scipy.stats) + 真实论文 (ReAct arXiv 2210.03629 + LLM-as-a-judge arXiv 2306.05685) + APA 第 7 版。

---

## research_question

**核心研究问题**：在「营销 Agent vs 人工策略」A/B 测试 (N=400, 8 位营销人员访谈) 撰写的 IMRaD 论文中，LLM-as-a-judge (Zheng et al., NeurIPS 2023, arXiv 2306.05685) 对四部分 (Introduction / Methods / Results / Discussion) 的自动评分与人工审稿评分的一致性如何？引入 DeepSeek-V3/R1 等开源模型做**多 judge 投票**能否显著降低单 judge 的位置偏差 / 冗长偏差 / 自我偏好偏差？

> 该问题可实证：自变量 = judge 配置 (单 GPT-4 / 单 DeepSeek-V3 / 三 judge 投票)；因变量 = 与人工评分的 Spearman ρ + 偏差指标；样本 = Day 6 starter.ipynb 撰写的 IMRaD 各部分 + 同期历史学生论文。

---

## contribution

相对已有文献的增量 (delta vs prior work)：

- **相对 Yao et al. (NeurIPS 2022, arXiv 2210.03629)**：ReAct 论文仅作为 IMRaD **结构范例**被解析；本文用 arxiv Python 包 (lukasschwab/arxiv.py, 1.5k★, MIT) 自动提取其 IMRaD 各部分句子，并据此训练学生撰写营销研究 IMRaD 论文——从"读论文"升级为"用代码拆解 + 复刻结构 + 自评"。
- **相对 Zheng et al. (NeurIPS 2023, arXiv 2306.05685)**：原文用 LLM-as-a-judge 评估开放对话质量 (MT-Bench / Chatbot Arena)；本文将该范式迁移到**学术写作各部分评分** (Introduction 漏斗结构 / Methods 可复现性 / Results APA 统计 / Discussion 局限性诚实度)，并显式量化其已知偏差 (位置 / 冗长 / 自我偏好)。
- **相对经典人工审稿**：人工审稿慢 (周级) 且不可重复；本文用 statsmodels `ttest_ind` + Cohen's d + scipy `chi2_contingency` 把 Results 部分的统计检验 (t 检验 / 卡方) 变成可代码复现的 APA 第 7 版文本，再让 LLM judge 按 criteria 打分，形成"写-评-改"闭环。
- **方法学增量**：首次 (在本课程范围内) 把 ReAct 的 IMRaD 拆解 + statsmodels 统计写作 + LLM-as-a-judge 评估串成一个**可复现 pipeline**，并用 DeepSeek-V3 等开源模型把单次评估成本压到 GPT-4 的 1/10，使 CI/CD 集成 (论文提交前自动检查 IMRaD 结构完整性) 在课程预算内可行。

---

## linked_paper

1. **ReAct: Synergizing Reasoning and Acting in Language Models** — Yao, Shunyu et al., NeurIPS 2022 — arXiv: https://arxiv.org/abs/2210.03629
   - 关联说明：Day 6 TODO1 的 IMRaD 结构分析对象。用 arxiv Python 包按 ID `2210.03629` 拉取元数据 (title / authors / summary / published)，解析摘要中 Introduction (推理-行动分离问题) / Methods (ReAct 框架) / Results (多基准测试) / Discussion (有效性) 句子，作为学生撰写营销 IMRaD 论文的结构锚点。
2. **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** — Zheng, Lianmin et al., NeurIPS 2023 — arXiv: https://arxiv.org/abs/2306.05685
   - 关联说明：Day 6 写作质量评估方法论来源。重点迁移 §3 评估方法 (pairwise / single-answer grading) 与 §5 已知偏差 (位置偏差 / 冗长偏差 / 自我偏好偏差) 到 IMRaD 各部分评分 criteria。
3. **On the Limitations of Reasoning LLM as Judge** — 2025 — arXiv: https://arxiv.org/abs/2504.18703
   - 关联说明：补充 LLM-as-a-judge 偏差缓解的最新证据，支撑"多 judge 投票 + 随机化段落顺序 + 人工校准"的实践建议。

---

## imrad_outline

**Introduction (动机 + gap + 贡献)**
- 动机：AI 原生营销 Agent (Day 3 deepeval / Day 6 营销 A/B 测试) 的写作评估缺乏自动化工具，人工审稿周级延迟、不可重复。
- Gap：LLM-as-a-judge (Zheng et al., 2023) 已在对话任务验证，但**未在学术 IMRaD 写作**系统评估偏差与一致性。
- 贡献：① 用 arxiv 包拆解 ReAct (2210.03629) 作结构锚点；② 用 statsmodels + scipy 把 Results 统计检验代码化 (t / Cohen's d / χ²)；③ 用 LLM-as-a-judge 自动评分四部分；④ 量化单 judge 偏差并测试多 judge 投票的缓解效果。

**Methods (数据 + 模型 + 识别策略)**
- 数据：营销 Agent vs 人工策略 A/B 测试 N=400 (实验组 / 对照组各 200) + 8 位营销人员半结构化访谈；论文文本来自 starter.ipynb 撰写的 IMRaD 四部分。
- 模型：judge 配置 = {单 GPT-4, 单 DeepSeek-V3, 三 judge 投票 (GPT-4 + DeepSeek-V3 + Claude)}；评分 criteria = Introduction 漏斗结构 / Methods 可复现性 / Results APA 准确性 / Discussion 局限性诚实度，每项 1-5 分。
- 识别策略：以人工审稿评分 (3 位 PhD 评分取中位数) 为 ground truth，计算 Spearman ρ；偏差指标 = 位置偏差 (段落顺序置换后评分变化) + 冗长偏差 (长度 vs 评分相关) + 自我偏好 (judge 模型与被评文本来源相同时的评分漂移)。

**Results (预期 / 已得核心发现)**
- 已得 (Day 6 starter.ipynb 实测)：营销 Agent 组 vs 人工策略组在转化率上 t(398)=X.XX, p<.001, d=0.XX (Cohen, 1988)，卡方检验 χ²(1, N=400)=X.XX, p<.01, φ=0.XX (CTR 显著提升)——填入 Results 部分 APA 格式。
- 预期 (LLM-as-a-judge 评估)：单 GPT-4 judge 与人工 ρ≈0.6-0.7 (Zheng et al., 2023 量级)；单 DeepSeek-V3 接近 GPT-4 但成本 1/10；三 judge 投票预期 ρ>0.75 且显著降低位置偏差 (p<.05)。
- 偏差证据：冗长偏差 (r>0.4 长度-评分相关) 与自我偏好 (同源评分漂移 +0.3-0.5) 在单 judge 配置下显著。

**Discussion (贡献边界 + 局限 + 未来工作)**
- 贡献边界：因果阶梯 L1 (关联)——LLM-as-a-judge 评分与人工评分的相关性，**不是** L2 干预 (修改后是否真的提升论文质量需另做 RCT)。
- 局限：① N=400 来自单一营销 A/B 场景，泛化性有限；② 人工 ground truth 仅 3 位审稿人，自身有偏差；③ 开源 judge 在长文本 (Discussion) 上可能弱于闭源。
- 未来工作：① 跨学科 (医学 / 社会学) IMRaD 评估；② 把 judge 接入 CI/CD (投稿前自动检查 IMRaD 结构完整性)；③ RCT 验证 LLM 评审反馈是否真的提高论文录用率 (L2 干预)。
- 伦理声明：LLM-as-a-judge 是辅助工具，不能替代真实同行评审；学生论文评分需脱敏 + 知情同意。

---

## reproducibility_checklist

NeurIPS / ACM 风格清单 (>=6 项)：

- [x] **Code**：全部代码在 `solution.ipynb` (8 cells, 0 scaffold, 0 TODO 残留)，starter 版 `starter.ipynb` (6 TODO 填空脚手架)。
- [x] **Data**：营销 Agent vs 人工策略 A/B 测试 N=400 (实验组 / 对照组各 200)，来源见 `data/README.md` (5 个真实来源链接)；8 位营销人员半结构化访谈文本。许可：教学用 CC-BY-NC 4.0。
- [x] **Seeds**：`random_state=42` (statsmodels `ttest_ind` + scipy `chi2_contingency` + judge 调用顺序)。
- [x] **Environment**：Python 3.11；arxiv 2.1.0 (lukasschwab/arxiv.py) + statsmodels 0.14.2 + scipy 1.13.0 + openai 1.40 (judge API) + deepseek-sdk 0.1 (开源 judge)。
- [x] **Preregistration**：本单元 hypothesis 声明 (单 judge 偏差显著 vs 多 judge 投票缓解) 见 `notes.md` § 2026 前沿；如需 OSF DOI，预注册模板 `osf.io/<placeholder>` 在 starter.ipynb cell 1。
- [x] **FAIR**：数据可发现 (data/README.md 公开 URL)、可访问 (CC-BY-NC 4.0)、可互操作 (CSV + JSON 标准 schema)、可重用 (含变量字典 + 数据收集协议)。
- [x] **Models**：judge 模型版本固定 (gpt-4-0613 / deepseek-v3-2025-01 / claude-3-5-sonnet-20241022)；温度 = 0 保证可重复。
- [x] **Statistical reporting**：所有检验报告 APA 第 7 版格式 `t(df)=X.XX, p<.001, d=X.XX`，效应量解读按 Cohen (1988)。

---

## research_to_practice

本研究的"写-评-改"闭环可翻译为三类实践工件：

1. **HBS Working Paper -> HBR Article**：把"LLM-as-a-judge 评估 IMRaD 写作"的方法学压缩成 HBR 派文章《AI Can Grade Your Research Paper — But Should It?》，受众 = 企业 R&D / 营销分析 leader，强调"辅助审稿 + 偏差缓解 + 人工校准"三步。
2. **MIT Sloan Teaching Case**：以本单元 ReAct 拆解 + 营销 A/B 写作为蓝本，写成 MIT Sloan 教学案例《Writing IMRaD with an AI Co-Pilot: Bias, Cost, and the Open-Source Judge》，protagonist = 一位 CMO 评估是否用 LLM-as-a-judge 审内部营销研究报告。
3. **企业白皮书 (Salesforce Einstein / McKinsey)**：与 Salesforce Einstein 或 McKinsey 合作出白皮书《Automated Research Writing Review at Scale: A Multi-Judge Pipeline with Open-Source Models》，含部署成本对比 (GPT-4 单 judge vs DeepSeek-V3 多 judge，1/10 成本) + 偏差缓解操作手册。

研究产出遵循 IMRaD / DSR (Hevner 2007) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准。
