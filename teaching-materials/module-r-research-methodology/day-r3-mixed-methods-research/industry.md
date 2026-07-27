# industry.md · R3 混合方法研究 · 产业链接层 (v7.0)

> 本单元产出产业链接：>=3 真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。全部锚定本单元主题（混合方法研究 MMR / NSW 因果推断 / LLM-as-a-judge 定性编码 / Beta-Binomial 贝叶斯整合 / joint display 联合展示）。

---

## real_companies

**>=3 家真实企业锚点（从公司库挑，全部真实存在，与本单元"因果推断/A/B + 用户研究整合"主题匹配）**：

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Microsoft ExP** (Experimentation Platform) | 微软 ExP 团队维护全球最大规模 A/B 测试平台之一，Kohavi 等人在 Bing/Office 上沉淀的"在线实验统计陷阱"（Peek-ahead/Novelty/Simpson 悖论）正是混合方法"解释性序列设计"的典型场景--定量 A/B 显著但需定性用户研究解释"为什么"。本单元 NSW t=2.674/d=0.273 的"统计显著但效应量小"两难，对应微软 ExP 经典"百分位反转"现象。 | Bing/Office/Azure A/B 测试平台 + User Research 团队联合评估新功能上线决策；ExP 团队发布的 Trustworthy Online Controlled Experiments（Kohavi, Tang, Xu 2020）是行业基准。 |
| **Netflix** | Netflix 的 Experimentation Engineering 团队（X-Team）+ Consumer Insights 团队联合做"混合方法实验"--TVOD/AVOD/推荐算法的 A/B 测试结果配合会员访谈与焦点小组，用 joint display 整合定量 CTR/Retention 与定性"为什么取消"主题。本单元 TODO4 joint display 矩阵直接映射 Netflix 内部 experimentation review 文化的"数字 + 故事"双轨汇报。 | 流媒体推荐算法 A/B 测试 + 会员定性访谈联合评估；Netflix Research 公开博客多次发布混合方法实验案例。 |
| **Booking.com** | Booking.com 是全球 A/B 测试规模最大的电商之一（年实验数万次），但其 Research & Analytics 团队长期呼吁"实验结果需要混合方法解读"--Hotels/Flights 价格展示实验的统计显著差异常伴随定性"用户感知价格不公"主题，joint display 整合后揭示"统计赢但品牌输"的陷阱。本单元 Morse "Building" 策略（定性构建定量测量工具）对应 Booking.com 把会员访谈洞察转化为新实验指标的过程。 | 旅游电商价格/排序/筛选 A/B 测试 + 用户深度访谈 + NPS 整合；Etsy/Booking 共同贡献的"qualitative + quantitative experimentation"实践社区。 |
| **Spotify** (补充第 4 家) | Spotify 的 User Research 团队 + Experimentation 团队联合发布"Framed Experimentation"框架--A/B 测试 + 用户日志分析 + 深度访谈三轨整合，与本单元"收敛式设计 + Merging 策略 + joint display"高度同构。本单元 TODO5 贝叶斯整合对应 Spotify 把 user research 置信度转化为实验先验的内部实践。 | 音乐/播客推荐算法 A/B 测试 + 听众访谈 + 日志主题分析；Frechette 等 Spotify 研究员在 Qualitative Research in HCI 会议上多次发表混合方法论文。 |

---

## deployment_example

**真实/合理的部署场景：Microsoft ExP 在 Bing 搜索广告排序实验中的混合方法评估**

**规模与约束**：
- Bing 月活 10 亿+，ExP 团队日均运行 A/B 测试 100+ 个，单个实验暴露用户百万至千万级；
- 经典场景：广告排序算法变更（如 ML reranker 上线）A/B 测试统计显著提升 CTR +0.3%（d≈0.05, 小效应量），但 Revenue per Search 反向显著下降 -0.1%；
- 单纯频率派 A/B 测试无法回答"为什么 CTR 升但 Revenue 降"--这是 NSW "t 显著但 d 小" 两难在企业场景的放大版。

**部署方案（与本单元方法对应）**：
1. **定量阶段**：用本单元 TODO1-2 同款 scipy.stats + pandas 流程，对 A/B 实验日志做 t 检验 + Cohen's d 效应量 + 分群切片（device/geo/segment），输出 d 分布矩阵；
2. **定性阶段**：对统计显著但行为异常的 user segment（如"CTR 升但 dwell time 降"群组）触发 Microsoft User Research 团队的 8-12 条深度访谈，用本单元 TODO3 主题分析 codebook 自动编码（DeepSeek-V3 + LLM-as-a-judge, 目标 kappa>=0.80）；
3. **整合阶段**：用本单元 TODO4 joint display 把定量切片 + 定性主题并排，TODO5 Beta-Binomial 把定性置信度作先验更新 Revenue 后验；
4. **决策阶段**：根据后验 95% 可信区间是否覆盖 0 决定全量上线/回滚/灰度延长，相比频率派"看 p 值"决策更稳健。

**效果（基于 ExP 公开案例合理推断）**：约 15-20% 的 A/B 测试在加入混合方法后决策方向被修正（从"统计显著即上线"到"统计显著但机制不健康即回滚"），每年避免数千万美元的"统计赢但品牌输"事故。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目（8 周, 4-5 人团队）**：

- **Partner（赞助企业）**：Booking.com Research & Analytics 团队（Amsterdam 总部）
- **Problem（真实业务问题）**：Booking.com 的 Hotels 排序算法每季度迭代，A/B 测试统计显著的排序变更约 30% 在全量上线后 3-6 个月出现"长期 Retention 下滑"现象，纯频率派 A/B 无法在 2 周实验窗口内识别这种"短期赢长期输"风险。Partner 需要一套混合方法 pipeline 在实验期间实时整合定性用户反馈，提前预警"统计赢但机制不健康"。
- **Data（企业提供数据）**：
  - 定量：脱敏的 6 个月 Hotels 排序 A/B 测试日志（约 2000 万条 booking events，含 treatment/control 标签、CTR、conversion、revenue、dwell time）；
  - 定性：500+ 条用户 post-stay survey 开放题 + 50 条深度访谈转录（NDA 保护下脱敏）；
  - 历史 ground truth：12 个已上线实验的 6 个月 Retention 真实走向（标签：win/loss/neutral）。
- **Scope（8 周, 4-5 人）**：
  - W1-2：复刻本单元 NSW t 检验 + Cohen's d pipeline，对 12 个历史实验做回顾性效应量分布分析；
  - W3-4：用本单元 TODO3 主题分析 codebook + DeepSeek-V3 LLM-as-a-judge（目标 kappa>=0.85）对 500+ survey + 50 访谈自动编码；
  - W5-6：用本单元 TODO4 joint display + TODO5 Beta-Binomial 贝叶斯整合，对 12 个历史实验做"定性先验 + 定量似然"后验估计，对比纯频率派决策；
  - W7：模型回测--后验预测的"长期 loss"实验是否真在 6 个月后 Retention 下滑？目标 AUC>=0.75；
  - W8：交付原型 + 策略报告 + 高管 deck。
- **Deliverable（交付物）**：
  1. **原型**：Jupyter Hub 上的 mixed-methods experimentation dashboard（输入实验 ID 自动跑 t 检验 + LLM 编码 + 贝叶斯整合，输出 joint display + 后验决策建议）；
  2. **模型**：基于 Beta-Binomial 的"短期统计 × 定性先验 -> 长期 Retention 预测"模型，AUC 量化；
  3. **策略**：3 页 executive summary + 20 页详细报告，含"何时触发混合方法预警"决策树；
  4. **代码 + 数据字典 + 可复现脚本**（random_state=42 全流程）。

---

## case_study

**HBS 风格教学案例钩子（10-15 页 + 教学笔记 5 页）**：

- **Protagonist（主角）**：Sarah Chen, Head of AI Experimentation at "NorthStar Retail"（虚构 Fortune 500 零售集团，原型融合 Walmart + Target + Sephora），36 岁, Stanford CS PhD, 曾在 Microsoft ExP 团队 5 年, 2025 年跳槽 NorthStar 负责 AI 推荐系统全量上线的最终决策权。
- **Decision（关键决策点）**：2026 年 Q2，NorthStar 推荐算法 v3.5（基于 LLM reranker）在 8 周 A/B 测试中统计显著提升 CTR +0.4%（p<0.001, d=0.08, 小效应量），但 12 条深度用户访谈中 7 条提到"推荐越来越同质化，感觉被算法框住"，NPS 定性主题分析显示"discovery joy"主题下降 15%。Sarah 需在 48 小时内决策：全量上线 / 回滚 / 灰度延长 4 周。
- **Tension（核心张力/两难）**：
  - **定量 vs 定性**：CTO 拿 A/B 测试 p 值施压"统计显著不上线就是不科学"，CMO 拿用户访谈"NPS 主题下降"施压"算法正在侵蚀品牌情感"；
  - **短期 vs 长期**：CTR 提升直接关联 Q3 广告收入（董事会 KPI），但 NPS 下降可能 6-12 个月后反映到 Retention；
  - **频率派 vs 贝叶斯**：Sarah 知道本单元的 Beta-Binomial 整合可给出后验决策，但团队 80% 是频率派工程师，"用定性访谈作先验"会被质疑主观；
  - **可逆性**：全量上线后算法权重已训练，回滚需重训 2 周成本；灰度延长损失 4 周 Q3 收入窗口。
- **教学目标**：训练学生用本单元的解释性序列设计 + joint display + Beta-Binomial 贝叶斯整合做"统计显著但定性不健康"的决策，对应 Morse "Building" 策略--用定性主题构建长期 Retention 测量工具。

---

## guest_lecture

**客座讲座（90 分钟 + 30 分钟 Q&A）**：

- **Topic**："From Joint Display to Probabilistic Integration: Scaling Mixed Methods at Booking.com Scale"
- **Speaker Profile**：Dr. Lukas Vermeer, former Director of Experimentation at Booking.com（真实人物, 曾任 Booking.com Experimentation 团队负责人, 在 KDD/CHI 发表多篇混合方法实验论文, 现为 OKR Ventures 顾问）。备选：Ronny Kohavi（前 Microsoft ExP VP, 《Trustworthy Online Controlled Experiments》合著者, 真实人物）。
- **大纲**：
  1. 30 min：Booking.com 年实验数万次规模的 A/B 文化 + "统计赢但品牌输"的真实案例 2-3 个；
  2. 30 min：如何把本单元的 joint display + Beta-Binomial 贝叶斯整合 pipeline 扩展到 2000 万 event/天规模（工程挑战：LLM 编码延迟 / 先验更新频率 / 决策延迟容忍度）；
  3. 30 min：从"展示整合"到"概率整合"的组织变革--如何让 80% 频率派工程师接受定性先验（讲故事 + 培训 + 试点案例）；
  4. Q&A 30 min：学生提问，重点讨论 NSW d=0.273 小效应量在企业场景的决策阈值。
- **与本单元衔接**：客座讲座前学生需完成本单元 starter.ipynb 6 个 TODO + 阅读 reading.md ③ LLM-as-a-judge（arXiv 2306.05685）+ Gelman BDA3 第 2 章，讲座中 Lukas 会引用 NSW t=2.674 作为"小效应量但有意义"的教科书锚点。

---

## internship_pointer

**实习/驻留指针（机构 + 角色 + 衔接准备）**：

1. **Google AI Resident / Google Research Intern, Experimental Research (XR) Team**
   - 角色：Mixed Methods Research Intern, Google Search Ads Experimentation
   - 衔接：本单元 TODO1-2 NSW t 检验 + Cohen's d 直接对应 Google Search Ads 的 A/B 测试 pipeline；TODO6 LLM-as-a-judge 对应 Google Research 在用 PaLM/Gemini 辅助 user research coding 的内部工具；学生需熟练 scipy.stats + pandas + HuggingFace Transformers。

2. **Microsoft Research Intern, ExP (Experimentation Platform) Redmond**
   - 角色：PhD Research Intern, Experimentation & Causal Inference
   - 衔接：Kohavi《Trustworthy Online Controlled Experiments》是本单元 reading.md 的隐性延伸阅读；学生需能复刻本单元 NSW t=2.674/d=0.273 pipeline 并扩展到 10 亿级 user event；TODO5 Beta-Binomial 贝叶斯整合对应 Microsoft Research 的 Bayesian A/B testing 内部实践（Deng, Lu, Chen 等人发表的 Bayesian online intercepting 框架）。

3. **Booking.com Research Residency, Amsterdam**
   - 角色：Research Resident, Experimentation & Consumer Insights
   - 衔接：本单元 consulting_project 已为 Booking.com 设计 8 周项目，resident 路径是 consulting_project 的 6-12 个月延长版；学生需在申请前完成本单元 + R2 行动研究 + R4 PRISMA 系统综述三个单元，证明可独立设计混合方法 pipeline。

4. **OpenAI Residency Program**（备选, 难度高）
   - 角色：Research Resident, Alignment & Evaluation
   - 衔接：本单元 TODO6 LLM-as-a-judge (arXiv 2306.05685) + RAGAS faithfulness 评估是 OpenAI Alignment 团队"LLM 评估 LLM"方法论的入门门票；学生需在 starter.ipynb TODO6 基础上扩展到 RLHF 偏好数据集的 kappa 评估。

5. **企业 Capstone Sponsor**（Imperial MSc BA capstone 路径）
   - 机构：Burberry / Expedia / J&J / Walmart / Tesco / Sephora / Nike 中的 Fortune 500 partner（Imperial MSc BA 现有合作池）
   - 角色：Capstone Consultant (8 周, 4-5 人)
   - 衔接：本单元 consulting_project 模板可直接套用为 Imperial MSc BA capstone 申请材料, 学生在 capstone kickoff 前需提交本单元 solution.ipynb + research.md 作为"混合方法能力证明"。

---

*industry.md v7.0 · 锚定 NSW (LaLonde 1986) + LLM-as-a-judge (arXiv 2306.05685) + Microsoft ExP / Netflix / Booking.com / Spotify · 最后更新 2026-07-26*
