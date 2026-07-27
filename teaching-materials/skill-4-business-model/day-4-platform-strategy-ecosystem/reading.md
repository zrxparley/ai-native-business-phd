# Day 4 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体书籍 / 论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## 1. 平台战略理论

### Platform Revolution（Geoffrey Parker et al., 2016，平台革命）
- 图书官网：https://platformrevolution.com/
- **用法**：Day 4 核心理论来源。Parker/Van Alstyne/Choudary 的平台战略三要素（匹配规则/价值创造/治理机制）和多边市场理论是本 Day 的理论基石。重点读 Ch.1（平台 vs 管道）、Ch.2（网络效应）、Ch.5（平台治理）。

### Network Effects（Brynjolfsson & McAfee, MIT Sloan）
- MIT Sloan 文章：https://sloanreview.mit.edu/article/the-truth-about-network-effects/
- **用法**：理解网络效应的数学结构（Metcalfe定律 n^2）和边界条件。网络效应不是万能的--当多归属成本低时，网络效应会被削弱。对标 starter.ipynb TODO3（多归属率分析）和 TODO6（天道推演临界点）。

### 多边市场经济学（Jean-Charles Rochet & Jean Tirole, 2003）
- 论文：https://scholar.harvard.edu/files/manzi/files/two-sided-markets.pdf
- **用法**：诺贝尔经济学奖得主 Tirole 的多边市场理论奠基论文。理解为什么平台对一方补贴、对另一方收费（定价结构比定价水平更重要）。对标 TODO5（平台战略框架分析）中的抽成比例分析。

---

## 2. AI 平台生态案例

### Hugging Face 官方文档（模型/数据集/Spaces）
- 官方文档：https://huggingface.co/docs/hub
- GitHub：https://github.com/huggingface
- **深链用法**：
  - [Models 文档](https://huggingface.co/docs/hub/models)：理解模型托管生态的运作方式
  - [Datasets 文档](https://huggingface.co/docs/hub/datasets)：数据集提供者的激励机制
  - [Spaces 文档](https://huggingface.co/docs/hub/spaces)：应用开发者生态
  - 对标 starter.ipynb TODO1（生态网络构建）中的 Hugging Face 节点

### MCP（Model Context Protocol）官方规范
- 官方文档：https://modelcontextprotocol.io/
- GitHub：https://github.com/modelcontextprotocol
- **深链用法**：
  - [MCP 规范](https://modelcontextprotocol.io/specification)：理解 MCP 作为开放协议的设计理念
  - [MCP 服务器](https://github.com/modelcontextprotocol/servers)：真实 MCP 工具生态
  - 对标 TODO1 中的 MCP Ecosystem 节点和 TODO5 中的"开放协议"平台类型
  - 2026 前沿：MCP 是新型平台形态，代表"去中心化平台"范式

### LangChain 生态文档
- 官方文档：https://python.langchain.com/docs/get_started/introduction
- GitHub：https://github.com/langchain-ai/langchain
- **深链用法**：
  - [LangGraph](https://github.com/langchain-ai/langgraph)：Agent 编排框架，理解工具集成网络效应
  - [LangSmith](https://docs.smith.langchain.com/)：可观测性 SaaS，理解 LangChain 的商业化路径
  - 对标 TODO5（平台战略框架）中 LangChain 的护城河分析

---

## 3. 天道推演 x 平台仿真

### 网络效应与临界点（Tipping Point）
- 经典论文：W. Brian Arthur, "Increasing Returns and the New World of Business" (HBR 1996)
  - 链接：https://hbr.org/1996/07/increasing-returns-and-the-new-world-of-business
- **用法**：Arthur 的收益递增经济学是平台赢者通吃（WTA）的理论基础。理解正反馈循环如何导致市场倾斜。对标 TODO6（天道推演蒙特卡洛模拟）中的网络效应系数和临界点。

### 蒙特卡洛模拟与贝叶斯推断
- PyMC 文档（贝叶斯推断框架）：https://www.pymc.io/
- **用法**：理解贝叶斯先验/后验更新在平台仿真中的应用。TODO6 用 Beta分布先验建模临界点阈值，用正态分布建模网络效应系数。PyMC 是 Python 贝叶斯推断标准库，本 Day 用 numpy 实现简化版，生产环境可用 PyMC。

### 多Agent仿真与平台生态
- Mesa 框架（Python 多Agent仿真）：https://mesa.readthedocs.io/
- GitHub：https://github.com/projectmesa/mesa
- **用法**：多Agent仿真（Multi-Agent Simulation）是推演平台生态演化的高级方法。本 Day 的 TODO6 是简化版蒙特卡洛模拟，生产级推演可用 Mesa 建模自主决策的 Agent 参与者。2026 前沿：A2A 协议让 Agent 成为平台生态的自主参与者，多Agent仿真成为平台战略推演的核心工具。

---

## 4. 2026 前沿：AI 平台新范式

### DeepSeek 与开源模型生态
- DeepSeek 官方：https://www.deepseek.com/
- Hugging Face 上的 DeepSeek 模型：https://huggingface.co/deepseek-ai
- **用法**：DeepSeek 等开源模型的崛起正在改变 AI 平台格局--开源模型降低了模型护城河，使数据护城河和生态护城河变得更重要。理解为什么 Hugging Face 的"零抽成+开源"模式能与传统30%抽成平台竞争。

### A2A（Agent-to-Agent）协议
- A2A 概念：Google A2A 协议 https://github.com/google/A2A
- **用法**：A2A 协议让不同 Agent 之间直接通信和交易，催生"Agent 经济"。MCP 连接 Agent 与工具，A2A 连接 Agent 与 Agent。两者共同构成 2026 新型平台生态的基础设施。对标 TODO1 中的 MCP Ecosystem 节点。

### 数据网络效应与AI飞轮
- Hugging Face 博客（数据飞轮）：https://huggingface.co/blog
- **用法**：理解 AI 平台特有的"数据网络效应"--使用产生数据，数据改善模型，模型吸引使用。这是 AI 平台与传统平台的本质区别。对标 TODO5 中的"网络效应类型"列。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §Day 4 | 平台战略/网络效应/护城河理论 | 1h |
| 2 | Platform Revolution Ch.1-2（选读） | 多边市场与网络效应 | 0.5h |
| 3 | `starter.ipynb` 上机（配 networkx 文档） | 真实库实操 | 2h |
| 4 | Hugging Face / MCP 官方文档 | 真实平台生态理解 | 0.5h |
| 5 | Arthur "Increasing Returns"（选读） | 收益递增与临界点 | 0.5h |
| 6 | Mesa 多Agent仿真文档（选读） | 仿真推演进阶 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
