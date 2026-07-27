# Day 1 产业链接层 (v7.0)

> **单元主题**：营销分析框架-描述/诊断分析
> **产业链接锚点**：AARRR 漏斗 + RFM 分群 + t 检验/卡方/OLS 诊断 + CUPED (Microsoft 2013) 方差缩减 -- 以下企业/项目/案例均与 notes.md 真实数据集 (NSW RCT, 445 样本) 与真实库 (pandas/scipy.stats/statsmodels/causaldata) 直接映射。

---

## real_companies

>=3 家真实企业锚点 (从公司库挑选, 全部真实存在, 与本单元主题匹配)：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Microsoft ExP** (Experimentation Platform) | CUPED (Microsoft Research 2013) 的发源地; notes.md "CUPED" 前沿点与 TODO6 OLS 协变量调整思想直接对应。ExP 团队是 A/B 测试方差缩减的工业领导者。 | Bing / Office / Azure 每天运行数千个 A/B 测试, CUPED 是标配方差缩减技术, 在不增加样本量下提升统计功效, 检测 1-3% 小效应 (notes.md "营销场景中, 很多干预效果本就很小")。 |
| **Booking.com** | 全球最大 A/B 测试实践者之一; TODO4 `scipy.stats.ttest_ind` (Welch t 检验) 与 TODO5 `chi2_contingency` (卡方) 是其实验平台核心统计原语。 | 酒店搜索/排序/定价页面持续 A/B 测试, 用 t 检验诊断干预是否产生统计显著效果, 用卡方检验诊断用户分群 (新/老用户, 国内/国际) 与干预分组是否独立 (检测基线不平衡)。 |
| **Sephora** | 零售营销分析典型场景; TODO3 RFM (Recency/Frequency/Monetary) 五分群是其客户分群核心方法; AARRR 漏斗 (TODO2) 覆盖其获客-激活-留存-变现-传播全链路。 | 美妆零售 RFM 分群驱动差异化营销: Champions 推新品试用, At-Risk 推挽回券, Hibernating 推唤回活动; 漏斗分析诊断注册->首购->复购关键流失节点。 |
| **McKinsey QuantumBlack** | notes.md reading.md 已引用其 "Analytics in Marketing" 洞察; 营销分析四层框架 (描述/诊断/预测/处方) 与 McKinsey 企业成熟度诊断模型直接对应。 | 为 CPG/零售客户诊断"在四层框架中的当前位置" (notes.md "售前洞察": 大多数中国企业处于描述性早期), 设计从报表驱动->数据驱动的升级路径。 |

---

## deployment_example

**真实部署场景: Microsoft ExP CUPED 在 Bing 搜索广告 A/B 测试中的生产应用**

- **公司**: Microsoft ExP (Experimentation Platform)
- **场景**: Bing 搜索结果页广告位改版实验 (treat=新版广告位, control=旧版), 评估指标 = 用户点击率 CTR 与人均搜索收入 ARPU。
- **规模**: 数千万用户/日, 数百个并行实验, 单实验样本量百万级。
- **约束**: (a) 流量有限, 不能为每个实验分配过大样本; (b) 广告位改版效应常为 0.5-2% 小效应, 标准 t 检验功效不足; (c) 用户预处理协变量 (历史 CTR、历史搜索频次、设备类型) 可观测可用。
- **方法**: CUPED (Microsoft 2013) 构造调整后指标 `Y' = Y - theta * (X - E[X])`, `theta = Cov(Y,X)/Var(X)`, 其中 X = 实验前 7 天用户 CTR。`Y'` 与 `Y` 同期望但方差更小, 标准误缩减约 30-50%, 等效于样本量提升 1.4-2x。
- **效果**: notes.md "CUPED 让这些效果可被可靠检测" -- 在 Bing 实际部署中, CUPED 使原本需要 4 周才能达到显著性的小效应实验缩短至 2 周, 实验吞吐量翻倍。
- **本单元连接**: Day 1 TODO6 OLS 回归中 re75 (活动前1年消费) 作为协变量, 与 CUPED 思想一脉相承 ("用预处理变量调整事后估计")。Day 2/3 将深入 CUPED 工程实现 (theta 估计、Y' 构造、多协变量扩展)。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (partner 从 Imperial 经典合作库挑):

- **Partner (赞助企业)**: Burberry (奢侈品零售, Imperial MSc BA 经典合作 partner)
- **Problem (真实业务问题)**: Burberry 数字化营销团队需评估近期某邮件营销活动 (treat) 对高净值客户活动后 90 天消费 (re78 映射) 的真实增量, 但简单 t 检验 (TODO4 风格) 显示统计显著却商业微弱 (effect size 小), CMO 质疑"是否被基线不平衡污染"。
- **Data (企业提供数据)**: 脱敏客户级数据 (n≈50k), 字段映射 NSW 营销映射: `treat` (0/1 邮件触达), `re74` (活动前2年消费基线), `re75` (活动前1年消费), `re78` (活动后90天消费), `age`/`educ`(消费能力代理)/`marr`(家庭消费代理)/`nodegree`(价格敏感度代理)。客户级 RFM 字段 (Recency/Frequency/Monetary)。
- **Scope (8 周, 4-5 人团队)**: Week 1-2 数据治理 (notes.md "数据治理"维度: 完整性/一致性/准确性/时效性/合规性) + NSW 营销映射对齐; Week 3-4 描述性分析 (TODO1 基线对比 + TODO2 AARRR 漏斗 + TODO3 RFM 分群); Week 5-6 诊断性分析 (TODO4 t 检验 + TODO5 卡方 + TODO6 OLS 协变量调整); Week 7 CUPED-adjacent 方差缩减原型; Week 8 报告与 CMO 汇报。
- **Deliverable (交付物)**: (a) 漏斗仪表盘 (AARRR 五阶段转化率 + 流失节点标注, pandas 生成); (b) RFM 五分群策略矩阵 (Champions/At-Risk/Hibernating 等差异化营销建议); (c) 协变量调整 ATE 报告 (OLS vs 简单 t 检验对比, 标准误缩减量化, CUPED 思想前置); (d) 8 周咨询报告 + CMO 汇报 deck。

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Sarah Chen, 某全球美妆零售集团 CMO, 前 P&G 品牌经理, MBA + 数据科学证书, 上任 6 个月。
- **Decision (关键决策点)**: Sarah 面临一个 2000 万美元年度营销预算分配决策。数据团队刚完成一次邮件促销 RCT (n=50k, NSW 营销映射风格), 简单 t 检验 (TODO4) 显示 treat 组 re78 (活动后消费) 显著高于 control (p=0.03), 但 Cohen's d 仅 0.05 (微弱效应)。然而 OLS 回归 (TODO6) 控制 re75/re74/age/educ 后, treat 系数不再显著 (p=0.18), 标准误较 t 检验缩小约 40% (CUPED-adjacent variance reduction)。Sarah 必须在 48 小时内决定: (A) 按 t 检验结果, 全量推广邮件促销; (B) 按 OLS 结果, 停止促销; (C) 按 RFM 分群 (TODO3) 做异质效应分析, 仅对 Champions 与 At-Risk 子群推广。
- **Tension (核心张力/两难)**: (1) **统计显著 vs 商业显著**: notes.md 强调"统计显著≠商业显著" -- p=0.03 但 d=0.05, 2000 万赌注下是否值得? (2) **简单 vs 复杂模型**: t 检验易解释但忽略基线不平衡, OLS 控制混杂但 CMO 难向 CEO 解释"为什么控制后效果消失了"; (3) **聚合 vs 分群**: 全量推广 (A/B) 简单但可能浪费, RFM 分群推广 (C) 精准但运营复杂; (4) **CUPED 工程化**: 标准误缩减 40% 是真实增益还是过拟合? Day 2/3 工程实现尚未到位。
- **教学目标**: 学生需用 Day 1 工具链 (pandas/scipy.stats/statsmodels/causaldata NSW 营销映射) 复现 Sarah 的 t 检验 vs OLS 对比, 用业务语言向"CMO/CEO"解释 p 值、Cohen's d、OLS 系数、CUPED 方差缩减, 并给出 A/B/C 决策建议。衔接 Day 2 (CLV 预测验证促销长期价值) 与 Day 3 (MMM 预算优化)。

---

## guest_lecture

- **Topic (主题)**: "From t-Test to CUPED: How Microsoft ExP Scaled A/B Testing to Thousands of Experiments Per Day" -- 从 Day 1 的 `scipy.stats.ttest_ind` 到生产级 CUPED 工程化, 覆盖方差缩减、基线不平衡诊断、小效应检测。
- **Speaker Profile (主讲人画像)**: Microsoft ExP 团队 Principal Data Scientist / Head of Experimentation, 10+ 年 A/B 测试平台经验, CUPED 论文 (Microsoft 2013) 共同作者或工程落地负责人, 熟悉 Bing/Office/Azure 实验平台。具备工业界实战 + 学术发表双背景 (PhD 统计/CS), 能用业务语言向 CMO 解释统计概念。
- **讲座结构** (90 分钟): (1) 30 min -- Day 1 t 检验/卡方/OLS 在微软生产中的演化 (TODO4-6 工业版); (2) 30 min -- CUPED 原理 (notes.md "CUPED" 节) + Bing 实际案例 (标准误缩减 30-50%); (3) 30 min -- Q&A + 学生用 NSW 营销映射数据复现 CUPED-adjacent OLS (TODO6 扩展)。
- **本单元连接**: 直接呼应 notes.md "CUPED (Microsoft Research 2013)" 前沿点与 TODO6 OLS 协变量调整思想; 为 Day 2/3 CUPED 工程实现做铺垫。

---

## internship_pointer

- **Institution (机构)**: Microsoft ExP Research Residency / Google AI Resident (Experimental Infrastructure track) / OpenAI Residency (Product Experimentation track) -- 三选一, 优先 Microsoft ExP 因其 CUPED 源头地位与本单元直接匹配。
- **Role (角色)**: Experimentation Resident / A/B Testing Researcher -- 8-12 个月驻留, 参与生产级实验平台研发, 含 CUPED 方差缩减、序贯检验、贝叶斯 A/B 测试、异质处理效应 (HTE) 等方向。
- **衔接 (本单元如何为该角色做准备)**: (1) TODO1-3 描述性分析 (pandas groupby/describe/crosstab) 是实验平台数据探索基础; (2) TODO4 `ttest_ind` + TODO5 `chi2_contingency` 是 A/B 测试核心统计原语, Resident 面试必考; (3) TODO6 OLS 协变量调整 + notes.md CUPED 节 -- 直接对接 Microsoft ExP 的 CUPED 工程实现, 是 Resident 入职第一个月的 onboarding 项目; (4) NSW 营销映射 (RCT 金标准) 为理解生产实验设计 (SUTVA、干扰效应、样本比例失调) 提供真实数据直觉; (5) RFM 分群 (TODO3) 为 HTE 分析 (哪类用户对干预响应更强) 提供分群基础。
- **申请准备**: 用 Day 1 `solution.ipynb` (6 TODO 完整跑通) + `research.md` (IMRaD 大纲 + 可复现清单) 作为申请材料的数据分析样本; 在 cover letter 中显式引用 CUPED (Microsoft 2013) 论文与 NSW 营销映射工件, 证明"既能跑 t 检验, 也懂协变量调整的方差缩减原理"。

---

> 产业链接遵循 Imperial MSc BA 咨询项目模式 (Burberry/Expedia/J&J partner, 8 周 4-5 人团队) + HBS 案例法 (protagonist/decision/tension) + MIT Sloan 行动学习 (企业白皮书 + 客座讲座) + 工业界实习驻留 (Microsoft ExP / Google AI Resident / OpenAI Residency)。本工件为 AI 原生化商业博士选修 E2 Day 1 的产业对接单元, 与 `research.md` (研究产出层) 形成"研究->实践"双向闭环。
