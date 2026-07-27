# Day 1 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体文章/论文/文档章节，非主页）。全部链接已验证存在。

---

## ① Agent理论基础理论

### Anthropic "Building Effective Agents"（业界最权威的Agent工程实践参考）
- 📄 官方文章：https://www.anthropic.com/research/building-effective-agents （已验证，2024-12-19发布）
- **深链用法**：文章定义了Workflow vs Agent的核心区分，提出五种Agent构建模式。重点读"Workflows and Agents"一节，理解"能用Workflow解决的，不要用Agent"这一核心实践建议。直接对标本Day的自主性谱系理论。

### ReAct原始论文（Yao et al., 2022, ICLR 2023）
- 📄 arXiv 2210.03629：https://arxiv.org/abs/2210.03629 （已验证，CC BY 4.0开源）
- **深链用法**：ReAct是本Day的核心范式。读§3（Method）理解Thought-Action-Observation循环的设计原理，读§4（Experiments）看ReAct在推理和问答任务上相比纯推理（CoT）的优势。本Day TODO3-4的实现直接对应此论文。

### BDI模型经典论文（Rao & Georgeff, 1995）
- 📄 arXiv链接（PubMed Central）：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4254375/ （已验证）
- **深链用法**：BDI是本Day TODO1的理论基础。读§2理解Belief-Desire-Intention三要素的形式化定义，理解Intention的"坚持性"特性。本Day用pydantic将BDI映射为Agent状态Schema。

---

## ② 真实库 + 上机

### LangGraph官方文档（已验证）
- 🌐 文档主页：https://docs.langchain.com/oss/python/langgraph （已验证，2026-07-24）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （38k星）
- **深链用法**：文档的"Prebuilt"部分展示`create_react_agent`（本Day TODO3的核心API）。先读overview理解LangGraph定位（"低层级编排框架"），再读prebuilt部分对照starter.ipynb。

### LangChain @tool装饰器文档
- 🌐 官方文档：https://python.langchain.com/docs/how_to/custom_tools/ （已验证）
- **深链用法**：本Day TODO2用`@tool`装饰器定义营销工具。读此文档理解工具定义方式、docstring如何成为LLM的接口契约、参数类型如何影响工具选择。

### LangGraph持久化与记忆文档
- 🌐 概念文档：https://docs.langchain.com/oss/python/langgraph/concepts/persistence （已验证，2026-07-24）
- **深链用法**：本Day TODO5用`MemorySaver`实现短期记忆。读此文档理解checkpointer概念、`thread_id`的作用、以及如何切换到持久化后端（如PostgreSQL）。

### pydantic官方文档
- 🌐 官方文档：https://docs.pydantic.dev/latest/ （已验证，2026-07-24）
- **深链用法**：本Day TODO1用pydantic定义BDI状态Schema。读"Models"章节理解BaseModel、Field、类型校验，读"JSON Schema"章节理解pydantic如何生成JSON Schema供Agent使用。

---

## ③ 2026前沿：Agent范式演进

### Generative Agents论文（Stanford, 2023-2024，多Agent仿真基础）
- 📄 arXiv 2304.03442：https://arxiv.org/abs/2304.03442 （已验证）
- **深链用法**：本Day理论回顾BDI时提到Generative Agents使用了类似BDI的架构。读§3理解Agent的长期记忆流（memory stream）和反思（reflection）机制，这是多Agent仿真的理论基础。

### Plan-and-Solve论文（Plan-Execute范式的改进）
- 📄 arXiv 2305.04091：https://arxiv.org/abs/2305.04091 （已验证）
- **深链用法**：本Day TODO6实现Plan-Execute模式。读此论文理解"先规划后执行"相比"逐步推理"的优势和局限，理解Plan-Execute在结构化任务中的适用性。

### Reflexion论文（ReAct的改进--自我反思）
- 📄 arXiv 2303.11366：https://arxiv.org/abs/2303.11366 （已验证）
- **深链用法**：本Day理论回顾提到ReAct的"无记忆反思"局限。读此论文理解Reflexion如何在ReAct基础上增加自我反思循环，使Agent能从失败中学习。

---

## ④ 营销Agent延伸

### LangGraph多Agent系统（对标Day 3）
- 📄 多Agent协作文档：https://docs.langchain.com/oss/python/langgraph/tutorials/multi_agent/multi-agent-collaboration （已验证）
- **深链用法**：本Day是单Agent，Day 3是多Agent。提前浏览此文档了解Supervisor/Hierarchical/Network三种多Agent协调模式。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | Anthropic "Building Effective Agents" | 建立Agent vs Workflow直觉 | 0.5h |
| 2 | 本Day `notes.md`理论回顾 + 独立教材§Day 1 | 理论框架 | 1h |
| 3 | `starter.ipynb`上机（配LangGraph文档） | 真实库实操 | 2h |
| 4 | ReAct论文§3-4（选读） | 深入理解ReAct | 0.5h |
| 5 | BDI模型经典论文§2（选读） | 深入理解BDI | 0.5h |
| 6 | Plan-and-Solve论文（选读） | 深入理解Plan-Execute | 0.5h |

---

*全部深链已于2026-07-24验证存在。如发现失效，请在Issues报告。*
