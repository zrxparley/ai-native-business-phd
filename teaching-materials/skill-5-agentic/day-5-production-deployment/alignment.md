# Skill 5 · Day 5 建构对齐 (Constructive Alignment)

> 依据 Biggs (1996) "Enhancing teaching through constructive alignment" 与 Bloom mastery learning。ILO (Intended Learning Outcome) ↔ TLA (Teaching/Learning Activity) ↔ AT (Assessment Task) 三者必须对齐, 每行附 mastery_threshold 与三自检 (Feed Up / Feed Back / Feed Forward)。

## ILO ↔ TLA ↔ AT 对齐矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能解释 Agent 从 PoC 到生产的五大挑战 (可靠性/成本/延迟/可观测性/安全合规) 并说明 PoC 能跑 != 生产能用 | 读 notes.md 关键回顾 1; 做 practice.md Diagnostic D1; 跟 tutorial.ipynb cell1-cell2 的 pre-tutorial retrieval | starter.ipynb TODO1 的 trace 配置 + tutorial.ipynb 后测问答 | >=80% 概念题正确率 (五大挑战各 1 题 + 1 题反例) |
| ILO2: 能用 LangSmith `@traceable` + `wrap_openai` 为营销 Agent 配端到端 trace, 查每步 token/延迟/工具调用 | 做 practice.md Drill-1 (Worked->Faded->Independent) + Interleaving A1/A2/A3; 读 reading.md LangSmith 条目; 跟 tutorial.ipynb cell3 Socratic 追问 | starter.ipynb TODO1 + Drill-1 Independent 交付 (5 步 Agent 加 trace 并用 Client 查 P95 span) | Drill-1 Independent 通过 feedback_rule (3 步全覆盖 + tokens 用 tiktoken + latency_ms 用 perf_counter) |
| ILO3: 能用 tiktoken 精确计 token, 结合定价算单次/日均成本, 识别成本瓶颈 | 做 practice.md Drill-2 (Worked->Faded->Independent); 用 schedule.json C2/C3 卡片间隔重复; 跟 tutorial.ipynb cell4 student_model 记盲点 | starter.ipynb TODO2 + Drill-2 Independent 交付 (20 条 prompt token + 成本 + P50/P95 三段剖析 + 300 字根因) | Drill-2 Independent 通过 feedback_rule (cl100k_base + 三段延迟分解 + P95 用 quantiles) |
| ILO4: 能实现延迟监控 (分步计时 P50/P95) + 灾备降级 (4 级 fallback) + CI/CD 评估门禁 | 做 practice.md Drill-3 (Worked->Faded->Independent) + Interleaving C1/C2/C3; 读 notes.md 灾备降级 + CI/CD 节; 跟 tutorial.ipynb cell5 Hattie 4 级反馈 | starter.ipynb TODO3/TODO4/TODO5 + Drill-3 Independent 交付 (4 级 fallback + 5 pytest + YAML + 50 并发压测) | Drill-3 Independent 通过 feedback_rule (4 级 try/except 特定异常 + 3 阈值门禁 + ThreadPoolExecutor 50 并发) |
| ILO5: 能用 vLLM/投机解码/MoE 推理优化降低单次推理成本, 解释与 LangGraph checkpointer 的协同 | 做 practice.md Drill-4 (Bonus); 用 schedule.json C6 卡片间隔重复; 读 reading.md vLLM/投机解码/MoE 条目 | Drill-4 Independent 交付 (300 字对比报告 + 决策矩阵) | Drill-4 Independent 通过 feedback_rule (PagedAttention + 14-24x + 区分延迟降低 vs 计算量降低) |

## 三自检问题 (Feed Up / Feed Back / Feed Forward)

### 1. Feed Up - TLA 是否训练 ILO?

逐行核对: 每个 ILO 是否有至少 1 个 TLA 显式训练它?

- ILO1 <- notes.md 关键回顾 1 + Diagnostic D1 ✓
- ILO2 <- Drill-1 + reading.md LangSmith ✓
- ILO3 <- Drill-2 + schedule.json C2/C3 ✓
- ILO4 <- Drill-3 + notes.md 灾备降级节 ✓
- ILO5 <- Drill-4 + reading.md vLLM 条目 ✓

无孤儿 ILO。若学生反映某 ILO 没有对应 TLA, 即对齐失败, 需补 TLA。

### 2. Feed Back - AT 是否测量 ILO?

逐行核对: 每个 AT 是否真正测量对应 ILO 的可观察技能 (而非测了别的)?

- AT for ILO2 = Drill-1 Independent 5 步 Agent 加 trace -> 测的是"能否加 trace", 不是"能否背 LangSmith API" ✓
- AT for ILO3 = Drill-2 Independent 20 条 token + P95 三段剖析 -> 测的是"能否用 tiktoken + 识别瓶颈", 不是"能否背定价表" ✓
- AT for ILO4 = Drill-3 Independent 4 级 fallback + 50 并发压测 -> 测的是"能否实现灾备 + 压测", 不是"能否背 fallback 顺序" ✓

若 AT 测的是记忆而非技能, 即对齐失败, 需改 AT。

### 3. Feed Forward - 不经 TLA 能过 AT 吗? 若能 = 对齐失败

试想: 一个学生跳过所有 TLA (不读 notes.md / 不做 Drill / 不跟 tutorial), 直接做 AT, 能过吗?

- 跳过 Drill-1 直接做 5 步 Agent 加 trace: 无法知道 `@traceable` 装饰器位置 + `wrap_openai` 自动 instrument 机制 -> 不过 ✓ (TLA 必要)
- 跳过 Drill-2 直接做 20 条 token + P95 剖析: 无法知道 `cl100k_base` 编码与 `statistics.quantiles` P95 算法 -> 不过 ✓ (TLA 必要)
- 跳过 Drill-3 直接做 4 级 fallback + 50 并发: 无法知道 `RedisSemanticCache` 与裸 except 反模式 -> 不过 ✓ (TLA 必要)

若某 AT 不经 TLA 也能过 (如纯概念题学生靠背书就能过), 即对齐失败, 需把 AT 改成技能型 (如本单元已把 AT 绑定 Drill Independent 阶段而非纸笔考试)。

## Mastery 阈值与补救

- 全单元 mastery = 5 个 ILO 的 AT 全部达到 mastery_threshold
- 任一 ILO 未达阈值: 触发 practice.md Weak Loop (回退 Faded + 补 Worked + 复述决策点)
- mastery 不取最高分, 取最近一次通过分 (鼓励长期保持而非考前突击)
- mastery 与 schedule.json 间隔重复联动: AT 通过后该 ILO 对应卡片仍按 FSRS-6 调度复习, 防遗忘
