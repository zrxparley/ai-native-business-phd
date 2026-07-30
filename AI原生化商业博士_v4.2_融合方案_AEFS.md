# AI原生化商业博士 v4.2 融合方案
# 融入 AI Engineering from Scratch (503 lessons × 20 phases)

> **编制日期**：2026-07-29
> **基于版本**：v4.1迭代计划（含AIBA + Applied AI双维对标）
> **融入项目**：[rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
> **项目规模**：503节课 · 20个阶段 · ~1050小时 · MIT开源
> **融合目标**：将AI Engineering from Scratch的"from scratch实现深度"注入博士课程的技术模块，同时保持商业博士的研究导向定位

---

## 一、融合策略

### 1.1 核心原则

AI Engineering from Scratch（以下简称AEFS）是一个纯技术工程导向的 curriculum，其特点是"每一节课都产出可复用的artifact"。我们的博士课程是商业研究导向的，特点是"研究深度+商业落地"。融合遵循三个原则：

**原则一：AEFS作为技术实现层引用，不替代商业研究框架**
- 博士课程的技能1-5保持其商业研究导向的结构
- AEFS的from-scratch实现作为"延伸实践"引用，嵌入每个技术章节
- 学习者按需深入AEFS的具体课程，不要求全部完成1050小时

**原则二：优先填补已识别的v4.1技术缺口**
- v4.1已识别的6份新教材（E4-E8, E11）对应的AEFS阶段直接引用
- v4.1已识别的8处扩展对应的AEFS阶段直接引用
- AEFS中完全新增的领域（语音/音频、自主系统）作为新选修

**原则三：建立双向交叉引用**
- 博士教材中标注"AEFS Phase X, Lesson Y"引用
- 建议学习者在AEFS仓库中标注"对应博士课程技能N"反向引用

### 1.2 融合后的版本变化

| 项目 | v4.0 | v4.1（计划） | v4.2（融合后） |
|------|------|------------|--------------|
| 独立教材 | 13份 | 19份（+6新） | 20份（+6新+1语音/音频） |
| 选修课 | 5门 | 11门 | 12门（+E12语音AI） |
| 技术实现引用 | 0 | 0 | 503节AEFS课程映射 |
| Capstone项目库 | 0 | 0 | 87个实操项目模板 |

---

## 二、20阶段完整映射表

### 2.1 映射总览

| AEFS阶段 | 阶段名称 | 课节数 | 预计时长 | 映射到博士课程 | 融合方式 |
|:---:|---------|:---:|:---:|---------|---------|
| 0 | Setup & Tooling | 12 | 14h | 技能0 Day 1-2 扩展 | 扩展引用 |
| 1 | Math Foundations | 22 | 23h | 技能0 Day 3-4 扩展 | 扩展引用 |
| 2 | ML Fundamentals | 18 | 21h | 技能0 Day 3-4 + v4.1扩展2 | 直接填补 |
| 3 | Deep Learning Core | 13 | 15h | v4.1 E8 Day 1 | 直接填补 |
| 4 | Computer Vision | 28 | 27h | v4.1 E7 | 直接填补 |
| 5 | NLP Foundations | 29 | 30h | 技能1 + E3 扩展 | 扩展引用 |
| 6 | Speech & Audio | 17 | 18h | **新选修E12** | 新增教材 |
| 7 | Transformers Deep Dive | 16 | 14h | E3 Day 1 扩展 | 扩展引用 |
| 8 | Generative AI | 14 | 14h | v4.1 E8 Day 2 | 直接填补 |
| 9 | Reinforcement Learning | 12 | 13h | v4.1 扩展7 + E9 | 直接填补 |
| 10 | LLMs from Scratch | 22 | 26h | E3 Day 1-2 扩展 | 扩展引用 |
| 11 | LLM Engineering | 15 | 17h | E3 Day 2-3 + 技能5 | 扩展引用 |
| 12 | Multimodal AI | 25 | 65h | v4.1 E7 Day 3 + E8 | 直接填补 |
| 13 | Tools & Protocols | 23 | 24.5h | 技能5 Day 2-4 扩展 | 扩展引用 |
| 14 | Agent Engineering | 42 | 42h | E1 + 技能5 Day 1-3 | 扩展引用 |
| 15 | Autonomous Systems | 22 | 20h | E1 扩展（高级） | 扩展引用 |
| 16 | Multi-Agent & Swarms | 25 | 28h | E1 Day 3 + E10 | 扩展引用 |
| 17 | Infrastructure & Production | 28 | 32h | v4.1 扩展4 + 技能5 Day 5 | 直接填补 |
| 18 | Ethics, Safety & Alignment | 30 | 31h | E9 扩展 | 扩展引用 |
| 19 | Capstone Projects | 87 | 620h | Capstone项目库 | 项目库引用 |

### 2.2 融合方式分类

**A. 直接填补（6个阶段）**：AEFS内容直接对应v4.1已识别的技术缺口，作为新教材的核心技术参考
- Phase 2 ML Fundamentals -> v4.1扩展2（SVM/KNN/决策树）
- Phase 3 Deep Learning Core -> v4.1 E8 Day 1（CNN/RNN/LSTM from scratch）
- Phase 4 Computer Vision -> v4.1 E7（计算机视觉）
- Phase 8 Generative AI -> v4.1 E8 Day 2（扩散模型）
- Phase 9 Reinforcement Learning -> v4.1扩展7（传统RL）
- Phase 17 Infrastructure & Production -> v4.1扩展4（MLOps/AutoML）

**B. 扩展引用（10个阶段）**：AEFS提供更深的from-scratch实现，作为现有/计划教材的延伸实践材料
- Phase 0 Setup & Tooling -> 技能0开发环境
- Phase 1 Math Foundations -> 技能0数学基础
- Phase 5 NLP Foundations -> 技能1 + E3 NLP深化
- Phase 7 Transformers -> E3 Transformer深化
- Phase 10 LLMs from Scratch -> E3 LLM训练深化
- Phase 11 LLM Engineering -> E3 + 技能5 LLM应用
- Phase 13 Tools & Protocols -> 技能5 MCP/工具链
- Phase 14 Agent Engineering -> E1 + 技能5 Agent工程
- Phase 16 Multi-Agent -> E1 + E10 多Agent
- Phase 18 Ethics & Safety -> E9 AI安全

**C. 新增内容（2个阶段）**：AEFS中有但博士课程完全没有的领域
- Phase 6 Speech & Audio -> 新选修E12
- Phase 15 Autonomous Systems -> E1高级扩展

**D. 项目库引用（1个阶段）**
- Phase 19 Capstone Projects -> 87个项目作为Capstone项目库

---

## 三、各阶段详细融合方案

### Phase 0: Setup & Tooling (12 lessons, 14h) -> 技能0扩展

**融合位置**：技能0 Day 1-2（Python编程基础 + 数据结构）

**引用AEFS课程**：

| AEFS课节 | 课节名称 | 融入方式 |
|---------|---------|---------|
| P0-01 | Dev Environment | 技能0 Day 1 延伸：Python开发环境完整搭建（conda/pyenv/poetry） |
| P0-02 | Git & Collaboration | 技能0 Day 1 延伸：Git版本控制基础（commit/branch/merge/PR） |
| P0-03 | GPU Setup & Cloud | 技能0 延伸：云GPU环境配置（Colab/Kaggle/AWS EC2） |
| P0-04 | APIs & Keys | 技能0 延伸：API密钥管理（OpenAI/Anthropic/HuggingFace） |
| P0-05 | Jupyter Notebooks | 技能0 Day 1 已覆盖，补充Jupyter高级技巧 |
| P0-06 | Python Environments | 技能0 Day 1 已覆盖，补充虚拟环境最佳实践 |
| P0-07 | Docker for AI | **新增**：技能0 Day 7 扩展，Docker容器化基础 |
| P0-08 | Editor Setup | 技能0 延伸：VS Code/Cursor配置 |
| P0-09 | Data Management | 技能0 Day 2 已覆盖，补充数据版本管理（DVC简介） |
| P0-10 | Terminal & Shell | 技能0 延伸：命令行基础 |
| P0-11 | Linux for AI | 技能0 延伸：Linux基础（文件系统/权限/进程） |
| P0-12 | Debugging & Profiling | 技能0 延伸：Python调试技巧（pdb/cProfile/memory_profiler） |

**预计新增引用**：~2,000字引用说明 + 链接

---

### Phase 1: Math Foundations (22 lessons, 23h) -> 技能0扩展

**融合位置**：技能0 Day 3-4（统计基础 + 回归分析）

**引用AEFS课程**：

| AEFS课节 | 融入方式 |
|---------|---------|
| P1-01 Linear Algebra Intuition | 技能0 Day 3 前置：向量/矩阵直觉 |
| P1-02 Vectors, Matrices & Operations | 技能0 Day 3 延伸：矩阵运算（为技能1 embedding打基础） |
| P1-03 Matrix Transformations & Eigenvalues | 技能1 引用：PCA/特征分解的数学基础 |
| P1-04 Calculus for ML | 技能0 Day 4 延伸：导数与梯度 |
| P1-05 Chain Rule & Auto Diff | 技能1 引用：反向传播的数学基础 |
| P1-06 Probability & Distributions | 技能0 Day 3 已覆盖，补充概率分布族 |
| P1-07 Bayes' Theorem | 技能0 Day 3 延伸：贝叶斯思维（为技能3因果推断打基础） |
| P1-08 Optimization - Gradient Descent | 技能0 Day 4 延伸：梯度下降家族 |
| P1-09 Information Theory | 技能1 引用：KL散度/交叉熵的数学基础 |
| P1-10 Dimensionality Reduction | 技能1 引用：PCA/t-SNE/UMAP |
| P1-11 SVD | 技能1 引用：矩阵分解（为推荐系统打基础） |
| P1-12 Tensor Operations | 技能1 引用：张量运算基础 |
| P1-13 Numerical Stability | v4.1 E8 引用：数值稳定性 |
| P1-14 Norms & Distances | 技能1 引用：距离度量（embedding相似度） |
| P1-15 Statistics for ML | 技能0 Day 3 已覆盖 |
| P1-16 Sampling Methods | 技能3 引用：采样方法（蒙特卡洛基础） |
| P1-17 Linear Systems | 技能0 延伸：线性方程组 |
| P1-18 Convex Optimization | v4.1 E6 引用：凸优化理论 |
| P1-19 Complex Numbers | 参考（与商业关联度低） |
| P1-20 Fourier Transform | Phase 6 语音处理前置 |
| P1-21 Graph Theory | 技能1 引用：图论基础（知识图谱/GNN前置） |
| P1-22 Stochastic Processes | v4.1 E6 引用：随机过程（时间序列/蒙特卡洛基础） |

**预计新增引用**：~3,000字引用说明 + 链接

---

### Phase 2: ML Fundamentals (18 lessons, 21h) -> v4.1扩展2 直接填补

**融合位置**：技能0 Day 3-4扩展（v4.1已规划的经典ML算法补充）

**这是直接填补v4.1已识别缺口的关键阶段。** AEFS提供了从零实现的完整课程：

| AEFS课节 | 融入方式 | v4.1缺口对应 |
|---------|---------|------------|
| P2-01 ML Types & Taxonomy | 技能0 Day 3 扩展 | ML基础分类 |
| P2-02 Linear Regression from Scratch | 技能0 Day 4 已有，补充from-scratch实现 | - |
| P2-03 Logistic Regression | 技能0 Day 4 扩展 | 分类基础 |
| P2-04 **Decision Trees & Random Forests** | **技能0 Day 3-4 扩展** | **v4.1缺口：决策树** |
| P2-05 **Support Vector Machines** | **技能0 Day 3-4 扩展** | **v4.1缺口：SVM** |
| P2-06 **K-Nearest Neighbors** | **技能0 Day 3-4 扩展** | **v4.1缺口：KNN** |
| P2-07 Unsupervised Learning - K-Means, DBSCAN | 技能0 已有K-Means，补充DBSCAN | 聚类扩展 |
| P2-08 Feature Engineering & Selection | 技能0 Day 2 已覆盖 | - |
| P2-09 Model Evaluation | 技能0 Day 3 已覆盖 | - |
| P2-10 Bias, Variance & Learning Curve | 技能0 Day 4 扩展 | 模型选择 |
| P2-11 Ensemble Methods | 技能0 扩展 | Boosting/Bagging |
| P2-12 **Hyperparameter Tuning & AutoML** | **v4.1扩展4 引用** | **v4.1缺口：AutoML** |
| P2-13 ML Pipelines & Experiment Tracking | v4.1扩展4 引用 | MLOps基础 |
| P2-14 Naive Bayes | 技能0 扩展 | 朴素贝叶斯 |
| P2-15 **Time Series Fundamentals** | **v4.1 E6 Day 1 引用** | **v4.1缺口：时间序列** |
| P2-16 **Anomaly Detection** | **技能1 扩展引用** | **v4.1缺口：异常检测** |
| P2-17 Handling Imbalanced Data | 技能3 引用 | 类别不平衡 |
| P2-18 Feature Selection | 技能0 Day 2 已覆盖 | - |

**融合产出**：在技能0 Day 3-4扩展中，每个算法标注"AEFS P2-XX"引用，建议学习者阅读AEFS对应课节的from-scratch实现。

---

### Phase 3: Deep Learning Core (13 lessons, 15h) -> v4.1 E8 Day 1

**融合位置**：v4.1新教材E8 Day 1（深度学习架构全景）

| AEFS课节 | 融入方式 |
|---------|---------|
| P3-01 The Perceptron | E8 Day 1 引用：感知机从零实现 |
| P3-02 Multi-Layer Networks & Forward Pass | E8 Day 1 引用：前向传播 |
| P3-03 **Backpropagation from Scratch** | **E8 Day 1 核心引用** |
| P3-04 Activation Functions | E8 Day 1 引用：ReLU/Sigmoid/GELU |
| P3-05 Loss Functions | E8 Day 1 引用：MSE/交叉熵/对比损失 |
| P3-06 Optimizers | E8 Day 1 引用：SGD/Momentum/Adam/AdamW |
| P3-07 Regularization | E8 Day 1 引用：Dropout/Weight Decay/BatchNorm |
| P3-08 Weight Initialization | E8 Day 1 引用 |
| P3-09 Learning Rate Schedules | E8 Day 1 引用 |
| P3-10 **Build Your Own Mini Framework** | **E8 Day 1 核心实践** |
| P3-11 Introduction to PyTorch | E8 Day 1 引用：PyTorch基础 |
| P3-12 Introduction to JAX | E8 Day 1 延伸：JAX简介 |
| P3-13 Debugging Neural Networks | E8 Day 1 引用：调试技巧 |

**融合产出**：E8 Day 1的每个概念标注AEFS课节链接，建议学习者完成P3-10"构建自己的mini框架"作为实践作业。

---

### Phase 4: Computer Vision (28 lessons, 27h) -> v4.1 E7

**融合位置**：v4.1新教材E7（计算机视觉与多模态感知）

AEFS的Phase 4是**全球最完整的开源CV课程之一**，28节课覆盖从像素到世界模型：

| AEFS课节 | E7映射 | 融入方式 |
|---------|--------|---------|
| P4-01 Image Fundamentals | E7 Day 1 | 图像基础 |
| P4-02 **Convolutions from Scratch** | E7 Day 1 | **核心引用** |
| P4-03 **CNNs - LeNet to ResNet** | E7 Day 1 | **核心引用** |
| P4-04 Image Classification | E7 Day 1 | 分类实践 |
| P4-05 Transfer Learning & Fine-Tuning | E7 Day 1 | 迁移学习 |
| P4-06 **Object Detection - YOLO** | E7 Day 2 | **核心引用** |
| P4-07 Semantic Segmentation - U-Net | E7 Day 2 | 分割 |
| P4-08 Instance Segmentation - Mask R-CNN | E7 Day 2 | 实例分割 |
| P4-09 Image Generation - GANs | E8 Day 2 引用 | GAN |
| P4-10 **Diffusion Models** | E8 Day 2 | **核心引用：扩散模型** |
| P4-11 **Stable Diffusion** | E8 Day 2 | **核心引用** |
| P4-12 Video Understanding | E7 Day 3 | 视频理解 |
| P4-13 3D Vision - NeRFs | 延伸阅读 | 3D视觉 |
| P4-14 Vision Transformers (ViT) | E7 Day 3 | ViT |
| P4-15 Real-Time Vision - Edge | 延伸阅读 | 边缘部署 |
| P4-16 Complete Vision Pipeline | E7 作业 | 综合实践 |
| P4-17 Self-Supervised Vision | 延伸阅读 | SimCLR/DINO/MAE |
| P4-18 **CLIP** | E7 Day 3 | **核心引用：CLIP** |
| P4-19 OCR & Document Understanding | E7 Day 2 | OCR（营销物料文字提取） |
| P4-20 Image Retrieval & Metric Learning | E7 Day 3 | 图像检索 |
| P4-21 Keypoint Detection | 延伸阅读 | 关键点检测 |
| P4-22 3D Gaussian Splatting | 延伸阅读 | 3D重建 |
| P4-23 Diffusion Transformers | E8 Day 2 | DiT |
| P4-24 SAM 3 & Open-Vocabulary | 延伸阅读 | 分割一切 |
| P4-25 **Vision-Language Models** | E7 Day 3 | **核心引用：VLM** |
| P4-26 Monocular Depth | 延伸阅读 | 深度估计 |
| P4-27 Multi-Object Tracking | 延伸阅读 | 多目标跟踪 |
| P4-28 World Models & Video Diffusion | 延伸阅读 | 世界模型 |

**融合产出**：E7教材中每个章节标注"AEFS P4-XX"引用。E7 Day 1核心概念引用P4-01~P4-05，Day 2引用P4-06~P4-08+P4-19，Day 3引用P4-14+P4-18+P4-25。扩散模型部分引用P4-10/11/23到E8。

---

### Phase 5: NLP Foundations (29 lessons, 30h) -> 技能1 + E3扩展

**融合位置**：技能1 Day 2（营销数据表示）+ 选修E3（LLM导论）

| AEFS课节 | 映射位置 | 融入方式 |
|---------|---------|---------|
| P5-01 Text Processing | 技能1 Day 2 | 文本预处理 |
| P5-02 Bag of Words, TF-IDF | 技能1 Day 2 | 经典文本表示 |
| P5-03 **Word2Vec from Scratch** | 技能1 Day 2 | **核心引用：词嵌入** |
| P5-04 GloVe, FastText | 技能1 Day 2 | 词嵌入扩展 |
| P5-05 Sentiment Analysis | E2 引用 | 情感分析（营销应用） |
| P5-06 **NER** | 技能1 Day 2 | **命名实体识别** |
| P5-07 POS Tagging & Parsing | 延伸阅读 | 句法分析 |
| P5-08 CNNs & RNNs for Text | E8 Day 1 引用 | 文本CNN/RNN |
| P5-09 Seq2Seq Models | E8 Day 1 引用 | 序列到序列 |
| P5-10 **Attention Mechanism** | E3 Day 1 | **核心引用** |
| P5-11 Machine Translation | 延伸阅读 | 机器翻译 |
| P5-12 Text Summarization | E3 引用 | 文本摘要 |
| P5-13 Question Answering | 技能5 引用 | 问答系统 |
| P5-14 Information Retrieval & Search | 技能5 引用 | 检索（RAG基础） |
| P5-15 Topic Modeling | E2 引用 | 主题模型（营销洞察） |
| P5-16 Text Generation Pre-Transformer | E3 Day 1 | 前Transformer时代 |
| P5-17 Chatbots | 技能5 引用 | 对话系统 |
| P5-18 Multilingual NLP | 延伸阅读 | 多语言NLP |
| P5-19 Subword Tokenization | E3 Day 1 | BPE/WordPiece |
| P5-20 Structured Outputs | 技能5 引用 | 结构化输出 |
| P5-21 NLI & Entailment | 延伸阅读 | 自然语言推理 |
| P5-22 **Embedding Models Deep Dive** | 技能1 Day 2 | **核心引用** |
| P5-23 **Chunking for RAG** | 技能5 引用 | **RAG分块策略** |
| P5-24 Coreference Resolution | 延伸阅读 | 共指消解 |
| P5-25 Entity Linking | 技能1 引用 | 实体链接（知识图谱） |
| P5-26 **Relation Extraction & KG** | 技能1 Day 3 | **核心引用：知识图谱构建** |
| P5-27 **LLM Evaluation - RAGAS** | 技能5 引用 | **LLM评估** |
| P5-28 Long-Context Evaluation | 技能5 引用 | 长上下文评估 |
| P5-29 Dialogue State Tracking | 技能5 引用 | 对话状态跟踪 |

**融合产出**：技能1和E3中标注AEFS引用。P5-03/22/26直接补强技能1的表示工程和知识图谱内容。

---

### Phase 6: Speech & Audio (17 lessons, 18h) -> 新选修E12

**融合位置**：**新选修E12：语音AI与音频处理**（v4.2新增）

这是博士课程完全缺失的领域，AEFS提供了完整的17节课：

| AEFS课节 | E12 Day | 内容 |
|---------|---------|------|
| P6-01 Audio Fundamentals | Day 1 | 波形/采样/傅里叶变换 |
| P6-02 Spectrograms & Mel Features | Day 1 | 频谱图/Mel尺度 |
| P6-03 Audio Classification | Day 1 | 音频分类 |
| P6-04 Speech Recognition (ASR) | Day 2 | 语音识别 |
| P6-05 **Whisper** | Day 2 | **Whisper架构与微调** |
| P6-06 Speaker Recognition | Day 2 | 说话人识别 |
| P6-07 **Text-to-Speech (TTS)** | Day 2 | **语音合成** |
| P6-08 Voice Cloning & Conversion | Day 3 | 语音克隆 |
| P6-09 Music Generation | Day 3 | 音乐生成 |
| P6-10 Audio-Language Models | Day 3 | 音频语言模型 |
| P6-11 Real-Time Audio Processing | Day 3 | 实时音频处理 |
| P6-12 Voice Assistant Pipeline | 作业 | 语音助手完整Pipeline |
| P6-13 Neural Audio Codecs | 延伸 | 神经音频编解码 |
| P6-14 Voice Activity Detection | 延伸 | VAD与轮次检测 |
| P6-15 Streaming Speech-to-Speech | 延伸 | 流式语音到语音 |
| P6-16 Anti-Spoofing & Watermarking | 延伸 | 音频防伪 |
| P6-17 Audio Evaluation | 延伸 | 音频评估指标 |

**与营销关联**：语音客服、语音广告、播客内容分析、语音搜索优化、品牌声音识别

**新选修E12设计**：

| 属性 | 内容 |
|------|------|
| 学时 | 6h |
| 对标 | AEFS Phase 6 |
| 对应技能 | 技能1+5深化 |
| Day 1 | 音频基础 + 音频分类（波形/频谱/Mel特征/分类模型） |
| Day 2 | 语音识别与合成（ASR/Whisper/TTS/语音助手） |
| Day 3 | 语音AI营销应用（语音搜索/播客分析/语音客服/品牌声音识别） |
| 作业 | 用Whisper构建播客内容分析Pipeline |

---

### Phase 7: Transformers Deep Dive (16 lessons, 14h) -> E3扩展

**融合位置**：选修E3 Day 1（LLM基础）

| AEFS课节 | 融入方式 |
|---------|---------|
| P7-01 Why Transformers | E3 Day 1 引用：RNN的问题 |
| P7-02 **Self-Attention from Scratch** | **E3 Day 1 核心引用** |
| P7-03 **Multi-Head Attention** | **E3 Day 1 核心引用** |
| P7-04 Positional Encoding | E3 Day 1 引用：RoPE/ALiBi |
| P7-05 Full Transformer | E3 Day 1 引用 |
| P7-06 BERT | E3 Day 1 引用 |
| P7-07 GPT | E3 Day 1 引用 |
| P7-08 T5, BART | E3 Day 1 引用 |
| P7-09 Vision Transformers | E7 Day 3 引用 |
| P7-10 Audio Transformers | E12 引用 |
| P7-11 **Mixture of Experts (MoE)** | **E3 延伸：MoE架构** |
| P7-12 **KV Cache & Flash Attention** | **技能5 引用：推理优化** |
| P7-13 Scaling Laws | E3 Day 1 引用 |
| P7-14 **Build Transformer from Scratch** | **E3 核心实践** |
| P7-15 Attention Variants | 技能5 延伸：滑动窗口/稀疏注意力 |
| P7-16 Speculative Decoding | 技能5 延伸：推测解码 |

**融合产出**：E3 Day 1中每个Transformer概念标注AEFS引用，建议完成P7-14"从零构建Transformer"作为核心实践。

---

### Phase 8: Generative AI (14 lessons, 14h) -> v4.1 E8 Day 2

**融合位置**：v4.1新教材E8 Day 2（扩散模型与生成AI）

| AEFS课节 | 融入方式 |
|---------|---------|
| P8-01 Generative Models Taxonomy | E8 Day 2 引用：生成模型分类 |
| P8-02 Autoencoders & VAE | E8 Day 2 引用（技能1已有，补充from-scratch） |
| P8-03 GANs | E8 Day 2 引用 |
| P8-04 Conditional GANs & Pix2Pix | E8 Day 2 引用 |
| P8-05 StyleGAN | 延伸阅读 |
| P8-06 **Diffusion Models - DDPM from Scratch** | **E8 Day 2 核心引用** |
| P8-07 **Latent Diffusion & Stable Diffusion** | **E8 Day 2 核心引用** |
| P8-08 ControlNet, LoRA & Conditioning | E8 Day 2 引用 |
| P8-09 Inpainting & Outpainting | E8 Day 2 引用（营销图片编辑） |
| P8-10 Video Generation | E8 Day 2 延伸 |
| P8-11 Audio Generation | E12 引用 |
| P8-12 3D Generation | 延伸阅读 |
| P8-13 Flow Matching & Rectified Flows | E8 Day 2 延伸 |
| P8-14 Evaluation - FID, CLIP Score | E8 Day 2 引用 |

**融合产出**：E8 Day 2的核心概念直接引用AEFS P8-06/07，建议学习者完成AEFS的DDPM from-scratch实现。

---

### Phase 9: Reinforcement Learning (12 lessons, 13h) -> v4.1扩展7

**融合位置**：v4.1扩展7（选修E3 Day 1扩展传统RL基础）

| AEFS课节 | 融入方式 | v4.1缺口 |
|---------|---------|---------|
| P9-01 **MDPs, States, Actions & Rewards** | **E3 Day 1 扩展** | **MDP形式化** |
| P9-02 Dynamic Programming | E3 扩展 | 值迭代/策略迭代 |
| P9-03 Monte Carlo Methods | E3 扩展 | 蒙特卡洛RL |
| P9-04 **Q-Learning, SARSA** | **E3 Day 1 扩展** | **Q-learning** |
| P9-05 **Deep Q-Networks (DQN)** | **E3 Day 1 扩展** | **DQN** |
| P9-06 Policy Gradient - REINFORCE | E3 扩展 | 策略梯度 |
| P9-07 Actor-Critic - A2C, A3C | E3 扩展 | Actor-Critic |
| P9-08 **PPO** | **E3/E9 引用** | **PPO（RLHF基础）** |
| P9-09 **Reward Modeling & RLHF** | **E9 引用** | **RLHF** |
| P9-10 Multi-Agent RL | E1 引用 | 多智能体RL |
| P9-11 Sim-to-Real Transfer | 延伸阅读 | 仿真到现实 |
| P9-12 RL for Games | 延伸阅读 | 游戏RL |

**融合产出**：E3 Day 1扩展中标注"AEFS P9-XX"引用，P9-01/04/05直接填补v4.1已识别的传统RL缺口。

---

### Phase 10: LLMs from Scratch (22 lessons, 26h) -> E3扩展

**融合位置**：选修E3 Day 1-2（LLM基础与应用）

| AEFS课节 | 融入方式 |
|---------|---------|
| P10-01 Tokenizers | E3 Day 1 引用 |
| P10-02 **Building a Tokenizer from Scratch** | **E3 实践** |
| P10-03 Data Pipelines for Pre-Training | E3 Day 1 引用 |
| P10-04 **Pre-Training a Mini GPT (124M)** | **E3 Day 1 核心实践** |
| P10-05 Scaling - Distributed Training | 技能5 延伸 |
| P10-06 Instruction Tuning - SFT | E3 Day 2 引用 |
| P10-07 **RLHF** | E3/E9 引用 |
| P10-08 **DPO** | E3/E9 引用 |
| P10-09 Constitutional AI | E9 引用 |
| P10-10 Evaluation | 技能5 引用 |
| P10-11 **Quantization** | **技能5 引用：量化** |
| P10-12 Inference Optimization | 技能5 引用 |
| P10-13 **Complete LLM Pipeline** | **E3 综合实践** |
| P10-14 Open Models Architecture | E3 延伸 |
| P10-15 Speculative Decoding | 技能5 延伸 |
| P10-16 Differential Attention | 前沿阅读 |
| P10-17 Native Sparse Attention | 前沿阅读 |
| P10-18 Multi-Token Prediction | 前沿阅读 |
| P10-19 DualPipe Parallelism | 前沿阅读 |
| P10-20 **DeepSeek-V3 Walkthrough** | **前沿阅读：DeepSeek架构** |
| P10-21 Jamba Hybrid SSM-Transformer | 前沿阅读 |
| P10-22 Async Inference | 前沿阅读 |

**融合产出**：E3中标注AEFS引用，P10-04"预训练Mini GPT"作为E3的核心from-scratch实践。

---

### Phase 11: LLM Engineering (15 lessons, 17h) -> E3 + 技能5扩展

**融合位置**：选修E3 Day 2-3 + 技能5 Day 2-4

| AEFS课节 | 融入方式 |
|---------|---------|
| P11-01 **Prompt Engineering** | E3 Day 2 引用 |
| P11-02 Few-Shot, CoT, ToT | E3 Day 2 引用 |
| P11-03 Structured Outputs | 技能5 引用 |
| P11-04 **Embeddings & Vector Representations** | 技能1 引用 |
| P11-05 Context Engineering | 技能5 引用 |
| P11-06 **RAG** | **技能5 Day 2 核心引用** |
| P11-07 **Advanced RAG** | **技能5 Day 2 核心引用** |
| P11-08 **Fine-Tuning with LoRA** | E3 Day 2 引用 |
| P11-09 Function Calling & Tool Use | 技能5 引用 |
| P11-10 Evaluation & Testing | 技能5 Day 3 引用 |
| P11-11 Caching & Cost Optimization | 技能5 Day 5 引用 |
| P11-12 Guardrails & Safety | 技能5 Day 4 引用 |
| P11-13 **Production LLM Application** | **技能5 Day 5 综合实践** |
| P11-14 **Model Context Protocol (MCP)** | **技能5 Day 2 核心引用** |
| P11-15 Prompt Caching | 技能5 引用 |

**融合产出**：技能5中RAG和MCP部分直接引用AEFS P11-06/07/14，P11-13作为生产部署综合实践参考。

---

### Phase 12: Multimodal AI (25 lessons, 65h) -> v4.1 E7 Day 3 + E8

**融合位置**：v4.1新教材E7 Day 3 + E8 Day 2-3

AEFS Phase 12是**最深入的多模态AI课程**，25节课覆盖从CLIP到GPT-4o的完整演进：

| AEFS课节 | 映射 | 融入方式 |
|---------|------|---------|
| P12-01 ViT and Patch-Token | E7 Day 3 | Vision Transformer |
| P12-02 **CLIP** | E7 Day 3 | **核心引用** |
| P12-03 BLIP-2 and Q-Former | E7 Day 3 | 模态桥接 |
| P12-04 Flamingo | E7 Day 3 | 门控交叉注意力 |
| P12-05 **LLaVA** | E7 Day 3 | **核心引用：视觉指令微调** |
| P12-06 Any-Resolution Vision | 延伸 | 任意分辨率 |
| P12-07 Open-Weight VLM Recipes | 延伸 | 开源VLM实践 |
| P12-08 LLaVA-OneVision | 延伸 | 单图/多图/视频 |
| P12-09 Qwen-VL Family | 延伸 | Qwen视觉 |
| P12-10 InternVL3 | 延伸 | 原生多模态预训练 |
| P12-11 Chameleon Early-Fusion | 前沿 | 早期融合 |
| P12-12 Emu3 Next-Token | 前沿 | 下一Token预测 |
| P12-13 Transfusion | 前沿 | AR+Diffusion统一 |
| P12-14 Show-o | 前沿 | 离散扩散统一 |
| P12-15 Janus-Pro | 前沿 | 解耦编码器 |
| P12-16 MIO Any-to-Any | 前沿 | 任意到任意 |
| P12-17 Video-Language Grounding | E7 Day 3 | 视频语言时序对齐 |
| P12-18 Long-Video Understanding | 延伸 | 长视频理解 |
| P12-19 Audio-Language Models | E12 引用 | 音频语言模型 |
| P12-20 **Omni Models** | E7 Day 3 | **核心引用：全能模型** |
| P12-21 Embodied VLAs | 延伸 | 具身智能 |
| P12-22 **Document Understanding** | E7 Day 2 | **文档理解（营销物料）** |
| P12-23 **ColPali Document RAG** | 技能5 引用 | **视觉原生RAG** |
| P12-24 **Multimodal RAG** | 技能5 引用 | **多模态RAG** |
| P12-25 Multimodal Agents | 技能5 引用 | 多模态Agent |

**融合产出**：E7 Day 3深度引用P12-02/05/20，技能5引用P12-23/24/25作为多模态RAG和Agent的参考。

---

### Phase 13: Tools & Protocols (23 lessons, 24.5h) -> 技能5扩展

**融合位置**：技能5 Day 2-4（Agent编排 + MCP）

| AEFS课节 | 融入方式 |
|---------|---------|
| P13-01 The Tool Interface | 技能5 Day 2 引用 |
| P13-02 Function Calling Deep Dive | 技能5 Day 2 引用 |
| P13-03 Parallel & Streaming Tool Calls | 技能5 延伸 |
| P13-04 Structured Output | 技能5 引用 |
| P13-05 Tool Schema Design | 技能5 引用 |
| P13-06 **MCP Fundamentals** | **技能5 Day 2 核心引用** |
| P13-07 **Building an MCP Server** | **技能5 Day 2 核心实践** |
| P13-08 Building an MCP Client | 技能5 实践 |
| P13-09 MCP Transports | 技能5 引用 |
| P13-10 MCP Resources and Prompts | 技能5 引用 |
| P13-11 MCP Sampling | 技能5 引用 |
| P13-12 MCP Roots and Elicitation | 技能5 引用 |
| P13-13 MCP Async Tasks | 技能5 延伸 |
| P13-14 MCP Apps | 技能5 延伸 |
| P13-15 **MCP Security - Tool Poisoning** | **技能5 Day 4 引用** |
| P13-16 **MCP Security - OAuth 2.1** | **技能5 Day 4 引用** |
| P13-17 MCP Gateways and Registries | 技能5 延伸 |
| P13-18 MCP Auth in Production | 技能5 延伸 |
| P13-19 **A2A Protocol** | **E1 引用：Agent-to-Agent协议** |
| P13-20 OpenTelemetry GenAI | 技能5 Day 3 引用 |
| P13-21 LLM Routing Layer | 技能5 Day 5 引用 |
| P13-22 Skills and Agent SDKs | 技能5 引用 |
| P13-23 Capstone - Tool Ecosystem | 技能5 作业 |

**融合产出**：技能5中MCP部分直接引用AEFS P13-06~18，这是目前最完整的MCP教学资源。A2A协议引用到E1。

---

### Phase 14: Agent Engineering (42 lessons, 42h) -> E1 + 技能5扩展

**融合位置**：选修E1（Agentic AI）+ 技能5 Day 1-3

AEFS Phase 14是**全球最深入的Agent工程课程**，42节课从Agent Loop到生产级Workbench：

| AEFS课节组 | 融入方式 |
|-----------|---------|
| P14-01~06 Agent基础（Loop/ReWOO/Reflexion/ToT/Self-Refine/Tool Use） | E1 Day 1 引用 |
| P14-07~10 Agent记忆（Virtual Context/Memory Blocks/Hybrid Memory/Skill Libraries） | **E1 Day 2 核心引用** |
| P14-11~14 编排（HTN/Anthropic Patterns/Stateful Graph/Actor Model） | **技能5 Day 2 核心引用** |
| P14-15~18 Agent团队（Role-Based/OpenAI SDK/Harness/Runtime） | E1 Day 3 引用 |
| P14-19~22 评估与Computer Use（Benchmarks/WebArena/Computer Use/Voice Agents） | **技能5 Day 3 核心引用** |
| P14-23~24 可观测性（OpenTelemetry/Langfuse/Phoenix） | 技能5 Day 3 引用 |
| P14-25~28 多Agent与安全（Debate/Failure Modes/Prompt Injection/Orchestration） | **技能5 Day 4 核心引用** |
| P14-29~31 生产运行时（Queue/Event/Cron + Eval-Driven Dev） | 技能5 Day 5 引用 |
| P14-31~42 **Agent Workbench系列**（12节课，从Workbench设计到实战） | **E1/技能5 综合实践** |

**融合产出**：E1和技能5中大量引用AEFS Phase 14。特别是P14-07~10的Agent记忆系列和P14-31~42的Workbench系列，这两块是现有教材最薄弱的部分。

---

### Phase 15: Autonomous Systems (22 lessons, 20h) -> E1高级扩展

**融合位置**：选修E1 延伸阅读（高级主题）

| AEFS课节组 | 融入方式 |
|-----------|---------|
| P15-01~08 自改进Agent（METR/STaR/AlphaEvolve/Darwin Gödel/AI Scientist/Recursive Self-Improvement） | E1 前沿阅读 |
| P15-09~16 自主Agent安全（Permission Modes/Browser Agents/Durable Execution/Action Budgets/Kill Switches/HITL/Checkpoints） | **技能5 Day 4 引用** |
| P15-17~22 安全框架（Constitutional AI/Llama Guard/RSP/Preparedness Framework/METR/CAIS） | E9 引用 |

**融合产出**：作为E1和技能5 Day 4的前沿延伸阅读材料，不作为必修内容。

---

### Phase 16: Multi-Agent & Swarms (25 lessons, 28h) -> E1 Day 3 + E10扩展

**融合位置**：选修E1 Day 3（多Agent系统设计）+ 选修E10（Agent经济）

| AEFS课节组 | 融入方式 |
|-----------|---------|
| P16-01~04 多Agent基础（Why/FIPA-ACL/Protocols/Primitive Model） | E1 Day 3 引用 |
| P16-05~08 架构模式（Supervisor/Hierarchical/Society of Mind/Role Specialization） | **E1 Day 3 核心引用** |
| P16-09~11 拓扑结构（Parallel Swarm/Group Chat/Handoffs） | E1 Day 3 引用 |
| P16-12 **A2A Protocol** | **E1 Day 3 核心引用** |
| P16-13~14 共享记忆与共识（Blackboard/Consensus/BFT） | **E1 Day 3 核心引用** |
| P16-15~16 投票与协商（Voting/Negotiation） | E10 引用 |
| P16-17~18 生成式Agent与心智理论 | E10 前沿阅读 |
| P16-19 Swarm Optimization (PSO/ACO) | 延伸阅读 |
| P16-20 **MARL (MADDPG/QMIX/MAPPO)** | **E1 前沿引用** |
| P16-21 **Agent Economies** | **E10 核心引用** |
| P16-22~25 生产扩展与故障模式 | 技能5 引用 |

**融合产出**：E1 Day 3深度引用P16-05~14，E10引用P16-21的Agent Economies内容。

---

### Phase 17: Infrastructure & Production (28 lessons, 32h) -> v4.1扩展4

**融合位置**：v4.1扩展4（技能5 Day 5 MLOps扩展）

| AEFS课节组 | 融入方式 | v4.1缺口 |
|-----------|---------|---------|
| P17-01~03 平台（Bedrock/Azure/Vertex + Economics + GPU Autoscaling） | 技能5 Day 5 引用 | 云平台 |
| P17-04~08 **推理引擎**（PagedAttention/Continuous Batching/Speculative Decoding/Prefix-Cache/FP8） | **技能5 Day 5 核心引用** | **推理优化** |
| P17-09~10 **量化**（AWQ/GPTQ/GGUF/FP8 + Cold Start） | **技能5 Day 5 核心引用** | **量化部署** |
| P17-11~12 多区域与边缘 | 延伸阅读 | - |
| P17-13~14 可观测性与缓存 | 技能5 Day 3 引用 | - |
| P17-15~16 Batch API与模型路由 | 技能5 Day 5 引用 | 成本优化 |
| P17-17~18 **分离式推理**（Prefill/Decode分离） | **前沿阅读** | - |
| P17-19~20 AI网关与部署策略 | 技能5 Day 5 引用 | - |
| P17-21~22 **A/B测试与负载测试** | **技能5 Day 5 引用** | **实验部署** |
| P17-23~24 SRE与混沌工程 | 延伸阅读 | - |
| P17-25~26 **安全与合规**（PII/SOC2/HIPAA/GDPR/EU AI Act） | **技能5 Day 4 / E9 引用** | **合规** |
| P17-27 **FinOps** | **技能5 Day 5 核心引用** | **成本管理** |
| P17-28 Self-Hosted Serving | 延伸阅读 | - |

**融合产出**：技能5 Day 5扩展中直接引用AEFS P17-04~10/27，填补v4.1已识别的MLOps/推理优化/FinOps缺口。

---

### Phase 18: Ethics, Safety & Alignment (30 lessons, 31h) -> E9扩展

**融合位置**：选修E9（AI安全与对齐）

| AEFS课节组 | 融入方式 |
|-----------|---------|
| P18-01~05 对齐基础（Instruction Following/Reward Hacking/DPO Family/Sycophancy/Constitutional AI） | E9 Day 1 引用 |
| P18-06~09 **欺骗性对齐**（Mesa-Optimization/Sleeper Agents/In-Context Scheming/Alignment Faking） | **E9 Day 1 前沿引用** |
| P18-10~11 AI Control & Scalable Oversight | E9 延伸 |
| P18-12~14 **红队**（PAIR/Many-Shot/ASCII Jailbreaks） | **E9 Day 2 核心引用** |
| P18-15 **间接Prompt注入** | **技能5 Day 4 / E9 核心引用** |
| P18-16 **红队工具**（Garak/Llama Guard/PyRIT） | **E9 Day 2 核心引用** |
| P18-17 WMDP & Dual-Use | E9 延伸 |
| P18-18 Safety Frameworks (RSP/PF/FSF) | E9 Day 3 引用 |
| P18-19 Model Welfare | 前沿阅读 |
| P18-20~21 **偏见与公平性** | **E9 / 模块R6 引用** |
| P18-22 **差分隐私** | **技能1 扩展引用** |
| P18-23 **水印**（SynthID/C2PA） | E9 引用 |
| P18-24 **监管框架**（EU/US/UK/Korea） | **E9 Day 3 核心引用** |
| P18-25 EchoLeak & CVEs | 延伸 |
| P18-26 Model/System/Dataset Cards | 模块R6 引用 |
| P18-27 Data Provenance | 模块R6 引用 |
| P18-28 Alignment Research Ecosystem | 前沿阅读 |
| P18-29 Moderation Systems | E9 引用 |
| P18-30 Dual-Use Risk | E9 延伸 |

**融合产出**：E9扩展中大量引用AEFS Phase 18。P18-06~09的欺骗性对齐系列和P18-12~16的红队系列是E9现有内容的强力补充。

---

### Phase 19: Capstone Projects (87 projects, 620h) -> Capstone项目库

**融合位置**：Capstone教材（项目库引用）

AEFS的87个Capstone项目按主题分类：

| 项目组 | 数量 | 映射到博士Capstone |
|--------|:---:|-------------------|
| Agent Workbench系列 (P19-20~29) | 10 | Capstone Phase 3（Agent系统架构） |
| LLM from Scratch系列 (P19-30~41) | 12 | E3 综合实践 |
| AI Scientist系列 (P19-50~57) | 8 | Capstone Phase 1（研究自动化） |
| Vision/VLM系列 (P19-58~63) | 6 | E7 综合实践 |
| RAG系列 (P19-64~69) | 6 | 技能5 / Capstone Phase 2 |
| Eval系列 (P19-70~75) | 6 | 技能5 Day 3 |
| 分布式训练系列 (P19-76~81) | 6 | 技能5 Day 5 |
| 安全系列 (P19-82~87) | 6 | E9 / 技能5 Day 4 |
| 独立Capstone项目 (P19-01~17) | 17 | Capstone参考项目库 |

**推荐的Capstone参考项目**（与博士论文方向最相关）：

| AEFS项目 | 博士Capstone关联 |
|---------|-----------------|
| P19-02 RAG over Codebase | Capstone Phase 2（知识图谱+RAG） |
| P19-04 Multimodal Document QA | 营销物料多模态分析 |
| P19-05 Autonomous Research Agent | Capstone Phase 1（研究自动化） |
| P19-08 Production RAG Chatbot | Capstone Phase 3（生产级系统） |
| P19-10 Multi-Agent Software Team | Capstone Phase 3（多Agent协作） |
| P19-11 LLM Observability Dashboard | 技能5 Day 3（评估可视化） |
| P19-13 MCP Server with Registry | 技能5 Day 2（MCP实践） |

**融合产出**：Capstone教材中新增"AEFS项目库"章节，列出87个项目并标注与博士Capstone各阶段的关联。

---

## 四、新增选修E12：语音AI与音频处理

### 教材设计

| 属性 | 内容 |
|------|------|
| **学时** | 6h |
| **对应技能** | 技能1+5深化 |
| **对标** | AEFS Phase 6 (17 lessons) |
| **与营销关联** | 语音搜索、播客分析、语音客服、品牌声音识别、语音广告 |

**三天教学计划**：

Day 1 - 音频基础与处理
- 数字音频基础：波形/采样率/位深/通道/编码格式（WAV/MP3/FLAC）
- 傅里叶变换与频谱分析：STFT/频谱图/Mel尺度/MFCC
- Python代码：用librosa加载和可视化音频波形与频谱图
- 音频分类：环境音分类/音乐流派分类
- Python代码：用torch音频分类模型

Day 2 - 语音识别与合成
- ASR（自动语音识别）：声学模型+语言模型、CTC/Attention机制
- Whisper架构详解：多语言/多任务/零样本迁移
- Python代码：用Whisper转录播客音频并提取关键内容
- TTS（文本转语音）：Tacotron/FastSpeech/VITS架构
- Python代码：用edge-tts生成营销语音广告
- 说话人识别与验证：声纹识别原理
- 语音助手Pipeline：ASR->LLM->TTS完整链路

Day 3 - 语音AI营销应用
- 语音搜索优化：如何让品牌内容在语音搜索中被发现
- 播客内容分析：自动转录->主题提取->情感分析->关键洞察
- 语音客服系统设计：意图识别+对话管理+语音合成
- 品牌声音识别：音频品牌化（Audio Branding）与声纹注册
- 语音广告效果评估：完听率/互动率/转化率
- 综合案例：构建一个播客营销分析Pipeline

**代码示例**：
- Python: 用Whisper转录+摘要播客内容
- Python: 用librosa分析音频特征
- Python: 用edge-tts生成语音广告

**作业**：
- 必做：用Whisper对一段10分钟播客做转录+主题提取+关键洞察摘要
- 挑战：设计一个语音客服系统的技术方案（含ASR/LLM/TTS选型和架构图）

---

## 五、v4.1迭代计划的更新

融合AEFS后，v4.1迭代计划需要以下更新：

### 5.1 新增教材变化

| v4.1原计划 | v4.2更新 |
|-----------|---------|
| 6份新教材（E4-E8, E11） | 7份新教材（+E12语音AI） |
| 选修池11门 | 选修池12门 |

### 5.2 新教材内容增强

| 新教材 | v4.1原内容来源 | v4.2增强（AEFS引用） |
|--------|-------------|-------------------|
| E4 商业智能 | 自编 | 无AEFS对应（AEFS无BI/Tableau内容） |
| E5 GenAI应用 | 自编 | 无AEFS对应（AEFS无无代码/低代码内容） |
| E6 应用统计 | 自编 | 引用AEFS P1-16/18 + P2-15/16 |
| E7 计算机视觉 | 自编 | **深度引用AEFS P4全部28节** |
| E8 深度学习进阶 | 自编 | **深度引用AEFS P3全部13节 + P8全部14节** |
| E11 推荐系统 | 自编 | 引用AEFS P5-14 + P11-04 |
| **E12 语音AI** | **新增** | **基于AEFS P6全部17节** |

### 5.3 扩展内容增强

| v4.1扩展 | v4.2增强（AEFS引用） |
|---------|-------------------|
| 技能0 Day 7 | 引用AEFS P0-07(Docker) + P0-12(Debugging) |
| 技能0 ML算法 | **深度引用AEFS P2-04/05/06(SVM/KNN/决策树)** |
| 技能0 NoSQL | 无AEFS对应 |
| 技能5 MLOps | **深度引用AEFS P17全部28节** |
| E2 数据叙事 | 无AEFS对应 |
| E1 RPA | 无AEFS对应 |
| E3 传统RL | **深度引用AEFS P9全部12节** |
| 技能1 GNN | 引用AEFS P1-21(Graph Theory) |

### 5.4 现有教材AEFS引用增强

| 现有教材 | 增强内容 |
|---------|---------|
| 技能0 | P0(开发工具) + P1(数学基础) + P2(ML基础) 引用 |
| 技能1 | P5-03/22/26(词嵌入/NER/知识图谱) 引用 |
| 技能2 | 无直接AEFS对应 |
| 技能3 | P1-07/16(贝叶斯/采样) 引用 |
| 技能4 | 无直接AEFS对应 |
| 技能5 | **P11(LLM工程) + P13(工具协议) + P14(Agent工程) + P17(基础设施) 大量引用** |
| 模块R | 无直接AEFS对应 |
| E1 Agentic AI | **P14(Agent工程42节) + P16(多Agent25节) 深度引用** |
| E2 Marketing Analytics | P5-05/15(情感分析/主题模型) 引用 |
| E3 LLM导论 | **P7(Transformers) + P10(LLM from Scratch) + P11(LLM工程) 深度引用** |
| E9 AI安全 | **P18(伦理安全30节) 深度引用** |
| E10 Agent经济 | P16-21(Agent Economies) 引用 |
| Capstone | **P19(87个项目) 项目库引用** |

---

## 六、版本变化总结

| 项目 | v4.0 | v4.1 | v4.2 |
|------|------|------|------|
| 独立教材 | 13份 | 19份 | 20份(+E12) |
| 选修课 | 5门 | 11门 | 12门 |
| AEFS引用课节数 | 0 | 0 | 503节全覆盖 |
| Capstone项目库 | 0 | 0 | 87个项目 |
| 新增内容 | - | 6份新教材+8处扩展 | +1份新教材(E12)+现有教材AEFS引用 |

### v4.2实施优先级

| 优先级 | 任务 | 依赖 |
|:-----:|------|------|
| P0 | 在所有现有教材中添加AEFS引用标注 | 无（可直接执行） |
| P0 | 产出E7/E8新教材（引用AEFS P3/P4/P8/P12） | v4.1计划 |
| P1 | 产出E6新教材（引用AEFS P1/P2/P9） | v4.1计划 |
| P1 | 产出E12新教材（基于AEFS P6） | v4.2新增 |
| P1 | 技能0扩展（引用AEFS P0/P1/P2） | v4.1计划 |
| P2 | 技能5扩展（引用AEFS P11/P13/P14/P17） | v4.1计划 |
| P2 | E3扩展（引用AEFS P7/P9/P10） | v4.1计划 |
| P2 | E1扩展（引用AEFS P14/P16） | v4.1计划 |
| P3 | E9扩展（引用AEFS P18） | v4.1计划 |
| P3 | Capstone项目库（引用AEFS P19） | v4.1计划 |
| P3 | 产出E4/E5/E11新教材 | v4.1计划 |
| P3 | README更新 | 全部完成后 |

---

## 七、引用格式规范

在教材中添加AEFS引用时使用统一格式：

```
> 🔗 **延伸实践**：本节的from-scratch实现详见 [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) 
> Phase X · Lesson Y: [课节名称](链接)
> 预计时长：~XX min
```

示例：
```
> 🔗 **延伸实践**：反向传播的from-scratch实现详见 AEFS Phase 3 · Lesson 03: Backpropagation from Scratch
> 预计时长：~75 min
```

---

*本方案将AI Engineering from Scratch的503节课程系统融入博士课程体系，使每个技术模块都获得"from scratch实现深度"的支撑，同时保持商业博士的研究导向定位。*
