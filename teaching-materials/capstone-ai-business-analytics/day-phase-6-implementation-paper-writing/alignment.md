# Phase 6 建构对齐 (Constructive Alignment, Biggs 1996 + Mastery Learning)

> **核心命题**：ILO (Intended Learning Outcome, 预期学习产出) ↔ TLA (Teaching/Learning Activity, 教学学习活动) ↔ AT (Assessment Task, 评估任务) 三者必须对齐。任何 AT 都必须由前置 TLA 训练；不经 TLA 能过 AT = 对齐失败。

---

## 一、ILO ↔ TLA ↔ AT 对齐矩阵

| ILO (预期学习产出, 学完能做到) | TLA (教学学习活动, 引用本单元材料) | AT (评估任务, 引用本单元材料) | mastery_threshold (过关阈值) |
|---|---|---|---|
| **ILO1**: 能用 DSR 六步框架（Hevner 2004 / Peffers 2007）把 Phase 1-5 整合为完整 Capstone artifact | 读 `notes.md` § 关键回顾 2 + `practice.md` drill D1 三阶段 worked-faded + `tutorial.ipynb` 苏格拉底追问 DSR Step 4 演示为何不能跳过 | `solution.ipynb` TODO1 (DSR Artifact 设计) 后测 + `practice.md` D1 Stage 3 (写 600-800 字 Discussion 含天道推演特色章节) | D1 Stage 3 论文 Discussion 段含 ≥3 个 DSR 传播要素 + 天道推演同构表 5 行齐; deepeval DSR 维度 ≥8/10 |
| **ILO2**: 能用 langsmith @traceable 构建可复现 trace 存档 + deepeval LLM-as-a-judge 五维评估 | 读 `notes.md` § 关键回顾 1 (端到端流水线) + `practice.md` drill D2 三阶段 + `tutorial.ipynb` 苏格拉底追问"trace hash 凭什么防版本漂移" | `solution.ipynb` TODO2 + TODO6 (langsmith trace 存档 + deepeval BaseMetric/GEval 评估) + `practice.md` D2 Stage 3 (5 维评分 JSON) | D2 Stage 3 输出 5 维评分 (0-10) 每维附改进建议; trace 存档含 ≥4 个 LangGraph 节点调用; deepeval 可复现性维度 ≥7/10 |
| **ILO3**: 能用 statsmodels + scipy 在 NSW RCT (N=445) 上跑 t 检验/Cohen's d/卡方检验并写 APA 第 7 版 Results | 读 `notes.md` § 关键回顾 3 (IMRaD Results) + `practice.md` drill D3 三阶段 worked-faded + `tutorial.ipynb` 苏格拉底追问"p=.049 vs p=.051 凭什么二分" | `solution.ipynb` TODO4 (统计报告) + `practice.md` D3 Stage 3 (写完整 Results 段 800-1000 字 + 表 1 + 表 2) | D3 Stage 3 Results 段含 3 项统计检验 + APA 表 1/2; t 检验 APA 完整 (t, df, p, d, 95%CI); deepeval 统计依据维度 ≥8/10 |
| **ILO4**: 能撰写含 DSR artifact 描述的 IMRaD 论文草稿 (3000-5000 字) + 学术发表路线图 | 读 `notes.md` § 关键回顾 3 + 4 (IMRaD + 发表路线图) + `practice.md` drill D4 三阶段 + `tutorial.ipynb` 苏格拉底追问"为什么 ICIS 比 MIS Quarterly 先投" | `solution.ipynb` TODO5 + TODO7 (IMRaD 草稿 + arXiv 路线图 + 天道推演章节) + `practice.md` D4 Stage 3 (完整 IMRaD + 20-30 篇 APA 参考文献) | D4 Stage 3 论文通过 deepeval 五维评估均 ≥7/10; arXiv 预印本上传计划一页可执行; 字数 3000-5000 范围 |

---

## 二、3 自检问题 (Biggs 三层反馈: Feed Up / Feed Back / Feed Forward)

### Feed Up (向上对齐: TLA 是否训练 ILO?)
> 自检问题 1: **本单元的 TLA 是否真正训练了 ILO 所声明的能力?**

- ILO1 要求"用 DSR 六步框架整合 Phase 1-5" -- TLA 中的 `practice.md` D1 是否让学生动手把 Step 1-6 映射到 IMRaD? **是**, D1 Stage 2 部分填空 + Stage 3 独立解都强制学生完成映射
- ILO3 要求"用 statsmodels+scipy 跑统计检验" -- TLA 是否提供 NSW RCT 真实数据? **是**, `solution.ipynb` TODO4 用 causaldata 加载 NSW (N=445), 不用 sim 数据
- 若发现 TLA 仅"读 notes.md"而 ILO 要求"能用", 视为对齐失败 -- 本单元通过 drill 三阶段保证 TLA 是"做"而非"读"

### Feed Back (向后对齐: AT 是否测量 ILO?)
> 自检问题 2: **本单元的 AT 是否真正测量了 ILO 所声明的能力?**

- ILO2 要求"构建可复现 trace 存档" -- AT (`solution.ipynb` TODO2) 是否检查 trace 含 4 类元数据? **是**, deepeval 可复现性维度会扣分
- ILO4 要求"撰写 3000-5000 字 IMRaD" -- AT 是否检查字数? **是**, D4 Stage 3 success_criteria 明文要求字数范围
- 若 AT 仅考"选择题"而 ILO 要求"能撰写", 视为对齐失败 -- 本单元所有 AT 都是产出性任务 (论文/代码/评分 JSON)

### Feed Forward (向前对齐: 不经 TLA 能过 AT 吗?)
> 自检问题 3: **如果学生完全跳过 TLA, 直接做 AT, 能过吗? 若能 = 对齐失败.**

- 跳过 D1 Stage 1-2 直接做 Stage 3 (写 Discussion 含天道推演)? **不能过** -- 学生不知道天道推演五项能力与多Agent仿真的同构表 (仅在 notes.md § 2026前沿 出现一次, 不做 worked example 难以迁移)
- 跳过 D2 Stage 1-2 直接写 5 个 deepeval BaseMetric? **不能过** -- 学生不知道 GEval 的 criteria 字段必须含 IMRaD 五节名 (worked example 才能教会)
- 跳过 D3 Stage 1-2 直接写 APA Results? **不能过** -- APA 第 7 版格式 (t(df)=X.XX, p=.XXX, d=X.XX, 95%CI) 需要 worked example 模板
- **结论**: 本单元所有 AT 都需要前置 TLA 训练, 对齐成立

---

## 三、Mastery 闭环 (Bloom + 标准)

- **Mastery 阈值**: 每个 AT 必须 ≥80% (即 deepeval 五维均 ≥7/10, D1/D2/D3 Stage 3 success_criteria 全达成)
- **未达标的处理**: 触发 `practice.md` § 七 Weak Loop, 回退上一阶段 + 补充 worked example + 1:1 答疑
- **Mastery 不等于完美**: 允许 1 个维度 7/10 (其他 ≥8/10), 但不允许任何维度 <6/10 (基础不达标)

---

## 四、对齐图 (可视化)

```
ILO1 (DSR整合)  ──TLA──>  practice.md D1 (worked-faded三阶段)
                ──AT───>  solution.ipynb TODO1 + D1 Stage3
                ──mastery─> ≥8/10 deepeval DSR维度

ILO2 (可复现+LLM评) ──TLA──> practice.md D2 + tutorial苏格拉底
                    ──AT───> solution.ipynb TODO2+TODO6 + D2 Stage3
                    ──mastery─> ≥7/10 可复现性维度 + 4节点trace

ILO3 (统计APA) ──TLA──> practice.md D3 (NSW真实数据)
                ──AT───> solution.ipynb TODO4 + D3 Stage3
                ──mastery─> ≥8/10 统计依据维度 + APA完整

ILO4 (IMRaD+发表) ──TLA──> practice.md D4 + notes.md §关键回顾3+4
                  ──AT───> solution.ipynb TODO5+TODO7 + D4 Stage3
                  ──mastery─> 五维均≥7/10 + 字数3000-5000
```
