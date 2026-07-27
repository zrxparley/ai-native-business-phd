---
unit: elective-e3-llm-intro/day-2-llm-application-engineering
version: v6.0
skill_target: 能独立用 tiktoken+langchain_core+numpy+langsmith+RAGAS 规则实现构建一个营销知识库 RAG 文案生成管道，并用 faithfulness/context_recall 评估其质量，给出 gpt-4o vs DeepSeek V3 的模型选型建议
---

# Day 2 刻意练习 (Deliberate Practice, Ericsson 1993 + MIT/Harvard/Stanford 教学法)

## skill_target (一句话可评估)
给定一个营销知识库语料，学生能在 90 分钟内独立交付：(a) tiktoken token 计数 + gpt-4o/DeepSeek V3 推理成本对比；(b) langchain_core ChatPromptTemplate 营销文案 Prompt 模板；(c) numpy TF-IDF + 余弦相似度 RAG 检索；(d) langsmith @traceable 全链路追踪；(e) RAGAS 简化 faithfulness / context_recall 评估--五项全过 80% 即 mastery。

## diagnostic (先测，CS229 pset0 式，3 题)
1. **D1-先验**：gpt-4o 用 `o200k_base`、DeepSeek V3 用 `cl100k_base`，同一句中文营销文案"限时抢购 5 折优惠"在两个分词器下 token 数会一样吗？为什么？这影响推理成本估算吗？
2. **D2-决策**：营销 Agent 需要基于私有产品知识库生成文案，且要求 JSON 输出。按 LLM 应用四种模式决策框架（Prompt Engineering -> RAG -> Fine-tuning），你会先尝试哪种？给出权衡理由（成本/灵活性）。
3. **D3-评估**：RAGAS 的 faithfulness 与 context_recall 各自防的是哪类 RAG 失败模式？若 faithfulness=0.6、context_recall=0.9，说明系统瓶颈在检索还是生成？

> 答不出 >=2 题 = 先验缺口，须先做 Subskill A 的 worked example 再进入 drill。

## subskills (3 个子技能拆解)
- **Subskill A · Prompt 工程 + Token 经济**：用 tiktoken 精确计 token，结合 gpt-4o/DeepSeek V3 定价算成本；用 langchain_core ChatPromptTemplate + StrOutputParser 构建 System+Human Prompt 模板，掌握 Few-shot/CoT/Structured Output 五种技术选型。
- **Subskill B · RAG 检索 + 全链路追踪**：用 numpy 手写 TF-IDF + 余弦相似度做营销知识库召回；理解分块策略/Embedding(all-MiniLM-L6-v2)/BM25+向量混合检索/重排序六维优化；用 langsmith @traceable 配置端到端追踪。
- **Subskill C · RAGAS 评估 + 工具协议**：用规则近似实现 faithfulness/context_recall/answer_relevance；理解 MCP (Model Context Protocol) 如何标准化 Function Calling 工具调用，使 Agent 可移植。

## drills (>=3, 含 difficulty/reps_required/feedback_rule/worked_faded 三阶段)

### drill_id: D1
difficulty: 2
reps_required: 4
subskill: A
feedback_rule: |
  自动检查：用 tiktoken.get_encoding("o200k_base") 与 ("cl100k_base") 对同一营销文案分别编码，
  断言 token 数差异在合理区间；用 gpt-4o input $2.50/M 与 DeepSeek V3 input $0.27/M 计算月成本，
  断言 DeepSeek V3 约为 gpt-4o 的 1/10。若学生答错分词器差异，回退到 Subskill A worked example。
worked_faded:
  - stage1_worked: 给出完整示范--用 tiktoken 对"618 全场 5 折，限时 3 天"分别在 o200k_base / cl100k_base 下编码，输出 token 数对比表 + 月成本（万次请求）对比表。
  - stage2_faded: 给出 langchain_core ChatPromptTemplate 骨架，学生填空 System 消息（营销专家人设）和 Human 消息（产品+受众），并用 StrOutputParser 接出。
  - stage3_independent: 学生独立选择 Few-shot vs CoT vs Structured Output，并说明为何 Structured Output 适合程序解析场景。
feedback_rule_domain: 任何引用 tiktoken / o200k_base / cl100k_base / gpt-4o 定价 / DeepSeek V3 MoE 37B 激活参数 的反馈才算合格。

### drill_id: D2
difficulty: 4
reps_required: 5
subskill: B
feedback_rule: |
  自动检查：学生提交的 numpy TF-IDF + 余弦相似度代码必须能对营销知识库语料召回 top-3 文档，
  且 langsmith @traceable 装饰器包裹检索+生成两层。若召回 ground-truth 文档不在 top-3，
  触发 weak_loop：回退 D1 + 补充分块策略 worked example（按句号切分 vs 按段落切分）。
worked_faded:
  - stage1_worked: 完整示范--对一个 5 篇产品 FAQ 的迷你语料做 TF-IDF 矩阵 + 余弦相似度，给出 top-1 召回的完整 numpy 代码。
  - stage2_faded: 学生填空 cosine_similarity 函数体（numpy dot + norm），并选择分块策略（按 512 字符滑窗 vs 按句号）。
  - stage3_independent: 学生独立用 langsmith @traceable 包裹 retrieve()+generate() 两层，并解释为何 @traceable 是 LLM 应用可观测性的"生产标配"。
feedback_rule_domain: 反馈必须引用 TF-IDF / 余弦相似度 / 分块策略 / all-MiniLM-L6-v2 / langsmith @traceable 这些本单元真实库与概念。

### drill_id: D3
difficulty: 5
reps_required: 6
subskill: C
feedback_rule: |
  自动检查：学生提交的 RAGAS 简化实现须输出 faithfulness / context_recall / answer_relevance 三个数值，
  且对一组构造的"幻觉回答"能识别 faithfulness < 0.5。若三个指标逻辑写反（如把召回当忠实度），
  触发 weak_loop：回退 D2 + 补充 RAGAS 三指标定义 worked example。
worked_faded:
  - stage1_worked: 完整示范--对一组 (query, retrieved_context, answer, ground_truth) 用规则近似计算 faithfulness（answer 中名词短语是否都在 context 中）。
  - stage2_faded: 学生填空 context_recall（ground_truth 信息点被检索到的比例）和 answer_relevance（answer 与 query 的关键词重合度）。
  - stage3_independent: 学生独立说明 MCP 如何替代厂商私有 tool calling 格式使 Function Calling 可移植，并给出"营销 Agent 接入 CRM API"的 MCP 工具签名设计。
feedback_rule_domain: 反馈必须引用 faithfulness / context_recall / answer_relevance / RAGAS / MCP / Function Calling 这些本单元真实概念，禁止用通用"做得不错"类空话。

### drill_id: D4 (stretch)
difficulty: 5
reps_required: 3
subskill: B+C
feedback_rule: |
  综合性 drill：把 D2 的 RAG 管道 + D3 的 RAGAS 评估 + D1 的成本分析串成一个"营销 Agent 文案生成 + 质量回归" mini-pipeline，
  写一段 300 字分析报告 gpt-4o vs DeepSeek V3 在万次/日场景下的月成本差异与质量权衡。
worked_faded:
  - stage1_worked: 给出 pipeline 完整骨架（retrieve -> prompt -> mock_generate -> ragas_eval -> cost_report）。
  - stage2_faded: 学生填空 cost_report 模块（用 D1 的定价表）。
  - stage3_independent: 学生独立选模型并论证（成本/质量/可观测性三维度）。

## interleaving (交叉排布, A1B1C1...B2C2A2...C3A3B3, 反块状)
本单元 drill 不按子技能块状排布，而是交叉以促进迁移。具体顺序（学生须按此顺序完成 reps，不跳序）：

```
第1轮: D1-A (Prompt+Token) -> D2-B (RAG 检索) -> D3-C (RAGAS 评估)
第2轮: D2-B (RAG 检索, 第2次 reps) -> D3-C (RAGAS, 第2次 reps) -> D1-A (Prompt+Token, 第2次 reps)
第3轮: D3-C (RAGAS, 第3次 reps) -> D1-A (Prompt+Token, 第3次 reps) -> D2-B (RAG 检索, 第3次 reps)
综合: D4 (stretch, 串联 A+B+C)
```

理由：研究显示 interleaving (Rohrer 2012) 比块状练习更能促进近迁移与远迁移，对 RAG 这种"检索-生成-评估"循环尤其重要。

## retry_policy (CS230 式)
- 每位学生有 **10 个 free late days**，可在学期内任意分配到任意 drill，不扣分。
- 任何 drill 失败（自动检查不通过）可**无限重试，不罚分**；只记录最后一次通过版本。
- D4 综合性 drill 若一次未过，建议先用 1 个 late day 回到 D1/D2/D3 对应 subskill 做 reps 再重试。

## weak_loop (连续 2 次失败触发)
若学生在同一 drill 连续 2 次自动检查失败：
1. 系统触发 **weak_loop**：自动回退到该 drill 所属 subskill 的 stage1_worked（完整示范）重新观看。
2. 强制补充一个 **worked example**（比 stage1 更细的逐步推导）。
3. 学生须在 weak_loop 中答对 1 道概念题（如"faithfulness 防的是哪类失败模式"）才能重新进入 stage2_faded。
4. weak_loop 退出后再失败 2 次，触发人工介入（导师 1:1 答疑），不无限自动循环。

## progressive_project (CS230 式, 渐进交付)
本单元设一个渐进式项目"营销知识库 RAG 文案生成 + 质量回归系统"，分四阶段交付：

- **proposal** (Day 2 上机前提交, 1 页)：选定一个营销场景（如电商 618 大促 / SaaS 产品发布会），列出知识库来源、目标输出格式（Structured Output JSON 字段）、评估指标阈值。
- **milestone** (Day 2 上机中, 90 分钟内)：交付 D1+D2+D3 三 drill 的 stage3_independent 产物（tiktoken 成本表 + RAG 检索 top-3 + RAGAS 三指标）。
- **final** (Day 2 课后 1 周内)：交付 D4 综合 pipeline + 300 字成本/质量/可观测性分析报告 + langsmith 追踪截图。
- **poster** (Day 3 课前 2 分钟 lightning talk)：用 1 张 slide 展示"我的 RAG 系统 faithfulness 从 X 提升到 Y 的关键改动"，强制 retrieval practice（提取练习）。

mastery_threshold: final 阶段四项（成本表/RAG召回/RAGAS指标/pipeline串联）均 >=80% 即 mastery 通过。

---
*本 practice.md 基于 Ericsson 刻意练习理论 + MIT/Harvard/Stanford 教学法 + CS229/CS230 渐进交付传统，所有 drill 的 feedback_rule 均引用本单元真实库（tiktoken / langchain_core / numpy TF-IDF / langsmith @traceable / RAGAS / MCP）。*
