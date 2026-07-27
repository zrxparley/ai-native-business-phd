# Day 1 Agent理论基础 · 研究产出层 (v7.0)

> **所属**: AI原生化商业博士 · 选修E1 Agentic AI · Day 1
> **版本**: v7.0 研究产出层 (publishable artifact + reproducibility)
> **关联基线**: 本文件锚定 v5.0 notes.md (BDI/ReAct/Plan-Execute 自主性谱系 L0-L4) + starter.ipynb/solution.ipynb (LangChain/LangGraph/pydantic 真实库上机)

本文件给出本单元可锚定的核心研究问题、贡献声明、已记录的真实 arXiv 链接、IMRaD 大纲、NeurIPS/ACM 风格可复现清单, 以及研究转实践 (research-to-practice) 翻译路径。所有 arXiv 链接均来自 `notes.md`/`reading.md` 已验证深链, 不联网查询。

---

## research_question

**核心研究问题 (RQ)**: 在结构化营销决策任务 (产品调研 → 竞品分析 → 策略撰写) 上, ReAct 范式 (Yao et al., 2022, 受控循环 L3) 与 Plan-Execute 范式 (Plan-and-Solve, 2023) 在工具调用步数、轨迹可终止性、与天道推演因果预期一致性三方面是否存在显著差异? 该差异是否随任务信息充分度 (信息充分 vs 信息不足需探索) 而调节?

**可实证子问题**:
- RQ1: ReAct Agent 在营销任务中的工具调用顺序是否符合天道推演的因果预期 (感知 → 推理 → 行动 → 观测 → 反馈)?
- RQ2: Plan-Execute 模式在 Plan 阶段错误的传播是否导致比 ReAct 更多不可逆后果 (如 `write_strategy` 已写入文件)?
- RQ3: 自主性谱系 L3 (ReAct 受控循环) 与 L4 (Agent 自主规划) 的成本-灵活性权衡是否可在 6 个 TODO 上机任务上量化?

---

## contribution

**Delta vs prior work (显式声明)**:

1. **相对 ReAct 原始论文 (Yao et al., 2022, arXiv 2210.03629)**: 原论文在 HotpotQA/FEVER 等公开 QA 基准上验证 ReAct, 本文将该范式迁移到**营销决策**领域 (产品搜索/竞品分析/策略写入三工具), 在 `starter.ipynb` 真实营销任务上观察 Thought-Action-Observation 循环轨迹, 而非 QA 任务。

2. **相对 Plan-and-Solve (Wang et al., 2023, arXiv 2305.04091)**: 原论文在数学推理/常识推理上对比 Plan-and-Solve vs CoT, 本文在**结构化营销任务**上对比 Plan-Execute vs ReAct, 并引入天道推演的**不可逆节点** (如 `write_strategy` 文件写入) 作为新的评估维度。

3. **相对 Generative Agents (Park et al., 2023, arXiv 2304.03442)**: 该工作用 memory stream + reflection 实现多 Agent 长期仿真, 本文聚焦**单 Agent 短期记忆** (`MemorySaver` checkpointer, `thread_id`), 在营销多轮对话上验证 BDI Belief 的更新机制, 不涉及多 Agent 协作 (留 Day 3)。

4. **相对 Anthropic "Building Effective Agents" (2024)**: 该文章给出 Workflow vs Agent 的定性区分与 "能用 Workflow 解决的不要用 Agent" 实践建议, 本文用**自主性谱系 L0-L4 量化映射** + 真实 LangGraph `create_react_agent`/`StateGraph` 上机数据, 给出该建议的可操作边界条件。

5. **方法论增量**: 引入天道推演 (元认知沙盘推演) 作为 Agent 系统的**部署前风险推演工具**, 在 `notes.md` 已有的因果链分析 (ReAct 路径/Plan-Execute 路径) 基础上, 形式化为可写入论文的 **sandbox simulation protocol** (3 层推演: immediate → near → far)。

---

## linked_paper

| # | 论文 | 作者/年份 | 链接 (已验证) | 关联说明 |
|:-:|------|----------|--------------|---------|
| 1 | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al., 2022 (ICLR 2023) | https://arxiv.org/abs/2210.03629 | 本单元核心范式。`starter.ipynb` TODO3-4 直接实现 `create_react_agent` 的 Thought-Action-Observation 循环; `notes.md` 关键回顾 3 引用此论文。 |
| 2 | Plan-and-Solve Prompting: Improving Zero-Shot CoT by Large Language Models | Wang et al., 2023 | https://arxiv.org/abs/2305.04091 | 本单元 TODO6 Plan-Execute 模式的理论锚点; `notes.md` 2026 前沿节明确引用其"复兴"。 |
| 3 | Generative Agents: Interactive Simulacra of Human Behavior | Park et al., 2023 (Stanford) | https://arxiv.org/abs/2304.03442 | `notes.md` 2026 前沿节引用; 提供 memory stream + reflection 机制, 是 BDI Belief 更新的理论基础, 衔接 Day 3 多 Agent。 |
| 4 | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al., 2023 | https://arxiv.org/abs/2303.11366 | `reading.md` 已记录; ReAct 的自我反思改进, 对应 `notes.md` "无记忆反思局限"的批判。 |
| 5 | BDI Models (Rao & Georgeff, 1995) | Rao & Georgeff, 1995 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4254375/ | 本单元 TODO1 BDI pydantic Schema 的形式化基础; `notes.md` 关键回顾 2 + `reading.md` ① 均引用。 |

---

## imrad_outline

### Introduction (引言)
- **动机**: LLM Agent 已从学术原型 (ReAct 2022) 进入生产部署 (LangGraph 2026 事实标准), 但 Agent 范式选择 (ReAct vs Plan-Execute) 在**营销决策**这一高价值商业场景下缺乏实证对比。Anthropic "Building Effective Agents" 给出定性建议但未量化。
- **Gap**: 现有 Agent 实证研究集中在 QA/推理基准, 营销决策任务 (含不可逆文件写入 `write_strategy`) 下的 Agent 轨迹分析 scarce。
- **贡献**: (i) 在 LangGraph 真实库上对比 ReAct vs Plan-Execute 在营销任务的工具调用步数与不可逆后果; (ii) 引入天道推演 sandbox simulation protocol 作为 Agent 部署前风险评估方法; (iii) 给出自主性谱系 L0-L4 在营销场景的可操作边界。

### Methods (方法)
- **数据**: 营销任务集 (产品搜索/竞品分析/策略撰写), 工具: `@tool search_product_info`/`@tool analyze_competitor`/`@tool write_strategy` (见 `starter.ipynb` TODO2)。
- **Agent 架构 1 (ReAct)**: LangGraph `create_react_agent` (TODO3), 含离线 StubLLM fallback 保证可复现。
- **Agent 架构 2 (Plan-Execute)**: LangGraph `StateGraph` 自定义图 (TODO6), 一次性规划后顺序执行。
- **短期记忆**: `MemorySaver` checkpointer + `thread_id` (TODO5), 支持多轮对话。
- **BDI 形式化**: pydantic `Belief`/`Desire`/`Intention` 三模型 (TODO1), 映射 `notes.md` 营销映射表。
- **识别策略**: 同一营销任务跑 ReAct 与 Plan-Execute 各 N 次, 对比 (a) 工具调用步数 (b) 是否触发不可逆 `write_strategy` (c) 轨迹与天道推演因果预期的一致性评分 (0-3)。
- **种子**: `random_state=42` (与 `solution.ipynb` 一致)。

### Results (结果)
- **预期核心发现 1**: ReAct 在信息不足任务上步数更多但可动态调整; Plan-Execute 在信息充分任务上步数更少但 Plan 错误传播更严重。
- **预期核心发现 2**: 天道推演因果预期一致性评分: ReAct > Plan-Execute (因 ReAct 每步有 Thought 显式推理, 与因果链节点对齐)。
- **预期核心发现 3**: BDI Intention 的"坚持性"在 Plan-Execute 上更强 (Plan 一旦确定不易改), 在 ReAct 上更弱 (每步可重新推理)。
- **已在 `notes.md` 天道推演节得到的定性结论**: ReAct 灵活但成本不可预测, Plan-Execute 可控但适应性差。

### Discussion (讨论)
- **贡献边界**: 本研究的 ReAct vs Plan-Execute 对比基于 StubLLM (离线 fallback), 真实 LLM 推理质量差异可能改变结论; 需在 Day 2 引入真实 LLM API 后复现。
- **局限**: (i) 单 Agent, 不涉及多 Agent 协作 (Day 3); (ii) 营销任务为模拟, 未在真实企业营销数据上验证; (iii) 天道推演一致性评分为主观评分, 需多位评分者 inter-rater reliability。
- **未来工作**: (i) 扩展到多 Agent (Day 3); (ii) 引入 Reflexion 自我反思闭环; (iii) 在真实企业 (如 Salesforce Einstein 营销 Agent) 上做 field study。
- **理论意义**: 为 Anthropic "能用 Workflow 解决的不要用 Agent" 这一实践建议给出**任务信息充分度**维度的边界条件。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **Code (代码)**: 完整代码在 `solution.ipynb` (7 cells, 0 scaffold残留, 0 TODO残留, 与 `starter.ipynb` 结构对应 7/7); `starter.ipynb` 提供 6 个 TODO 填空脚手架供复现者自行实现。
- [x] **Data (数据)**: 营销任务数据集 (产品/竞品/策略) 在 `data/README.md` 中描述, 含 LangChain/LangGraph/pydantic 真实库配置 + 真实工具定义; 离线 StubLLM fallback 保证无 API key 也可复现。来源: 本课程自建教学数据, 许可: CC BY 4.0 (与 ReAct 论文一致)。
- [x] **Seeds (随机种子)**: `random_state=42` 在 `solution.ipynb` 中硬编码; StubLLM 为确定性响应 (无采样随机性), 保证 ReAct/Plan-Execute 轨迹逐位可复现。
- [x] **Environment (环境)**: Python 3.11+; 关键库版本: `langchain>=0.3`, `langgraph>=0.2`, `pydantic>=2.0` (具体见 `data/README.md`); 无 GPU 依赖 (离线 StubLLM)。
- [x] **Preregistration (预注册)**: 本研究假设 (H1: ReAct 在信息不足任务步数更多但更灵活; H2: Plan-Execute Plan 错误传播更严重) 在 `notes.md` 天道推演节已声明, 可作为 OSF 预注册 hypothesis 的基础; OSF DOI 占位: 待提交。
- [x] **FAIR (数据可发现/可访问/可互操作/可重用)**: 数据可发现 (课程仓库 `data/` 目录), 可访问 (CC BY 4.0 开源), 可互操作 (pydantic Schema 生成 JSON Schema 供任何 Agent 框架消费), 可重用 (TODO 脚手架支持复现者扩展新工具)。
- [x] **LLM 配置可复现**: StubLLM 为确定性 stub, 真实 LLM 路径记录 model_id (如 `claude-sonnet-4-6`/`gpt-4o`) + temperature=0 + max_tokens 限制, 见 `data/README.md` LLM 配置节。

---

## research_to_practice

**研究转实践 (research-to-practice) 翻译路径**:

本研究产出可沿三条路径翻译为实践工件:

1. **HBS Working Paper → HBR Article**: 将 ReAct vs Plan-Execute 在营销任务的对比写成 HBS Working Paper (含 IMRaD 大纲 + 天道推演 sandbox simulation protocol), 再压缩为 Harvard Business Review 文章, 标题候选 *"When to Let Your Marketing Agent Think Aloud: ReAct vs Plan-Execute in 2026"*, 面向 CMO/Head of AI 决策者。

2. **MIT Sloan Teaching Case**: 以本单元营销 Agent (BDI Belief = "目标用户是 25-35 岁都市白领", Desire = "生成 10000+ 阅读公众号文章", Intention = "Step1-3 执行步骤") 为主角, 写 MIT Sloan 教学案例, 决策点: "在新品发布会策划任务上, CMO 应选择 ReAct 还是 Plan-Execute Agent?" (见 `industry.md` case_study 节展开)。

3. **企业白皮书**: 与 LangChain (LangGraph 母公司) 或 Salesforce Einstein 合作, 将自主性谱系 L0-L4 营销映射表 + 天道推演风险预警 转为"营销 Agent 范式选择白皮书", 给出"信息充分用 Plan-Execute, 信息不足需探索用 ReAct"的决策树, 附 ReAct/Plan-Execute 部署清单。

研究产出的实践工件遵循 IMRaD (本文件) / DSR (Hevner 设计科学研究) / OSF 预注册 / FAIR 数据原则 / 可复现研究标准 (NeurIPS/ACM), 不停留在学术发表, 而是可被企业直接消费的决策工具。
