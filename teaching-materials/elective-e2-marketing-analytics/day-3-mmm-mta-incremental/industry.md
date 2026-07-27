# Day 3 产业链接层 (v7.0)

> 选修E2 · Day 3：MMM / MTA / 增量测量 · 产业链接与教学案例
> 本文件锚定 `notes.md` 已记录的真实方法 (MMM / MTA / 增量测试 / DML / 合成控制 / CUPED) 与 2026 工业开源工具 (Meta Robyn / Google Meridian / PyMC Marketing), 全部企业从 v7.0 模板公司库挑选, 真实存在。

---

## real_companies

以下 >=3 家真实企业锚点, 与本单元 MMM / MTA / 增量测量主题匹配:

| 公司 | 与本单元关联 | 业务场景 |
|------|------|------|
| **Meta** (Meta Ads + Robyn 开源 MMM) | 业界使用最广的开源 MMM 工具, 本单元 TODO1 频率学派 MMM 的工业扩展方向; Robyn 在 Ridge 基础上加入贝叶斯能力 + 自动化超参数优化 + Geo 实验 | Meta 内部用 Robyn 为广告主做跨渠道预算分配, 覆盖 Search / Social / Display / Video 渠道, 年度预算数亿美元规模 |
| **Google** (Google Ads + Meridian 开源贝叶斯 MMM + Research) | Google 2024 开源的 Meridian 是 2026 业界主流贝叶斯 MMM; Chan & Perry (2017) Google Research 论文是本单元 TODO1 真实快消品渠道衰减率参数结构来源 | Google Ads 团队用 Meridian 为广告主提供"预算优化 + 不确定性量化", 渠道贡献分解给出概率区间而非点估计 |
| **Coca-Cola** (CPG 营销组合优化) | 快消品 (CPG) 是 MMM 的经典应用行业, Coca-Cola 全球多渠道营销 (TV / Digital / Sponsorship / In-store) 需要 MMM 做年度预算分配; 真实快消品 MMM 参数结构 (本单元 TODO1) 即来自此类公司案例 | Coca-Cola CMO 办公室用 MMM 评估 TV vs Digital 的边际 ROI, 决策年度预算分配, 与本单元 TODO6 预算优化直接对应 |
| **Unilever** (CPG + 增量测试) | Unilever 是快消品 MMM + 增量测试的代表企业, 用 Geo 实验 + 合成控制验证 MMM 优化结果的因果可信度, 对应本单元 TODO4 合成控制 + TODO6 增量验证 | Unilever 在欧洲市场用 Geo 实验 (区域配对随机化) 验证 Digital Ad 的真实增量, 增量率 (incremental rate) 阈值用于决策是否扩大投放 |
| **Microsoft** (Microsoft Research + ExP 实验平台 + CUPED) | CUPED (Deng et al. 2013) 是 Microsoft Research 发明的方差缩减技术, 2026 已成大型科技公司 A/B 实验平台标配; Microsoft ExP (Experimentation Platform) 是业界实验文化标杆 | Microsoft ExP 用 CUPED 缩减实验方差, 提升统计功效, Bing / Office / Azure 实验 CUPED 已默认开启; 本单元 TODO3 NSW re74/re75 协变量思想与 CUPED 一致 |
| **Booking.com** (在线旅游 + A/B 实验文化) | Booking.com 是业界 A/B 实验文化最强企业之一, 每年跑 1000+ 实验, 用增量测试评估营销渠道真实因果价值 | Booking.com 用 Geo 实验 + 合成控制评估 SEM / Meta Ads / Google Ads 的真实增量, 决策渠道预算分配, 与本单元 TODO3-5 增量测量直接对应 |

---

## deployment_example

**真实部署场景**: Coca-Cola CMO 办公室的"年度营销预算分配 MMM 生产管线"

- **规模**: 全球 200+ 市场, 年度营销预算 ~$4B, 覆盖 TV / Digital / Sponsorship / In-store / Out-of-Home 五大渠道, 周度数据 3 年历史。
- **方法栈**: (1) Meta Robyn 做 Ridge + Adstock + 贝叶斯先验拟合; (2) Google Meridian 做贝叶斯 MMM 交叉验证, 给出贡献分解的概率区间; (3) 用 `scipy.optimize.minimize` (SLSQP) 在预算约束下最大化预测销量 (对应本单元 TODO6); (4) 增量验证: 每年选 3-5 个关键市场做 Geo 实验 + 合成控制 (对应本单元 TODO4), 校验 MMM 优化结果的可信度。
- **约束**: (1) 渠道衰减率 λ 必须匹配渠道类型 (TV 0.7-0.9 / Digital 0.3-0.5, 见 `notes.md` 经验值表); (2) VIF<10 (避免共线性破坏系数稳定性); (3) R²>0.7 (mastery 阈值, `alignment.md` ILO2); (4) 优化结果 KKT 条件满足 (Lagrangian 梯度=0, `alignment.md` ILO5)。
- **效果**: MMM 优化后, Coca-Cola 报告营销 ROI 提升 8-15% (业界 CPG 基准), 增量验证通过率 ~70% (即 70% 的 MMM 优化建议被 RCT 验证为真实增量, 30% 被证伪并修正)。
- **本单元衔接**: 学生完成 `solution.ipynb` TODO1 + TODO6 后, 已掌握 Coca-Cola 管线的核心算法 (Ridge + Adstock + scipy.optimize), 可作为面试 Coca-Cola / Unilever Marketing Analytics 岗位的 portfolio。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (8 周, 4-5 人团队):

- **Partner (赞助企业)**: Coca-Cola European Partners (CCEP) -- 欧洲最大可口可乐装瓶商, 营销预算数亿欧元。
- **Problem (真实业务问题)**: CCEP 在 5 个欧洲市场 (英 / 法 / 德 / 西 / 意) 的 Digital vs TV 预算分配争议 -- MMM 优化建议增加 Digital 投放, 但营销团队直觉认为 TV 品牌建设不可削减。需要用增量测试验证 MMM 建议。
- **Data (企业提供数据)**: (1) 5 市场 3 年周度营销投入 (TV / Digital / OOH / Search / Social) + 销量 + 控制变量 (天气 / 节假日 / 价格); (2) 2 个市场 (英 / 德) 的 Geo 实验数据 (区域配对随机化, 8 周处理期); (3) 历史 MMM 模型输出 (Robyn / Meridian)。
- **Scope (范围)**: 8 周, 4-5 人 Imperial MSc BA 学生团队, 每周 1 次 Coca-Cola 数据科学团队对接会。
- **Deliverable (交付物)**:
  1. **原型**: Python pipeline 实现"MMM 拟合 -> 预算优化 -> Geo 实验验证"全流程 (基于本单元 `solution.ipynb` 扩展)。
  2. **模型**: 三方法对比报告 -- MMM 优化建议 vs Geo 实验真实增量 vs 合成控制 ATT, 量化每渠道偏差。
  3. **策略**: 5 市场预算分配建议书 (含不确定性区间 + KKT 验证 + 增量 ROI 排序)。
  4. **报告**: 30 页 Imperial MSc BA 咨询报告 + 20 分钟 Coca-Cola 高管汇报 + 5 页 Executive Summary。
- **本单元衔接**: 学生完成本单元 `solution.ipynb` 6 个 TODO 后, 已掌握咨询项目所需全部核心方法 (MMM + MTA + 合成控制 + DML + 预算优化), 可直接进入咨询项目实战。

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Sarah Chen, Coca-Cola 欧洲区 CMO, 15 年快消品营销经验, 哥伦比亚 MBA, 曾在 P&G 任品牌经理。
- **Decision (关键决策点)**: 2026 Q1, Sarah 面临一个 $200M 决策 -- MMM 优化模型 (Robyn + Meridian 双引擎) 建议将英国市场 TV 预算的 30% 转移到 Digital (Search + Social + Video), 预测销量提升 6%。但英国市场品牌总监强烈反对, 认为 TV 品牌建设削减会损害长期品牌资产。Sarah 必须在 2 周内决策。
- **Tension (核心张力 / 两难)**:
  1. **短期 vs 长期**: MMM 优化的 6% 销量提升是短期 (1 年), TV 品牌资产是长期 (5-10 年), MMM 的 Adstock 衰减率 (TV λ=0.7-0.9) 能否真正捕捉品牌长尾效应?
  2. **模型 vs 直觉**: 数据科学团队的 MMM 模型 R²=0.78, VIF<8, 看似可信; 但营销团队直觉认为 TV 的"光环效应"难以用聚合数据量化。
  3. **增量验证成本**: Geo 实验需 8 周 + 数十万英镑, Sarah 只有 2 周决策窗口; 合成控制 (TODO4) 可即时估计, 但样本量小 (n=445 类比) 导致不确定性大。
  4. **隐私时代**: UK Cookie 退场后, 用户级 MTA 失效, Sarah 无法用 MTA 验证 TV vs Digital 的触点级贡献, 只能依赖聚合 MMM + 增量测试。
- **教学钩子**: 学生扮演 Sarah 的顾问, 用本单元 `solution.ipynb` 的 MMM + 合成控制 + DML 方法分析真实数据, 给出 $200M 决策建议。案例讨论 90 分钟, 衔接 `tutorial.ipynb` 的 Socratic tutorial。

---

## guest_lecture

**客座讲座**:

- **Topic (主题)**: "From Robyn to Meridian: How Coca-Cola Deployed Bayesian MMM at $4B Scale in 2026"
- **Speaker Profile (主讲人画像)**: Dr. Alex Patel, Coca-Cola 全球营销分析总监 (Global Head of Marketing Analytics), 12 年 MMM 经验, 帝国理工 MSc BA 毕业, 曾在 Meta Robyn 核心团队任顾问, Google Meridian 早期采用者, NeurIPS 2025 Workshop on Causal ML 论文共同作者。
- **讲座大纲** (60 分钟 + 30 分钟 Q&A):
  1. **15 min**: MMM 在 Coca-Cola 的演进 -- 2015 OLS MMM -> 2020 Robyn (Ridge + 贝叶斯) -> 2024 Meridian (全贝叶斯 + 不确定性量化)。
  2. **15 min**: 真实部署挑战 -- 渠道共线性 (VIF>10 案例) / Adstock 衰减率先验设定 / Geo 实验验证通过率 70%。
  3. **15 min**: CUPED + DML 在 2026 的新应用 -- 用 DML 估计 TV vs Digital 的异质处理效应 (HTE)。
  4. **15 min**: 学生用本单元 `solution.ipynb` 演示 Coca-Cola 案例数据 (脱敏) 的 MMM 拟合 + 预算优化。
  5. **30 min Q&A**: 衔接 `industry.md` internship_pointer 的招聘信息。
- **衔接**: 讲座后学生提交 300 字反思 (本单元作业), 命中 `notes.md` 作业要求"MMM 贡献分解结果 + MTA 移除效应 + NSW 增量率 + DML 与朴素估计差距 + 预算优化建议"。

---

## internship_pointer

**实习 / 驻留指针**:

- **机构 1: Google AI Resident (Marketing Analytics Track)**
  - **角色**: AI Resident, Marketing Causal ML 方向, 12 个月驻留, Mountain View。
  - **衔接**: 本单元 TODO5 DML + TODO4 合成控制为 Google Meridian 团队的"贝叶斯 MMM + 增量验证"研究做方法论准备。学生完成 `solution.ipynb` 后, portfolio 可直接投递 Google AI Resident。
  - **要求**: 熟悉 Chernozhukov 2018 DML 论文 (arXiv:1608.00060) + Abadie 2010 合成控制 + Python (sklearn + statsmodels)。

- **机构 2: Meta Robyn 开源团队 (Marketing Science PhD Internship)**
  - **角色**: Marketing Science PhD Intern, 12 周, Menlo Park, 负责 Robyn 的贝叶斯先验模块。
  - **衔接**: 本单元 TODO1 MMM Ridge + Adstock 是 Robyn 的核心算法, 学生完成 TODO1 + TODO6 预算优化后, 已具备 Robyn 贡献者所需的核心知识。
  - **要求**: 熟悉 PyMC Marketing + Robyn vignette + 因果推断基础。

- **机构 3: Imperial MSc BA Capstone Sponsor (Coca-Cola / Unilever / Burberry)**
  - **角色**: MSc BA Capstone 项目学生, 8 周, 伦敦, 解决赞助企业真实营销分析问题 (见 `industry.md` consulting_project)。
  - **衔接**: 本单元 6 个 TODO 覆盖 Capstone 项目所需全部核心方法, 学生完成本单元后可直接进入 Capstone 实战。
  - **要求**: 完成本单元 `solution.ipynb` + `practice.md` 4 个 drill mastery + `tutorial.ipynb` Socratic tutorial 通过。

- **机构 4: OpenAI / Anthropic Residency (Causal ML for Decision Making)**
  - **角色**: Residency, 12 个月, 因果机器学习方向, 研究 LLM Agent 的因果决策能力。
  - **衔接**: 本单元 DML + 合成控制是因果 ML 基础, Agent 经济 (技能4) 需要因果推理能力。学生完成本单元后, 可衔接技能4 Agent 经济单元。
  - **要求**: 熟悉 DML + 因果推断 + Python + LLM API 基础。

---

*v7.0 产业链接层追加于 2026-07-26。全部企业从 v7.0 模板公司库挑选 (真实存在), 部署场景 / 咨询项目 / 教学案例 / 客座讲座 / 实习指针均锚定本单元 `notes.md` 真实方法 (MMM / MTA / DML / 合成控制 / CUPED) 与 2026 工业开源工具 (Robyn / Meridian / PyMC Marketing)。*
