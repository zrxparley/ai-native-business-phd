# 刻意练习 · 多模态融合与跨域对齐 (v6.0)

> 本单元刻意练习基于 Ericsson 刻意练习五要素 + MIT Open Learning 提取练习/交叉/Worked-Faded。所有 drill 围绕 transformers CLIP/BLIP-2 真实库与对比学习对齐展开。

## skill_target

能在 90 分钟内独立实现一个**多模态融合 + 跨域对齐**原型：用 transformers CLIP/BLIP-2 编码真实图文、用 InfoNCE + 对称损失训练对齐、用 zero-shot 分类评估对齐质量，并解释温度参数 τ、Q-Former、原生多模态演进对企业营销架构的影响。

## subskills

- **S1 融合策略**：实现并区分早融合（MLP 拼接）/中融合（注意力）/晚融合（决策加权），能在广告创意场景选择合适策略
- **S2 对比学习对齐**：从零实现 InfoNCE + CLIP 对称损失，理解 τ 对分布尖锐度的影响，能诊断"正负样本相似度差距"
- **S3 跨域应用与前沿**：用 CLIP 做图文检索与零样本分类，用 BLIP-2 做 image captioning/VQA，能对比 CLIP→BLIP-2→LLaVA→GPT-4o 四阶段演进

## diagnostic (3 道，前测)

> 开练前先做。每题 60 秒，不会写就写"我不会，卡在 ___"。这是 retrieval practice，不是评分。

1. **D-1**：写出 InfoNCE 损失公式，并说明当 τ→0+ 时分布如何变化。CLIP 为何还要再加一个对称的 text2img 损失？
2. **D-2**：给定 4 张产品图 + 4 段文案，CLIP 返回 4×4 余弦相似度矩阵。请写出 top-k 检索的伪代码（image-to-text），并指出"对齐成功"在矩阵上的视觉特征。
3. **D-3**：BLIP-2 的 Q-Former 夹在冻结 ViT 和冻结 LLM 之间，为什么要这样设计？相比 CLIP 双塔，Q-Former 解决了什么双塔做不到的事？

## drills (>=3)

### drill_id: D1
**difficulty**: 3
**reps_required**: 3
**feedback_rule**:
- 若学生 τ 写死成 1.0 或漏掉 softmax 分母 -> 提示"InfoNCE 分母必须有 sum over negatives，τ 是除在 logit 上不是除在 loss 上"；让其重看 CLIP 原文式 (1)。
- 若学生只写了 img2text 一个方向 -> 提示"CLIP 是对称损失，必须 text2img 也算一遍并取平均"；让其补 symmetric_loss 函数。
- 若学生对角线对齐但不收敛 -> 提示检查温度 τ 是否过大（>0.5 平坦）或 embedding 是否 L2 归一化。
- 关联真实库：参考 `transformers.CLIPModel.logit_scale` 与 `F.cross_entropy` 对称写法。
**worked_faded**:
- Stage 1 (Worked)：完整示范一个 2×2 的 InfoNCE 计算手算过程，每步数字标出。
- Stage 2 (Faded)：给出 symmetric CLIP loss 函数骨架，留 3 处 `# 你的代码`（τ 缩放、softmax、对称项）让学生填。
- Stage 3 (Independent)：学生独立实现 `info_nce_loss(z_img, z_text, tau)` 并跑温度实验 τ ∈ {0.01, 0.07, 0.5}，画相似度矩阵热力图。

### drill_id: D2
**difficulty**: 4
**reps_required**: 3
**feedback_rule**:
- 若学生用 `CLIPProcessor` 但忘了 `return_tensors="pt"` -> 提示"processor 输出需是 batched tensor，否则 CLIPModel 报维度错"。
- 若学生 top-k 检索时混淆 dim=0/dim=1 -> 提示"image-to-text 是按行找 top-k（每张图找最匹配文案），text-to-image 是按列"；让其画 4×4 矩阵箭头。
- 若零样本分类准确率接近随机 -> 提示检查 prompt template（"a photo of a {label}" vs 单词），让其对比 4 种 prompt 的差距，理解 CLIP prompt engineering。
- 关联真实库：`CLIPModel.get_text_features` / `get_image_features` 必须分两次调，不要混。
**worked_faded**:
- Stage 1 (Worked)：完整示范 1 张图 + 4 段文案的图文检索（编码→相似度→top-1→对齐差距分析），每步打印 shape。
- Stage 2 (Faded)：给出 4×4 检索函数骨架，留 4 处 `# 你的代码`（归一化、相似度矩阵、top-k idx、margin 计算）。
- Stage 3 (Independent)：学生独立实现 `image_to_text_retrieval(images, texts, k=2)` 并在 3 张模拟产品图上跑通，输出对齐 margin（diag - offdiag_mean）。

### drill_id: D3
**difficulty**: 5
**reps_required**: 3
**feedback_rule**:
- 若学生用 `BlipForConditionalGeneration` 做 VQA 但没传 `text=` question -> 提示"VQA 是 conditional generation，必须把问题作为 text 输入"；让其对比 caption 和 VQA 的 API 差异。
- 若学生架构图缺少"对齐层"或把 CLIP 和 BLIP-2 混在一个塔 -> 提示"CLIP 是双塔对齐（检索），BLIP-2 是 Q-Former 桥接（生成），架构图要分两路"。
- 若学生解释 GPT-4o 原生多模态时只说"更强大" -> 提示"原生 = 同一 token 空间，不再编码后对齐"；让其对比 CLIP 双塔与 GPT-4o 端到端的延迟差。
- 关联真实库：`BlipProcessor(images=..., text=question, return_tensors="pt")` + `model.generate(...)`。
**worked_faded**:
- Stage 1 (Worked)：完整示范 BLIP-2 captioning + VQA 两条 API 调用链 + ASCII 架构图（编码层/融合层/对齐层/存储层）。
- Stage 2 (Faded)：给出企业架构图骨架（4 层 + 模块连线），留 5 处 `# 你的模块` 让学生填（向量库选型、Q-Former 位置、对比损失层、在线/离线分离、瓶颈标注）。
- Stage 3 (Independent)：学生独立设计"广告创意图文匹配系统"架构，评估每个模块延迟（编码/检索/对齐/生成），标注 2 个瓶颈 + 1 个单点故障。

## progressive_project

渐进式项目脚手架（参考 MIT 6.5940 / CS230 milestone 思路）：

- **Milestone 1 (Day 4 上机当堂)**：完成 starter.ipynb 6 个 TODO，跑通 CLIP 图文检索 + BLIP captioning。
- **Milestone 2 (Week 2)**：把模拟图片换成真实产品图（自家商品图或公开数据集），用 CLIP zero-shot 给 50 张图自动打标签，报告 top-1 准确率与 confusion matrix。
- **Milestone 3 (Week 4, Capstone 衔接)**：设计并实现一个端到端"广告创意图文匹配"原型：CLIP 检索（召回）+ BLIP-2 captioning（生成解释）+ 架构图 + 延迟评估。这是 Day 5 系统设计的基础。

## interleaving

**明文交叉排布 A1B1C1 → B2C2A2 → C3A3B3**（不块状练习）：

- A = 融合策略类 drill（D1 子任务）
- B = 对比学习对齐类 drill（D2 子任务）
- C = BLIP-2/架构类 drill（D3 子任务）

具体排布（每次练习 30 分钟，每 10 分钟切一类）：

```
Session 1: A1(早融合 MLP)  → B1(InfoNCE 手算 2×2) → C1(BLIP captioning 调用)
Session 2: B2(CLIP 检索代码) → C2(架构图 4 层填空) → A2(中融合注意力)
Session 3: C3(企业架构瓶颈) → A3(晚融合决策加权) → B3(τ 实验 + 热力图)
```

理由：A/B/C 三类共享"图文表示"底座但调用不同脑区（实现/对齐/设计）。块状练习会让学生短期看似熟练但 1 周后混淆；A1B1C1 交叉强制每次都重新 load context，长期保留率提升 (Butler 2010, Rohrer 2012)。

## retry_policy

- 单次 drill 失败：48 小时内可重试，重试前必须先回看 worked example 1 遍。
- 单次 drill 连续 2 次失败：触发 `weak_loop`（见下），不允许直接第 3 次硬冲。
- Milestone 逾期：CS230 风格，每逾期 1 天扣 20% 该 milestone 分数，最多扣到 0；可使用 2 次"宽限日"（每学员每学期总共 10 天池子）。
- 整单元 retry 上限：3 次/单元，超过则必须预约 1:1 tutorial。

## weak_loop

**连续 2 次失败触发弱项循环**：

1. 回退到当前 drill 的上一 Stage（如 D2 Stage 3 失败 → 退回 D2 Stage 2 Faded）。
2. 补充 1 个 worked example（教师手算/手写完整过程，学生 5 分钟内复读）。
3. 学生口头复述 worked example 的关键步骤（retrieval practice，不复述不让进 Stage 3）。
4. 24 小时间隔后重试 Stage 3（不是立刻重试，spaced retrieval 比 massed practice 保留率高 2 倍）。
5. 若仍失败：换一个 modality 的同难度 drill（如 D2→D1 同 Stage 3），用交叉练习打破"卡在一种表述"的僵局。
6. 若 3 轮 weak_loop 仍未通过：升级到 1:1 Oxford tutorial（tutorial.ipynb persona），Socratic 追问定位认知盲点。

---

*本刻意练习设计基于 Ericsson (1993) deliberate practice + MIT Open Learning extraction/interleaving/worked-faded + CS230 retry policy + Butler (2010) retrieval practice 证据。*
