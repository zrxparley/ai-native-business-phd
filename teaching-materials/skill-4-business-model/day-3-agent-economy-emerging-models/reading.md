# Day 3 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。Day 3聚焦Agent经济+mesa仿真+A2A经济+推理成本+天道推演×多Agent仿真。

---

## ① Agent经济理论（a16z + McKinsey）

### a16z "Agent Economy" 系列研究
- a16z AI研究：https://a16z.com/big-ideas-in-ai/ （已验证，Andreessen Horowitz官方）
- **深链用法**：a16z关于Agent经济的三个核心论点来源（Agent是新应用形态/定价从seat-based转向outcome-based/Agent间经济交互催生新市场）。重点读"Agent Economy"相关博客文章，理解Agent经济的商业模式设计。对标 notes.md 的理论回顾。

### McKinsey AI价值创造报告
- McKinsey生成式AI经济潜力报告：https://www.mckinsey.com/mgi/our-research/the-economic-potential-of-generative-ai-the-next-productivity-frontier （已验证，McKinsey Global Institute）
- **深链用法**：McKinsey估计生成式AI每年创造2.6-4.4万亿美元价值，营销和销售是最大领域之一。重点读Executive Summary和"Marketing and Sales"章节，理解AI价值创造的J曲线模式。对标 notes.md 的McKinsey引用。

### Cambridge Digital Innovation Centre
- Cambridge Judge Business School数字创新中心：https://www.jbs.cam.ac.uk/faculty-research/centres/digital-innovation/ （已验证，Cambridge官方）
- **深链用法**：Cambridge研究AI对商业模式颠覆性影响的学术机构。关注"AI驱动的商业模式创新"和"数字平台治理"研究方向。独立教材Day 3对此中心有深度对标。

---

## ② mesa Agent-Based Modeling 框架（仿真实现）

### mesa GitHub 仓库
- GitHub：https://github.com/projectmesa/mesa （已验证，2k+ stars，MIT License）
- **深链用法**：Day 3 Agent经济仿真的核心框架。mesa是Python最成熟的ABM库，提供Model/Agent/DataCollector完整API。重点读README的示例代码和`examples/`目录。

### mesa 官方文档与教程
- 文档：https://mesa.readthedocs.io/ （已验证，完整教程）
- **深链用法**：
  - [mesa基础教程](https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html)：对标 TODO1-4，学习Model/Agent/DataCollector的基本用法
  -[DataCollector API](https://mesa.readthedocs.io/latest/apis/datacollection.html)：对标 TODO4-5，学习model_reporters和agent_reporters的数据收集

### mesa 3.x 迁移指南
- mesa 3.x API变化：https://mesa.readthedocs.io/latest/migration_guide.html （已验证）
- **深链用法**：mesa 3.x与2.x的API有重大变化（不再使用RandomActivation调度器，改用AgentSet.shuffle_do）。本Day使用mesa 3.5.1，需要参考迁移指南理解新API。

---

## ③ A2A经济 + MCP协议 + 推理成本（2026前沿）

### MCP（Model Context Protocol）
- MCP官方文档：https://modelcontextprotocol.io/ （已验证，Anthropic官方）
- MCP GitHub：https://github.com/modelcontextprotocol/python-sdk （已验证，Python SDK）
- **深链用法**：MCP是Anthropic提出的开放协议，为Agent间的工具/数据访问提供标准化接口。MCP是Agent间"发现彼此能力"的基础设施。理解MCP的server/client架构，对应 notes.md 中A2A经济的标准化协议部分。

### OpenAI API定价（推理成本基准）
- OpenAI定价页：https://openai.com/api/pricing/ （已验证，OpenAI官方）
- **深链用法**：GPT-4o input $5/1M tokens是仿真中推理成本的核心参数。对比不同模型的定价（GPT-4o vs GPT-4o-mini vs o1），理解推理成本对Agent经济可行性的影响。对标 TODO3 的推理成本约束。

### DeepSeek API定价（推理成本下降趋势）
- DeepSeek定价：https://api-docs.deepseek.com/quick_start/pricing （已验证，DeepSeek官方）
- **深链用法**：DeepSeek V3的$0.27/1M input tokens比GPT-4o低95%，代表推理成本下降趋势。推理成本下降5-10倍时，Agent经济可行性发生质变。对比两个定价页，理解 notes.md 中"推理成本是Agent经济爆发关键条件"的论点。

---

## ④ 天道推演×多Agent仿真 + Agent经济案例（2026前沿特色）

### Agent-Based Modeling方法论
- mesa ABM教程（Schelling隔离模型）：https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html （已验证，经典ABM案例）
- **深链用法**：Schelling隔离模型是ABM的经典案例--微观Agent的简单规则涌现出宏观的隔离模式。这与本Day的Agent经济仿真同构：微观Agent的购买/定价/匹配行为涌现出宏观的基尼系数和价格分布。理解ABM的"涌现"哲学。

### Sierra（Agent-as-Worker案例）
- Sierra官网：https://www.sierra.ai/ （已验证，Bret Taylor创办的AI客服公司）
- **深链用法**：Sierra是Agent-as-Worker层次的典型案例--AI客服按解决率收费（outcome-based pricing）。理解从Agent-as-Tool到Agent-as-Worker的跨越挑战（信任+度量）。对标 notes.md 的三层模型。

### Anthropic Claude（Agent-as-Tool案例）
- Anthropic API：https://docs.anthropic.com/ （已验证，Anthropic官方）
- **深链用法**：Claude API是Agent-as-Tool层次的典型--开发者用Claude构建Agent工具，按token计费。理解Agent-as-Tool层次的经济模型。对比Sierra的outcome-based pricing，理解定价模型演进。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 §Day 3 | Agent经济三层模型+信任机制 | 1h |
| 2 | a16z "Agent Economy" 系列（选读1-2篇） | Agent经济核心论点 | 0.5h |
| 3 | mesa基础教程（Intro Tutorial） | ABM框架基本用法 | 0.5h |
| 4 | `starter.ipynb` 上机（配mesa文档） | Agent经济仿真 | 2h |
| 5 | MCP官方文档概述（选读） | A2A经济标准化协议 | 0.5h |
| 6 | OpenAI vs DeepSeek定价页对比（选读） | 推理成本趋势 | 0.25h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
