# 选修E1 · Day 1：Agent理论基础 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E1 Agentic AI · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Agent如何从"工具调用器"进化为"自主决策系统"？ReAct循环如何驱动营销决策？
> **v5.0 升级点**：① 真实库上机（LangChain/LangGraph/pydantic 构建ReAct Agent）② TODO填空式起始笔记本 ③ 独立.ipynb ④ 深链阅读 ⑤ 2026前沿（ReAct/Plan-Execute/LangGraph/天道推演映射）

---

## 学习目标（学完你能做到）

1. 能解释Agent的自主性谱系（L0-L4），区分Workflow与Agent的本质差异，并在售前场景中准确判断客户的真实自主性需求层级
2. 能用BDI（Belief-Desire-Intention）模型分析营销Agent的认知结构，并用pydantic将BDI形式化为Agent状态Schema
3. 能用LangGraph的`create_react_agent`和LangChain的`@tool`装饰器构建一个带工具调用的ReAct Agent，在真实营销任务上运行并观察Thought-Action-Observation循环
4. 能用`MemorySaver`实现Agent短期记忆，支持多轮对话，理解checkpointer机制
5. 能实现Plan-Execute模式并与ReAct对比，理解两种Agent范式在营销决策中的适用边界
6. 能用天道推演框架分析Agent的因果链路--从感知到决策到行动到反馈，识别关键因果节点和不可逆后果

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E1_Agentic_AI.md` § Day 1](../../AI原生化商业博士_独立教材_选修E1_Agentic_AI.md)（一至四节，已包含自主性谱系/BDI架构/ReAct范式/工具使用）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：自主性谱系--从Workflow到Agent

Anthropic在"Building Effective Agents"中提出核心区分：

| 层级 | 名称 | 自主性 | 典型模式 | 营销示例 |
|:----:|------|:------:|---------|---------|
| L0 | 单次调用 | 无 | Prompt -> Response | 翻译营销文案 |
| L1 | 链式调用 | 极低 | A -> B -> C | 调研 -> 写文案 -> 检查 |
| L2 | 条件路由 | 低 | Workflow with branching | 按用户类型选策略 |
| L3 | 受控循环 | 中 | ReAct Loop | 反复搜索-推理直到完成 |
| L4 | 自主规划 | 高 | Agent自主分解任务 | "策划新品发布会" |

**核心洞见**：Agent的灵活性来源于LLM自主决策，但代价是不可预测性和高成本。"能用Workflow解决的，不要用Agent"。

### 关键回顾 2：BDI架构--经典Agent理论

BDI（Belief-Desire-Intention）由Bratman(1987)提出，Rao & Georgeff(1995)形式化。虽早于LLM数十年，但为理解Agent行为提供了强大分析框架：

| 要素 | 哲学含义 | LLM Agent对应 | 营销Agent示例 |
|------|---------|--------------|-------------|
| **Belief（信念）** | 对世界的认知 | System Prompt + Context + 检索信息 | "目标用户是25-35岁都市白领" |
| **Desire（愿望）** | 想达成的目标 | 用户给定的任务 | "生成10000+阅读的公众号文章" |
| **Intention（意图）** | 承诺执行的计划 | Agent制定的执行步骤 | "Step1:分析热门模式 -> Step2:生成大纲 -> Step3:撰写" |

**核心洞见**：Agent行为是"感知-思考-承诺-行动"，Intention的"坚持性"使Agent不会因微小变化放弃计划。

### 关键回顾 3：ReAct范式--推理与行动的交织

ReAct（Yao et al., 2022, arXiv 2210.03629）解决了纯推理型Agent不能使用工具、纯行动型Agent不会显式推理的问题：

```
Thought: 我需要了解竞品情况
Action: search_product_info("透肌精华")
Observation: 透肌焕亮精华液，299元，含烟酰胺3%...
Thought: 现在分析竞品雅诗兰黛
Action: analyze_competitor("雅诗兰黛")
Observation: 雅诗兰黛小棕瓶，760元，市场占有率18%...
Thought: 信息足够，撰写策略
Action: write_strategy("strategy.txt", "...")
Observation: 策略已写入
Thought: 任务完成
```

ReAct的精妙：每步行动前有Thought（推理），行动后有Observation（观测），形成"思考-行动-观测"闭环。这已成为几乎所有现代Agent框架的基础范式。

### 关键回顾 4：工具使用（Tool Use）--Agent的"手"

工具使用三个层次：
1. **Function Calling**：LLM输出结构化工具调用请求（JSON）
2. **工具选择**：从众多工具中选最合适的（工具描述优化、索引检索）
3. **工具组合**：多工具串联，理解依赖关系

在LangChain中，用`@tool`装饰器定义工具。工具的**名称、docstring、参数类型**就是LLM看到的"接口契约"。

### 关键回顾 5：Agent形式化定义

学术研究中，Agent形式化为元组 `<S, A, T, O, π>`：
- **S** 状态空间 / **A** 动作空间 / **T** 转移函数 / **O** 观测函数 / **π** 策略
- LLM Agent特殊性：策略π由LLM推理动态生成，非固定函数

---

## 上机部分：用真实库构建营销ReAct Agent

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）| [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📦 **真实库说明**：[`data/README.md`](./data/README.md)（LangChain/LangGraph/pydantic + 真实工具 + LLM配置）

### 为什么用真实库而非模拟代码

v4.0的代码用"伪代码+模拟输出"--让你看到结构但学不到真实API调用。v5.0改用 **LangChain + LangGraph + pydantic** 真实库：`create_react_agent`是生产级API，`@tool`装饰器是真实工具定义方式，`MemorySaver`是真实会话持久化。代码可直接用于生产。

### 营销映射（关键桥接）

| Agent理论 | 营销对应 | 本Day实现 |
|-----------|---------|----------|
| BDI Belief | 产品知识+市场认知 | pydantic Belief模型 |
| BDI Desire | 营销任务目标 | pydantic Desire模型 |
| BDI Intention | 执行计划步骤 | pydantic Intention模型 |
| ReAct循环 | 分析->竞品->策略->输出 | `create_react_agent` |
| 工具：产品搜索 | 产品知识检索 | `@tool search_product_info` |
| 工具：竞品分析 | 竞品策略分析 | `@tool analyze_competitor` |
| 工具：策略写入 | 策略输出归档 | `@tool write_strategy` |
| 记忆 | 多轮对话上下文 | `MemorySaver` checkpointer |
| Plan-Execute | 先规划后执行 | `StateGraph` 自定义图 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用pydantic定义BDI状态Schema（Belief/Desire/Intention三要素）
2. **TODO2**：用`@tool`装饰器定义三个营销工具（产品搜索/竞品分析/策略写入）
3. **TODO3**：用LangGraph的`create_react_agent`构建ReAct Agent（含离线StubLLM fallback）
4. **TODO4**：运行Agent处理营销任务，观察并分析Thought-Action-Observation循环轨迹
5. **TODO5**：用`MemorySaver`添加短期记忆，实现多轮对话
6. **TODO6**：用`StateGraph`实现Plan-Execute模式，对比与ReAct的差异

---

## 天道推演视角：Agent决策的因果链分析

天道推演框架可用于分析Agent系统的因果网络：

```
输入：营销任务 + 可用工具集 + Agent架构选择（ReAct vs Plan-Execute）

推演：
  1. ReAct路径：感知任务 -> 推理(Thought) -> 行动(Action) -> 观测(Obs) -> 循环
     - 因果节点：每次Action改变Belief，影响下一次Thought
     - 不可逆点：write_strategy执行后文件已写入，撤销需额外操作
     - 风险：循环不终止、工具选择错误导致信息偏差
  
  2. Plan-Execute路径：感知任务 -> 一次性规划 -> 顺序执行
     - 因果节点：Plan阶段的错误会传播到所有后续Execute步骤
     - 不可逆点：Plan一旦确定，Execute阶段无法动态调整
     - 风险：前提假设错误导致整个计划失效

输出：
  ├── 路径诊断：ReAct灵活但成本不可预测，Plan-Execute可控但适应性差
  ├── 策略建议：营销任务中，信息充分用Plan-Execute，信息不足需探索用ReAct
  └── 认知盲点：StubLLM无法真实模拟LLM的推理质量，真实LLM可能出现非预期工具选择
```

> 💡 **天道推演与Agent理论的结合**：Agent系统的设计本质上是在构建一个因果网络--每个决策节点（Thought/Action/Plan）都是因果链上的一环。用天道推演的沙盘模拟方法，可以在部署前推演Agent在不同输入下的行为路径，预判风险。

---

## 2026前沿补充：Agent范式演进趋势

> v5.0新增前沿点。本Day聚焦ReAct和Plan-Execute两大基础范式，2026年前沿已扩展到多个方向：

**从ReAct到多Agent仿真**：2024-2026年研究热点从单Agent转向多Agent协作仿真。Generative Agents（Stanford, arXiv 2304.03442）展示了Agent的长期记忆和计划修订，MetaGPT将SOP引入多Agent协作。多Agent仿真已成为模拟复杂商业场景的核心技术。

**LangGraph生态成熟**：LangGraph从2024年的新兴框架发展为2026年Agent编排的事实标准之一。`create_react_agent`、`StateGraph`、`MemorySaver`构成Agent开发的"三件套"，与LangSmith（可观测性）、LangGraph Platform（部署）形成完整生产链路。

**Plan-Execute的复兴**：Plan-Execute模式在2025年因Plan-and-Solve论文和BabyAGI的实践重新受到关注。其"先规划后执行"的思路在结构化营销任务中表现优于ReAct的逐步探索。

> 🔗 深入阅读见 [`reading.md`](./reading.md)。

---

## 与后续Day的衔接

- **Day 2**：Agent框架对比--今天是ReAct理论，Day 2对比LangGraph/CrewAI/AutoGen/MetaGPT四框架
- **Day 3**：多Agent系统设计--今天是单Agent，Day 3是多Agent协作（通信协议/共识机制/冲突解决）

---

## 作业与评估

作业、评分标准、费曼演练沿用独立教材 § Day 1 既有设计。本学习材料包新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：你的ReAct Agent在营销任务中的工具调用顺序是否符合天道推演的因果预期？为什么？
- [ ] （可选）对比ReAct与Plan-Execute在同一个营销任务上的步数和输出质量差异

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库+TODO脚手架。*
*最后更新：2026-07-24*


## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。研究锚点为本单元 ReAct (arXiv 2210.03629) vs Plan-Execute (arXiv 2305.04091) 在营销任务上的对比, contribution 声明相对 ReAct 原论文在 QA 基准上迁移到营销决策领域。linked_paper 5 篇均来自 reading.md 已验证深链。详见 research.md 与 industry.md。
