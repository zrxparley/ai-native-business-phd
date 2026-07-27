# industry.md · 产业链接层 (v7.0)

> 本单元 (技能3 · Day 2: A/B 测试统计 · NSW 做 RCT 视角 A/B + CUPED) 的产业链接。本文件遵循 Imperial MSc Business Analytics 咨询项目模式 + HBS 案例法 + MIT Sloan 行动学习模式, 把"教学上机"升级为"产业可接入的实践工件"。

---

## real_companies

>=3 真实企业锚点 (从公司库挑, 全部真实存在, 与 A/B 测试 / CUPED 主题匹配):

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Microsoft ExP** (Experimentation Platform) | CUPED 共同作者 Kohavi 是微软 A/B 体系奠基人; 本单元 CUPED 公式与方差缩减 1-ρ² 直接来自微软实践 | Bing / Office / Azure 每日跑数千个在线对照实验, CUPED 是其标准方差缩减技术, 用实验前查询/点击协变量缩减结果方差, 相同样本量检测更小效应 |
| **Netflix** | A/B 测试工业标准实践者; CUPED 工业变体 (CUPAC, ML-based variance reduction) 公开技术博客 | 流媒体推荐算法 / UI 改版 A/B 测试, 用实验前观看时长 / 活跃度作 CUPED 协变量; 在 retention / streaming quality 指标上做方差缩减, 缩短实验周期 |
| **Uber** | 大规模 A/B 测试 + CUPED 实践者; 技术博客公开 variance reduction 方法 | 司机端 / 乘客端产品实验, 用实验前订单量 / 完成率作 CUPED 协变量, 在 surge pricing / 派单算法改动上提升检测灵敏度 |
| **Booking.com** | 在线对照实验工业标杆, Kohavi 著作引用案例 | 房源排序 / 价格展示 A/B 测试, 用历史预订 / 浏览行为协变量缩减转化率指标方差 |
| **Amazon** | 大规模 A/B 实验平台 + CUPED 实践者 | 商品详情页 / 推荐栏位 A/B 测试, 用实验前购买 / 加购行为作 CUPED 协变量, 检测微小 CVR 提升 |

---

## deployment_example

**部署场景: Microsoft ExP 在 Bing 搜索结果页 A/B 测试中部署 CUPED**

- **规模**: Bing 每日数千个在线对照实验, 单实验覆盖百万至千万级用户查询; 实验平台 (ExP) 自动为每个实验计算 CUPED 调整后的指标与原始指标并列报表。
- **协变量**: 用户实验前 4 周的查询频次 / 点击率 / 会话时长 (pre-experiment data, 不受当前处理影响), 与实验期 Y (CTR / Dwell time / Revenue) 高度相关, $\rho \approx 0.3-0.6$, 故理论方差缩减 $1-\rho^2 \approx 9\%-36\%$。
- **约束**: (1) 协变量必须在处理分配前已观测 (避免信息泄漏); (2) 新用户无 pre-experiment 数据, CUPED 退化为原始均值差 (需分层报告); (3) 多重检验场景需对 CUPED 调整后的 p 值做 FDR 控制。
- **效果**: CUPED 使相同 MDE 所需样本量减少约 20-40% (Kohavi et al. 2020), 等价于实验周期从 14 天缩至 8-11 天, 直接节省实验流量机会成本。
- **本单元迁移**: NSW 场景中 `re75` (实验前 1975 收入) -> `re78` (实验后 1978 收入) 的 CUPED 调整, 与 Bing 场景结构同构 -- 协变量"实验前已观测 + 与 Y 相关 + 不受 T 影响"的三条件均成立。营销场景迁移: 实验前 4 周活跃度 -> 实验期转化率。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (8 周, 4-5 人团队):

- **Partner (赞助企业)**: Booking.com (在线旅游 A/B 测试工业标杆, 阿姆斯特丹总部)
- **Problem (真实业务问题)**: Booking.com 的房源排序算法改版 A/B 测试中, "预订转化率"指标方差大 (低基线, 5%-8%), 导致真实有效但微小的 +0.5% CVR 提升被噪声淹没, 实验周期长达 21 天才能达到 power=0.80, 严重影响迭代速度。Partner 希望量化评估 CUPED + 其工业变体 (CUPAC, ML-based) 能否将周期缩至 12 天以内。
- **Data (企业提供)**: (1) 脱敏的 1000 万用户级实验日志, 含处理分配 / 实验期预订 / 实验前 8 周浏览与预订行为; (2) 历史已结案 A/B 测试 50 个, 含原始指标与 ground-truth 决策 (ship / no-ship); (3) 协变量目录 (用户层级 / 会话层级 / 设备层级)。
- **Scope (8 周 4-5 人)**:
  - W1-W2: 复现 NSW CUPED baseline (本单元 solution.ipynb) 作为方法论校准; 文献综述 (Deng 2013 / Kohavi 2020 / Netflix CUPAC 博客)。
  - W3-W4: 在 5 个历史已结案 A/B 上回测 CUPED vs 原始, 量化方差缩减比例 vs $1-\rho^2$; 评估协变量选择对增益的敏感性。
  - W5-W6: 设计 ML-based variance reduction (CUPAC) 原型, 用实验前协变量预测 Y, 取残差作调整后指标; 对比 CUPED vs CUPAC 增益。
  - W7-W8: 在 1 个 live A/B 上验证 (前 7 天数据); 撰写 final report + executive deck + 代码仓库。
- **Deliverable (交付物)**:
  1. 可复现 Jupyter notebook (CUPED + CUPAC 原型, 命中本单元 reproducibility_checklist 8 项);
  2. 50 个历史 A/B 的回测报告 (方差缩减比例 / 功效提升 / 假阴性减少数);
  3. Executive deck 给 Booking.com VP of Experimentation;
  4. 策略建议: 何时用 CUPED vs CUPAC vs 原始 (decision tree by sample size / baseline rate / $\rho$)。

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Maria Chen, 38 岁, 中型电商 (年 GMV $500M) 新任 Head of Experimentation, 前 Netflix Senior Data Scientist, 上任第 90 天。
- **Decision (关键决策点)**: 大促前 6 周, Maria 面临决策: 是否在下一次首页推荐算法 A/B 中强制引入 CUPED 调整, 要求产品团队为每个实验预收集"实验前 4 周用户活跃度"协变量。这会增加 2 天数据准备周期, 但据她在 Netflix 的经验可使样本量节省 30%。
- **Tension (核心张力)**:
  - **数据团队 vs 业务团队**: 数据团队支持 CUPED (方法严谨, 功效提升); 业务团队反对 (额外协变量收集延迟大促, 机会成本高, 且业务团队不理解"为什么不能直接跑")。
  - **短期 vs 长期**: 短期 2 天延迟可能错过大促窗口; 长期 CUPED 标准化可使全年实验数翻倍。
  - **方法论纯粹 vs 实用主义**: Maria 知道 CUPED 在 NSW 小样本 (N≈700) 上增益有限, 在 Booking/Netflix 大规模场景才显著; 公司规模介于两者之间, 增益不确定。
  - **信任资本**: Maria 上任 90 天, 尚未建立足够信任推动方法论改革; 强推 CUPED 可能被视为"过度工程化"。
- **教学钩子**: 案例在 Maria 决定是否发邮件给 CMO 推迟大促 A/B 时切断, 学员需代入 Maria 决策, 结合本单元 CUPED 理论 (方差缩减 $1-\rho^2$) + NSW 实证证据 + 组织变革管理, 给出 go/no-go 建议。配套 teaching note 引用 Kohavi et al. 2020 Ch.1-3 + Deng 2013。

---

## guest_lecture

**客座讲座**:

- **Topic (主题)**: "From NSW to Bing: CUPED at Industrial Scale -- How Pre-Experiment Data Halves Your A/B Sample Size"
- **Speaker Profile (主讲人画像)**: Dr. Ron Kohavi (前 Microsoft Distinguished Engineer / Bing Experimentation Lead, 《Trustworthy Online Controlled Experiments》合著者, CUPED 工业推广奠基人); 备选: Alex Deng (Microsoft ExP, CUPED 原论文一作) 或 Netflix Experimentation 团队 Tech Lead。
- **形式**: 60 分钟讲座 + 30 分钟 Q&A, 远程视频。
- **内容锚点**:
  1. CUPED 数学基础 (本单元 NSW 场景的 $1-\rho^2$ 公式);
  2. 微软 Bing 部署案例 (本 deployment_example 场景的扩展);
  3. 工业变体: CUPAC (ML-based), stratified CUPED, ratio metrics;
  4. 何时**不要**用 CUPED (协变量受处理影响 / 新用户无 pre-data / 极小样本);
  5. Q&A 聚焦本单元学员的营销迁移问题 (历史消费作协变量的边界条件)。

---

## internship_pointer

**实习 / 驻留指针**:

- **机构 (Institution)**:
  1. **Microsoft ExP Internship** (Bing / Office / Azure Experimentation Platform, Redmond) -- 直接对接 CUPED 原作团队;
  2. **Netflix Experimentation Internship** (Los Gatos, CA, 或远程) -- 推荐 / 流媒体 A/B 平台, CUPAC 工业变体;
  3. **Google AI Resident** (Mountain View, CA) -- 通用 AI 驻留, 可选 experimentation 方向;
  4. **Booking.com Data Science Internship** (Amsterdam) -- 在线对照实验工业标杆;
  5. **Uber Experimentation Internship** (San Francisco) -- 双边市场 A/B + CUPED。
- **角色 (Role)**: Applied Scientist Intern / Experimentation Analyst Intern / Data Science Intern (12 周 summer internship 或 6 个月 co-op)。
- **衔接 (Bridge)**: 本单元如何为该角色做准备:
  1. **理论锚点**: NSW RCT 视角让学员掌握"均值差 = ATE"的识别条件, 这是工业 A/B 平台统计底座的入门门槛;
  2. **CUPED 上机**: solution.ipynb TODO6 的 CUPED 实现 (从公式到代码) 是面试常考点, 直接对应 Microsoft ExP / Netflix 的 take-home assignment;
  3. **可复现研究**: research.md 的 NeurIPS 风格 checklist 训练学员的"研究工件交付"习惯, 这是 internship 转正 return offer 的关键区分点;
  4. **产业语言**: industry.md 的 5 家企业锚点 + deployment_example 让学员在面试中能用对方术语 (CUPAC / pre-experiment data / variance reduction ratio) 沟通;
  5. **咨询项目**: consulting_project 的 Booking.com 8 周项目模板, 可直接转化为 internship 的 capstone 项目提案。

---

*本文件遵循 Imperial MSc Business Analytics 咨询项目模式 (Burberry / Expedia / J&J partner 案例) + HBS 案例法 (protagonist + decision + tension) + MIT Sloan 行动学习模式。*
*最后更新: 2026-07-26 (v7.0 产业链接层追加)*
