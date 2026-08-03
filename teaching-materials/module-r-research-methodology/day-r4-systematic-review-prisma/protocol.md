# R4 PRISMA 2020 系统综述 Protocol（CQ-R4-1）

> 状态：教学模板。正式研究必须在运行筛选、质量评估和综合前冻结本文件；任何修改都记录为 protocol amendment。

## 1. 研究问题

- RQ：在 "AI marketing" 主题的 arXiv 系统综述中，ASReview 风格主动学习能否在保持双人独立筛选一致性 κ≥0.61 的前提下，将 title/abstract 阅读量降低至少 40%，并保持 ≥90% recall？
- 主指标：达到 90% recall 所需阅读论文数。
- 次指标：Cohen's kappa、PRISMA 各阶段计数、RoB proxy 分布、证据确定性等级。

## 2. 信息源与检索式

- 数据库：arXiv API；离线复现使用 `data/arxiv_fallback.json`。
- 检索式：以 `data/README.md` 的 6 条 query 为冻结口径。
- 检索日志必须记录：query、date、max_results、returned_count、API/fallback、工具版本。

## 3. 纳入与排除标准

- 纳入：2022 年及以后；标题/摘要同时覆盖 AI 与营销/广告/消费者/推荐/商业语境；有足够摘要支持方法或应用分类。
- 排除：非 AI 主题、非营销/商业语境、无摘要、重复记录、无法判断研究对象或方法的记录。
- Full-text 复筛：正式研究需要记录全文不可得、主题不符、方法不足、重复发表等排除理由。

## 4. 双人独立筛选

- 两名筛选者独立完成 title/abstract 筛选，先不互看结果。
- 冲突由第三人或共识会议裁决，保存裁决理由。
- 报告 Cohen's kappa 点估计与置信区间。
- 当前 `solution.ipynb` 的第二筛选者为随机翻转模拟，仅用于教学；发表级结果不得把该模拟写成真实双人独立筛选。

## 5. 偏倚与证据确定性

- 研究内偏倚：记录研究设计、数据来源、测量偏差、选择偏差、混杂控制、局限讨论。
- 报告偏倚：披露 arXiv 单库偏差、开放摘要偏差、英文/CS 学科偏差、未发表结果不可见风险。
- RoB：Kitchenham 五维分数可作为 RoB proxy；正式表格必须附逐项理由。
- 证据确定性：按 High / Moderate / Low / Very low 标注，并说明因研究内偏倚、不一致性、间接性、不精确性、报告偏倚导致的降级。

## 6. 自动化工具披露

- 检索：arxiv Python 包和 arXiv API。
- 处理：pandas 去重与计数。
- 一致性与主动学习：scikit-learn Cohen's kappa、TF-IDF、LogisticRegression；ASReview 仅为 proxy 模拟，除非实际运行 ASReview LAB。
- LLM/RAGAS：若用于摘要抽取或综合，必须披露模型、温度、提示词版本、人工复核比例、失败回退规则。
- 最终论文须显式映射 PRISMA 2020 Item 8（选择过程与自动化）、Item 11（研究内偏倚评估）、Item 13-15（综合、报告偏倚、证据确定性）与 Item 24（注册和协议）。

## 7. 数字冻结与 protocol amendment

- 冻结离线复现实验口径：`data/arxiv_fallback.json` 顶层元数据记录 210→135→40→23。
- `data/README.md` 的 44/26 是历史在线记录；最终报告必须明确选择 online 或 fallback 模式，并由同一 run manifest 生成所有计数。
- protocol amendment 字段：date、author、changed_field、old_value、new_value、reason、affected_outputs。
