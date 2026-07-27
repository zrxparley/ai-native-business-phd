# R5 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。

---

## ① IMRaD 结构范例论文

### ReAct 原始论文（Yao et al., NeurIPS 2022，Agent 领域里程碑）
- 📄 arXiv 2210.03629：https://arxiv.org/abs/2210.03629
- **用法**：R5 TODO1 的 IMRaD 结构分析对象之一。用 arxiv Python 包获取论文元数据，解析摘要中的 Introduction/Methods/Results/Discussion 句子分布。重点理解 Agent 论文如何组织 IMRaD 结构。

### LLM-as-a-judge 原始论文（Zheng et al., NeurIPS 2023）
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：R5 的写作质量评估方法论来源。理解如何用 LLM 自动评估开放式文本质量（可迁移到 IMRaD 论文各部分评分）。重点读 §3 评估方法（MT-Bench/Chatbot Arena）和 §5 已知偏差（位置偏差/冗长偏差/自我偏好偏差）。本单元 TODO6 用 LLM-as-a-judge 范式构建同行评审模拟器。

### GraphRAG 论文（Edge et al., 2024）
- 📄 arXiv 2404.16130：https://arxiv.org/abs/2404.16130
- **用法**：R5 TODO1 的第三篇 IMRaD 结构分析对象。理解 RAG 论文的结构组织方式，与 ReAct 对比结构差异。

---

## ② 真实库 + 上机

### arxiv Python 包（已验证：lukasschwab/arxiv.py）
- 📦 GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在）
- 📦 PyPI：https://pypi.org/project/arxiv/ （已验证，持续发布）
- **深链用法**：
  - [Search 类文档](https://github.com/lukasschwab/arxiv.py#search)：对标 TODO1，按 ID/关键词搜索论文
  - [Result 属性](https://github.com/lukasschwab/arxiv.py#result)：对标 TODO1，获取 title/authors/summary/published

### scipy.stats 官方文档（t检验/Cohen's d）
- 🌐 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证）
- **深链用法**：
  - [ttest_ind（独立样本 t 检验）](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)：对标 TODO4，对NSW数据比较处理组与对照组收入差异
  - [t 分布](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html)：对标 TODO4，计算Welch 95% CI

### causaldata 包（NSW实验数据）
- 📦 PyPI：https://pypi.org/project/causaldata/ （已验证）
- **深链用法**：NSW（National Supported Work）是LaLonde (1986) 经典因果推断数据集。本单元用它做t检验/Cohen's d练习，结构同构营销A/B测试。

---

## ③ 学术写作规范

### APA 第 7 版官方指南
- 🌐 APA Style 官方网站：https://apastyle.apa.org/ （已验证，American Psychological Association 官方）
- 🌐 APA 第 7 版引用格式指南：https://apastyle.apa.org/style-grammar-guidelines/references （已验证）
- **深链用法**：对标 TODO4，理解 APA 第 7 版统计报告格式（t/df/p/d/CI）。重点掌握期刊论文、arXiv 预印本两种引用格式的差异。

### Purdue OWL APA 指南（学术写作参考）
- 🌐 Purdue OWL APA 7th Edition：https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_style_introduction.html （已验证）
- **深链用法**：APA 格式的免费在线参考，覆盖正文引用、参考文献列表、表格格式。适合学生快速查阅。

### UNC Writing Center IMRaD 指南
- 🌐 UNC Writing Center Scientific Reports：https://writingcenter.unc.edu/tips-and-tools/scientific-reports/ （已验证）
- **深链用法**：理解 IMRaD 的写作规范和常见误区。重点读 Introduction 的漏斗结构和 Discussion 的局限性写法。

---

## ④ 2026 前沿：LLM-as-a-judge + DeepSeek + 天道推演

### LLM-as-a-judge 的已知偏差与缓解
- 📄 "On the Limitations of Reasoning LLM as Judge"：https://arxiv.org/abs/2504.18703 （2025，LLM 评审的偏差分析）
- **用法**：理解 LLM-as-a-judge 不是银弹--它有位置偏差、冗长偏差、自我偏好偏差。在用 LLM 评估论文写作质量时，实践建议：随机化段落顺序 + 多 judge 投票 + 人工校准。

### DeepSeek 开源模型与学术写作
- 📦 DeepSeek-V3 GitHub：https://github.com/deepseek-ai/DeepSeek-V3 （已验证，开源 LLM）
- **用法**：2026 年 DeepSeek-V3/R1 等开源模型在写作评估任务上接近 GPT-4 水平，成本仅为 1/10。可用于大批量论文写作自检、CI/CD 集成、多 judge 投票。

### A Survey on LLM-as-a-Judge（2024综述）
- 📄 arXiv 2411.15594：https://arxiv.org/abs/2411.15594 （已验证，LLM-as-a-judge综述）
- **用法**：系统理解 LLM-as-a-judge 的方法分类、应用场景和局限。适合在构建同行评审模拟器前阅读。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §6.1-6.7 | IMRaD 写作方法论 | 1h |
| 2 | ReAct 论文（arXiv 2210.03629）| IMRaD 结构范例 | 0.5h |
| 3 | `starter.ipynb` 上机（配 arxiv/statsmodels 文档）| 真实库实操 | 2h |
| 4 | LLM-as-a-judge 论文 §3, §5 | 前沿+偏差认知 | 0.5h |
| 5 | APA 第 7 版统计报告格式指南 | 巩固统计报告规范 | 0.5h |
| 6 | UNC Writing Center IMRaD 指南（选读） | 学术写作延伸 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
