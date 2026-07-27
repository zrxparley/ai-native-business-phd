---
unit: R5
title: 学术论文写作 IMRaD · 刻意练习 (Deliberate Practice)
version: v6.0
skill_target: 能用 arxiv/statsmodels/scipy/causaldata 拆解真实论文 IMRaD 结构、对 NSW 数据按 APA 第7版撰写统计报告、并用 LLM-as-a-judge checklist 模拟同行评审 (可观察可评估)
---

# R5 学术写作 IMRaD · 刻意练习

> 基于 Ericsson 刻意练习 + MIT CS229 pset0 先测 + Harvard/Stanford 工程教育。所有 drill 引用本单元真实数据集/库 (arxiv / statsmodels / scipy.stats / causaldata NSW / LLM-as-a-judge / DeepSeek)，不是通用模板。

## diagnostic (先测, CS229 pset0 式, 3 道, 探测先验缺口)

1. **D1 结构辨识**：给定 ReAct (Yao et al., 2022) 摘要第 1-3 句，请逐句标注 I/M/R/D（或 N/A），并说明凭什么这样标。**先验缺口**：学生常把"贡献声明"误标为 Results。
2. **D2 APA 报告**：写出 `t(443) = 2.84, p = .005, d = 0.27` 的 APA 第7版完整报告句（含效应量解读 + 95% CI 占位）。**先验缺口**：学生常漏效应量解读，或把 p = .005 写成 p < .01。
3. **D3 同行评审偏差**：LLM-as-a-judge 给 Introduction 打了 4/5 但理由只有"写得不错"。这是哪类偏差（位置/冗长/自我偏好）？为什么？请给出 1 条追问。**先验缺口**：学生不知道 LLM judge 的偏差谱系。

> 评分：每题 0/1/2 分，<4 分触发 subskill A 的 worked example 重学。

## subskills (3 个子技能, 拆自 skill_target)

- **A. IMRaD 结构元分析**：跨多篇真实论文 (arxiv 下载) 做句级 IMRaD 分类、节占比对比、漏斗结构识别
- **B. APA 第7版统计报告**：对 NSW 数据 (N=445) 跑 t/Cohen's d/CI，按 APA 模板撰写 Results 句子
- **C. 同行评审模拟**：构建 LLM-as-a-judge checklist 对 IMRaD 各部分打分，识别偏差与局限

## drills (>=3, 每个 difficulty 1-5 + reps_required + feedback_rule + worked_faded)

### drill_id: A1
- difficulty: 3
- reps_required: 4
- feedback_rule: 用 arxiv 下载 ReAct/LLM-as-a-judge/GraphRAG 三篇，对摘要做句级 I/M/R/D 分类。反馈规则：若某句标 R 但句中无数字/无显著性词 (significantly/improved/p<) → 标记"过度归类 Results"，提示回读原文 figure caption。引用 NSW/DeepSeek 无关，引用 arxiv lukasschwab/arxiv.py 1.5k★ 真实包。
- worked_faded:
  - 阶段1 完整示范: 给出 ReAct 摘要第 1 句的 I/M/R/D 标注 + 理由（"We propose..."→ I，含贡献动词）
  - 阶段2 部分填空: 给 GraphRAG 摘要前 3 句，标好 I，让学生填 M/R/D
  - 阶段3 独立解: 学生独立标 LLM-as-a-judge 摘要全 8 句的 IMRaD 分类

### drill_id: B1
- difficulty: 4
- reps_required: 5
- feedback_rule: 用 statsmodels.stats.weightstats.ttest_ind 对 causaldata NSW 的 re78 (treat=1 vs treat=0) 跑 t 检验，scipy.stats.t 可得 95% CI，按 APA 第7版输出 `t(df) = X.XX, p = .XXX, d = X.XX, 95% CI [LL, UL]`。反馈规则：若学生写 `p < .01` 而 p ≥ .001 → 标"精度丢失"，强制精确报告；若漏 Cohen's d 解读 (小/中/大) → 标"效应量解读缺失"。
- worked_faded:
  - 阶段1 完整示范: 给出 NSW treat vs control 的完整 APA 句 `An independent-samples t-test showed that the treatment group earned significantly higher 1978 earnings than controls, t(443) = 2.84, p = .005, d = 0.27 (small effect, Cohen, 1988), 95% CI [$482, $2614].`
  - 阶段2 部分填空: 给出 t/p/CI 数值，让学生拼 APA 模板 + 效应量解读
  - 阶段3 独立解: 学生对 age/educ/nodegree 三个变量独立撰写 APA 报告句

### drill_id: C1
- difficulty: 5
- reps_required: 3
- feedback_rule: 构建 LLM-as-a-judge checklist (Introduction 清晰度/Methods 可复现性/Results 统计严谨/Discussion 诚实度，各 1-5 分)，对自己写的 IMRaD 草稿打分。反馈规则：若 judge 理由 < 20 字 → 触发"冗长偏差"自检；若所有部分同分 → 触发"自我偏好偏差"自检；引用 Zheng et al. NeurIPS 2023 (arXiv 2306.05685) 三类偏差。
- worked_faded:
  - 阶段1 完整示范: 给出 Methods 部分 4/5 分的 judge 输出 + 200 字理由 (引用可复现性五要素)
  - 阶段2 部分填空: 给 Discussion 打分模板，让学生填"诚实度"维度的理由
  - 阶段3 独立解: 学生对自己 Introduction 全独立跑 judge + 自评偏差

### drill_id: A2 (天道推演论证路径)
- difficulty: 4
- reps_required: 3
- feedback_rule: 用天道推演 (因果链追踪 → 沙盘模拟 → 最优路径) 设计论文 Introduction 的论证路径。构建"假设→证据→结论"有向图，识别薄弱节点。反馈规则：若论证链 > 3 步无证据支撑 → 标"逻辑跳跃"；若多条路径并列未比较说服力/严谨性/新颖性 → 标"未做沙盘展开"。
- worked_faded:
  - 阶段1 完整示范: 给"AI营销Agent效果评估"研究的 3 条论证路径 (先理论后实证 / 先实证后理论 / 交替) 及推演 3 层 (审稿人质疑→回应→再质疑)
  - 阶段2 部分填空: 给定 2 条路径，让学生评估说服力并选最优
  - 阶段3 独立解: 学生为自己的 IMRaD 草稿独立设计 3 条论证路径并选最优

## progressive_project (CS230 式 proposal → milestone → final → poster)

- **proposal (Day 3)**: 提交 1 页研究问题 + IMRaD 大纲 + 数据集选择 (NSW/自选 A/B 测试)，含天道推演论证路径草图
- **milestone (Day 7)**: 提交 Methods + Results 草稿，含 APA 统计报告 + 95% CI，跑通 statsmodels ttest_ind
- **final (Day 14)**: 完整 IMRaD 短论文 (2000 字)，含 Title/结构化 Abstract (200 词内)/Discussion 六要素
- **poster (Day 17)**: 1 页学术海报，含核心 figure (NSW 效应量 forest plot) + LLM-as-a-judge 自评分表

## interleaving (交叉排布, 不块状)

按 A1B1C1 → B2C2A2 → C3A3B3 交叉排布 (避免连续同类型)：

| 周 | 周一 | 周三 | 周五 |
|----|------|------|------|
| W1 | A1 (结构辨识 drill) | B1 (NSW t 检验) | C1 (judge checklist) |
| W2 | B2 (APA 模板填空) | C2 (偏差自检) | A2 (天道推演论证路径) |
| W3 | C3 (全 IMRaD judge) | A3 (跨论文节占比对比) | B3 (多变量 APA 报告) |

明文交叉顺序：A1 → B1 → C1 → B2 → C2 → A2 → C3 → A3 → B3 (A=结构/B=统计/C=评审 三类技能轮转, 不连续两节同类)

## retry_policy (CS230 式)

- 10 free late days (整学期), 用完每日 -1 分
- 任一 drill 失败可重试，重试不罚分 (取最高分)
- diagnostic < 4 分自动开放 A 的 worked example 重学入口，不计入 late days

## weak_loop (连续 2 次失败触发)

连续 2 次同一 drill 失败 (分数 < 60%) 触发**弱项循环**：
1. 回退到上一 drill (如 C1 失败 → 回 B1 重做)
2. 强制观看对应 subskill 的 worked example (阶段1 完整示范)
3. 完成 1 次部分填空 (阶段2) 才能重新挑战原 drill
4. 弱项循环内的 reps 不计入 reps_required，需额外完成

> 例：学生 C1 (LLM-as-a-judge) 连续 2 次给所有部分同分 → 触发 weak_loop → 回退 B1 重做 APA 报告 (巩固统计严谨性, 这是 judge Results 的前置) → 看 C1 阶段1 完整示范 → 完成 C1 阶段2 部分填空 → 再战 C1 阶段3。
