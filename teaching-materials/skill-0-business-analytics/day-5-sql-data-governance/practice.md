# Day 5 刻意练习 - 数据治理与 SQL (v6.0)

## skill_target
能在真实 sqlite3 + pandas.read_sql 环境下, 独立设计电商营销数据库 Schema (6 表 + 主外键 + 约束 + 范式化 3NF), 用 SQL DQL (JOIN / GROUP BY / 窗口函数 / CTE / 子查询) 完成 RFM 52/49/31/45 客户分群, 并执行六维数据治理审计 (准确性/完整性/一致性/及时性/唯一性/有效性), 输出可复现的 SQL + DataFrame 分析报告.

## diagnostic (前测 3 道, 检测先备)
1. 给定客户订单 CSV (含重复手机号/缺失金额/格式混乱), 写出 3 条 SQL 或 pandas 检测语句, 识别违反了哪几个数据质量维度.
2. 用 sqlite3 创建 orders 表: order_id 主键 / customer_id 外键 / amount CHECK > 0 / created_at DEFAULT CURRENT_TIMESTAMP. 写完整 DDL.
3. 解释 RFM 52/49/31/45 四组客户的消费特征差异, 写出用窗口函数计算 R/F/M 排名的 SQL 思路.

## subskills
- S1: SQL Schema 设计与范式化 (1NF/2NF/3NF + 约束 + 索引)
- S2: SQL DQL 多表查询与聚合 (JOIN / GROUP BY-HAVING / 窗口函数 / CTE / 子查询)
- S3: 六维数据治理审计与 RFM 分群 (准确性/完整性/一致性/及时性/唯一性/有效性 + RFM 52/49/31/45)

## drills

### drill D1 (Schema 设计)
drill_id: D1
difficulty: 3
reps_required: 3
feedback_rule: 若 sqlite3 CREATE TABLE 缺 PRIMARY KEY / FOREIGN KEY / CHECK / DEFAULT 任一类, 反馈"回到 Schema: 该约束缺失会导致哪种数据异常? 重写 DDL 并预测一条会触发约束的 INSERT"; 若违反 3NF, 反馈"哪个字段冗余? 拆出关联表"; 用 sqlite3 + pandas.read_sql 实测验证
worked_faded: 阶段1 完整示范 - 给出 customers 表完整 DDL 含 5 类约束; 阶段2 部分填空 - 给出 products 表骨架, 学生填 PRIMARY KEY 与 FOREIGN KEY; 阶段3 独立解 - 学生独立设计 order_items 表 (复合主键 + 双外键 + CHECK)

### drill D2 (DQL 查询与 RFM)
drill_id: D2
difficulty: 4
reps_required: 3
feedback_rule: 若 JOIN 缺 ON 或 GROUP BY 缺 HAVING, 反馈"用 sqlite3 跑这条 SQL, 看报错或笛卡尔积行数; 用 pandas.read_sql 验证返回 DataFrame 的 shape"; 若 RFM 窗口函数写错, 反馈"RANK 与 DENSE_RANK 并列时差异? 写两条 SQL 对比"; 若 RFM 52/49/31/45 阈值没依据, 反馈"阈值从业务来还是分位数来? pandas.describe 看分布"
worked_faded: 阶段1 完整示范 "某客户买了什么产品" (3 表 INNER JOIN); 阶段2 填空 - 按品类聚合 GMV (GROUP BY + HAVING); 阶段3 独立 - 用窗口函数 + CTE 实现 RFM 排名与 52/49/31/45 分群

### drill D3 (数据治理审计)
drill_id: D3
difficulty: 5
reps_required: 3
feedback_rule: 若六维审计漏维度, 反馈"六维 (准确性/完整性/一致性/及时性/唯一性/有效性) 漏了哪维? 用 SQL COUNT(DISTINCT) / IS NULL / strftime 各写一条检测"; 若 RFM 分群报告无修复建议, 反馈"检测出问题后, 数据治理的闭环是修复 - 写 3 条 UPDATE / 约束 / 索引建议"; 引用 DAMA-DMBOK 数据治理框架
worked_faded: 阶段1 完整示范唯一性检测 (COUNT(*) vs COUNT(DISTINCT customer_id)); 阶段2 填空完整性检测 (每字段 IS NULL 比例); 阶段3 独立完成六维审计 + RFM 52/49/31/45 分群 + 修复建议报告

## interleaving (A1B1C1 明文交叉, 不块状)
- A = Schema 设计 (D1), B = DQL 查询 (D2), C = 数据治理审计 (D3)
- 交叉排布: A1 (D1 阶段1) → B1 (D2 阶段1) → C1 (D3 阶段1) → A2 (D1 阶段2) → B2 (D2 阶段2) → C2 (D3 阶段2) → A3 (D1 阶段3) → B3 (D2 阶段3) → C3 (D3 阶段3)
- 禁止块状练完 A1A2A3 再练 B - 必须按 1-2-3-1-2-3-1-2-3 跨子技能切换, 触发提取练习与交叉干扰 (Butler 2010; interleaving A1B1C1 明文)

## progressive_project
单一电商营销数据库项目贯穿全单元, 分 3 里程碑交付:
- M1: 创建 6 表 Schema (customers/products/categories/orders/order_items/campaigns) + 插入营销数据 (200 客户/50 商品/500 订单)
- M2: 用 SQL 完成 6 个分析查询 (品类 GMV / 客户购买路径 / 热销排名 / 营销活动 ROI / RFM 52/49/31/45 排名 / 月度趋势)
- M3: 数据治理审计报告 (六维度检测 + Great Expectations 风格期望规则 + 修复建议)

## retry_policy
- 每个 drill 阶段3 (独立解) 必须连续 2 次通过 (自评 + 同伴评) 才算掌握
- 失败 1 次: 回阶段2 复看 worked example, 重做阶段3
- 失败 2 次: 触发 weak_loop, 回退到上一 drill + 补充 worked example
- 每周最多 3 次 retry, 防止"刷题" - 掌握是阈值不是次数

## weak_loop
连续 2 次失败触发弱项循环:
1. 暂停当前 drill, 回退到上一 drill 阶段2 (部分填空)
2. 补充 worked example: 完整 SQL 解题注解 + 数据治理审计模板
3. 重新做 student_model.json 标记的盲点 (sqlite3 DDL / JOIN / RFM / 六维审计)
4. 通过后回原 drill 阶段3, 连续 2 次过才算掌握
