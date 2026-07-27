---
unit: elective-e3-llm-intro/day-1
topic: Transformer架构与训练 (Self-Attention, Multi-Head, Pre-training/SFT/RLHF-DPO, MoE, Tokenization)
version: v6.0
skill_target: 能手写 torch 版 Self-Attention (Q×K^T/√d_k → softmax → ×V) 并解释为何它比 RNN 更适合长程依赖, 且能判断一个 LLM 表现不佳属于 Pre-training(知识不足)/SFT(不遵循指令)/Alignment(不安全或风格不对) 哪一阶段
---

# practice.md · 刻意练习 (Ericsson + MIT/CS229 pset0 + Harvard/Stanford Worked-Faded)

> 本文件锚定 `notes.md` 的 5 条学习目标, 把"听得懂 Transformer"切成可观察、可评分的子技能与 drill。每个 drill 的 feedback_rule 引用本单元真实库 (transformers / torch / tiktoken) 与真实数据 (GPT-2 config, 营销文案语料), 不写通用模板。

---

## 1. diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 3 道题, 5 分钟内作答, 不计入总分。目的是让 tutorial 决定从哪个 drill 起步。

DQ1. 给定 Q (1×d_k)、K (N×d_k)、V (N×d_v), 写出 Attention(Q,K,V) 的逐元素公式。问: 为什么分母是 √d_k 而不是 d_k? 若去掉缩放, softmax 在 d_k=768 (GPT-2 small) 时会发生什么?

DQ2. 一个营销 Agent 生成的文案"知识正确但不听指令"(用户要短句, 它写长段)。这是 Pre-training / SFT / Alignment 哪一阶段没做好? 写出你的判据。

DQ3. 用 tiktoken 对"限时特惠买一送一"编码, 估算 token 数; 同义英文 "Limited time offer, buy one get one free" 的 token 数大致是多少? 哪个更贵 (按 GPT-4o 定价)?

> 评分: 每题 0/1/2 分。0=完全空白, 1=方向对但缺关键, 2=完整且能解释。总分 <3 者先做 D1+D3, >=4 者可直接进 D2+D4。

---

## 2. subskills (3 个可观察子技能)

- **subskill_A (S-A) Attention 计算与可视化**: 能用 torch 写出 Self-Attention 与 Multi-Head Attention, 给定营销文案 token 后能画出注意力矩阵, 指出哪些词对相互关联最强。
- **subskill_B (S-B) 训练三阶段故障诊断**: 给定一个 LLM 故障现象 (空洞/不遵循指令/不安全/风格不对), 能定位到 Pre-training / SFT / RLHF-DPO 哪一阶段, 并给出修复方向 (继续预训练 vs 加 SFT 数据 vs 重做偏好对齐)。
- **subskill_C (S-C) Tokenization 与推理成本推算**: 能用 tiktoken + transformers AutoTokenizer 对中英文营销文案做 tokenization, 结合 GPT-2 config (n_layer=12, n_head=12, n_embd=768, vocab=50257) 推算参数量 ~124M, 结合模型定价计算单次推理成本与 MoE/投机解码的节省倍数。

---

## 3. drills (>=5 个, 每个 Worked-Faded 三阶段)

> 每个 drill 三阶段: **Worked** (完整示范, 学生读) → **Faded** (部分填空, 学生补关键行) → **Solo** (独立解, 学生写). feedback_rule 领域特定。

### drill_id: D1
- **target_subskill**: S-A
- **difficulty**: 2
- **reps_required**: 3 (Worked 1 + Faded 1 + Solo 1)
- **task**: 用 torch 手写 Self-Attention: 输入 X (N×d), 学习 W_Q/W_K/W_V (d×d), 输出 softmax(QK^T/√d_k)V。在营销文案 "我们的智能助手帮你省时省力" 的 token 上跑前向, 输出 (N, d) 注意力加权表示。
- **worked_example** (完整示范):
  ```python
  import torch, torch.nn as nn, tiktoken
  enc = tiktoken.get_encoding("cl100k_base")
  ids = enc.encode("我们的智能助手帮你省时省力")
  X = torch.nn.functional.one_hot(torch.tensor(ids), num_classes=100352).float()
  d = 64; W_Q = nn.Linear(100352, d, bias=False); W_K = nn.Linear(100352, d, bias=False); W_V = nn.Linear(100352, d, bias=False)
  Q, K, V = W_Q(X), W_K(X), W_V(X)
  scores = Q @ K.T / (d ** 0.5)        # (N, N)
  attn = torch.softmax(scores, dim=-1)
  out = attn @ V                       # (N, d)
  ```
- **faded**: 给出上面代码, 但删掉 `scores = ...` 与 `attn = ...` 两行, 学生补全 (含 √d_k 缩放与 softmax 维度)。
- **solo**: 学生独立写完, 并额外打印 attn 矩阵中 (i,j) 最大的 3 个词对, 解释为何"智能"与"助手"相互注意力高。
- **feedback_rule**: 自动检查 (a) 是否含 `/ (d ** 0.5)` (b) softmax dim 是否为 -1 (c) 输出 shape 是否为 (N, d)。若 (a) 缺失, 提示 "GPT-2 small d_k=64, 不缩放时 softmax 输入方差 ~64, 梯度会饱和--回去看 DQ1"。若 (c) shape 错, 提示 "V 的形状是 (N, d), attn @ V 不能转置 V"。

### drill_id: D2
- **target_subskill**: S-B
- **difficulty**: 3
- **reps_required**: 3
- **task**: 给定 4 个 LLM 故障案例 (营销 Agent 真实场景), 判断属于 Pre-training / SFT / Alignment 哪一阶段, 并写修复方向。
- **worked_example** (完整示范):
  - 案例: "模型输出的营销文案事实正确、语法通顺, 但用户让它写 3 句话它写 5 段。" → 故障在 **SFT** (指令遵循不够, Pre-training 知识没问题, Alignment 通常只做安全不做长度约束)。修复: 加 SFT 数据, 标注 "请用 3 句话回答" 的样本。
- **faded**: 给出案例 "模型把竞品名字写错" → 学生补: 故障阶段 = ? 修复 = ? (提示: 事实错误通常是 Pre-training 知识不足或 tokenizer 边界)
- **solo**: 学生独立诊断剩余 3 案例 (含 "模型拒绝写营销文案说涉及诱导消费" / "文案千篇一律像模板" / "中文文案夹英文 token 导致乱码")。
- **feedback_rule**: 用 LLM-as-judge 静态 rubric 检查 (a) 是否明确写出阶段名 (b) 是否给出 >=1 条数据层修复 (加预训练 token / 加 SFT 对 / 重做 DPO 偏好对)。若学生把"不安全"归到 SFT, 提示 "RLHF/DPO 才是安全对齐, SFT 只教指令格式--回看 notes.md 训练三阶段表"。

### drill_id: D3
- **target_subskill**: S-C
- **difficulty**: 2
- **reps_required**: 3
- **task**: 用 tiktoken (cl100k_base) 和 transformers AutoTokenizer (gpt2) 对 5 条中英文营销文案做 tokenization, 统计 token 数, 按 GPT-4o 定价 ($5/M input) 计算单次推理成本, 推算日均 10000 次请求的月成本。
- **worked_example** (完整示范):
  ```python
  import tiktoken
  from transformers import AutoTokenizer
  tk = tiktoken.get_encoding("cl100k_base")
  gpt2 = AutoTokenizer.from_pretrained("gpt2")
  zh = "限时特惠买一送一"; en = "Limited time offer, buy one get one free"
  print(len(tk.encode(zh)), len(tk.encode(en)))    # ~10 vs ~8
  print(len(gpt2.encode(zh)), len(gpt2.encode(en)))# GPT-2 BPE 中文更碎
  ```
- **faded**: 给出代码, 删掉定价计算行, 学生补 `cost = n_tokens * 5 / 1_000_000 * 10000 * 30`。
- **solo**: 学生独立完成 5 条文案的对比表, 并回答 "为什么同一意思中文比英文贵 1.5-2 倍" (提示: BPE 词表英文优先, 中文被切成更多 byte token)。
- **feedback_rule**: 自动检查 (a) 是否同时用 tiktoken 和 gpt2 tokenizer (b) 是否给出 $ 单位成本 (c) 是否解释中英文差异。若学生只给 token 数不解释原因, 提示 "GPT-2 BPE 词表 50257 中英文 token 占比不均, 中文走 byte fallback--回看 notes.md Tokenization 节"。

### drill_id: D4
- **target_subskill**: S-A + S-B
- **difficulty**: 4
- **reps_required**: 3
- **task**: 手写一个 Transformer Block (Multi-Head Attention + FFN 4x 扩展 + 残差 + LayerNorm), 在 GPT-2 config (n_layer=12, n_head=12, n_embd=768) 下跑一次前向, 并回答: Pre-training 阶段哪一类参数 (QKV / FFN / LayerNorm) 对"知识存储"贡献最大?
- **worked_example** (完整示范):
  ```python
  class TransformerBlock(nn.Module):
      def __init__(self, d=768, h=12):
          super().__init__()
          self.ln1 = nn.LayerNorm(d); self.ln2 = nn.LayerNorm(d)
          self.attn = nn.MultiheadAttention(d, h, batch_first=True)
          self.ffn = nn.Sequential(nn.Linear(d, 4*d), nn.GELU(), nn.Linear(4*d, d))
      def forward(self, x):
          a, _ = self.attn(x, x, x, need_weights=False)
          x = self.ln1(x + a)
          f = self.ffn(x)
          return self.ln2(x + f)
  ```
  知识存储主要在 **FFN** (4×d 扩展 = 2.36M 参数/layer × 12 layer = 28.3M, 占 GPT-2 small 124M 的 ~23%, 且 GeLU 非线性形成键值存储)。
- **faded**: 删掉残差与 ln2, 学生补 `x = self.ln2(x + f)`。
- **solo**: 学生独立写完, 并把 QKV 参数量 (3 × 768² = 1.77M/layer) 与 FFN 参数量对比, 写一段 100 字解释 "为什么 MoE 替换 FFN 而不是 Attention"。
- **feedback_rule**: 自动检查 (a) 是否含残差 `x + a` 与 `x + f` (b) LayerNorm 是否在残差外 (Post-LN) 或内 (Pre-LN, 都接受, 但要标注) (c) FFN 是否 4× 扩展。若学生把 MoE 写成替换 Attention, 提示 "DeepSeek-MoE 替换的是 FFN, Attention 仍 Dense--回看 notes.md DeepSeek-MoE 节"。

### drill_id: D5
- **target_subskill**: S-C
- **difficulty**: 5
- **reps_required**: 3
- **task**: 从 `AutoConfig.from_pretrained("gpt2")` 读 n_layer=12/n_head=12/n_embd=768/vocab_size=50257, 推算 GPT-2 small 总参数量 (~124M), 再推算 DeepSeek-MoE (671B total / 37B active) 在相同质量下推理成本节省倍数, 给营销 Agent 的日均万次请求算一笔账。
- **worked_example** (完整示范):
  - Embedding: 50257 × 768 = 38.6M
  - Per-layer: QKV 3×768² + FFN 2×768×3072 + LN ≈ 7.1M; ×12 = 85.2M
  - Total ≈ 38.6 + 85.2 + 0.4 (final LN) ≈ 124M ✓
  - DeepSeek-V3: 671B total / 37B active = 激活比 5.5%, 单次推理 FLOPs ~ Dense 37B 的成本, 而非 671B 的成本 → 节省 ~18 倍 vs 同质量 Dense。
- **faded**: 给出公式, 删掉 12 层乘法, 学生补 `× 12`。
- **solo**: 学生独立推算 GPT-2 medium (n_layer=24, n_embd=1024) 参数量, 并回答 "Scale Law 对营销 Agent 选型意味着什么" (提示: 中小营销场景 GPT-4o-mini 或 7B SFT 已够, 不必上 671B)。
- **feedback_rule**: 自动检查 (a) Embedding 是否含 vocab×d (b) per-layer 是否含 QKV+FFN (c) 是否给出 MoE 激活比 = active/total。若学生算 124M 时漏掉 Embedding, 提示 "GPT-2 的 embedding 占 31% 参数, 不是小头--回看 notes.md GPT-2 config 节"。

---

## 4. progressive_project (CS230 式 4 阶段交付)

> 贯穿 Day 1 上机的渐进项目。每阶段独立评分, 后阶段依赖前阶段。

| 阶段 | 交付物 | 评分 rubric | 占比 |
|------|--------|------------|------|
| proposal | 选定一个营销场景 (如"母婴品牌短文案生成")+ 模型选型 (GPT-4o-mini / 7B SFT / DeepSeek-V3 MoE 三选一, 含成本预估) | 场景具体 + 选型有数据支撑 | 15% |
| milestone | 跑通 D1 (手写 Self-Attention) + D3 (tokenization 成本), 输出注意力矩阵截图 + 成本表 | 代码能跑 + 数值合理 | 25% |
| final | D2 三阶段故障诊断报告 (>=3 案例) + D5 参数量推算 + Scale Law 选型论证 | 诊断准确 + 推算误差 <10% | 40% |
| poster | 一页 A4 海报: "营销 Agent 的 Transformer 内核与成本账", 含 1 张注意力图 + 1 张成本柱状图 + 3 句话结论 | 可被非技术同事看懂 | 20% |

---

## 5. interleaving (交叉排布, 不块状)

> 不按 A-A-A-B-B-B-C-C-C 块状练习, 而按 A1-B1-C1-A2-B2-C2-A3-B3-C3 交叉, 促进迁移 (Rohrer 2007)。

**本单元交叉顺序** (9 个 session, 每 session 25 分钟):

| session | drill | subskill | 变体 |
|--------|-------|----------|------|
| 1 | D1-worked | S-A | 营销文案 "智能助手省时省力" |
| 2 | D2-worked | S-B | 故障案例 "知识对不听指令" |
| 3 | D3-worked | S-C | 5 条中英文文案 tokenization |
| 4 | D1-faded | S-A | 改文案为 "618 全场五折" |
| 5 | D2-faded | S-B | 新案例 "竞品名写错" |
| 6 | D3-faded | S-C | 改用 GPT-2 tokenizer 对比 |
| 7 | D1-solo | S-A | 学生自选文案 + 注意力矩阵 |
| 8 | D2-solo | S-B | 学生自选 3 故障案例诊断 |
| 9 | D3-solo | S-C | 学生自选 5 文案 + 成本表 |

> 第 10-12 session 可插入 D4 / D5 (高难度, 留给已过 D1-D3 的学生)。块状顺序 (D1×3 → D2×3 → D3×3) 是**反模式**, 会让学生在 session 4 时已忘 D1。

明文交叉序列: `D1 → D2 → D3 → D1 → D2 → D3 → D1 → D2 → D3 → (D4 → D5 → 回路)`

---

## 6. retry_policy (CS230 式, 失败不罚分)

- **10 free late days**: 整个 Day 1 单元有 10 个"迟到日"配额, 学生可任意分配到 4 阶段交付物, 不扣分。
- **失败重试不罚分**: 任一 drill 的 Solo 阶段未达 mastery (>=80%) 可重做, 最终分取最高分, 不计重试次数。
- **Worked/Faded 不评分**: 仅 Solo 阶段评分, 鼓励在 Worked/Faded 阶段充分试错。
- **跨阶段依赖豁免**: 若 milestone 因 D1 未过被卡, 学生可用 proposal 的"文字推演"替代代码跑通, 不阻塞 final 阶段。

---

## 7. weak_loop (连续 2 次失败触发弱项循环)

> 监测: 每次 Solo 提交后, 系统记录 pass/fail。**连续 2 次 fail 同一 subskill** → 触发弱项循环。

**弱项循环流程** (以 S-A 连续 2 次 fail 为例):

1. **回退**: 退回上一难度 drill (D1-solo fail 2 次 → 回 D1-faded)。
2. **补充 worked example**: 系统推送一个**新的** worked example (变体文案, 如 "618 全场五折"), 学生只读不写。
3. **概念重检**: 推送 notes.md "关键回顾 1: Self-Attention" 段落 + 一道 5 题选择题 (含 √d_k 缩放、softmax dim、Q/K/V 角色)。
4. **重做 Solo**: 用**第 3 个变体**文案重做 Solo, 不与原题重复。
5. **若再 fail**: 触发 tutorial.ipynb 的 1-on-1 Socratic session (限频每天 1 次), 由 tutorial 引导学生口述 Q/K/V 流程。

**退出条件**: Solo 达 >=80% → 退出弱项循环, 回主 interleaving 序列。若 3 次循环仍未过, 退出循环并标记"需人工辅导", 不再自动重试 (防挫败)。

---

## 8. 与 v5.0 starter/solution 的衔接

| drill | 对应 starter TODO | 对应 solution |
|-------|------------------|---------------|
| D1 | TODO3 (手写 Self-Attention) | solution TODO3 |
| D2 | TODO6 (训练三阶段概述) | solution TODO6 |
| D3 | TODO1 (tiktoken + GPT-2 tokenizer) | solution TODO1 |
| D4 | TODO4 (Multi-Head + Transformer Block) | solution TODO4 |
| D5 | TODO2 (GPT-2 config 参数推算) | solution TODO2 |

> D1-D5 是 starter TODO 的"刻意练习放大版": starter TODO 是一次性填空, drill 是 Worked-Faded-Solo 三阶段 + 交叉排布 + 弱项循环。

---

*v6.0 practice.md · 锚定 Ericsson deliberate practice + MIT/CS229 pset0 diagnostic + Harvard/Stanford Worked-Faded + CS230 progressive project + Rohrer interleaving。*
