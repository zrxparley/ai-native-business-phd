# 建构对齐矩阵 (Constructive Alignment, Biggs 1996) · Capstone Phase 5

> 理论基础: Biggs (1996) constructive alignment - ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者对齐; mastery learning (Bloom 1968) 要求达到阈值才算掌握。
> 本单元 AT 全部引用 starter.ipynb / solution.ipynb / tutorial.ipynb 的真实任务, TLA 引用 drills / starter TODO / tutorial Socratic loop。

---

## ILO ↔ TLA ↔ AT 对齐矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 pandas 构建 AI 适配商业模式画布 9 宫格, 价值主张整合 Phase 4 ATE | 阅读 notes.md § 关键回顾 1 + 完成 practice.md D1 Stage A/B/C (worked-faded) + starter.ipynb TODO1 | solution.ipynb TODO1 输出 9 行 DataFrame, 价值主张含 "+ 因果验证 ATE=3.8pp" | 9 格全填 + 价值主张必含 "因果验证" 字样 (>=80%) |
| **ILO2**: 能用 numpy-financial 把 Phase 4 ATE 推导为 NPV/IRR/PI/回收期, 判断投资可行性 | notes.md § 关键回顾 2 + practice.md D1 + starter.ipynb TODO2/TODO3 | solution.ipynb TODO2/3: `npf.npv` + `npf.irr` 输出四指标 | NPV 量级合理 ($100K-$10M), IRR > 折现率, PI > 1 (>=80%) |
| **ILO3**: 能用 scipy.stats 蒙特卡洛 (truncnorm, N>=10000) 传播 ATE CI, 输出 P(NPV>0) | notes.md § 关键回顾 4 + practice.md D2 + starter.ipynb TODO4 | solution.ipynb TODO4: 直方图 + P(NPV>0) 数值 | N=10000, P(NPV>0)∈[0,1], 直方图含 95% CI 标注 (>=80%) |
| **ILO4**: 能用 matplotlib 画龙卷风图识别 NPV 高杠杆因子 (ATE/推理成本/毛利率) | notes.md § 2026前沿 + practice.md D3 + starter.ipynb TODO5 | solution.ipynb TODO5: 龙卷风图按 \|ΔNPV\| 降序, 三因子全出现 | 三因子出现 + 排序正确 + 推理成本排名合理 (>=80%) |
| **ILO5**: 能用天道推演做 Bull/Base/Bear 三路径 (每路径 immediate/near/far 三层) | notes.md § 天道推演×投资评估 + practice.md D3 Stage C + starter.ipynb TODO6 | solution.ipynb TODO6: 三路径表 + 300 字投资建议 | 三路径×三层全填 + Bear=CI 下界 / Bull=CI 上界 (>=80%) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### Q1 (Feed Up): TLA 是否训练 ILO?
- ILO1 的 TLA 是否让学生真的画 9 宫格? 是 - D1 Stage A 给完整示例, B 填空, C 独立; starter TODO1 直接产出 DataFrame。
- ILO3 的 TLA 是否让学生真跑蒙特卡洛? 是 - D2 Stage A 示范 truncnorm, B 填空 size/scale, C 独立写循环。
- ILO5 的 TLA 是否让学生真做三路径推演? 是 - D3 Stage C 要求 Bull/Base/Bear × immediate/near/far。
- **判定**: TLA->ILO 训练链完整, Feed Up 通过。

### Q2 (Feed Back): AT 是否测量 ILO?
- AT1 (solution TODO1 输出) 是否测 ILO1 (画 9 宫格)? 是 - 直接对应, 检查 "因果验证" 字样。
- AT3 (P(NPV>0) 数值) 是否测 ILO3 (蒙特卡洛)? 是 - 数值与直方图是直接产物。
- AT5 (龙卷风图排序) 是否测 ILO4 (高杠杆因子)? 是 - 排序即测量理解。
- **判定**: AT->ILO 测量链完整, Feed Back 通过。

### Q3 (Feed Forward): 不经 TLA 能过 AT 吗? 若能 = 对齐失败
- 不做 D1 (TLA) 能否过 TODO1 (AT)? 不能 - 9 宫格 DataFrame 需要画布框架知识, 不练 worked-faded 难独立完成。
- 不做 D2 (TLA) 能否过 TODO4 (AT)? 不能 - truncnorm 参数 (a, b, loc, scale) 不练会写错, N<10000 不达标。
- 不做 D3 (TLA) 能否过 TODO5/6 (AT)? 不能 - 龙卷风图排序逻辑 + 三路径三层推演不练不会。
- **判定**: 无 TLA 则 AT 不可过, 对齐成功, Feed Forward 通过。

---

## mastery 阈值与补救

- 每条 ILO 的 AT 必须达到 mastery_threshold (>=80%) 才算掌握。
- 未达阈值: 触发 practice.md 的 weak_loop - 回退 Stage A + 补充 worked example + reps +2。
- 全部 5 条 ILO 达阈 = 本单元 pass, 可进入 Phase 6。
- tutorial.ipynb 的 Socratic loop 会优先追问未达阈的 ILO 对应 subskill (查 student_model.json)。

---

## 引用

- Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*.
- Bloom, B. (1968). Learning for Mastery.
- Hattie, J. (2009). Visible Learning. (4 级反馈见 tutorial.ipynb)
- 本单元 notes.md § 关键回顾 1-4 + § 2026前沿
