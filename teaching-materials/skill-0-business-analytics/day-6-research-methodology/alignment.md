# Constructive Alignment - Day 6 研究方法论入门 (v6.0)

> Biggs 建构对齐 (Constructive Alignment): ILO (Intended Learning Outcome) ↔ TLA (Teaching/Learning Activity) ↔ AT (Assessment Task) 三者必须对齐, 否则"不经 TLA 也能过 AT" = 对齐失败.

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 arxiv 包查询真实 arXiv API 并处理 HTTPError 限流 fallback | starter.ipynb drill D1 + tutorial.ipynb Socratic 第 1-2 轮 + worked_faded 阶段 1-2 | solution.ipynb TODO1 + tutorial 后测 + diagnostic D0.1 | >=80% TODO1 通过 + 能口头解释 fallback 必要性 |
| ILO2: 能用 pandas 完成文献计量统计 (年份/作者/主题) | drill D2 阶段 1-2 + schedule.json C2 复习 + interleaving A1/B2 交叉 | starter.ipynb TODO2-3 + 项目 P2 交付 (论文增长趋势 + Top-10 作者) | >=70% TODO2-3 通过 + 300 字分析准确 |
| ILO3: 能用 networkx 构建 200 节点 3303 边合作网络与关键词共现网络, 计算度中心性与社区检测 | drill D2 阶段 3 (独立解) + worked_faded 阶段 3 + interleaving B1/B2/B3 | starter.ipynb TODO4-5 + 项目 P3 交付 (核心团队 + 新兴方向) | 能独立解 TODO4-5 + 识别 Top-5 核心作者 + 1 个新兴方向 |
| ILO4: 能解释可复现研究三大支柱与 FAIR 原则并在自己的研究中实践 OSF 预注册 | drill D3 + schedule.json C4/C5 间隔重复 + tutorial Socratic 第 3-4 轮 + worked_faded 阶段 1-3 | 项目 P5 (OSF 预注册包 + FAIR 自检表 + requirements.txt) + diagnostic D0.3 | OSF 模板三件套完整 + FAIR 四字母全对 + ASReview 范式正确 |

## mastery_threshold 说明

- **单元总体 mastery**: 4/4 ILO 全部达标 (任一 ILO 未达 threshold = 单元未掌握)
- **drill mastery**: 单 drill 连续 2 次无 hint 通过阶段 3 (独立解) = 掌握; 连续 2 次失败触发 weak_loop
- **项目 mastery**: P1-P6 全部交付 + P5 (OSF/FAIR 可复现包) 通过同行评阅
- **间隔重复 mastery**: schedule.json 5 张卡片在 60 天间隔内 EF >= 2.5 (FSRS-6 request_retention=0.9)
- **tutorial mastery**: student_model.json 中所有 topic mastery >= 0.7 + blind_spots 清空

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

> 这三个自检问题来自 Biggs 建构对齐理论, 用于检验本单元的教学设计是否真正对齐.

### 自检 1: Feed Up (TLA 是否训练 ILO?)

每个 ILO 是否都有对应的 drill + tutorial Socratic 轮次 + worked_faded 阶段训练?

- ILO1 -> D1 + Socratic T1-T2 + worked_faded 阶段 1-2 ✓
- ILO2 -> D2 阶段 1-2 + C2 复习 + interleaving ✓
- ILO3 -> D2 阶段 3 + worked_faded 阶段 3 + interleaving B1/B2/B3 ✓
- ILO4 -> D3 + C4/C5 + Socratic T3-T4 + worked_faded 阶段 1-3 ✓

若 ILO4 没有对应 worked_faded 阶段 3, 则对齐失败. 当前: 通过.

### 自检 2: Feed Back (AT 是否测量 ILO?)

starter.ipynb 的 TODO 是否精确对应每个 ILO? 项目 P1-P6 是否覆盖所有 ILO?

- TODO1 (arxiv 查询) -> ILO1 ✓
- TODO2-3 (pandas 统计) -> ILO2 ✓
- TODO4-5 (networkx 网络) -> ILO3 ✓
- 项目 P5 (OSF/FAIR 包) -> ILO4 ✓

若 ILO3 (合作网络) 无对应 TODO, 则 AT 测量失败. 当前: 通过.

### 自检 3: Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)

- 若学生不练 drill D2 也能通过 TODO4-5, 说明 TLA 设计有冗余 -> 应增加 worked_faded 阶段 3 的独立性 (禁看 solution.ipynb)
- 若不读 schedule.json 也能过 AT, 说明间隔重复未真正嵌入评估 -> 应把 C4/C5 的复习记录纳入项目 P5 评分
- 若不进 tutorial.ipynb 也能过 ILO4, 说明 Socratic 追问未实质训练 OSF/FAIR 辩护 -> 应把 tutorial exit artifact 写入 student_model.json 作为 ILO4 的前置

当前: 通过 (所有 AT 都依赖对应 TLA).
