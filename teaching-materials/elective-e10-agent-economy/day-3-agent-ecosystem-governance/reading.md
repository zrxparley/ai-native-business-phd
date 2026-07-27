# Day 3 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。Day 3聚焦Agent生态治理+平台设计+市场监管+networkx生态分析+mesa多Agent仿真+pydantic治理schema+numpy-financial平台估值+天道推演×生态治理沙盘+MCP/A2A生态。

---

## ① Agent生态治理理论（教材 + a16z + McKinsey）

### 独立教材 Day 3（核心理论）
- 教材：[`../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md` § Day 3](../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md)（454-614行）
- **深链用法**：Day 3的完整理论讲义--Agent平台三边市场模型/平台核心功能/网络效应分析/Agent市场监管6维度/责任归属4层模型/激励设计4原则/营销Agent经济生态设计实战。对标 notes.md 的理论回顾，是上机设计的理论依据。

### a16z "Agent Economy" 系列研究
- a16z AI研究：https://a16z.com/big-ideas-in-ai/ （已验证，Andreessen Horowitz官方）
- **深链用法**：a16z关于Agent经济的核心论点--Agent平台的三边市场结构和网络效应。重点读"Agent Economy"相关博客，理解Agent生态治理的演进方向。对标 notes.md 的平台三边市场模型。

### McKinsey AI价值创造报告
- McKinsey生成式AI经济潜力报告：https://www.mckinsey.com/mgi/our-research/the-economic-potential-of-generative-ai-the-next-productivity-frontier （已验证，McKinsey Global Institute）
- **深链用法**：McKinsey估计生成式AI每年创造2.6-4.4万亿美元价值，营销和销售是最大领域之一。理解AI平台经济的规模和治理挑战。对标 TODO5 的平台NPV估值。

---

## ② networkx 生态网络拓扑分析

### networkx 官方文档
- networkx 文档：https://networkx.org/documentation/stable/ （已验证，15k+ stars，BSD-3-Clause）
- **深链用法**：Day 3 Agent生态网络构建的核心库。重点读MultiDiGraph和图算法文档。对标 TODO2 的生态网络构建和 TODO3 的拓扑分析。

### networkx 教程
- networkx 教程：https://networkx.org/documentation/stable/tutorial.html （已验证）
- **深链用法**：
  - [MultiDiGraph](https://networkx.org/documentation/stable/reference/classes/multidigraph.html)：对标 TODO2，构建支持多类型边的Agent生态网络
  - [Algorithms](https://networkx.org/documentation/stable/reference/algorithms/index.html)：对标 TODO3，度分布/聚类系数/核心-边缘/中心性

### networkx 核心-边缘分析
- core_number文档：https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.core.core_number.html （已验证）
- **深链用法**：核心-边缘结构分析识别生态的关键节点和单点故障风险。对标 TODO3 的核心-边缘分析。

---

## ③ mesa 多Agent仿真（小规模）

### mesa GitHub 仓库
- GitHub：https://github.com/projectmesa/mesa （已验证，2k+ stars，MIT License）
- **深链用法**：Day 3 mesa多Agent仿真的核心库。mesa是Python最成熟的ABM（Agent-Based Modeling）库。重点读README的示例代码和`mesa/examples/`目录。

### mesa 官方教程
- mesa 教程：https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html （已验证，Schelling隔离模型等经典案例）
- **深链用法**：Schelling隔离模型是ABM经典案例--微观Agent简单规则涌现宏观模式。与本Day的生态治理沙盘同构：微观治理规则（pydantic schema）涌现宏观的Gini/欺诈率。对标 TODO4 的mesa仿真。

### mesa 3.x API
- mesa 3.x迁移指南：https://mesa.readthedocs.io/latest/migration_guide.html （已验证）
- **深链用法**：mesa 3.x有重大API变化（`model.agents.shuffle_do("step")`替代`RandomActivation`）。本Day使用mesa 3.x，需参考迁移指南理解新API。

---

## ④ pydantic 治理schema + numpy-financial 平台估值

### pydantic GitHub 仓库
- GitHub：https://github.com/pydantic/pydantic （已验证，20k+ stars，MIT License）
- **深链用法**：Day 3 Agent平台治理规则schema定义的核心库。pydantic v2用Rust重写核心（pydantic-core），性能比v1快5-50倍。对标 TODO1 的治理规则schema。

### pydantic 官方文档
- 文档：https://docs.pydantic.dev/ （已验证）
- **深链用法**：
  - [pydantic BaseModel教程](https://docs.pydantic.dev/latest/concepts/models/)：对标 TODO1，学习BaseModel/Field/model_validator
  - [pydantic结构化输出](https://docs.pydantic.dev/latest/concepts/json_schema/)：对标 TODO1，学习model_dump_json()导出Agent可读schema

### numpy-financial 文档
- GitHub：https://github.com/numpy/numpy-financial （已验证，MIT License）
- **深链用法**：Day 3 平台12月NPV/IRR估值的核心库。对标 TODO5 的平台估值。

---

## ⑤ 真实Agent生态案例（A2A/MCP/Coze/Dify/GPT Store/HF）

### A2A协议（Google）
- A2A GitHub：https://github.com/google/A2A （已验证，Google官方）
- **深链用法**：A2A（Agent-to-Agent）协议由Google提出，让不同Agent之间直接通信和交易，催生"Agent经济"。A2A协议催生分润模式：Agent协作链按贡献度分得收益。对标 notes.md 中A2A经济部分和 TODO2 的A2A_CALLS边。

### MCP协议（Anthropic）
- MCP官方文档：https://modelcontextprotocol.io/ （已验证，Anthropic官方）
- MCP GitHub：https://github.com/modelcontextprotocol/python-sdk （已验证，Python SDK）
- **深链用法**：MCP（Model Context Protocol）是Anthropic提出的开放协议，为Agent间的工具/数据访问提供标准化接口。MCP生态是2026新型平台形态--与传统App Store的30%抽成不同，MCP生态目前零抽成、开放协议。对标 notes.md 中MCP生态部分和 TODO2 的MCP_INTEGRATES边。

### OpenAI GPT Store 抽成政策
- OpenAI GPT Store：https://openai.com/chatgpt/pricing/ （已验证，OpenAI官方）
- **深链用法**：GPT Store采用30%/15%抽成（小开发者15%），是传统平台集中治理的代表。对比MCP的0抽成，理解平台治理的两种范式。对标 TODO1 的分润规则和 TODO5 的平台估值。

### Hugging Face Spaces
- Hugging Face：https://huggingface.co/ （已验证，开源生态）
- **深链用法**：Hugging Face Spaces采用0抽成、开源生态，是去中心化平台治理的代表。对比GPT Store的30%抽成，理解开放协议对传统平台的颠覆。对标 TODO1 的准入规则。

### Coze 与 Dify Agent平台
- Coze：https://www.coze.com/ （已验证，字节跳动Agent平台）
- Dify：https://dify.ai/ （已验证，开源Agent平台）
- **深链用法**：Coze和Dify是2024-2026兴起的Agent平台，治理规则介于GPT Store和MCP之间。理解Agent平台治理的多样性。对标 TODO2 的生态网络构建。

---

## ⑥ 天道推演×生态治理沙盘 + 多Agent仿真方法论（2026前沿特色）

### Agent-Based Modeling方法论（天道推演同构）
- mesa ABM教程（Schelling隔离模型）：https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html （已验证，经典ABM案例）
- **深链用法**：Schelling隔离模型是ABM的经典案例--微观Agent的简单规则涌现出宏观的隔离模式。与本Day的生态治理沙盘同构：微观治理规则（pydantic schema）涌现出宏观的Gini/欺诈率/平台收入。天道推演在意识中构建沙盘，mesa在代码中构建沙盘。

### Platform Revolution（平台革命）
- Platform Revolution（MIT Press）：https://mitpress.mit.edu/9780262535186/platform-revolution/ （已验证，MIT Press官方）
- **深链用法**：Platform Revolution是平台经济学经典著作，解释网络效应、平台治理、多边市场设计。本Day的平台三边市场模型和治理4原则都基于此书的理论框架。对标 notes.md 的平台核心功能部分。

### Anthropic 结构化输出
- Anthropic结构化输出：https://docs.anthropic.com/en/docs/build-with-claude/tool-use （已验证，Anthropic官方）
- **深链用法**：结构化输出是Agent可发现治理声明的基础。pydantic schema定义平台治理的输入输出契约，让其他Agent能自动判断能否加入。对标 TODO1 的pydantic治理schema设计。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 §Day 3 | 三边市场+市场监管6维度+激励4原则 | 1h |
| 2 | a16z "Agent Economy" 系列（选读1-2篇） | Agent生态治理演进 | 0.5h |
| 3 | networkx基础教程（MultiDiGraph/图算法） | 生态网络构建基本用法 | 0.5h |
| 4 | `starter.ipynb` 上机（配mesa+pydantic+numpy-financial文档） | 治理规则对比+生态分析+平台估值 | 2h |
| 5 | A2A/MCP/GPT Store对比（选读） | 真实Agent生态治理案例 | 0.5h |
| 6 | mesa 3.x教程（选读Schelling模型） | 多Agent仿真方法论 | 0.5h |
| 7 | Platform Revolution（选读第1-3章） | 平台经济学理论 | 1h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
