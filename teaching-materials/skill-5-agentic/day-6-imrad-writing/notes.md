# 技能5 · Day 6：IMRaD 论文写作 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 6
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：IMRaD 不是格式要求，而是科学交流效率的最优解--如何用 Python 拆解真实论文 + 撰写营销研究各部分？
> **v5.0 升级点**：① 新增真实库上机（arxiv + statsmodels）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM-as-a-judge 评估写作质量 + DeepSeek 等开源模型对学术写作的影响）

---

## 学习目标（学完你能做到）

1. 能解释 IMRaD（Introduction, Methods, Results, and Discussion）四部分结构，并说明为什么它是科学交流效率的最优解（回答读者最关心的四个问题）
2. 能用 **arxiv** Python 包下载/解析真实论文（如 ReAct, arXiv 2210.03629），自动提取其 IMRaD 各部分结构，理解学术论文的"骨架"
3. 能撰写 **Introduction**（漏斗结构：背景 -> 问题 -> 空白 -> 贡献 -> 结构），基于一个营销研究问题（"营销Agent vs 人工策略效果对比"）
4. 能用 **statsmodels** 跑统计检验（独立样本 t 检验 / Cohen's d / 卡方检验），把结果写成 APA 格式学术表述，撰写 **Results** 部分
5. 能撰写 **Methods**（研究设计/数据收集/分析方法，确保可复现性）和 **Discussion**（发现解读/局限性/未来方向），并生成 **APA 第 7 版**参考文献列表

---

## 理论部分：精炼索引（详见独立教材）

> Day 6 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md` § Day 6](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)（3.6.1–3.6.7 节，已包含 IMRaD 四部分结构/Introduction 漏斗/Methods 可复现性/Results 数据说话/Discussion 论文灵魂/APA 引用规范/写作检查清单）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：IMRaD 四部分结构

| 读者的问题 | IMRaD 对应部分 | 核心功能 |
|-----------|:----------:|---------|
| "你为什么要做这个研究？" | Introduction | 建立研究背景和动机 |
| "你是怎么做的？" | Methods | 让别人能复现你的研究 |
| "你发现了什么？" | Results | 用数据说话 |
| "这意味着什么？" | Discussion | 解读发现，承认局限 |

**核心洞察**：IMRaD 不是任意的格式要求，而是科学交流效率的最优解。7 所全球顶尖大学的博士论文全部采用这一格式（或其变体）。

### 关键回顾 2：Introduction 漏斗结构

Introduction 遵循"漏斗结构"--从大到小，从宽到窄：

```
领域背景（宽） -> 具体问题（窄） -> 研究空白（更窄） -> 本文贡献（最窄） -> 论文结构
```

**写作要点**：
- 研究背景：2-3 段，引用行业报告和学术文献
- 研究问题：1-2 段，明确指出当前系统的问题
- 研究空白：1 段，通过文献综述指出前人没做什么
- 本文贡献：3-4 个 bullet points，清晰声明本文做了什么
- 论文结构：1 段，概述后续各节内容

### 关键回顾 3：Methods 可复现性

Methods 的核心要求是**可复现性**：别人读完你的 Methods，应该能用同样的方法重复你的研究。

**Methods 五要素**：研究设计（DSR/混合方法） -> 系统架构 -> 数据收集（定量+定性） -> 评估指标 -> 数据分析方法

### 关键回顾 4：Results 数据说话 + APA 统计报告

Results 的原则是**先描述再解释**。统计检验结果用 APA 格式：

- t 检验：`t(df) = X.XX, p < .001, d = X.XX`
- 卡方检验：`χ²(df, N = XXX) = X.XX, p < .01, φ = 0.XX`
- 效应量解读：d = 0.2 小，d = 0.5 中，d = 0.8 大（Cohen, 1988）

### 关键回顾 5：Discussion 论文灵魂 + APA 引用规范

Discussion 六要素：发现解读 -> 理论贡献 -> 实践启示 -> 局限性 -> 未来方向 -> 伦理声明

APA 第 7 版正文引用：(Smith, 2025) / (Smith & Jones, 2025) / (Smith et al., 2025)

---

## 上机部分：用 Python 拆解真实论文 + 撰写营销研究各部分

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实论文/库**：[`data/README.md`](./data/README.md)（arxiv 包 + ReAct 论文 + statsmodels + 营销 A/B 测试数据）

### 为什么用真实库（arxiv + statsmodels）而非手写文本

v4.0 的"IMRaD 写作"只是讲解格式模板--学生看了模板还是不会写。v5.0 改用**真实论文 + 真实统计工具**：

- **arxiv**（lukasschwab/arxiv.py，1.5k★）：用 Python 下载真实论文（如 ReAct, arXiv 2210.03629）的元数据，自动解析摘要中的 IMRaD 结构--让学生从真实论文中学习结构，而非看抽象模板
- **statsmodels**（Python 统计库）：用 `ttest_ind` 跑独立样本 t 检验，计算 Cohen's d 效应量，用 `scipy.stats.chi2_contingency` 跑卡方检验--让 Results 部分有真实数据支撑，而非编造数字
- **APA 第 7 版**：用代码生成格式准确的参考文献列表，而非手写容易出错

> **与 Day 3 的衔接**：Day 3 用 deepeval 评估 Agent 轨迹质量（LLM-as-a-judge），Day 6 用 LLM-as-a-judge 评估**写作质量**--同一范式在不同场景的应用。Day 6 的 Results 部分使用 statsmodels 做统计检验，与技能3（因果推断）的统计方法形成连贯。

### 营销映射（关键桥接）

本 Day 撰写一篇"营销Agent vs 人工策略效果对比"的 IMRaD 论文：

| IMRaD 部分 | 营销研究内容 | 工具/方法 |
|-----------|------------|----------|
| Introduction | AI原生营销趋势 + Agent效果评估空白 | 漏斗结构写作 |
| Methods | A/B测试设计（N=400）+ 8位营销人员访谈 | 混合方法设计 |
| Results | t检验 + Cohen's d + 卡方检验 | statsmodels + scipy |
| Discussion | Agent效率优势大但质量优势小 + LLM-as-a-judge偏差 | 发现解读 |
| References | 6条真实引用（ReAct/LLM-as-a-judge/DSR等） | APA第7版 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 arxiv 包下载/解析 ReAct 论文，自动提取其 IMRaD 各部分结构
2. **TODO2**：撰写 Introduction（漏斗结构：背景 -> 问题 -> 空白 -> 贡献 -> 结构）
3. **TODO3**：撰写 Methods（研究设计/数据收集/分析方法，确保可复现性）
4. **TODO4**：用 statsmodels 跑统计检验（t检验/Cohen's d/卡方），撰写 Results（APA格式）
5. **TODO5**：撰写 Discussion（发现解读/局限性/未来方向/伦理声明）
6. **TODO6**：生成 APA 第 7 版参考文献列表（6条真实引用，格式准确）

---

## 2026 前沿补充：LLM-as-a-judge 评估写作质量 + DeepSeek 开源模型

> v5.0 新增前沿点。IMRaD 论文写作的核心难题是"写作质量"需要语义理解--人工审稿太慢，格式检查太浅。2026 年的趋势是用 **LLM-as-a-judge**（NeurIPS 2023, arXiv 2306.05685）自动评估论文各部分质量，并用 **DeepSeek** 等开源模型降低评估成本。

**怎么用**：把撰写的 IMRaD 各部分文本整理成结构化输入，让一个 LLM 扮演"论文审稿人"，按预设 criteria 打分：

- **Introduction**：研究问题是否清晰？贡献声明是否具体？漏斗结构是否连贯？
- **Methods**：是否可复现？评估指标是否合理？数据分析方法是否恰当？
- **Results**：统计检验是否正确？APA 格式是否准确？效应量解读是否合理？
- **Discussion**：局限性是否诚实？理论贡献是否有深度？未来方向是否有可行性？

**DeepSeek 等开源模型的作用**：LLM-as-a-judge 传统依赖 GPT-4 等闭源模型（成本高、不可控）。2026 年 DeepSeek-V3/R1 等开源模型在写作评估任务上接近 GPT-4 水平，成本仅为 1/10，可用于：
- 大批量论文写作自检（每次修改后自动评分）
- CI/CD 集成（论文提交前自动检查 IMRaD 结构完整性）
- 多 judge 投票（用多个开源模型交叉评估，缓解单一模型偏差）

**注意**：LLM-as-a-judge 是**辅助评估工具**，有自身偏差（偏好长答案/位置偏差/自我偏好）。它对应因果阶梯的 L1（对文本的关联分析），不能替代真实同行评审（L2 干预：修改后重新提交）。定位为"投稿前自检工具"。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 LLM-as-a-judge 条目。

---

## 与后续 Day 的衔接

- **Day 7**：端到端交付 + Capstone 整合--今天的 IMRaD 论文是 Capstone 报告的写作框架
- **技能3衔接**：Day 6 的 Results 部分使用 statsmodels 做统计检验，与技能3（因果推断）的统计方法形成连贯

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 6 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 IMRaD 论文在哪个部分最难写？为什么？（提示：Introduction 的漏斗结构？Methods 的可复现性？Results 的 APA 格式？Discussion 的局限性诚实度？）
- [ ] （可选）用 LLM-as-a-judge 评估你写的 Introduction 质量，记录评分和理由，分析 LLM 评审与你自评的差异

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（arxiv + statsmodels）+ TODO 脚手架。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)

本单元在 v5.0 学习材料包基础上, 新增**学习科学层**, 不破坏原有 7/7 基线:

- **刻意练习 (deliberate practice, Ericsson 1993)**: 见 `practice.md`, 拆 3 子技能 (结构识别 / 统计写作 / 批判 Discussion), 含 >=3 个领域特定 drill (引用 arxiv 2210.03629 + statsmodels + LLM-as-a-judge 2306.05685, 非通用模板), 三阶段 Worked-Faded 示范 (完整->填空->独立), 交叉练习 interleaving (A1B1C1...B2C2A2...C3A3B3, 不块状), CS230 式渐进交付 (proposal->milestone->final->poster), 失败重试不罚分 (10 free late days), 连续 2 次失败触发 weak_loop 弱项循环 (回退上一 drill + 补充 worked example)。
- **间隔重复 (spaced retrieval, FSRS-6 / SM-2)**: 见 `schedule.json`, 7 张卡片覆盖 IMRaD 四部分 / 漏斗结构 / Methods 五要素 / APA 第 7 版 / arxiv 包 / LLM-as-a-judge, due 序列 [1,3,8,21,60,180] 天, request_retention=0.9, EF0=2.5。
- **建构对齐 (constructive alignment, Biggs 1996)**: 见 `alignment.md`, 5 行 ILO↔TLA↔AT 矩阵 (覆盖 notes.md 全部 5 条学习目标), 每行附 mastery_threshold, 3 自检问题 (Feed Up / Feed Back / Feed Forward), 确保无 ILO 可绕过 TLA 直通 AT。
- **牛津 tutorial LLM 仿真 (Socratic, Hattie 四级反馈)**: 见 `tutorial.ipynb`, persona 为 Oxford tutorial fellow (不直接给答案, Socratic 追问, HBS devil's advocate, 拒绝模糊陈述), 静态 if/else 模拟 4 轮苏格拉底问 (为什么/反例/若前提变/凭什么, cell5 补第 5 问如何-迁移, 总数 >=5), Hattie 四级形成性反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避免 Self 级表扬, 表扬 d=0.14 几乎无效), student_model.json 记录掌握度/盲点, 限频 1 次/天防 LLM 依赖, exit artifact 强制 retrieval 闭环。

mastery 阈值与 Worked-Faded 示例见 `practice.md` 与 `alignment.md`。交叉练习 (interleaving) 促进迁移, 提取练习 (retrieval practice) 优于重读 (Hattie 2009, retrieval d=0.6-0.7 vs rereading d=0.1)。本层不改动 v5.0 任何原文一字, 仅在 notes.md 末尾追加本节, 并新增 4 个独立文件。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-5-agentic.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：Agent评估 × LLM-as-a-Judge × Agent可靠性。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
