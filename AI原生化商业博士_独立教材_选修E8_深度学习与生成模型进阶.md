# 选修E8：深度学习与生成模型进阶

> **版本**：v4.2 | **日期**：2026-07-30 | **学时**：6h
> **修读者**：aha.gare
> **对标AEFS阶段**：Phase 3 (Deep Learning Core, 13 lessons) + Phase 7 (Transformers, 16 lessons) + Phase 8 (Generative AI, 14 lessons) + Phase 1 (Math Foundations, Lesson 21) + Phase 12 (Multimodal AI,前沿课节)
> **对标大学**：Stanford CS231n / CS224N / MIT 6.S191 / DeepLearning.AI
> **前置条件**：完成技能0（Python+统计基础）；了解神经网络基本概念（建议同时选修E7）
> **课程哲学**：不理解深度学习的地基，就无法理解生成AI的摩天大楼--从感知机到扩散模型，每一步数学推导都是通向AI原生营销能力的阶梯

---

## 课程概述

### 定位

本选修课是AI原生化商业博士课程中最"硬核"的技术深度课，系统覆盖深度学习基础架构（CNN/RNN/LSTM）、生成模型（VAE/GAN/Diffusion）和图神经网络（GNN）三大领域。

与E7（计算机视觉）侧重"视觉应用"不同，E8侧重"模型原理"--为什么卷积能提取特征？为什么扩散模型能生成逼真图像？为什么LSTM能记住长序列？本课程要求学习者不仅会用PyTorch调用API，更要理解每个架构背后的数学直觉和工程权衡。每个技术概念都标注AEFS对应课节，AEFS的"from scratch"实现哲学与本课程完美契合--真正理解一个算法的最好方式就是从零实现它。

对于售前解决方案产品经理而言，这门课的价值在于：当客户问"为什么用扩散模型而不是GAN""为什么需要LoRA微调""GNN能解决什么业务问题"时，你能够给出有技术深度的回答，而不只是调用API。

### 学习目标

完成本课程后，学习者将能够：

1. **掌握深度学习核心组件的原理**：从感知机到反向传播，理解激活函数、损失函数、优化器、正则化的数学含义和工程选择
2. **理解CNN和RNN/LSTM的架构设计**：解释卷积梯度传播、特征可视化（CAM/Grad-CAM）、LSTM门控机制、Seq2Seq+Attention演进
3. **理解生成模型的完整谱系**：区分VAE/GAN/Diffusion/Flow的技术路线，掌握DDPM数学推导和Stable Diffusion架构
4. **掌握LoRA/ControlNet等可控生成技术**：理解参数高效微调原理，能用diffusers库生成营销创意图片
5. **理解GNN基础与前沿**：掌握消息传递机制和GCN/GraphSAGE/GAT架构，了解Transfusion/Janus-Pro等统一模型前沿

### 与主课程的关联

| 关联技能/选修 | 关联点 |
|-------------|--------|
| 选修E7 计算机视觉 | E8 Day 1的CNN基础是E7 Day 1的前置深化；E8 Day 2的扩散模型补充E7未覆盖的生成内容 |
| 选修E3 LLM导论 | E8 Day 1的Seq2Seq+Attention是Transformer的前置知识 |
| 技能1 表示工程 | E8 Day 3的GNN与技能1的知识图谱部分互补 |
| 技能5 Agentic系统工程 | 理解模型内部机制有助于Agent系统设计中的模型选型和调优 |

---

## 学习计划表（3天 · 6h）

| 天次 | 主题 | 时长 | 核心产出 | AEFS引用 |
|:---:|------|:----:|---------|---------|
| Day 1 | 深度学习架构全景 | 2h | 从零理解CNN/RNN/LSTM，能用PyTorch实现LSTM和CNN | P3-01~13, P7-01~05, P7-14 |
| Day 2 | 扩散模型与生成AI | 2h | 理解VAE/GAN/Diffusion原理，能用diffusers生成营销图片 | P8-01~03, P8-06~09, P8-13~14 |
| Day 3 | 图神经网络与前沿 | 2h | 理解GNN消息传递，能用PyG实现GCN，了解统一模型前沿 | P1-21, P12-12~13, P12-15 |

---

## 详细学习内容

### Day 1：深度学习架构全景

#### 1.1 感知机与多层网络

**感知机（Perceptron）**是神经网络的最小单元，由Rosenblatt在1958年提出。它模拟单个神经元的行为：

$$y = \sigma(\mathbf{w}^T \mathbf{x} + b)$$

其中 $\mathbf{x}$ 是输入向量，$\mathbf{w}$ 是权重，$b$ 是偏置，$\sigma$ 是激活函数。感知机的输出是对输入的加权求和再经过非线性变换。

**从感知机到多层网络**：

单个感知机只能解决线性可分问题（如AND/OR），无法解决XOR（异或）问题。多层感知机（MLP）通过堆叠多个感知机层来解决非线性问题：

```
输入层 -> 隐藏层1 -> 隐藏层2 -> ... -> 输出层
```

每一层的输出是下一层的输入，层与层之间全连接。隐藏层的非线性激活函数使网络能够拟合任意复杂的函数（万能逼近定理，Universal Approximation Theorem）。

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 01: [The Perceptron](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/01-the-perceptron) 和 Lesson 02: [Multi-Layer Networks](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/02-multi-layer-networks)
> 预计时长：~60 min + ~60 min

#### 1.2 反向传播从零实现

反向传播（Backpropagation）是训练神经网络的核心算法--它通过链式法则（Chain Rule）高效计算损失函数对每个参数的梯度。

**链式法则回顾**：

如果 $y = f(g(x))$，则 $\frac{dy}{dx} = \frac{df}{dg} \cdot \frac{dg}{dx}$。

在多层网络中，输出层的损失需要逐层回传到每个参数。反向传播的"反向"指的是梯度从输出层向输入层方向计算。

**反向传播的四步循环**：

```
1. 前向传播（Forward Pass）：
   输入 -> 逐层计算 -> 输出 -> 计算损失 L

2. 计算输出层梯度：
   ∂L/∂(输出层输出)

3. 反向传播（Backward Pass）：
   利用链式法则逐层计算 ∂L/∂w 和 ∂L/∂b

4. 参数更新：
   w <- w - η · ∂L/∂w   (η 为学习率)
   b <- b - η · ∂L/∂b
```

**从零实现反向传播的伪代码**（不使用PyTorch的autograd）：

```python
# 简化的两层网络反向传播
import numpy as np

# 前向传播
z1 = X @ W1 + b1          # 第一层线性变换
a1 = np.maximum(0, z1)     # ReLU激活
z2 = a1 @ W2 + b2          # 第二层线性变换
a2 = softmax(z2)           # Softmax输出概率

# 计算损失（交叉熵）
loss = -np.sum(y_true * np.log(a2)) / N

# 反向传播
dz2 = (a2 - y_true) / N                    # 输出层梯度
dW2 = a1.T @ dz2                            # W2的梯度
db2 = np.sum(dz2, axis=0)                   # b2的梯度
da1 = dz2 @ W2.T                            # 传播到第一层
dz1 = da1 * (z1 > 0)                        # ReLU的梯度（z1>0时为1，否则为0）
dW1 = X.T @ dz1                             # W1的梯度
db1 = np.sum(dz1, axis=0)                   # b1的梯度

# 参数更新
W1 -= lr * dW1
b1 -= lr * db1
W2 -= lr * dW2
b2 -= lr * db2
```

**理解要点**：ReLU的梯度非常简单--正数区域梯度为1，负数区域梯度为0。这正是ReLU比Sigmoid更受欢迎的原因之一：梯度不易消失。

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 03: [Backpropagation](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/03-backpropagation)
> 预计时长：~75 min

#### 1.3 激活函数：ReLU、Sigmoid与GELU

激活函数引入非线性，是神经网络能够拟合复杂函数的关键。

| 激活函数 | 公式 | 优点 | 缺点 | 典型用途 |
|---------|------|------|------|---------|
| **Sigmoid** | $\sigma(x) = \frac{1}{1+e^{-x}}$ | 输出在(0,1)，适合概率输出 | 梯度消失（x很大/很小时梯度趋近0）、非零中心 | 二分类输出层 |
| **Tanh** | $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ | 零中心，比Sigmoid梯度更大 | 仍有梯度消失问题 | RNN隐藏层 |
| **ReLU** | $\max(0, x)$ | 计算简单、梯度不消失（正区）、收敛快 | "死亡ReLU"（负区梯度恒为0） | CNN/MLP隐藏层（默认选择） |
| **Leaky ReLU** | $\max(0.01x, x)$ | 解决死亡ReLU | 需调斜率超参 | 深层网络 |
| **GELU** | $x \cdot \Phi(x)$ | 平滑可导、概率启发、Transformer标配 | 计算稍复杂 | Transformer/BERT/GPT |

**GELU的直觉**：GELU（Gaussian Error Linear Unit）可以理解为"以输入值的大小为概率决定是否激活"--输入越大越可能被保留，输入越小越可能被置零。它比ReLU更平滑，在Transformer中表现更好。

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 04: [Activation Functions](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/04-activation-functions)
> 预计时长：~60 min

#### 1.4 损失函数：MSE、交叉熵与对比损失

损失函数衡量模型预测与真实标签的差距，是优化的目标。

**均方误差（MSE）**：

$$\mathcal{L}_{MSE} = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2$$

适用于回归任务。梯度为 $\frac{\partial \mathcal{L}}{\partial \hat{y}} = \frac{2}{N}(\hat{y} - y)$，与预测误差成正比。

**交叉熵损失（Cross-Entropy Loss）**：

$$\mathcal{L}_{CE} = -\sum_{i=1}^{C} y_i \log(\hat{y}_i)$$

适用于分类任务。其中 $y_i$ 是one-hot编码的真实标签，$\hat{y}_i$ 是Softmax输出的预测概率。当预测概率与真实标签一致时损失趋近0。

**对比损失（Contrastive Loss）**：

$$\mathcal{L}_{contrast} = -\log\frac{\exp(\text{sim}(z_i, z_j^+)/\tau)}{\sum_k \exp(\text{sim}(z_i, z_k)/\tau)}$$

用于学习嵌入表示（如CLIP）。正样本对（$z_j^+$）的相似度被拉近，负样本对的相似度被推远。$\tau$ 是温度参数。

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 05: [Loss Functions](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/05-loss-functions)
> 预计时长：~60 min

#### 1.5 优化器：SGD、Momentum、Adam与AdamW

优化器决定如何利用梯度更新参数，直接影响训练速度和最终效果。

| 优化器 | 核心思想 | 公式（简化） | 特点 |
|--------|---------|-------------|------|
| **SGD** | 沿梯度方向更新 | $w \leftarrow w - \eta \cdot g$ | 简单但收敛慢，易卡在鞍点 |
| **Momentum** | 累积历史梯度方向 | $v \leftarrow \beta v + g$; $w \leftarrow w - \eta v$ | 加速收敛，减少震荡 |
| **Adam** | 自适应学习率 + 动量 | 结合一阶矩和二阶矩估计 | 最常用，自动调学习率 |
| **AdamW** | Adam + 解耦权重衰减 | 将权重衰减从梯度中分离 | Transformer训练标配，比Adam泛化更好 |

**Adam的工作原理直觉**：
- 维护梯度的移动平均（一阶矩，类似Momentum）--决定更新方向
- 维护梯度平方的移动平均（二阶矩）--自动调整每个参数的学习率
- 梯度变化大的参数学习率自动减小，梯度稳定的参数学习率保持

**实践建议**：CNN常用SGD+Momentum（泛化更好），Transformer使用AdamW（稳定性更好）。学习率是最重要的超参数，建议用学习率预热（Warmup）+余弦退火（Cosine Annealing）策略。

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 06: [Optimizers](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/06-optimizers) 和 Lesson 09: [Learning Rate Schedules](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/09-learning-rate-schedules)
> 预计时长：~75 min + ~45 min

#### 1.6 正则化：Dropout、Weight Decay与BatchNorm

正则化防止过拟合，提升模型的泛化能力。

**Dropout**：训练时随机将部分神经元输出置零（如概率p=0.5），测试时使用全部神经元但输出乘以(1-p)。直觉：迫使网络不依赖任何单个神经元，学习更鲁棒的特征表示。

**Weight Decay（权重衰减/L2正则）**：在损失函数中加入权重的L2范数惩罚 $\mathcal{L}_{total} = \mathcal{L} + \lambda \sum w^2$，迫使权重保持较小值，防止模型过于复杂。

**Batch Normalization（批归一化）**：在每个mini-batch内对中间层输出进行标准化（均值为0，方差为1），然后通过可学习的缩放和平移参数恢复表示能力。效果：(1) 加速训练；(2) 允许使用更大学习率；(3) 轻微的正则化效果。

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 07: [Regularization](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/07-regularization) 和 Lesson 08: [Weight Initialization](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/08-weight-initialization)
> 预计时长：~60 min + ~45 min

#### 1.7 CNN深入：卷积梯度传播与特征可视化

**卷积层的梯度传播**：

卷积层的前向传播是卷积运算，其反向传播本质上是"转置卷积"（Transposed Convolution）--将梯度从输出层"展开"回输入层。具体来说：
- 对权重的梯度：将输入特征图与输出梯度做卷积
- 对输入的梯度：将输出梯度与翻转的卷积核做"全卷积"（Full Convolution）

**特征可视化：CAM与Grad-CAM**：

理解CNN"看到了什么"对于建立模型信任至关重要，特别是在营销场景中需要解释模型决策。

- **CAM（Class Activation Mapping）**：通过全局平均池化层的权重直接可视化每个空间位置对分类决策的贡献。限制：要求网络结构中有GAP层。
- **Grad-CAM**：使用最后卷积层输出对目标类别的梯度，计算各通道的重要性权重，生成热力图。适用范围更广，不需要特定网络结构。

$$\text{Grad-CAM}(x, y) = \text{ReLU}\left(\sum_k \alpha_k \cdot A_k(x, y)\right)$$

其中 $\alpha_k = \frac{1}{Z}\sum_{x,y} \frac{\partial y^c}{\partial A_k(x,y)}$ 是第k个通道的重要性权重，$A_k$ 是第k个通道的特征图。ReLU确保只显示正贡献区域。

**营销应用**：Grad-CAM可以展示CNN在分类产品图片时"关注"了哪个区域--如果模型关注的是背景而非产品本身，说明训练数据可能存在偏差。

#### 1.8 RNN架构：隐状态与梯度消失/爆炸

**RNN（Recurrent Neural Network）** 用于处理序列数据（文本、时间序列、购买行为序列）。核心思想是维护一个隐状态（Hidden State），在每个时间步更新：

$$h_t = \tanh(W_h h_{t-1} + W_x x_t + b)$$

隐状态 $h_t$ 编码了到时间步 $t$ 为止的序列信息。输出 $y_t = W_y h_t + b_y$。

**梯度消失/爆炸问题**：

在反向传播时，梯度需要穿过所有时间步。由于每一步都乘以权重矩阵 $W_h$，经过T步后梯度变为 $W_h^T$。如果 $W_h$ 的特征值小于1，梯度指数衰减（消失）；如果大于1，梯度指数增长（爆炸）。

这导致标准RNN难以学习长距离依赖--它"记住"了最近的输入但"忘记"了很久以前的输入。

#### 1.9 LSTM详解：遗忘门、输入门与输出门

**LSTM（Long Short-Term Memory）** 通过精心设计的门控机制解决RNN的梯度消失问题。

**LSTM的三个门**：

| 门 | 公式 | 作用 |
|---|------|------|
| **遗忘门（Forget Gate）** | $f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$ | 决定从细胞状态中丢弃什么信息（0=遗忘, 1=保留） |
| **输入门（Input Gate）** | $i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$ | 决定哪些新信息被写入细胞状态 |
| **输出门（Output Gate）** | $o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$ | 决定细胞状态的哪些部分作为输出 |

**细胞状态更新**：

$$\tilde{C}_t = \tanh(W_C [h_{t-1}, x_t] + b_C) \quad \text{(候选信息)}$$
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t \quad \text{(更新细胞状态)}$$
$$h_t = o_t \odot \tanh(C_t) \quad \text{(输出隐状态)}$$

其中 $\odot$ 是逐元素乘法。

**LSTM为什么能解决梯度消失**：

细胞状态 $C_t$ 的更新是加法操作（$f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$），而非乘法。这意味着梯度可以通过细胞状态直接回传，不需要反复乘以权重矩阵。遗忘门 $f_t$ 可以学习到"接近1"的值，使长期信息得以保留。

**GRU（Gated Recurrent Unit）对比**：

GRU是LSTM的简化版，将遗忘门和输入门合并为更新门（Update Gate），合并细胞状态和隐状态。参数更少、训练更快，在多数任务上效果与LSTM相当。

| 维度 | LSTM | GRU |
|------|------|-----|
| 门数量 | 3个（遗忘/输入/输出） | 2个（更新/重置） |
| 状态 | 细胞状态 + 隐状态 | 仅隐状态 |
| 参数量 | 较多 | 较少（约LSTM的75%） |
| 长序列 | 略优 | 接近 |
| 训练速度 | 较慢 | 较快 |

> 🔗 **延伸实践**：AEFS Phase 3的完整深度学习核心课程（13节课）提供了从感知机到调试的全链路from-scratch实现。建议完成P3-10 [Mini Framework](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/10-mini-framework)（~90 min）构建自己的mini深度学习框架，以及P3-11 [Intro to PyTorch](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/11-intro-to-pytorch)（~60 min）和P3-13 [Debugging Neural Networks](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/13-debugging-neural-networks)（~60 min）

#### 1.10 Seq2Seq + Attention演进

**Seq2Seq（序列到序列）** 模型用编码器-解码器架构处理变长输入输出序列：

```
编码器 LSTM: 输入序列 -> 最终隐状态（上下文向量 context vector）
解码器 LSTM: 上下文向量 -> 输出序列
```

**问题**：整个输入序列被压缩为一个固定长度的上下文向量，信息瓶颈严重--长序列的前端信息容易被"挤压"丢失。

**Attention机制**的引入解决了这个问题：

解码器在每一步不再只依赖固定的上下文向量，而是"注意"输入序列的不同部分：

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

其中 $Q$（Query）来自解码器当前状态，$K$（Key）和 $V$（Value）来自编码器所有时间步的隐状态。注意力权重 $\text{softmax}(QK^T/\sqrt{d_k})$ 决定了在当前解码步骤应该"关注"输入序列的哪些位置。

**从Attention到Transformer**：

2017年Google的"Attention Is All You Need"论文提出Transformer，完全抛弃RNN，仅用Self-Attention机制。Transformer的优势是：(1) 可并行计算（RNN必须逐时间步计算）；(2) 长距离依赖建模更好。这直接催生了BERT、GPT系列和后续所有大语言模型。

> 🔗 **延伸实践**：详见 AEFS Phase 7 · Lesson 01: [Why Transformers](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/01-why-transformers) / Lesson 02: [Self-Attention from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch) / Lesson 03: [Multi-Head Attention](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/03-multi-head-attention) / Lesson 04: [Positional Encoding](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/04-positional-encoding) / Lesson 05: [Full Transformer](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/05-full-transformer) / Lesson 14: [Build a Transformer (Capstone)](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/14-build-a-transformer-capstone)
> 预计时长：~45 min + ~60 min + ~45 min + ~45 min + ~60 min + ~90 min

#### 1.11 实战代码一：用PyTorch实现LSTM预测客户购买序列

```python
"""
客户购买行为序列预测
使用LSTM预测客户下一步可能购买的产品类别
依赖: pip install torch pandas numpy
"""

import torch
import torch.nn as nn
import numpy as np
from collections import Counter

# === 1. 模拟客户购买序列数据 ===
# 每个客户有一个按时间排序的购买类别序列
def generate_purchase_sequences(num_customers=500, max_seq_len=20):
    """生成模拟购买序列数据"""
    categories = ['服装', '电子', '食品', '家居', '美妆', '运动']
    # 模拟购买模式：买完服装后倾向买美妆，买完电子后倾向买家居...
    transition_bias = {
        '服装': ['美妆', '服装', '运动'],
        '电子': ['家居', '电子', '食品'],
        '食品': ['食品', '家居', '服装'],
        '家居': ['家居', '食品', '电子'],
        '美妆': ['服装', '美妆', '食品'],
        '运动': ['服装', '运动', '食品'],
    }
    np.random.seed(42)
    sequences = []
    for _ in range(num_customers):
        seq_len = np.random.randint(5, max_seq_len)
        seq = [np.random.choice(categories)]
        for _ in range(seq_len - 1):
            current = seq[-1]
            next_cat = np.random.choice(transition_bias[current])
            seq.append(next_cat)
        sequences.append(seq)
    return sequences, categories

sequences, categories = generate_purchase_sequences()
cat_to_idx = {c: i for i, c in enumerate(categories)}
idx_to_cat = {i: c for i, c in enumerate(categories)}
vocab_size = len(categories)

# === 2. 数据预处理 ===
def prepare_data(sequences, max_len=20):
    """将序列转为模型输入格式"""
    X, Y = [], []
    for seq in sequences:
        # 用前n-1步预测第n步
        for i in range(1, len(seq)):
            input_seq = seq[:i]
            target = seq[i]
            # 填充到max_len
            padded = [cat_to_idx[c] for c in input_seq]
            padded = padded[-max_len:]  # 截断
            padded = [0] * (max_len - len(padded)) + padded  # 左填充
            X.append(padded)
            Y.append(cat_to_idx[target])
    return torch.tensor(X, dtype=torch.long), torch.tensor(Y, dtype=torch.long)

X, Y = prepare_data(sequences)
# 划分训练/测试
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
Y_train, Y_test = Y[:split], Y[split:]
print(f"训练样本: {len(X_train)}, 测试样本: {len(X_test)}")

# === 3. LSTM模型定义 ===
class PurchaseLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=32, hidden_dim=64, num_layers=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.3 if num_layers > 1 else 0
        )
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        # x shape: [batch, seq_len]
        embedded = self.embedding(x)  # [batch, seq_len, embed_dim]
        lstm_out, (hidden, cell) = self.lstm(embedded)
        # 使用最后一个时间步的输出
        last_output = lstm_out[:, -1, :]  # [batch, hidden_dim]
        logits = self.fc(last_output)     # [batch, vocab_size]
        return logits

# === 4. 训练 ===
model = PurchaseLSTM(vocab_size)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

BATCH_SIZE = 64
NUM_EPOCHS = 15

for epoch in range(NUM_EPOCHS):
    model.train()
    total_loss = 0
    correct = 0
    total = 0

    for i in range(0, len(X_train), BATCH_SIZE):
        batch_X = X_train[i:i+BATCH_SIZE]
        batch_Y = Y_train[i:i+BATCH_SIZE]

        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_Y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        _, predicted = outputs.max(1)
        correct += predicted.eq(batch_Y).sum().item()
        total += batch_Y.size(0)

    # 测试集评估
    model.eval()
    test_correct = 0
    test_total = 0
    with torch.no_grad():
        outputs = model(X_test)
        _, predicted = outputs.max(1)
        test_correct = predicted.eq(Y_test).sum().item()
        test_total = Y_test.size(0)

    print(f"Epoch {epoch+1}/{NUM_EPOCHS} | "
          f"Loss: {total_loss/len(X_train)*BATCH_SIZE:.4f} | "
          f"Train Acc: {100.*correct/total:.1f}% | "
          f"Test Acc: {100.*test_correct/test_total:.1f}%")

# === 5. 预测函数 ===
def predict_next_purchase(purchase_history, model, top_k=3):
    """预测客户下一步可能购买的产品类别"""
    model.eval()
    padded = [cat_to_idx.get(c, 0) for c in purchase_history[-20:]]
    padded = [0] * (20 - len(padded)) + padded
    input_tensor = torch.tensor([padded], dtype=torch.long)

    with torch.no_grad():
        output = model(input_tensor)
        probs = torch.nn.functional.softmax(output[0], dim=0)
        top_probs, top_indices = probs.topk(top_k)

    print(f"购买历史: {' -> '.join(purchase_history)}")
    print(f"预测下一步:")
    for prob, idx in zip(top_probs, top_indices):
        print(f"  {idx_to_cat[idx.item()]}: {prob.item():.1%}")
    return idx_to_cat[top_indices[0].item()]

# 使用示例
# predict_next_purchase(['服装', '美妆', '服装', '运动'])
```

#### 1.12 实战代码二：用PyTorch实现简单CNN图像分类器

```python
"""
简单CNN图像分类器（from scratch，不使用预训练权重）
演示卷积层、池化层、全连接层的完整实现
依赖: pip install torch torchvision
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# === 1. 数据准备 ===
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))  # MNIST均值和标准差
])

train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

# === 2. CNN模型定义 ===
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷积层1: 1->16通道, 3x3卷积, padding=1
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(16)
        # 卷积层2: 16->32通道, 3x3卷积
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        # 池化层
        self.pool = nn.MaxPool2d(2, 2)
        # 全连接层
        self.fc1 = nn.Linear(32 * 7 * 7, 128)  # 28x28 -> 14x14 -> 7x7
        self.fc2 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        # x: [batch, 1, 28, 28]
        x = self.pool(torch.relu(self.bn1(self.conv1(x))))  # -> [batch, 16, 14, 14]
        x = self.pool(torch.relu(self.bn2(self.conv2(x))))  # -> [batch, 32, 7, 7]
        x = x.view(x.size(0), -1)  # 展平
        x = self.dropout(torch.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

# === 3. 训练 ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleCNN().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(5):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

    # 评估
    model.eval()
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1)
            correct += pred.eq(target).sum().item()

    print(f"Epoch {epoch+1} | Test Acc: {100.*correct/len(test_dataset):.2f}%")
```

---

### Day 2：扩散模型与生成AI

#### 2.1 生成模型分类：VAE、GAN、Diffusion与Flow

生成模型（Generative Model）的目标是学习数据分布 $p(x)$，并能从该分布中采样生成新数据。

| 模型类型 | 核心思想 | 优势 | 劣势 | 代表模型 |
|---------|---------|------|------|---------|
| **VAE** | 编码到潜在空间再解码，最大化ELBO | 理论优雅、潜在空间有结构 | 生成模糊 | VAE, beta-VAE |
| **GAN** | 生成器与判别器对抗训练 | 生成锐利逼真 | 训练不稳定、模式坍塌 | StyleGAN, BigGAN |
| **Diffusion** | 前向加噪+反向去噪 | 质量最高、训练稳定、可控性好 | 采样速度慢 | DDPM, Stable Diffusion |
| **Flow** | 可逆变换，精确对数似然 | 精确似然计算、可逆 | 表达能力受限 | Glow, Rectified Flow |

**2024-2026趋势**：Diffusion已成为图像生成的主流方法（Stable Diffusion/DALL-E 3/Midjourney），Flow Matching作为Diffusion的推广正在崛起（Stable Diffusion 3采用Rectified Flow），而统一模型（Transfusion/Janus-Pro）试图用单一架构同时处理理解和生成。

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 01: [Generative Models Taxonomy & History](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/01-generative-models-taxonomy-history)
> 预计时长：~60 min

#### 2.2 VAE详解：变分推断、ELBO与重参数化

**变分自编码器（VAE）** 是一种概率生成模型，它假设数据由一个潜在变量 $z$ 生成。

**变分推断的核心思想**：

我们无法直接计算数据的真实分布 $p(x)$，但可以通过一个易于采样的分布 $q(z|x)$（编码器）来近似后验分布 $p(z|x)$。VAE最大化证据下界（ELBO）：

$$\log p(x) \geq \mathbb{E}_{q(z|x)}[\log p(x|z)] - D_{KL}(q(z|x) \| p(z))$$

- 第一项是**重建项**：从编码器采样的 $z$ 应该能重建出 $x$
- 第二项是**正则项**：编码器输出的分布应接近先验 $p(z)$（通常是标准正态分布）

**重参数化技巧（Reparameterization Trick）**：

VAE的一个关键技术难点是采样操作 $z \sim q(z|x)$ 不可微，无法反向传播。重参数化技巧将采样改写为：

$$z = \mu + \sigma \cdot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

这样梯度可以通过 $\mu$ 和 $\sigma$ 回传，而随机性被"外化"到 $\epsilon$。

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 02: [Autoencoders & VAE](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/02-autoencoders-vae)
> 预计时长：~60 min

#### 2.3 GAN详解：生成器与判别器、训练不稳定性

**生成对抗网络（GAN）** 通过生成器（Generator）和判别器（Discriminator）的博弈来学习生成：

```
生成器 G: 噪声 z -> 生成假样本 G(z)
判别器 D: 样本 x -> 判断真假 D(x)

G的目标: 让D无法区分真假（min_G max_D V(D,G)）
D的目标: 准确区分真假（max_D V(D,G)）
```

**GAN的损失函数**：

$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

**训练不稳定性**：
- **模式坍塌（Mode Collapse）**：生成器只学会生成少数几种样本，丧失多样性
- **训练震荡**：G和D的能力不均衡时，训练无法收敛
- **WGAN**：用Wasserstein距离替代JS散度，提供更有意义的梯度信号，改善训练稳定性

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 03: [GANs: Generator & Discriminator](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/03-gans-generator-discriminator)
> 预计时长：~60 min

#### 2.4 扩散模型原理：前向扩散与反向扩散

**扩散模型（Diffusion Model）** 的核心思想非常直觉：给一张清晰的图片逐步加噪直到变成纯噪声，然后学习反向过程--从噪声中逐步去噪恢复出清晰图片。

**前向扩散过程（加噪）**：

定义一个马尔可夫链，在T步内逐步向数据添加高斯噪声：

$$q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t} x_{t-1}, \beta_t I)$$

其中 $\beta_t$ 是预定义的噪声调度（Noise Schedule）。经过T步后，$x_T$ 近似为纯高斯噪声。

关键性质：可以直接从 $x_0$ 跳跃到任意 $x_t$：

$$q(x_t | x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t) I)$$

其中 $\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_s$，$\alpha_s = 1 - \beta_s$。这意味着训练时不需要逐步加噪，可以直接采样任意时间步的噪声版本。

**反向扩散过程（去噪）**：

学习一个神经网络 $\epsilon_\theta(x_t, t)$ 来预测时间步 $t$ 时添加的噪声。模型的目标是：

$$\mathcal{L}_{simple} = \mathbb{E}_{t, x_0, \epsilon} \left[ \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right]$$

即：给定加噪后的图片 $x_t$ 和时间步 $t$，预测加入的噪声 $\epsilon$。然后用预测的噪声逐步去噪。

**DDPM（Denoising Diffusion Probabilistic Models）数学推导要点**：

DDPM的反向过程每一步也是一个高斯分布：

$$p_\theta(x_{t-1} | x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$

Ho et al. (2020) 的关键简化是：将方差固定为 $\Sigma_\theta = \beta_t I$（不可学习），只学习均值 $\mu_\theta$。进一步推导表明，学习均值等价于学习预测噪声 $\epsilon$，因此最终的训练目标简化为上面的简单MSE损失。

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 06: [Diffusion: DDPM from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/06-diffusion-ddpm-from-scratch)
> 预计时长：~90 min

#### 2.5 条件生成与Classifier-free Guidance

**条件生成**让扩散模型可以按照文本提示生成图片：

$$\epsilon_\theta(x_t, t, c)$$

其中 $c$ 是条件（如文本提示的CLIP嵌入）。

**Classifier-free Guidance（CFG）** 是控制生成质量与多样性平衡的关键技术：

$$\tilde{\epsilon} = \epsilon_\theta(x_t, t, \varnothing) + w \cdot (\epsilon_\theta(x_t, t, c) - \epsilon_\theta(x_t, t, \varnothing))$$

- $\epsilon_\theta(x_t, t, \varnothing)$：无条件预测（生成"一般"图像）
- $\epsilon_\theta(x_t, t, c)$：有条件预测（生成"符合提示"的图像）
- $w$：引导强度（Guidance Scale）。$w=0$ 时纯条件生成；$w$ 越大越遵循提示但多样性降低

训练时以一定概率（如10%）丢弃条件 $c$（替换为空），使模型同时学习有条件和无条件两种模式。

#### 2.6 U-Net架构在扩散模型中的角色

扩散模型中的去噪网络通常使用U-Net架构（Day 1已介绍其结构）。在扩散模型中，U-Net的输入是加噪图像 $x_t$ 和时间步 $t$，输出是预测的噪声 $\epsilon$。

**扩散U-Net的特殊设计**：
- **时间嵌入（Time Embedding）**：将时间步 $t$ 编码为向量，通过AdaGN（Adaptive Group Normalization）注入到每个残差块中，使网络知道当前的噪声水平
- **交叉注意力（Cross-Attention）**：在U-Net的中间层加入文本条件的交叉注意力，使文本提示能影响图像生成
- **大感受野**：通过多级下采样，U-Net能在不同分辨率上理解图像的全局和局部信息

#### 2.7 Stable Diffusion架构：潜在扩散

**Stable Diffusion（SD）** 的核心创新是**潜在扩散（Latent Diffusion）**--不在像素空间做扩散，而在压缩的潜在空间中做扩散。

**SD的三大组件**：

```
1. VAE编码器: 图像(3×512×512) -> 潜在表示(4×64×64)  [压缩48倍]
2. U-Net: 在潜在空间中进行扩散去噪  [核心生成模型]
3. 文本编码器(CLIP Text Encoder): 文本提示 -> 条件嵌入  [控制生成内容]
```

**为什么在潜在空间做扩散**：

像素空间扩散的计算量正比于图像分辨率（512×512×3≈78万像素）。潜在空间将图像压缩到4×64×64=16384维，计算量减少约48倍，同时保留了语义信息。这使得SD能在消费级GPU上运行。

**生成流程**：

```
文本提示 -> CLIP文本编码器 -> 条件嵌入
                                ↓
随机噪声(4×64×64) -> U-Net去噪(T步) -> 去噪潜在表示
                                        ↓
                                   VAE解码器 -> 生成图像(3×512×512)
```

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 07: [Latent Diffusion & Stable Diffusion](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/07-latent-diffusion-stable-diffusion)
> 预计时长：~75 min

#### 2.8 ControlNet与LoRA在图像生成中的应用

**ControlNet**：

ControlNet为SD添加空间条件控制--你可以用一张线稿、深度图、姿态图来精确控制生成图像的构图。

**ControlNet的原理**：复制U-Net的编码器部分作为"控制分支"，通过零卷积（Zero Convolution，初始权重为0的卷积层）连接到主U-Net。零卷积确保训练初始时ControlNet不影响主模型，训练过程中逐渐学习条件控制。

**LoRA（Low-Rank Adaptation）**：

LoRA是一种参数高效微调方法，不修改原始模型权重，而是在旁边添加低秩矩阵：

$$W' = W + \Delta W = W + B \cdot A$$

其中 $A \in \mathbb{R}^{r \times d}$，$B \in \mathbb{R}^{d \times r}$，$r \ll d$（如 $r=8$）。原始参数量为 $d \times d$，LoRA参数量仅为 $2 \times r \times d$，大幅减少。

**LoRA在营销中的应用**：用少量品牌产品图微调SD，使其能生成符合品牌风格的创意图片，而不需要修改整个模型。一个4GB的SD模型只需训练约10MB的LoRA权重。

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 08: [ControlNet, LoRA & Conditioning](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/08-controlnet-lora-conditioning) 和 Lesson 09: [Inpainting, Outpainting & Editing](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/09-inpainting-outpainting-editing)
> 预计时长：~60 min + ~60 min

#### 2.9 主流生成模型对比

| 模型 | 架构 | 特点 | 商业模式 | 营销适用性 |
|------|------|------|---------|-----------|
| **Stable Diffusion** | 潜在扩散 | 开源、可微调、社区生态强 | 开源+托管API | 高：可本地部署，数据不出域 |
| **DALL-E 3** | 扩散+对话 | 文本理解强、与ChatGPT集成 | API付费 | 中：生成质量高但不可微调 |
| **Midjourney** | 扩散 | 艺术风格突出、审美在线 | 订阅制 | 中：适合创意概念图 |
| **Sora** | 扩散Transformer(DiT) | 视频生成、物理理解 | API受限 | 高：视频营销内容生成 |

**Flow Matching与Rectified Flow**：

Flow Matching是扩散模型的推广，它不限于高斯噪声的扩散过程，而是学习任意两个分布之间的连续变换（流）。Rectified Flow是Flow Matching的一种实现，路径更直、采样更快。Stable Diffusion 3采用了Rectified Flow，在质量和速度上都有提升。

> 🔗 **延伸实践**：详见 AEFS Phase 8 · Lesson 13: [Flow Matching & Rectified Flows](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/13-flow-matching-rectified-flows) 和 Lesson 14: [Evaluation: FID & CLIP Score](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/14-evaluation-fid-clip-score)
> 预计时长：~60 min + ~45 min

#### 2.10 实战代码：用diffusers库生成营销创意图片

```python
"""
AI营销创意图片生成系统
使用Stable Diffusion + LoRA生成品牌风格营销图片
依赖: pip install diffusers transformers torch accelerate
"""

import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from PIL import Image

# === 1. 加载Stable Diffusion模型 ===
model_id = "stabilityai/stable-diffusion-2-1"

# 使用Euler调度器（速度快，质量好）
scheduler = EulerDiscreteScheduler.from_pretrained(
    model_id, subfolder="scheduler"
)

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    scheduler=scheduler,
    torch_dtype=torch.float16,
    safety_checker=None  # 营销场景中可自行配置安全检查
).to("cuda" if torch.cuda.is_available() else "cpu")

# 启用内存优化（显存不足时）
pipe.enable_attention_slicing()

# === 2. 基础文生图 ===
def generate_marketing_image(prompt, negative_prompt="", num_images=1,
                              width=512, height=512, steps=30, guidance=7.5):
    """
    根据文本提示生成营销图片
    """
    images = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,
        guidance_scale=guidance,
        num_images_per_prompt=num_images,
        width=width,
        height=height,
    ).images

    return images

# === 3. 营销场景提示词模板 ===
MARKETING_PROMPTS = {
    "product_hero": (
        "professional product photography of {product}, "
        "studio lighting, clean white background, "
        "high detail, 8k, commercial photography, "
        "centered composition"
    ),
    "lifestyle_scene": (
        "lifestyle photography of {product} in a {scene} setting, "
        "natural lighting, warm atmosphere, "
        "shallow depth of field, premium aesthetic, "
        "social media ready"
    ),
    "social_media_ad": (
        "eye-catching social media advertisement featuring {product}, "
        "vibrant colors, modern design, "
        "instagram aesthetic, bold composition, "
        "trending style"
    )
}

def generate_from_template(template_name, product, scene=None, **kwargs):
    """使用预设模板生成营销图片"""
    template = MARKETING_PROMPTS[template_name]
    prompt = template.format(product=product, scene=scene or "modern")

    negative = ("blurry, low quality, distorted, watermark, "
                "text, logo, extra objects, cluttered background")

    print(f"Prompt: {prompt}")
    images = generate_marketing_image(prompt, negative, **kwargs)

    for i, img in enumerate(images):
        filename = f"marketing_{template_name}_{i}.png"
        img.save(filename)
        print(f"已保存: {filename}")

    return images

# === 4. 图生图（基于参考图的创意延展） ===
def img2img_variation(init_image_path, prompt, strength=0.75, **kwargs):
    """
    基于参考图片生成变体（保留构图，修改风格/内容）
    strength: 0=完全保留原图, 1=完全重新生成
    """
    from diffusers import StableDiffusionImg2ImgPipeline

    init_image = Image.open(init_image_path).convert("RGB")
    init_image = init_image.resize((512, 512))

    img2img = StableDiffusionImg2ImgPipeline(**pipe.components).to(pipe.device)

    images = img2img(
        prompt=prompt,
        image=init_image,
        strength=strength,
        **kwargs
    ).images

    return images

# === 5. LoRA加载（品牌风格微调） ===
def load_brand_lora(lora_path, weight_name=None, scale=0.8):
    """
    加载品牌风格LoRA权重
    lora_path: LoRA模型路径（HuggingFace或本地）
    scale: LoRA影响强度 (0-1)
    """
    pipe.load_lora_weights(lora_path, weight_name=weight_name)
    pipe.fuse_lora(lora_scale=scale)
    print(f"已加载品牌LoRA: {lora_path} (强度: {scale})")

# === 6. 批量生成营销素材 ===
def batch_generate_campaign(product, styles, scenes):
    """
    为一次营销活动批量生成多种风格和场景的素材
    """
    results = []
    for style in styles:
        for scene in scenes:
            prompt = (
                f"{style} photography of {product} in {scene}, "
                f"professional, high quality, commercial use"
            )
            images = generate_marketing_image(
                prompt=prompt,
                negative_prompt="low quality, blurry, distorted",
                num_images=1
            )
            results.append({
                'style': style,
                'scene': scene,
                'image': images[0]
            })
            print(f"已生成: {style} × {scene}")

    return results

# 使用示例
if __name__ == "__main__":
    # 示例1: 生成产品主图
    # generate_from_template("product_hero", "luxury skincare bottle")

    # 示例2: 生成生活方式场景图
    # generate_from_template("lifestyle_scene",
    #                        product="premium coffee cup",
    #                        scene="cozy morning kitchen")

    # 示例3: 加载品牌LoRA后生成
    # load_brand_lora("your-brand/lora-model", scale=0.8)
    # generate_from_template("social_media_ad", "summer collection dress")

    # 示例4: 批量生成营销活动素材
    # results = batch_generate_campaign(
    #     product="wireless earbuds",
    #     styles=["minimalist", "vibrant", "luxury"],
    #     scenes=["urban street", "office desk", "gym"]
    # )
    pass
```

#### 2.11 营销案例：AI生成广告创意与产品图片

**业务背景**：某DTC（Direct-to-Consumer）品牌每次上新需要100+张营销素材（主图/详情图/社媒图），传统拍摄+后期成本约500元/张，周期2周。

**解决方案**：部署Stable Diffusion + 品牌LoRA微调。

**实施流程**：
1. 用品牌历史素材（500张）训练品牌风格LoRA（训练时间约3小时，成本约50元GPU）
2. 上新时先用SD生成产品基础图（白底主图），再用ControlNet控制构图生成场景图
3. 人工筛选和微调（约10%需要重新生成）

**效果**：
- 单张素材成本从500元降至约5元（GPU推理成本）
- 产出周期从2周缩短到2天
- 100张素材中约70%可直接使用，30%需人工调整
- A/B测试显示AI生成素材的CTR（点击率）与实拍素材无显著差异

**关键经验**：
1. LoRA训练数据需要风格一致，混合过多风格会降低生成质量
2. ControlNet的线稿模式比深度图模式更适合产品图构图控制
3. 生成后的人工审核环节不可省略--确保品牌一致性和无AI痕迹

---

### Day 3：图神经网络（GNN）与前沿

#### 3.1 图数据基础：节点、边与邻接矩阵

图（Graph）是一种非欧几里得数据结构，由节点（Node/Vertex）和边（Edge）组成。许多商业数据天然具有图结构：

| 图类型 | 节点 | 边 | 营销应用 |
|--------|------|---|---------|
| 社交网络 | 用户 | 关注/好友关系 | 影响者识别、传播路径分析 |
| 知识图谱 | 实体（产品/品牌/概念） | 关系（属于/竞品/搭配） | 智能推荐、搜索增强 |
| 用户-商品二部图 | 用户、商品 | 购买/浏览/收藏 | 推荐系统 |
| 交易网络 | 账户 | 转账关系 | 欺诈检测 |

**邻接矩阵（Adjacency Matrix）**：

图结构用邻接矩阵 $A$ 表示，$A_{ij}=1$ 表示节点 $i$ 和 $j$ 之间有边，$A_{ij}=0$ 表示没有。对于无向图，$A$ 是对称矩阵。实际应用中图通常很稀疏（大部分 $A_{ij}=0$），因此常用稀疏矩阵存储。

**节点特征矩阵**：$X \in \mathbb{R}^{N \times d}$，其中 $N$ 是节点数，$d$ 是特征维度。每个节点有一个 $d$ 维特征向量（如用户的年龄/性别/购买频次等）。

> 🔗 **延伸实践**：详见 AEFS Phase 1 · Lesson 21: [Graph Theory](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/21-graph-theory)
> 预计时长：~60 min

#### 3.2 消息传递机制

**消息传递（Message Passing）** 是GNN的统一框架，几乎所有GNN变体都可以用消息传递来描述：

$$h_i^{(l+1)} = \gamma\left(h_i^{(l)}, \bigoplus_{j \in \mathcal{N}(i)} \phi\left(h_i^{(l)}, h_j^{(l)}, e_{ij}\right)\right)$$

直觉解释：
1. **消息生成**：对节点 $i$ 的每个邻居 $j$，用函数 $\phi$ 生成一条"消息"（基于两者的特征和边特征）
2. **消息聚合**：用聚合函数 $\bigoplus$（如求和/平均/最大值）汇总所有邻居的消息
3. **节点更新**：用函数 $\gamma$ 将聚合后的消息与节点自身特征融合，更新节点表示

经过 $L$ 层消息传递后，每个节点的表示融合了 $L$ 跳邻居的信息。这类似于CNN中感受野的概念--层数越多，每个节点"看到"的范围越广。

#### 3.3 GCN、GraphSAGE与GAT

| 架构 | 核心创新 | 聚合方式 | 优势 | 适用场景 |
|------|---------|---------|------|---------|
| **GCN** | 归一化邻接矩阵 | 对称归一化求和 | 简洁高效 | 中小规模图 |
| **GraphSAGE** | 邻居采样 | 可选（均值/LSTM/池化） | 可扩展到大图 | 大规模图、inductive学习 |
| **GAT** | 注意力权重 | 注意力加权求和 | 自动学习邻居重要性 | 异构图、重要性区分 |

**GCN（Graph Convolutional Network）**：

GCN的更新公式：

$$H^{(l+1)} = \sigma\left(\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2} H^{(l)} W^{(l)}\right)$$

其中 $\tilde{A} = A + I$（添加自环），$\tilde{D}$ 是度矩阵，$W^{(l)}$ 是可学习权重。$\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ 是对称归一化的邻接矩阵，它使每个节点对其邻居的影响按度数归一化（度数高的节点影响被适当降低）。

**GraphSAGE**：

GraphSAGE的核心改进是**邻居采样**--不使用全部邻居，而是随机采样固定数量的邻居。这使得每个节点的计算量固定，可扩展到百万级节点的大图。同时GraphSAGE支持inductive学习（可以处理训练时未见过的节点）。

**GAT（Graph Attention Network）**：

GAT用注意力机制替代固定的归一化权重：

$$\alpha_{ij} = \text{softmax}_j(\text{LeakyReLU}(a^T [Wh_i \| Wh_j]))$$

注意力权重 $\alpha_{ij}$ 自动学习邻居 $j$ 对节点 $i$ 的重要性，不需要预先假设图结构的重要性分布。多头注意力（Multi-Head Attention）进一步提升表达能力。

#### 3.4 图分类、节点分类与链路预测

| 任务类型 | 输入 | 输出 | 营销应用 |
|---------|------|------|---------|
| **节点分类** | 节点特征+图结构 | 每个节点的类别 | 用户分群、欺诈检测 |
| **链路预测** | 节点特征+图结构 | 节点对之间是否存在边 | 好友推荐、商品推荐 |
| **图分类** | 整个图的特征 | 图的类别 | 分子性质预测、社区分类 |

#### 3.5 异构图与知识图谱嵌入

**异构图（Heterogeneous Graph）** 包含多种类型的节点和边。例如在营销知识图谱中：
- 节点类型：用户、产品、品牌、类别、评论
- 边类型：购买、浏览、评论、属于、竞品

异构图GNN（如R-GCN、HGT）为不同类型的边学习不同的变换权重，更精确地建模复杂关系。

**知识图谱嵌入（Knowledge Graph Embedding）**：

将知识图谱中的实体和关系映射到低维向量空间，如TransE：

$$f(h, r, t) = -\|h + r - t\|$$

其中 $h$ 是头实体向量，$r$ 是关系向量，$t$ 是尾实体向量。直觉：头实体加上关系向量应该接近尾实体。这使得知识图谱可以用于推理（如"品牌A的竞品是谁"）和推荐（基于实体相似性）。

#### 3.6 实战代码：用PyTorch Geometric实现GCN客户分群

```python
"""
基于社交网络的GCN客户分群
利用用户社交关系和特征进行客户群体分类
依赖: pip install torch torch-geometric
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
import numpy as np

# === 1. 构建图数据 ===
def build_customer_graph(num_customers=1000):
    """
    构建客户社交网络图
    节点特征: [年龄, 月消费, 活跃度, 购买频次]
    边: 社交关系（好友/关注）
    标签: 客户群体（高价值/成长型/流失风险/休眠）
    """
    np.random.seed(42)

    # 节点特征
    node_features = np.random.randn(num_customers, 4).astype(np.float32)
    # 使特征与标签有相关性
    labels = np.random.randint(0, 4, num_customers)
    for i in range(num_customers):
        if labels[i] == 0:  # 高价值
            node_features[i] += [2, 3, 2, 3]
        elif labels[i] == 1:  # 成长型
            node_features[i] += [0, 1, 2, 1]
        elif labels[i] == 2:  # 流失风险
            node_features[i] += [-1, -1, -1, -1]

    # 构建边（社交关系）
    edges = []
    for i in range(num_customers):
        # 每个客户连接2-5个好友
        num_friends = np.random.randint(2, 6)
        friends = np.random.choice(num_customers, num_friends, replace=False)
        for f in friends:
            edges.append([i, f])
            edges.append([f, i])  # 无向图，添加反向边

    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
    x = torch.tensor(node_features)
    y = torch.tensor(labels, dtype=torch.long)

    # 训练/验证/测试掩码
    perm = torch.randperm(num_customers)
    train_mask = torch.zeros(num_customers, dtype=torch.bool)
    val_mask = torch.zeros(num_customers, dtype=torch.bool)
    test_mask = torch.zeros(num_customers, dtype=torch.bool)
    train_mask[perm[:600]] = True
    val_mask[perm[600:800]] = True
    test_mask[perm[800:]] = True

    data = Data(x=x, edge_index=edge_index, y=y,
                train_mask=train_mask, val_mask=val_mask, test_mask=test_mask)
    return data

data = build_customer_graph()
print(f"图数据: {data}")
print(f"节点数: {data.num_nodes}, 边数: {data.num_edges}, 特征维度: {data.num_features}")

# === 2. GCN模型定义 ===
class CustomerGCN(nn.Module):
    def __init__(self, in_channels, hidden_channels, num_classes, num_layers=2, dropout=0.5):
        super().__init__()
        self.convs = nn.ModuleList()
        self.convs.append(GCNConv(in_channels, hidden_channels))
        for _ in range(num_layers - 2):
            self.convs.append(GCNConv(hidden_channels, hidden_channels))
        self.convs.append(GCNConv(hidden_channels, num_classes))
        self.dropout = dropout

    def forward(self, x, edge_index):
        for i, conv in enumerate(self.convs[:-1]):
            x = conv(x, edge_index)
            x = F.relu(x)
            x = F.dropout(x, p=self.dropout, training=self.training)
        x = self.convs[-1](x, edge_index)
        return x

# === 3. 训练 ===
model = CustomerGCN(
    in_channels=data.num_features,
    hidden_channels=64,
    num_classes=4,
    num_layers=3,
    dropout=0.5
)

optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
criterion = nn.CrossEntropyLoss()

for epoch in range(100):
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    loss = criterion(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()

    # 验证
    model.eval()
    with torch.no_grad():
        pred = model(data.x, data.edge_index).argmax(dim=1)
        train_acc = (pred[data.train_mask] == data.y[data.train_mask]).float().mean()
        val_acc = (pred[data.val_mask] == data.y[data.val_mask]).float().mean()
        test_acc = (pred[data.test_mask] == data.y[data.test_mask]).float().mean()

    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch+1:3d} | Loss: {loss:.4f} | "
              f"Train: {train_acc:.3f} | Val: {val_acc:.3f} | Test: {test_acc:.3f}")

# === 4. 分析节点嵌入 ===
def extract_and_visualize_embeddings(model, data):
    """提取GCN学习的节点嵌入并可视化"""
    model.eval()
    with torch.no_grad():
        embeddings = model.convs[0](data.x, data.edge_index)
        embeddings = F.relu(embeddings)
        embeddings = model.convs[1](embeddings, data.edge_index)

    print(f"\n节点嵌入形状: {embeddings.shape}")
    print(f"嵌入向量范数: {embeddings.norm(dim=1).mean():.3f} (均值)")

    # 计算同群节点间的平均距离 vs 跨群距离
    from collections import defaultdict
    group_embeds = defaultdict(list)
    for i in range(data.num_nodes):
        group_embeds[data.y[i].item()].append(embeddings[i])

    print("\n群体间嵌入距离（余弦相似度）:")
    groups = list(group_embeds.keys())
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            mean_i = torch.stack(group_embeds[groups[i]]).mean(0)
            mean_j = torch.stack(group_embeds[groups[j]]).mean(0)
            sim = F.cosine_similarity(mean_i.unsqueeze(0), mean_j.unsqueeze(0)).item()
            print(f"  群体{groups[i]} vs 群体{groups[j]}: {sim:.3f}")

    return embeddings

embeddings = extract_and_visualize_embeddings(model, data)
```

#### 3.7 营销案例：社交网络影响传播分析

**业务背景**：某品牌计划发起一场KOL营销活动，预算有限只能选择5个KOL，需要选择能最大化传播效果的KOL组合。

**解决方案**：用GNN分析社交网络图，识别高影响力节点。

**分析步骤**：
1. 构建社交网络图：节点=用户，边=关注关系，节点特征=[粉丝数/互动率/历史转化率]
2. 用GCN学习每个用户的影响力嵌入表示
3. 用链路预测评估每个KOL的传播潜力（预测其关注者是否会转发）
4. 贪心算法选择5个KOL使覆盖面最大化（考虑重叠效应）

**关键发现**：GNN发现几个中等粉丝量但位于网络"桥梁"位置的KOL，其传播效果比几个百万粉丝但处于网络边缘的KOL更好。这是因为桥梁位置的KOL能连接不同的社群，实现跨圈层传播。

#### 3.8 前沿阅读：统一模型

**统一模型（Unified Model）** 试图用单一架构同时处理理解和生成任务，是多模态AI的前沿方向。

| 模型 | 核心思想 | 技术路线 |
|------|---------|---------|
| **Transfusion** | 一个模型、一套参数同时做自回归（文本）和扩散（图像） | 在同一Transformer中混合Next-Token预测和扩散去噪损失 |
| **Janus-Pro** | 解耦理解和生成的视觉编码 | 理解用CLIP编码器提取语义，生成用VQ编码器提取离散Token |
| **Emu3** | 统一为Next-Token预测 | 将图像也转为离散Token，文本和图像Token在同一序列中预测 |

**Transfusion的核心洞察**：文本生成本质是自回归（左到右逐Token），图像生成本质是扩散（从噪声到清晰）。Transfusion在同一个Transformer中为文本Token使用自回归损失，为图像Token使用扩散损失，两者共享Transformer参数但使用不同的损失函数。这避免了维护两套模型（如SD+LLM）的复杂性。

**Janus-Pro的设计哲学**：理解和生成对视觉信息的需求不同--理解需要高层语义特征（如"这是一只猫"），生成需要低层细节信息（如像素级的纹理）。Janus-Pro用不同的视觉编码器分别处理，但在LLM中统一。

**Emu3的极简路线**：将一切转化为Next-Token预测--图像被VQ-VAE编码为离散Token序列，与文本Token拼接后用标准自回归模型处理。这证明了"Next-Token预测是万能的"这一假说在视觉领域也成立。

**对营销的影响**：统一模型意味着未来可能用一个模型完成"理解营销图片+生成营销创意+撰写文案"的全流程，而不需要分别部署CV模型、生成模型和LLM。这将大幅降低营销AI系统的工程复杂度。

> 🔗 **延伸实践**：详见 AEFS Phase 12 · Lesson 12: [Emu3: Next-Token for Generation](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/12-emu3-next-token-for-generation) / Lesson 13: [Transfusion: Autoregressive + Diffusion](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion) / Lesson 15: [Janus-Pro: Decoupled Encoders](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/15-janus-pro-decoupled-encoders)
> 预计时长：~150 min + ~150 min + ~150 min

---

## 知识问答（15题）

**Q1：为什么ReLU比Sigmoid更适合深度网络的隐藏层？**

答案要点：(1) 梯度不消失：ReLU在正区梯度恒为1，Sigmoid在输入绝对值较大时梯度趋近0，深层网络梯度连乘后消失；(2) 计算高效：ReLU只需max(0,x)，Sigmoid需要指数运算；(3) 稀疏激活：ReLU使部分神经元输出为0，产生稀疏表示。但ReLU有"死亡ReLU"问题（负区梯度为0），Leaky ReLU/GELU等变体对此做了改进。

**Q2：解释Adam优化器中一阶矩和二阶矩的作用。**

答案要点：一阶矩（梯度的移动平均，类似Momentum）决定参数更新的方向，平滑梯度波动减少震荡。二阶矩（梯度平方的移动平均）估计每个参数的梯度方差，用于自适应调整学习率--梯度波动大的参数学习率自动减小，梯度稳定的参数保持较大学习率。两者结合使Adam在不同参数维度上自动调节步长。

**Q3：BatchNorm为什么能加速训练？**

答案要点：(1) 减少内部协变量偏移（Internal Covariate Shift）--每层输入的分布在训练中不断变化，BN将其归一化到稳定分布；(2) 允许更大学习率--归一化后损失曲面更平滑，不易因大学习率发散；(3) 轻微正则化--mini-batch的统计量引入噪声，有类似Dropout的正则化效果。

**Q4：Dropout在训练和测试时的行为有何不同？为什么？**

答案要点：训练时以概率p随机将神经元输出置零；测试时使用全部神经元但输出乘以(1-p)（或训练时做Inverted Dropout缩放，测试时不做变换）。原因是训练时丢弃p比例的神经元，期望输出减小为原来的(1-p)倍，测试时需补偿这个缩放。Dropout迫使网络不依赖任何单个神经元，学习更鲁棒的分布式表示。

**Q5：LSTM的细胞状态更新为什么用加法而不是乘法？**

答案要点：加法操作 $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$ 使梯度可以通过细胞状态直接回传。如果是乘法 $C_t = f_t \cdot C_{t-1} \cdot \tilde{C}_t$，多步连乘会导致梯度指数级衰减或增长（RNN的梯度消失/爆炸）。加法操作中遗忘门 $f_t$ 可以学习到接近1的值，使长期信息通过加法路径保留。

**Q6：对比LSTM和GRU的异同。**

答案要点：相同点--都使用门控机制控制信息流，都能解决RNN的梯度消失问题。不同点--LSTM有3个门（遗忘/输入/输出）和独立的细胞状态；GRU有2个门（更新/重置）且合并了细胞状态和隐状态。GRU参数更少训练更快，LSTM在超长序列上略优。实践中通常先试GRU（更快），效果不足再换LSTM。

**Q7：Seq2Seq的Attention机制解决了什么问题？**

答案要点：传统Seq2Seq将整个输入序列压缩为固定长度的上下文向量，长序列信息丢失严重。Attention机制让解码器在每一步动态"关注"输入序列的不同部分，不再依赖单一上下文向量。这解决了信息瓶颈问题，显著提升了长序列翻译/摘要的质量。Attention也是Transformer的基础。

**Q8：VAE的重参数化技巧为什么是必要的？**

答案要点：VAE需要从编码器输出的分布 $q(z|x) = \mathcal{N}(\mu, \sigma^2)$ 中采样 $z$，但采样操作不可微，无法反向传播。重参数化将 $z = \mu + \sigma \cdot \epsilon$（$\epsilon \sim \mathcal{N}(0,I)$），使随机性被外化到 $\epsilon$，梯度可以通过 $\mu$ 和 $\sigma$ 正常回传。没有这个技巧，VAE无法用梯度下降训练。

**Q9：GAN的"模式坍塌"是什么？如何缓解？**

答案要点：模式坍塌指生成器只学会生成少数几种样本（如只生成一种脸），丧失多样性。原因是生成器找到了欺骗判别器的捷径。缓解方法：(1) WGAN用Wasserstein距离提供更有意义的梯度；(2) Minibatch Discrimination让判别器比较一个batch内的样本；(3) Unrolled GAN让生成器考虑判别器未来几步的更新。

**Q10：扩散模型为什么比GAN更稳定？**

答案要点：(1) 扩散模型的训练目标是简单的MSE损失（预测噪声），没有GAN的对抗训练博弈；(2) 不存在模式坍塌问题--扩散过程自然覆盖全部数据分布；(3) 不需要精心平衡生成器和判别器的训练进度。代价是采样速度慢（需要多步去噪），但可通过DDIM、一致性模型等加速。

**Q11：解释Classifier-free Guidance的工作原理。**

答案要点：CFG同时计算有条件预测 $\epsilon(x_t,t,c)$ 和无条件预测 $\epsilon(x_t,t,\varnothing)$，然后取二者的差值放大：$\tilde{\epsilon} = \epsilon_{uncond} + w \cdot (\epsilon_{cond} - \epsilon_{uncond})$。差值 $(\epsilon_{cond} - \epsilon_{uncond})$ 是条件信号的方向，放大这个方向使生成更遵循文本提示。$w$ 越大越忠实于提示但多样性降低。训练时随机丢弃条件（约10%）使模型同时学习有条件和无条件两种模式。

**Q12：Stable Diffusion为什么在潜在空间而非像素空间做扩散？**

答案要点：像素空间扩散的计算量正比于像素数（512×512×3≈78万），每个去噪步都要处理这么大的张量。VAE将图像压缩到4×64×64=16384维潜在空间，计算量减少约48倍。潜在空间保留了语义信息但去除了高频细节，使扩散更高效。代价是VAE编码/解码可能引入轻微信息损失。

**Q13：LoRA的数学原理是什么？为什么能减少参数？**

答案要点：LoRA假设权重更新 $\Delta W$ 是低秩的，将其分解为 $\Delta W = B \cdot A$，其中 $A \in \mathbb{R}^{r \times d}$，$B \in \mathbb{R}^{d \times r}$，$r \ll d$。原始参数量为 $d^2$，LoRA参数量为 $2rd$。当 $r=8, d=1024$ 时，参数从约100万降至约1.6万，减少60倍以上。初始化时 $A$ 用随机值、$B$ 用零，确保训练初始时 $\Delta W = 0$ 不影响原模型。

**Q14：GCN的归一化邻接矩阵 $\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ 有什么作用？**

答案要点：归一化使每个节点的特征聚合不受度数影响。不归一化时，度数高的节点（如大V）的邻居消息累加值很大，会"淹没"度数低的节点。对称归一化 $\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ 使每条边的权重为 $1/\sqrt{d_i \cdot d_j}$，即两端节点度数越高边权重越小。自环 $\tilde{A} = A + I$ 确保节点自身特征也被包含在聚合中。

**Q15：Transfusion和Emu3在统一理解和生成方面的技术路线有何不同？**

答案要点：Transfusion在同一个Transformer中混合两种损失--文本Token用自回归损失（Cross-Entropy），图像Token用扩散损失（MSE），两者共享模型参数但损失函数不同。Emu3更极简--将图像也编码为离散Token，文本和图像Token在同一个序列中用统一的Next-Token预测（Cross-Entropy）处理，不需要扩散损失。Transfusion保留了扩散的生成质量优势，Emu3证明了纯自回归路线的可行性。

---

## 作业设计

### 必做作业：From-Scratch实现 + 生成模型应用

**任务包含两部分**：

**Part A - From-Scratch实现（必做）**：

不使用PyTorch的autograd，用NumPy从零实现一个两层全连接网络的反向传播：
1. 网络结构：输入层(4维) -> 隐藏层(16维, ReLU) -> 输出层(3维, Softmax)
2. 实现前向传播、交叉熵损失计算、反向传播（手写梯度计算）、参数更新
3. 在自制数据集上训练并收敛（准确率>80%）
4. 提交代码和训练损失曲线图

**Part B - 生成模型应用（必做）**：

选择以下任一任务完成：
1. 用diffusers库生成一组营销创意图片（至少10张），附Prompt Engineering策略说明
2. 用PyTorch实现一个简单VAE并在MNIST上训练，展示重建和生成结果
3. 用LSTM/GRU实现一个营销文本生成模型（如产品描述自动生成）

**评分标准（5分制）**：

| 维度 | 5分（优秀） | 3分（合格） | 1分（需改进） |
|------|-----------|-----------|-------------|
| From-Scratch正确性 | 梯度计算正确，收敛到>85% | 基本正确，收敛到>80% | 梯度错误或未收敛 |
| 代码质量 | 清晰注释，模块化设计 | 可运行但缺乏注释 | 无法运行 |
| 应用部分深度 | 有对比实验和深入分析 | 基本完成任务 | 仅调用API无理解 |
| 分析报告 | 有独到见解和商业洞察 | 基本描述 | 缺少分析 |

### 挑战作业：扩散模型mini实现 + GNN营销分析

**任务**：

1. 用PyTorch实现一个简化版DDPM（在MNIST或CIFAR-10上），包括前向加噪和反向去噪，生成可辨识的图像
2. 用PyTorch Geometric构建一个客户社交网络图，用GCN进行节点分类，分析节点嵌入的聚类效果
3. 撰写1000字报告：讨论深度学习、生成模型和GNN在营销中的协同应用场景

**评分标准**：额外考察(1)DDPM实现的完整性（是否包含噪声调度/采样算法）；(2)GNN分析的深度（是否发现有商业意义的图结构模式）；(3)三技术协同应用的创意性。

---

## 推荐资源清单

### AEFS延伸实践（按学习顺序）

| 顺序 | AEFS课节 | 课节名称 | 预计时长 | 链接 |
|:---:|---------|---------|:------:|------|
| 1 | P3-01 | The Perceptron | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/01-the-perceptron) |
| 2 | P3-02 | Multi-Layer Networks | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/02-multi-layer-networks) |
| 3 | P3-03 | Backpropagation | 75min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/03-backpropagation) |
| 4 | P3-04 | Activation Functions | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/04-activation-functions) |
| 5 | P3-05 | Loss Functions | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/05-loss-functions) |
| 6 | P3-06 | Optimizers | 75min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/06-optimizers) |
| 7 | P3-07 | Regularization | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/07-regularization) |
| 8 | P3-08 | Weight Initialization | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/08-weight-initialization) |
| 9 | P3-09 | Learning Rate Schedules | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/09-learning-rate-schedules) |
| 10 | P3-10 | Mini Framework | 90min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/10-mini-framework) |
| 11 | P3-11 | Intro to PyTorch | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/11-intro-to-pytorch) |
| 12 | P3-12 | Intro to JAX | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/12-intro-to-jax) |
| 13 | P3-13 | Debugging Neural Networks | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/13-debugging-neural-networks) |
| 14 | P7-01 | Why Transformers | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/01-why-transformers) |
| 15 | P7-02 | Self-Attention from Scratch | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch) |
| 16 | P7-03 | Multi-Head Attention | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/03-multi-head-attention) |
| 17 | P7-04 | Positional Encoding | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/04-positional-encoding) |
| 18 | P7-05 | Full Transformer | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/05-full-transformer) |
| 19 | P7-14 | Build a Transformer (Capstone) | 90min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/14-build-a-transformer-capstone) |
| 20 | P8-01 | Generative Models Taxonomy | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/01-generative-models-taxonomy-history) |
| 21 | P8-02 | Autoencoders & VAE | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/02-autoencoders-vae) |
| 22 | P8-03 | GANs: Generator & Discriminator | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/03-gans-generator-discriminator) |
| 23 | P8-06 | Diffusion: DDPM from Scratch | 90min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/06-diffusion-ddpm-from-scratch) |
| 24 | P8-07 | Latent Diffusion & Stable Diffusion | 75min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/07-latent-diffusion-stable-diffusion) |
| 25 | P8-08 | ControlNet, LoRA & Conditioning | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/08-controlnet-lora-conditioning) |
| 26 | P8-09 | Inpainting, Outpainting & Editing | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/09-inpainting-outpainting-editing) |
| 27 | P8-13 | Flow Matching & Rectified Flows | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/13-flow-matching-rectified-flows) |
| 28 | P8-14 | Evaluation: FID & CLIP Score | 45min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/14-evaluation-fid-clip-score) |
| 29 | P1-21 | Graph Theory | 60min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/21-graph-theory) |
| 30 | P12-12 | Emu3: Next-Token for Generation | 150min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/12-emu3-next-token-for-generation) |
| 31 | P12-13 | Transfusion: AR + Diffusion | 150min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion) |
| 32 | P12-15 | Janus-Pro: Decoupled Encoders | 150min | [链接](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/15-janus-pro-decoupled-encoders) |

### 其他推荐资源

| 资源 | 类型 | 链接/说明 |
|------|------|---------|
| Stanford CS231n | 课程 | CNN原理与作业，含反向传播从零实现 |
| MIT 6.S191 | 课程 | 深度学习入门，含RNN/生成模型讲座 |
| DeepLearning.AI | 课程 | Andrew Ng的深度学习专项课程 |
| HuggingFace Diffusers | 文档 | Stable Diffusion/ControlNet/LoRA实战指南 |
| Lilian Weng Blog | 博客 | "What are Diffusion Models?"等深度技术博文 |
| PyTorch Geometric | 文档 | GNN框架文档，含GCN/GraphSAGE/GAT教程 |
| Distill.pub | 可视化 | 交互式深度学习概念可视化（Attention/GAN等） |
| The Illustrated Transformer | 博客 | Transformer架构的图解教程 |

---

*本教材深度引用AEFS Phase 3（Deep Learning Core, 13 lessons）、Phase 7（Transformers, 16 lessons）、Phase 8（Generative AI, 14 lessons）、Phase 1 Lesson 21（Graph Theory）和Phase 12前沿课节（Emu3/Transfusion/Janus-Pro），共32节核心课程。AEFS的"from scratch"实现哲学贯穿全教材--建议学习者至少完成P3-03（反向传播）、P3-10（mini框架）、P8-06（DDPM从零实现）三节核心实践课，获得代码级的深度理解。*
