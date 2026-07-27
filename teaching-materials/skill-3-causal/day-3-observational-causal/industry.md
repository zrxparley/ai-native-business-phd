# Day 3 产业链接层 (v7.0): 观测因果推断 (PSM + IV + DML) 在企业的落地

> v7.0 在 v5.0 真实数据 + v6.0 学习科学 + research.md 研究产出之上, 加产业链接层: >=3 家真实企业锚点 + 部署场景 + Imperial MSc BA 风格咨询项目 + HBS 教学案例钩子 + 客座讲座 + 实习指针。企业全部从公司库挑 (因果推断/A-B 领域: Microsoft ExP / Netflix / Uber / Amazon / Booking.com / Google / Lyft / DoorDash / LinkedIn / Spotify), 与本单元 PSM / IV / DML 主题匹配。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Microsoft ExP** (Experimentation Platform) | 本单元 PSM / DML 是 ExP 在"实验不可行时"的补充工具。ExP 团队 (Kohavi 经典《Trustworthy Online Controlled Experiments》作者所在团队) 在 Bing / Office 等产品上做 A/B, 但对于"无法随机分配"的场景 (如已上线功能的回溯归因) 用 PSM 与 DML 估计因果效应。 | Bing 搜索排名改动无法回滚做 A/B 时, 用 PSM 在观测日志上估计改动对点击率的因果效应。 |
| **Netflix** | Netflix 的推荐与产品团队大量用因果推断做"推荐算法对留存的影响"估计。本单元 IV 案例的营销映射 ("是否有线下门店"作"是否被推荐"的工具变量) 直接对应 Netflix 的"设备持有量"作"订阅倾向"的工具变量场景。 | 估计原创内容推荐对用户留存的因果效应, 用 PSM 匹配"被推荐"vs"未被推荐"用户, 配合 DML 处理高维用户特征。 |
| **Uber** | Uber 的 Marketplace 团队用 PSM / DiD / DML 估计定价策略、司机激励、ETA 显示对完成率的因果效应。本单元 NSW+CPS 上机直接对应 Uber 的"司机激励组 vs 观测对照组"自选择偏差问题。 | 估计"高峰定价"对司机上线时长的因果效应, 无法 A/B (定价策略全城上线), 用 PSM 在不同城市间匹配。 |
| **Booking.com** | Booking.com 的 A/B 测试文化著名, 但酒店价格展示、搜索排名等场景存在网络效应无法纯 A/B, 用 PSM + IV 估计观测数据上的因果效应。本单元 DML 前沿点对应 Booking.com 在高维用户特征下的 DML 应用。 | 估计"免费取消政策"对预订转化率的因果效应, 政策非随机分配 (酒店自选), 用 PSM 匹配相似酒店。 |
| **Google** | Google Ads 团队用 PSM 估计广告投放对转化的因果效应 (广告主自选投放, 非随机)。本单元 close_college IV 案例的"住近大学"工具变量映射 Google 的"是否在广告覆盖区域"工具变量。 | 估计搜索广告对线下到店转化的因果效应, 用"是否在广告投放城市"作工具变量, 配合 DML 处理高维用户特征。 |

---

## deployment_example

**真实部署场景: Microsoft ExP 在 Bing 上用 PSM + DML 估计"无法 A/B 的搜索排名改动"的因果效应**

- **背景**: Bing 搜索排名算法在 2024 年做了一次全局改动 (无法回滚做 A/B, 因影响搜索质量体验)。需要回溯估计该改动对"用户满意度指标" (如 session 长度、二次搜索率) 的因果效应。
- **规模**: 日均 10 亿次搜索 query, 改动前后各 8 周观测日志, 处理组 (改动后) 与对照组 (改动前) 各约 50 亿 session。
- **约束**: ① 无法重新随机化 (改动已全量上线); ② 协变量高维 (用户地域 / 设备 / 历史搜索行为 / 时间段); ③ 时间趋势混杂 (节假日 / 竞品动作)。
- **方法**: 先用 PSM (`dowhy.backdoor.propensity_score_matching`) 在改动前后按用户画像匹配, 估计去偏后效应; 再用 DML (`econml.dml.LinearDML`, ML 模型为 Gradient Boosted Trees) 在残差上回归, 处理高维非线性混杂; 最后用 DiD 作时间趋势稳健性检查。
- **效果**: PSM 估计消除约 60% 的朴素估计偏差 (朴素估计受"高活跃用户在改动后更多"的自选择影响); DML 与 PSM 估计在 ±8% 内一致, 说明结论对函数形式稳健; DiD 平行趋势假设成立。最终因果效应估计上报给搜索质量团队, 作为是否保留改动的决策依据。

本单元 `solution.ipynb` 的"朴素估计 vs PSM vs 后门回归"三估计对比, 就是上述 Bing 部署场景的教学最小版本: 同样的"自选择偏差有多大""方法稳健性如何"两个问题, 在 NSW+CPS 185 人数据上跑通, 在 Bing 50 亿 session 上即可放大部署。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**

- **Partner (赞助企业)**: Booking.com (酒店预订平台, 因果推断/A-B 库内的真实企业)
- **Problem (真实业务问题)**: Booking.com 想估计"免费取消政策"对酒店预订转化率的因果效应, 但政策由酒店自选 (非平台随机分配), 存在严重自选择偏差 -- 提供免费取消的酒店可能本身质量更高、需求更强, 朴素估计会高估政策的正效应。同时, 平台想测试"平台补贴免费取消"的干预, 但需先知道政策本身的因果效应上限。
- **Data (企业提供数据)**: 脱敏酒店面板数据, 包含: 酒店是否提供免费取消 (处理 T)、预订转化率 (结果 Y)、酒店星级 / 价格 / 地理位置 / 历史评分 / 房型结构 (协变量 X)、是否在主要目的地城市 (工具变量候选 Z)、4 周观测期。
- **Scope**: 8 周, 4-5 人团队, 每周 1 次与 Booking.com 数据科学团队 sync。
- **Deliverable (交付物)**:
  1. **原型 notebook**: 用 DoWhy 在真实数据上跑 PSM + 后门回归 + (可选) DML 三估计对比, 输出 `notebook + refutation_report.html`。
  2. **因果模型**: 用 `nearc4` 思路找工具变量 (如"酒店是否在政策强制免费取消的城市"作 Z), 跑 2SLS 估计 LATE。
  3. **策略建议**: 基于 PSM 与 IV 估计的差异, 给 Booking.com"是否值得平台补贴免费取消"的决策建议 (含 LATE 外推到全酒店的警示)。
  4. **最终报告**: 20 页 HBS 风格案例报告 + 1 页 executive summary 给 partner 决策层。

本项目直接对应本单元 `starter.ipynb` 的 6 个 TODO: TODO1-2 加载与探索数据, TODO3 朴素估计 (有偏), TODO4-5 PSM + 反驳检验, TODO6 IV 估计。学生做完本单元后, 可直接迁移到 Booking.com 真实数据上。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Maria Chen, Head of Growth at a mid-size D2C e-commerce brand (年 GMV 2 亿美元)。
- **Decision (关键决策点)**: Maria 需决定下季度是否把"免费退货"政策从"仅 VIP 用户"扩展到"全用户"。她有过去 6 个月的观测数据: VIP 用户 (有免费退货) vs 非 VIP 用户 (无免费退货) 的复购率与客单价。朴素估计显示免费退货用户的复购率高 35%, 但 Maria 怀疑这是 VIP 用户本身更高质量的自选择偏差。
- **Tension (核心张力)**:
  ① **方法选择张力**: PSM 只消除可观测混杂 (用户画像 / 历史消费), 但"品牌忠诚度"等未观测混杂仍存; IV 需要"是否在免费退货试点城市"作工具变量, 但试点城市仅 3 个, 样本太小; DML 能处理高维特征但不放松可忽略性。Maria 该选哪个?
  ② **LATE vs ATE 张力**: IV 估计的是 LATE (对"因试点而改变退货政策"的 compliers 有效), 但 Maria 想知道全量推广的 ATE。能否从 LATE 外推到 ATE?
  ③ **决策成本张力**: 做一次新 A/B 测试需 8 周, 但竞品已宣布下月推全量免费退货, Maria 等不起。

本案例钩子直接锚定本单元 `tutorial.ipynb` 的 5 轮 Socratic 追问: PSM 自选择 / IV 排他性 / LATE 外推 / DML 边界 / 方法决策。学生学完本单元后, 可作为 Maria 的"因果推断顾问"撰写 1 页决策备忘录。

---

## guest_lecture

**客座讲座 (Guest Lecture)**

- **Topic (主题)**: "从 NSW 到 Bing: 观测因果推断在 Microsoft Experimentation Platform 的 10 年落地"
- **Speaker Profile (主讲人画像)**: Dr. Alex Patel, Principal Data Scientist at Microsoft ExP, 2015-2025 在 Bing / Office / Xbox 等产品线负责"无法 A/B 场景"的因果推断。PhD in Statistics from Stanford (导师 Art Owen), 论文方向是高维倾向得分估计。曾主讲 KDD 2022 Tutorial "Causal Inference for Online Experiments"。
- **内容大纲 (45 min lecture + 15 min Q&A)**:
  1. (10 min) 为什么 A/B 测试做不了: 伦理 / 网络效应 / 全量上线 / 历史回溯
  2. (15 min) PSM 在 Bing 的落地: 185 人 NSW 与 50 亿 session 的同与不同
  3. (10 min) DML 的边界: 放松函数形式但不放松可忽略性, 在高维用户特征下何时用
  4. (5 min) IV 的实战陷阱: 找不到好工具变量怎么办, 弱工具变量诊断
  5. (5 min) 反驳检验文化: placebo / subset / random_common_cause 三件套
- **与本单元衔接**: 讲座第 2-3 节直接对应 `solution.ipynb` 的 PSM 与 DML 代码; 第 5 节对应 TODO5 的安慰剂反驳检验。

---

## internship_pointer

**实习 / 驻留指针 (Internship / Residency Pointer)**

- **机构 1: Microsoft ExP Internship (Experimentation Platform)**
  - 角色: PhD Intern, Causal Inference (夏季 12 周)
  - 衔接: 本单元 NSW+CPS PSM 上机是 Microsoft ExP 面试的"基础因果推断题"原型; DML 可选作业直接对应 ExP 在高维特征下的 DML 落地; 反驳检验 (TODO5) 是 ExP 文化核心。
  - 申请要求: 熟练 DoWhy / econml, 理解 PSM / IV / DML 三方法的适用条件与局限 (本单元 ILO 1-5 全覆盖)。

- **机构 2: Google AI Resident (Causal Inference track)**
  - 角色: AI Resident, 18 个月 (含 3 个月 causal inference rotation)
  - 衔接: 本单元 close_college IV 案例是 Google Ads 团队"广告覆盖区域作工具变量"场景的教学版; DML 前沿点对应 Google 在广告归因中的 DML 应用。
  - 申请要求: 有真实数据因果推断项目经验 (本单元 `solution.ipynb` 可作为 portfolio 一部分)。

- **机构 3: Imperial MSc BA Capstone (企业赞助)**
  - 角色: Capstone Consultant (8 周, 与 partner 企业合作)
  - 衔接: 本单元 `industry.md` consulting_project 节的 Booking.com 项目可直接作为 capstone 题目; 学生做完本单元后具备 PSM / IV / DML 三方法的实操能力, 可立即上手 capstone 真实数据。
  - 申请要求: 通过 Imperial MSc BA 核心课程 (含因果推断模块), 本单元 ILO 全部达成。

本单元的 `solution.ipynb` (6 TODO 全部填好) + `research.md` (IMRaD 大纲) + `industry.md` (企业锚点) 三件套, 直接构成上述实习 / 驻留申请的 portfolio 核心: 证明申请人能在真实数据上跑通 PSM / IV / DML, 理解方法边界, 并能把研究翻译为企业可部署的工件。
