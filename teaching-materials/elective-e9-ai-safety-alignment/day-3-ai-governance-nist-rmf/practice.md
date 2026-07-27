# Day 3 刻意练习 (Deliberate Practice) - AI治理框架

> 基于 Ericsson 刻意练习 + MIT OCW CS229 pset0 先测 + Harvard/Stanford Worked-Faded 示例 + CS230 渐进交付

```yaml
skill_target: 能用 pydantic 实现 NIST AI RMF 1.0 合规扫描器 + 三框架风险分级器 (NIST/EU AI Act/中国生成式AI管理办法) + pandas 治理台账与闭环追踪, 并对9个真实营销AI用例 (推荐/文案/定价/客服/画像/竞品/投放/深合/情感) 给出 5层企业AI安全策略落地检查
unit: 选修E9-Day3
algorithm: deliberate_practice (Ericsson) + worked-faded (Harvard/Stanford)
```

## diagnostic (CS229 pset0 式先测, 探测先验知识缺口)

Q1 (先验-NIST四步): NIST AI RMF 1.0 的四步循环是 ______ / ______ / ______ / ______。其中"贯穿全过程而非第一步做完就结束"的是哪一步? 为什么?

Q2 (先验-EU AI Act 4级): EU AI Act 将 AI 系统分为 ______ / ______ / ______ / ______ 4级。AI生成文案需标注"AI生成"对应哪一级? 工作场所情感识别对应哪一级?

Q3 (先验-三框架互补): NIST是"______"(治理方法论), EU AI Act是"______"(法律合规分级), 中国法规是"______"(备案+标识+透明)。三者能否互相替代? 为什么跨国企业需同时满足?

## subskills

- **S1 NIST合规扫描**: 用pydantic定义18个真实控制项schema (Govern-1~5 / Map-1~5 / Measure-1~4 / Manage-1~4), 实现 assess_control + score_to_status + scan_nist_rmf
- **S2 三框架风险分级**: 实现 classify_eu_ai_act (4级) + classify_china_ai_law (备案/标识/透明/知情同意/跨境) + compare_three_frameworks, 识别三框架互补与冲突
- **S3 治理台账+闭环+5层策略**: 用pandas构建 build_governance_ledger + closed_loop_status, 识别"登记->评估->控制->监控->审计"5环节的断链; 落地 enterprise_security_check (L1治理/L2评估/L3技术防护/L4运营/L5合规)

## drills

drill_id: D1
- 子技能: S1
- difficulty: 3
- reps_required: 5
- feedback_rule: 自动比对NIST真实控制项编号 (Govern-1~5/Map-1~5/Measure-1~4/Manage-1~4); 若遗漏GOVERN-2(问责结构)或MEASURE-3(指标追踪)直接判不合格, 因前者是MCP治理即代码的代码化锚点, 后者是garak/PyRIT红队测试的度量归宿; pydantic ValidationError 必须保留字段路径 (loc/__root__) 用于断链定位
- worked_faded (示范-填空-渐退 三阶段):
  - Stage 1 完整示范: 给出 GOVERN-1 完整pydantic模型 + assess_control("GOVERN-1", use_case) 真实代码
  - Stage 2 部分填空: MEASURE-1 模型留 3 处 TODO (description/assess_method/status字段), 学生填
  - Stage 3 独立解: 学生独立实现 MANAGE-4 风险响应控制项的 schema + assess_control

drill_id: D2
- 子技能: S2
- difficulty: 4
- reps_required: 5
- feedback_rule: 自动比对EU AI Act真实条款号 (Article 5禁止/Annex III高风险/Article 50有限风险/最小风险); 检查中国法规映射是否引用真实法规名 (《生成式AI服务管理暂行办法》《算法推荐管理规定》《深度合成管理规定》《个人信息保护法》《数据安全法》); 营销AI用例必须覆盖9个真实场景 (推荐/文案/定价/客服/画像/竞品/投放/深合/情感), 漏1个扣分; 情感分析在工作场所使用属Article 5禁止, 此点错则D2重做
- worked_faded (示范-填空-渐退 三阶段):
  - Stage 1 完整示范: AI自动文案生成 -> EU: 有限风险(Article 50) + 中国: 生成式AI备案 完整分类代码
  - Stage 2 部分填空: AI动态定价 -> EU: 最小风险(若涉保险升Annex III) 留 2 处条件分支 TODO
  - Stage 3 独立解: 学生独立分类 AI情感分析定向 (注意工作场所 vs 非工作场所分支)

drill_id: D3
- 子技能: S3
- difficulty: 4
- reps_required: 4
- feedback_rule: closed_loop_status 必须识别5环节 (登记/评估/控制/监控/审计) 的断链; pandas DataFrame 列必须含 use_case/risk_level/controls/audit_log/closed_loop; 断链报告需引用天道推演"因果链追踪"指出最可能断链点 (常见: 评估->控制脱节, 监控->审计脱节); 5层架构必须映射Day2的5层Prompt Injection防御 (L3技术防护层=Day2已实现)
- worked_faded (示范-填空-渐退 三阶段):
  - Stage 1 完整示范: build_governance_ledger + 1个营销用例完整闭环代码
  - Stage 2 部分填空: closed_loop_status 留 5 处断链判定 TODO
  - Stage 3 独立解: 学生独立完成 enterprise_security_check (L1-L5全5层)

drill_id: D4
- 子技能: S1+S2+S3 综合
- difficulty: 5
- reps_required: 3
- feedback_rule: MCP治理即代码 vs computer use治理风险必须区分"事前自动拦截"vs"UI操作权限/可逆性/审计粒度"; 必须映射NIST对应控制项 (GOVERN-2问责/MANAGE-4风险响应/MEASURE-3指标追踪/MANAGE-3第三方风险); 漏MCP或computer use任一概念即D4重做
- worked_faded (示范-填空-渐退 三阶段):
  - Stage 1 完整示范: MCP合规检查Agent + NIST GOVERN-2 完整映射示例
  - Stage 2 部分填空: computer use权限矩阵留 4 处 TODO (权限/可逆性/审计粒度/隔离性)
  - Stage 3 独立解: 学生独立设计企业MCP+computer use混合治理工具

## progressive_project (CS230 式渐进交付)

- **Proposal (Day3当天提交)**: 选择1个真实企业营销AI系统 (推荐/文案/定价/客服/画像/竞品/投放/深合/情感 9选1), 写300字proposal: 该系统在三框架下风险分级是什么? 治理闭环5环节哪里最可能断链? 对应天道推演风险路径是什么?
- **Milestone (Day3+3天)**: 提交 pydantic 18控制项schema + 该用例的三框架风险分级代码 (跑通)
- **Final (Day3+7天)**: 提交完整治理台账 + 5层安全策略落地检查 + MCP/computer use治理升级方案 (跑通 + 300字分析)
- **Poster (Day3+10天)**: 1页A3海报: 三框架对比矩阵 + 9用例风险热力图 + 治理闭环断链热力图

## interleaving (交叉排布, 不块状)

按 A1B1C1...B2C2A2...C3A3B3 模式交叉练习3子技能, 避免块状疲劳, 促进迁移:
- 第1轮: A1(D1-stage1 NIST合规) -> B1(D2-stage1 EU+中国分级) -> C1(D3-stage1 台账闭环)
- 第2轮: B2(D2-stage2 定价填空) -> C2(D3-stage2 闭环断链填空) -> A2(D1-stage2 Measure填空)
- 第3轮: C3(D3-stage3 5层独立) -> A3(D1-stage3 Manage独立) -> B3(D2-stage3 情感分析独立)
- 综合轮: D4 (MCP+computer use综合) 在A3B3C3全通过后解锁

## retry_policy (CS230 式)

- 10 free late days (整个Day3学习周期, 不需理由, 自动生效)
- 任何drill失败可重试, **不扣分** (mastery-oriented, 不是ranking-oriented)
- 重试时worked_faded自动回退到Stage 1 (完整示范) 重新走一遍

## weak_loop (连续2次失败触发)

若同一drill连续2次未通过:
1. 自动回退到上一难度drill (D4->D3, D3->D2, D2->D1; D1则补worked example)
2. 推送补充worked example (NIST AI RMF官网示例 / EU AI Act Annex III真实案例 / 中国生成式AI备案实操案例)
3. 强制进入student_model.json的weak_topic字段, tutorial.ipynb的Socratic loop会优先追问该弱项
4. weak_loop解除条件: 回退drill连续2次满分, 才能回原drill
