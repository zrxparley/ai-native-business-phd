# industry.md · Day 3 描述统计与推断统计 · 产业链接层 (v7.0)

> 锚定单元：技能0 · Day 3 · 描述统计与推断统计 (scipy.stats / t 检验 / 卡方 / Beta-Binomial / ASA p 值声明)
> 产出类型：产业链接 (industry linkage) · 真实企业锚点 + 部署场景 + 咨询项目 + 教学案例 + 客座讲座 + 实习指针
> 范式依据：Imperial College MSc Business Analytics 咨询项目模式 / HBS 案例法 / MIT Sloan 行动学习 (Action Learning)

---

## real_companies

下表列出 >=3 家真实企业锚点，全部来自本单元主题（A/B 测试 + 统计推断 + 频率派/贝叶斯）的相关公司库，按"与本单元关联度"排序：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Microsoft** (ExP - Experimentation Platform) | 直接对应本单元 scipy.stats.ttest_ind / chi2_contingency；ExP 是业界最早大规模部署频率派 A/B 测试 + 多重比较校正的平台之一，每年跑数十万实验 | Bing/Office/Edge 的搜索排名、UI 改版、推荐算法 A/B 测试，单实验百万级用户，需处理 SRM（Sample Ratio Mismatch）、peeking、heterogeneous treatment effects |
| **Netflix** | 直接对应本单元 Beta-Binomial 贝叶斯推断；Netflix 研究博客长期发表"贝叶斯 A/B 测试"主题，用层次贝叶斯处理多区域/多设备异质效应 | 推荐算法迭代、UI 界面（如封面个性化）、订阅漏斗优化；用贝叶斯后验直接回答"新方案更好的概率"，避免频率派 p 值被高管误读 |
| **Booking.com** | 直接对应本单元 t 检验 + 置信区间 + p-hacking 议题；Booking.com 是业界 A/B 测试规模最大的公司之一（年实验数万），公开发表过 online experimentation 与 Type I/II error 控制研究 | 搜索排序、酒店详情页、支付漏斗、信任徽章；面临"微小效应 + 大样本"陷阱（p 显著但商业意义微弱），与 ASA p 值声明第 3 条直接相关 |
| **Google** (Google Ads / Search) | 对应本单元 ttest_ind 两比例 Z 检验（广告点击率差异）；Google 内部用 scipy.stats 同类工具 + 自研 Causal Impact | 广告创意 A/B、搜索排名升级、YouTube 推荐卡；多重比较校正（BH/FDR）与连续 peeking 的 sequential testing 是日常 |
| **Spotify** | 对应本单元卡方独立性检验（用户分群 × 品类）+ Beta-Binomial 转化率估计 | Discover Weekly / Daily Mix 推荐算法迭代、Free-to-Premium 转化漏斗；用多臂老虎机 + 贝叶斯后验做自适应路由 |
| **Amazon** | 对应本单元描述统计（右偏客单价 AOV 用中位数）+ 频率派 t 检验 | 商品详情页、推荐卡、Prime 漏斗；面对右偏 spend 数据与本单元 TODO1 同构 |

> 说明：以上 6 家公司全部来自公司库（因果推断/A/B 类 + 营销分析类 + 零售/CPG 类），均真实存在且与本单元 scipy.stats/t检验/卡方/Beta-Binomial 主题匹配。

---

## deployment_example

**部署场景：Microsoft ExP 在 Bing 搜索排名 A/B 测试中规模化部署 scipy.stats 同类统计推断栈**

- **规模**：ExP 平台支持 Bing/Office/Edge 等产品线每年跑 **数十万次** A/B 实验，单实验覆盖百万到亿级用户。统计推断层使用与 scipy.stats.ttest_ind 同构的两样本 t 检验（含 Welch 校正）+ 多重比较校正（Benjamini-Hochberg FDR）+ 连续 peeking 的 always-valid p-values（mSPRT）。
- **约束**：
  1. **Sample Ratio Mismatch (SRM)**：分桶不均会污染所有推断，ExP 在 ttest_ind 前先跑卡方分桶校验（与本单元 TODO5 chi2_contingency 同族方法）。
  2. **Peeking 与 p-hacking**：持续观察 p 值会膨胀 Type I error。ExP 用 sequential testing 替代固定 horizon t 检验，并强制预注册（与本单元 research.md preregistration 项一致）。
  3. **异质处理效应 (HTE)**：整体 p 值显著可能掩盖子群负效应，ExP 用分段 t 检验 + Beta-Binomial 后验（与本单元 TODO6 同模型）做子群分析。
- **效果**：据 Kohavi et al. (2020)《Trustworthy Online Controlled Experiments》，ExP 每年通过 A/B 测试发现的"反直觉"获胜方案（即直觉判断错误、但统计显著提升）创造数亿美元增量收入；同时通过 SRM 检测与多重比较校正经手挡掉约 10-20% 的"假阳性"获胜方案。
- **与本单元映射**：ExP 的统计栈 = 本单元 TODO3 (ttest_ind) + TODO4 (Wilson CI) + TODO5 (chi2) + TODO6 (Beta-Binomial) 的工业放大版；本单元的 seed=42 1000 用户模拟是 ExP 亿级实验的"教学微缩"。

---

## consulting_project

**Imperial College MSc Business Analytics 风格咨询项目（8 周，4-5 人团队）**

- **Partner（赞助企业）**：Booking.com（或同业 Expedia、Burberry 数字营销部）
- **Problem（真实业务问题）**：Booking.com 的酒店详情页"信任徽章"实验出现"频率派 p<0.05 但效应量极小"的判定困境——产品经理催促全量上线，但数据科学家担心落入 ASA p 值声明第 3 条陷阱（p 显著 ≠ 商业显著）。需构建一套"频率派 + 贝叶斯对照报告 + ASA 六原则自检"的标准化分析流程。
- **Data（企业提供数据）**：Booking.com 提供 4 周内某实验的脱敏用户级数据（约 50 万行），字段：user_id、group(A/B)、converted(0/1)、spend(右偏)、market(EMEA/APAC/NA)、device(desktop/mobile)、user_segment(new/returning/VIP)。与本单元 1000 用户模拟数据字段一一对应，是"放大版"。
- **Scope（8 周，4-5 人）**：
  - W1-2：探索性描述统计（右偏 spend 用中位数 + IQR，对照本单元 TODO1-2）
  - W3-4：频率派推断（ttest_ind + Wilson CI + chi2 market×converted，对照 TODO3-5）
  - W5-6：贝叶斯 Beta-Binomial 后验（Beta(1,1) 先验 + 分市场层次先验，对照 TODO6）
  - W7：ASA 六原则自检 + 预注册模板（OSF）+ 企业内部 workshop
  - W8：final presentation + handover
- **Deliverable（交付物）**：
  1. **原型**：一份 Jupyter notebook（仿本单元 solution.ipynb 结构），自动生成"频率派 + 贝叶斯对照报告"
  2. **模型**：分层 Beta-Binomial（市场级先验共享）的 PyMC 实现，作为 TODO6 的工业扩展
  3. **策略**：企业 A/B 测试预注册 + 三量并报（p + CI + credible interval）SOP 文档
  4. **报告**：25 页咨询报告 + 15 分钟 final presentation（含 ASA 六原则自检表）

---

## case_study

**HBS 风格教学案例钩子（8-10 页 case + teaching note）**

- **Protagonist（主角）**：Lena Chen，某 DTC 美妆品牌（年 GMV ~$200M）Head of Growth Marketing，本科统计学背景，MBA。直接向 CMO 汇报。
- **Decision（关键决策点）**：新版落地页（B 组）A/B 测试跑了 14 天、n=10000，结果显示：转化率 B=6.2% vs A=3.1%，单侧 t 检验 p=0.041（<0.05），Wilson 95% CI=[0.5pp, 5.7pp]（不含 0）。但 Beta(1,1) 先验下的后验 95% credible interval=[0.3pp, 5.9pp]，且 P(B>A|data)=0.97（不是 0.95）。Lena 必须在周五 CMO 会议前决定：是否全量上线新版？
- **Tension（核心张力/两难）**：
  1. **频率派 vs 贝叶斯分歧**：p=0.041 刚过 0.05 线（边缘显著），但 Bayesian P(B>A)=0.97 未到 0.975 的"强证据"门槛——两派结论在阈值边缘不一致。
  2. **统计显著 vs 商业显著**：Wilson CI 下界 0.5pp，若真实提升只有 0.5pp，全年增量 GMV 仅 $1M，低于新版落地页的工程维护成本 $1.5M——ASA 第 3 条警告成真。
  3. **Peeking 嫌疑**：实验第 7 天 p=0.048 就被 PM 偷看过一次，可能已膨胀 Type I error；预注册时声明的 horizon 是 14 天，但 PM 的偷看违反了停止规则。
  4. **子群异质**：整体显著但 new 用户子群 p=0.12 不显著，VIP 子群 p=0.01 显著——全量上线可能伤害 new 用户。
- **教学目标**：让学员用本单元 scipy.stats.ttest_ind + chi2_contingency + Beta-Binomial 三件套复盘 Lena 的决策，照搬 research.md 的 ASA 六原则自检清单，理解"统计显著性 ≠ 商业显著性"在真实决策中的代价。

---

## guest_lecture

**客座讲座（90 分钟，本单元 Day 3 上机课后附加 session）**

- **Topic**：*From p-values to Posteriors: Building a Bayesian-Frequentist 对照 A/B Testing Practice at Scale*
- **Speaker Profile**：某全球流媒体平台（Netflix / Spotify 量级）Head of Experimentation 或 Senior Staff Data Scientist。背景：统计学或贝叶斯方法 PhD，曾在 Microsoft ExP 或 Booking.com 实验团队工作 5+ 年，主导过该平台从纯频率派 t 检验迁移到"频率派 + 贝叶斯对照"双轨报告。公开发表过 experimentation related blog / paper（如 Netflix Tech Blog《Improving Experimentation Efficiency at Netflix》系列）。
- **大纲**：
  1. (15 min) **War Story**：一次 p=0.049 全量上线后导致留存下降的事故——为什么 ASA 第 2 条救不了你，还需要效应量 + CI + 子群分析。
  2. (25 min) **频率派 vs 贝叶斯实操**：用本单元 TODO6 的 Beta-Binomial 做现场 live coding，对比 scipy.stats.beta.ppf credible interval 与 Wilson CI 的数值与语义差异。
  3. (25 min) **规模化挑战**：如何把 Beta-Binomial 扩展到层次贝叶斯（PyMC）；peeking / SRM / multiple testing 在亿级用户的处理。
  4. (25 min) Q&A：学员扮演 Lena Chen（见 case_study）向 speaker 提问决策建议。
- **衔接**：讲座内容直接对应本单元 notes.md"2026 前沿补充"的 PyMC 与可复现研究两条线，并为技能3因果推断铺垫。

---

## internship_pointer

**实习 / 驻留指针（本单元为该角色做准备的路径）**

- **机构/项目（候选）**：
  1. **Microsoft ExP Internship (Experimentation Platform)**——Redmond / Remote，12 周，每年春/暑期开放。岗位：Data Scientist Intern, Experimentation。
  2. **Google AI Resident / Data Scientist Intern, Search Ads Quality**——Mountain View，12-24 个月 residency（面向新毕业 PhD/MSc）。
  3. **Booking.com Data Science Internship (Amsterdam)**——专设 experimentation track，6 个月。
  4. **OpenAI / Anthropic Residency**（若学员转向 AI 安全/对齐方向）——12 个月，与本单元统计推断基础强相关（RLHF 中的偏好建模用 Beta-Binomial 同族模型）。
- **角色**：A/B Testing Analyst / Experimentation Data Scientist。日常工作：撰写实验预注册、跑 scipy.stats.ttest_ind + chi2_contingency、构建 Beta-Binomial 后验报告、用 PyMC 扩展层次贝叶斯、做 SRM 与 multiple testing 校正、向产品经理与 CMO 解释"p=0.04 边缘显著"的决策风险。
- **衔接（本单元如何为该角色做准备）**：
  1. **技术栈**：本单元 TODO3-6 直接覆盖 ExP / Netflix / Booking.com 面试的统计学技术题（t 检验 + 卡方 + 贝叶斯 + ASA 原则）。
  2. **可复现研究素养**：research.md 的 IMRaD + NeurIPS 风格 reproducibility_checklist 培养企业 experimentation 团队要求的预注册 + 三量并报习惯。
  3. **产业链接**：industry.md 的 case_study（Lena Chen）让学员提前体验企业真实决策张力，面试时可作"我曾分析过一个 p=0.04 边缘显著的 A/B 案例"的叙事素材。
  4. **下一站**：本单元学完后，学员应能在技能3（因果推断）中升级到 DML / 合成控制，进一步胜任 OpenAI / Anthropic Residency 中"超越 A/B 走向因果"的高级角色。

---

*industry.md v7.0 · 锚定 Day 3 描述统计与推断统计 · 公司全部来自公司库 · 遵循 Imperial MSc BA 咨询项目 / HBS 案例法 / MIT Sloan 行动学习模式 · 2026-07-26*
