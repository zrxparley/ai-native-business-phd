# 研究产出 (v7.0) - AI商业模式类型学 + PRISMA文献综述

> 本单元产出一个可发表研究工件 (publishable artifact): 研究问题 + 贡献声明 + 真实论文链接 + IMRaD大纲 + NeurIPS可复现清单 + research-to-practice翻译

## research_question

在 2023-2026 年的 arXiv 文献中, AI 商业模式五大类型 (基础设施 / 增强产品 / 原生产品 / 平台 / Agent经济) 的分布如何? Agent经济型占比是否随年份显著上升?

## contribution

**delta vs prior work**: 现有 AI 商业模式分类 (Accenture 三分法 / a16z 投资视角) 多基于专家访谈或个案归纳; 本研究用 **真实 arXiv API + PRISMA 系统文献综述 (160->96->30->30)** 实证验证五类型分布, 并用 ASReview 主动学习模拟加速筛选。增量在于: (1) 方法可重复 (arxiv.Search 查询串公开) (2) 样本可追溯 (每篇纳入文献有 arXiv ID) (3) 用天道推演对类型演化做贝叶斯预判, 而非静态分类。

## linked_paper

- **标题**: PRISMA 2020 声明 (Page et al., BMJ 2021) -- 本单元 PRISMA 四步流程的方法论源头
- **作者/年份**: Page MJ, McKenzie JE, Bossuyt PM, et al. / 2021
- **链接**: https://www.bmj.com/content/372/bmj.n71 (BMJ, 已验证)
- **关联**: 本单元 starter.ipynb 的 PRISMA 四步 (识别/去重/筛选/纳入) 直接对应 PRISMA 2020 Checklist §3-4; 真实数字 160->96->30->30 即 PRISMA Flow Diagram 的本单元实例化

补充真实链接 (均已验证, 见 reading.md):
- ASReview (AI辅助综述): https://github.com/asreview/asreview
- arxiv.py (查询库): https://github.com/lukasschwab/arxiv.py
- DeepSeek-V3 (LLM辅助摘要): https://github.com/deepseek-ai/DeepSeek-V3
- RAGAS (合成质量评估): https://github.com/explodinggradients/ragas

## imrad_outline

- **Introduction**: AI 商业模式分类现有研究多基于专家判断 (Accenture/a16z), 缺乏可重复的实证综述; 本文用 PRISMA 系统综述 + arXiv 真实文献构建并验证五类型学, gap = 实证分布 + 演化预判
- **Methods**: 数据 = arxiv.Search 4 条查询 (AI business model / LLM business model / generative AI commerce / AI marketing) 真实元数据; 流程 = PRISMA 四步 (识别160 -> 去重96 -> 筛选30 -> 纳入30); 分类器 = `classify_type(title, abstract) -> str` 五类型规则函数; 加速 = ASReview 主动学习模拟 (5篇种子集 + sklearn LogisticRegression + predict_proba 排序)
- **Results**: PRISMA 流程图真实数字 160/96/30/30; 五类型分布 (pandas.value_counts); 年份分布 (groupby); ASReview top-20% 覆盖率 vs 人工全读覆盖率对比
- **Discussion**: Agent经济型是否上升 (天道推演三沙盘分支: Agent主导 / 平台整合 / 基础设施商品化); 局限 = arXiv 偏 CS 文献, 缺商业实战案例; 未来工作 = 扩展到 Google Scholar / Semantic Scholar + LLM 辅助全文复筛

## reproducibility_checklist (NeurIPS/ACM 风格)

- [x] **code**: 代码在 `solution.ipynb`, 依赖见 `data/README.md` (arxiv / pandas / matplotlib / scikit-learn)
- [x] **data**: 真实数据 = arXiv API 实时查询 + `data/fallback.json` 离线快照 (160篇元数据); 来源 = arXiv.org 公开 API; 许可 = arXiv 非排他许可
- [x] **seeds**: ASReview 主动学习模拟用 `random_state=42` (sklearn LogisticRegression + 种子集采样)
- [x] **environment**: Python 3.11 + arxiv>=2.1.3 + pandas>=2.0 + matplotlib>=3.7 + scikit-learn>=1.3
- [x] **preregistration**: 4 条 arxiv.Search 查询串 + 五类型假设分布 (prior: 预估每类型几篇, 标注置信区间) 在 practice.md progressive_project proposal 阶段固化, 属假设预注册
- [x] **FAIR**: 数据可发现 (arXiv API 公开) / 可访问 (无认证) / 可互操作 (JSON 元数据) / 可重用 (CC 许可)

## research_to_practice

本研究可翻译为两个实践工件:
1. **HBR 风格文章**: "The 5 Types of AI Business Models -- and Which One Wins by 2028" (把类型学分布 + 天道推演演化预判转译为高管可读的决策框架, 类似 HBS working paper -> HBR article 路径)
2. **MIT Sloan 教学案例**: 以 Cursor/Midjourney 被 misclassify (AI原生 vs AI增强) 为案例钩子, 写一个 45 分钟教学案例, 让 MBA 学生用五类型框架重新分类并辩论 outcome-based pricing 的可持续性
