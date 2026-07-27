# Practice - Day 6 研究方法论入门 (v6.0 刻意练习)

> 基于 Ericsson 刻意练习 5 要素 + MIT OpenLearning 渐退示例 (Worked-Faded) + 交叉练习 (interleaving A1B1C1).

## skill_target

用真实 Python 库 (arxiv + pandas + networkx + matplotlib) 完成营销 AI 领域的微型文献计量, 并按 OSF / FAIR 标准交付可复现研究包.

## subskills

- **S1**: arxiv API 查询与异常 fallback (论文元数据获取, arxiv.Search + Client().results())
- **S2**: pandas 文献计量 (按年份/作者/主题统计) + networkx 合作网络 (200 节点 3303 边) 与关键词共现
- **S3**: 可复现研究封装 (OSF 预注册 / Registered Reports / FAIR / 环境锁定 / ASReview 主动学习)

## diagnostic (前测, 3 道, 检测起点)

- **D0.1**: `arxiv.Search` 与 `Client().results()` 的调用顺序是什么? 网络异常 (HTTPError 限流) 时如何 fallback?
- **D0.2**: 给定作者合作网络 (200 节点 3303 边), 用什么 networkx 函数计算度中心性? 如何识别 Top-5 核心作者? 边用 `itertools.combinations` 还是 `permutations`?
- **D0.3**: OSF 预注册如何对抗 p-hacking 与发表偏倚? FAIR 四字母分别指什么? ASReview 用什么机器学习范式加速文献综述?

## drills (>=3, 每含 difficulty / reps_required / feedback_rule / worked_faded)

### Drill D1

drill_id: D1
difficulty: 3
reps_required: 3
feedback_rule: 若 API 调用错误 -> 指向 arxiv.Search 构造与 try/except fallback; 若元数据字段缺失 -> 指向 result.entry_id / result.title / result.published / result.summary 命名; 若空结果 -> 检查 query 语法 (双引号 / 布尔 AND/OR); 若未处理限流 -> 补 HTTPError 重试
worked_faded: 阶段1 (完整示范: arxiv.Search(query="marketing analytics", max_results=50) + Client().results() + try/except HTTPError 重试) -> 阶段2 (填空: 补全 query / max_results / except 块) -> 阶段3 (独立: 自行查 "causal inference marketing" 并处理空结果与限流)

### Drill D2

drill_id: D2
difficulty: 4
reps_required: 3
feedback_rule: 若 DataFrame 构造错 -> 指向 pd.DataFrame 从 result 对象抽取字段; 若统计错 -> 指向 groupby('year').size() / value_counts(); 若合作网络边重复 -> 指向 itertools.combinations (非 permutations) 去重; 若度中心性排序错 -> 指向 sorted(nx.degree_centrality(G).items(), key=lambda x: x[1], reverse=True)[:5]; 若社区检测缺 -> 补 nx.community.louvain_communities
worked_faded: 阶段1 (完整示范: 论文元数据 -> DataFrame -> 年份趋势 + 200 节点 3303 边合作网络 + 度中心性 Top-5) -> 阶段2 (填空: 补全 groupby 与 combinations 部分) -> 阶段3 (独立: 自建 200 节点合作网络, 计算度中心性 + 社区检测 + 关键词共现)

### Drill D3

drill_id: D3
difficulty: 5
reps_required: 3
feedback_rule: 若 FAIR 缺一 -> 指向 Findable / Accessible / Interoperable / Reusable 四字母映射; 若 OSF 预注册步骤错 -> 指向 hypothesis + analysis_plan + data_collection_order 三件套; 若 Registered Reports 概念错 -> 指向 Stage 1 (方法审稿) / Stage 2 (结果发表承诺); 若环境锁定不全 -> 指向 requirements.txt + Dockerfile + random_state=42; 若 ASReview 范式错 -> 指向 Active Learning (主动学习, 非监督)
worked_faded: 阶段1 (完整示范: OSF 预注册模板 + FAIR 自检表 + requirements.txt + random_state 锁定) -> 阶段2 (填空: 补全 FAIR 四字母与预注册三件套) -> 阶段3 (独立: 给一篇 LLM marketing 论文写可复现研究包, 含 ASReview 筛选流程)

## interleaving (A1B1C1 交叉, 不块状刷题)

按 **A1 B1 C1 ... B2 C2 A2 ... C3 A3 B3** 显式交叉: 同一 drill 不连续刷两遍, 每轮换 query / 网络规模 / 论文主题.

- A1 = D1 (arxiv 查询 "marketing analytics", 50 篇)
- B1 = D2 (200 节点合作网络, 度中心性)
- C1 = D3 (OSF 预注册三件套)
- B2 = D2 (3303 边规模, 关键词共现)
- C2 = D3 (FAIR 四字母自检表)
- A2 = D1 (arxiv 查询 "causal inference marketing", 限流处理)
- C3 = D3 (ASReview 主动学习 + Registered Reports)
- A3 = D1 (arxiv 查询 "LLM marketing", 空结果处理)
- B3 = D2 (社区检测 louvain_communities)

**反块状原则**: 不允许连续两次同一 drill (A1 A2 ... 是禁止的). 每轮结束后 24h 间隔 (配合 schedule.json 间隔重复).

## progressive_project (跨 6 步骤渐进式脚手架, 参考 MIT 6.5940 / CS230)

- **P1 (proposal)**: 选定营销 AI 主题 (如 "LLM marketing"), 写 1 页研究问题 + 假设 + 预注册草稿
- **P2 (milestone)**: arxiv 查询 + pandas 统计, 交付论文增长趋势折线图 + 高产作者 Top-10
- **P3 (milestone)**: networkx 合作网络 (200 节点) + 关键词共现, 识别核心团队与新兴方向
- **P4 (milestone)**: matplotlib 可视化 (折线图 + 网络图, 双图)
- **P5 (final)**: OSF 预注册模板 + FAIR 自检表 + requirements.txt + random_state=42, 封可复现包
- **P6 (poster)**: 2 分钟话术 + 1 张图回答 "该领域 2026 年研究热度与新兴方向", 附依据

每阶段不通过可在 7 天内修订 1 次 (retry_policy). P5 是 mastery 关卡——必须通过同行评阅.

## retry_policy

- 沿用 CS230 风格: 10 late days / 20% 罚分每天
- drill 失败 24h 后可重试 (配合 schedule.json 间隔重复, 避免短期刷题)
- 连续 2 次失败触发 weak_loop
- 项目 P1-P6 任一阶段不通过可在 7 天内修订 1 次; P5 (可复现包) 修订后需重新同行评阅

## weak_loop (连续 2 次同 drill 失败触发弱项循环)

连续 2 次同 drill 失败 -> 触发弱项循环:

1. **回退**: 回退到上一 drill (如 D3 失败回退 D2 worked example 阶段 1)
2. **重看 worked example**: 只看 practice.md 的 worked_faded 阶段 1 (不看 solution.ipynb)
3. **降级**: 降一级 difficulty (D3 difficulty 5 -> 4, 用更小网络规模或更简单 query)
4. **自检**: 再次回答 diagnostic 对应题 (D0.x)
5. **重试**: 通过后方可重试原 drill; 若再失败则进入 1 对 1 tutorial (tutorial.ipynb)

weak_loop 出口: 连续 2 次通过原 drill 的阶段 3 (独立解) 方算掌握.
