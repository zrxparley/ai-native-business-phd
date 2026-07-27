# Day 3 建构对齐 (Constructive Alignment) - Biggs ILO<->TLA<->AT 矩阵

> 基于 Biggs 建构对齐 + Bloom mastery learning + Hattie 可见学习

## ILO<->TLA<->AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1 能解释 NIST AI RMF 1.0 四步循环 (Govern/Map/Measure/Manage), 说明为什么Govern贯穿全过程, 并用pydantic定义18个真实控制项schema | starter.ipynb TODO1+TODO3 (定义ComplianceStatus枚举+ControlItem模型+18控制项, 实现assess_control+score_to_status+scan_nist_rmf) + practice.md drill D1 worked-faded + tutorial.ipynb Socratic追问Govern贯穿性 | solution.ipynb TODO1+TODO3 后测 + tutorial.ipynb student_model.json掌握度>=0.8 | scan_nist_rmf跑通且18控制项全覆盖, 掌握度>=80% |
| ILO2 能实现三框架风险分级器 (NIST/EU AI Act/中国), 说明三者互补关系 | starter.ipynb TODO4 (classify_eu_ai_act+classify_china_ai_law+compare_three_frameworks) + practice.md drill D2 worked-faded + tutorial.ipynb Socratic追问三框架能否互相替代 | solution.ipynb TODO4后测 + 9个营销AI用例三框架分级全对 | 9用例三框架分级9/9正确 (含情感分析工作场所Article 5禁止) |
| ILO3 能用pandas构建企业AI治理台账, 追踪治理闭环 (登记->评估->控制->监控->审计), 识别闭环"断链"风险 | starter.ipynb TODO5 (build_governance_ledger+closed_loop_status) + practice.md drill D3 worked-faded + tutorial.ipynb Socratic追问5环节最可能断链点 | solution.ipynb TODO5后测 + 5环节断链识别>=4个 | 闭环断链识别>=80% (5环节至少识别4个) |
| ILO4 能为营销AI系统设计5层安全策略 (治理/评估/技术防护/运营/合规), 区分MCP治理即代码与computer use治理风险 | starter.ipynb TODO6 (enterprise_security_check+marketing_governance_analysis) + practice.md drill D4 worked-faded + tutorial.ipynb Socratic追问MCP vs computer use治理差异 | solution.ipynb TODO6后测 + MCP/computer use治理工具设计方案 | 5层架构检查全通过 + MCP/computer use区分清晰 |

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 1. Feed Up (TLA 是否训练 ILO?)

starter.ipynb的6个TODO + practice.md的4个drill worked-faded是否真正训练了4个ILO?
- 自检: TODO1/3训练ILO1, TODO4训练ILO2, TODO5训练ILO3, TODO6训练ILO4. drill D1->ILO1, D2->ILO2, D3->ILO3, D4->ILO4(综合). 是, TLA与ILO一一对应.

### 2. Feed Back (AT 是否测量 ILO?)

solution.ipynb后测 + tutorial.ipynb student_model.json + 9用例分级全对 + 闭环断链识别 + 5层架构检查, 是否真正测量了4个ILO?
- 自检: solution后测直接跑通代码=测量ILO1-4的代码能力; 9用例分级测量ILO2的知识; 闭环断链识别测量ILO3的诊断能力; 5层架构+MCP/computer use区分测量ILO4的综合设计能力. 是, AT与ILO对齐.

### 3. Feed Forward (不经 TLA 能过 AT 吗? 若能=对齐失败!)

学生不写starter.ipynb的6个TODO, 不做drill D1-D4, 直接看solution.ipynb抄答案能过后测吗?
- 自检: 抄solution.ipynb能让代码跑通, 但tutorial.ipynb的Socratic追问 (Govern为什么贯穿/EU+中国能否替代/5环节断链在哪/MCP vs computer use差异) 无法蒙混, student_model.json会暴露弱项. 9用例分级中的情感分析工作场所分支 (Article 5禁止) 也需要真正理解. 因此不经TLA难以过AT, 对齐成功.

## mastery 阈值

- ILO1: scan_nist_rmf跑通且18控制项全覆盖, 掌握度>=80%
- ILO2: 9用例三框架分级9/9正确
- ILO3: 闭环断链识别>=80%
- ILO4: 5层架构检查全通过 + MCP/computer use区分清晰

未达mastery的ILO触发practice.md weak_loop (回退上一drill + 补充worked example).
