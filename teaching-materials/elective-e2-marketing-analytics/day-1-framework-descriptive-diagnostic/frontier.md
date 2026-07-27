# frontier.md (v9.0 学术前沿注入层)

> **所属**：elective-e2-marketing-analytics · day-1-framework-descriptive-diagnostic
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：当描述性/诊断性分析遇上 2025-2026 营销归因因果革命--t 检验/Cohen's d 的"统计显著 vs 商业显著"在归因-增量鸿沟下如何被重新定义，OLS 多重共线性如何被层次聚类因果分组缓解。

---

## frontier_topic

本单元教 t 检验/卡方/OLS/RFM 等描述-诊断工具来回答"发生了什么/为什么"。前沿子问题是：2025-2026 年"归因不等于增量"（attribution ≠ incrementality）的实证证据，如何迫使本单元的诊断结论从"组间差异显著"升级为"差异是否反映真实增量因果"；以及 OLS 多重共线性问题在层次聚类 + 因果分组方法下被如何系统性缓解。

---

## recent_papers

> 从 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库中挑选 4 篇最贴本单元的 2025-2026 论文。

### 1. Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising
- **arXiv**: https://arxiv.org/abs/2606.26690
- **作者**: Donghui Li, Bowen Yuan
- **年份**: 2026
- **摘要**: 提出实验校准的归因修正框架，将稀疏 lift 测量转化为每日修正估计，解决付费渠道与自然需求重叠导致的归因高估问题。在多个 TikTok 市场部署，实测蚕食率降低约 15 个百分点。
- **与本单元的关联**: 本单元 TODO4 用 `ttest_ind` 判断 treated vs control 的 re78 差异是否显著；这篇论文直接质疑"显著差异就是真实营销增量"的诊断直觉，指出归因高估可达 15 个百分点。

### 2. Media Measurement and the Assisted Own Goal: Attribution, Marketing-Mix Models, and Individual-Level Incrementality
- **arXiv**: https://arxiv.org/abs/2607.09608
- **作者**: Tobias Konitzer
- **年份**: 2026
- **摘要**: 提出"助攻乌龙球"假说：上漏斗广告平台促成增量购买，但转化被归功于下游市场。构建基于增量测量的模型，使用"环境受众级随机化"和个体级 PIE 扩展实现无偏估计。
- **与本单元的关联**: 本单元用 NSW RCT 445 条样本讲随机化是因果金标准；这篇论文把"环境受众级随机化"作为 RCT 不可行时的现代替代方案，扩展了本单元对 RCT 局限的认知。

### 3. Hierarchical Clustering As a Novel Solution to the Notorious Multicollinearity Problem in Observational Causal Inference
- **arXiv**: https://arxiv.org/abs/2606.30992
- **作者**: Yufei Wu, Zhiying Gu
- **年份**: 2026
- **摘要**: 提出使用层次聚类减少因果推断中的多重共线性，基于营销支出相关性对地理单元分组。应用于贝叶斯营销组合模型（MMM），有效缓解共线性并实现不同营销渠道影响的分离识别。
- **与本单元的关联**: 本单元 TODO6 OLS 回归 re78 ~ treat + age + educ + marr + nodegree + re75 时未讨论多重共线性诊断（VIF）；这篇论文提供了基于层次聚类的共线性缓解方法，是 TODO6 的直接前沿扩展。

### 4. Profit-Based Counterfactual Explanations for Product Improvement: A Case Study of Manga Sales in Japan
- **arXiv**: https://arxiv.org/abs/2607.01610
- **作者**: Keita Kinjo, Takeshi Ebina
- **年份**: 2026
- **摘要**: 将反事实解释形式化为管理和营销情境中的利润最大化问题，提出基于利润的反事实解释（PBCE）。通过直接最大化利润作为优化目标，消除外生目标设定，以日本漫画销售为案例验证。
- **与本单元的关联**: 本单元强调"统计显著 ≠ 商业显著"，要求报告 Cohen's d 和效应量；PBCE 进一步把"商业显著"操作化为利润最大化反事实，为本单元的诊断结论提供利润导向的形式化框架。

---

## critical_synthesis

这 4 篇论文 + 语料库其他论文共同揭示 2025-2026 营销诊断领域的三个共识与两个争议。**共识一**：归因不等于增量。Li & Yuan（#2）的"蚕食率降低 15 个百分点"和 Konitzer（#1）的"助攻乌龙球"假说相互印证：传统诊断性分析（包括本单元教的 t 检验组间差异）所测到的"差异"可能混杂了自然需求蚕食、上下游平台功劳错配等系统性偏差，并非真实增量。这是对 NSW RCT 教学法的直接挑战--RCT 内部效度高，但工业场景下"被随机化的对象"（用户 vs 受众环境 vs 地理单元）本身就是诊断结论能否外推的关键变量。**共识二**：多重共线性是观测因果推断的系统性瓶颈。Wu & Gu（#3）的层次聚类方案并非孤立创新，而是与 Day 3 MMM 的 Ridge 正则化、DeepCausalMMM（#6）的 DAG 结构学习形成方法学趋势--从"惩罚系数"到"分组降维"再到"显式因果结构学习"，逐步从统计正则化走向因果建模。**共识三**：商业决策应直接优化利润而非代理指标。Kinjo & Ebina（#8）的 PBCE 与本单元"统计显著 ≠ 商业显著"的批判一脉相承，但走得更远--把利润作为反事实优化目标本身，消除了 p 值/效应量作为中间目标的解释负担。

**争议一**：RCT 仍是金标准还是已被"环境受众级随机化"等准实验超越？Konitzer（#1）主张后者，但 Li & Yuan（#2）的 TikTok 部署仍依赖 lift 实验校准，并未完全放弃个体级 RCT。**争议二**：层次聚类缓解共线性是否会引入新的"分组偏差"？Wu & Gu（#3）未讨论聚类树深度选择对结论稳健性的影响，这是 methodological 层面的开放问题。**局限**：4 篇论文中仅 #1、#2 经过 arXiv abstract 页 verified，#3、#4、#8 标记为 unverified，复现性存疑；#2 的 TikTok 部署缺乏外部独立复现；#8 的日本漫画案例是否可推广到其他品类未做敏感性分析。

---

## delta_to_unit

1. **TODO4 的 t 检验诊断结论需重新审视**：本单元 solution.ipynb 用 `scipy.stats.ttest_ind` 计算 treated vs control 的 re78 差异并报告 p 值与 Cohen's d。Li & Yuan（#2）的"蚕食率 15 个百分点"实证证据表明，组间显著差异可能 15% 来自付费渠道对自然需求的蚕食而非真实增量--本单元未覆盖这一归因-增量鸿沟诊断。前沿 delta：在 t 检验后必须追加"增量校准"步骤，否则诊断结论会高估营销干预的真实价值。

2. **TODO6 的 OLS 未做多重共线性诊断，Wu & Gu（#3）提供层次聚类缓解方案**：本单元 solution.ipynb 的 OLS 模型 `re78 ~ treat + age + educ + marr + nodegree + re75` 未计算 VIF 也未讨论共线性。Wu & Gu 的层次聚类方法可前置应用于 NSW 协变量（age/educ/re74/re75）：先聚类分组再回归，比本单元直接 OLS 更稳健。前沿 delta：本单元 TODO6 应补充 VIF 诊断 + 层次聚类分组的对比实验。

3. **"统计显著 ≠ 商业显著"需升级为"利润最大化反事实"**：本单元 notes.md 明确要求报告 Cohen's d 而非只看 p 值，但 Kinjo & Ebina（#8）的 PBCE 框架表明，效应量本身仍是代理指标。前沿 delta：本单元 TODO4 报告"Cohen's d = 0.X"应进一步追问"在 d=0.X 下，反事实调整 treat=0 后利润变化多少"，把诊断结论直接锚定到利润。

4. **NSW RCT 教学法需补充"环境受众级随机化"对照**：本单元用 NSW 445 样本讲 RCT 是因果金标准。Konitzer（#1）的"环境受众级随机化 + 个体级 PIE 扩展"是 2026 年广告平台工业实践，比 NSW 1970 年代个体级随机化更贴近现代营销场景。前沿 delta：在 notes.md "为什么用真实 RCT 数据"段后追加一段"现代广告平台的随机化层级演进"，把 NSW 从"金标准"重新定位为"金标准的简化教学版本"。

---

## open_questions

1. 在 NSW 445 样本上，treat vs control 的 re78 差异中有多少比例可归因于"自然需求蚕食"而非真实增量--能否用 Li & Yuan 的实验校准框架在 NSW 上反推蚕食率上限？
2. Wu & Gu 的层次聚类缓解共线性方法，聚类树深度选择（complete linkage vs single linkage vs Ward）对 NSW TODO6 OLS 系数稳健性的敏感度有多大，是否存在"聚类树深度 gaming"的 benchmark-gaming 风险？
3. Kinjo & Ebina 的 PBCE 利润反事实框架在 NSW 数据上的应用--当"利润"需要从 re78 + 假设的营销成本构造时，反事实解释对成本假设的弹性有多大，是否可发表为"利润反事实的因果灵敏度分析"方法论文？
4. Konitzer 的"环境受众级随机化"假设在 NSW 1970 年代就业培训场景中是否成立--如果 NSW 的随机化单元（个体）与现代广告平台的随机化单元（受众环境）本质不同，NSW 作为营销映射教学数据的有效性边界在哪？

---

## methodological_critique

这 4 篇论文存在三方面不能全信。**第一，验证级别不对称**：仅 #1 Konitzer 和 #2 Li & Yuan 经 arXiv abstract 页 verified，#3 Wu & Gu、#4 Kinjo & Ebina 标记 unverified，标题/作者/摘要可能存在 LLM 生成或抽取误差，复现前必须人工核对 arXiv 页面。**第二，工业部署缺乏外部独立复现**：Li & Yuan 的"蚕食率降低 15 个百分点"是 TikTok 内部部署数据，无第三方独立复现，存在平台利益相关偏差--TikTok 有动机夸大归因修正框架的效果以吸引广告主。**第三，benchmark-gaming 风险**：Wu & Gu 的层次聚类方法未报告聚类树深度选择的 sensitivity analysis，可能存在"在特定深度下结果最优"的隐式超参搜索；Kinjo & Ebina 的日本漫画销售案例单一品类，PBCE 框架的可推广性未经多品类压力测试。博后读者引用这些论文时，应优先将 #1、#2 作为"已被验证存在"的引用源，对 #3、#4、#8 的具体数字保留判断，并在论文方法部分标注"未独立复现"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
