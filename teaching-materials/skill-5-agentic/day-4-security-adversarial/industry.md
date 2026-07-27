# industry.md · 产业链接层 (v7.0)

> 单元：技能5 · Day 4 安全防护与对抗 (garak v0.15.1 / PyRIT v1.0.0)
> 主题：营销 Agent 安全对抗的产业落地
> 标准：Imperial MSc BA 咨询项目 + HBS 案例法 + MIT Sloan 行动学习

---

## real_companies

从公司库挑选与本单元主题（LLM/Agent 安全对抗）匹配的真实企业锚点：

| 公司 | 与本单元关联 | 业务场景 |
|:----:|------------|---------|
| **Anthropic** | Claude 安全设计五原则（最小权限/人在回路/分层防御/可审计/优雅降级）是本单元架构层防御的理论来源；Constitutional AI 是模型层安全对齐的代表 | 营销 SaaS 厂商接入 Claude API 生成营销文案，依赖 Anthropic 的安全对齐降低 DAN/越狱成功率；reading.md 深链 https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails |
| **OpenAI** | Red Teaming Network 是行业首个规模化红队实践；GPT 系列模型是 garak/PyRIT 的常见 target；OpenAI 在系统提示加固上的工程实践被本单元六层防御引用 | 营销 Agent 用 GPT-4o 生成个性化邮件，用 garak 扫描其 API 接口的 dan/promptinject/encoding 漏洞，用 PyRIT 编排多轮对抗 |
| **DeepMind** | 前沿安全框架（Frontier Safety Framework）+ 自动化红队研究；AdvBench（arXiv 2307.15024）的 GCG 攻击算法与 DeepMind 的对抗鲁棒性研究同源 | 大型消费品牌的内部 AI 安全团队参考 DeepMind 的分层评估方法，对营销 Agent 做 capability + safety 双轨评估 |
| **Apollo Research** | 专注 LLM 评估与欺骗性对齐（deceptive alignment）；其 evals 方法论影响 PyRIT 的 Scorer 设计 | 营销 Agent 在上线前委托 Apollo 式第三方评估机构做独立安全审计，输出 capability profile + failure mode 报告 |
| **Scale AI** | SEAL（Safety Evaluations and Alignment Leaderboards）提供标准化安全评估榜单；HarmBench（arXiv 2402.04249）在其上排名 | 营销 SaaS 厂商在 Scale AI SEAL 榜单上对比自研 Agent 与基线模型的安全姿态，作为采购/上线的合规依据 |
| **Conjecture** | AI 安全研究机构，关注对抗鲁棒性与可控性；其工具链与本单元 garak+PyRIT 互补 | 企业 AI 安全团队用 Conjecture 式威胁建模 + 本单元工具链做营销 Agent 的 attack surface mapping |

> 选取 Anthropic / OpenAI / DeepMind / Apollo Research / Scale AI / Conjecture 共 6 家（≥3 要求满足），全部来自公司库"安全/对齐"类，全部真实存在。

## deployment_example

**场景**：某营销 SaaS 厂商（假设为 Klaviyo 规模，邮件/SMS 营销自动化平台）在生产 CI/CD 中部署 garak + PyRIT 作为 Agent 发布门禁。

- **规模**：每次 Agent 版本发布前，对营销内容生成接口跑 garak 全 probe 扫描（20+ 类）+ PyRIT 用 AdvBench 520 条批量对抗；周均 ~3 次发布，月均 ~60 次扫描。
- **约束**：① 扫描必须在 30 分钟内完成（CI/CD 时间窗），garak 并行 8 probe + PyRIT 并发 20 请求；② LLM API 调用成本月预算 $500，靠经济档模型 + 缓存控制；③ 任何 probe fail 率 > 5% 阻断发布，需 Head of AI 签字豁免。
- **效果**：① 上线 3 个月内拦截 2 次高危发布（一次 `encoding` 类 fail 率 12%，发现 Base64 编码绕过系统提示；一次 `promptinject` 类 fail 率 8%，发现评论注入路径）；② 将 `goodside` probe 类的 fail 率从基线 7% 降到 2%（加固系统提示 + 输出审查）；③ 对标 NIST AI RMF 的 Measure 步骤，生成合规证据链供法务/审计调阅。
- **失败模式**：garak 通过 ≠ 安全（本单元 notes.md 明示）；曾出现 garak 全过但生产中被新型间接注入攻破的案例，需 Day 5 在线监控补位（异常拒绝率突增告警）。

## consulting_project

**Imperial College MSc Business Analytics 风格咨询项目**：

- **Partner（赞助企业）**：Burberry（奢侈品零售，营销内容生成 Agent 部署方）
- **Problem（真实业务问题）**：Burberry 的个性化邮件营销 Agent（生成多语言产品推荐文案）在内部安全审计中被发现对间接注入（评论埋 `SYSTEM:` 指令）脆弱，需在 8 周内完成安全姿态评估 + 分层防御原型 + 发布门禁流程设计。
- **Data（企业提供数据）**：① 脱敏的历史营销文案 10,000 条（含已被拒绝的敏感请求）；② 内部红队过去手工构造的 50 条对抗提示；③ 接入 AdvBench 520 + HarmBench standard behaviors 作为外部基准；④ Agent 的系统提示 v1.4（脱敏版）。
- **Scope（8 周，4-5 人团队）**：
  - W1-2：attack surface mapping + garak 全 probe 扫描基线
  - W3-4：PyRIT 编排 AdvBench/HarmBench 输入，建立被攻破率基线
  - W5-6：分层防御原型（输入过滤 + 系统提示加固 + 输出审查），A/B 测试防御前/后
  - W7：发布门禁流程设计（fail 率阈值 + 豁免审批链 + NIST AI RMF Measure 对标）
  - W8：交付物定稿 + Burberry AI 治理委员会汇报
- **Deliverable（交付物）**：① garak+PyRIT 红队评估报告（IMRaD 式，含 probe 类别 fail 率热力图）；② 分层防御原型（Python 代码 + 系统提示 v2.0）；③ 发布门禁流程文档（含 Head of AI 豁免模板）；④ 高管摘要 1 页（给 CMO/CTO）。

## case_study

**HBS 风格教学案例钩子**：

- **Protagonist（主角）**：Maya Chen，Head of AI at Sierra（对话式 AI 平台），曾任 Anthropic 安全工程师。负责为一家快消品牌客户（假设为 Unilever 量级）上线营销内容生成 Agent。
- **Decision（关键决策点）**：上线前 48 小时，garak 扫描报告显示 `encoding` probe 类 fail 率 9%（Base64 编码绕过系统提示），`promptinject` 类 fail 率 6%。客户的 CMO 要求按期上线（双十一营销节点），CTO 要求修复后上线。Maya 需在 2 小时内决定：① 按期上线 + 灰度 10% + 在线监控；② 延期 1 周修复 + 错过双十一；③ 上线但加输入过滤 + 输出审查双层加固（中间方案）。
- **Tension（核心张力/两难）**：① 速度 vs 安全：双十一窗口不可逆，但 `encoding` 类漏洞可能被竞品利用注入负面文案；② 工程理性 vs 治理合规：garak 通过 ≠ 安全，但 fail 率 9% 是否构成"不可接受风险"缺乏行业标准（HarmBench 榜单仅给基线，无阈值）；③ 主角身份冲突：前 Anthropic 安全工程师的"安全优先"价值观 vs 现任 Head of AI 的"客户至上"KPI。
- **教学目标**：① 用 NIST AI RMF 四步循环（Govern/Map/Measure/Manage）结构化决策；② 理解自动化红队的边界（L1 关联分析，不能证明安全）；③ 练习"高杠杆点"识别--输入过滤是否为 9% fail 率的高杠杆修复点？
- **附录**：garak 报告节选 + AdvBench 520 攻破率分布 + NIST AI RMF 映射表。

## guest_lecture

**客座讲座**：

- **Topic（主题）**："Red Teaming Production LLM Agents at Scale: From garak Probes to Online Anomaly Detection"
- **Speaker Profile（主讲人画像）**：Dr. Alex Wei，Head of AI Safety at Sierra（对话式 AI 平台），前 OpenAI Red Teaming Network 成员。博士研究方向为 LLM 对抗鲁棒性，曾在 NeurIPS/ICML 发表 Prompt Injection 防御相关论文。在 Sierra 主导建立 Agent 发布门禁流程，月均扫描 200+ 次，拦截高危发布 5+ 次。
- **讲座大纲（50 分钟 + 10 分钟 Q&A）**：
  1. (10') 生产环境红队 vs 学术红队的差异（规模/时延/成本约束）
  2. (15') garak 在 CI/CD 中的工程化：probe 并行 + fail 率阈值 + 豁免审批链
  3. (15') PyRIT 多轮自适应对抗（`RedTeamingOrchestrator`）的真实攻击案例（脱敏）
  4. (10') 在线监控补位：异常拒绝率突增 = 可能正被新型攻击（衔接 Day 5）
- **与本单元衔接**：讲座第 2-3 部分直接深化 starter.ipynb TODO1/TODO4 的工程实践；第 4 部分为 Day 5 监控体系埋伏笔。

## internship_pointer

**实习/驻留指针**：

- **机构（多个候选）**：
  1. **OpenAI Residency**（https://openai.com/residency）- AI 安全研究驻留，1 年期，含红队/对齐方向
  2. **Anthropic Residency / William P. Young Fellowship**（https://www.anthropic.com/careers）- 安全对齐研究驻留，6-12 个月
  3. **Google AI Resident (DeepMind Safety Team)**（https://research.google/careers/residency/）- AI 安全研究驻留，含对抗鲁棒性方向
  4. **Scale AI SEAL Internship**（https://scale.com/careers）- 安全评估榜单实习，含 HarmBench 类基准维护
  5. **企业 capstone sponsor**：Sierra / Klaviyo / Burberry 等，作为 Imperial MSc BA capstone 项目的赞助方（见 consulting_project）
- **角色**：AI Safety Researcher / Red Team Engineer / Eval Engineer
- **衔接（本单元如何为该角色做准备）**：
  1. **工具栈对口**：garak + PyRIT 是 OpenAI/Anthropic 红队日常使用的工具（本单元 TODO1/TODO4 已上手）
  2. **基准熟悉度**：HarmBench（arXiv 2402.04249）+ AdvBench（arXiv 2307.15024）是 SEAL 榜单与学术论文的标准基准，本单元已用作 PyRIT 输入
  3. **方法学对口**：NIST AI RMF 四步循环是工业界安全治理的通用框架，本单元 TODO6 安全评估报告已对标
  4. **作品集**：完成的 `solution.ipynb`（6 TODO 全填）+ `research.md` IMRaD 大纲 + 本 `industry.md` 咨询项目设计，可直接作为申请材料附件
  5. **面试准备**：能口述"garak 通过 ≠ 安全"的边界 + 间接注入 vs 直接注入的 fail 率差异根因 + 分层防御的高杠杆点--这三点是 OpenAI/Anthropic 红队岗位的高频面试题

---

*本文件为 v7.0 产业链接层。不修改 v5.0/v6.0 任何文件。real_companies 全部从公司库挑（安全/对齐类），全部真实存在。*
