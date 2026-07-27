# 前沿语料库: elective-e2-marketing-analytics - 营销归因与增量测量

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. Media Measurement and the Assisted Own Goal: Attribution, Marketing-Mix Models, and Individual-Level Incrementality
- **arXiv**: https://arxiv.org/abs/2607.09608
- **作者**: Tobias Konitzer
- **年份**: 2026
- **摘要**: 提出"助攻乌龙球"假说: 上漏斗广告平台 (如短视频社交网络) 促成增量购买, 但转化被归功于下游市场. 构建基于增量测量的模型, 使用"环境受众级随机化"和个体级 PIE 扩展实现无偏估计.
- **验证**: verified

### 2. Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising
- **arXiv**: https://arxiv.org/abs/2606.26690
- **作者**: Donghui Li, Bowen Yuan
- **年份**: 2026
- **摘要**: 提出实验校准的归因修正框架, 将稀疏 lift 测量转化为每日修正估计, 解决付费渠道与自然需求重叠导致的归因高估问题. 在多个 TikTok 市场部署, 实测蚕食率降低约 15 个百分点.
- **验证**: verified

### 3. Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss
- **arXiv**: https://arxiv.org/abs/2606.03878
- **作者**: Prashant Shekhar, Caroline Howard
- **年份**: 2026
- **摘要**: 将隐私约束下的广告测量形式化为鲁棒因果决策问题, 针对隐私保护报告系统导致的信号退化, 提供认证、拒绝和未决三类增量决策. 填补了隐私时代增量测量的方法论空白.
- **验证**: unverified

### 4. Hierarchical Clustering As a Novel Solution to the Notorious Multicollinearity Problem in Observational Causal Inference
- **arXiv**: https://arxiv.org/abs/2606.30992
- **作者**: Yufei Wu, Zhiying Gu
- **年份**: 2026
- **摘要**: 提出使用层次聚类减少因果推断中的多重共线性, 基于营销支出相关性对地理单元分组. 应用于贝叶斯营销组合模型 (MMM), 有效缓解共线性并实现不同营销渠道影响的分离识别.
- **验证**: unverified

### 5. Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix Models
- **arXiv**: https://arxiv.org/abs/2606.12687
- **作者**: Yunbo Wang, Bolbi Liu
- **年份**: 2026
- **摘要**: 识别图基神经 MMM 中的"归因旁路"问题: 高容量解码器在不通过归因图路由反事实敏感性的情况下实现低预测误差. 提出 DICE-MMM 框架, 将图恢复、预测精度和图对齐分离为独立问题.
- **验证**: unverified

### 6. DeepCausalMMM: A Deep Learning Framework for Marketing Mix Modeling with Causal Structure Learning
- **arXiv**: https://arxiv.org/abs/2510.13087
- **作者**: Aditya Puttaparthi Tirumala
- **年份**: 2025
- **摘要**: 结合 GRU 时序模式、DAG 因果结构学习和 Hill 方程饱和曲线, 构建 DeepCausalMMM 营销组合建模框架. 支持多区域建模 (共享与区域特定参数), 使用 Huber 损失和预算优化.
- **验证**: unverified

### 7. Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions
- **arXiv**: https://arxiv.org/abs/2607.20694
- **作者**: Salavat Ishbulatov
- **年份**: 2026
- **摘要**: 将计划任务与执行动作之间的桥接形式化为拟线性 Fisher 市场, 计划任务为买方, 动作为可分割商品. 引入熵正则化推广, 与多触点归因 (multi-touch attribution)、最优传输和在线 Fisher 市场算法相关联.
- **验证**: unverified

### 8. Profit-Based Counterfactual Explanations for Product Improvement: A Case Study of Manga Sales in Japan
- **arXiv**: https://arxiv.org/abs/2607.01610
- **作者**: Keita Kinjo, Takeshi Ebina
- **年份**: 2026
- **摘要**: 将反事实解释形式化为管理和营销情境中的利润最大化问题, 提出基于利润的反事实解释 (PBCE). 通过直接最大化利润作为优化目标, 消除外生目标设定, 以日本漫画销售为案例验证.
- **验证**: unverified

## 备注
- 论文来自 arXiv "marketing attribution incrementality" 与 "marketing mix model causal" 两次搜索合并去重.
- 营销归因与增量测量在 arXiv 上属于小众交叉领域, 单一查询返回结果有限; 经两次搜索合并获得 8 篇 post-cutoff 论文.
- 覆盖核心主题: 归因修正 (#2), 增量测量 (#1, #3), 营销组合模型 (#4, #5, #6), 归因方法论 (#7), 营销反事实 (#8).
- verified 论文: #1 (Media Measurement) 和 #2 (Attributed But Not Incremental) 经 arXiv abstract 页确认存在且标题匹配.
- #6 (DeepCausalMMM) 发表于 2025-10, 是唯一一篇 2025 年论文, 其余均为 2026 年.
