---
unit: elective-e3-llm-intro/day-1
topic: Transformer架构与训练
version: v6.0
framework: Biggs Constructive Alignment (ILO ↔ TLA ↔ AT) + Mastery Learning (Bloom 1968)
---

# alignment.md · 建构对齐 (Biggs ILO ↔ TLA ↔ AT) + Mastery Threshold

> 本文件把 `notes.md` 的 5 条学习目标 (ILO) 与 starter.ipynb / practice.md drill / tutorial.ipynb (TLA) 与 solution.ipynb / 后测 (AT) 一一对齐, 每行附 mastery_threshold。若 AT 可在未经 TLA 的情况下通过, 即对齐失败 (Hattie Feed Forward 检测)。

---

## 1. ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出, Intended Learning Outcome) | TLA (教学学习活动, Teaching/Learning Activity) | AT (评估任务, Assessment Task) | mastery_threshold |
|---|---|---|---|
| **ILO1** 能解释 Transformer 三大核心机制: Self-Attention (Q/K/V 点积+缩放+softmax)、Multi-Head Attention (12 heads × 64=768)、Positional Encoding (RoPE), 并说明为何比 RNN 适合长程依赖 | starter.ipynb TODO3 (手写 Self-Attention) + practice.md D1 (Worked-Faded-Solo) + tutorial.ipynb cell3 Socratic 追问 "为什么 √d_k" | solution.ipynb TODO3 + practice.md D1-Solo 自动检查 (含 √d_k + softmax dim=-1 + shape) + tutorial.ipynb cell5 后测 | D1-Solo >=80% + tutorial 后测 >=3/5 |
| **ILO2** 能阐述训练三阶段 (Pre-training 预测下一 token / SFT 指令微调 / RLHF-DPO 对齐) 各自的数据/目标/产出, 并判断 LLM 故障属于哪一阶段 | starter.ipynb TODO6 (CLM 前向+三阶段概述) + practice.md D2 (4 案例诊断) + tutorial.ipynb cell3 Socratic "若模型不遵循指令是哪阶段" | solution.ipynb TODO6 + practice.md D2-Solo (3 案例诊断报告) + alignment.md §3 自检问题 | D2-Solo >=80% (>=3/4 案例阶段判断正确) |
| **ILO3** 能用 tiktoken + transformers AutoTokenizer 对营销文案做 tokenization, 对比中英文 token 消耗, 结合定价算推理成本 | starter.ipynb TODO1 (tiktoken+GPT-2 tokenizer) + practice.md D3 (Worked-Faded-Solo) + tutorial.ipynb cell2 pre-tutorial 提交 tokenization 表 | solution.ipynb TODO1 + practice.md D3-Solo (5 文案成本表) + 300 字分析 (notes.md 作业) | D3-Solo >=80% + 300 字分析含中英文倍数解释 |
| **ILO4** 能用 torch 手写 Multi-Head Attention + Transformer Block (FFN 4×+残差+LayerNorm), 理解架构而非黑箱 | starter.ipynb TODO4 (Multi-Head+Block) + practice.md D4 (Worked-Faded-Solo) + tutorial.ipynb cell3 Socratic "MoE 为何替换 FFN" | solution.ipynb TODO4 + practice.md D4-Solo (含 MoE 解释 100 字) | D4-Solo >=80% (含残差+LN+4×FFN) |
| **ILO5** 能从 transformers AutoConfig (GPT-2) 读 n_layer/n_head/n_embd/vocab_size, 推算参数量 (~124M), 理解 Scale Law 对商业决策的影响 | starter.ipynb TODO2 (GPT-2 config 推算) + practice.md D5 (Worked-Faded-Solo) + tutorial.ipynb cell3 Socratic "Scale Law 选型" | solution.ipynb TODO2 + practice.md D5-Solo (推算 GPT-2 medium + Scale Law 论证) + progressive_project poster | D5-Solo >=80% (推算误差 <10%) + poster 可被非技术同事看懂 |

---

## 2. 对齐完整性 (覆盖率检查)

- ILO 数: 5 (来自 notes.md "学习目标" 节)
- TLA 覆盖: 5/5 (每 ILO 都映射到 starter TODO + practice drill + tutorial Socratic)
- AT 覆盖: 5/5 (每 ILO 都映射到 solution TODO + practice Solo + 后测/分析/poster)
- mastery_threshold 显式: 5/5 (每行都标了 >=80% 或等价可观察标准)

> 无"悬空 ILO"(有 ILO 但无 TLA/AT), 也无"幽灵 AT"(有 AT 但无对应 ILO)。

---

## 3. 三自检问题 (Hattie Feed Up / Feed Back / Feed Forward)

> 三个问题逐项作答。若任一答 "否", 即对齐失败, 需回改 TLA 或 AT。

### Q1. Feed Up: TLA 是否训练 ILO? (学生是否知道"在练什么")

**答: 是。** 每个 drill 在 practice.md §3 都标注 `target_subskill` (S-A/S-B/S-C), 而 subskill 直接来自 ILO1-ILO5 的拆分。学生在 D1 起步时看到 "本 drill 训练 S-A: Self-Attention 计算与可视化, 对应 ILO1"。tutorial.ipynb cell1 的 persona prompt 也明示 "today we drill ILO1-ILO5 via Socratic", 学生不可能不知道当下练的是哪条 ILO。

### Q2. Feed Back: AT 是否测量 ILO? (评估是否真测目标, 而非周边)

**答: 是。** AT 与 ILO 一一对应, 不是泛考:
- ILO1 测 Self-Attention 公式 -> D1-Solo 自动检查含 `/ (d ** 0.5)` 与 `softmax(dim=-1)`, 直接测三机制中的缩放与 softmax, 不是泛泛"理解 Transformer"。
- ILO2 测三阶段诊断 -> D2-Solo 给 3 个新案例 (非 worked 重复), 学生必须显式写出阶段名 + 数据层修复, 直接测 ILO2 的"判断"能力, 不是背诵。
- ILO3 测 tokenization + 成本 -> D3-Solo 要 5 条新文案的 token 数 + $ 成本 + 中英文倍数解释, 直接测"对比 + 计算成本"。
- ILO4 测 Block 手写 -> D4-Solo 自动检查残差 `x + a` + LN + 4×FFN, 直接测架构而非黑箱调用。
- ILO5 测参数推算 -> D5-Solo 推算 GPT-2 medium (新模型, 非 worked 重复), 直接测 Scale Law 推广能力。

### Q3. Feed Forward: 不经 TLA 能过 AT 吗? (若能=对齐失败)

**答: 否, 对齐成立。** 验证如下:
- D1-Solo 要求打印 attn 矩阵中 (i,j) 最大的 3 个词对并解释 "智能" 与 "助手" 相互注意力高。学生若没做 D1-Worked (读完整示范, 含 tiktoken encode + one_hot + W_Q/W_K/W_V 定义), 不可能 5 分钟内写出 shape 正确的代码。Worked 示范的 7 行 torch 代码是 Solo 的脚手架, 跳过 Worked 直接 Solo 的学生 90% 会卡在 `one_hot(num_classes=100352)` 这一步 (tiktoken cl100k_base vocab=100352 不是常识)。
- D2-Solo 的 3 案例 "模型拒绝写营销文案说涉及诱导消费" 是 Alignment 故障 (非 SFT), 学生若没读 D2-Worked 的 "故障阶段判据" (事实错=Pre-training, 不听指令=SFT, 不安全/拒答=Alignment), 会下意识归到 SFT (因为 "营销" 像指令场景), 测试通过率 <30%。Worked-Faded 不可跳过。
- D5-Solo 推算 GPT-2 medium 需复用 D5-Worked 的公式 (Embedding=vocab×d, per-layer=QKV+FFN+LN), 但 medium 的 n_layer=24/n_embd=1024 是新值。学生若没做 Worked, 不知道 "Embedding 占 31% 不是小头" 这个反直觉点, 会漏算 embedding 导致误差 >10%, 达不到 mastery。
- tutorial.ipynb 的 Socratic 追问 (cell3) 会探测学生是否做过 TLA: 若学生答 "Q/K/V 是查询键值" 但说不出 √d_k, tutorial 会回推到 D1-Worked。即 AT (tutorial 后测) 与 TLA (drill) 形成闭环, 不经 TLA 在 AT 上会被 Socratic 拆穿。

> 三自检全 "是/否" 成立, 建构对齐通过。若后续教学中发现某 AT 可绕过 TLA 通过, 需回改 AT (加 Socratic 追问) 或 TLA (加 Worked 示范)。

---

## 4. mastery 阈值与补救

- **mastery_threshold 统一**: Solo 阶段 >=80% (自动检查 + rubric 评分)。低于 80% 触发 practice.md §7 weak_loop (回退 Faded + 新 worked + 重做 Solo)。
- **跨 ILO 依赖**: ILO4 (Block 手写) 依赖 ILO1 (Self-Attention)。若 ILO1 未达 mastery, ILO4 的 AT 自动降级为"只需写 FFN+残差+LN, 不需写 Attention", 但 ILO1 必须在 final 阶段前补到 mastery。
- **终判**: progressive_project final (40% 占比) 是 ILO2+ILO5 的综合 AT。若 final <80%, 整单元判 "未 mastery", 需重做 weak_loop + 重交 final (retry_policy 不罚分)。

---

## 5. 与 v5.0 / v6.0 文件的交叉引用

| 文件 | 角色 | 对齐贡献 |
|------|------|---------|
| notes.md (v5.0) | ILO 来源 | 5 条学习目标 = 5 条 ILO |
| starter.ipynb (v5.0) | TLA 主载体 | 6 个 TODO = 6 个 TLA 触点 |
| solution.ipynb (v5.0) | AT 参考答案 | 6 个 TODO = 6 个 AT 评分锚 |
| reading.md (v5.0) | TLA 深读 | DeepSeek-MoE / 投机解码 / vLLM 深链 |
| practice.md (v6.0) | TLA 刻意练习 | D1-D5 = ILO1-ILO5 的 Worked-Faded-Solo |
| schedule.json (v6.0) | TLA 间隔重复 | 8 卡 = ILO 核心概念 FSRS-6 复习 |
| tutorial.ipynb (v6.0) | TLA Socratic + AT 后测 | cell3 Socratic + cell5 Hattie 4 级反馈 |

---

*v6.0 alignment.md · 锚定 Biggs & Tang Constructive Alignment + Bloom Mastery Learning + Hattie Feed Up/Back/Forward 三问。*
