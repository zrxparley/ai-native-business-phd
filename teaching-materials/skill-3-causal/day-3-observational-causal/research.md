# Day 3 研究产出层 (v7.0): 观测因果推断 (PSM + IV + DML)

> v7.0 在 v5.0 真实数据 (NSW+CPS / close_college) + v6.0 学习科学之上, 加一个可发表研究工件 (publishable research artifact): 研究问题 + 贡献声明 + 已有 arXiv 链接 + IMRaD 大纲 + NeurIPS 风格可复现清单 + research-to-practice 翻译。全部锚定本单元真实数据集与真实数字, 不引入模拟数据。

---

## research_question

**核心研究问题**: 在 NSW+CPS 观测对照 (NSW 实验处理组 185 人 + CPS 观测对照组, 公共支撑限制后) 下, 倾向得分匹配 (PSM) 相对朴素均值差能否消除由 `age` / `educ` / `re74` / `re75` 等可观测协变量引起的自选择偏差, 其修正幅度与"后门线性回归"和"双重机器学习 (DML)"的估计差异 (作为函数形式假设的稳健性指标) 是否在 ±10% 以内一致?

可实证子问题: 在 close_college (Card 1995) 数据上, 以 `nearc4` 为 `educ` 的工具变量, 2SLS 估计的 LATE 是否显著高于 OLS 估计 (即 OLS 是否存在由"个人能力"导致的向下偏差)?

---

## contribution

**Delta vs prior work (显式声明)**:

1. **相对 LaLonde (1986) 的 NSW 实验对照分析**: LaLonde 用 NSW 随机对照估计培训效应, 本单元换用 **NSW 处理组 + CPS 观测对照组** (`causaldata.cps_mixtape`), 显式构造可观测混杂下的自选择偏差, 在 `solution.ipynb` 上同时输出朴素估计 / 后门回归 / PSM 三估计对比 -- 让"自选择偏差有多大"成为可量化对象, 而非仅理论描述。

2. **相对 Card (1995) 原始 IV 应用**: Card 用 `nearc4` 估计教育回报, 本单元在 `starter.ipynb` TODO6 中用 DoWhy 的 `iv.instrumental_variable` 方法重做, 并显式对比 IV (LATE) 与 OLS 估计的符号方向, 把"能力偏误"从文字结论变为代码可复现的数字差异。

3. **相对 Chernozhukov et al. (2018, arXiv 1705.07626) 的 DML 理论文**: 原论文在模拟数据上证明 $\sqrt{n}$ 一致性, 本单元在 (可选) `econml.dml.LinearDML` 上对同一 NSW+CPS 数据再估一次, 把 DML 从"理论前沿"翻译为"营销归因可跑代码", 并显式标注 DML 放松**函数形式**但不放松**可忽略性**的边界 -- 这是 PSM/DML 用户最常踩的认知盲点。

4. **方法学增量**: 把 PSM / IV / DML 三方法在同一真实数据集上并列对比, 输出"方法选择决策树", 而非孤立介绍每种方法 -- 弥补 Cunningham《Mixtape》按方法独立成章的横向对比缺口。

---

## linked_paper

**论文 1 (DML, 本单元前沿锚点)**:
- 标题: *Double/debiased machine learning for treatment and structural parameters*
- 作者: Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, Whitney Newey, James Robins
- 年份: 2018 (The Econometrics Journal, Vol 21, Issue 1)
- 链接: https://arxiv.org/abs/1705.07626
- 关联说明: 本单元 `notes.md` "2026 前沿补充" 节直接引用此论文作为 DML 的理论源头; `solution.ipynb` 反思题第 5 题与 DML 不放松可忽略性假设的边界直接对应论文 §2.3 正交化条件; 可选作业"用 econml DML 在 NSW+CPS 上再估一次"是对论文算法 1 (cross-fitting) 的最小复现。

**论文 2 (IV 经典, close_college 数据源头)**:
- 标题: *Aspects of Labour Economics: Essays in Honor of John Vanderkamp* 中的 "Using Geographic Variation in College Proximity to Estimate the Return to Schooling" 一章
- 作者: David Card
- 年份: 1995
- 链接: 数据可通过 `causaldata.close_college` 加载 (https://pypi.org/project/causaldata/)
- 关联说明: 本单元 `starter.ipynb` TODO6 与 `solution.ipynb` 第 6 节直接使用 Card 1995 的 `nearc4` 工具变量, 估计教育对 `lwage` 的因果效应, 是 IV 三条件 (相关性 / 独立性 / 排他性) 的教科书级真实数据应用。

**论文 3 (PSM 真实数据源头, NSW+CPS)**:
- 标题: *Causal Effects in Nonexperimental Studies: Reevaluating the Evaluation of Training Programs*
- 作者: Rajeev H. Dehejia, Sadek Wahba
- 年份: 1999 (Journal of the American Statistical Association, Vol 94, No 447)
- 数据链接: `causaldata.nsw_mixtape` + `causaldata.cps_mixtape` (https://pypi.org/project/causaldata/)
- 关联说明: 本单元 PSM 上机 (TODO4-5) 用的就是 Dehejia & Wahba 整理的 NSW 处理组 + CPS 观测对照组, 15992 人 CPS 全样本经公共支撑限制 (age ≤ 40, re75 ≤ 10000) 后与 185 人 NSW 处理组合并, 是 PSM 在"严重失衡观测对照"场景下消除自选择偏差的最经典案例。

---

## imrad_outline

### Introduction
- **动机**: 数字营销与平台经济中, 大部分"是否收到优惠券 / 是否被推荐 / 是否看到广告"的处理变量并非随机分配, A/B 测试成本高或受合规约束, 准实验方法 (PSM / IV / DiD / RDD) 与 DML 成为观测数据因果推断的主力工具。
- **Gap**: 现有教学材料 (Cunningham《Mixtape》, Huntington-Klein《The Effect》) 按方法独立成章, 缺乏"同一真实数据集上多方法横向对比 + 自选择偏差可量化"的训练。
- **贡献**: 本单元在 NSW+CPS + close_college 两个真实数据集上, 让朴素估计 / 后门回归 / PSM / IV / DML 五估计并列对比, 把"自选择偏差有多大""LATE vs ATE 差多少""DML 放松了什么没放松什么"全部变为代码可复现的数字。

### Methods
- **数据**: `causaldata.nsw_mixtape` (NSW 实验处理组, 185 人) + `causaldata.cps_mixtape` (CPS 观测对照组, 全样本 15992 人, 公共支撑限制 `age<=40 & re75<=10000`) + `causaldata.close_college` (Card 1995, `nearc4` 工具变量)。
- **处理变量 (PSM)**: `treat` (是否参加 NSW 培训 -> 营销映射: 是否收到优惠券); **结果**: `re78` (1978 收入 -> 营销映射: 转化率/GMV); **协变量**: `age` / `educ` / `black` / `hisp` / `marr` / `nodegree` / `re74` / `re75`。
- **处理变量 (IV)**: `educ` (受教育年限 -> 营销映射: 推荐次数); **结果**: `lwage` (对数工资); **工具**: `nearc4` (是否住近四年制大学 -> 营销映射: 是否有线下门店); **外生协变量**: `exper` / `black` / `smsa` / `south` / `married`。
- **识别策略 (PSM)**: Rosenbaum & Rubin (1983) 可忽略性 + Logistic 倾向得分 + 1:1 匹配 + 标准化均值差 < 0.1 平衡检查。
- **识别策略 (IV)**: 2SLS, 第一阶段 `educ ~ nearc4 + controls`, 第二阶段 `lwage ~ fitted_educ + controls`; 估计量为 LATE, 仅对 compliers 有效。
- **识别策略 (DML, 可选)**: `econml.dml.LinearDML`, ML 模型估计 $E[T|X]$ 与 $E[Y|X]$, 交叉拟合 (cross-fitting) 避免过拟合, 正交化保证 $\sqrt{n}$ 一致性。
- **反驳检验**: DoWhy `placebo_treatment_refuter` -- 安慰剂处理下新估计应接近 0。

### Results (预期 / 已得核心发现)
- **朴素估计 (观测对照)**: `naive_ate = re78[treat=1].mean() - re78[treat=0].mean()`, 因 CPS 对照组协变量与 NSW 处理组严重失衡, 朴素估计包含自选择偏差。
- **PSM 估计**: DoWhy `backdoor.propensity_score_matching` 给出去偏后 ATE; 与朴素估计的差值即为"可观测自选择偏差大小"。
- **后门回归**: `backdoor.linear_regression` 作为方法稳健性参照; 若与 PSM 接近, 说明线性函数形式假设不主导结论。
- **IV 估计**: `iv.instrumental_variable` 给出教育对 `lwage` 的 LATE; 若 IV > OLS, 暗示 OLS 存在能力偏误 (向下偏差)。
- **安慰剂反驳**: 新估计应接近 0, 否则方法在虚假处理上"发现"效应, 估计不可靠。
- **DML (可选)**: 在 NSW+CPS 上 DML 估计与 PSM 的差异反映函数形式假设的影响; 差异小 = 结论对函数形式稳健。

### Discussion
- **贡献边界**: PSM 与 DML 仅消除可观测混杂, 不放松可忽略性 -- 若有未观测混杂 (如个人上进心 / 购买意向), 仍需 IV; IV 估计的是 LATE 而非 ATE, 外推到非 compliers 不可靠。
- **局限**: NSW+CPS 公共支撑限制 (`age<=40 & re75<=10000`) 是启发式, 不同限制下估计会变; `nearc4` 的排他性约束在 2026 年的居住自选择下可能不成立 (近大学家庭可能本身教育偏好高)。
- **未来工作**: 把 DML 升级为因果森林 (`econml.dml.CausalForestDML`) 估计异质处理效应 (HTE); 把 IV 扩展为弱工具变量稳健估计 (Anderson-Rubin 检验); 在营销真实数据上做 PSM-DID 组合设计。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **Code**: 完整代码在 `solution.ipynb` (8 cells, 6 TODO 全部填好可跑通); `starter.ipynb` 为 TODO 填空版脚手架 (8 cells, 6 个 TODO 占位)。
- [x] **Data**: 真实数据集 `causaldata.nsw_mixtape` (NSW 实验处理组, 185 人) + `causaldata.cps_mixtape` (CPS 观测对照组, 15992 人) + `causaldata.close_college` (Card 1995 IV 数据), 通过 `pip install causaldata` 加载, 来源 https://pypi.org/project/causaldata/, 许可见 causaldata 包文档。
- [x] **Seeds**: 随机种子 `random_state=42` (PSM 匹配与 DML 交叉拟合均显式设置, 保证可复现)。
- [x] **Environment**: Python 3.10+, 关键库版本 `dowhy>=0.8`, `econml>=0.15` (可选 DML), `statsmodels>=0.14` (2SLS 手动实现), `causaldata>=0.1.3`, `scikit-learn>=1.3`。
- [x] **Preregistration**: 本单元 `alignment.md` 已声明 ILO (学习目标) 与 AT (评估任务), 等价于 hypothesis 预注册: "PSM 估计应显著低于朴素估计, 差值反映自选择偏差大小"; 可上传至 OSF (https://osf.io/) 作为教学预注册 DOI。
- [x] **FAIR**: 数据可发现 (PyPI 索引) / 可访问 (pip install) / 可互操作 (pandas DataFrame 标准格式) / 可重用 (开源许可); 代码与笔记本可重用 (本仓库教学材料, 课堂使用)。
- [x] **Randomization check**: 公共支撑限制后协变量平衡检查 (标准化均值差 < 0.1) 作为 PSM"准随机化"的诊断。

---

## research_to_practice

本单元研究产出可翻译为三类实践工件:

1. **HBS Working Paper -> HBR Article**: 把"NSW+CPS 上 PSM 修正自选择偏差的幅度"案例改写为 HBR 文章《当 A/B 测试做不了时: 用观测数据做营销因果归因的 3 个陷阱》, 面向 CMO / 增长负责人, 把朴素估计 vs PSM vs DML 的差异翻译为"你的归因模型可能高估优惠券效应多少"。

2. **MIT Sloan Teaching Case**: 以 close_college IV 案例为模板, 写《线下门店作"是否被推荐"的工具变量: 某零售品牌 LATE vs ATE 外推风险》, protagonist 为 Head of Growth, tension 在"门店覆盖区域用户与非覆盖区域用户的 compliers 差异"。

3. **企业白皮书 (Consulting Deliverable)**: 把 PSM / IV / DML 三方法决策树 + DoWhy 代码片段打包为《观测因果推断实操指南》, 给企业数据科学团队作为 methodology playbook; 配套 1-day workshop (lecture + lab + code review), 输出原型 `notebook + decision_tree.pdf + refutation_report.html`。

研究 -> 实践的翻译遵循 Imperial MSc BA 项目"做中学"传统: 研究问题必须是 partner 企业真实问题, 数据必须是企业提供的真实 (脱敏) 数据, 交付物必须是企业可立即部署的工件, 而非仅学术论文。本单元的 PSM/IV/DML 三方法在同一真实数据上并列对比, 直接对应企业"在多种方法中选择最合适的一种"的实操需求。
