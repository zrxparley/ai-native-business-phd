# 前沿语料库: module-r-research-methodology - LLM辅助系统综述与可复现性

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop
- **arXiv**: https://arxiv.org/abs/2607.21920
- **作者**: Zexin Ren, Zixuan Zhao
- **年份**: 2026
- **摘要**: 提出两个带人在回路的multi-agentic系统用于临床试验系统文献综述，含异构人设LLM代理进行筛选与迭代纠错提取。应用于已发表的网络荟萃分析，系统恢复了原始研究所有试验并发现人工评审遗漏的额外合格试验。
- **验证**: verified

### 2. L-PRISMA: An Extension of PRISMA in the Era of Generative Artificial Intelligence (GenAI)
- **arXiv**: https://arxiv.org/abs/2603.19236
- **作者**: Samar Shailendra, Rajan Kadel
- **年份**: 2026
- **摘要**: 提出在PRISMA框架中整合人工主导综合与GenAI辅助统计预筛选，应对LLM非确定性带来的可复现性、透明度与可审计性挑战。统计层的确定性增强了可复现性，为负责任地将GenAI纳入系统综述工作流提供路径。
- **验证**: verified

### 3. meta-pipe: An LLM-agent pipeline for end-to-end automated systematic review and meta-analysis
- **arXiv**: https://arxiv.org/abs/2606.28363
- **作者**: Hsieh-Ting Lin, Jiunn-Tyng Yeh
- **年份**: 2026
- **摘要**: 开源LLM-agent流水线，集成完整系统综述/荟萃分析工作流并强制人工监督。作者明确声明为系统描述而非验证研究，无验证数据报告，体现了LLM辅助综述工具从原型到验证的方法论缺口。
- **验证**: unverified

### 4. Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs
- **arXiv**: https://arxiv.org/abs/2604.27006
- **作者**: Gilberto Sussumu Hida, Danilo Monteiro Ribeiro
- **年份**: 2026
- **摘要**: 评估12个LLM与4个经典模型在SLR证据筛选中的表现与变异性。发现LLM即使在温度为零时仍表现出显著异质性与残余非确定性，对LLM辅助综述的可复现性提出根本性挑战。
- **验证**: unverified

### 5. LLM-Assisted Empirical Software Engineering: Systematic Literature Review and Research Agenda
- **arXiv**: https://arxiv.org/abs/2604.26192
- **作者**: Victoria Gomes, Delaney Selb
- **年份**: 2026
- **摘要**: 对50篇LLM在实证软件工程中使用的主要研究进行系统综述。发现LLM使用正在增长但仍以自动化为导向，在以人为中心的整合与透明度方面存在缺口，提出研究议程。
- **验证**: unverified

### 6. A Collection of Systematic Reviews in Computer Science
- **arXiv**: https://arxiv.org/abs/2604.16330
- **作者**: Pierre Achkar, Tim Gollub
- **年份**: 2026
- **摘要**: 引入SR4CS，收录1,212篇计算机科学系统综述的集合，用于查询生成与筛选的可复现研究。数据集在Zenodo上以开放许可发布，为LLM辅助综述方法的基准测试提供基础设施。
- **验证**: unverified

### 7. Chained Prompting for Better Systematic Review Search Strategies
- **arXiv**: https://arxiv.org/abs/2602.00011
- **作者**: Fatima Nasser, Fouad Trad
- **年份**: 2025
- **摘要**: 提出基于LLM的链式提示工程框架，用于系统综述中自动搜索策略开发。框架达到0.9平均召回率，展示LLM在综述检索阶段的潜力与可量化评估路径。
- **验证**: unverified

### 8. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis
- **arXiv**: https://arxiv.org/abs/2512.05925
- **作者**: Federico Bianchi, Yongchan Kwon
- **年份**: 2025
- **摘要**: 使用GPT-5检查器识别已发表AI论文中的客观错误。发现每篇论文平均错误数随时间增长——从NeurIPS 2021的3.8个增至NeurIPS 2025的5.9个，对LLM辅助科研的可复现性与质量保障提出警示。
- **验证**: unverified

### 9. ROBoto2: An Interactive System and Dataset for LLM-assisted Clinical Trial Risk of Bias Assessment
- **arXiv**: https://arxiv.org/abs/2511.03048
- **作者**: Anthony Hevia, Sanjana Chintalapati
- **年份**: 2025
- **摘要**: 开源平台用于LLM辅助临床试验偏倚风险评估，包含521篇儿科临床试验报告数据集（8954个信号问题与1202条证据段落）。为LLM辅助综述的质量评估阶段提供可复现的工具与基准数据。
- **验证**: unverified

### 10. Eligibility-Aware Evidence Synthesis: An Agentic Framework for Clinical Trial Meta-Analysis
- **arXiv**: https://arxiv.org/abs/2604.02678
- **作者**: Yao Zhao, Zhiyue Zhang
- **年份**: 2026
- **摘要**: 提出整合自动试验发现与资格感知荟萃分析的代理框架。LLM从自然语言查询生成可解释规则，而逻辑操作确定性地执行以确保可复现性，展示了LLM与确定性方法混合的综述范式。
- **验证**: unverified

## 备注
- 模块聚焦LLM辅助系统综述（multi-agent SLR、PRISMA扩展、链式提示）与可复现性（温度零的非确定性、错误量化、确定性-LLM混合架构）。
- 2篇verified论文（2607.21920 Multi-Agentic SLR、2603.19236 L-PRISMA）经arXiv abstract页确认标题、作者与日期一致。
- 论文#4（Beyond Accuracy）揭示温度零下LLM仍有残余非确定性，是可复现性讨论的核心证据，建议教学重点引用。
- 论文#8（To Err Is Human）显示AI论文错误率逐年上升，对"LLM辅助科研是否降低质量"提供量化辩论素材。
- 论文#3（meta-pipe）作者自述为"系统描述而非验证研究"，适合作为方法论验证缺口的案例。
- arXiv搜索原始query: "LLM systematic review reproducibility"。
