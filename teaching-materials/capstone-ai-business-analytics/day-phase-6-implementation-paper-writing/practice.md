# Phase 6 刻意练习 (Deliberate Practice, Ericsson + MIT/Stanford)

> **本单元核心可观察技能 (skill_target)**：能用 DSR 六步框架（Hevner 2004 / Peffers 2007）把 Phase 1-5 的 LangGraph Agent + DoWhy 因果产出整合为可发表的 IMRaD 论文 artifact，并用 langsmith @traceable 构建可复现 trace 存档、用 statsmodels/scipy 跑统计检验、用 deepeval LLM-as-a-judge 五维度评分。

---

## 一、Diagnostic 先测题 (CS229 pset0 式, 探测先验缺口)

> 规则：开卷但限 25 分钟，不查 LLM；答不出无惩罚，仅用于定位弱项。

**Q1 (DSR/IMRaD 映射)**: DSR 六步框架中"Step 5 评估"应映射到 IMRaD 的哪个章节？为什么不能映射到 Methods？(提示：DSR Step 3 = 设计开发，Step 5 = 评估)

**Q2 (统计报告)**: 给定 NSW RCT (N=445, treatment=185, control=260) 的 treatment 组 1975 年收入均值 \$8345、control 组 \$7923、pooled SD \$6218，请用 statsmodels/scipy 写出独立样本 t 检验 + Cohen's d 的 APA 第 7 版表述（含 t、df、p、d、95%CI）。

**Q3 (可复现研究)**: 若他人要复现你的 Agent 系统，仅给 GitHub 代码够吗？请列出 langsmith @traceable trace 存档需要保存的 4 类元数据（提示：API 版本、模型版本、prompt hash、tool call 序列）。

---

## 二、subskills 拆解 (3 个子技能, 对应 Phase 6 三大能力)

- **A. DSR-to-IMRaD 写作 (subskill A)**：把 DSR 六步映射到 IMRaD 七节，撰写含 artifact 描述的 3000-5000 字论文草稿
- **B. 可复现 trace + LLM-as-a-judge (subskill B)**：用 langsmith @traceable 追踪 Phase 1-5 执行链，用 deepeval BaseMetric + GEval 五维度评估论文质量
- **C. 统计报告 APA 化 (subskill C)**：用 statsmodels + scipy 在 NSW RCT 上跑 t 检验/Cohen's d/卡方检验，输出 APA 第 7 版 Results 段

---

## 三、Drills (>=3 个, 每个 drill 三阶段 worked-faded: 完整示范 -> 部分填空 -> 独立解)

### drill_id: D1
- **subskill**: A (DSR-to-IMRaD 写作)
- **difficulty**: 3 (1-5)
- **reps_required**: 4
- **feedback_rule**: 领域特定 -- 检查 DSR Step → IMRaD 节的映射完整性；漏掉 DSR Step 4 (演示) 直接判 FAIL（演示必须出现在 Methods 的 system architecture 子节）；天道推演×多Agent仿真 必须出现在 Discussion 而非 Introduction
- **worked_faded** (三阶段):
  - *Stage 1 (完整示范)*：给出已填好的 DSR→IMRaD 映射表（Step1→Intro, Step2→Intro, Step3→Methods, Step4→Methods/Results, Step5→Results, Step6→Discussion）
  - *Stage 2 (部分填空)*：给出表骨架，学生填 Step 4 与 Step 6 两行的 IMRaD 节名 + 字数
  - *Stage 3 (独立解)*：学生从零撰写 Discussion 草稿 600-800 字，必须含 DSR Step 6 传播要素 + 天道推演×多Agent仿真 500 字特色章节
- **success_criteria**: Stage 3 论文 Discussion 段含 ≥3 个 DSR 传播要素（arXiv/会议/期刊）+ 天道推演同构表 (局势感知/因果链/沙盘模拟/概率评估/最优路径)

### drill_id: D2
- **subskill**: B (可复现 trace + LLM-as-a-judge)
- **difficulty**: 4 (1-5)
- **reps_required**: 5
- **feedback_rule**: 领域特定 -- langsmith @traceable 必须包裹 Phase 3 的 LangGraph Agent 节点（不是普通函数）；deepeval GEval 必须使用自定义 criteria（IMRaD 完整性/统计依据/DSR 描述/可复现性/天道推演视角）五维度；缺 trace hash 直接 retry
- **worked_faded** (三阶段):
  - *Stage 1 (完整示范)*：给出 `@traceable` 装饰 LangGraph node + deepeval BaseMetric 子类的完整代码
  - *Stage 2 (部分填空)*：TODO 填空版 -- 学生补全 `def measure(self, test_case)` 与 `GEval(model="deepseek", criteria=...)` 的 criteria 字段
  - *Stage 3 (独立解)*：学生独立写 5 个 BaseMetric 子类（IMRaD/Stats/DSR/Reproducibility/TianDao），跑论文草稿评估并输出 5 维评分 JSON
- **success_criteria**: Stage 3 输出 5 维评分 (0-10)，每维附 1 句改进建议；trace 存档含 ≥4 个 LangGraph 节点调用

### drill_id: D3
- **subskill**: C (统计报告 APA 化)
- **difficulty**: 3 (1-5)
- **reps_required**: 4
- **feedback_rule**: 领域特定 -- NSW RCT (N=445, treatment=185, control=260) 必须用 causaldata 加载，禁止 sim 数据；APA 第 7 版必须含 t(df)=X.XX, p=.XXX, d=X.XX, 95% CI [X.XX, X.XX]；卡方检验必须报 χ²(df, N=445)=X.XX, p=.XXX, φ=X.XX
- **worked_faded** (三阶段):
  - *Stage 1 (完整示范)*：给出 t 检验 + Cohen's d + 95%CI 的完整 statsmodels/scipy 代码与 APA 输出
  - *Stage 2 (部分填空)*：学生补全 `scipy.stats.ttest_ind(...)` 与 `sm.stats.weightstats.ttest_ind(...)` 参数；填 APA 模板字符串
  - *Stage 3 (独立解)*：学生独立在 NSW 上跑 (1) t 检验 (2) Cohen's d (3) 卡方检验 (种族分布)，写完整 Results 段 800-1000 字
- **success_criteria**: Stage 3 Results 段含 3 项统计检验 + APA 表 1（描述统计）+ 表 2（推断统计），无 p-hacking 痕迹

### drill_id: D4
- **subskill**: A (DSR-to-IMRaD 写作 - 进阶)
- **difficulty**: 5 (1-5)
- **reps_required**: 3
- **feedback_rule**: 领域特定 -- 学术发表路线图必须按 arXiv (即时) → ICIS/HICSS (6月) → MIS Quarterly/DSS/IJIM (3-6月) 三层；天道推演×多Agent仿真 必须作为特色章节而非附录；PRISMA 综述必须出现在 Related Work 而非 Introduction
- **worked_faded** (三阶段):
  - *Stage 1 (完整示范)*：给出已完成的 IMRaD 论文骨架 (3000-5000字) + arXiv→会议→期刊 三层路线图
  - *Stage 2 (部分填空)*：学生填 Title 模板 `[方法] for [问题]: A [框架] Approach`、Abstract 150-250 字、Related Work 600-800 字
  - *Stage 3 (独立解)*：学生整合 D1/D2/D3 产出，输出完整 IMRaD 草稿 + 发表路线图 + 20-30 篇 APA 第 7 版参考文献
- **success_criteria**: Stage 3 论文通过 deepeval 五维评估均 ≥7/10；arXiv 预印本上传计划一页可执行

---

## 四、Progressive Project (CS230 式, 渐进交付)

| 阶段 | 交付物 | 占比 | 评审 |
|------|--------|:----:|------|
| Proposal (Week 1) | DSR Step 1-2 + 研究问题 + PRISMA 综述大纲 | 15% | 同伴互评 |
| Milestone (Week 2) | DSR Step 3-4 + LangGraph 系统 + langsmith trace 存档 | 25% | deepeval 自动评 |
| Final (Week 3) | IMRaD 论文 3000-5000 字 + DoWhy ATE + statsmodels APA 报告 | 40% | 教师评分 |
| Poster & Defense | 一页 poster + 2 分钟话术 + 反驳检验 (devil's advocate) | 20% | 公开答辩 |

---

## 五、Interleaving (交叉排布, A1B1C1...B2C2A2...C3A3B3)

> 不块状训练。每天轮换三个 subskill，促进迁移。

**Day 1**: A1 (D1 Stage1) → B1 (D2 Stage1) → C1 (D3 Stage1)
**Day 2**: B2 (D2 Stage2) → C2 (D3 Stage2) → A2 (D1 Stage2)
**Day 3**: C3 (D3 Stage3) → A3 (D1 Stage3) → B3 (D2 Stage3)
**Day 4**: D4 Stage1 → D4 Stage2 → D4 Stage3 (整合 D1-D3 产出)
**Day 5**: 全综合：写完整 IMRaD + 跑 deepeval 五维评估 + arXiv 路线图

**明文交叉顺序**: A1B1C1 B2C2A2 C3A3B3 D4-1 D4-2 D4-3 (5 天 15 个 session)

---

## 六、Retry Policy (CS230 式)

- **10 free late days**: 整个 Phase 6 共 10 天延迟额度，自行分配
- **失败重试不罚分**: D1/D2/D3 Stage 3 若未达 success_criteria，可无限重试，取最高分
- **同伴互评豁免**: Proposal 阶段收到同伴 ≥3 条具体建议，Final 可加 5% (上限 100%)

---

## 七、Weak Loop (连续 2 次失败触发弱项循环)

触发条件：同一 drill 连续 2 次未达 success_criteria。

执行步骤：
1. **回退上一阶段**：从 Stage 3 回退到 Stage 2 (部分填空)，重做 1 rep
2. **补充 worked example**：教师/teaching assistant 提供 1 个完整 worked example (含手写注释)
3. **诊断盲点**：用 `tutorial.ipynb` 的 student_model.json 记录盲点关键词（如"DSR Step4 演示"/"APA 卡方"/"trace hash"）
4. **再挑战 Stage 3**：盲点修复后再尝试；若仍失败，触发 1:1 答疑

**Phase 6 常见弱项循环**：
- 弱项 A1：DSR Step 4 演示被漏掉 → 回退 D1 Stage 2 + worked example "LangGraph node 调用即演示"
- 弱项 B1：deepeval GEval criteria 太泛 → 回退 D2 Stage 2 + worked example "criteria 必须含 IMRaD 五节名"
- 弱项 C1：APA 格式漏 95%CI → 回退 D3 Stage 2 + worked example "ttest_ind + ConfInt 模板"
