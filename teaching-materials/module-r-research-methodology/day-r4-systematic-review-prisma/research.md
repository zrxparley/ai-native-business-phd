# R4 系统文献综述（PRISMA 2020）· 研究产出层 (v7.0)

> 质量契约：CQ-R4-1。

> **本文件用途**：将本单元的 PRISMA 2020 方法论训练（arxiv + pandas + scikit-learn + matplotlib + ASReview proxy）重构为“可发表研究工件”的模板。冻结 fallback 计数为 210→135→40→23；Cohen's kappa=0.7424 与 ASReview 47.4% 缩减来自规则标签和随机翻转的教学模拟，不是两名真人筛选者的研究结果。

---

## research_question

**RQ**：在 "AI marketing" 主题的 arXiv 系统文献综述中，ASReview 风格的主动学习筛选（TF-IDF + LogisticRegression，种子集 5 正例+5 负例）相对人工全筛基线，在保持两位筛选者 Cohen's kappa ≥ 0.61（substantial agreement）的前提下，能否将 Phase 2 Screening 阶段需要人工阅读的标题摘要量从 135 篇降至 ≤ 71 篇（即 ≥ 47.4% 缩减），同时维持 ≥ 90% 召回率？

**可实证性说明**：`starter.ipynb` TODO5 只能验证代码路径和形成先验假设；要真正回答 RQ，必须替换为两名真人独立筛选、保存裁决记录，并在预注册阈值下测量 recall。当前 47.4% 与 kappa 仅作为设计教学和功效规划的模拟锚点。

---

## contribution

相对已有文献，本研究有 3 项显式 delta：

1. **相对 Page et al. (2021) PRISMA 2020 声明**：PRISMA 规范报告透明度，但不替研究者决定“主动学习何时可停止”。本教学模板把 Item 8 的选择过程/自动化披露、Item 11 的研究内偏倚评估和预注册的 recall 门槛组合为待实证协议；当前模拟不能宣称已锁定安全边界。
2. **相对 Kitchenham & Charters (2007)**：原文五维质量评估框架（研究问题清晰度/方法适当性/数据系统性/分析恰当性/局限讨论）是手工 0-5 分打分。本文用 scikit-learn 的 `cohen_kappa_score` 与 TF-IDF+LogReg 把"质量评估"与"主动学习排序"耦合——质量分≥4（Low Risk of Bias）的论文优先进入 ASReview 种子集，形成"质量驱动的主动学习"新流程。
3. **相对 ASReview 原始论文（van de Schoot et al.）**：本单元只用 TF-IDF+LogisticRegression 演示 ASReview 风格排序，并设计 DeepSeek/RAGAS 辅助综合的候选质量门；在真人标签、人工复核和可审计输出完成前，这些是研究方案，不是 AI marketing 领域的有效性证据。综合方法对应 PRISMA Item 13。

---

## linked_paper

| # | 标题 | 作者/年份 | 链接 | 关联说明 |
|---|------|----------|------|---------|
| 1 | The PRISMA 2020 statement: an updated guideline for reporting systematic reviews | Page MJ, McKenzie JE, Bossuyt PM, et al. / 2021 / BMJ | https://www.bmj.com/content/372/bmj.n71 | 本单元 TODO1-TODO6 的方法论母标准。Item 8 要求说明选择过程、独立筛选者与自动化工具；Item 16a 要求用流程图呈现选择结果 |
| 2 | Guidelines for performing Systematic Literature Reviews in Software Engineering | Kitchenham B, Charters S / 2007 / Keele University Technical Report CS-TR-2007-2 | https://kclpure.kcl.ac.uk/ws/portalfiles/portal/174162/1/CS-TR-2007-2.pdf | 本单元 TODO4 五维质量评估框架来源。本文 delta 在于把其手工 0-5 分打分与 ASReview 种子集选择耦合 |
| 3 | ASReview LAB: A Tool for AI-Assisted Systematic Reviews | van de Schoot R, de Bruin J, Schöglman R, et al. / Utrecht University | https://github.com/asreview/asreview | 本单元 TODO5 主动学习机制的工业实现。本文用 scikit-learn TF-IDF+LogisticRegression 复现其内部原理，并报告 47.4% 缩减 |
| 4 | arxiv.py: Python wrapper for the arXiv API | Schwab L / MIT License | https://github.com/lukasschwab/arxiv.py | 本单元 TODO1 PRISMA Phase 1 Identification 的检索工具。本研究全部 210 篇原始论文元数据由其 `arxiv.Search()` 获取 |

> 全部链接来自 `reading.md` 已验证深链，未联网重查。

---

## imrad_outline

### I — Introduction
- **动机**：AI marketing 文献年增长率 > 40%，博士论文第一章必须用 PRISMA 2020 而非叙述性综述（可重复性要求）；但人工全筛 135 篇标题摘要在单人博士时间预算下不可持续。
- **Gap**：PRISMA 2020 要求透明报告选择与综合方法，但不会给出特定领域主动学习的停止阈值；ASReview 在 AI marketing 领域仍缺真人标注的迁移证据。
- **拟议贡献**：① 用冻结 arXiv 元数据定义可复现实验框；② 预注册 recall、一致性和阅读量三重门槛；③ 将 DeepSeek/RAGAS 设为待验证的辅助信号，并强制人工复核与失败回退。

### M — Methods
- **协议与预注册**：正式研究以 `protocol.md` 为冻结协议，记录 RQ、检索式、纳排标准、双人独立筛选、RoB proxy、证据确定性和自动化工具披露；任何阈值变化都作为 protocol amendment。
- **数据**：arxiv.Search() 6 条查询（"AI marketing"/"LLM advertising"等），获取 210 篇原始元数据（title/authors/summary/published/primary_category）；fallback JSON 用于离线复现。
- **PRISMA Phase 1 Identification**：pandas.drop_duplicates() 按标题去重，冻结复现实验口径为 210→135。
- **Phase 2 Screening**：notebook 当前用规则标签 + 10% 随机翻转模拟第二筛选者，训练 Cohen's kappa 计算；发表级研究必须改为两名筛选者独立记录 title/abstract 与 full-text 决策、排除理由和冲突裁决。
- **Phase 3 Quality Assessment**：Kitchenham & Charters 五维 0-5 分 + RoB 三级是教学 RoB proxy；正式证据表需逐项记录研究内偏倚、报告偏倚、间接性、不精确性和证据确定性降级理由。
- **Phase 4 Synthesis**：模拟 ASReview 主动学习——种子集 5 正例+5 负例 → TfidfVectorizer + LogisticRegression → 迭代排序 → 计算读前 N 篇的召回率曲线；LLM/RAGAS 只能作为自动化辅助，需披露模型、参数、人工复核比例和失败回退。

### R — Results
- **Identification**：210 → 去重后 135（去重率 35.7%）。
- **Screening**：冻结 fallback 元数据为 135 → 40；历史在线记录为 44。正式报告必须声明运行模式并由同一 run manifest 生成。
- **Quality Assessment**：冻结 fallback 元数据为纳入 23；历史在线记录为 26。当前 Low/Moderate/High 是 RoB proxy，不是完整 GRADE/CERQual 证据确定性。
- **Synthesis / ASReview**：ASReview 模拟显示读前 71 篇覆盖 90% 相关论文，相对人工全筛 135 篇实现 47.4% 阅读量缩减；该结果依赖模拟标签和种子集，不应外推为真实人工筛选节省。
- **LLM 辅助**：DeepSeek/RAGAS 指标只作为拟纳入质量门；未在 notebook 形成可审计输出前，不得写成已验证结果。

### D — Discussion
- **贡献边界**：本研究在单一领域（AI marketing）单一数据库（arXiv）验证，迁移到医学/心理学需重跑 kappa 门槛；47.4% 缩减依赖种子集质量，种子集偏置会导致召回率下降。
- **局限**：① arXiv 偏 CS，未覆盖 Scopus/Web of Science；② ASReview 模拟用 TF-IDF+LogReg，未用 ASReview LAB 的官方模型；③ LLM 证据合成是 L1 关联分析，不能替代 L2 人工全文复筛。
- **未来工作**：① 多数据库（Scopus + WoS + IEEE Xplore）扩展；② 用 ASReview LAB 官方 oracle 模式对比本模拟；③ 加入天道推演+贝叶斯推断预判研究空白演化（3 条沙盘分支：Agent 自主决策 / LLM 合规 / 多模态营销）。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单（>= 6 项）：

- [x] **Code**：完整代码在 `solution.ipynb`（8 个 code cells，无 scaffold 残留，0 TODO）；starter.ipynb 为 TODO 填空版（6 个 scaffold block）。
- [x] **Data**：arXiv API 真实元数据（210 篇），通过 `arxiv.Search()` 在线获取；fallback JSON 在 `data/` 目录供离线复现。数据许可：arXiv API 使用条款（https://info.arxiv.org/help/api/tou.html），元数据可自由用于研究。
- [x] **Seeds**：`random_state=42`（scikit-learn LogisticRegression 与 train_test_split）；ASReview 种子集固定为前 5 正例+5 负例（按 entry_id 排序确保可复现）。
- [x] **Environment**：Python 3.11；arxiv==2.1.3；pandas==2.2.x；scikit-learn==1.5.x；matplotlib==3.9.x。`requirements.txt` 见 `data/README.md`。
- [x] **Preregistration**：`protocol.md` 提供 OSF/PROSPERO 风格模板；本仓库内的 notes/research 只能视为教学预声明，正式研究需在运行分析前冻结协议并记录 protocol amendment。
- [x] **FAIR**：Findable（arXiv entry_id 全局唯一）；Accessible（arXiv API 公开 + fallback JSON）；Interoperable（pandas DataFrame 标准结构）；Reusable（CC-BY 元数据 + 代码 MIT License 沿用 arxiv.py）。
- [x] **Hardware**：纯 CPU 运行，无 GPU 依赖；单次 PRISMA 全流程 < 60 秒（含 arXiv API 调用）。
- [x] **Statistical reporting**：κ 报告点估计（0.7424）与 ASReview 召回率曲线为教学演示；发表级报告必须补 bootstrap CI、筛选者冲突表、RoB proxy 限制、报告偏倚和证据确定性表。

---

## research_to_practice

本研究工件可沿三轨道翻译为实践产物：

1. **HBS Working Paper → HBR Article**：把"ASReview 在 AI marketing 的 47.4% 缩减 + kappa=0.7424 substantial 一致性"写成 HBS Working Paper（标题候选 *"When Can Active Learning Replace Human Screening? Evidence from 210 AI Marketing Papers"*），再压缩为 HBR 文章（*"How AI Cuts Literature Review Time in Half Without Sacrificing Rigor"*），面向 CMO/Head of Research 受众。
2. **MIT Sloan Teaching Case**：以本单元 PRISMA 四阶段为骨架，撰写 MIT Sloan 教学案例 *"PRISMA in the Age of LLMs: AI Marketing Evidence Synthesis at Scale"*，主角为某 AI 营销 startup 的 Head of Research，决策点是"是否用 ASReview 替代人工全筛"。Case A 给数据与 kappa，Case B 给 LLM 辅助综合的 RAGAS 评分。
3. **企业白皮书 / 政策简报**：以 DeepSeek/RAGAS LLM 辅助证据合成的三指标（faithfulness/answer_relevancy/context_precision）为基础，撰写企业白皮书 *"LLM-Assisted Systematic Review: A Quality-First Playbook for Enterprise Research Teams"*，定位为面向企业战略/咨询/法务团队的"AI 辅助文献综述合规手册"，与 MCP 协议自动化检索场景衔接。

三轨道均须将冻结 fallback 计数（210→135→40→23）与历史在线记录（210→135→44→26）分开报告，并把 κ=0.7424、47.4% 缩减明确标为模拟筛选结果；没有真人筛选数据时不得使用“without sacrificing rigor”等已证实措辞。

---

*本文件为 v7.0 研究产出层。所有 arXiv 链接来自 reading.md 已验证深链。最后更新：2026-07-26。*
