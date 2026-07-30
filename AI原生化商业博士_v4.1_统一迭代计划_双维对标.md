# AI原生化商业博士 v4.1 统一迭代计划
# 对标 MSc in Applied Artificial Intelligence + AIBA 双维度

> **编制日期**：2026-07-29
> **基于版本**：v4.0（含13份独立教材，总计约973KB）
> **对标维度一**：Fairfield University MS in Applied Artificial Intelligence（AIBA方向）- 应用层
> **对标维度二**：MSc in Applied Artificial Intelligence 标准学位 - 技术层
> **迭代目标**：在博士级研究深度的同时，补齐应用层实操能力和技术层基础广度，使课程体系同时覆盖商业应用硕士和技术硕士的双重标准

---

## 一、双维度差距分析总览

### 1.1 维度一：AIBA应用层差距（Fairfield课程对标）

| Fairfield课程 | 课程名称 | 现有覆盖 | 差距 |
|:---:|---------|:-------:|:---:|
| - | 统计学基础（含时间序列） | 中等 | ⚠️ |
| DATA 5405 | 商业分析编程基础（Python/R/AI辅助编程） | 中等 | ⚠️ |
| DATA 6500 | AI驱动商业分析（蒙特卡洛/优化） | 浅 | 🔴 |
| DATA 6515 | AI伦理与治理 | 充分 | 🟢 |
| DATA 6505 | 商业分析数据工程 | 中等 | ⚠️ |
| DATA 6510 | 数据设计与分析（SQL/NoSQL/数据仓库） | 中等 | ⚠️ |
| DATA 6545 | 商业AI系统（AI生命周期/AutoML） | 浅 | 🔴 |
| DATA 6540 | 商业智能（Tableau/仪表盘/数据叙事/UI/UX） | 极浅 | 🔴 |
| DATA 6570 | 商业生成式AI应用（无代码/低代码/流程自动化） | 极浅 | 🔴 |

### 1.2 维度二：Applied AI技术层差距

| 技术主题 | 现有覆盖 | 差距 | 与营销关联度 |
|---------|:-------:|:---:|:---:|
| 多智能体系统 | 充分 | 🟢 | 高 |
| Transformer/Attention | 充分 | 🟢 | 高 |
| 迁移学习(Fine-tuning) | 充分 | 🟢 | 高 |
| 强化学习(RLHF部分) | 有章节 | ⚠️ | 中 |
| ML算法(K-Means/RF) | 有代码 | ⚠️ | 高 |
| 知识表示(本体设计) | 有章节 | ⚠️ | 高 |
| 优化算法(梯度下降) | 有代码 | ⚠️ | 高 |
| 生成模型(VAE/GAN/Flow) | 有章节 | ⚠️ | 中高 |
| 推荐系统(Two-Tower) | 有代码 | ⚠️ | 高 |
| 计算机视觉 | 仅提及 | 🔴 | **高** |
| 图神经网络(GNN) | 仅提及 | 🔴 | **高** |
| 扩散模型(Diffusion) | 无 | 🔴 | **中高** |
| 异常检测 | 仅提及 | 🔴 | 中 |
| 联邦学习 | 仅提及 | 🔴 | 中 |
| 传统RL(MDP/Q-learning) | 无 | 🔴 | 中 |
| SVM/KNN/决策树 | 无 | 🔴 | 中 |
| 搜索算法(A*/CSP) | 无 | 🔴 | 低 |
| 机器人学 | 无 | 🔴 | 低 |

### 1.3 合并后的缺口分类

将两个维度的缺口合并后，按处理方式分为三类：

**A类 - 需要新增独立教材的领域（6份）**：完全缺失或仅有概念性提及，需要系统化教学

**B类 - 需要扩展现有教材的领域（8处）**：有部分覆盖但深度不足，在现有教材中增加内容

**C类 - 保持现状的领域**：已充分覆盖或与项目定位关联度极低（机器人学、传统搜索算法），在教材中添加"延伸阅读"指针即可

---

## 二、新增独立教材清单（6份）

### 2.1 新增教材总览

| 编号 | 教材名称 | 学时 | 对标缺口 | 预计字数 | 优先级 |
|:---:|---------|:---:|---------|:-------:|:-----:|
| E4 | 商业智能与数据可视化 | 6h | DATA 6540 | 10,000-12,000 | 高 |
| E5 | 商业生成式AI应用与流程自动化 | 6h | DATA 6570 | 10,000-12,000 | 高 |
| E6 | 应用统计与优化方法 | 6h | DATA 6500 + 统计学 + R语言 | 12,000-15,000 | 高 |
| E7 | 计算机视觉与多模态感知 | 6h | Applied AI: CV | 10,000-12,000 | 高 |
| E8 | 深度学习与生成模型进阶 | 6h | Applied AI: DL/Diffusion/GNN | 12,000-15,000 | 中 |
| E11 | 推荐系统与个性化营销 | 6h | Applied AI: RecSys | 10,000-12,000 | 中 |

### 2.2 各教材详细设计

---

#### E4：商业智能与数据可视化

| 属性 | 内容 |
|------|------|
| **对标课程** | DATA 6540 Business Intelligence |
| **对应技能** | 技能0深化 + 技能1深化 |
| **核心缺口** | Tableau/Power BI、交互式仪表盘、数据叙事、UI/UX设计原则 |
| **与营销关联** | 营销KPI仪表盘、客户分析可视化、营销效果汇报 |

**三天教学计划**：

Day 1 - 数据可视化原理与工具
- 可视化语法（Wilkinson Grammar of Graphics）
- 图表选择决策树（何时用柱状图/折线图/散点图/热力图/树状图）
- matplotlib/seaborn进阶（pairplot/jointplot/facetgrid/自定义样式）
- Plotly交互式图表（散点图/气泡图/地理图/动画图）
- Tableau Public实操（数据连接/计算字段/参数/筛选器）
- Power BI Service入门（Power Query/DAX基础/可视化矩阵）

Day 2 - 交互式仪表盘设计
- 仪表盘设计五原则：层次性（overview->detail）/对比性/焦点引导/交互性/叙事性
- Tableau Dashboard搭建实操（布局/容器/设备适配/操作按钮）
- Power BI报表设计（书签/按钮/问答/分解树）
- 云端部署（Tableau Cloud / Power BI Service / 分享与权限管理）
- 实时数据刷新与数据网关
- 代码示例：用Plotly Dash构建Python Web仪表盘

Day 3 - 数据叙事与UI/UX设计
- 数据叙事三幕结构：发现（数据探索）-> 解释（根因分析）-> 行动（决策建议）
- 故事板设计：受众分析（高管/运营/技术）、信息层次、叙事弧线
- 案例分析：一份营销季度报告的叙事重构
- UI设计原则：色彩理论（色盲友好/品牌一致）、排版层级、留白节奏、一致性规范
- UX设计流程：用户研究（人物画像）-> 原型设计（Figma/Sketch简介）-> 可用性测试
- 数据产品原型设计实践

**代码示例**：
- Python: 用Plotly构建交互式营销KPI仪表盘（含下拉筛选、时间范围选择、图表联动）
- Python: 用seaborn进阶可视化（客户分群pairplot、RFM热力图、漏斗图）
- Tableau: 营销KPI仪表盘搭建步骤指南

**作业**：
- 必做：用Tableau或Power BI搭建一个营销分析仪表盘（含至少5个图表+筛选器+数据叙事注释），提交截图+设计说明
- 挑战：设计一个面向CMO的数据产品原型，包含UI/UX设计文档和用户流程图

---

#### E5：商业生成式AI应用与流程自动化

| 属性 | 内容 |
|------|------|
| **对标课程** | DATA 6570 Generative AI Applications for Business |
| **对应技能** | 技能5深化 + 技能2深化 |
| **核心缺口** | 无代码/低代码AI工具、流程自动化/RPA、ChatGPT/Claude工具串联 |
| **与营销关联** | 自动化营销内容生成、智能客服、报告自动化 |

**三天教学计划**：

Day 1 - 无代码/低代码AI工具生态
- 工具全景图：Zapier / Make / n8n / Microsoft Power Automate / Google Workspace AI
- ChatGPT/Claude API基础调用（Python requests库 + curl）
- Prompt模板设计：系统提示+用户提示+输出格式控制
- AI工具串联模式：串联（A->B->C）/并行（A->B+C）/条件分支（if-else路由）
- 实操：用Zapier+OpenAI构建自动化邮件回复流程（收到邮件->AI分析意图->生成回复->人工审核->发送）
- 实操：用Make.com构建社交媒体内容自动发布流程

Day 2 - 业务流程自动化设计
- RPA概念与适用场景：规则驱动 vs AI驱动（意图驱动）的自动化边界
- 传统RPA工具：UiPath / Blue Prism / Automation Anywhere的功能定位
- 流程挖掘（Process Mining）基础：事件日志分析、Celonis简介
- 流程自动化机会评估矩阵：任务频率 x 人工成本 x AI成熟度
- 实操：用n8n构建营销内容自动生成-审核-发布流程（Webhook触发->AI生成->审核队列->CMS发布）
- Python代码：用Pyautogui实现简单RPA脚本（自动填表+截图+报告）

Day 3 - 企业级GenAI应用设计
- GenAI应用架构模式：嵌入式（API调用集成到现有系统）/ 对话式（AI助手+知识库）/ 自主式（Agent自主执行任务）
- 企业AI助手设计：知识库构建 + RAG + 对话界面 + 用户管理
- 自动化方案提案撰写模板：现状分析->痛点识别->方案设计->技术选型->ROI估算->实施路线图
- ROI计算与价值评估：效率提升量化、错误率降低、人力释放
- 案例分析：某零售企业营销流程自动化全方案（从邮件营销到社媒管理到报告生成）

**代码示例**：
- Python: 用OpenAI API + LangChain构建无代码AI助手（含知识库+对话界面）
- JSON: n8n工作流定义文件示例（完整可导入）
- Python: 用Pyautogui实现营销报告自动生成脚本

**作业**：
- 必做：选择一个真实业务流程，设计完整的AI驱动自动化方案（含流程图、工具选型、ROI估算），3000字方案文档
- 挑战：用Zapier/Make/n8n实现一个可运行的自动化流程并录制3分钟演示视频

---

#### E6：应用统计与优化方法

| 属性 | 内容 |
|------|------|
| **对标课程** | DATA 6500 + 统计学基础 |
| **对应技能** | 技能0深化 + 技能3深化 |
| **核心缺口** | 时间序列预测（ARIMA/Prophet）、蒙特卡洛模拟、线性与非线性优化、R语言 |
| **与营销关联** | 销售预测、预算分配优化、风险评估 |

**三天教学计划**：

Day 1 - 时间序列预测
- 时间序列分解：趋势（Trend）/季节性（Seasonality）/残差（Residual），STL分解法
- 平稳性检验：ADF检验、KPSS检验、差分操作
- 自相关分析：ACF/PACF图解读、滞后阶数选择
- ARIMA模型详解：AR(p) + I(d) + MA(q) 的数学原理、参数选择策略、模型诊断
- Seasonal ARIMA (SARIMA)：季节性参数选择
- Prophet模型（Facebook开源）：加法模型 + 变点检测 + 季节性 + 节日效应
- Python代码：用statsmodels实现ARIMA预测营销月度销售额（含模型选择、诊断、预测、置信区间）
- Python代码：用Prophet预测含节日的电商促销销量
- 模型评估：MAPE / RMSE / MASE / 时间序列交叉验证

Day 2 - 蒙特卡洛模拟与优化方法
- 蒙特卡洛模拟原理：随机采样、大数定律收敛、方差缩减技术（重要性采样/对偶变量）
- 应用场景：营销ROI风险评估、定价策略模拟、库存优化、项目工期估算
- Python代码：用numpy实现营销预算蒙特卡洛模拟（10000次采样，输出ROI分布和风险概率）
- 线性规划：标准形式、单纯形法直觉、对偶问题
- Python代码：用scipy.optimize.linprog求解营销资源分配问题（多渠道预算最优分配）
- 非线性优化：无约束优化（梯度下降/牛顿法）、有约束优化（拉格朗日乘子/KKT条件）
- Python代码：用scipy.optimize.minimize求解非线性营销定价优化
- 整数规划简介：分支定界法、营销选址问题
- 遗传算法/模拟退火简介：元启发式优化在复杂营销优化中的应用

Day 3 - R语言基础与统计应用
- R语言环境搭建：RStudio安装、tidyverse生态、R Markdown
- R数据操作：dplyr（filter/mutate/summarise/join）、tidyr（pivot_longer/pivot_wider）
- R数据可视化：ggplot2语法（图层+美学映射+标度+主题）、经典图表类型
- R统计建模：lm()线性回归、glm()广义线性模型、arima()时间序列、t.test()假设检验
- R vs Python对比：何时用R（统计建模/学术发表/生物统计）、何时用Python（工程/ML/数据处理）、如何在Python中调用R（rpy2）
- 代码示例：用R完成一份完整的营销数据分析报告（数据清洗->可视化->统计检验->时间序列预测->报告输出）

**代码示例**：
- Python: ARIMA完整代码（statsmodels）+ Prophet预测代码 + 模型评估
- Python: 蒙特卡洛模拟（numpy）+ 线性规划（scipy.optimize.linprog）+ 非线性优化（scipy.optimize.minimize）
- R: ggplot2可视化 + dplyr数据操作 + arima建模 + lm回归

**作业**：
- 必做：用ARIMA或Prophet对一份营销时间序列数据做预测（含模型选择理由、诊断图、评估指标），2000字报告
- 挑战：用蒙特卡洛模拟评估一个全年营销预算方案的ROI分布（含至少3个随机变量），给出P(ROI>0)和VaR

---

#### E7：计算机视觉与多模态感知

| 属性 | 内容 |
|------|------|
| **对标缺口** | Applied AI: Computer Vision（完全缺失） |
| **对应技能** | 技能1深化 |
| **核心缺口** | CNN架构、图像分类、目标检测、图像分割、多模态融合 |
| **与营销关联** | 营销图像/视频内容分析、产品图片自动标注、社媒视觉内容理解、视觉搜索 |

**三天教学计划**：

Day 1 - 计算机视觉基础与CNN
- 数字图像基础：像素/通道/分辨率/色彩空间（RGB/HSV/灰度）
- 卷积操作详解：卷积核/步长/填充/感受野，数学公式与直觉
- CNN经典架构演进：LeNet -> AlexNet -> VGG -> ResNet（残差连接的数学原理）-> EfficientNet
- 池化层：最大池化/平均池化/全局平均池化
- 迁移学习在CV中的应用：预训练模型（ImageNet权重）+ 微调策略
- Python代码：用PyTorch/transformers构建图像分类模型（产品图片自动分类：服装/电子/食品/家居）
- Python代码：用预训练ResNet提取图像特征用于营销内容分析

Day 2 - 目标检测与图像分割
- 目标检测演进：R-CNN -> Fast R-CNN -> Faster R-CNN -> YOLO -> DETR
- YOLO架构详解：网格划分/锚框/非极大值抑制(NMS)/损失函数
- Python代码：用YOLOv8检测营销图片中的产品、品牌Logo、文字
- 图像分割：语义分割（FCN/U-Net）vs 实例分割（Mask R-CNN）vs 全景分割
- Python代码：用预训练模型分割产品图片中的前景物体
- OCR（光学字符识别）：Tesseract / PaddleOCR在营销物料文字提取中的应用
- 应用案例：社媒图片自动标注系统（检测产品+品牌+场景+情绪）

Day 3 - 多模态感知与视觉营销应用
- 视觉-语言模型（VLM）：CLIP（对比学习对齐图像和文本）、BLIP、LLaVA
- GPT-4o/Gemini多模态能力：图像理解+生成+推理
- Python代码：用CLIP计算营销图片与文案的匹配度
- 视觉搜索系统：以图搜图（用embedding相似度检索相似产品）
- 视觉内容分析平台架构：图像采集->预处理->特征提取->索引->检索->分析
- 营销应用全景：产品自动标注/UGC内容审核/竞品视觉监测/广告创意效果预测/品牌Logo监测
- 综合案例：构建一个社媒视觉内容分析Pipeline

**代码示例**：
- Python: PyTorch CNN图像分类完整代码（数据增强/训练/评估/混淆矩阵）
- Python: YOLOv8目标检测代码（营销图片产品检测）
- Python: CLIP图文匹配度计算代码

**作业**：
- 必做：用预训练CNN模型对一组营销图片做分类和特征提取，分析视觉内容分布
- 挑战：用CLIP构建一个营销图文匹配度评估工具，能判断广告文案与配图是否一致

---

#### E8：深度学习与生成模型进阶

| 属性 | 内容 |
|------|------|
| **对标缺口** | Applied AI: DL架构(CNN/RNN/LSTM) + 扩散模型 + GNN |
| **对应技能** | 技能1深化 + 选修E3深化 |
| **核心缺口** | CNN/RNN/LSTM架构详解、扩散模型、图神经网络 |
| **与营销关联** | 营销内容生成（扩散模型）、客户关系图谱分析（GNN）、序列行为建模（RNN/LSTM） |

**三天教学计划**：

Day 1 - 深度学习架构全景（补齐CNN/RNN/LSTM）
- CNN深入：卷积层的梯度传播、感受野计算、特征可视化（CAM/Grad-CAM）
- RNN架构：隐状态传递、梯度消失/爆炸、BPTT算法
- LSTM详解：遗忘门/输入门/输出门、细胞状态、数学公式与直觉
- GRU对比：简化版LSTM、重置门/更新门
- Python代码：用PyTorch实现LSTM预测客户购买序列（用户行为序列->下次购买概率）
- Seq2Seq + Attention：编码器-解码器架构、注意力机制的演进（从Bahdanau到Transformer）
- Python代码：用Transformer实现营销文本摘要（长篇营销报告->执行摘要）

Day 2 - 扩散模型与生成AI
- 扩散模型原理：前向扩散（加噪过程）+ 反向扩散（去噪生成）
- DDPM数学推导：马尔可夫链、重参数化技巧、损失函数推导
- 条件生成：Classifier-free Guidance / 文本条件生成（CLIP文本编码器+U-Net去噪器）
- 架构详解：U-Net（编码器-瓶颈-解码器+跳跃连接）、时间嵌入
- Stable Diffusion架构：潜在扩散模型（Latent Diffusion）、VAE编码器/解码器、文本编码器
- 主流生成模型对比：Stable Diffusion / DALL-E 3 / Midjourney / Sora（视频生成）
- Python代码：用diffusers库（HuggingFace）生成营销图片（产品场景图/广告创意图）
- 营销应用：AI生成广告创意/产品图片/社媒视觉内容/品牌风格迁移
- VAE/GAN进阶：VAE的变分推断、GAN的训练不稳定性及解决方案（WGAN/Spectral Norm）

Day 3 - 图神经网络（GNN）
- 图数据基础：节点/边/邻接矩阵/度/图同构
- 消息传递机制：聚合（Aggregate）-> 更新（Update）-> 循环
- GCN（Graph Convolutional Network）：谱图卷积->空间域简化、传播规则
- GraphSAGE：邻居采样策略（均值/LSTM/池化）、归纳式学习
- GAT（Graph Attention Network）：注意力机制在图上的应用、多头注意力
- 图分类vs节点分类vs链路预测：三类任务的差异
- Python代码：用PyTorch Geometric实现GCN进行客户分群（基于社交关系图）
- 营销应用：社交网络影响传播分析、客户关系图谱嵌入、推荐系统中的图方法
- 异构图与知识图谱嵌入：R-GCN / HAN（异构注意力网络）

**代码示例**：
- Python: LSTM客户行为预测代码（PyTorch）
- Python: diffusers库营销图片生成代码
- Python: PyTorch Geometric GCN客户分群代码

**作业**：
- 必做：用LSTM或Transformer对一份客户行为序列数据建模，预测下一步行为
- 挑战：用diffusers库生成一组营销创意图片，并写一份"AI生成内容在营销中的应用可行性分析"报告

---

#### E11：推荐系统与个性化营销

| 属性 | 内容 |
|------|------|
| **对标缺口** | Applied AI: Recommendation Systems（部分覆盖） |
| **对应技能** | 技能1深化 + 技能3深化 |
| **核心缺口** | 协同过滤、基于内容的推荐、矩阵分解、深度学习推荐、冷启动、推荐公平性 |
| **与营销关联** | 个性化推荐是营销转化的核心技术 |

**三天教学计划**：

Day 1 - 推荐系统基础
- 推荐系统范式：协同过滤（CF）/ 基于内容（CB）/ 混合方法
- 基于用户的协同过滤：相似度计算（余弦/Pearson）、邻居选择、预测公式
- 基于物品的协同过滤：物品相似度矩阵、Amazon的item-to-item方法
- 矩阵分解：SVD / PMF / ALS的数学原理和优化方法
- Python代码：用Surprise库实现协同过滤推荐（MovieLens/电商数据集）
- 评估指标：Precision@K / Recall@K / NDCG / MAP / Hit Rate
- Python代码：用scikit-learn评估推荐系统效果

Day 2 - 深度学习推荐系统
- 神经协同过滤（NCF）：用MLP替代内积、广义矩阵分解（GMF）+ MLP融合
- Wide & Deep Learning：宽部分（记忆能力）+ 深部分（泛化能力）
- DeepFM：FM层（二阶特征交叉）+ DNN层（高阶特征交叉）
- Two-Tower模型回顾（与技能1的表示工程连接）：双塔检索 + 在线推理
- 序列推荐：SASRec / BERT4Rec（用Transformer建模用户行为序列）
- Python代码：用PyTorch实现NCF推荐模型
- Python代码：用Two-Tower模型构建营销内容推荐

Day 3 - 推荐系统工程与公平性
- 推荐系统架构：召回层（多路召回）-> 排序层（精排）-> 重排层（多样性/新鲜度）
- 冷启动问题：新用户/新物品策略（内容特征/人口统计学/流行度/探索利用）
- 多目标推荐：点击率+转化率+停留时长的多任务学习（MMoE / PLE）
- 推荐公平性：位置偏差/曝光偏差/流行度偏差/选择偏差
- 因果推荐（与技能3连接）：IPS（逆倾向得分）/ 反事实推理在推荐去偏中的应用
- 可解释推荐：解释生成方法（邻域解释/注意力权重/反事实解释）
- 综合案例：设计一个电商个性化营销推荐系统的完整架构

**代码示例**：
- Python: 用Surprise库实现协同过滤 + 评估
- Python: 用PyTorch实现NCF推荐模型
- Python: 用Two-Tower模型构建营销内容推荐（含召回+排序）

**作业**：
- 必做：在一个公开数据集上实现并评估两种推荐算法（协同过滤 + 深度学习），对比效果
- 挑战：设计一个解决冷启动问题的推荐方案，包含技术方案和评估方法

---

## 三、现有教材扩展清单（8处）

### 3.1 扩展总览

| 序号 | 教材 | 扩展位置 | 扩展内容 | 预计新增字数 | 对标缺口 |
|:---:|------|---------|---------|:---------:|---------|
| 1 | 技能0 | 新增Day 7 | AI辅助编程 + R语言入门 + 数据仓库 | 3,000-4,000 | DATA 5405 |
| 2 | 技能0 | Day 3-4扩展 | SVM/KNN/决策树/朴素贝叶斯经典ML算法 | 2,000-3,000 | Applied AI: ML |
| 3 | 技能0 | Day 5扩展 | NoSQL四类数据建模（文档/键值/图/列式） | 1,500-2,000 | DATA 6510 |
| 4 | 技能5 | Day 5扩展 | MLOps工具链（MLflow/DVC/Kubeflow）+ AutoML | 4,000-5,000 | DATA 6545 |
| 5 | 选修E2 | 新增章节 | 数据叙事方法论 + BI框架 + Tableau/Power BI简介 | 2,000-3,000 | DATA 6540 |
| 6 | 选修E1 | 新增章节 | RPA对比 + 流程挖掘基础 | 1,500-2,000 | DATA 6570 |
| 7 | 选修E3 | Day 1扩展 | 传统RL基础（MDP/Q-learning/DQN）作为RLHF前置 | 2,000-3,000 | Applied AI: RL |
| 8 | 技能1 | Day 3扩展 | GNN基础（GCN/GraphSAGE/GAT）+ 异常检测简介 + 联邦学习简介 | 2,500-3,500 | Applied AI: GNN/Anomaly/Federated |

### 3.2 各扩展详细内容

---

**扩展1：技能0新增Day 7 - AI辅助编程与开发工具**

新增一天的教学内容，覆盖：
- AI辅助编程工具生态：GitHub Copilot / Cursor / Codeium / Tabnine 的功能对比和适用场景
- AI辅助调试技巧：用ChatGPT/Claude分析报错信息、生成调试步骤、建议修复方案
- AI辅助代码审查：用AI检测代码异味、安全漏洞、性能瓶颈
- Prompt-to-Code实践：如何用自然语言描述需求让AI生成可运行代码
- R语言入门：RStudio环境、基础语法、与Python的对比和互操作（rpy2）
- 数据仓库概念：维度建模（星型/雪花模型）、ETL vs ELT、数据湖概念、OLAP vs OLTP

---

**扩展2：技能0 Day 3-4 - 经典ML算法补充**

在现有统计基础教学中补充经典机器学习算法：
- SVM（支持向量机）：最大间隔原理、核函数（线性/RBF/多项式）、软间隔、Python代码（sklearn.svm）
- KNN（K近邻）：距离度量、K值选择、kd树加速、Python代码
- 决策树：信息增益/基尼系数、剪枝策略、Python代码（sklearn.tree）
- 随机森林：Bagging原理、特征随机选择、OOB评估、Python代码
- 朴素贝叶斯：贝叶斯定理、条件独立假设、拉普拉斯平滑、Python代码
- XGBoost/LightGBM：梯度提升树原理、正则化、Python代码
- 模型选择与评估：交叉验证、网格搜索、学习曲线、过拟合诊断

---

**扩展3：技能0 Day 5 - NoSQL数据建模扩展**

在现有SQL教学中扩展NoSQL内容：
- CAP定理：一致性/可用性/分区容错性的权衡
- ACID vs BASE：关系型与非关系型的设计哲学差异
- 文档数据库（MongoDB）：文档模型、CRUD操作、索引、聚合管道
- 键值数据库（Redis）：数据类型（String/List/Hash/Set/ZSet）、持久化、缓存模式
- 图数据库（Neo4j）：属性图模型、Cypher查询语言、与技能1知识图谱的连接
- 列式数据库（Cassandra）：分区键/聚类键、宽表模型、适用场景
- SQL vs NoSQL选型矩阵：数据结构/查询模式/一致性要求/扩展方式

---

**扩展4：技能5 Day 5 - MLOps与AutoML扩展**

在现有生产部署内容中大幅扩展MLOps和AutoML：
- MLOps成熟度模型：Level 0（手动）-> Level 1（ML Pipeline自动化）-> Level 2（CI/CD）
- MLflow：实验追踪（Tracking）、模型注册（Model Registry）、模型服务（Serving）、代码版本（Projects）
- DVC（Data Version Control）：数据版本管理、Pipeline复现、实验对比
- Kubeflow：Kubernetes上的ML管道编排、训练/ Serving / 监控
- 模型监控：数据漂移检测（Population Stability Index）、概念漂移、预测质量监控
- AutoML原理：超参数优化（HPO：网格/随机/贝叶斯）、神经网络架构搜索（NAS）、自动集成
- AutoML工具对比：Auto-sklearn / H2O.ai / Google AutoML / TPOT / Optuna
- CI/CD for ML：ML管道自动化测试、模型AB部署、灰度发布、回滚策略
- Feature Store：特征存储与管理（Feast/Tecton）

---

**扩展5：选修E2 - 数据叙事与BI扩展**

在营销分析教材中新增数据叙事和BI内容：
- 数据叙事三幕结构：发现->解释->行动
- 故事板设计：受众分析、信息层次、叙事弧线
- 数据叙事与数据可视化的关系：图表为叙事服务
- 商业智能框架：BI系统架构、OLAP多维分析、数据仓库分层（ODS/DW/DM）
- Tableau/Power BI简介：工具对比、基本操作、与Python可视化生态的关系
- 案例：将一份营销分析报告重构为数据叙事

---

**扩展6：选修E1 - RPA与流程挖掘扩展**

在Agentic AI教材中增加传统RPA对比：
- RPA vs AI Agent自动化：规则驱动 vs 意图驱动的适用边界
- 传统RPA工具：UiPath / Blue Prism / Automation Anywhere 的功能定位
- 流程挖掘（Process Mining）：事件日志分析、Celonis简介
- 何时用RPA vs 何时用AI Agent：决策矩阵

---

**扩展7：选修E3 - 传统RL基础扩展**

在LLM导论的预训练-微调-对齐部分之前补充传统RL基础：
- MDP（马尔可夫决策过程）：状态/动作/转移/奖励/策略的形式化定义
- 值函数：状态值V(s)、动作值Q(s,a)、贝尔曼方程
- 值迭代与策略迭代：动态规划方法
- Q-learning：时序差分学习、探索-利用权衡（ε-greedy）、Python代码
- DQN（Deep Q-Network）：经验回放、目标网络、Python代码
- 策略梯度方法：REINFORCE算法、策略梯度定理
- PPO（Proximal Policy Optimization）：截断目标函数、作为RLHF的基础算法
- 与RLHF的连接：传统RL为RLHF提供理论和算法基础

---

**扩展8：技能1 - GNN/异常检测/联邦学习扩展**

在表示工程教材的知识图谱部分扩展：
- GNN基础：消息传递机制、GCN传播规则、GraphSAGE邻居采样、GAT注意力
- Python代码：用PyTorch Geometric实现GCN
- GNN与知识图谱的连接：R-GCN用于关系图嵌入
- 异常检测方法：Isolation Forest / One-class SVM / 自编码器异常检测
- Python代码：用Isolation Forest检测营销数据异常
- 联邦学习基础：FedAvg算法、差分隐私、安全聚合
- 联邦学习在跨企业营销数据协作中的应用场景

---

## 四、不迭代的领域说明

以下主题经评估后保持现状，在教材中添加"延伸阅读"指针即可：

| 主题 | 不迭代原因 |
|------|---------|
| 机器人学 | 与AI+营销领域关联度极低，项目定位不需要 |
| 传统搜索算法（A*/CSP） | 属于符号主义AI，与当前深度学习/LLM范式距离较远 |
| 逻辑推理/描述逻辑 | 知识图谱本体设计已覆盖实用部分，形式逻辑偏理论 |
| 遗传算法/模拟退火 | 蒙特卡洛和scipy.optimize已覆盖主流优化需求，在E6中简介即可 |

---

## 五、实施计划

### 5.1 分阶段实施

**第一阶段：新增6份独立教材**

| 批次 | 教材 | 预计字数 | 对标维度 |
|:---:|------|:-------:|---------|
| 批次1 | E4 商业智能与数据可视化 | 10,000-12,000 | AIBA |
| 批次1 | E6 应用统计与优化方法 | 12,000-15,000 | AIBA + Applied AI |
| 批次1 | E7 计算机视觉与多模态感知 | 10,000-12,000 | Applied AI |
| 批次2 | E5 商业生成式AI应用与流程自动化 | 10,000-12,000 | AIBA |
| 批次2 | E8 深度学习与生成模型进阶 | 12,000-15,000 | Applied AI |
| 批次2 | E11 推荐系统与个性化营销 | 10,000-12,000 | Applied AI |

**第二阶段：扩展8处现有教材**

| 序号 | 教材 | 扩展内容 | 预计新增 |
|:---:|------|---------|:-------:|
| 1 | 技能0 Day 7 | AI辅助编程+R+数据仓库 | 3,000-4,000 |
| 2 | 技能0 Day 3-4 | SVM/KNN/决策树等ML算法 | 2,000-3,000 |
| 3 | 技能0 Day 5 | NoSQL数据建模 | 1,500-2,000 |
| 4 | 技能5 Day 5 | MLOps+AutoML | 4,000-5,000 |
| 5 | 选修E2 | 数据叙事+BI框架 | 2,000-3,000 |
| 6 | 选修E1 | RPA对比+流程挖掘 | 1,500-2,000 |
| 7 | 选修E3 | 传统RL基础 | 2,000-3,000 |
| 8 | 技能1 | GNN+异常检测+联邦学习 | 2,500-3,500 |

**第三阶段：交叉引用与README更新**

- 在8份现有教材中添加交叉引用
- 更新README.md文件结构、选修池和版本说明
- 更新版本号至v4.1
- 更新项目记忆

### 5.2 版本变化

| 项目 | v4.0 | v4.1 | 变化 |
|------|------|------|------|
| 选修课数量 | 5门 | 11门（+E4/E5/E6/E7/E8/E11） | +6门 |
| 选修学时 | 18h（选3门） | 18h（选3门，池更大） | 不变 |
| 独立教材数 | 13份 | 19份 | +6份 |
| 现有教材扩展 | 0处 | 8处 | +18,500-25,500字 |
| 总学时 | 122-136h | 128-142h | +6h |
| 总文件大小 | ~973KB | ~1,150KB | +177KB |

### 5.3 选修池更新

v4.1的选修池扩展为11门：

| 编号 | 选修课 | 对应深化技能 | 对标维度 |
|:---:|------|-------------|---------|
| E1 | Agentic AI | 技能5 | - |
| E2 | Marketing Analytics and Intelligence | 技能1+3 | AIBA: 统计学 |
| E3 | Introduction to Large Language Models | 技能2+5 | - |
| **E4** | **商业智能与数据可视化** ⭐ | **技能0+1** | **AIBA: DATA 6540** |
| **E5** | **商业生成式AI应用与流程自动化** ⭐ | **技能5+2** | **AIBA: DATA 6570** |
| **E6** | **应用统计与优化方法** ⭐ | **技能0+3** | **AIBA: DATA 6500 + R语言** |
| **E7** | **计算机视觉与多模态感知** ⭐ | **技能1** | **Applied AI: CV** |
| **E8** | **深度学习与生成模型进阶** ⭐ | **技能1+E3** | **Applied AI: DL/Diffusion/GNN** |
| E9 | AI安全与对齐 | 技能5+2 | AIBA: DATA 6515 |
| E10 | Agent经济与商业模式 | 技能4 | - |
| **E11** | **推荐系统与个性化营销** ⭐ | **技能1+3** | **Applied AI: RecSys** |

**推荐组合更新**：
- 组合C（原推荐）：E1 + E2 + E3 - Agentic AI + 营销分析 + LLM
- 组合D：E2 + E5 + E6 - 营销分析 + GenAI应用 + 统计优化（偏AIBA应用）
- 组合E：E1 + E4 + E5 - Agentic AI + BI + GenAI应用（偏企业落地）
- 组合F（新增）：E7 + E8 + E11 - 计算机视觉 + 深度学习进阶 + 推荐系统（偏Applied AI技术）
- 组合G（新增）：E4 + E6 + E11 - BI + 统计优化 + 推荐系统（偏营销数据科学）

### 5.4 预计工作量

| 阶段 | 产出 | 预计字数 | 优先级 |
|------|------|---------|:------:|
| 第一阶段 | 6份新教材 | 64,000-78,000字 | 高 |
| 第二阶段 | 8处教材扩展 | 18,500-25,500字 | 中 |
| 第三阶段 | 交叉引用+README | ~3,000字 | 低 |
| **总计** | **v4.1完整迭代** | **85,500-106,500字** | - |

---

## 六、验证标准

### 6.1 AIBA应用层验证

| 验证项 | 标准 | 验证方法 |
|--------|------|---------|
| 蒙特卡洛模拟 | 有原理+代码+营销场景 | 搜索"蒙特卡洛/Monte Carlo" |
| AutoML | 有概念+工具+适用场景 | 搜索"AutoML" |
| R语言 | 有语法+数据操作+可视化+建模 | 搜索"R语言/ggplot2/tidyverse" |
| AI辅助编程 | 有工具+调试+实操 | 搜索"Copilot/AI辅助编程" |
| 时间序列预测 | 有ARIMA+Prophet代码 | 搜索"ARIMA/Prophet" |
| 优化方法 | 有线性+非线性优化代码 | 搜索"scipy.optimize/linprog" |
| 商业智能 | 有Tableau/Power BI+仪表盘 | 搜索"Tableau/Power BI/dashboard" |
| 数据叙事 | 有方法论+故事板 | 搜索"数据叙事/storytelling" |
| 无代码/低代码 | 有工具实操+流程 | 搜索"Zapier/n8n/无代码" |
| 流程自动化 | 有RPA对比+方案设计 | 搜索"RPA/流程自动化" |
| MLOps | 有MLflow+管道+监控 | 搜索"MLflow/MLOps" |
| NoSQL | 有四类对比+数据建模 | 搜索"MongoDB/Cassandra/NoSQL" |
| UI/UX | 有设计原则+原型 | 搜索"UI/UX/用户体验设计" |

### 6.2 Applied AI技术层验证

| 验证项 | 标准 | 验证方法 |
|--------|------|---------|
| 计算机视觉 | 有CNN+目标检测+代码 | 搜索"CNN/YOLO/计算机视觉" |
| 扩散模型 | 有DDPM原理+diffusers代码 | 搜索"diffusion/扩散模型/DDPM" |
| GNN | 有GCN/GraphSAGE/GAT+代码 | 搜索"GNN/GCN/图神经网络" |
| 传统RL | 有MDP/Q-learning/DQN+代码 | 搜索"Q-learning/MDP/DQN" |
| SVM/KNN | 有算法原理+代码 | 搜索"SVM/KNN/支持向量机" |
| 推荐系统 | 有CF+矩阵分解+深度学习 | 搜索"协同过滤/矩阵分解/recommendation" |
| 异常检测 | 有Isolation Forest+代码 | 搜索"anomaly detection/异常检测" |
| 联邦学习 | 有FedAvg原理+应用 | 搜索"federated learning/联邦学习" |
| LSTM/RNN | 有架构+代码 | 搜索"LSTM/RNN/循环神经网络" |

---

## 七、版本命名

- 版本标签：v4.1 双维对标版（应用层 + 技术层）
- 版本特色：+ 商业智能与数据可视化 + 生成式AI应用与流程自动化 + 应用统计与优化方法 + 计算机视觉与多模态感知 + 深度学习与生成模型进阶 + 推荐系统与个性化营销 + MLOps/AutoML + R语言 + AI辅助编程 + GNN + 扩散模型 + 传统RL
- 文件命名：保持现有模式，新增教材以"选修E*_*.md"命名

---

*本计划合并了Fairfield University MSc in Applied Artificial Intelligence（AIBA方向）和标准MSc in Applied AI学位的双维度对标分析，等待审阅确认后执行。*
