# 产业链接层 (v7.0) · 规模实验与营销应用

> v7.0 升级: 把 Day 5 (NSW + Thompson MAB + CausalForestDML CATE + Uplift Qini) 的研究产出翻译为**产业链接**。本文件锚定 >=3 家真实企业 (从公司库挑), 演示自适应实验/异质效应/增量建模如何在生产中创造价值, 并给出 Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针四类衔接。

---

## real_companies

>=3 家真实企业锚点 (从 v7.0 公司库挑, 全部与本单元主题匹配):

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Microsoft ExP** (Experimentation Platform) | 自适应实验 / MAB | Microsoft 365 / Bing / Azure 每年跑 >20,000 个受控实验; ExP 团队是 Kohavi《Trustworthy Online Controlled Experiments》作者的母单位, 把固定 A/B + 序贯检验 + 部分自适应 (MAB) 工业化部署, 直接对标 Day 5 TODO3 的 Thompson Sampling 与"实验成本节省"权衡。 |
| **Booking.com** | A/B 规模化 / CATE 异质效应 | 全球最大 A/B 测试团队之一 (年实验数 >1,000), 在搜索排名/定价/页面优化上用因果推断识别"对哪类用户改变 UI 收益最大", 直接对标 TODO4 econml CausalForestDML CATE 与 TODO6 Uplift "可被说服"群体。 |
| **Meta Ads** | 营销归因 / 自适应创意优化 (DCO) | Meta Ads 平台用 MAB 做动态创意优化 (Dynamic Creative Optimization), 对广告创意/受众组合自适应分配流量, 直接对标 Day 5 MAB 营销应用; 配合 MMM (Media Mix Modeling) 做跨渠道增量归因, 对标 Day 5 MMM Adstock/饱和/协同理论。 |
| **Unilever** | Uplift 增量营销 / CPG 精准投放 | 快消巨头 Unilever 在 CRM/优惠券/电商推广上从"全量发券"走向"Uplift 精准投放", 把用户分"可被说服/必然转化/必不转化/反响应"四类, 只对"可被说服"发券, 直接对标 Day 5 2026 前沿 Uplift Modeling + Qini 曲线, 解决"反响应"用户被优惠券伤害的真实业务痛点。 |

---

## deployment_example

**真实合理部署场景: Meta Ads 动态创意优化 (DCO) + 异质效应投放**

- 规模: Meta Ads 每天服务 >1,000 万广告主, 单广告位有 >50 个创意变体 (文案/图/视频/CTA)。固定 A/B 每个变体需跑 7-14 天 + 数十万曝光才显著, 全量测试成本极高。Meta 用 Thompson Sampling MAB (类 Day 5 TODO3) 自适应分配流量到高 CTR 创意, 在线更新 Beta 后验, 把实验成本降低约 30-50%。
- 约束: (a) 实时性--MAB 决策需 <50ms; (b) 探索-利用权衡--新创意需保证最小曝光防冷启动死锁; (c) 因果可识别性--自适应数据分布受前期策略影响, Meta 用 IPW (逆概率加权) + 加权似然消除选择偏差 (类 Day 5 MAB 与因果推断关系)。
- 异质效应: Meta 在 MAB 之上叠加 CATE 模型 (类 TODO4 CausalForestDML), 估计"哪类用户对哪类创意响应最大", 实现 audience × creative 的二维 Uplift 投放。结合 Qini 曲线 (类 TODO6) 评估"按预测 CATE 从高到低投放, 累计增量转化", 把广告预算从"必然转化"用户重分配到"可被说服"用户。
- 效果: 工业级案例 (Meta 公开技术博客) 显示自适应实验 + CATE 投放在 ROAS (广告支出回报率) 上提升 10-20%。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**

- **Partner (赞助企业)**: Sephora (LVMH 旗下美妆零售, 公司库候选)
- **Problem**: Sephora CRM 有 >5,000 万会员, 当前"全量发券"策略在优惠券上年支出 >$2 亿, 但 Uplift 分析发现仅 ~30% 优惠券真正驱动增量转化, 其余浪费在"必然转化"或伤害"反响应"用户。Sephora 希望用因果推断 + Uplift 重新设计优惠券投放, 在相同预算下最大化增量 GMV。
- **Data**: Sephora 提供 12 个月去标识化会员级数据 (是否收到优惠券 T, 12 个月内 GMV Y, 协变量 X: 历史购买/品类偏好/会员等级/最近活跃/地区/设备); 已有 RCT 数据 (随机发券的 A/B 测试历史, ~50 万样本)。
- **Scope**: 8 周, 4-5 人团队。Week 1-2 数据清洗 + EDA + ATE 估计 (类 Day 5 TODO2); Week 3-4 CATE 估计 econml CausalForestDML (类 TODO4) + 安慰剂检验 (类 TODO5); Week 5-6 Uplift Qini + 四类用户分类 (类 TODO6); Week 7-8 投放策略原型 + A/B 验证 + 报告。
- **Deliverable**: (a) Uplift 模型原型 (Python, 可复跑, Sephora 数据团队可接手); (b) 投放策略建议书--"可被说服"群体识别规则 + 预算重分配方案; (c) Imperial MSc BA 论文 + Sephora 内部 CMO 汇报; (d) 预期增量 GMV 提升测算 (保守 5-10%)。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist**: Sarah Chen, Unilever 全球高级总监 Head of AI Marketing (虚构人名, 真实岗位)。
- **Decision**: Unilever 2026 年 Q1 全球 CRM 预算 $5 亿, 是否从"固定 A/B + 全量发券"切换到"自适应实验 (MAB) + Uplift 精准投放", 并把 30% 预算转向识别出的"可被说服"用户群?
- **Tension (核心两难)**:
  - (a) **实验成本节省 vs CATE 估计方差**: MAB 节省实验成本 (Day 5 TODO3 Thompson Sampling), 但 CATE 在小样本/细分群体上方差大 (Day 5 TODO4 CausalForestDML), 可能误判"反响应"用户为"可被说服", 伤害 GMV。
  - (b) **短期 GMV vs 长期品牌**: Uplift 只投"可被说服", 但"必然转化"用户若不再收优惠券可能产生习惯依赖破坏, 长期品牌资产受损。
  - (c) **数据合规 vs 因果精度**: Unilever 全球数据跨 GDPR/CCPA/中国 PIPL 多法域, 精细 CATE 需用户级画像, 与隐私合规存在张力。
- **教学目标**: 学员在案例中应用 Day 5 三段式 (ATE → CATE → Uplift), 权衡 MAB 节省与 CATE 风险, 给出有数据支撑的投放策略建议。可对接 HBS Case Method + Imperial MSc BA。

---

## guest_lecture

- **Topic**: "From Trusted A/B to Uplift: How Booking.com Scales Causal Decisions Across 1,000+ Experiments a Year"
- **Speaker Profile**: Principal Data Scientist, Booking.com Experimentation Science Team (画像: 5-10 年工业级 A/B + 因果推断经验, NeurIPS/KDD 论文, 曾主导 Booking.com 自适应实验平台建设)。
- **内容大纲**:
  - (1) Booking.com 实验平台架构: 每年 >1,000 实验, CUPED 方差缩减, 序贯检验防 peeking (对接 Day 5 选择性停止陷阱)。
  - (2) 自适应实验在搜索排名/定价的落地: Thompson Sampling vs UCB 的工业权衡 (对接 Day 5 TODO3)。
  - (3) 异质效应从"是不是有效"到"对谁有效": econml CausalForestDML 在 Booking.com 的部署 (对接 Day 5 TODO4)。
  - (4) Uplift 的边界: 当"反响应"用户占比 >15% 时的业务警讯 (对接 Day 5 TODO6 + 2026 前沿)。
- **互动**: 学员带自己的 NSW starter.ipynb 结果, 与主讲人讨论"NSW 营销映射在真实 OTA 场景的迁移路径"。

---

## internship_pointer

- **机构 / 角色 (3 个候选, 学员按兴趣择一申请)**:
  1. **Microsoft ExP Research Intern (Redmond)**: 角色--Experimentation Science Intern, 主导自适应实验方法学 (MAB + 序贯检验) 在 Microsoft 365/Bing 的应用研究; 衔接--Day 5 TODO3 Thompson Sampling + Kohavi《Trustworthy Online Controlled Experiments》是面试必备; 申请窗口每年 9-11 月。
  2. **Meta Ph.D. Residency (Ads & Core Data Science)**: 角色--Causal Inference Resident, 在 Ads Ranking / DCO / MMM 项目做 12-18 个月驻留研究; 衔接--Day 5 MAB 营销应用 + MMM Adstock/饱和 + Uplift 是核心预备知识; 申请窗口每年 10-1 月。
  3. **econml/scikit-uplift Open Source Capstone (PyWhy 孵化器)**: 角色--开源贡献者 + GSoC-style 项目 (由 Microsoft Research / PyWhy 赞助); 衔接--Day 5 solution.ipynb 的 CausalForestDML + Qini 实现可作为 capstone 申请材料; 全年滚动。
- **衔接说明**: Day 5 的 `solution.ipynb` (NSW 三段式: MAB → CATE → Uplift) 是上述三角色的最小预备工件; 学员应在实习申请前完成 6 个 TODO + 一段 300 字分析 (作业要求), 并能口头解释 Thompson Sampling 后验更新 (TODO3) 与 CATE 安慰剂检验 (TODO5) 的逻辑。

---

*v7.0 产业链接层由 v7.0 升级 agent 追加, 不动 v5.0/v6.0 原文。产业链接遵循 Imperial MSc BA Consulting Project (Burberry/Expedia/J&J 模式) / HBS Case Method / MIT Sloan Action Learning 模式; 企业锚点全部从 v7.0 公司库挑选 (Microsoft ExP / Booking.com / Meta Ads / Unilever / Sephora)。*
