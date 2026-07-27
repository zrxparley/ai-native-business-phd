# 刻意练习 - A/B 测试 (NSW RCT 视角 + CUPED + causaldata)

> Loop Engineering v6.0 学习科学层 · 配套 notes.md / starter.ipynb / solution.ipynb
> 研究依据: Ericsson 刻意练习 5 要素 + MIT OpenLearning (Worked-Faded + Interleaving A1B1C1)

---

## skill_target
能在真实 RCT 数据 (NSW 职业培训实验, causaldata.nsw) 上独立完成 A/B 测试统计分析全流程: 均衡性检验 -> 样本量计算 -> 显著性检验/CI/事后功效 -> CUPED 方差缩减, 并解释每个统计量在 NSW/营销场景中的因果与业务含义 (不混淆"统计显著"与"业务重要")。

## subskills
- **S1 均衡性检验**: 在 NSW RCT 数据上逐变量做 t 检验/χ² 检验, 判断处理组与对照组在 age/education/re75 等协变量上是否均衡 (p>0.05), 论证"随机化消除混杂"使均值差=ATE。
- **S2 样本量与功效**: 给定基线转化率 p1、MDE、α、power, 计算 A/B 测试每组样本量; 做事后功效分析, 识别"p<0.05 但功效不足"陷阱, 不被显著性绑架。
- **S3 CUPED 方差缩减**: 用 re75 作 CUPED 协变量调整 re78, 计算 β=Cov(Y,X)/Var(X) 与方差缩减比 1-ρ², 对比调整前后 t/p/CI, 解释"相同样本量检测更小效应"的工业意义 (Deng et al. 2013 WSDM)。

## diagnostic (前测, 识别弱项, 不计入 AT)
1. 给定 NSW treat=1/0 两组的 age 均值与方差, 写出两样本 t 检验的 H0、t 统计量公式, 并解释 p>0.05 在 RCT 语境下意味着什么 (与 Day 1 观测视角对比)。
2. 营销场景: 基线转化率 5%, MDE=1%, α=0.05, power=0.80, 请估算每组样本量量级 (10²/10³/10⁴/10⁵), 并说明 MDE 减半时样本量约翻几倍。
3. 在 NSW 上用 re75 做 CUPED 调整 re78, 若 Corr(re75,re78)=0.6, 方差缩减比例是多少? 调整后的 t 统计量大约会变几倍? 为什么 re75 不受 treat 影响?

---

## drills

### Drill D1 - 均衡性检验 (ILO1)

drill_id: D1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 若均衡性检验 p<0.05 出现, 提示学生回到 NSW `treat` 列随机性 -- RCT 失败意味着什么? 引用 NSW RCT 设计 (Lalonde 1986 / Dehejia-Wahba 1999) 讨论随机化机制破坏的后果; 若 t 检验公式写错 (如分母用了 SD 而非 SE), 回退到 D1 worked example 重做"两样本 t 检验三步法"; 若学生把"p>0.05 无法拒绝 H0"说成"接受 H0", 引用 notes.md §关键回顾 3 纠正。所有反馈引用 NSW RCT 视角与 A/B 测试两类错误矩阵。
- **worked_faded**:
  - **阶段1 (完整示范)**: 给出 NSW `age` 变量 t 检验的完整 statsmodels/scipy 调用代码 + t 统计量 + p 值 + 解读"p>0.05 => 均衡 => 随机化成功 => 均值差=ATE 无需后门调整"
  - **阶段2 (部分填空)**: 给出 `education` 变量的代码骨架, 学生填入 t_stat 公式 (`(m1-m0)/sqrt(v1/n1+v0/n0)`) 与 p 值解读
  - **阶段3 (独立解)**: 学生独立对 `re75` 做均衡性检验, 并写 50 字结论对比 Day 1 观测视角的不均衡

### Drill D2 - 样本量与功效 (ILO2)

drill_id: D2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若样本量公式记错或量级判断离谱 (>10x), 提示重读 notes.md §关键回顾 2 公式 n=(z_α/2+z_β)²·[p1(1-p1)+p2(1-p2)]/(p2-p1)²; 若学生混淆 α 与 power, 引用 A/B 测试两类错误矩阵 (notes.md 表格) 让其重新标注第一类/第二类错误; 若 MDE 减半样本量翻 2 倍 (而非 4 倍), 提示回到 n ∝ 1/MDE² 的反比平方关系; 若学生说"p<0.05 就上线", 引用 notes.md §关键回顾 3 营销警示 -- 大样本下微小效应也显著, 需看效应大小+CI+业务意义。所有反馈引用 A/B 测试工业实践。
- **worked_faded**:
  - **阶段1 (完整示范)**: 完整示范"基线 5%, MDE=1%, α=0.05, power=0.80"的样本量计算 (statsmodels NormalIndPower.solve_power), 得 n≈8200/组
  - **阶段2 (部分填空)**: 填空"基线 5%, MDE=0.5%"场景, 学生填入 MDE 与 z_beta, 推出 n≈32000 (4 倍)
  - **阶段3 (独立解)**: 独立做营销场景"贴片广告 CTR 基线 2%, MDE=0.1%"估算并解释为何需要 10⁵ 量级; 做事后功效分析 (给定 n=5000, MDE=1%, power=?)

### Drill D3 - CUPED 方差缩减 (ILO3)

drill_id: D3
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 若 CUPED β 公式写错 (如写成 Cov/SD), 提示 β=Cov(Y,X)/Var(X) 不是 Cov/SD; 若方差缩减比写成 ρ 而非 1-ρ², 引用 Deng et al. 2013 WSDM 原文公式; 若学生忘记检查"X 不受 T 影响"假设, 提示回到 RCT 原理 -- re75 是实验前协变量, 不受 treat 影响, 故合法; 若调整后 t 没变大, 提示检查 β 符号与 (X-X̄) 中心化是否正确; 若学生把 CUPED 与后门调整混淆, 引用 notes.md §关键回顾 4 区分"CUPED 是方差缩减不是去偏"。所有反馈引用 NSW re75/re78 与 A/B 测试灵敏度。
- **worked_faded**:
  - **阶段1 (完整示范)**: 完整示范用 re75 做 CUPED 调整 re78 的 numpy 代码 (β=Cov/Var, θ=Y-β(X-X̄)) + 调整前后 t/p/CI 对比表 + 方差缩减比 1-ρ² 计算
  - **阶段2 (部分填空)**: 填空 -- 学生填 β 计算行 (`beta = np.cov(Y,X)[0,1]/np.var(X)`) 与 θ 行 (`theta = Y - beta*(X-np.mean(X))`)
  - **阶段3 (独立解)**: 独立做营销映射"用实验前 7 日活跃度作 CUPED 协变量调整 GMV", 给定 ρ=0.5 计算方差缩减比, 并写 100 字业务建议"相同样本量检测更小效应 -> 节省实验成本"

---

## progressive_project (渐进式交付, 脚手架渐退, MIT Sloan 行动学习风格)
- **M1 (proposal)**: 选定一个 NSW 变量作 A/B 指标 (re78 连续 / re78>0 二值), 提交 1 页方案 (H0/H1/MDE/α/power/样本量预估)
- **M2 (milestone)**: 完成均衡性检验 + 样本量计算 + 显著性检验 (t 检验+比例 Z 检验) + CI + 事后功效, 提交可跑 .ipynb
- **M3 (final)**: 加入 CUPED 方差缩减, 对比调整前后统计量, 写 300 字营销业务建议 (无标准答案, 防抄)
- **M4 (poster)**: 2 分钟话术 -- "假如我是营销负责人, 这个 A/B 测试结果如何决策 (上/不上/继续实验)"

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布, 不块状)
本单元 3 子技能 **不**按 S1->S2->S3 块状练习, 而是 A1B1C1 交叉排布:
- **第1轮 (A1B1C1)**: D1-阶段1 (worked) -> D2-阶段1 (worked) -> D3-阶段1 (worked) -- 各练 1 次, 建立完整示范印象
- **第2轮 (B2C2A2)**: D2-阶段2 (faded) -> D3-阶段2 (faded) -> D1-阶段2 (faded) -- 打乱顺序, 部分填空, 强迫检索
- **第3轮 (C3A3B3)**: D3-阶段3 (independent) -> D1-阶段3 (independent) -> D2-阶段3 (independent) -- 独立解, 顺序再打乱, 巩固迁移
- **跨单元交叉**: 每轮之间穿插 Day 1 (观测因果后门调整) 与 Day 3 (准实验 PSM/DiD) 的旧知识点, 强化"何时用 RCT、何时用准实验"的判断 (ILO4)。
- **理论依据**: interleaving (A1B1C1) 比块状 (AAABBBCCC) 迁移效果更好, Rohrer & Taylor 2007, Taylor & Rohrer 2010 实证支持。

## retry_policy
- 任一 drill 阶段3 (独立解) 失败: 24h 后重试 (间隔重复, 避免短时记忆假象, Butler 2010 retrieval practice)
- 连续 2 次失败: 触发 weak_loop
- 每日最多 3 次重试同一 drill (防止刷题, 与 tutorial.ipynb 限频一致)

## weak_loop (弱项循环, 连续 2 次失败触发)
1. **回退**: 回到该 drill 的阶段 1 (完整 worked example) 重新观看 + 抄写
2. **补充 worked**: 补充一个简化版 worked example (难度降 1 级) -- 例: D3 失败则补"用模拟 ρ=0.3 数据做 CUPED"的小例, D2 失败则补"基线 50%, MDE=10%"的直觉例
3. **重进 faded**: 重新进入阶段 2 (部分填空) -- 必须过才能回阶段 3
4. **Socratic 救援**: 若仍失败, 触发 tutorial.ipynb Socratic 追问 (限 1 次/天) 定位概念盲点, 写入 student_model.json 的 blindspots 列表
5. **跨单元回扣**: 若盲点是"随机化=do 操作", 回扣 Day 1 因果阶梯 L2; 若盲点是"准实验适用条件", 预习 Day 3 PSM/DiD
