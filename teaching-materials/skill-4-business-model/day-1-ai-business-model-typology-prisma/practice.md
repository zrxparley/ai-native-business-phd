# 刻意练习 (v6.0) - AI商业模式类型学 + PRISMA

> Ericsson 刻意练习 5 要素 + MIT 6.5940 提取/间隔/交叉练习 + Worked-Faded 渐达示例
> 参考: Ericsson (1993), MIT Open Learning 明文原则, Butler (2010) 检索练习证据

## skill_target

能在 90 分钟内独立完成一个 PRISMA 系统文献综述: 用 `arxiv` 包查 arXiv API, pandas 去重/筛选, 把纳入文献归类到 AI 商业模式五大类型, 并用 matplotlib 画出 PRISMA 流程图 (真实数字 160->96->30->30)。

## diagnostic (pset0 式先测, 3 道)

> 开课前必须完成。CS229 pset0 风格 -- 测先备知识, 不计入成绩, 决定起点。

- **D0.1**: 写出 AI 商业模式五大类型名称, 各举一个真实企业 (不能看 notes.md)。
- **D0.2**: PRISMA 四步 (识别 / 筛选 / 质量评估 / 综合) 各自的输入和输出是什么?
- **D0.3**: `arxiv.Search(query=...)` 返回对象的哪个字段含标题/摘要/DOI? `pandas` 去重用哪个方法? `matplotlib` 画流程图用哪个函数?

> 评分规则: 3 道全对 -> 跳到 D3 Independent; 2 道对 -> 从 D2 Faded 开始; <=1 道对 -> 从 D1 Worked 开始。

## subskills

- **S1 (A) AI 商业模式类型识别**: 给定论文摘要/企业描述, 归类到五大类型之一 (基础设施 / 增强产品 / 原生产品 / 平台 / Agent经济)
- **S2 (B) PRISMA 流程执行**: arxiv 查询 -> pandas 去重 -> 年份+相关性筛选 -> 类型学分类函数 -> matplotlib 流程图
- **S3 (C) ASReview 主动学习加速**: 模拟种子集标注 + 主动学习排序 + 与人工筛选对比 + DeepSeek/RAGAS 证据合成

## drills

drill_id: D1
- difficulty: 2
- reps_required: 3
- feedback_rule: 若归类错误, 指向 `notes.md` 关键回顾 1 表格的"核心驱动力"列, 让学生用驱动力重新判断 (商业模式类型学); 若两次仍错, 触发 weak_loop 回退到类型对照表 worked example; 若学生混淆"AI增强产品"和"AI原生产品", 追问"剥离AI后产品是否成立"。
- worked_faded:
  - **阶段1 Worked (完整示范)**: 给出 "OpenAI GPT API 按 token 计费" -> 对照表格 -> 核心驱动力=算力+模型, 收入=按用量计费 -> 归类"AI基础设施"。完整展示判断链条。
  - **阶段2 Faded (部分填空)**: 给出 "Salesforce Einstein" + 表格框架 (类型/驱动力/收入/护城河), 学生填"核心驱动力"和"类型"两列。
  - **阶段3 Independent (独立解)**: 给 5 篇 arxiv 摘要 (Perplexity / Hugging Face / Sierra / Cursor / Midjourney), 学生独立归类到五大类型, 给出驱动力依据。

drill_id: D2
- difficulty: 3
- reps_required: 3
- feedback_rule: 若去重数量错, 提示 `df.drop_duplicates(subset='title')` 用 title 字段 (arxiv 包返回字段); 若筛选数量与 `notes.md` 真实数字 (160->96->30) 偏差 >5%, 让学生对照 PRISMA 流程图找漏步 (PRISMA 四步); 若 query 太宽泛返回 10000+, 收窄到 'AI business model' (arxiv.Search 用法); 若两次仍错, 触发 weak_loop。
- worked_faded:
  - **阶段1 Worked (完整示范)**: 完整代码示范 `arxiv.Search(query="AI business model", max_results=50)` + `pd.DataFrame(results)` + `df.drop_duplicates(subset='title')` + `df[df.year >= 2023]` + 输出每步数字 (160->96->30)。
  - **阶段2 Faded (部分填空)**: 给出 arxiv 查询和 DataFrame 框架, 学生填 `drop_duplicates` 的 subset 参数 + 年份筛选条件 + 相关性筛选关键词。
  - **阶段3 Independent (独立解)**: 学生独立从 0 写 PRISMA 四步 (识别->去重->筛选->纳入), 输出 160/96/30/30 真实数字, 用 matplotlib 画流程图。

drill_id: D3
- difficulty: 4
- reps_required: 3
- feedback_rule: 若 ASReview 排序与人工筛选差异 >20%, 指向 `notes.md` 2026 前沿 ASReview 小节, 让学生解释主动学习加速原理 (种子集->分类器->排序) (ASReview); 若学生混淆 ASReview 与 DeepSeek/RAGAS, 明确区分: ASReview=筛选加速 (主动学习), RAGAS=合成质量评估 (检索增强生成评估), DeepSeek=LLM辅助摘要提取; 若种子集偏置导致召回率低, 追问"种子集如何选才能减少偏置"。
- worked_faded:
  - **阶段1 Worked (完整示范)**: 完整示范 -- 用 5 篇种子集 (3 相关 / 2 不相关) 训练 `sklearn.LogisticRegression`, 对剩余 25 篇 predict_proba 排序, 输出 top-10 召回率 vs 人工全读召回率。
  - **阶段2 Faded (部分填空)**: 给出种子集和分类器框架, 学生填 `fit(X_train, y_train)` 和 `predict_proba(X_remaining)[:, 1]` 排序调用。
  - **阶段3 Independent (独立解)**: 学生独立实现 ASReview 模拟, 对比 top-20% 覆盖率与人工全读覆盖率, 输出节省时间百分比; 并用天道推演预判 ASReview 在 3 年后的演化 (主动学习 vs LLM 直评)。

## interleaving (明文排布, 不块状)

不要按 D1 -> D2 -> D3 块状刷题。按以下交叉序列执行 (A=类型识别, B=PRISMA流程, C=ASReview):

```
第1轮 (Worked 阶段):   A1 (D1-Worked) -> B1 (D2-Worked) -> C1 (D3-Worked)
第2轮 (Faded 阶段):    B2 (D2-Faded) -> C2 (D3-Faded) -> A2 (D1-Faded)
第3轮 (Independent):   C3 (D3-Independent) -> A3 (D1-Independent) -> B3 (D2-Independent)
```

明文模式: **A1B1C1...B2C2A2...C3A3B3** (MIT 6.5940 交叉练习 interleaving 规范)。每轮间隔 1 天, 由 `schedule.json` 卡片调度。不块状 (block practice) -- 块状短期高分但长期保持差 (Butler 2010)。

## progressive_project (proposal -> milestone -> final -> poster)

- **proposal (Day1 课后)**: 提交 PRISMA 检索策略 (4 条 `arxiv.Search` query) + 五大类型假设分布 (prior: 预估每类型几篇, 标注置信区间)。
- **milestone (Day2 课前)**: 去重 + 筛选完成, 输出 160->96->30 真实数字 + 类型学分类函数 `classify_type(title, abstract) -> str`。
- **final (Day2 课末)**: 类型学分布统计 (`pandas.value_counts`) + PRISMA 流程图 (matplotlib, 真实数字) + 300 字分析 (哪个阶段排除比例最高, 为什么)。
- **poster (Day3 课前)**: 类型学分布海报 + 天道推演三沙盘分支 (Agent主导 / 平台整合 / 基础设施商品化) 的 3 层推演 (immediate -> near -> far) + 概率分布标注。

## retry_policy

- 每个 drill 每天最多 3 次 retry (CS229 pset0 风格, 鼓励间隔重复而非突击)
- 连续 2 次失败 -> 自动触发 weak_loop
- 累计 3 天未能进入 Independent 阶段 -> 主动预约 tutorial (见 `tutorial.ipynb`)
- late days: progressive_project 每阶段允许 2 天延期 (CS230 风格, 超期 20%/天 罚分)

## weak_loop

连续 2 次失败触发弱项循环:

1. **回退**: 回到上一 drill 的 Worked 阶段重看一遍 (例如 D2 失败 -> 重看 D1 Worked)
2. **补充 worked example**: 读 `notes.md` 关键回顾表格 + `reading.md` 对应条目 (arxiv包/PRISMA/ASReview)
3. **间隔复习**: `schedule.json` 中相关卡片的 ef0 调低至 2.0, 加密复习 (当天 + 次日 + 3 日后)
4. **重试**: 通过后回到原 drill 的 Faded 阶段重试 (不直接跳 Independent)

```
weak_loop 流程: 失败x2 -> 回退 worked -> 补充 example -> schedule.json 加密复习 -> 回到 faded 重试 -> 通过则进 independent
```
