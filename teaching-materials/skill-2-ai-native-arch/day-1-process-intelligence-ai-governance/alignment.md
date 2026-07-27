# Constructive Alignment (Biggs 建构对齐) · Day 1 流程智能驱动 + AI治理框架

> v6.0 学习科学层。本文件将本 Day 的 ILO (Intended Learning Outcomes) / TLA (Teaching-Learning Activities) / AT (Assessment Tasks) 三者对齐，避免"教的不考、考的没教"。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 pydantic 定义 NIST AI RMF 控制项 schema，覆盖 18 个真实控制项与 4 状态枚举 | starter.ipynb TODO1 + practice.md D1 (Worked->Faded->Independent) + tutorial.ipynb Socratic 追问 schema 设计 | solution.ipynb TODO1 自动跑通 + tutorial 后测：解释 PARTIAL vs NOT_APPLICABLE 区别 | >=80% 控制项字段完整 + 能口头解释枚举语义 |
| **ILO2**: 能实现 NIST 合规扫描器 (0-100 评分) + EU AI Act 风险分级器 (4 级瀑布判定) | starter.ipynb TODO3+TODO4 + practice.md D2 (Worked->Faded->Independent) + schedule.json C1+C2 卡片复习 | solution.ipynb TODO3+TODO4 跑通 + 300 字分析：8 用例在哪个 NIST 功能得分最低 + 对应 EU 等级 | >=70% 用例评分正确 + 瀑布判定顺序无错 |
| **ILO3**: 能用 pandas 生成"用例×功能"风险热力图，识别最弱控制项，并用天道推演输出 2-3 条风险路径 | starter.ipynb TODO5+TODO6 + practice.md D3 (Worked->Faded->Independent) + schedule.json C3 卡片复习 + tutorial 推演追问 | solution.ipynb TODO5+TODO6 跑通 + 天道推演 300 字风险路径分析 (immediate->near->far 3 层) | 能独立解 + 推演 >=2 条平行时间线 + 识别 1 个高杠杆点 |
| **ILO4**: 能为营销 AI 系统设计 NIST + EU Act 双框架治理控制点，并说明 MCP 如何将治理内嵌到 Agent 工作流 | practice.md progressive_project (proposal->milestone->final->poster) + tutorial.ipynb Hattie [FEED-FORWARD] 反馈 + notes.md 2026 前沿补充章节 | poster (Day 2 课前 5 分钟) + 可选 MCP 治理工具设计 | poster 能说清最弱控制项 + EU 等级 + 1 条高杠杆干预 |

---

## mastery_threshold (整体掌握阈值)

参照 MIT 6.5940 课程"至少 4/5 实验提交方可及格"的明文规则，本 Day 整体掌握阈值为：

- **及格线 (Pass)**：4 个 AT 中至少 3 个达标（>=70% 各自 mastery_threshold）
- **优秀线 (Distinction)**：4 个 AT 全部达标 + poster 被同伴评为 top 30%
- **未达及格线**：进入 `practice.md` weak_loop，回退到 D1 阶段 1 重做

---

## 3 自检问题 (Biggs + Hattie Feed Up/Back/Forward)

> Biggs 建构对齐的三问，对应 Hattie (2007 RER 77(1):81-112) 三级反馈：Feed Up (任务对齐目标) / Feed Back (差距诊断) / Feed Forward (下一步改进)。

### 1. TLA 是否训练 ILO? (Feed Up - 任务对齐目标)

- D1 (pydantic schema) 是否训练 ILO1？**是**。D1 阶段 1 Worked 演示真实控制项建模 -> 阶段 2 Faded 填字段 -> 阶段 3 Independent 完整 18 项。学生若跳过 D1 直接做 AT，会在 ComplianceStatus 枚举上卡住。
- D2 (双框架判定) 是否训练 ILO2？**是**。D2 阶段 1 演示 assess_control 函数 -> 阶段 2 填阈值 -> 阶段 3 独立实现 classify_eu_ai_act。跳过 D2 学生会在 EU Act 瀑布判定顺序上出错。
- D3 (热力图+推演) 是否训练 ILO3？**是**。D3 阶段 1 演示 pivot_table + 推演路径 -> 阶段 2 填因果节点 -> 阶段 3 独立完成 2 个用例。跳过 D3 学生会在天道推演 3 层结构上漏掉 far 层。
- tutorial Socratic 追问是否训练 ILO4？**是**。Oxford tutorial 仿真禁直接答案，迫使学生口头辩护 MCP 治理工具设计。

**自检结论**：TLA 与 ILO 1:1 对齐，无"训练真空"。

### 2. AT 是否测量 ILO? (Feed Back - 差距诊断)

- AT1 (solution.ipynb TODO1 跑通 + 口头解释枚举) 是否测量 ILO1？**是**。代码跑通测"能做"，口头解释测"懂为什么"。
- AT2 (solution.ipynb TODO3+TODO4 + 300 字分析) 是否测量 ILO2？**部分**。代码跑通测"能实现"，但 300 字分析只测"能识别短板"而非"能解释为什么短板在该功能"。**改进**：tutorial 后测加问"为什么 NIST 的 Measure 维度得分普遍低于 Govern 维度？根因是什么？"
- AT3 (TODO5+TODO6 + 推演 300 字) 是否测量 ILO3？**是**。代码 + 推演双测，但推演 300 字字数太少难以容纳 3 层结构。**改进**：放宽到 500 字或允许图表。
- AT4 (poster + MCP 工具设计) 是否测量 ILO4？**是**。poster 5 分钟口述测"能讲清"，MCP 工具设计测"能设计"。

**自检结论**：AT 与 ILO 对齐，AT2/AT3 有改进空间，已写入 tutorial Hattie [FEED-FORWARD]。

### 3. 不经 TLA 能过 AT 吗? 若能 = 对齐失败 (Feed Forward - 下一步改进)

- 学生能不经 D1 直接过 AT1 吗？**理论上能**（pydantic schema 简单，看过文档就能写）。**风险**：学生跳过 D1 阶段 1 Worked 示范，导致 ComplianceStatus 枚举不完整。**对策**：AT1 加口测"NOT_APPLICABLE 何时使用"，没看 Worked 示范答不出。
- 学生能不经 D2 直接过 AT2 吗？**较难**。EU AI Act 瀑布判定顺序容易出错（保险定价例外），必须经过 D2 阶段 1 Worked 示范。
- 学生能不经 D3 直接过 AT3 吗？**很难**。天道推演 3 层结构 + 平行时间线 + 高杠杆点，不经 D3 Worked 示范学生只能列 1 条线性路径。
- 学生能不经 tutorial 直接过 AT4 吗？**不能**。poster 口述需经过 tutorial Socratic 追问训练，否则会被同伴追问"你的高杠杆点凭什么不是另一个？"卡住。

**自检结论**：D1 有对齐裂缝（学生可能跳过），已加口测对策。其他 TLA 均为 AT 必经之路。**Feed Forward**：下版本 v7.0 考虑把 D1 阶段 1 Worked 示范改为强制视频观看（带进度条追踪），堵住跳过漏洞。

---

## 交叉引用

- `practice.md`：drills D1/D2/D3 即本文件 TLA 的具体实现
- `schedule.json`：FSRS-6 卡片 C1/C2/C3 对应 ILO1/ILO2/ILO3 的核心概念复习
- `tutorial.ipynb`：Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] 实现 Feed Back + Feed Forward
- `notes.md`：v5.0 原文提供 ILO 的理论指针，本文件是 v6.0 学习科学层
