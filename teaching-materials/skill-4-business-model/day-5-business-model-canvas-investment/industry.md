# Day 5 产业链接层 (v7.0)

> 本单元 (商业模式画布 + 投资估值) 的产业链接层: >=3 真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。与 v5.0 (NPV=$451.2K / IRR=20.08% / P(NPV>0)=55.7%) 和 v6.0 学习科学层对齐。产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。

## real_companies

>=3 家真实企业锚点 (从公司库挑, 与本单元"AI 商业模式画布 + 投资估值"主题匹配):

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **HubSpot** | AI SaaS 财务基准 (2023 Revenue $2.17B, GM ~78%) | MarketingAgent Pro DCF 模型的毛利率校准源; HubSpot Marketing Hub 内嵌 AI Agent (Content Assistant, ChatSpot), 用 outcome-based pricing 扩展, 与本单元 TODO1 收入流适配 |
| **OpenAI** | 推理成本基准 ($0.03/1K input, $0.06/1K output GPT-4) | 本单元龙卷风图第一高杠杆因子 (推理成本) 直接用 OpenAI 定价校准; OpenAI 自身商业模式 (API + ChatGPT Plus + Enterprise) 是 AI 商业模式画布九宫格的教科书案例 |
| **Anthropic** | 推理成本 + 安全双约束 | Anthropic Claude API 定价与 OpenAI 同量级, 在 AI 商业模式画布"核心伙伴"格形成依赖; Constitutional AI 方法对成本结构有直接影响 |
| **Jasper AI** | AI SaaS 估值对标 ($125M ARR, $1.5B 估值 2022 Series A) | MarketingAgent Pro 直接竞品, 单位经济模型 (ARPU/CAC/LTV) 校准自 Jasper Crunchbase 公开数据; Jasper 2023-2024 估值回调是 Bear 路径的真实案例 |
| **DeepSeek** | 推理成本颠覆者 (-90%+) | 天道推演 Bull 路径的触发变量; DeepSeek V3/R1 把开源模型推理成本砍到 OpenAI 的 1/10, 直接改变 AI SaaS 毛利率结构, 本单元蒙特卡洛 Bull 场景的核心假设 |
| **Perplexity** | AI 原生商业模式新形态 | Perplexity 的订阅 + 广告分成 + API 三收入流, 是本单元 TODO1 收入流 (outcome-based + 价值分成) 的真实样本; 其 Series B 估值 $9B (2024) 是 AI 估值最新基准 |

## deployment_example

**部署场景**: 某中型 B2B SaaS 公司 (200 人, ARR $50M, 类 HubSpot 中端客户) 内部投资委员会用本单元方法评估"是否自建 vs 调用 OpenAI/Anthropic API 部署内部 MarketingAgent"。

- **规模**: 5000 个企业客户, 每客户月均 100 万 tokens (50 万 input + 50 万 output) 推理用量, 5 年评估窗口。
- **约束**:
  1. CFO 要求 5 年 NPV > 0 且 IRR > 15%;
  2. CTO 要求 P(NPV>0) > 70% (蒙特卡洛 10000 次);
  3. CEO 要求天道推演三路径中 Bear 路径 NPV > -$1M (下行保护);
  4. 合规要求: 数据不可出域, 推理成本用美元计价。
- **方法**: 用本单元 `starter.ipynb` 的 6 个 TODO 流程, 把"自建模型"和"调用 API"两个方案分别跑一遍 DCF (TODO2-3) + 蒙特卡洛 (TODO4) + 龙卷风图 (TODO5) + 天道推演 Bull/Base/Bear (TODO6)。
- **效果**: 输出两套 NPV/IRR/PI + P(NPV>0) + Bull/Base/Bear 三路径表; 投资委员会用龙卷风图识别高杠杆因子 (推理成本 vs 自建折旧 vs 数据成本), 用天道推演沙盘识别"OpenAI 涨价 50% / DeepSeek 开源新模型 / 客户 churn 翻倍"三个 far 层场景的连锁反应; 最终决策带不确定性区间而非单一数值, CFO 可直接用于董事会汇报。
- **真实基准**: 推理成本用 OpenAI Pricing (https://openai.com/api/pricing/) 和 DeepSeek Pricing (https://api-docs.deepseek.com/quick_start/pricing) 校准; 毛利率用 HubSpot 2023 财报 78% 作为 SaaS 上限, 用本单元 MarketingAgent Pro 65% 作为 AI SaaS 基准; 估值用 Jasper AI $1.5B / Perplexity $9B 作为可比交易倍数。

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (8 周, 4-5 人团队):

- **Partner (赞助企业)**: Burberry (奢侈品零售, 需评估"AI Stylist Agent"投资可行性)。
- **Problem**: Burberry CMO 想在全渠道部署 AI Stylist Agent (个性化推荐 + 虚拟试穿 + AI 客服), CFO 要求用真实财务模型量化 5 年投资回报, 并评估推理成本对毛利率的长期影响; 同时 CEO 要求给出 Bull/Base/Bear 三路径下的下行保护。
- **Data**: Burberry 提供 (脱敏) 12 个月 50 万活跃客户的 ARPU / CAC / LTV / 复购率 / 推理用量数据; OpenAI / Anthropic / DeepSeek API 定价 (公开); HubSpot / Jasper AI 财报基准 (公开)。
- **Scope**: 8 周, 4-5 人 Imperial MSc BA 学生团队; 周 1-2 数据清洗 + 单位经济建模, 周 3-4 DCF + 蒙特卡洛 (本单元 TODO2-4), 周 5-6 敏感性分析 + 天道推演 Bull/Base/Bear (TODO5-6), 周 7-8 报告 + 董事会汇报。
- **Deliverable (交付物)**:
  1. 可执行 Jupyter notebook (复用本单元 `starter.ipynb` 模板, 换入 Burberry 数据);
  2. 投资评估报告 (NPV / IRR / PI + P(NPV>0) + 三路径 NPV 区间);
  3. 龙卷风图 + 天道推演沙盘可视化 (高管友好版);
  4. 战略建议书 (含"自建 vs API"决策 + DeepSeek 效应的 Bull 路径 capital reallocation 建议 + Bear 路径下行保护方案)。

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Sarah Chen, Head of AI @ HubSpot (虚构角色, 真实公司场景), 向 CFO 和 CEO 汇报。
- **Decision (关键决策点)**: HubSpot 是否在 2026 Q2 把 Marketing Hub 的 AI Agent 从"调用 OpenAI GPT-4 API"切换到"自研 7B 参数小模型 + DeepSeek 蒸馏"? 切换需投入 $2M 一次性研发 + 6 个月迁移期。
- **Tension (核心张力/两难)**:
  - 切换可把推理成本砍 80% (DeepSeek 效应), 毛利率从 65% 提到 75%, NPV 显著上升 (Bull 路径, P(NPV>0) ↑ 至 80%);
  - 但自研模型 quality 下降可能流失 10% 企业客户, CAC 上升, LTV 下降 (Bear 路径, P(NPV>0) < 30%);
  - 同时, OpenAI 可能在 2026 Q3 推出 GPT-5 + 降价 50% (Base 路径的 far 层黑天鹅), 自研投入可能被即时颠覆;
  - Sarah 必须用蒙特卡洛 + 天道推演量化这三个场景的 P(NPV>0), 并向 CFO 给出带不确定性区间的决策建议, 而非单一 NPV 数值;
  - CFO 反问: "如果 P(NPV>0) = 55.7%, 你建议 go 还是 no-go?" -- 这是教学案例的核心张力。
- **教学目标**: 学会用本单元方法 (DCF + 蒙特卡洛 + 龙卷风图 + 天道推演) 在真实业务约束下做投资决策; 理解推理成本作为 AI 估值第一高杠杆因子的战略含义; 培养学生在不确定性下做决策的判断力。

## guest_lecture

**客座讲座**:

- **Topic**: "From PoC to Scale: How HubSpot Values AI Investments with Monte Carlo + Scenario Planning"
- **Speaker Profile**: HubSpot Director of AI Strategy (或 Jasper AI 前 CFO, 或 Sequoia Capital AI 投资合伙人) -- 真实在生产中用过 DCF + 蒙特卡洛评估 AI 项目投资的人, 最好有"用推理成本建模改变 CFO 决策"的一手经验; 优先选 HubSpot 内部有 ChatSpot 投资评估经验的高管。
- **内容钩子**:
  1. 真实案例: HubSpot ChatSpot 投资决策的 NPV / IRR + P(NPV>0) 推算过程, 以及实际 outcomes 对比;
  2. 推理成本曲线: 从 GPT-4 ($0.03/1K) 到 DeepSeek (-90%) 的 18 个月观察, 以及 HubSpot 内部毛利率的实际变化;
  3. 天道推演实战: Bull / Base / Bear 三路径在 2024-2026 的实际 outcomes 对比, 哪个路径成真, 哪个偏离;
  4. Q&A: 学生用本单元 `starter.ipynb` 跑出的 MarketingAgent Pro NPV=$451.2K / IRR=20.08% / P(NPV>0)=55.7% 与主讲人对比, 讨论"为什么我们的数字与实际偏差 15%"。
- **形式**: 60 分钟 (40 分钟分享 + 20 分钟 Q&A), 可远程 Zoom; 配合本单元 tutorial.ipynb 的牛津 Socratic 仿真作为预习。

## internship_pointer

**实习 / 驻留指针**:

- **机构 (多个候选, 全部真实)**:
  - **OpenAI Residency / Anthropic Residency** (1 年, AI 研究驻留) -- 适合想做 AI 安全 + 商业模式交叉研究的学生;
  - **McKinsey / BCG / Bain AI Practice** (暑期实习, 10-12 周) -- 适合想做 AI ROI 咨询的学生;
  - **HubSpot / Jasper AI / Perplexity Business Operations** (暑期实习, 10-12 周) -- 适合想做 AI SaaS 内部投资评估的学生;
  - **Sequoia Capital / a16z AI 投资组** (Associate, 2 年) -- 适合想做 AI 估值投资的学生;
  - **Imperial MSc BA Capstone Sponsor** (8 周咨询项目, 见 consulting_project 节) -- 适合想拿学位同时积累实战的学生。
- **角色**: AI Strategy Intern / Business Operations Analyst / AI Investment Associate / AI Research Resident
- **衔接 (本单元如何为该角色做准备)**:
  1. **TODO1-3** (画布 + DCF + IRR/PI) -> 咨询/投资面试的标准 case 题 ("评估某 AI SaaS 的投资可行性"), 是 McKinsey/BCG/Sequoia 面试的常见题型;
  2. **TODO4** (蒙特卡洛) -> 投资银行与 PE 的估值建模必备技能, OpenAI/Anthropic Residency 的研究方法基础;
  3. **TODO5** (敏感性分析 + 龙卷风图) -> 战略咨询的"高杠杆点"识别能力, 是 Bain/Bainbridge 的核心方法论;
  4. **TODO6** (天道推演 Bull/Base/Bear) -> 投资合伙人的"沙盘推演"思维, 与项目 CLAUDE.md 天道推演系统同构, 是 Sequoia/a16z 投资决策的核心思维;
  5. **本单元产出** (research.md + industry.md) 可直接作为 OpenAI Residency / McKinsey AI 实习申请的 writing sample, 证明候选人能用真实数据 + 真实库做可复现的 AI 估值研究。

产业链接遵循 Imperial MSc BA 咨询项目 (Burberry / Expedia / J&J) / HBS 案例法 / MIT Sloan 行动学习模式; 与项目 CLAUDE.md 天道推演系统的"沙盘模拟"和"反馈学习"能力同构。
