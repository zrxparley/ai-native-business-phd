# R5 学术写作 IMRaD · 建构对齐 (Biggs ILO ↔ TLA ↔ AT)

> 基于 Biggs 建构对齐 (Constructive Alignment) + Bloom mastery learning。所有教学学习活动 (TLA) 与评估任务 (AT) 都引用本单元真实数据集/库 (arxiv / statsmodels / scipy.stats / causaldata NSW / LLM-as-a-judge / DeepSeek / OSF / 天道推演)，不是通用模板。

## ILO ↔ TLA ↔ AT 对齐矩阵 (>=3 行)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO-1**: 能用 arxiv 下载多篇真实论文 (ReAct/LLM-as-a-judge/GraphRAG)，对摘要做句级 IMRaD 分类，跨论文对比结构差异 | practice.md drill A1/A2/A3 (worked_faded 三阶段) + starter.ipynb TODO1 + tutorial.ipynb cell3 Socratic 追问漏斗结构 | starter.ipynb TODO1 自动判分 + tutorial.ipynb 后测 (给新摘要独立分类) | >=80% 句级分类正确, 且节占比误差 <10% |
| **ILO-2**: 能阐述 Introduction 漏斗结构 + Discussion 六要素, 并用天道推演因果链设计论证路径 | practice.md drill A2 (天道推演 3 路径沙盘) + notes.md 关键回顾 2/5 + tutorial.ipynb cell3 Socratic 追问"凭什么选这条路径" | progressive_project proposal (Day 3, 1 页论证路径草图) + final (Day 14, Discussion 六要素完整) | >=80%: 漏斗五段齐全 + 六要素全 + 论证路径>=3 条含 3 层推演 |
| **ILO-3**: 能用 statsmodels + scipy.stats 对 causaldata NSW (N=445) 跑 t 检验/Cohen's d/95% CI, 按 APA 第7版撰写 Results | practice.md drill B1/B3 (worked_faded 三阶段, NSW re78 真实数据) + starter.ipynb TODO4 + tutorial.ipynb cell3 Socratic 追问"p=.005 怎么写" | starter.ipynb TODO4 自动判分 + progressive_project milestone (Day 7, APA 报告句 + CI) | >=80%: APA 模板 4 要素齐全 (t/p/d/CI) + 效应量解读正确 + p 精确报告 |
| **ILO-4**: 能撰写符合规范的 Title (信息密度/关键词布局) + 结构化 Abstract (IMRaD 微缩, 200 词内) | practice.md drill A1 阶段2 (摘要填空) + starter.ipynb TODO2 + tutorial.ipynb cell3 Socratic 追问"标题广告性 vs 学术性" | starter.ipynb TODO2 + progressive_project final (Day 14, 200 词 Abstract) | >=80%: Abstract<=200 词 + 四部分 IMRaD 微缩齐全 + 关键词>=3 |
| **ILO-5**: 能用 LLM-as-a-judge 范式构建同行评审模拟器 (checklist 驱动), 理解偏差与局限 | practice.md drill C1/C2/C3 (worked_faded 三阶段, 引 Zheng et al. 2023 三类偏差) + starter.ipynb TODO6 + tutorial.ipynb cell5 Hattie 反馈 | starter.ipynb TODO6 + progressive_project poster (Day 17, judge 自评分表) | >=80%: checklist 4 维度齐全 + 偏差识别>=2 类 + 理由>=200 字/维度 |
| **ILO-6**: 能阐述 Preregistration + OSF 在可复现研究中的作用, 对抗 p-hacking/HARKing | schedule.json card C8 (间隔重复) + notes.md v6.0 追加节 + tutorial.ipynb cell6 exit artifact 推荐复习单元 | tutorial.ipynb cell3 后测 (口述 preregistration 价值) + alignment.md 自检 | >=80%: 能口述 p-hacking/HARKing 定义 + OSF 三步流程 |

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 1. Feed Up (TLA 是否训练 ILO？)
- **问**：practice.md 的 drill A1 (arxiv 句级分类) 是否真的训练了 ILO-1 (跨论文结构对比)？
- **答**：是。drill A1 用真实 arxiv 包下载 3 篇论文 (ReAct/LLM-as-a-judge/GraphRAG) 做句级 I/M/R/D 分类，worked_faded 三阶段从完整示范到独立解, 直接对应 ILO-1 的"跨论文对比"。

### 2. Feed Back (AT 是否测量 ILO？)
- **问**：starter.ipynb TODO4 (NSW t 检验) 是否真的测量了 ILO-3 (APA 第7版统计报告)？
- **答**：是。TODO4 要求对真实 NSW 数据 (N=445) 跑 statsmodels ttest_ind + scipy CI, 输出必须含 t/p/d/CI 四要素 + 效应量解读, 直接对应 ILO-3 的 APA 模板。判分自动检查 4 要素齐全度。

### 3. Feed Forward (不经 TLA 能过 AT 吗？若能 = 对齐失败)
- **问**：学生如果不做 practice.md drill C1 (LLM-as-a-judge checklist), 能直接过 progressive_project poster (judge 自评分表) 吗？
- **答**：不能。poster 要求 judge 自评分表含 4 维度 checklist + 偏差识别, 这些概念只在 drill C1 阶段1 完整示范 (Zheng et al. 2023 三类偏差) 中讲授。跳过 C1 的学生无法识别"自我偏好偏差", poster 必失分。**对齐成立**。
- **反例自检**：若学生仅读 notes.md 也能过 AT, 则 TLA 冗余, 对齐失败。本单元 AT (TODO + project) 都要求真实数据操作 (arxiv 下载/statsmodels 计算), notes.md 无此实操, 学生无法绕过 TLA。**对齐成立**。

## mastery 阈值汇总

| ILO | mastery_threshold | 不达标触发 |
|---|---|---|
| ILO-1 | >=80% 句级分类正确 | weak_loop: 回退 A1 worked example |
| ILO-2 | >=80% 漏斗+六要素+3 路径 | weak_loop: 回退 A2 阶段1 |
| ILO-3 | >=80% APA 4 要素 + 效应量解读 | weak_loop: 回退 B1 阶段1 |
| ILO-4 | >=80% Abstract<=200 词 + 四部分 | weak_loop: 回退 A1 阶段2 |
| ILO-5 | >=80% checklist + 偏差识别 + 理由 | weak_loop: 回退 C1 阶段1 |
| ILO-6 | >=80% p-hacking/HARKing/OSF | weak_loop: 重读 schedule.json C8 |

> 所有 ILO 共享 retry_policy: 10 free late days + 失败重试不罚分 (取最高分)。
