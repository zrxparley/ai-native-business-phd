# Day 2 建构对齐 (Constructive Alignment, Biggs 1996 + Bloom mastery)

> 本单元采用 Biggs 建构对齐框架: 预期学习产出 (ILO) ↔ 教学学习活动 (TLA) ↔ 评估任务 (AT) 三者对齐, 每行附 mastery_threshold。所有 TLA 引用 starter.ipynb / practice.md drill / tutorial.ipynb, 所有 AT 引用 solution.ipynb / tutorial.ipynb 后测。

## ILO ↔ TLA ↔ AT 矩阵 (>=3 行)

| ILO (预期学习产出, 学完能做到) | TLA (教学学习活动, 引用 starter/drill/tutorial) | AT (评估任务, 引用 solution/tutorial 后测) | mastery_threshold |
|---|---|---|---|
| ILO-1: 能阐述 LLM 应用四种模式 (Prompt Engineering / RAG / Fine-tuning / Function Calling) 决策框架, 说明"先 Prompt Engineering, 不够再 RAG, 最后才 Fine-tuning"背后的成本与灵活性权衡 | TLA-1: (a) 阅读 notes.md §关键回顾1 决策树; (b) 在 starter.ipynb TODO1 用 tiktoken 实测中英文 token 差异; (c) 在 practice.md drill D1 stage2_faded 填空 ChatPromptTemplate; (d) 在 tutorial.ipynb 接受 Socratic 追问"凭什么先 Prompt Engineering" | AT-1: (a) solution.ipynb TODO1 给出 gpt-4o vs DeepSeek V3 token+成本对比; (b) tutorial.ipynb cell5 后测"决策框架三步权衡"作答; (c) practice.md diagnostic D2 先测题 | >=80% (三步权衡 + 成本数量级 1/10 + 灾难性遗忘风险三点全对) |
| ILO-2: 能用 numpy TF-IDF + 余弦相似度实现 RAG 检索, 理解分块策略/Embedding/混合检索/重排序六维优化, 并说明 all-MiniLM-L6-v2 在生产环境的作用 | TLA-2: (a) notes.md §关键回顾3 RAG 工作流程; (b) starter.ipynb TODO4 用 numpy 写 TF-IDF + cosine; (c) practice.md drill D2 三阶段 worked_faded (示范->填空->独立); (d) tutorial.ipynb Socratic 追问"若 ground-truth 不在 top-3 怎么办" | AT-2: (a) solution.ipynb TODO4 给出 top-3 召回代码; (b) practice.md D2 stage3_independent 独立包 langsmith @traceable; (c) schedule.json C4 卡片复习 | >=80% (召回 top-3 含 ground-truth + 六维优化能说出 >=4 维) |
| ILO-3: 能用 RAGAS 简化实现评估 RAG 质量 (faithfulness / context_recall / answer_relevance), 理解 MCP 如何标准化 Function Calling 使 Agent 可移植 | TLA-3: (a) notes.md §关键回顾5 RAGAS 三指标; (b) starter.ipynb TODO6 写规则近似评估; (c) practice.md drill D3 三阶段 worked_faded; (d) tutorial.ipynb Socratic 追问"faithfulness=0.6 context_recall=0.9 瓶颈在哪" | AT-3: (a) solution.ipynb TODO6 给出三指标数值; (b) practice.md D3 stage3_independent 设计 MCP 工具签名; (c) schedule.json C5+C6 卡片复习 | >=80% (三指标定义正确 + 瓶颈诊断对 + MCP 可移植性论证) |
| ILO-4: 能用 langchain_core ChatPromptTemplate + StrOutputParser 构建营销文案 Prompt 管道, 用 langsmith @traceable 配置端到端追踪, 选对 Few-shot/CoT/Structured Output | TLA-4: (a) notes.md §关键回顾2 五种 Prompt 技术; (b) starter.ipynb TODO2+TODO3 填空; (c) practice.md drill D1 stage3_independent 选型; (d) tutorial.ipynb Socratic "为何 Structured Output 适合程序解析" | AT-4: (a) solution.ipynb TODO2+TODO3 完整管道; (b) practice.md D4 综合 pipeline 串联 | >=80% (管道能跑 + 选型理由 + @traceable 覆盖检索+生成两层) |
| ILO-5 (mastery 整合): 能把 Prompt 工程 + RAG + RAGAS 评估 + 成本分析串成营销 Agent 文案生成 mini-pipeline, 并用 300 字论证 gpt-4o vs DeepSeek V3 选型 | TLA-5: (a) practice.md progressive_project 四阶段 (proposal->milestone->final->poster); (b) interleaving A1B1C1...B2C2A2...C3A3B3 交叉练习; (c) tutorial.ipynb cell6 exit artifact 提炼盲点 | AT-5: (a) practice.md D4 final 交付 + 300 字报告; (b) Day 3 课前 2 分钟 poster lightning talk (retrieval practice) | >=80% (四项 subskill 全过 + 报告含成本/质量/可观测性三维度) |

## 3 自检问题 (Feed Up / Feed Back / Feed Forward, Hattie 2007)

### 自检 1 · Feed Up (TLA 是否训练 ILO?)
**问**: 本单元的 5 项 TLA (notes 阅读 / starter TODO 填空 / practice drill 三阶段 / tutorial Socratic / interleaving 交叉) 是否每一项都在直接训练至少一个 ILO? 是否存在"为活动而活动"的 TLA (如纯讲授无 retrieval)?

**自检答**: 5 项 TLA 一一映射到 5 个 ILO (见矩阵), 无悬空活动。notes 阅读后必须做 diagnostic 先测 (retrieval), 不允许只读不练; starter TODO 填空即训练 ILO-1/2/3/4; practice drill 三阶段 (worked->faded->independent) 直接训练 ILO-1/2/3; tutorial Socratic 训练高阶推理 (ILO-5 整合); interleaving 防止块状练习的虚假流畅感, 促进迁移。**结论: Feed Up 对齐**。

### 自检 2 · Feed Back (AT 是否测量 ILO?)
**问**: AT-1~5 是否真实测量 ILO-1~5, 而不是测量"做题熟练度"或"记忆"? 是否有 AT 能被"不经理解靠刷题"通过?

**自检答**: AT 设计规避了刷题路径: AT-1 的"成本数量级 1/10"必须基于 tiktoken 实测而非背诵; AT-2 的"召回 top-3 含 ground-truth"必须跑代码而非抄答案; AT-3 的"瓶颈诊断"必须理解三指标定义而非套公式; AT-5 的 300 字报告 + poster lightning talk 强制 retrieval practice, 不能照搬。tutorial.ipynb 的 Socratic 追问进一步用反例/若前提变等探针排除套话。**结论: Feed Back 对齐**。

### 自检 3 · Feed Forward (不经 TLA 能过 AT 吗? 若能=对齐失败)
**问**: 假设学生**跳过所有 TLA**, 直接做 AT-1~5, 能通过 mastery (>=80%) 吗? 若能, 说明 AT 没真正依赖 TLA, 对齐失败。

**自检答**: 不能。AT-1 的 gpt-4o vs DeepSeek V3 token 对比必须先在 TLA-1(b) 用 tiktoken 实测过两个分词器 (o200k_base / cl100k_base) 才能答对差异方向; AT-2 的 numpy TF-IDF + cosine 代码必须先在 TLA-2(b)(c) 经历 worked->faded 三阶段才能独立写出 (矩阵乘法 + norm 归一化 + argsort 三步缺一不可); AT-3 的 MCP 工具签名设计必须先在 TLA-3(d) 经过 Socratic 追问"凭什么用 MCP 而非厂商私有格式"才能给出可移植性论证; AT-5 的 poster 强制 retrieval practice, 不练讲不出 2 分钟。**结论: 不经 TLA 不能过 AT, Feed Forward 对齐**。

## mastery 阈值总表

| ILO | mastery_threshold | 不达标触发 |
|---|---|---|
| ILO-1 | >=80% (三步权衡 + 成本 1/10 + 灾难性遗忘) | 回退 practice.md D1 stage1_worked |
| ILO-2 | >=80% (top-3 召回 + 六维说出 >=4) | 回退 D2 stage1_worked + 分块策略补充 |
| ILO-3 | >=80% (三指标定义 + 瓶颈诊断 + MCP 论证) | 回退 D3 stage1_worked + RAGAS 定义补充 |
| ILO-4 | >=80% (管道跑通 + 选型 + @traceable 双层) | 回退 D1 stage2_faded |
| ILO-5 | >=80% (四项 subskill + 三维度报告) | 触发 weak_loop, 导师 1:1 答疑 |

---
*本 alignment.md 基于 Biggs (1996) Constructive Alignment + Bloom mastery learning + Hattie (2007) formative feedback 三级自检 (Feed Up/Back/Forward)。所有 TLA/AT 均引用本单元真实文件 (starter.ipynb / solution.ipynb / practice.md / tutorial.ipynb / schedule.json), 不使用通用模板。*
