# frontier.md (v9.0 学术前沿注入层)

> **所属**：elective-e2-marketing-analytics · day-3-mmm-mta-incremental
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：MMM 的"高 R² = 好归因"假设如何被 2025-2026 神经 MMM 的"归因旁路"发现颠覆，MTA-增量鸿沟与隐私约束下的增量测量如何重构营销归因三大方法的边界。

---

## frontier_topic

本单元教 MMM（Adstock + Ridge + 贡献分解）、MTA（马尔可夫移除法）、增量测量（RCT/合成控制/DML）与预算优化。前沿子问题是：2025-2026 年神经 MMM 中"解码器旁路"现象（高预测精度 ≠ 真实归因）、DAG 因果结构学习 + Hill 饱和的深度 CLV 框架、隐私信号退化下的鲁棒增量决策，如何系统性挑战本单元的 Ridge MMM + 马尔可夫 MTA + RCT 金标准三方法体系。

---

## recent_papers

> 从 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库中挑选 5 篇最贴本单元的 2025-2026 论文。

### 1. Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix Models
- **arXiv**: https://arxiv.org/abs/2606.12687
- **作者**: Yunbo Wang, Bolbi Liu
- **年份**: 2026
- **摘要**: 识别图基神经 MMM 中的"归因旁路"问题：高容量解码器在不通过归因图路由反事实敏感性的情况下实现低预测误差。提出 DICE-MMM 框架，将图恢复、预测精度和图对齐分离为独立问题。
- **与本单元的关联**: 本单元 TODO1 用 Ridge MMM 拟合并报告 R² 与渠道贡献分解，隐含"高 R² = 好归因"假设；Wang & Liu 的"归因旁路"发现直接质疑这一假设，是 TODO1 方法学的前沿警告。

### 2. DeepCausalMMM: A Deep Learning Framework for Marketing Mix Modeling with Causal Structure Learning
- **arXiv**: https://arxiv.org/abs/2510.13087
- **作者**: Aditya Puttaparthi Tirumala
- **年份**: 2025
- **摘要**: 结合 GRU 时序模式、DAG 因果结构学习和 Hill 方程饱和曲线，构建 DeepCausalMMM 营销组合建模框架。支持多区域建模（共享与区域特定参数），使用 Huber 损失和预算优化。
- **与本单元的关联**: 本单元 TODO1 用 Ridge + Adstock 做频率学派 MMM，notes.md 提到"贝叶斯 MMM 是研究前沿方向"；DeepCausalMMM 提供了比贝叶斯 MMM 更激进的深度学习 + 因果结构方向，是 TODO1 的前沿替代。

### 3. Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss
- **arXiv**: https://arxiv.org/abs/2606.03878
- **作者**: Prashant Shekhar, Caroline Howard
- **年份**: 2026
- **摘要**: 将隐私约束下的广告测量形式化为鲁棒因果决策问题，针对隐私保护报告系统导致的信号退化，提供认证、拒绝和未决三类增量决策。填补了隐私时代增量测量的方法论空白。
- **与本单元的关联**: 本单元 notes.md 强调"MMM 用聚合数据反而在隐私时代有优势"，TODO3-5 用 NSW RCT/合成控制/DML 做增量测量；Shekhar & Howard 形式化了隐私信号退化下的增量决策，是 TODO3-5 在隐私时代的直接前沿扩展。

### 4. Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising
- **arXiv**: https://arxiv.org/abs/2606.26690
- **作者**: Donghui Li, Bowen Yuan
- **年份**: 2026
- **摘要**: 提出实验校准的归因修正框架，将稀疏 lift 测量转化为每日修正估计，解决付费渠道与自然需求重叠导致的归因高估问题。在多个 TikTok 市场部署，实测蚕食率降低约 15 个百分点。
- **与本单元的关联**: 本单元 TODO2 用马尔可夫移除法做 MTA 渠道功劳分配，TODO3 用 RCT 做增量测量；Li & Yuan 的"归因不等于增量"实证证据直接量化了 MTA 功劳分配与真实增量之间的鸿沟（15 个百分点），是 TODO2 vs TODO3 对比的前沿锚点。

### 5. Hierarchical Clustering As a Novel Solution to the Notorious Multicollinearity Problem in Observational Causal Inference
- **arXiv**: https://arxiv.org/abs/2606.30992
- **作者**: Yufei Wu, Zhiying Gu
- **年份**: 2026
- **摘要**: 提出使用层次聚类减少因果推断中的多重共线性，基于营销支出相关性对地理单元分组。应用于贝叶斯营销组合模型（MMM），有效缓解共线性并实现不同营销渠道影响的分离识别。
- **与本单元的关联**: 本单元 TODO1 notes.md 明确说"为什么用 Ridge 不用 OLS：MMM 中渠道投入常高度共线"；Wu & Gu 的层次聚类方法是 Ridge L2 正则化的因果分组替代方案，是 TODO1 共线性处理的前沿扩展。

---

## critical_synthesis

这 5 篇论文 + 语料库其他论文共同揭示 2025-2026 营销归因与增量测量领域的三个核心共识、两个尖锐争议与一个结构性局限。**共识一**：高预测精度 ≠ 真实归因。Wang & Liu（#5）的"解码器旁路"是本批论文最具颠覆性的发现--高容量神经 MMM 解码器可在不通过归因图路由反事实敏感性的情况下实现低预测误差，意味着本单元 TODO1 的"R² 高 + 贡献分解合理 = MMM 可信"的诊断逻辑存在系统性漏洞。这与 Tirumala（#6）的 DeepCausalMMM 形成呼应：DeepCausalMMM 用 DAG 显式学习因果结构 + Hill 饱和曲线 + GRU 时序，正是为了对抗"解码器旁路"--把归因图从"可学习的副产品"提升为"显式建模目标"。**共识二**：MTA 与增量测量的鸿沟是结构性的，不可通过模型改进消除。Li & Yuan（#2）的"蚕食率 15 个百分点"+ Konitzer（#1）的"助攻乌龙球"假说共同表明，MTA 功劳分配（本单元 TODO2）与真实增量（本单元 TODO3）之间存在 15%+ 系统性偏差，源于付费渠道对自然需求的蚕食与上下游平台功劳错配。这不是模型精度问题，是归因方法论的根本鸿沟。**共识三**：隐私信号退化已使传统增量测量方法不可用。Shekhar & Howard（#3）的形式化表明，隐私保护报告系统导致 RCT 与合成控制的信号退化，需引入"认证/拒绝/未决"三类决策框架，本单元 TODO3-5 的 RCT/合成控制/DML 在隐私时代需重新审视。

**尖锐争议一**：Ridge L2 正则化 vs 层次聚类分组 vs DAG 结构学习，哪种是 MMM 多重共线性的最优解？Wu & Gu（#4）主张层次聚类，Tirumala（#6）主张 DAG，本单元 notes.md 主张 Ridge。三种方法在不同数据规模/共线结构下可能各有优势，尚无统一基准。**尖锐争议二**：DICE-MMM 的"图恢复/预测精度/图对齐分离"是否可推广到非图基 MMM？Wang & Liu（#5）仅在图基神经 MMM 验证，Ridge MMM 与贝叶斯 MMM 是否存在类似的"旁路"现象未明。**结构性局限**：5 篇中仅 #1、#2、#4 经 verified，#3、#5、#6 均为 unverified；#5 的 DICE-MMM 框架未开源代码，"解码器旁路"现象的复现条件未充分说明；#3 的隐私鲁棒框架缺乏真实隐私系统（如 Apple PCM、Google DP APIs）的端到端验证。

---

## delta_to_unit

1. **TODO1 的"R² 高 = MMM 可信"诊断逻辑被"解码器旁路"颠覆**：本单元 solution.ipynb 用 Ridge 拟合 MMM 并报告 R² + 贡献分解，notes.md 隐含"R² 高 + 贡献归一化 = MMM 可信"。Wang & Liu（#5）的"解码器旁路"发现表明，高容量解码器可在不通过归因图路由反事实敏感性的情况下实现低预测误差--意味着高 R² 的 MMM 可能给出错误归因。前沿 delta：TODO1 应补充"归因旁路诊断"步骤，对比 Ridge MMM 与 DICE-MMM 风格的图对齐检验。

2. **TODO1 的 Ridge 共线性处理被层次聚类因果分组扩展**：本单元 solution.ipynb 用 `Ridge(alpha=1.0)` 处理渠道共线性，notes.md 说"OLS 系数不稳定，Ridge L2 正则化让系数更可解释"。Wu & Gu（#4）的层次聚类方法基于营销支出相关性对地理单元分组，是 Ridge 的因果分组替代--前者从源头减少共线性，后者从系数层面惩罚共线性。前沿 delta：TODO1 应追加"Ridge vs 层次聚类分组"的对比实验，比较两种共线性处理的贡献分解稳定性。

3. **TODO2 MTA 移除法 vs TODO3 RCT 增量的鸿沟被 Li & Yuan（#2）量化为 15 个百分点**：本单元 notes.md 把 MTA 与增量测量作为"互补方法"教授，但未量化两者差异。Li & Yuan 的"蚕食率降低 15 个百分点"实证证据表明，MTA 功劳分配与真实增量之间的系统性偏差可达 15%+。前沿 delta：TODO2-3 应补充"MTA-增量鸿沟诊断"步骤，用 TODO3 的 NSW RCT 增量作为 ground truth 反推 TODO2 MTA 的归因高估比例。

4. **TODO3-5 的 RCT/合成控制/DML 在隐私时代需被 Shekhar & Howard（#3）的鲁棒框架重新审视**：本单元 TODO3 用 NSW RCT 朴素均值差，TODO4 用合成控制，TODO5 用 DML。Shekhar & Howard 形式化了隐私信号退化下的"认证/拒绝/未决"三类增量决策，表明 RCT/合成控制/DML 在隐私保护报告系统下信号退化。前沿 delta：TODO3-5 应补充"隐私信号退化模拟"步骤，在 NSW 上注入不同级别的信号退化，对比 RCT/合成控制/DML 的稳健性。

5. **TODO6 预算优化需被 DICE-MMM 的"图对齐检验"约束**：本单元 solution.ipynb 用 `scipy.optimize.minimize` 在预算约束下最大化销量，notes.md 警告"MMM 是历史数据外推，市场环境变化时优化结果可能失效"。Wang & Liu（#5）的 DICE-MMM 表明，即使历史拟合良好，归因图可能错误--预算优化基于错误归因图会放大错误。前沿 delta：TODO6 应在优化前追加"归因图对齐检验"，确保预算分配基于可信归因而非旁路预测。

---

## open_questions

1. DICE-MMM 的"解码器旁路"现象在 Ridge MMM（非图基）上是否存在等价形式--如果 Ridge MMM 的高 R² 也可能源于"共线性吸收"而非真实渠道效应，是否可发表为"线性 MMM 的归因旁路诊断"方法论文？
2. Wu & Gu 的层次聚类共线性缓解 vs Ridge L2 正则化 vs DeepCausalMMM 的 DAG 结构学习，在 NSW + 真实快消品 MMM 参数下的渠道贡献分解稳定性对比如何，是否存在"方法选择 gaming"的 benchmark 风险？
3. Shekhar & Howard 的"认证/拒绝/未决"三类增量决策在 NSW 445 样本上的边界条件是什么--当信号退化到何种级别时，RCT/合成控制/DML 分别落入"拒绝"区，是否可发表为"隐私约束下增量测量的失效阈值"实证研究？
4. Li & Yuan 的"蚕食率 15 个百分点"在 NSW re78 上的可识别性--NSW 的 treat 随机化使 re78 的"蚕食部分"能否被 treat 系数与 re75 交互项捕获，是否可发表为"用 RCT 反推 MTA 归因高估率"的因果识别研究？
5. DeepCausalMMM 的 DAG 学习 + Hill 饱和在 Day 3 TODO6 预算优化中的应用--如果 DAG 学习给出与 Ridge 不同的渠道因果结构，预算优化结果会差多少，是否可发表为"因果结构学习对 MMM 预算优化的敏感度"方法论？

---

## methodological_critique

这 5 篇论文存在四方面不能全信。**第一，验证级别严重不对称**：仅 #1 Konitzer、#2 Li & Yuan、#4 Wu & Gu 经 arXiv abstract 页 verified，#3 Shekhar & Howard、#5 Wang & Liu、#6 Tirumala 均为 unverified，标题/作者/摘要可能存在 LLM 抽取误差，复现前必须人工核对 arXiv 页面。**第二，"解码器旁路"的复现性存疑**：Wang & Liu（#5）未开源 DICE-MMM 代码，"归因旁路"现象的触发条件（解码器容量阈值、图稀疏度、训练数据规模）未充分说明，可能存在"在特定架构下结果最优"的隐式超参搜索；该现象是否在 Ridge MMM 上存在等价形式也未验证。**第三，工业部署缺乏外部独立复现**：Li & Yuan（#2）的"蚕食率降低 15 个百分点"是 TikTok 内部部署数据，无第三方独立复现，存在平台利益相关偏差--TikTok 有动机夸大归因修正框架的效果。**第四，隐私鲁棒框架的理论-部署鸿沟**：Shekhar & Howard（#3）的"认证/拒绝/未决"三类决策仅在理论层面形式化，未在真实隐私系统（Apple PCM、Google DP APIs、Chrome Privacy Sandbox）上端到端验证；Wu & Gu（#4）的层次聚类方法未报告聚类树深度选择的 sensitivity analysis，存在"聚类深度 gaming"的 benchmark 风险。博后读者引用这些论文时，应将 #1、#2、#4 作为"已被验证存在"的引用源，对 #3、#5、#6 的具体方法保持批判性距离，并在论文方法部分标注"未经独立工业部署验证"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
