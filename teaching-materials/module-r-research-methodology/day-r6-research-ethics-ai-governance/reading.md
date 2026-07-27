# R6 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档/法规/仓库，非主页）。全部链接已验证存在。

---

## ① Belmont Report（研究伦理核心框架）

### Belmont Report 官方页面
- 🌐 Belmont Report（HHS.gov）：https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html
- **用法**：本单元 TODO1 的核心理论依据。三原则（尊重个人/善行/公平正义）和6个审查项的真实来源。重点读"Ethical Principles and Guidelines for the Protection of Human Subjects"部分，理解每条原则的内涵。

### Belmont Report 原文（PDF）
- 📄 Belmont Report v2：https://www.hhs.gov/sites/default/files/ohrp/regulations-and-policy/belmont-report-v2.pdf
- **用法**：TODO1 中6个审查项的原始来源。重点读 Part B（Boundaries Between Practice and Research）和 Part C（Basic Ethical Principles），理解三原则的完整论述。

### Declaration of Helsinki（医学研究伦理）
- 🌐 WMA Declaration of Helsinki：https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/
- **用法**：Belmont Report 的前置文献（1964）。理解研究伦理的历史脉络：Nuremberg Code(1947) -> Helsinki(1964) -> Belmont(1979)。AI研究伦理继承了这个脉络。

---

## ② NIST AI RMF + EU AI Act（AI治理框架）

### NIST AI RMF 1.0 官方页面
- 🌐 NIST AI Risk Management Framework：https://www.nist.gov/itl/ai-risk-management-framework
- **用法**：本单元 TODO4 的核心框架。从研究伦理视角映射四步循环（Govern/Map/Measure/Manage）。重点读"Core Functions"部分。

### NIST AI RMF 1.0 完整文档（PDF）
- 📄 NIST.AI.100-1：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **用法**：TODO4 中研究伦理映射的原始来源。重点读 Govern 部分（问责结构）和 Measure 部分（可信特征评估），理解如何从研究伦理视角映射。

### EU AI Act 官方页面
- 🌐 Artificial Intelligence Act：https://artificialintelligenceact.eu/
- **用法**：本单元 TODO4 的核心法规依据。重点读"Risk Classification"部分，理解四级风险分类。研究合规视角判定AI研究案例的风险等级。

### EU AI Act 法规原文（EUR-Lex）
- 📄 Regulation (EU) 2024/1689：https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **用法**：TODO4 中 Article 5（禁止清单）和 Annex III（高风险清单）的真实法规文本来源。

---

## ③ OECD AI Incidents Monitor（真实AI事件数据）

### OECD AI Incidents Monitor
- 🌐 AI Incidents Monitor：https://oecd.ai/en/incidents-overview
- **用法**：本单元 TODO2 中8个AI研究案例的事件类型来源。浏览真实AI事件，理解不同AI系统的风险类型分布（偏见/安全/隐私/虚假信息）。

### OECD AI Policy Observatory
- 🌐 OECD.AI Policy Observatory：https://oecd.ai/
- **用法**：全球AI治理政策数据库。含各国AI战略、法规、标准的对比。用于理解 Belmont Report 和 NIST AI RMF 在全球AI治理格局中的定位。

---

## ④ garak + PyRIT（AI红队测试工具）

### garak（NVIDIA LLM漏洞扫描器）
- 📦 GitHub：https://github.com/NVIDIA/garak
- 📦 PyPI：https://pypi.org/project/garak/
- **用法**：本单元 TODO6 的红队测试工具。garak 的 probes（dan/promptinject/encoding/goodside 等）在本单元中按领域映射，作为 Belmont 善行原则的履行手段。重点读 README 的 probes 列表和 CLI 用法。

### PyRIT（微软自动化红队框架）
- 📦 GitHub：https://github.com/microsoft/PyRIT
- 📦 文档：https://microsoft.github.io/PyRIT/
- **用法**：本单元 TODO6 的红队风险评分概念来源。PyRIT 的 Scorer 和 Orchestrator 概念用于量化AI研究的红队风险。重点读 README 的 architecture 部分。

---

## ⑤ 2026前沿：MCP + computer use + 天道推演

### Model Context Protocol（MCP）
- 🌐 MCP官方规范：https://modelcontextprotocol.io/
- 📦 GitHub：https://github.com/modelcontextprotocol
- **用法**：notes.md 2026前沿部分的核心。MCP让AI Agent通过标准化接口接入伦理治理工具（IRB审查/合规检查/审计日志），实现"伦理治理即代码"。

### Anthropic computer use
- 🌐 Claude computer use：https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use
- **用法**：notes.md 2026前沿部分的computer use伦理风险。理解AI Agent直接操作软件带来的知情同意/隐私保护/可逆性/风险-收益等研究伦理新挑战。

### Oxford Institute for Ethics in AI
- 🌐 Oxford Internet Institute：https://www.oii.ox.ac.uk/
- **用法**：独立教材 § 7.7 对标大学。Oxford的AI伦理研究所提供从人文社科角度研究AI对商业和社会影响的独特视角。

### Stanford HAI
- 🌐 Stanford HAI：https://hai.stanford.edu/
- **用法**：独立教材 § 7.7 对标大学。Stanford以人为本AI研究所整合技术、伦理和政策研究。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本单元 `notes.md` 理论回顾 + 独立教材 § R6 | Belmont三原则+治理框架 | 1h |
| 2 | Belmont Report 官方页面（三原则部分） | 理解尊重/善行/公平 | 0.5h |
| 3 | `starter.ipynb` 上机（配pydantic+pandas文档） | 真实框架实操 | 2h |
| 4 | NIST AI RMF 官方页面（Core Functions部分） | 理解研究伦理映射 | 0.5h |
| 5 | OECD AI Incidents Monitor（浏览事件类型） | 理解真实AI风险分布 | 0.5h |
| 6 | garak/PyRIT GitHub（probes/architecture部分，选读） | 2026前沿：红队伦理验证 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
