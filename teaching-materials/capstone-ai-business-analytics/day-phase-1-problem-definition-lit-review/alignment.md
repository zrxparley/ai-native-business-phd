# 建构对齐 · Capstone Phase 1：问题定义与文献综述

> 基于 Biggs constructive alignment (Biggs 1996) + mastery learning (Bloom 1968)。ILO (Intended Learning Outcome) ↔ TLA (Teaching-Learning Activity) ↔ AT (Assessment Task) 三者对齐，mastery 阈值确保掌握。

## ILO ↔ TLA ↔ AT 对齐矩阵

| ILO（预期学习产出） | TLA（教学学习活动） | AT（评估任务） | mastery_threshold |
|------------------|-------------------|--------------|------------------|
| ILO-1: 能用 DSR 六步框架的 Step 1-2 + pydantic 把模糊研究想法转化为可验证 artifact 定义（4 字段 Schema + 类型约束 + model_validate 通过） | starter.ipynb TODO1 + practice.md drill-1 (worked->faded->independent) + tutorial.ipynb Socratic 追问"为什么这个字段需要 min_length 约束" | AT-1: 提交研究问题定义书（pydantic Schema 实例化 Capstone 主题 "AI 营销 Agent 系统因果评估"，model_validate 通过，4 字段非空） | >=80% 字段类型约束生效 + model_validate 通过 |
| ILO-2: 能用 arxiv 包查询真实 arXiv API + pandas 执行 PRISMA 四步（识别/去重/筛选/纳入）+ matplotlib 画带真实数字的 PRISMA 流程图 | starter.ipynb TODO2-4 + practice.md drill-2 (worked->faded->independent) + tutorial.ipynb Socratic 追问"PRISMA 哪步排除比例最高？为什么？" | AT-2: 提交 PRISMA 文献综述 draft（>=15 篇真实 arXiv 论文 + 4 框流程图带真实数字 + DataFrame 统计表 + 去重前后数记录） | PRISMA 四步数字链单调递减 + 流程图数字 == DataFrame len() + >=15 真实论文 |
| ILO-3: 能用 pandas 文献计量统计识别 2-3 个研究空白 + 用天道推演沙盘展开 3 条研究路径 × 3 层 + 用贝叶斯更新选最优路径 | starter.ipynb TODO5-6 + practice.md drill-3 (worked->faded->independent) + tutorial.ipynb Socratic 追问"你的 gap 是数字支撑还是定性陈述？天道推演不是占卜，凭什么选这条路径？" | AT-3: 提交 gap analysis + 天道推演沙盘报告（pandas groupby 统计表 + 2-3 个 gap 数字证据 + 3 路径 × 3 层沙盘 + 贝叶斯先验/似然比/后验数字） | >=2 个 gap 有数字支撑 + 3 路径沙盘完整 + 贝叶斯后验有数字计算 |

## 3 自检问题（Feed Up / Feed Back / Feed Forward）

### 1. Feed Up: TLA 是否训练 ILO？
- TLA 是否覆盖 ILO 的全部能力点？
  - starter.ipynb TODO1 + drill-1 (worked/faded/independent) 是否训练了 pydantic Schema 4 字段类型约束？ **是** -- Worked 阶段完整演示，Faded 阶段填空 Field 约束，Independent 阶段从零写。
  - starter.ipynb TODO2-4 + drill-2 是否训练了 arxiv 查询 + pandas 去重/筛选 + matplotlib 流程图？ **是** -- Worked 演示完整 PRISMA 四步，Faded 填 drop_duplicates + 筛选条件 + 流程图绘制，Independent 换 query 独立完成。
  - starter.ipynb TODO5-6 + drill-3 是否训练了 pandas groupby gap 识别 + 天道推演沙盘 + 贝叶斯更新？ **是** -- Worked 演示数字支撑的 gap + 3 路径沙盘 + 贝叶斯后验，Faded 填数字证据 + 似然比 + 后验，Independent 换数据子集独立完成。

### 2. Feed Back: AT 是否测量 ILO？
- AT-1 model_validate 通过 + 4 字段非空 = 直接测量 ILO-1 的 "可验证 artifact 定义"。 **对齐**。
- AT-2 PRISMA 四步数字链单调递减 + 流程图数字 == DataFrame len() + >=15 真实论文 = 直接测量 ILO-2 的 "arxiv+pandas+matplotlib PRISMA"。 **对齐**。
- AT-3 >=2 gap 有数字支撑 + 3 路径沙盘 + 贝叶斯后验数字 = 直接测量 ILO-3 的 "gap 识别 + 天道推演路径选择"。 **对齐**。

### 3. Feed Forward: 不经 TLA 能过 AT 吗？若能 = 对齐失败。
- 不做 drill-1 Worked/Faded，能直接写 pydantic Schema 过 AT-1？ **不能** -- 学生不熟悉 Field(min_length=10) 约束语法，会写裸字段导致 model_validate 失败。
- 不做 drill-2 Worked/Faded，能直接 arxiv.Search + pandas PRISMA 四步过 AT-2？ **不能** -- 学生不熟悉 arxiv.Search query 语法 + drop_duplicates subset 参数 + matplotlib flow chart 绘制，会卡在第一步。
- 不做 drill-3 Worked/Faded，能直接 gap + 天道推演 + 贝叶斯过 AT-3？ **不能** -- 学生不熟悉 pandas groupby 数字统计 + 天道推演沙盘 3 层结构 + 贝叶斯似然比计算，会给出定性陈述而非数字支撑。
- **结论：3 条 ILO 均对齐，不经 TLA 不能过 AT**。

## mastery 机制

- 每个 drill 的 feedback_rule 是 mastery 的客观标准（如 D2 "PRISMA 四步数字链单调递减 + 流程图数字 == DataFrame len()"）。
- 未达 mastery 的 drill 触发 weak_loop（连续 2 次失败 -> 回退上一 drill + 补 Worked example）。
- Final 交付物未达 >=80% 可重交 1 次（retry_policy）。
- tutorial.ipynb 的 student_model.json 记录每个 ILO 的掌握度（0-1）+ blind_spots 列表，供 tutor 动态调整 TLA。

---

*本 alignment.md 基于 Biggs constructive alignment (Biggs 1996, Higher Education) + Bloom mastery learning。ILO/TLA/AT 三者对齐且引用本单元真实库（arxiv/pydantic/pandas/matplotlib）与真实评估（PRISMA 流程图 + gap analysis + 天道推演沙盘）。*
