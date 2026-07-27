# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档/法规/仓库，非主页）。全部链接已验证存在。

---

## ① NIST AI RMF（AI风险管理框架）

### NIST AI RMF 1.0 官方页面
- 🌐 NIST AI Risk Management Framework：https://www.nist.gov/itl/ai-risk-management-framework
- **用法**：本Day TODO1/TODO3的核心理论依据。四步循环（Govern/Map/Measure/Manage）和控制项清单的真实来源。重点读"Core Functions"部分，理解每个功能的categories和subcategories。

### NIST AI RMF 1.0 完整文档（PDF）
- 📄 NIST.AI.100-1：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **用法**：TODO1中18个控制项的原始来源。重点读第4-7页的"AI RMF Core"部分，以及Appendix A的subcategory完整清单。

### NIST AI RMF Generative AI Profile
- 📄 NIST.AI.600-1：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **用法**：2024年7月发布的生成式AI专用配置文件。补充了针对LLM/生成式AI的12个独特风险（如幻觉、内容溯源、训练数据隐私）。对应notes.md中2026前沿的MCP治理部分。

---

## ② EU AI Act（欧盟人工智能法案）

### EU AI Act 官方页面
- 🌐 Artificial Intelligence Act：https://artificialintelligenceact.eu/
- **用法**：本Day TODO4的核心法规依据。网站提供法规全文、解读、实施时间线。重点读"Risk Classification"部分，理解四级风险分类。

### EU AI Act 法规原文（EUR-Lex）
- 📄 Regulation (EU) 2024/1689：https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **用法**：TODO4中Article 5（禁止清单）和Annex III（高风险清单）的真实法规文本来源。重点读Article 5的8项禁止实践和Annex III的8类高风险AI系统。

### EU AI Act 第50条（透明度义务）
- 📄 Article 50 Transparency obligations：https://artificialintelligenceact.eu/ai-act-articles/article-50/
- **用法**：TODO4中"有限风险"判定的条款来源。营销AI（文案生成/客服机器人）主要受Article 50约束。重点读4(a) AI生成内容标注和4(b) 聊天机器人告知义务。

---

## ③ OECD AI Incidents Monitor（真实AI事件数据）

### OECD AI Incidents Monitor
- 🌐 AI Incidents Monitor：https://oecd.ai/en/incidents-overview
- **用法**：本Day TODO2中8个AI用例的事件类型来源。浏览真实AI事件，理解不同AI系统的风险类型分布（偏见/安全/隐私/虚假信息）。可按领域/风险类型/时间筛选。

### OECD AI Policy Observatory
- 🌐 OECD.AI Policy Observatory：https://oecd.ai/
- **用法**：全球AI治理政策数据库。含各国AI战略、法规、标准的对比。用于理解NIST AI RMF和EU AI Act在全球AI治理格局中的定位。

---

## ④ pydantic + pandas（真实Python库）

### pydantic 官方文档
- 🌐 pydantic docs：https://docs.pydantic.dev/
- **用法**：TODO1/TODO2的库文档。重点读"Models"（BaseModel定义）和"Fields"（Field约束）。pydantic v2的`model_copy(update={...})` API用于TODO3创建带分数的副本。

### pandas pivot_table 文档
- 🌐 pandas pivot_table：https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
- **用法**：TODO5中`df.pivot_table()`的API参考。用于将合规扫描明细结果透视为"用例×功能"的风险热力图。

---

## ⑤ 2026前沿：MCP + computer use + 天道推演

### Model Context Protocol（MCP）
- 🌐 MCP官方规范：https://modelcontextprotocol.io/
- 📦 GitHub：https://github.com/modelcontextprotocol
- **用法**：notes.md 2026前沿部分的核心。MCP让AI Agent通过标准化接口接入治理工具（合规检查/审计日志），实现"治理即代码"。重点读"Architecture"理解MCP的client-server模型。

### Anthropic computer use
- 🌐 Claude computer use：https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use
- **用法**：notes.md 2026前沿部分的computer use治理风险。理解AI Agent直接操作软件带来的权限/可逆性/审计挑战。

### McKinsey "The agentic organization"
- 🌐 McKinsey报告：https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-organization
- **用法**：独立教材Day 1的McKinsey模型详解的理论来源。重点读三维度重塑（Work/Structure/Governance）部分，理解Agentic Organization对AI治理的要求。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 § Day 1 | 范式演进+治理框架 | 1h |
| 2 | NIST AI RMF 1.0 官方页面（Core Functions部分） | 理解Govern/Map/Measure/Manage | 0.5h |
| 3 | `starter.ipynb` 上机（配pydantic+pandas文档） | 真实框架实操 | 2h |
| 4 | EU AI Act 官方页面（Risk Classification部分） | 理解四级风险分类 | 0.5h |
| 5 | OECD AI Incidents Monitor（浏览事件类型） | 理解真实AI风险分布 | 0.5h |
| 6 | MCP官方规范（Architecture部分，选读） | 2026前沿：治理即代码 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
