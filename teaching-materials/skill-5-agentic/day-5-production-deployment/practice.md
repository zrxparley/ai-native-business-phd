---
unit: U5-D5
title: Agent 生产部署刻意练习
skill_target: 能用 LangSmith + tiktoken 为营销 Agent 配置端到端可观测性、成本核算、延迟优化、灾备降级、CI/CD 评估门禁, 并能用 vLLM/投机解码/MoE 推理优化降低单次推理成本
---

# Skill 5 · Day 5 刻意练习 (Deliberate Practice)

> 依据 Ericsson "Deliberate Practice and the Acquisition of Expert Performance"、MIT 6.867/CS229 pset 风格、CS230 渐进交付、Harvard/Stanford Worked-Faded 范式设计。每个 drill 都针对本单元真实库 (LangSmith / tiktoken / vLLM / concurrent.futures / pytest)。

## Diagnostic (先测, 探测先验知识缺口, CS229 pset0 风格)

完成下列 3 道先测题, 不查资料, 限时 15 分钟。每题答错或留白即对应 subskill 的弱项, 进入对应 drill。

- **D1 (可观测性)**: 给定一段未加 trace 的营销 Agent 代码 (搜索知识库 -> 调 LLM 生成文案 -> 调工具改写), 你会如何用 LangSmith 的 `@traceable` 装饰器 + `wrap_openai` 为它加上端到端 trace? 写出 3 个装饰器的位置, 并指出每个 trace span 应记录哪些字段 (input/output/latency/tokens/tool_name)。
- **D2 (成本)**: 用 tiktoken 对 prompt `"给这款护肤品写一段小红书种草文案, 强调保湿与温和, 字数 150 字以内"` 精确计数 input tokens; 若模型定价为 $5/M input + $15/M output, 输出 200 token, 求单次请求成本与日均万次请求的月成本。
- **D3 (灾备)**: 营销 Agent 主模型 gpt-4o 在压测中触发 429 限流。请写出 4 级 fallback 链的触发顺序 (主模型 -> 备用模型 -> 语义缓存 -> 默认模板), 并说明每一级应记录到 LangSmith 的字段以便事后定位降级路径。

诊断映射: D1 错 -> subskill S1; D2 错 -> S2; D3 错 -> S3。

## subskills (子技能拆解)

- **S1 可观测性 / Observability**: 用 LangSmith `@traceable` + `wrap_openai` 为 Agent 加端到端 trace, 用 Client 查询 trace 数据, 区分第一层(Prometheus)/第二层(APM)/第三层(业务)三层监控
- **S2 成本与延迟 / Cost & Latency**: 用 tiktoken BPE 精确计 token, 结合定价算单次/日均成本; 用 `time.perf_counter` 分步计时识别 P50/P95 瓶颈; 用语义缓存 (RedisSemanticCache) + 模型路由降本
- **S3 灾备与 CI/CD / Resilience & CI-CD**: 实现 ResilientLLM 多级 fallback; 用 pytest + 评估门禁 (任务完成率>=90% / 幻觉率<=5% / 安全违规=0%) + GitHub Actions YAML 构建 CI 流水线; 用 ThreadPoolExecutor 压测并发, 用 LangGraph checkpointer 做中断恢复省 token

## Drills (>=3, 每个 drill 含 worked_faded 三阶段)

### Drill-1: LangSmith 端到端 trace 配置 (S1, difficulty=3, reps_required=2)

- **目标**: 把一个裸营销 Agent (3 步: 检索知识库 -> 生成文案 -> 改写) 套上 LangSmith trace, 在 Dashboard 看到 4 个 span 的调用链与字段
- **feedback_rule**: 领域特定 - 检查 trace 是否覆盖"知识库检索 / LLM 推理 / 工具调用"三步; span 元数据是否含 `tokens` (用 tiktoken 算, 不是字符估算) 与 `latency_ms` (`time.perf_counter`); `wrap_openai` 是否自动 instrument 了 OpenAI 调用 (而非手动 print)。参考 starter.ipynb TODO1 的脚手架位置
- **worked_faded**:
  - **Worked (完整示范)**: 给出 3 个 `@traceable` 装饰器全部就位的完整 notebook, 配套 trace 截图, 学生读+复述
  - **Faded (部分填空)**: 删去 1 个 `@traceable` 与 1 行 `wrap_openai`, 学生补全
  - **Independent (独立解)**: 给一个全新 5 步 Agent (新增"事实核查"与"格式校验"两步), 学生从零加 trace 并用 Client 查询出 P95 延迟最高的 span

### Drill-2: tiktoken 成本核算 + P50/P95 延迟剖析 (S2, difficulty=4, reps_required=3)

- **目标**: 对 20 条真实营销 prompt, 用 tiktoken 算 input tokens, 估算输出 token 上限, 算单次成本; 再用 `time.perf_counter` 分步计时, 算 P50/P95, 识别瓶颈 (检索 vs LLM vs 工具)
- **feedback_rule**: 领域特定 - 必须用 tiktoken BPE 而非 `len(text)/4` 估算; 必须按 `cl100k_base` 编码 (GPT-4o 系列编码); P95 必须用 `statistics.quantiles` 或 numpy 算而非排序取中点; 必须给出"知识库检索 / LLM 推理 / 工具调用"三段延迟分解, 指出哪一段是 P95 瓶颈。参考 starter.ipynb TODO2/TODO3
- **worked_faded**:
  - **Worked**: 给出 1 条 prompt 的完整 token 计数 + 成本公式 + 三段计时示例
  - **Faded**: 给 5 条 prompt 的 token 计数已填, 学生填成本公式与 P95 计算
  - **Independent**: 学生自选 20 条 prompt (来自 data/README.md 营销日志样本), 独立完成 token + 成本 + P50/P95 三段剖析, 输出 300 字瓶颈根因分析

### Drill-3: ResilientLLM 多级 fallback + CI/CD 评估门禁 (S3, difficulty=5, reps_required=3)

- **目标**: 实现 ResilientLLM (主模型 gpt-4o -> 备用 gpt-4o-mini -> RedisSemanticCache 语义缓存 -> 默认模板) 4 级 fallback; 写 pytest 回归测试套件 (>=5 个 test case), 配评估门禁 YAML (完成率>=90% / 幻觉率<=5% / 安全违规=0%); 模拟 GitHub Actions 跑通流水线
- **feedback_rule**: 领域特定 - fallback 链每一级必须 try/except 捕获特定异常 (RateLimitError / APIConnectionError / Timeout), 不得用裸 `except:`; 语义缓存必须用 `RedisSemanticCache` 而非普通 dict 缓存; 评估门禁 YAML 必须含 3 个阈值 (完成率/幻觉率/安全违规率), 缺一不可; pytest 必须复用 Day 3 的 deepeval 断言风格。参考 starter.ipynb TODO4/TODO5
- **worked_faded**:
  - **Worked**: 给出 2 级 fallback 的完整实现 + 2 个 pytest case + 完整 YAML
  - **Faded**: 给 2 级 fallback, 学生补后 2 级 (语义缓存 + 默认模板) + 补 3 个 pytest case
  - **Independent**: 学生独立写完整 4 级 fallback + 5 个 pytest case + YAML, 并用 ThreadPoolExecutor 模拟 50 并发验证 fallback 触发顺序, 用 LangGraph checkpointer 验证中断恢复省 token

### Drill-4 (Bonus, 前沿): vLLM/投机解码/MoE 推理成本对比 (S2, difficulty=5, reps_required=1)

- **目标**: 给定一个日均万次请求的营销 Agent, 计算用商业 API vs 自建 vLLM (PagedAttention + continuous batching) 的月成本对比; 分析投机解码 (draft model 2-3x 延迟降低) 与 MoE (Mixtral 8x7B 只激活 2/8 专家) 各自的降本机制, 写 300 字对比
- **feedback_rule**: 领域特定 - 必须引用 vLLM 的 PagedAttention KV Cache 优化与 14-24x 吞吐提升; 必须区分"延迟降低"(投机解码)与"单次计算量降低"(MoE); 不得混淆"自建推理"与"商业 API"的成本结构 (固定 GPU 成本 vs 变动 token 成本)。参考 notes.md 2026 前沿一节
- **worked_faded**:
  - **Worked**: 给出商业 API 月成本计算 (定价表 + 日均万次) 完整示例
  - **Faded**: 给 vLLM 单卡 A100 月租 + 吞吐数字, 学生算单次推理成本并对比
  - **Independent**: 学生独立写 300 字对比报告, 含"何时选商业 API / 何时选 vLLM 自建 / 何时叠加投机解码与 MoE"决策矩阵

## Progressive Project (CS230 风格渐进交付)

仿 CS230 course project 四阶段交付, 每阶段独立评分, 后阶段依赖前阶段:

- **Proposal (Day 5 当天交)**: 选一个真实营销 Agent (小红书种草 / 朋友圈广告 / 抖音脚本), 写 1 页 proposal: 列出 5 大生产化挑战 (可靠性/成本/延迟/可观测性/安全合规) 各自的现状与目标指标 (如 P95<5s, 单次成本<$0.01, 任务完成率>=90%)
- **Milestone (Week 1)**: 提交 LangSmith trace 配置 + tiktoken 成本基线 + P50/P95 延迟剖析报告, 至少跑通 Drill-1/Drill-2 的 Independent 阶段
- **Final (Week 2)**: 提交完整 ResilientLLM 4 级 fallback + pytest CI 套件 + GitHub Actions YAML + 50 并发压测结果, 至少跑通 Drill-3 的 Independent 阶段
- **Poster (Week 3)**: IMRaD 风格 poster, 报告"我的 Agent 在压测中的瓶颈根因 + 降本/降延迟措施的效果 (前后对比数字)", 为 Day 6 IMRaD 论文写作打素材

## Interleaving (交叉排布, 不块状)

按 A1B1C1...B2C2A2...C3A3B3 顺序交叉练习 3 个 subskill, 避免块状刷题 (块状练习短期流畅度高但迁移差, Rohrer 2007):

- A1: Drill-1 Worked (S1)
- B1: Drill-2 Worked (S2)
- C1: Drill-3 Worked (S3)
- A2: Drill-1 Faded (S1)
- B2: Drill-2 Faded (S2)
- C2: Drill-3 Faded (S3)
- A3: Drill-1 Independent (S1)
- B3: Drill-2 Independent (S2)
- C3: Drill-3 Independent (S3)
- (可选) D4: Drill-4 Independent (前沿, Bonus)

每天做 3 项 (跨 subskill), 不允许一天只刷一个 subskill。

## Retry Policy (CS230 风格)

- **10 free late days**: 整个单元累计可用 10 天迟到豁免, 不扣分, 鼓励试错
- **失败重试不罚分**: Drill 的 Independent 阶段若首次未过 feedback_rule, 可无限次重试, 不扣分; 重试前必须先回看 Worked 示范并复述
- **mastery 导向**: 不取最高分, 取最近一次通过分; mastery_threshold 见 alignment.md

## Weak Loop (连续 2 次失败触发弱项循环)

若某 drill 的 Independent 阶段连续 2 次未通过 feedback_rule, 自动触发弱项循环:

1. 回退到该 drill 的 Faded 阶段重做 1 次
2. 补充 1 个额外 Worked example (导师/助教现场示范, 或读 solution.ipynb 对应 cell)
3. 复述 Worked 示范的关键决策点 (为什么装饰器加在这里 / 为什么用 RedisSemanticCache 而非 dict / 为什么评估门禁含 3 个阈值)
4. 重新进入 Independent 阶段

弱项循环不计入 retry 次数, 不影响 mastery 评分。
