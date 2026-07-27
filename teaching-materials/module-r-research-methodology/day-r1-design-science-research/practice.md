---
unit: U-R1
title: 设计科学研究（DSR）刻意练习
skill_target: 能用 pydantic 将一个真实 AI 系统建模为 DSR artifact，并用 pandas 按 Hevner 七准则结构化评估，输出可复用的设计原则
---

# U-R1 刻意练习（Deliberate Practice, Ericsson 1993 + MIT/Harvard pedagogy）

> 本练习以 `starter.ipynb` / `solution.ipynb` 的 NSW 真实 RCT 营销 Agent 实例为靶子，
> 以 `data/README.md` 的 causaldata NSW（445 样本, ATE=1794.34）与 LangGraph 三节点 Agent 为真实数据/库锚点。
> 目标不是"做完 TODO"，而是把"做了一个系统"重构为"产出可复用设计原则"的 DSR 认知跃迁。

## diagnostic（先测，CS229 pset0 风格，3 题）

> 提交前自答，不许查 notes.md / 不许问 LLM。每题 < 60 秒。

1. **概念辨析**：March & Smith (1995) 的四种 artifact 类型（constructs/models/methods/instantiations）
   中，"营销因果图模型 treat->re78"属于哪一种？"基于 GraphRAG 的营销知识增强检索系统"属于哪一种？
   若你的 Capstone 同时包含两者，哪一个是 DSR 的"主贡献 artifact"？
2. **rigor vs design 张力**：Hevner 七准则中准则 5（研究严谨性）与准则 2（问题相关性）冲突时，
   你会优先牺牲哪一侧？给出一个**真实工程场景**说明你的取舍（不要泛泛而谈）。
3. **Peffers 六步回溯**：给定 NSW ATE=1794.34 这一评估结果，回溯到 Peffers Step 2（目标定义）应是什么？
   若 Step 5 评估结果与 Step 2 目标不对应，这是哪一条 Hevner 准则失败？

## subskills（拆 3 个子技能）

- **S1 Artifact Schema 建模**：用 pydantic 把 Peffers 六步定义为类型安全的 ArtifactSpec，每步 Field 必填且有 validation
- **S2 七准则结构化评估**：用 pandas DataFrame 给七准则打 1-5 分 + 写 evidence，能算 rigor/design 平衡分
- **S3 设计原则抽取**：从 Step 6 Communication 反推可复用原则（原则/依据/泛化性三件套），不是工程总结

## drills（>=3 个，含 difficulty / reps_required / feedback_rule / worked-faded 三阶段）

### drill_id: D1 — Artifact Schema 建模（constructs/models/methods/instantiations 四型映射）
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 用 pydantic ValidationError 检验 schema；若 `ArtifactType` 枚举未包含 March & Smith 四型即 FAIL；引用真实库 `pydantic.BaseModel` + `enum.Enum`，artifact_name 必须出现 "营销Agent" 或 "GraphRAG" 之一才领域锚定
- **worked_faded**:
  - *Worked（完整示范）*：教练给出 `ArtifactType(Enum)` + `ConstructArtifact(BaseModel)` 完整代码，并实例化"营销知识多模态表示框架"作为 construct
  - *Faded（部分填空）*：给出 `ModelArtifact` 骨架，学生填 `relationships: list[str]` 字段并把"营销因果图模型 treat->re78"实例化
  - *Independent（独立解）*：学生独立定义 `MethodArtifact` + `InstantiationArtifact`，并把 GraphRAG 系统实例化，要求 `theory_basis` 字段引用 ReAct/DSR/因果推断理论之一
- **通过判据**：4 种 artifact 类型全部 schema 化 + 实例化，pydantic.validate 通过

### drill_id: D2 — Hevner 七准则 pandas 评估（rigor vs design 张力）
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: DataFrame 必须为 7 行 4 列（criterion/score_1_5/evidence/weakness）；引用真实数据 NSW ATE=1794.34 作为准则 3 评估证据；准则 5 evidence 必须引用 Imbens & Rubin (2015) 潜在结果框架；若 rigor 侧（准则 5）与 design 侧（准则 2）分数差 >2 即触发 weak_loop
- **worked_faded**:
  - *Worked*：教练示范准则 1（artifact 贡献）+ 准则 5（严谨性）两行完整填充，含"LangGraph 三节点 Agent"作为 instantiation 证据
  - *Faded*：学生填准则 2（问题相关性）+ 准则 3（设计评估）两行，证据必须含 "NSW RCT" 或 "causaldata"
  - *Independent*：学生独立完成准则 4/6/7 三行，准则 6（设计即搜索）必须列出至少 1 个被否决的替代方案（如"全规则策略 vs ReAct"）
- **通过判据**：7 行全填 + rigor/design 平衡分（准则 5+准则 1 平均 - 准则 2+准则 3 平均）的绝对值 < 1.5

### drill_id: D3 — 设计原则抽取（从工程经验到可复用知识）
- **difficulty**: 5
- **reps_required**: 2
- **feedback_rule**: 每条设计原则必须三件套（principle / rationale / generalizability）；rationale 必须引用 Hevner 准则编号；generalizability 必须说明"能否迁移到非营销领域"（如 R&D / 采购 ClawBot）；若原则只是"我们用了 LangGraph"即 FAIL（这是工程描述不是原则）
- **worked_faded**:
  - *Worked*：教练示范"因果证据优先"原则：principle=策略生成前必须先做因果效应估计；rationale=Hevner 准则 5（严谨性，潜在结果框架）；generalizability=可迁移至采购供应商选择 Agent
  - *Faded*：学生补"多 Agent 仿真作为演示高级形式"原则的 rationale 和 generalizability
  - *Independent*：学生独立产出第 3、4 条原则，至少一条来自天道推演同构映射（局势感知/沙盘模拟/概率评估之一）
- **通过判据**：>=4 条原则 + 三件套完整 + 至少 1 条可跨领域迁移

## progressive_project（CS230 式 proposal -> milestone -> final -> poster）

- **proposal（Day 1）**：选你的 Capstone 方向，写 1 页 DSR problem statement（Peffers Step 1），引用至少 3 篇文献
- **milestone（Day 3）**：提交 pydantic `DSRArtifact` schema 定义 + 营销 Agent 系统实例化代码（跑通 pydantic.validate）
- **final（Day 7）**：提交完整 `solution.ipynb` 风格 notebook：6 步全填 + Hevner 七准则 DataFrame + 4 条设计原则
- **poster（Day 10）**：1 页 poster，左半 artifact + 评估数字（ATE/评分），右半设计原则 + 跨领域迁移路径

## interleaving（交叉排布，非块状）

> 每天不连续练同一子技能。建议交叉顺序（A=D1 schema, B=D2 七准则, C=D3 原则）：
>
> **Day1: A1 → Day2: B1 → Day3: C1 → Day4: A2 → Day5: B2 → Day6: C2 → Day7: A3B3C3 混合复盘**
>
> 不要先连做 3 次 D1 再做 D2 -- 那是块状练习，迁移效果差 30%（Bjork 1979 desirable difficulty）。

## retry_policy（CS230 式 retry，失败不罚分）

- 10 free late days（无需理由，自动生效）
- 每个 drill 失败可重试，**重试不扣分**，但必须提交"上次错在哪 + 这次改了什么"的 50 字反思
- 连续 2 次失败触发 `weak_loop`

## weak_loop（连续 2 次失败触发弱项循环）

1. 回退到上一难度 drill（D3 → D2，D2 → D1）
2. 重做该 drill 的 Worked 阶段（完整示范），口头复述教练的每一步推理
3. 补充 1 个 worked example（教练新写，非原题）
4. 通过后才能回到原 drill 的 Faded 阶段

## 反思与迁移

- 完成后写 300 字："我的 artifact 在 Hevner 七准则中哪一条最弱？如何改进？"（与 notes.md 作业对齐）
- 迁移测试：能否把 DSR 六步框架套用到本博士项目其他模块（如 R2 行动研究、R3 混合方法）？写出 1 个跨模块映射。

---

*本文件遵循 Ericsson 刻意练习原则 + CS229/CS230 渐进交付 + Bjork desirable difficulty。feedback_rule 全部锚定本单元真实数据集（causaldata NSW）与真实库（pydantic/pandas/LangGraph）。*
