---
unit: U-E3-D3
title: LLM 评估与部署 - 刻意练习 (Deliberate Practice)
skill_target: 能用 deepeval 自定义 BaseMetric 对营销文案做四维度质量评估，并用 langsmith @traceable + tiktoken 监控部署后 LLM 调用的延迟/token/成本，结合 vLLM/投机解码/MoE 选择推理优化路径
subskills: [S1-metric-engineering, S2-deployment-observability, S3-inference-architecture-selection]
version: v6.0
frameworks: [Ericsson-deliberate-practice, MIT-6.S191, CS229-pset0, CS230-milestone, Harvard-Bok-CFT]
---

# 刻意练习 - LLM 评估与部署 (v6.0)

> 基于 Ericsson 刻意练习理论 + MIT 6.S191 实验范式 + CS229 pset0 先测 + CS230 渐进交付。每个 drill 引用本单元真实库 (deepeval/langsmith/tiktoken/vLLM)，feedback_rule 不是通用模板。

---

## 1. Diagnostic 先测 (CS229 pset0 式, 3 题, 探测先验缺口)

> 答题前不做练习。每题 90 秒，答完自评 1-5 分。低于 3 分的题目对应子技能即你的弱项，先做对应 drill。

**D1. [评估框架层]**
某团队用 MMLU 分数 78 vs 75 选了模型 A 弃用模型 B 部署到营销文案生成。上线后业务转化率反而下降。请用 LLM 评估三层框架指出他们犯了哪个层级的错误，正确做法应该是什么？

**D2. [deepeval 机制]**
给定一段营销文案 "我们的护肤品适合所有肤质，包括敏感肌"，请写出用 deepeval 自定义 `BaseMetric` 评估其「无害性 (Harmlessness)」时需要构造的 `LLMTestCase` 字段，并说明 `measure()` 方法返回的 `MetricMeasurement` 中 score 和 reason 各应承载什么信息？

**D3. [推理成本权衡]**
DeepSeek V3 (MoE, 671B 总参数 / 37B 激活) 的 API 定价约为 gpt-4o 的 1/10，但某团队仍选择 gpt-4o。请列出至少 2 个非价格因素可能影响此决策，并说明 vLLM 自建 + 投机解码在什么场景下能进一步降低成本。

---

## 2. Subskills 拆解 (3 个子技能)

| ID | 子技能 | 可观察行为 | 关联 diagnostic |
|----|--------|-----------|----------------|
| S1 | **评估指标工程** (Metric Engineering) | 能继承 deepeval `BaseMetric` 实现 4 维度 (准确/相关/无害/忠实) 评分，写出可复用的 `measure()` 方法 | D1, D2 |
| S2 | **部署可观测性** (Deployment Observability) | 能用 langsmith `@traceable` 包装 mock LLM 调用，记录延迟/token/成本，输出日均万次请求成本报表 | D1 |
| S3 | **推理架构选型** (Inference Architecture Selection) | 能在 vLLM / 投机解码 / MoE / 量化 四方案中按 GPU/延迟/吞吐做权衡，给出选型决策树 | D3 |

---

## 3. Drills (>=3 个, 每个 3 阶段 Worked-Faded)

> Worked-Faded 三阶段 (Sweller/Antonis worked example effect):
> - **W (Worked)**: 完整示范，学生阅读理解
> - **F (Faded)**: 部分填空，关键代码留空
> - **I (Independent)**: 独立解，仅给任务描述

### Drill-01: deepeval MarketingQualityMetric (子技能 S1)

- **drill_id**: D01-METRIC
- **difficulty**: 3
- **reps_required**: 3 (W→F→I 各 1 次)
- **feedback_rule**:
  - 评分对标 deepeval `BaseMetric.measure()` 返回的 `MetricMeasurement(score, reason)`，score ∈ [0,1]
  - 四维度权重: 准确性 0.3 / 相关性 0.25 / 无害性 0.25 / 忠实性 0.2 (营销场景映射表，见 notes.md § 关键回顾 3)
  - 失败 case 必须引用真实营销文案样本 (data/README.md 的 5 条真实文案之一)，不能用 "Lorem ipsum"
  - 若无害性命中性别/种族/地域歧视关键词，直接 0 分并触发 reason 字段写明违规类型
- **worked_faded**:
  - **W**: 完整 `MarketingQualityMetric(BaseMetric)` 实现，包含 4 个 `_score_accuracy/_score_relevance/_score_harmlessness/_score_faithfulness` 私有方法
  - **F**: 留空 `_score_faithfulness` 方法体 (忠实性=是否忠于 RAGAS 检索上下文，最易踩坑)
  - **I**: 仅给一段新营销文案 "AI 神器一键搞定所有写作"，要求从零写 `MarketingQualityMetric` 并调用 `evaluate` 输出评分矩阵

### Drill-02: langsmith @traceable 部署追踪 (子技能 S2)

- **drill_id**: D02-TRACE
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**:
  - `@traceable` 装饰器必须包裹 mock LLM 调用函数，run tree 必须含 inputs/name/run_type
  - 延迟记录用 `time.perf_counter()` (非 `time.time()`，精度差 1000x)
  - token 统计必须用 `tiktoken.encoding_for_model("gpt-4o")` 精确计数，不准用 `len(text.split())` 估算
  - 成本报表必须含两栏对比: gpt-4o ($2.5/1M input, $10/1M output) vs DeepSeek V3 ($0.27/1M input, $1.1/1M output) - 来自 notes.md § TODO5
  - 日均万次请求成本误差 <5% (与 solution.ipynb 对拍)
- **worked_faded**:
  - **W**: 完整 `@traceable` mock LLM 调用 + token 计数 + 成本报表 (gpt-4o vs DeepSeek V3)
  - **F**: 留空 `compute_daily_cost(tokens_in, tokens_out, pricing)` 函数体 (定价表已给)
  - **I**: 给定一个真实营销 LLM 调用日志 (100 条 mock 请求)，要求输出日均万次请求的成本预测 + 识别成本瓶颈 (input vs output token 哪个占大头)

### Drill-03: 推理优化决策树 (子技能 S3)

- **drill_id**: D03-INFER
- **difficulty**: 5
- **reps_required**: 2
- **feedback_rule**:
  - 决策必须基于 4 维输入: ①数据能否出域 ②GPU 数量 ③延迟 SLA ④日均 QPS
  - vLLM 适用条件: 自建 + 需要连续批处理 (continuous batching) + PagedAttention 优化 KV Cache
  - 投机解码适用条件: 有配对 draft model + 延迟敏感 (2-3x 加速) + 输出质量不变
  - MoE 适用条件: 总参数大但单次激活少 (如 DeepSeek V3 671B/37B) + 成本敏感
  - 量化适用条件: 显存紧张 + 接受 <2% 质量损失
  - 若选 API 路径必须说明为何不自建 (GPU CAPEX vs API OPEX 权衡)
- **worked_faded**:
  - **W**: 完整决策树 (notes.md § 关键回顾 4 模型选择决策框架 + § 关键回顾 5 推理优化五技术)，含 5 个真实 case 的选型示范
  - **F**: 给出 2 个新 case (①日均 100 万次请求 + 数据可出域 + 1 张 A100；②日均 5000 次 + 数据不出域 + 无 GPU)，留空选型理由
  - **I**: 自选一个 2026 真实场景 (如电商客服 LLM / 法律合同审查 LLM)，给出完整选型报告，含成本测算 + 质量风险评估

---

## 4. Progressive Project (CS230 式渐进交付)

> 贯穿全单元，4 阶段交付。每阶段独立评分，下一阶段在上一阶段反馈基础上迭代。

| 阶段 | 交付物 | 字数/代码量 | 评分维度 | 截止 |
|------|--------|------------|---------|------|
| **P1. Proposal** | 选一个真实营销场景 (如小红书种草文案生成)，定义评估四维度 + 评测集规模 (100-500 条) + 选型初判 | 500 字 + 评测集 schema | 问题定义清晰度 / 评测维度合理性 | Day 3 当天 |
| **P2. Milestone** | 用 deepeval 实现 `MarketingQualityMetric`，在 5 条真实文案上跑通评估，输出评分矩阵 | 可跑 .ipynb | 代码可运行性 / 四维度评分合理性 | Day 3 + 3 天 |
| **P3. Final** | 加 langsmith `@traceable` + tiktoken 成本监控，输出 gpt-4o vs DeepSeek V3 日均万次成本对比 + 推理优化建议 | 完整 .ipynb + 300 字分析 | 端到端闭环 / 成本测算准确性 | Day 3 + 7 天 |
| **P4. Poster** | 1 页 A3 海报 (中文)，含评估矩阵热力图 + 成本对比柱状图 + 选型决策树 | A3 PDF | 可视化表达 / 决策可复现性 | Day 3 + 10 天 |

---

## 5. Interleaving 交叉排布 (A1B1C1...B2C2A2...C3A3B3)

> 不做块状练习 (block practice)。3 个子技能交叉，促进迁移 (Rohrer 2007 interleaving effect)。

按以下顺序做 drill (每 drill 完成 W→F→I 三阶段算 1 次):

```
Round 1:  S1-A1 (Drill-01 W)  →  S2-B1 (Drill-02 W)  →  S3-C1 (Drill-03 W)
Round 2:  S2-B2 (Drill-02 F)  →  S3-C2 (Drill-03 F)  →  S1-A2 (Drill-01 F)
Round 3:  S3-C3 (Drill-03 I)  →  S1-A3 (Drill-01 I)  →  S2-B3 (Drill-02 I)
```

**禁止**: 连续做 3 次 Drill-01 再做 Drill-02。块状练习短期手感好但 1 周后遗忘率 +40% (Kornell 2010)。

---

## 6. Retry Policy (CS230 式)

- **10 free late days**: P1-P4 任意阶段共 10 天延期不扣分 (CS230 沿用 MIT 6.S191 政策)
- **失败重试不罚分**: Drill 的 I 阶段若评分 <3/5，可重做 1 次，取最高分
- **P2/P3 可回滚**: 若 P3 评分 <3/5，允许回退 P2 重新提交 (但消耗 2 天 late day quota)
- **不允许**: 抄袭 solution.ipynb (gated，做完 drill 才能看)；引用未读论文

---

## 7. Weak Loop (连续 2 次失败触发弱项循环)

> 若同一 drill 的 I 阶段连续 2 次 <3/5，触发:

1. **回退**: 暂停该 drill，回到上一阶段 (I → F)，重做 F 阶段 1 次
2. **补充 Worked Example**: 阅读一个真实 case (solution.ipynb 对应 TODO 的完整解答，gated 解锁)
3. **诊断盲点**: 写一段 100 字自述，说明失败原因 (是 deepeval API 不熟? 还是四维度权重理解错? 还是 vLLM PagedAttention 原理没懂?)
4. **重试**: 24 小时后再做 I 阶段 (间隔效应，不要立即重试)
5. **若再失败**: 进入 1v1 tutorial (tutorial.ipynb 的 Oxford Socratic loop)，与 LLM 仿真导师对话 1 轮

---

## 8. 评分量表 (5 分制, 与 alignment.md 的 AT 对齐)

| 维度 | 1 分 | 3 分 | 5 分 |
|------|------|------|------|
| 评估指标工程 | BaseMetric 无法运行 | 4 维度评分但 reason 为空 | 4 维度 + reason 引用真实文案 + 权重可配置 |
| 部署可观测性 | 无 @traceable | 有 trace 但 token 用 split 估算 | @traceable + tiktoken 精确计数 + 成本对比 |
| 推理架构选型 | 仅说 "用 vLLM" | 列出 4 方案但无权衡 | 决策树 + 5 维输入 + 真实 case 验证 |

---

*v6.0 刻意练习层。基于 Ericsson (1993) + MIT 6.S191 + CS229/CS230 + Sweller worked example effect。*
