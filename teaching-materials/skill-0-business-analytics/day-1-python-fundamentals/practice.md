# 刻意练习 - Python 编程基础 (pandas / numpy / Apache Arrow / Polars)

> v6.0 学习科学层 · Ericsson 刻意练习 5 要素 + MIT 提取/间隔/交叉 + Worked-Faded 渐退示例
> 适用单元: skill-0-business-analytics / day-1-python-fundamentals
> 真实库锚定: pandas (DataFrame/dtypes/groupby/apply), numpy (向量化), Apache Arrow (pandas 2.x 后端), Polars (LazyFrame)

---

## skill_target
能在 60 分钟内, 用 pandas 加载营销数据 (产品/客户/订单), 用控制流+apply 完成 RFM 客户分类, 用 numpy 向量化计算 ROI/AOV/转化率/复购率, 并能口述 pandas 2.x Arrow 后端 vs Polars LazyFrame 的取舍依据。

## subskills
- **S1 - DataFrame 加载与类型治理**: pd.read_csv / dtypes / info / head / describe; 识别前导零丢失 (customer_id str vs int)、日期解析错误、缺失值 NA vs NaN。
- **S2 - 控制流 + apply 向量化 RFM 分类**: 用 if-elif-else + df['col'].apply(func) 实现 R/F/M 三维分群, 解释 apply 比 for 循环快 10-100x 的向量化原理。
- **S3 - 营销指标计算与 IO**: 用 pandas + numpy 聚合计算 ROI / 转化率 / 客单价 AOV / 复购率, 用 to_csv / read_json 读写, 理解 random_state=42 可复现性。

## diagnostic (pset0 式先测, 3 道, 不计分, 仅诊断盲点)
> 规则: 独立完成, 不查文档, 15 分钟。诊断结果决定你从哪个 drill 起步。

- **Q1 (加载)**: 给定 `orders.csv` 含 `customer_id` 形如 `"00123"` (前导零)。写出 pandas 加载代码, 保证 customer_id 读入后仍是 `"00123"` 而非 `123`。若忘了 dtype 参数, 数据会发生什么不可逆损失?
- **Q2 (向量化)**: 下列两段代码哪段快? 为什么? 写出向量化版本的 `df['rfm_label'] = df.apply(rfm_classify, axis=1)` 的替代实现 (提示: np.select / np.where)。
  ```python
  # A
  for i in range(len(df)):
      df.loc[i, 'label'] = rfm_classify(df.loc[i])
  # B
  df['label'] = df.apply(rfm_classify, axis=1)
  ```
- **Q3 (前沿)**: pandas 2.x 的 `dtype_backend="pyarrow"` 与 Polars `LazyFrame.scan_csv().collect()` 在处理 5GB 用户行为日志时, 各自的内存策略是什么? 为什么 Arrow 后端能"零拷贝"传给 DuckDB? (开放题, 测你能否说出列式存储 + Arrow C ABI)

---

## drills (>=3, 每含 drill_id/difficulty/reps_required/feedback_rule/worked_faded)

### drill_id: D1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 若 dtype 检查漏掉 customer_id 前导零 → 反馈"打开 df.dtypes, 找到 customer_id 列, 它是 int64 还是 object? 哪个会丢前导零? 重读 notes.md 关键回顾 3 的 dtype 行"。若 describe() 只看到数值列 → 反馈"df.describe(include='all') 会暴露 object 列的 unique/top/freq, 你的客户名列有几种唯一值?"。引用 pandas 真实 API, 不直接给代码。
- **worked_faded**:
  - **阶段 1 (完整示范 Worked)**: 演示 `df = pd.read_csv('orders.csv', dtype={'customer_id': str}); print(df.dtypes); print(df.describe(include='all'))` 完整解 + 注释每行作用。
  - **阶段 2 (部分填空 Faded)**: 给 `df = pd.read_csv('orders.csv', dtype={____: ____}); print(df.____())`, 学生填 customer_id/str/dtypes。
  - **阶段 3 (独立解 Independent)**: 学生独立写加载代码, 处理 orders.csv + products.csv + customers.csv 三张表, 全部 dtype 正确。

### drill_id: D2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若 RFM 用 for 循环而非 apply → 反馈"apply 比 for 快 10-100x 的原因是向量化, 你的 for 循环每次都触发 Python 解释器开销。把 rfm_classify 函数保持, 改成 df.apply(rfm_classify, axis=1)"。若 RFM 阈值硬编码无注释 → 反馈"R 阈值 30 天、F 阈值 3 次、M 阈值 500 元是营销行业惯例, 你为什么选这些值? 在函数 docstring 写清楚"。若 apply axis=1 vs axis=0 混淆 → 反馈"axis=1 是逐行, axis=0 是逐列, RFM 是逐行分类, 你选哪个?"
- **worked_faded**:
  - **阶段 1 (完整示范 Worked)**: 演示完整 RFM 函数 + `df['rfm_label'] = df.apply(rfm_classify, axis=1)`, 含 R/F/M 阈值注释和 docstring。
  - **阶段 2 (部分填空 Faded)**: 给函数骨架, 学生填 if-elif-else 分支判断逻辑和 apply 调用。
  - **阶段 3 (独立解 Independent)**: 学生独立实现 RFM 分类, 并用 np.select 重写一遍, 对比两版性能 (用 %timeit)。

### drill_id: D3
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 若 ROI 公式写成 (收入 - 成本) / 成本 但成本为 0 时除零 → 反馈"numpy 会给 inf, 你应该用 np.divide(..., where=cost>0) 或 df['cost'].replace(0, np.nan) 屏蔽"。若复购率漏掉"至少购买 2 次"的分子定义 → 反馈"复购率 = 购买>=2次的客户数 / 总客户数, 你写成订单数比了吗? 用 df.groupby('customer_id').size() >= 2"。若 to_csv 没加 index=False → 反馈"默认会写一列无用 index, 商业交付物必须 index=False, 重读 notes.md 文件 IO 表"。若 random_state 没固定 → 反馈"可复现研究要求 random_state=42, 否则别人跑不出你的结果, 见 notes.md 可复现研究一节"。
- **worked_faded**:
  - **阶段 1 (完整示范 Worked)**: 演示 ROI / AOV / 转化率 / 复购率四指标完整计算 + to_csv(index=False) + read_json 验证 + random_state=42。
  - **阶段 2 (部分填空 Faded)**: 给 ROI/AOV 完整, 学生填转化率/复购率公式 + IO 写出。
  - **阶段 3 (独立解 Independent)**: 学生独立完成 4 指标计算 + IO 双向 (csv + json) + 写一段 300 字分析报告 (各层级客户占比 / ROI 最高产品 / 数据质量问题)。

---

## progressive_project (proposal → milestone → final → poster, MIT CS230 模式)
> 渐进交付脚手架, 每阶段反馈后才能进入下一阶段。

- **proposal (Day 1 上机第 1 小时末提交)**: 选一个真实营销数据集 (Kaggle/UCI/公司脱敏), 写 1 页 proposal: 业务问题、数据规模、拟用 pandas API 列表、预计难点。反馈后进入 milestone。
- **milestone (Day 1 上机第 2 小时末提交)**: 数据已加载, dtypes 治理完成, RFM 分类跑通, 至少 1 个指标 (ROI/AOV/转化率/复购率) 计算正确。反馈后进入 final。
- **final (课后 3 天提交)**: 4 指标全部计算, to_csv + read_json IO 双向, random_state=42 固定, 300 字分析报告。反馈后进入 poster。
- **poster (课后 7 天提交)**: 1 页 A3 海报 (matplotlib seaborn 可选), 含数据流图 + RFM 分布图 + ROI 排行 + 3 条商业建议。同伴互评 (Ed Discussion 模式)。

---

## interleaving (A1B1C1...B2C2A2...C3A3B3 明文交叉顺序, 不块状)
> 不允许"先把 D1 做 3 遍再做 D2"的块状练习。按以下交叉序列训练 (A=D1加载, B=D2 RFM, C=D3 指标):

- **第 1 轮**: A1 (D1 第 1 次) → B1 (D2 第 1 次) → C1 (D3 第 1 次)
- **第 2 轮**: B2 (D2 第 2 次) → C2 (D3 第 2 次) → A2 (D1 第 2 次)
- **第 3 轮**: C3 (D3 第 3 次) → A3 (D1 第 3 次) → B3 (D2 第 3 次)

每轮之间隔 1 天 (间隔重复, 见 schedule.json FSRS-6)。理由: 交叉强迫大脑每次都重新检索"现在该用哪个 API", 而非块状练习的机械重复。Butler 2010 证据: 交叉练习比块状练习在 1 周后保留率高 43%。

## retry_policy (10 late days + 失败不罚)
- 总计 10 个 late days, 任一阶段超期消耗, 用完为止 (MIT CS230 政策)。
- 任一 drill 失败 (低于 mastery_threshold) 不扣分, 不计入 late days, 仅触发 weak_loop。
- 重交上限: 每 drill 最多 3 次重交, 第 3 次仍失败 → 强制 weak_loop。

## weak_loop (连 2 次失败 → 回退 + worked example)
> 触发条件: 同一 drill 连续 2 次未达 mastery_threshold (>=80%)。

- **回退**: 退到上一难度 drill (D3 → D2 → D1; D1 已是最底则停留)。
- **补充 worked example**: 重新走该 drill 的阶段 1 (完整示范), 导师/TA 口头讲解每行, 学生复述。
- **重练**: 阶段 2 (部分填空) 重做 2 次, 再进入阶段 3 (独立解)。
- **记录**: 写入 student_model.json 的 `weak_drills` 字段, 跨单元复用 (Day 2 JSON/API 处理时会优先复习 D1 加载)。

---

## 与本单元 v5.0 文件的映射
- starter.ipynb 的 6 个 TODO 对应 D1 (TODO1-2) / D2 (TODO3-4) / D3 (TODO5-6)
- solution.ipynb 是 D1/D2/D3 阶段 1 (完整示范) 的参考答案 (gated, 做完再看)
- notes.md 关键回顾 1-4 是 worked example 的理论支撑
- reading.md 的 pandas 2.x / Arrow / Polars 链接是 D3 阶段 3 独立解的前沿延伸
