# R2 行动研究 · 建构对齐 (Constructive Alignment, Biggs 1996)

> 基于 Biggs (1996) 建构对齐: ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐。
> mastery_threshold 引用 Bloom 掌握学习 (1968): 学生必须达到阈值才进入下一单元。
> 本单元引用 v5.0 文件: `notes.md` / `starter.ipynb` / `solution.ipynb` / `reading.md` / `data/README.md`, 以及 v6.0 新增 `practice.md` / `tutorial.ipynb`。

---

## 1. ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---------------------|---------------------|----------------|-------------------|
| ILO1: 能阐述行动研究的认识论基础 (research as intervention, change agent 角色), 并与 Case Study/DSR 做认识论层区分 | ① 读 `notes.md` § 关键回顾 1/5 (AR vs DSR vs Case Study 对比表) <br> ② 完成 `practice.md` D3 阶段 1-3 (trustworthiness 量化) <br> ③ 在 `tutorial.ipynb` 接受 Socratic 追问"为什么 AR 用 trustworthiness 而非 internal validity" | `solution.ipynb` TODO5 (AR vs DSR 认识论对比表) + `practice.md` 先测 Q1 | >=80% TODO5 正确 + Q1 命中"研究者作为干预者"关键点 |
| ILO2: 能用 pandas 建模 4 轮 Plan-Act-Observe-Reflect 循环, 分析 KPI 改善幅度, 识别高杠杆轮次 | ① 做 `starter.ipynb` TODO1 (AR 循环数据构建) + TODO2 (KPI 改善分析) <br> ② 完成 `practice.md` D1 (AR 循环建模) + D2 (高杠杆轮次) <br> ③ 读 `data/README.md` 4 轮真实文献 KPI | `solution.ipynb` TODO1+TODO2 + `practice.md` D1/D2 阶段 3 独立解 | >=80% TODO1+TODO2 正确 + D2 阶段 3 独立通过 |
| ILO3: 能量化评估 AR 效度 (三角验证数据源数 + 成员校验率 + 反思性评分) 并识别不合格轮次 | ① 读 `notes.md` § 关键回顾 4 (trustworthiness 四准则) <br> ② 做 `starter.ipynb` TODO3 (效度评估) <br> ③ 完成 `practice.md` D3 (trustworthiness 综合分) | `solution.ipynb` TODO3 + `practice.md` D3 阶段 3 独立解 | >=80% TODO3 正确 + D3 阶段 3 trustworthiness 综合分在 [0,1] 且不合格轮次标注非空 |
| ILO4: 能设计 PAR 利益相关方共创方案, 用权力-利益矩阵分析共创度演化 | ① 读 `notes.md` § 关键回顾 3 (PAR + power-interest grid) <br> ② 做 `starter.ipynb` TODO4 (PAR 利益相关方分析) <br> ③ 完成 `practice.md` D5 (PAR 共创度) | `solution.ipynb` TODO4 + `practice.md` D5 阶段 3 独立解 | >=80% TODO4 正确 + D5 阶段 3 四象限标注与 power/interest 列一致 |
| ILO5: 能用 Beta-Binomial 共轭贝叶斯更新, 从每轮观察数据推断"干预有效"的后验概率, 量化 AR 不确定性 | ① 读 `notes.md` § 贝叶斯更新与行动研究 <br> ② 做 `starter.ipynb` TODO7 (贝叶斯干预评估) <br> ③ 完成 `practice.md` D4 (贝叶斯后验更新) | `solution.ipynb` TODO7 + `practice.md` D4 阶段 3 独立解 (后验 α'/β' + 95% HDI) | >=80% TODO7 正确 + D4 阶段 3 后验均值在合理区间 [0.3, 0.9] |
| ILO6: 能用天道推演视角说明 Plan 阶段的沙盘推演如何减少试错成本 (连接 CLAUDE.md 天道推演系统) | ① 读 `notes.md` § 天道推演作为行动研究的预演工具 <br> ② 在 `tutorial.ipynb` 接受 Socratic 追问"天道推演的 5 项能力如何映射到 Plan 阶段" <br> ③ 写 500 字天道推演反思 (Final 阶段) | `practice.md` Final 阶段 500 字天道推演反思 + `tutorial.ipynb` student_model.json 的 `blind_spots` 字段 | 反思命中 >=3 项天道推演能力 (局势感知/因果链/沙盘/概率/最优路径) |

---

## 2. 三自检问题 (Feed Up / Feed Back / Feed Forward)

### Q1: Feed Up — TLA 是否训练 ILO?
- **检查**: 每个 ILO 是否至少有 1 个 TLA 直接训练它?
- **本单元自检**:
  - ILO1 (认识论) -> TLA①读 notes.md § 关键回顾 1/5 ✓ + TLA②practice.md D3 ✓ + TLA③tutorial Socratic ✓
  - ILO2 (pandas 循环建模) -> TLA①starter TODO1+2 ✓ + TLA②practice D1+D2 ✓ + TLA③data/README ✓
  - ILO3 (效度量化) -> TLA①notes § 关键回顾 4 ✓ + TLA②starter TODO3 ✓ + TLA③practice D3 ✓
  - ILO4 (PAR 共创) -> TLA①notes § 关键回顾 3 ✓ + TLA②starter TODO4 ✓ + TLA③practice D5 ✓
  - ILO5 (贝叶斯) -> TLA①notes § 贝叶斯更新 ✓ + TLA②starter TODO7 ✓ + TLA③practice D4 ✓
  - ILO6 (天道推演) -> TLA①notes § 天道推演预演 ✓ + TLA②tutorial Socratic ✓ + TLA③500 字反思 ✓
- **结论**: 全部 ILO 有 >=3 个 TLA 训练, Feed Up 对齐 ✓

### Q2: Feed Back — AT 是否测量 ILO?
- **检查**: 每个 AT 是否直接测量对应的 ILO, 而非测量别的?
- **本单元自检**:
  - AT for ILO1 = solution.ipynb TODO5 (AR vs DSR 对比表) — 直接测量认识论区分 ✓
  - AT for ILO2 = solution.ipynb TODO1+TODO2 — 直接测量 pandas 循环建模与 KPI 改善 ✓
  - AT for ILO3 = solution.ipynb TODO3 — 直接测量 trustworthiness 量化 ✓
  - AT for ILO4 = solution.ipynb TODO4 — 直接测量 PAR 权力-利益矩阵 ✓
  - AT for ILO5 = solution.ipynb TODO7 — 直接测量贝叶斯后验更新 ✓
  - AT for ILO6 = 500 字天道推演反思 — 直接测量天道推演映射能力 ✓
- **结论**: 全部 AT 精准测量对应 ILO, Feed Back 对齐 ✓

### Q3: Feed Forward — 不经 TLA 能过 AT 吗? 若能 = 对齐失败
- **检查**: 是否存在"绕过 TLA 直接刷 AT 答案"的捷径? 若存在, 对齐失败。
- **本单元自检**:
  - TODO5 (AR vs DSR 对比表) 不读 notes.md § 关键回顾 5 能过吗? 不能 — 表中 7 个维度 (认识论/角色/产出/循环/效度/学者/场景) 必须从 notes.md 提取, 无捷径 ✓
  - TODO1 (AR 循环数据构建) 不做 practice.md D1 能过吗? 不能 — 4 轮 × 4 KPI 的 schema 设计需要 D1 训练, 直接抄 solution 算抄袭 ✓
  - TODO7 (贝叶斯后验) 不做 practice.md D4 能过吗? 不能 — Beta-Binomial 共轭需要 D4 的 worked-faded 三阶段训练, 未训练学生无法正确推导 α'/β' ✓
  - 500 字天道推演反思不读 notes.md § 天道推演预演能过吗? 不能 — 5 项能力的名称必须从 notes.md 提取 ✓
- **结论**: 全部 AT 必须经 TLA 才能通过, Feed Forward 对齐 ✓ (无捷径)

---

## 3. mastery 阈值执行规则

- 任何 ILO 的 AT 正确率 < 80% → 触发 `practice.md` § 7 弱项循环 (连续 2 次失败 → 回退阶段 1 worked example)
- 全部 6 个 ILO 达到 mastery_threshold → 解锁 R3 (混合方法) 单元
- 单个 ILO 未达 mastery, 其他 ILO 仍可继续推进, 但该 ILO 必须在 Final 阶段前补齐

---

## 4. 对齐图 (可视化)

```
ILO1 (认识论) ─┬─> notes § 关键回顾 1/5 ─┬─> solution TODO5 ─> >=80%
               ├─> practice D3            │
               └─> tutorial Socratic ─────┘

ILO2 (pandas) ─┬─> starter TODO1+2 ───────┬─> solution TODO1+2 ─> >=80%
               ├─> practice D1+D2 ────────┤
               └─> data/README ───────────┘

ILO3 (效度) ───┬─> notes § 关键回顾 4 ────┬─> solution TODO3 ─> >=80%
               ├─> starter TODO3 ─────────┤
               └─> practice D3 ───────────┘

ILO4 (PAR) ────┬─> notes § 关键回顾 3 ────┬─> solution TODO4 ─> >=80%
               ├─> starter TODO4 ─────────┤
               └─> practice D5 ───────────┘

ILO5 (贝叶斯) ─┬─> notes § 贝叶斯更新 ────┬─> solution TODO7 ─> >=80%
               ├─> starter TODO7 ─────────┤
               └─> practice D4 ───────────┘

ILO6 (天道) ───┬─> notes § 天道推演预演 ───┬─> 500字反思 ─> >=3能力命中
               └─> tutorial Socratic ─────┘
```
