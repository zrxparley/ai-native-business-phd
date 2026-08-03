# AI原生化商业博士 · 独立教材：选修E11 推荐系统与个性化营销

> **修读者**：aha.gare  
> **导师系统**：Claude / 天道推演 + 系统觉醒 + 学位对标融合 + 牛津自然学习法 + 全球七校对标  
> **版本**：v4.0 | **日期**：2026-07-30  
> **学时**：6h | 建议节奏：3天集中学习  
> **对标课程**：Stanford CS246 Mining Massive Datasets + Google Recommendations Course + UCSD Recommender Systems + Wharton Customer Analytics + Imperial Recommendation Systems  
> **对应技能**：技能1（表示工程与营销智能）推荐系统深化 + 技能0（AI商业分析基础）  
> **前置条件**：完成技能1核心课程（理解Embedding和向量空间），具备Python和PyTorch基础  
> **定位**：从"理解推荐算法原理"升级到"能设计端到端个性化营销推荐系统"，掌握从经典CF到深度学习到工程架构到公平性的完整能力链

---

## 课程概述

### 核心命题

**推荐系统如何从"猜你喜欢"进化为"驱动商业增长的个性化引擎"？**

推荐系统是个性化营销的技术核心。当Amazon说"购买此商品的顾客也购买了"、当Netflix说"为你推荐"、当抖音说"下一个视频"时，背后都是推荐系统在驱动用户行为。推荐系统直接影响平台的核心指标--转化率、停留时长、客单价、留存率。一个优秀的推荐系统可以为电商带来20-30%的收入提升。

对于售前解决方案产品经理而言，推荐系统理解力决定了你在个性化营销方案中的技术深度。当客户说"我们想做精准营销"时，你需要能判断：他们的问题是冷启动（新用户没有行为数据）？是排序质量差（推荐了但不精准）？还是覆盖面不够（只推荐热门商品）？不同问题对应完全不同的技术方案。

### 学习目标

完成本课程后，你将能够：

1. **算法层**：掌握协同过滤、基于内容、矩阵分解三大经典推荐范式的原理和实现，理解各自的优势和局限
2. **深度学习层**：理解NCF、Wide & Deep、DeepFM、Two-Tower、序列推荐等深度学习推荐模型的核心架构
3. **工程层**：掌握推荐系统"召回->排序->重排"的三级架构，理解冷启动和多目标优化的工程方案
4. **公平性层**：理解推荐系统中的位置偏差、曝光偏差、流行度偏差，掌握因果推荐和可解释推荐的基本思路
5. **应用层**：能为电商/内容/营销场景设计端到端个性化推荐系统架构

---

## 学习计划表（3天）

| 天次 | 主题 | 时长 | 核心产出 |
|:---:|------|:----:|---------|
| **Day 1** | 推荐系统基础：经典方法 | 2h | Surprise协同过滤代码 + 评估指标计算代码 |
| **Day 2** | 深度学习推荐系统 | 2h | PyTorch NCF代码 + Two-Tower营销推荐代码 |
| **Day 3** | 推荐系统工程与公平性 | 2h | 电商推荐系统架构设计文档 |

---

## 详细学习内容

---

### Day 1：推荐系统基础

#### 一、推荐范式总览

推荐系统的核心任务是：给定一个用户和一组候选物品，预测用户对每个物品的偏好程度，然后推荐偏好最高的物品。

**三大推荐范式**：

| 范式 | 核心思想 | 数据需求 | 优势 | 局限 |
|------|---------|---------|------|------|
| **协同过滤（CF）** | "喜欢相似物品的用户有相似偏好" | 用户-物品交互矩阵 | 不需要物品内容信息，能发现隐含兴趣 | 冷启动问题、数据稀疏 |
| **基于内容（CB）** | "推荐与用户历史偏好相似的物品" | 物品特征向量 | 无冷启动（新物品有特征即可），可解释 | 难以发现新兴趣（信息茧房） |
| **混合推荐** | 结合CF和CB | 两者都需要 | 互补各自局限 | 系统复杂度高 |

**协同过滤的两个子方向**：

- **基于用户的CF（User-based CF）**：找到与目标用户相似的"邻居"用户，推荐邻居喜欢但目标用户未接触的物品。适用于用户数远少于物品数的场景（如小型电商）。
- **基于物品的CF（Item-based CF）**：找到与用户历史交互物品相似的物品进行推荐。Amazon在2003年提出的item-to-item推荐就是这种方法的经典应用，适用于物品数相对稳定的场景。

> 💡 **售前洞察**：当客户说"要做推荐系统"时，第一步是评估他们的数据基础。如果只有用户行为数据（点击/购买记录），从CF开始；如果有丰富的物品特征（商品描述、标签、图片），CB可以解决冷启动；如果两者都有，混合方案效果最佳。不要一上来就推深度学习--经典方法在小数据集上往往更稳健。

#### 二、基于用户的CF

**核心算法步骤**：

1. **计算用户相似度**：用余弦相似度或Pearson相关系数衡量用户间的偏好相似度
2. **选择邻居**：选择相似度最高的K个用户作为"邻居"
3. **生成推荐**：将邻居喜欢但目标用户未交互的物品推荐给目标用户，用相似度加权预测评分

```python
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ===== User-based CF 手动实现 =====

class UserBasedCF:
    """基于用户的协同过滤"""

    def __init__(self, n_neighbors=20):
        self.n_neighbors = n_neighbors
        self.user_similarity = None
        self.user_item_matrix = None

    def fit(self, user_item_matrix: pd.DataFrame):
        """
        user_item_matrix: 行=用户, 列=物品, 值=评分(或隐式反馈)
        """
        self.user_item_matrix = user_item_matrix
        # 计算用户间的余弦相似度
        self.user_similarity = pd.DataFrame(
            cosine_similarity(user_item_matrix.fillna(0)),
            index=user_item_matrix.index,
            columns=user_item_matrix.index
        )

    def predict(self, user_id, item_id) -> float:
        """预测用户对物品的评分"""
        if user_id not in self.user_item_matrix.index:
            return 0  # 新用户冷启动

        # 找到对该物品有交互的邻居用户
        item_raters = self.user_item_matrix[item_id].dropna()
        if len(item_raters) == 0:
            return 0  # 新物品冷启动

        # 选择最相似的K个邻居（在已评分用户中）
        neighbors = self.user_similarity.loc[user_id, item_raters.index]
        neighbors = neighbors.sort_values(ascending=False).head(self.n_neighbors)

        # 加权预测
        if neighbors.sum() == 0:
            return item_raters.mean()  # 相似度为0时用均值

        predicted = np.dot(neighbors.values, item_raters.loc[neighbors.index].values) / neighbors.sum()
        return predicted

    def recommend(self, user_id, n_recommendations=10) -> list:
        """为用户生成Top-N推荐"""
        if user_id not in self.user_item_matrix.index:
            # 冷启动：推荐热门物品
            popular = self.user_item_matrix.count().sort_values(ascending=False)
            return popular.head(n_recommendations).index.tolist()

        # 获取用户未交互的物品
        user_items = self.user_item_matrix.loc[user_id]
        unrated_items = user_items[user_items.isna()].index

        # 预测评分并排序
        predictions = [(item, self.predict(user_id, item)) for item in unrated_items]
        predictions.sort(key=lambda x: x[1], reverse=True)

        return [item for item, score in predictions[:n_recommendations]]


# ===== 模拟营销场景：用户-营销内容交互矩阵 =====
np.random.seed(42)
users = [f'User_{i:03d}' for i in range(50)]
items = [f'Campaign_{j:03d}' for j in range(30)]

# 生成稀疏交互矩阵（模拟点击/转化数据）
interaction_data = np.random.choice([np.nan, 1, 2, 3, 4, 5], size=(50, 30), p=[0.7, 0.06, 0.08, 0.06, 0.05, 0.05])
interaction_matrix = pd.DataFrame(interaction_data, index=users, columns=items)

# 训练推荐模型
cf = UserBasedCF(n_neighbors=10)
cf.fit(interaction_matrix)

# 为User_001生成推荐
recommendations = cf.recommend('User_001', n_recommendations=5)
print(f"User_001的推荐：{recommendations}")

# 预测User_001对Campaign_010的评分
score = cf.predict('User_001', 'Campaign_010')
print(f"预测评分：{score:.2f}")
```

#### 三、基于物品的CF：Amazon item-to-item

基于物品的CF不计算用户相似度，而是计算物品相似度。核心假设是：用户倾向于喜欢与自己历史喜欢物品相似的物品。

**为什么Amazon选择Item-based CF？**

Amazon的商品数量（数百万）远大于用户数，且商品集合相对稳定。计算物品相似度矩阵比用户相似度矩阵更高效，且可以离线预计算。当用户浏览一本Python书时，系统只需查找与该书最相似的N本书--这个过程可以在毫秒级完成。

#### 四、矩阵分解：SVD/PMF/ALS

矩阵分解是协同过滤的进阶方法。它将庞大的用户-物品交互矩阵分解为两个低维矩阵（用户隐因子矩阵和物品隐因子矩阵），通过隐因子捕捉用户偏好和物品特征的潜在结构。

**矩阵分解的核心思想**：

```
R (M×N) ≈ U (M×K) × V (K×N)

其中：
- R: 用户-物品交互矩阵 (M用户 × N物品)
- U: 用户隐因子矩阵 (M用户 × K隐因子)
- V: 物品隐因子矩阵 (K隐因子 × N物品)
- K: 隐因子维度（通常10-200）
```

**三种矩阵分解方法**：

| 方法 | 全称 | 特点 | 适用场景 |
|------|------|------|---------|
| **SVD** | Singular Value Decomposition | 经典数学方法，要求矩阵完整（无缺失） | 数据密集场景 |
| **PMF** | Probabilistic Matrix Factorization | 概率模型，能处理缺失值，用SGD优化 | 中等规模数据 |
| **ALS** | Alternating Least Squares | 交替优化U和V，适合并行计算 | 大规模稀疏数据（Spark内置） |

**用Surprise库实现协同过滤**：

```python
from surprise import Dataset, KNNBasic, SVD, accuracy
from surprise.model_selection import train_test_split, cross_validate
import pandas as pd

# ===== 使用Surprise库实现协同过滤 =====

# 创建营销内容交互数据集
interaction_records = []
np.random.seed(42)
for user_id in range(100):
    for item_id in range(50):
        if np.random.random() > 0.8:  # 20%的交互率
            rating = np.random.randint(1, 6)  # 1-5分
            interaction_records.append({
                'user_id': f'user_{user_id}',
                'item_id': f'content_{item_id}',
                'rating': rating
            })

df = pd.DataFrame(interaction_records)

# 加载到Surprise格式
from surprise import Reader
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# 划分训练集和测试集
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

# ===== 方法1：User-based CF =====
print("=" * 50)
print("User-based CF")
print("=" * 50)
sim_options = {'name': 'cosine', 'user_based': True, 'k': 20}
user_cf = KNNBasic(sim_options=sim_options)
user_cf.fit(trainset)
user_pred = user_cf.test(testset)
print(f"RMSE: {accuracy.rmse(user_pred):.4f}")
print(f"MAE: {accuracy.mae(user_pred):.4f}")

# ===== 方法2：Item-based CF =====
print("\n" + "=" * 50)
print("Item-based CF")
print("=" * 50)
sim_options = {'name': 'cosine', 'user_based': False, 'k': 20}
item_cf = KNNBasic(sim_options=sim_options)
item_cf.fit(trainset)
item_pred = item_cf.test(testset)
print(f"RMSE: {accuracy.rmse(item_pred):.4f}")
print(f"MAE: {accuracy.mae(item_pred):.4f}")

# ===== 方法3：SVD（矩阵分解）=====
print("\n" + "=" * 50)
print("SVD (Matrix Factorization)")
print("=" * 50)
svd = SVD(n_factors=50, n_epochs=30, lr_all=0.005, reg_all=0.02, random_state=42)
svd.fit(trainset)
svd_pred = svd.test(testset)
print(f"RMSE: {accuracy.rmse(svd_pred):.4f}")
print(f"MAE: {accuracy.mae(svd_pred):.4f}")

# ===== 交叉验证比较 =====
print("\n" + "=" * 50)
print("5-Fold Cross Validation")
print("=" * 50)
for name, algo in [('UserCF', KNNBasic(sim_options={'name': 'cosine', 'user_based': True})),
                    ('ItemCF', KNNBasic(sim_options={'name': 'cosine', 'user_based': False})),
                    ('SVD', SVD(n_factors=50, random_state=42))]:
    cv_results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=False)
    print(f"{name}: RMSE={cv_results['test_rmse'].mean():.4f}, MAE={cv_results['test_mae'].mean():.4f}")

# ===== 为指定用户生成推荐 =====
def get_top_n_recommendations(algo, user_id, all_items, interacted_items, n=10):
    """获取Top-N推荐"""
    predictions = []
    for item_id in all_items:
        if item_id not in interacted_items:
            pred = algo.predict(user_id, item_id)
            predictions.append((item_id, pred.est))

    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:n]

# 获取user_10的推荐
all_items = df['item_id'].unique().tolist()
user_10_items = df[df['user_id'] == 'user_10']['item_id'].tolist()
top_n = get_top_n_recommendations(svd, 'user_10', all_items, user_10_items, n=5)

print(f"\n为 user_10 推荐的Top-5内容：")
for item, score in top_n:
    print(f"  {item}: 预测评分 {score:.2f}")
```

> 🔗 **延伸实践**：详见 AEFS Phase 5 · Lesson 14: Information Retrieval & Search（信息检索与搜索--推荐系统的底层技术基础，包括倒排索引、向量检索、相似度计算等）

> 🔗 **延伸实践**：详见 AEFS Phase 11 · Lesson 04: Embeddings（嵌入表示--推荐系统中用户和物品的向量化表示方法）

#### 五、评估指标

推荐系统的评估与一般ML任务不同，因为推荐的核心目标不是"预测评分准确"，而是"推荐的列表用户是否喜欢"。

**分类1：评分预测指标**（适用于显式评分场景）

| 指标 | 全称 | 含义 | 适用场景 |
|------|------|------|---------|
| **RMSE** | Root Mean Square Error | 预测评分与真实评分的均方根误差 | 评分预测任务 |
| **MAE** | Mean Absolute Error | 预测评分与真实评分的平均绝对误差 | 评分预测任务 |

**分类2：排序质量指标**（适用于Top-N推荐场景，更贴近实际业务）

| 指标 | 全称 | 含义 | 优势 |
|------|------|------|------|
| **Precision@K** | 精确率 | 推荐的Top-K中用户实际喜欢的比例 | 直观 |
| **Recall@K** | 召回率 | 用户喜欢的物品中被推荐到Top-K的比例 | 衡量覆盖 |
| **NDCG@K** | Normalized Discounted Cumulative Gain | 考虑排序位置的加权指标 | 排在前面的更重要 |
| **MAP** | Mean Average Precision | 平均精度的均值 | 综合排序质量 |

```python
# ===== 推荐系统评估指标实现 =====

def precision_at_k(recommended_items, relevant_items, k=10):
    """Precision@K: 推荐的Top-K中相关物品的比例"""
    recommended_k = recommended_items[:k]
    relevant_set = set(relevant_items)
    hits = len([item for item in recommended_k if item in relevant_set])
    return hits / k

def recall_at_k(recommended_items, relevant_items, k=10):
    """Recall@K: 相关物品中被推荐到Top-K的比例"""
    recommended_k = recommended_items[:k]
    relevant_set = set(relevant_items)
    hits = len([item for item in recommended_k if item in relevant_set])
    return hits / len(relevant_set) if len(relevant_set) > 0 else 0

def ndcg_at_k(recommended_items, relevant_items, k=10):
    """NDCG@K: 考虑排序位置的归一化折损累计增益"""
    relevant_set = set(relevant_items)

    # DCG: 折损累计增益
    dcg = 0
    for i, item in enumerate(recommended_items[:k]):
        if item in relevant_set:
            dcg += 1 / np.log2(i + 2)  # i从0开始，所以+2

    # IDCG: 理想DCG（所有相关物品排在前面的最大DCG）
    ideal_hits = min(len(relevant_items), k)
    idcg = sum(1 / np.log2(i + 2) for i in range(ideal_hits))

    return dcg / idcg if idcg > 0 else 0

# 使用示例
recommended = ['item_1', 'item_5', 'item_3', 'item_8', 'item_2']
relevant = ['item_3', 'item_5', 'item_9', 'item_10']

print(f"Precision@5: {precision_at_k(recommended, relevant, k=5):.2f}")
print(f"Recall@5: {recall_at_k(recommended, relevant, k=5):.2f}")
print(f"NDCG@5: {ndcg_at_k(recommended, relevant, k=5):.4f}")
```

**业务指标 vs 算法指标**：

算法指标（Precision@K、NDCG）衡量推荐质量，但最终需要转化为业务指标才有商业意义。常见的映射关系：Precision@K提升10% -> 点击率提升5-8% -> 转化率提升3-5% -> 收入提升2-4%。在方案提案中，应该同时展示算法指标和预估的业务影响。

---

### Day 2：深度学习推荐系统

#### 一、神经协同过滤（NCF）

NCF是2017年新加坡国立大学提出的模型，用神经网络替代传统矩阵分解中的内积操作，让模型能学习用户和物品之间的非线性关系。

**NCF的核心创新**：

传统矩阵分解用用户隐向量和物品隐向量的**内积**来预测评分：

```
y_hat = u_i · v_j  (内积)
```

内积是线性操作，表达能力有限。NCF用多层感知机（MLP）替代内积：

```
y_hat = MLP(concat(u_i, v_j))  (非线性变换)
```

**NCF的两种架构**：

1. **GMF（Generalized Matrix Factorization）**：用元素级乘法替代内积，再加一层线性映射。保留了矩阵分解的结构，但增加了可学习权重。
2. **NeuMF（Neural Matrix Factorization）**：将GMF和MLP的输出拼接，再用一层全连接层融合。结合了线性和非线性能力。

**PyTorch实现NCF**：

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd

# ===== NCF模型定义 =====

class NCFDataset(Dataset):
    """推荐系统数据集"""

    def __init__(self, interactions: pd.DataFrame, n_users: int, n_items: int,
                 neg_ratio: int = 4):
        """
        interactions: DataFrame with columns [user_id, item_id, rating]
        neg_ratio: 每个正样本对应的负样本数
        """
        self.n_users = n_users
        self.n_items = n_items

        # 正样本
        self.samples = []
        user_items = interactions.groupby('user_id')['item_id'].apply(set).to_dict()

        for _, row in interactions.iterrows():
            self.samples.append((row['user_id'], row['item_id'], 1.0))

            # 负采样：随机选择用户未交互的物品
            for _ in range(neg_ratio):
                neg_item = np.random.randint(0, n_items)
                while neg_item in user_items.get(row['user_id'], set()):
                    neg_item = np.random.randint(0, n_items)
                self.samples.append((row['user_id'], neg_item, 0.0))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        user, item, label = self.samples[idx]
        return (
            torch.LongTensor([user]),
            torch.LongTensor([item]),
            torch.FloatTensor([label])
        )


class NCFModel(nn.Module):
    """Neural Collaborative Filtering模型"""

    def __init__(self, n_users: int, n_items: int, embedding_dim: int = 32,
                 mlp_layers: list = [64, 32, 16], dropout: float = 0.1):
        super().__init__()

        # Embedding层
        self.user_embedding_gmf = nn.Embedding(n_users, embedding_dim)
        self.item_embedding_gmf = nn.Embedding(n_items, embedding_dim)
        self.user_embedding_mlp = nn.Embedding(n_users, embedding_dim)
        self.item_embedding_mlp = nn.Embedding(n_items, embedding_dim)

        # MLP层
        mlp_input = embedding_dim * 2
        mlp_modules = []
        for hidden in mlp_layers:
            mlp_modules.append(nn.Linear(mlp_input, hidden))
            mlp_modules.append(nn.ReLU())
            mlp_modules.append(nn.Dropout(dropout))
            mlp_input = hidden
        self.mlp = nn.Sequential(*mlp_modules)

        # 输出层：拼接GMF和MLP的输出
        self.output = nn.Linear(embedding_dim + mlp_layers[-1], 1)
        self.sigmoid = nn.Sigmoid()

        # 初始化权重
        self._init_weights()

    def _init_weights(self):
        for emb in [self.user_embedding_gmf, self.item_embedding_gmf,
                     self.user_embedding_mlp, self.item_embedding_mlp]:
            nn.init.normal_(emb.weight, mean=0, std=0.01)

    def forward(self, user_ids, item_ids):
        # GMF路径：元素级乘法
        gmf_user = self.user_embedding_gmf(user_ids).squeeze(1)
        gmf_item = self.item_embedding_gmf(item_ids).squeeze(1)
        gmf_output = gmf_user * gmf_item

        # MLP路径：拼接后过MLP
        mlp_user = self.user_embedding_mlp(user_ids).squeeze(1)
        mlp_item = self.item_embedding_mlp(item_ids).squeeze(1)
        mlp_input = torch.cat([mlp_user, mlp_item], dim=-1)
        mlp_output = self.mlp(mlp_input)

        # 拼接GMF和MLP输出
        combined = torch.cat([gmf_output, mlp_output], dim=-1)

        # 输出预测
        output = self.sigmoid(self.output(combined))
        return output.squeeze()


# ===== 训练流程 =====

def train_ncf(n_users=100, n_items=50, n_epochs=10):
    """训练NCF模型"""
    # 生成模拟数据
    np.random.seed(42)
    interactions = pd.DataFrame({
        'user_id': np.random.randint(0, n_users, 500),
        'item_id': np.random.randint(0, n_items, 500),
        'rating': np.random.randint(1, 6, 500)
    })
    # 只保留评分>=4的作为正样本
    interactions = interactions[interactions['rating'] >= 4].reset_index(drop=True)

    # 创建数据集和数据加载器
    dataset = NCFDataset(interactions, n_users, n_items, neg_ratio=4)
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    # 初始化模型
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NCFModel(n_users, n_items, embedding_dim=32).to(device)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 训练循环
    for epoch in range(n_epochs):
        model.train()
        total_loss = 0
        n_batches = 0

        for user_ids, item_ids, labels in dataloader:
            user_ids = user_ids.to(device)
            item_ids = item_ids.to(device)
            labels = labels.to(device).squeeze()

            optimizer.zero_grad()
            predictions = model(user_ids, item_ids)
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            n_batches += 1

        avg_loss = total_loss / n_batches
        print(f"Epoch {epoch+1}/{n_epochs}, Loss: {avg_loss:.4f}")

    return model


# 训练模型
model = train_ncf(n_epochs=10)

# 为指定用户生成推荐
def recommend_ncf(model, user_id, n_items, top_k=5, device='cpu'):
    """用训练好的NCF模型生成推荐"""
    model.eval()
    with torch.no_grad():
        user_tensor = torch.LongTensor([user_id] * n_items).to(device)
        item_tensor = torch.LongTensor(range(n_items)).to(device)
        scores = model(user_tensor.unsqueeze(1), item_tensor.unsqueeze(1))

    top_indices = scores.topk(top_k).indices.cpu().numpy()
    return [(idx, scores[idx].item()) for idx in top_indices]


recommendations = recommend_ncf(model, user_id=5, n_items=50, top_k=5)
print(f"\n用户5的Top-5推荐：")
for item_id, score in recommendations:
    print(f"  Item {item_id}: score={score:.4f}")
```

> 🔗 **延伸实践**：详见 AEFS Phase 3 · Lesson 11: PyTorch（PyTorch深度学习框架--NCF等推荐模型的实现基础）

#### 二、Wide & Deep Learning

Wide & Deep是Google在2016年提出的模型，用于Google Play的应用推荐。它的核心思想是**结合记忆（Memorization）和泛化（Generalization）**。

**Wide部分（记忆）**：一个广义线性模型，使用交叉特征（特征叉积）来记忆频繁共现的模式。例如"男性 AND 25-30岁 AND 喜欢体育"这个交叉特征对推荐体育类内容很有效。

**Deep部分（泛化）**：一个多层感知机，将稀疏特征嵌入为稠密向量，学习特征的泛化关系。它可以推荐用户未曾明确表达过兴趣但语义相关的物品。

**两者联合训练**：Wide部分擅长记住明确的规则，Deep部分擅长发现隐含的关联。联合训练让模型既有记忆又有泛化。

#### 三、DeepFM

DeepFM是2017年华为提出的模型，将FM（Factorization Machine）和DNN结合，是Wide & Deep的改进版。

**Wide & Deep的局限**：Wide部分需要人工设计交叉特征，这需要领域知识和特征工程。

**DeepFM的改进**：用FM替代Wide部分的线性模型。FM能自动学习二阶特征交叉，不需要人工设计交叉特征。DeepFM = FM（自动特征交叉）+ DNN（高阶特征学习）。

**FM的核心公式**：

```
y_FM = w0 + Σ wi·xi + Σ Σ <vi, vj>·xi·xj
                一阶          二阶交叉
```

其中`<vi, vj>`是隐向量的内积，用于建模特征i和特征j的交互。FM的优势在于：即使两个特征从未在训练数据中共现，只要它们各自与其他特征共现过，FM就能通过隐向量推断它们的交互强度。

#### 四、Two-Tower模型

Two-Tower模型（又称DSSM, Dual Encoder）是工业界推荐系统中最常用的召回模型之一，特别适合大规模候选集的场景。

**架构**：

```
用户特征 -> User Tower -> 用户向量 u
                              |
                        相似度 = cos(u, v) 或 dot(u, v)
                              |
物品特征 -> Item Tower -> 物品向量 v
```

**Two-Tower的核心优势**：

1. **解耦计算**：用户向量和物品向量可以独立计算。物品向量可以离线预计算并建立向量索引，在线只需要计算用户向量然后做近邻搜索。
2. **高效召回**：用向量检索（如FAISS）从百万级候选集中快速召回Top-K，耗时毫秒级。
3. **多模态融合**：User Tower和Item Tower可以分别处理不同类型的特征（文本、图像、行为序列）。

**用Two-Tower构建营销内容推荐**：

```python
import torch
import torch.nn as nn

class TwoTowerModel(nn.Module):
    """Two-Tower模型用于营销内容推荐"""

    def __init__(self, user_feature_dim: int, item_feature_dim: int,
                 embedding_dim: int = 64):
        super().__init__()

        # User Tower: 用户特征 -> 用户向量
        self.user_tower = nn.Sequential(
            nn.Linear(user_feature_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, embedding_dim)
        )

        # Item Tower: 内容特征 -> 内容向量
        self.item_tower = nn.Sequential(
            nn.Linear(item_feature_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, embedding_dim)
        )

    def forward(self, user_features, item_features):
        user_vec = self.user_tower(user_features)
        item_vec = self.item_tower(item_features)

        # 归一化后用内积计算相似度
        user_vec = torch.nn.functional.normalize(user_vec, p=2, dim=1)
        item_vec = torch.nn.functional.normalize(item_vec, p=2, dim=1)

        # 相似度 = 内积（归一化后等价于余弦相似度）
        similarity = (user_vec * item_vec).sum(dim=1)
        return similarity

    def get_user_embedding(self, user_features):
        """获取用户向量（用于在线召回）"""
        return torch.nn.functional.normalize(
            self.user_tower(user_features), p=2, dim=1
        )

    def get_item_embedding(self, item_features):
        """获取物品向量（用于离线索引）"""
        return torch.nn.functional.normalize(
            self.item_tower(item_features), p=2, dim=1
        )


# ===== 营销内容推荐示例 =====

# 用户特征：[年龄归一化, 性别(one-hot 2), 消费水平, 活跃度, 历史CTR]
# 内容特征：[内容类型(one-hot 5), 时效性, 热度, 情感倾向, 长度归一化]

user_feature_dim = 6   # 用户特征维度
item_feature_dim = 9   # 内容特征维度

model = TwoTowerModel(user_feature_dim, item_feature_dim, embedding_dim=64)

# 模拟数据
batch_size = 32
user_features = torch.randn(batch_size, user_feature_dim)
item_features = torch.randn(batch_size, item_feature_dim)
labels = torch.randint(0, 2, (batch_size,)).float()  # 0/1标签

# 训练
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.BCEWithLogitsLoss()

for epoch in range(5):
    optimizer.zero_grad()
    scores = model(user_features, item_features)
    loss = criterion(scores, labels)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 离线计算所有内容向量
all_item_features = torch.randn(1000, item_feature_dim)  # 1000个营销内容
item_embeddings = model.get_item_embedding(all_item_features)

# 在线推荐：给定用户，检索最相似的内容
target_user = torch.randn(1, user_feature_dim)
user_embedding = model.get_user_embedding(target_user)

# 用内积计算相似度并取Top-K
similarities = torch.mm(user_embedding, item_embeddings.T)
top_k = 10
top_indices = similarities.topk(top_k).indices[0]

print(f"\n推荐给该用户的Top-{top_k}内容索引：{top_indices.tolist()}")
print(f"相似度分数：{similarities[0, top_indices].tolist()}")
```

> 💡 **售前洞察**：Two-Tower模型是推荐系统方案中最容易"讲故事"的模型。你可以向客户解释："用户的画像特征通过一个神经网络变成一个向量，每个营销内容也变成一个向量，然后我们用向量相似度来匹配最合适的内容推给用户"。这个解释直观且有技术深度，非常适合方案提案中的技术讲解环节。

#### 五、序列推荐：SASRec/BERT4Rec

传统的推荐方法将用户的历史交互视为无序集合，忽略了时间顺序信息。序列推荐（Sequential Recommendation）将用户行为视为一个时间序列，建模用户兴趣的动态变化。

**SASRec（Self-Attentive Sequential Recommendation）**：用Transformer的Self-Attention机制建模用户行为序列。给定用户最近N次交互的物品序列，预测下一个可能交互的物品。核心优势是能捕捉长程依赖（用户10次前看过的物品可能影响当前推荐）。

**BERT4Rec**：用BERT的双向Self-Attention建模用户行为序列。与SASRec的单向注意力不同，BERT4Rec使用双向注意力（遮盖预测），能更好地理解用户行为序列的全局上下文。

**营销场景应用**：序列推荐特别适合内容营销场景。用户的兴趣随时间变化（从关注产品功能到关注价格优惠到关注售后保障），序列推荐能捕捉这种动态，在正确的时机推正确的内容。

#### 六、LLM驱动的推荐与对话式推荐

> **2026前沿补丁**：本节探索LLM如何重塑推荐系统的范式，从"基于行为数据的隐式推荐"进化为"基于语言理解的显式推荐"。

**1. LLM-based推荐**

LLM正在改变推荐系统的构建方式。传统推荐模型需要大量用户行为数据训练，而LLM凭借其世界知识，可以在没有训练数据的情况下直接推荐。

| 方法 | 核心思想 | 数据需求 | 优势 | 局限 |
|------|---------|---------|------|------|
| LLM作为推荐器 | 直接用LLM生成推荐列表 | 用户画像文本描述 | 零样本、可解释 | 推理慢、成本高 |
| 生成式推荐(P5) | 将推荐建模为语言生成任务 | 交互数据+指令微调 | 统一多任务框架 | 需要大规模训练 |
| LLM+传统推荐 | LLM做特征提取/解释，传统模型排序 | 行为数据+物品文本 | 互补增强 | 系统复杂度高 |
| 零样本推荐 | 用LLM世界知识直接推荐 | 无需训练数据 | 冷启动友好 | 精度不如训练模型 |

**P5（Recommendation as Language Generation）**是2023年提出的统一推荐框架，将推荐任务（评分预测、序列推荐、解释生成、对话推荐）统一建模为语言生成任务。用指令微调（Instruction Tuning）让LLM学会"推荐"这个技能。例如输入"用户历史：买了iPhone、AirPods、MacBook。请推荐3个产品"，P5直接输出推荐列表和理由。

**LLM + 传统推荐的混合架构**是2026年的主流方案：用LLM从物品文本（商品描述、评论）中提取语义特征向量，用传统模型（DeepFM/Two-Tower）做排序。LLM负责"理解"，传统模型负责"高效排序"。

**2. 对话式推荐系统（Conversational Recommender Systems）**

传统推荐是"一次性"的--系统推荐，用户被动接受或拒绝。对话式推荐（CRS）将推荐变成多轮对话，系统通过对话逐步理解用户需求。

**多轮对话的典型流程**：

```
轮次1 [澄清]：用户"想买个耳机" -> 系统"您偏好入耳式还是头戴式？有预算范围吗？"
轮次2 [探索]：用户"头戴式，1000-2000元" -> 系统"推荐Sony WH-1000XM5和Bose QC45"
轮次3 [反馈]：用户"Sony的太重了" -> 系统"了解，您重视佩戴舒适度。推荐Bose QC45（仅240g）"
轮次4 [推荐]：系统"基于您的需求（头戴式/1000-2000元/轻量/降噪），Bose QC45最匹配"
```

**用CoT引导推荐推理**：Chain-of-Thought（CoT）让LLM的推荐过程显式化，提升推荐质量和可解释性：

```
CoT推理链：
Step 1 [用户画像]：用户是25-30岁都市白领，关注健康和效率
Step 2 [偏好推断]：偏好轻便、智能功能多、品牌感强的产品
Step 3 [候选筛选]：从候选池中筛选出3个符合条件的产品
Step 4 [推荐解释]：推荐产品A，因为它在轻便性和智能功能上评分最高
```

**3. 推荐的可解释性**

LLM为推荐可解释性带来了质的飞跃--从"基于注意力权重的间接解释"到"自然语言的直接解释"。

**LLM生成自然语言解释**：传统推荐系统的"解释"通常是"因为你买了X，所以推荐Y"这种基于关联的浅层解释。LLM可以生成深层解释："推荐这款降噪耳机是因为：您最近在通勤场景下浏览了多款耳机（行为信号），您的评价中多次提到'地铁太吵'（需求信号），这款耳机的主动降噪在地铁场景下效果最佳（产品匹配），且重量仅240g符合您之前偏好轻量设备的习惯（偏好匹配）。"

**解释的忠实性（Fidelity）**：LLM生成的解释是否反映了模型的真实决策逻辑？这是一个关键问题。LLM可能在"编造"合理的解释而非反映模型的真实推理。评估方法：(1)对比有/无解释的推荐一致性；(2)用反事实测试--修改解释中的某个因素，推荐结果是否相应变化。

**反事实解释**："如果你改变X，推荐结果会变为Y"。例如"如果您将预算从2000元提高到3000元，我会推荐Sony WH-1000XM5，因为它的降噪效果在3000元价位段最优"。反事实解释帮助用户理解推荐系统的决策边界，也帮助用户发现"如何调整偏好可以获得更好的推荐"。

**4. Python实战：用LangChain实现对话式推荐Agent**

```python
from openai import OpenAI
import json

client = OpenAI()

class ConversationalRecommenderAgent:
    """基于LLM的对话式推荐Agent，支持多轮交互和CoT推理"""

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog
        self.conversation_history = []
        self.user_profile = {
            'stated_preferences': [],
            'inferred_preferences': [],
            'budget': None,
            'use_case': None
        }

    def _build_system_prompt(self):
        """构建包含产品目录和CoT指令的系统prompt"""
        catalog_str = json.dumps(self.product_catalog, ensure_ascii=False, indent=2)

        return f"""你是一个专业的产品推荐助手。以下是产品目录：

{catalog_str}

推荐规则：
1. 每次回复最多推荐3个产品
2. 推荐前先用CoT推理分析用户需求
3. 推荐后附上简短理由
4. 如果用户需求不明确，先提问澄清
5. 记录用户的偏好和反馈，用于后续推荐

CoT推理格式：
[用户画像] 分析用户的显式需求和隐式偏好
[偏好推断] 根据对话历史推断用户偏好
[候选筛选] 从产品目录中筛选匹配的候选
[推荐解释] 解释为什么推荐这些产品
"""

    def chat(self, user_message):
        """处理用户消息，返回推荐响应"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        messages = [
            {"role": "system", "content": self._build_system_prompt()}
        ] + self.conversation_history

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7
        )

        assistant_reply = response.choices[0].message.content
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        # 更新用户画像（简化版，实际中用LLM提取结构化信息）
        self._update_profile(user_message)

        return assistant_reply

    def _update_profile(self, user_message):
        """从用户消息中提取偏好信息更新画像"""
        prompt = f"""
        从以下用户消息中提取偏好信息，以JSON格式返回：
        - budget: 预算范围（如有）
        - preferences: 提到的偏好关键词列表
        - use_case: 使用场景（如有）

        用户消息："{user_message}"
        """
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            extracted = json.loads(response.choices[0].message.content)
            if extracted.get('budget'):
                self.user_profile['budget'] = extracted['budget']
            if extracted.get('preferences'):
                self.user_profile['stated_preferences'].extend(extracted['preferences'])
            if extracted.get('use_case'):
                self.user_profile['use_case'] = extracted['use_case']
        except Exception:
            pass  # 提取失败不影响主流程

    def get_user_profile(self):
        """获取当前用户画像"""
        return self.user_profile


# ===== 示例使用 =====
product_catalog = [
    {"id": "P001", "name": "Sony WH-1000XM5", "price": 2899, "type": "头戴式",
     "weight": "250g", "features": ["主动降噪", "LDAC", "30h续航"]},
    {"id": "P002", "name": "Bose QC45", "price": 1799, "type": "头戴式",
     "weight": "240g", "features": ["主动降噪", "24h续航", "舒适佩戴"]},
    {"id": "P003", "name": "AirPods Pro 2", "price": 1899, "type": "入耳式",
     "weight": "5.3g", "features": ["主动降噪", "空间音频", "通透模式"]},
    {"id": "P004", "name": "华为 FreeBuds Pro 3", "price": 1099, "type": "入耳式",
     "weight": "5.8g", "features": ["主动降噪", "LDAC", "30h续航"]},
    {"id": "P005", "name": "森海塞尔 Momentum 4", "price": 2399, "type": "头戴式",
     "weight": "293g", "features": ["主动降噪", "60h续航", "高保真音质"]},
]

agent = ConversationalRecommenderAgent(product_catalog)

# 模拟多轮对话
print("=" * 60)
print("对话式推荐Agent Demo")
print("=" * 60)

# 第一轮：用户初始需求
print("\n用户: 想买个耳机，主要在地铁上用，预算2000左右")
reply1 = agent.chat("想买个耳机，主要在地铁上用，预算2000左右")
print(f"Agent: {reply1}")

# 第二轮：用户提供反馈
print("\n用户: 不喜欢入耳式的，戴着不舒服")
reply2 = agent.chat("不喜欢入耳式的，戴着不舒服")
print(f"Agent: {reply2}")

# 第三轮：用户追问
print("\n用户: 你推荐的这两款哪个更轻？降噪效果差别大吗？")
reply3 = agent.chat("你推荐的这两款哪个更轻？降噪效果差别大吗？")
print(f"Agent: {reply3}")

# 查看Agent积累的用户画像
print("\n" + "=" * 60)
print("Agent积累的用户画像：")
print(json.dumps(agent.get_user_profile(), ensure_ascii=False, indent=2))
```

**代码解读**：这段代码实现了一个完整的对话式推荐Agent。核心设计：(1)系统prompt包含产品目录和CoT推理指令，让LLM按结构化方式推理；(2)`_update_profile`方法在每轮对话后自动提取用户偏好，积累用户画像；(3)支持多轮对话，每轮都携带完整对话历史让LLM理解上下文。与传统推荐系统相比，对话式推荐的优势在于：能处理模糊需求（"地铁上用"隐含需要降噪）、能通过反馈修正推荐（"不喜欢入耳式"）、推荐过程完全可解释。局限在于：推理延迟较高（每轮1-3秒），不适合需要毫秒级响应的场景。

#### 七、跨学科桥梁：医疗推荐与教育推荐

**医疗推荐：治疗方案推荐**

医疗推荐系统面临比电商推荐高得多的准确性要求和合规约束。LLM在医疗推荐中的应用方向：(1)基于患者病历和最新临床指南，推荐个性化治疗方案；(2)解释推荐理由，引用循证医学文献支撑；(3)对比不同治疗方案的利弊，支持医患共同决策。关键约束：LLM推荐必须标注为"辅助决策建议"而非最终诊断，所有推荐需要医生审核，必须符合医疗法规和伦理要求。与电商推荐不同，医疗推荐的"误推"成本可能是生命，因此可解释性和安全性优先于推荐精度。

**教育推荐：学习路径推荐**

教育领域的推荐核心是"学习路径推荐"--根据学生的知识水平、学习风格和目标，推荐个性化的学习内容序列。LLM增强的教育推荐可以：(1)分析学生的答题历史，诊断知识薄弱点；(2)生成个性化的学习路径（"先复习基础概念A，再做练习B，然后挑战进阶C"）；(3)用对话式交互进行苏格拉底式提问，引导学生自主发现知识缺口。与电商推荐"一次推荐一个商品"不同，教育推荐需要考虑知识的前置依赖关系（不能在学会加法前推荐乘法内容），是一个序列决策问题。

> 💡 **售前洞察**：LLM驱动的推荐是对话式营销的技术基础。当客户说"我们想做智能客服推荐"时，你可以展示一个对话式推荐Agent的Demo--让客户亲自与Agent对话，体验"AI理解我的需求并给出有理由的推荐"。这种互动式Demo比任何PPT都有说服力。关键定位：传统推荐系统负责"大规模批量推荐"（万人级别的个性化），LLM推荐负责"高价值深度推荐"（与用户的多轮对话式交互），两者互补而非替代。

---

### Day 3：推荐系统工程与公平性

#### 一、推荐系统架构：召回->排序->重排

工业级推荐系统不是单一模型，而是一个多阶段 pipeline。每个阶段有不同的目标和约束。

**三级架构**：

| 阶段 | 目标 | 候选规模 | 模型特点 | 延迟要求 |
|:----:|------|:--------:|---------|:--------:|
| **召回（Retrieval）** | 从海量候选中快速筛选出相关候选 | 百万 -> 千 | 简单高效，多路召回 | <10ms |
| **排序（Ranking）** | 对召回候选精确排序 | 千 -> 百 | 复杂精确，多特征 | <100ms |
| **重排（Re-ranking）** | 在排序基础上考虑多样性、公平性、商业规则 | 百 -> 最终展示 | 规则+模型 | <10ms |

**召回阶段的多路策略**：

| 召回通道 | 方法 | 作用 |
|---------|------|------|
| **协同过滤召回** | Item-CF / User-CF | 基于行为相似性 |
| **向量召回** | Two-Tower + FAISS | 基于语义相似性 |
| **热门召回** | 全局/分品类Top-K | 保证基础覆盖 |
| **标签召回** | 用户标签匹配物品标签 | 基于显式兴趣 |
| **社交召回** | 好友喜欢的内容 | 社交影响 |
| **探索召回** | 随机/Bandit策略 | 发现新兴趣 |

> 💡 **售前洞察**：多路召回是推荐系统方案中的关键设计决策。不要只用一个模型--单一召回通道会导致信息茧房（只推荐用户已知喜欢的东西）。多路召回保证了多样性，每条通道负责一种"发现"逻辑。在方案中画出多路召回架构图，比展示一个复杂的排序模型更能体现工程能力。

**排序阶段的特征工程**：

排序模型是最复杂的部分，通常使用Wide & Deep、DeepFM等模型。特征分为四类：

| 特征类别 | 示例 | 作用 |
|---------|------|------|
| **用户特征** | 年龄、性别、消费水平、历史CTR | 描述用户画像 |
| **物品特征** | 类目、价格、热度、发布时间 | 描述物品属性 |
| **交叉特征** | 用户×类目CTR、用户×价格带偏好 | 捕捉用户-物品交互模式 |
| **上下文特征** | 时间、设备、位置、天气 | 描述推荐场景 |

**重排阶段的策略**：

- **多样性保障**：确保推荐列表中不会出现过多同类物品。用MMR（Maximal Marginal Relevance）等方法在相关性和多样性之间平衡。
- **商业规则**：保证某些物品的曝光（如新品扶持、赞助内容），限制某些物品的曝光（如低质内容、合规风险）。
- **公平性**：控制长尾物品的曝光比例，避免马太效应（热门越来越热，冷门越来越冷）。

#### 二、冷启动问题与策略

冷启动是推荐系统最经典的难题。三种冷启动场景需要不同的策略：

| 冷启动类型 | 问题 | 解决策略 |
|-----------|------|---------|
| **新用户冷启动** | 新用户无行为数据，无法个性化 | 用注册信息（年龄/性别/地域）做粗粒度推荐；用热门内容做默认推荐；引导用户选择兴趣标签 |
| **新物品冷启动** | 新物品无交互数据，无法被CF推荐 | 用物品内容特征做CB推荐；用专家标注做初始推荐；对新物品给予探索流量 |
| **系统冷启动** | 系统刚上线，无数据 | 用规则推荐（热门/编辑推荐）积累数据；用迁移学习从其他域迁移知识 |

**冷启动的工程方案**：

```python
class ColdStartHandler:
    """推荐系统冷启动处理器"""

    def __init__(self, popular_items: list, category_items: dict):
        self.popular_items = popular_items  # 全局热门物品
        self.category_items = category_items  # 按类目的热门物品

    def recommend_new_user(self, user_info: dict = None, n: int = 10) -> list:
        """新用户推荐策略"""
        if not user_info or 'interests' not in user_info:
            # 无任何信息：推荐全局热门
            return self.popular_items[:n]

        # 有兴趣标签：推荐对应类目的热门
        recommendations = []
        for interest in user_info.get('interests', []):
            if interest in self.category_items:
                recommendations.extend(self.category_items[interest][:3])

        # 补充全局热门
        recommendations.extend(self.popular_items[:n - len(recommendations)])
        return recommendations[:n]

    def recommend_new_item(self, item_features: dict, similar_items: list,
                           n: int = 10) -> list:
        """新物品推荐策略：基于内容特征找相似物品，推荐给喜欢相似物品的用户"""
        # 实际中用CB模型计算物品相似度
        # 这里简化为：新物品推给喜欢相似物品的用户
        return similar_items[:n]


# 使用示例
handler = ColdStartHandler(
    popular_items=['item_001', 'item_002', 'item_003', 'item_004', 'item_005'],
    category_items={
        'electronics': ['item_101', 'item_102', 'item_103'],
        'fashion': ['item_201', 'item_202', 'item_203'],
        'food': ['item_301', 'item_302', 'item_303']
    }
)

# 新用户（无信息）
print("新用户（无信息）推荐：", handler.recommend_new_user(n=5))

# 新用户（有兴趣标签）
print("新用户（兴趣：electronics）推荐：",
      handler.recommend_new_user({'interests': ['electronics']}, n=5))
```

#### 三、多目标推荐：MMoE/PLE

真实的推荐系统需要同时优化多个目标。例如电商推荐需要同时考虑点击率（CTR）、转化率（CVR）、GMV（成交额）、停留时长。这些目标之间可能存在冲突--高点击率的内容不一定高转化率。

**多目标模型架构演进**：

| 模型 | 全称 | 核心思想 | 优势 |
|------|------|---------|------|
| **Shared-Bottom** | 共享底层模型 | 所有目标共享特征提取层，各自有独立的输出层 | 简单，但目标间可能互相干扰 |
| **MMoE** | Multi-gate Mixture-of-Experts | 多个专家网络+多个门控（每个目标有自己的门控权重） | 自动学习目标间的关系 |
| **PLE** | Progressive Layered Extraction | 分层专家+渐进式路由，MMoE的改进版 | 更好地处理目标间冲突 |

**PLE的核心改进**：MMoE的所有专家被所有目标共享，当目标间存在冲突时会导致负迁移。PLE将专家分为"共享专家"和"任务专属专家"，并分层提取，让冲突目标和协同目标分别处理。

#### 四、推荐公平性

推荐系统不是中性的--它会在用户和物品之间分配曝光机会，而这种分配可能存在系统性偏差。

**三类常见偏差**：

| 偏差类型 | 定义 | 危害 | 缓解方法 |
|---------|------|------|---------|
| **位置偏差** | 排在前面的物品获得更多点击，不论其真实质量 | 排序模型难以区分"质量好"和"位置好" | 位置去偏（Position Debiasing）、逆倾向得分（IPS） |
| **曝光偏差** | 只有被曝光的物品才有交互数据，形成循环 | 长尾物品永远得不到曝光 | 探索与利用（Bandit算法）、公平性约束 |
| **流行度偏差** | 热门物品被推荐得更多，冷门物品被埋没 | 马太效应，生态多样性下降 | 流行度惩罚、长尾扶持 |

**因果推荐基础**：

传统推荐模型学习的是"用户在看到物品后点击的概率"，但这混杂了"物品被展示给用户"的选择偏差。因果推荐试图回答反事实问题："如果用户看到了这个物品（即使实际上没看到），他会点击吗？"

**IPS（Inverse Propensity Scoring，逆倾向得分）**是因果推荐的经典方法：

```python
# IPS去偏示例（概念性代码）

def ips_weighted_loss(predictions, labels, propensities):
    """
    IPS加权的损失函数

    predictions: 模型预测的点击概率
    labels: 实际点击标签（0/1）
    propensities: 每个物品被曝光的概率（倾向得分）
    """
    # IPS权重：1/倾向得分
    # 被曝光概率低的物品，其交互数据的权重更高
    # 因为这些数据更"珍贵"（不是因为热门才被看到的）
    ips_weights = 1.0 / propensities

    # 加权交叉熵损失
    loss = -(labels * torch.log(predictions + 1e-8) +
             (1 - labels) * torch.log(1 - predictions + 1e-8))
    weighted_loss = (loss * ips_weights).mean()

    return weighted_loss
```

#### 五、可解释推荐

可解释推荐（Explainable Recommendation）不仅推荐物品，还给出推荐理由。这对用户信任和商业价值都至关重要。

**两种可解释性方向**：

1. **事后解释（Post-hoc Explanation）**：先推荐，再用另一个模型生成解释。例如推荐后用LLM生成"推荐理由：因为你最近浏览了多款无线耳机，这款产品在音质和续航方面评分最高。"
2. **内在可解释（Intrinsic Explanation）**：推荐模型本身就能输出解释。例如基于注意力机制的模型，注意力权重可以解释为"模型关注了哪些特征"。

**营销场景中的可解释推荐**：

在营销内容推荐中，可解释性尤为重要。用户需要知道"为什么给我推这个内容"才能建立信任。一个可解释的推荐系统可以在邮件营销中写出："因为我们注意到您上个月浏览了3次CRM相关内容，为您推荐这篇《2026年CRM趋势报告》。"这种个性化+可解释的推荐比泛泛的"猜你喜欢"转化率高3-5倍。

#### 六、综合案例：电商个性化营销推荐系统架构

**客户背景**：某中型电商平台，SKU数量50万，月活用户200万，当前推荐系统基于简单的热门排序，转化率1.2%。

**目标**：构建端到端个性化推荐系统，目标转化率提升至2.0%+。

**系统架构设计**：

```
                    ┌──────────────────────────────┐
                    │        数据层                 │
                    │  用户行为日志 + 商品特征库    │
                    │  + 用户画像 + 实时特征        │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │        召回层                 │
                    │  ┌────────┐ ┌────────┐      │
                    │  │Item-CF │ │Two-Tower│      │
                    │  │ 召回   │ │ 向量召回│      │
                    │  └────────┘ └────────┘      │
                    │  ┌────────┐ ┌────────┐      │
                    │  │热门召回 │ │标签召回 │      │
                    │  └────────┘ └────────┘      │
                    │  输出：~2000候选             │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │        排序层                 │
                    │  DeepFM多目标排序模型         │
                    │  目标：CTR + CVR + GMV        │
                    │  特征：用户+物品+交叉+上下文  │
                    │  输出：~200候选               │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │        重排层                 │
                    │  多样性保障（MMR）            │
                    │  商业规则（新品扶持/赞助）    │
                    │  公平性约束（长尾曝光）       │
                    │  输出：最终展示列表           │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │        服务层                 │
                    │  在线AB测试框架               │
                    │  实时反馈收集                 │
                    │  模型监控与自动重训           │
                    └──────────────────────────────┘
```

**实施路线图**：

| 阶段 | 时间 | 目标 | 关键交付 |
|------|------|------|---------|
| **Phase 1: 基础** | 1-2月 | 搭建数据管道和召回系统 | Item-CF召回 + 热门兜底，转化率1.5% |
| **Phase 2: 排序** | 2-3月 | 上线排序模型 | DeepFM排序，转化率1.8% |
| **Phase 3: 优化** | 2-3月 | 多目标+多样性 | MMoE多目标+MMR重排，转化率2.0%+ |
| **Phase 4: 智能化** | 持续 | 冷启动优化+可解释推荐 | 序列推荐+LLM推荐理由生成 |

**预期ROI**：转化率从1.2%提升到2.0%（+67%），按月GMV 5000万计算，月增量GMV约3350万，年收入增加约4亿元。系统建设和运营成本约200万/年，ROI极高。

> 💡 **售前洞察**：这个综合案例展示了推荐系统方案的核心逻辑：不是"用最先进的模型"，而是"分阶段交付可衡量的价值"。Phase 1用最简单的Item-CF就能提升25%的转化率（从1.2%到1.5%），这已经足以证明推荐系统的价值。然后逐步迭代到更复杂的模型。这种"快速交付基础价值，逐步深化"的策略是大型项目成功的关键。

---

## 真实数据集案例研究

> 本节通过真实数据集 MovieLens 100K，演示推荐系统核心方法的完整分析流程，从数据加载到商业洞察。

### 案例背景

**数据集**：MovieLens 100K，由明尼苏达大学 GroupLens 研究小组发布，是推荐系统领域最经典的基准数据集。

- **规模**：100,000 条评分记录，来自 943 位用户对 1,682 部电影的评分（1-5分）
- **稀疏度**：99.6%（用户-物品矩阵中仅 0.4% 的格子有评分）
- **附加信息**：用户人口统计信息（年龄、性别、职业、邮编）、电影类型标签
- **商业对应**：Netflix、爱奇艺等流媒体平台的推荐场景

**业务场景模拟**：假设你是一家视频流媒体平台（类似爱奇艺）的售前解决方案产品经理，客户希望构建个性化推荐系统。你用 MovieLens 100K 作为概念验证（POC）数据集，向客户演示协同过滤和矩阵分解的完整流程及效果。

### 数据加载与探索

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from surprise import Dataset, KNNBasic, SVD, accuracy, Reader
from surprise.model_selection import train_test_split, cross_validate

# ===== 加载 MovieLens 100K 数据集 =====
# Surprise库内置了MovieLens 100K，首次运行会自动下载
data = Dataset.load_builtin('ml-100k')

# 转换为DataFrame进行EDA
raw_ratings = data.raw_ratings
df = pd.DataFrame(raw_ratings, columns=['user_id', 'item_id', 'rating', 'timestamp'])

print(f"=== 数据集概览 ===")
print(f"评分总数: {len(df):,}")
print(f"用户数: {df['user_id'].nunique()}")
print(f"电影数: {df['item_id'].nunique()}")
print(f"评分范围: {df['rating'].min()} - {df['rating'].max()}")
print(f"平均评分: {df['rating'].mean():.2f}")
print(f"稀疏度: {1 - len(df) / (df['user_id'].nunique() * df['item_id'].nunique()):.4f}")

# ===== EDA: 评分分布、用户活跃度、电影热度 =====
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 评分值分布
rating_counts = df['rating'].value_counts().sort_index()
axes[0].bar(rating_counts.index, rating_counts.values, color='#2E86AB')
axes[0].set_title('评分值分布')
axes[0].set_xlabel('评分'); axes[0].set_ylabel('数量')

# 用户活跃度分布（每用户评分数）
user_activity = df.groupby('user_id').size()
axes[1].hist(user_activity, bins=50, color='#2A9D8F', edgecolor='white')
axes[1].set_title('用户活跃度分布')
axes[1].set_xlabel('评分数量'); axes[1].set_ylabel('用户数')

# 电影热度分布（每电影被评分数）
movie_popularity = df.groupby('item_id').size()
axes[2].hist(movie_popularity, bins=50, color='#E63946', edgecolor='white')
axes[2].set_title('电影热度分布')
axes[2].set_xlabel('被评分数'); axes[2].set_ylabel('电影数')

plt.tight_layout()
plt.savefig('movielens_eda.png', dpi=150)
plt.show()

print(f"\n用户评分数中位数: {user_activity.median():.0f}")
print(f"电影被评分数中位数: {movie_popularity.median():.0f}")
```

### 核心分析

```python
# ===== 方法对比：User-CF / Item-CF / SVD =====
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

results = {}

# 方法1: User-based CF
sim_options_user = {'name': 'cosine', 'user_based': True, 'k': 30}
user_cf = KNNBasic(sim_options=sim_options_user)
user_cf.fit(trainset)
user_pred = user_cf.test(testset)
results['User-CF'] = {
    'RMSE': accuracy.rmse(user_pred, verbose=False),
    'MAE': accuracy.mae(user_pred, verbose=False)
}

# 方法2: Item-based CF
sim_options_item = {'name': 'cosine', 'user_based': False, 'k': 30}
item_cf = KNNBasic(sim_options=sim_options_item)
item_cf.fit(trainset)
item_pred = item_cf.test(testset)
results['Item-CF'] = {
    'RMSE': accuracy.rmse(item_pred, verbose=False),
    'MAE': accuracy.mae(item_pred, verbose=False)
}

# 方法3: SVD 矩阵分解
svd = SVD(n_factors=50, n_epochs=30, lr_all=0.005, reg_all=0.02, random_state=42)
svd.fit(trainset)
svd_pred = svd.test(testset)
results['SVD'] = {
    'RMSE': accuracy.rmse(svd_pred, verbose=False),
    'MAE': accuracy.mae(svd_pred, verbose=False)
}

# ===== 结果对比表 =====
print("=" * 50)
print(f"{'方法':<15} {'RMSE':>10} {'MAE':>10}")
print("=" * 50)
for method, metrics in results.items():
    print(f"{method:<15} {metrics['RMSE']:>10.4f} {metrics['MAE']:>10.4f}")
print("=" * 50)

# ===== 为指定用户生成 Top-N 推荐 =====
def get_top_n(algo, user_id, trainset, n=10):
    """生成Top-N推荐：预测用户未评分物品的评分并排序"""
    inner_uid = trainset.to_inner_uid(user_id)
    rated_inner_iids = set([iid for (iid, _) in trainset.ur[inner_uid]])
    rated_items = set([trainset.to_raw_iid(iid) for iid in rated_inner_iids])
    all_items = set([trainset.to_raw_iid(iid) for iid in trainset.all_items()])
    unrated = all_items - rated_items

    predictions = [(iid, algo.predict(user_id, iid).est) for iid in unrated]
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:n]

# 为用户 '196' 生成推荐
top10 = get_top_n(svd, '196', trainset, n=10)
print(f"\n用户 196 的 Top-10 推荐（SVD）:")
print(f"{'排名':<6} {'电影ID':<12} {'预测评分':>10}")
print("-" * 30)
for rank, (movie_id, score) in enumerate(top10, 1):
    print(f"{rank:<6} {movie_id:<12} {score:>10.2f}")

# ===== 推荐多样性分析（流行度偏差检测） =====
top10_movie_ids = [mid for mid, _ in top10]
top10_popularity = [movie_popularity.get(mid, 0) for mid in top10_movie_ids]
avg_popularity = np.mean(top10_popularity)
global_avg_popularity = movie_popularity.mean()

print(f"\n推荐电影平均热度（被评分数）: {avg_popularity:.1f}")
print(f"全局电影平均热度: {global_avg_popularity:.1f}")
print(f"热度比: {avg_popularity / global_avg_popularity:.2f}x （>1说明偏向热门）")
```

### 结果解读

三种方法在 MovieLens 100K 上的表现对比：

| 方法 | RMSE | MAE | 特点 |
|------|:----:|:----:|------|
| User-CF | ~0.98 | ~0.77 | 基于用户相似度，适合用户数少的场景 |
| Item-CF | ~0.97 | ~0.76 | 基于物品相似度，Amazon经典方案 |
| SVD | ~0.94 | ~0.74 | 矩阵分解，精度最高 |

**关键发现**：
1. **SVD优于CF方法**：SVD的RMSE比CF低约3-4%，因为隐因子能捕捉评分矩阵的潜在结构
2. **长尾效应显著**：推荐电影的平均热度远高于全局平均，说明推荐系统倾向于推荐热门电影（流行度偏差）
3. **稀疏度影响**：99.6%的稀疏度下，CF方法仍能工作，但依赖每用户至少20条评分的最低门槛

### 商业启示

1. **模型选择策略**：POC阶段优先用SVD（精度最高），生产环境可结合Item-CF（可解释性强、离线预计算高效）和SVD（排序精度），形成多路召回+排序的架构

2. **流行度偏差的治理**：推荐列表偏向热门电影是推荐系统的通病。生产环境必须在重排阶段加入多样性约束（如MMR），否则用户会陷入"信息茧房"，长期留存率下降

3. **冷启动的工程方案**：MovieLens要求每用户至少20条评分才能有效推荐。生产环境对新用户应采用"兴趣标签选择 -> 热门兜底 -> 快速积累行为数据 -> 切换个性化推荐"的分阶段策略

4. **A/B测试的必要性**：离线指标（RMSE/MAE）提升3%不等于业务指标提升3%。必须通过A/B测试验证推荐算法对点击率、转化率、留存率的实际影响。建议测试周期至少2周，覆盖足够多的用户（>10,000）以获得统计显著性

5. **售前场景应用**：用MovieLens做POC有两个优势：数据公开可信、结果可复现。现场展示"为某个用户生成推荐"的过程，让客户直观感受个性化推荐的效果，比任何PPT都有说服力

---

## 核心文献

> 本节列出与本教材主题密切相关的核心学术文献，供博士级深入研究和论文写作参考。

1. **[arXiv:1708.05031]** - "Neural Collaborative Filtering" (He et al., 2017)
   与本教材的关联：NCF神经协同过滤论文，是本教材Day 2"神经协同过滤（NCF）"部分的核心文献，用神经网络替代矩阵分解内积的奠基性工作。

2. **[arXiv:1904.06690]** - "BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer" (Sun et al., 2019)
   与本教材的关联：BERT4Rec序列推荐论文，是本教材Day 2"序列推荐：SASRec/BERT4Rec"的直接文献来源，Transformer在推荐系统中的经典应用。

3. **[arXiv:2005.14165]** - "Language Models are Few-Shot Learners" (Brown et al., 2020)
   与本教材的关联：GPT-3大语言模型论文，是本教材Day 2"LLM驱动的推荐"部分的理论基础，大语言模型的零样本/少样本能力开创了推荐系统新范式。

4. **[arXiv:2304.03442]** - "Generative Agents: Interactive Simulacra of Human Behavior" (Park et al., 2023)
   与本教材的关联：生成式Agent论文，与本教材Day 2"对话式推荐系统"和用户仿真的前沿参考，生成式Agent为推荐系统用户模拟提供了新方法。

5. **[arXiv:2210.03629]** - "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022)
   与本教材的关联：ReAct推理-行动框架论文，是本教材Day 2"对话式推荐Agent"的框架基础，推理-行动协同机制是构建对话式推荐Agent的核心范式。

---

## 知识问答

| # | 问题 | 参考答案要点 | 难度 |
|:--:|------|------------|:----:|
| Q1 | 协同过滤（CF）和基于内容（CB）推荐的核心区别是什么？各自的数据需求有什么不同？ | CF基于"用户-物品交互矩阵"推荐，不需要物品内容信息，但需要足够的交互数据。CB基于物品特征向量推荐，需要物品内容特征，但不需要大量交互数据。CF能发现隐含兴趣，CB更适合冷启动。 | ⭐⭐ |
| Q2 | User-based CF和Item-based CF在什么场景下应该选择哪种？Amazon为什么选择Item-based？ | User-based适合用户数<物品数的场景；Item-based适合物品数稳定且<用户数的场景。Amazon选择Item-based因为商品数百万但相对稳定，物品相似度矩阵可以离线预计算，在线推理毫秒级。 | ⭐⭐⭐ |
| Q3 | 矩阵分解中的隐因子（latent factor）有什么业务含义？以电影推荐为例解释。 | 隐因子是模型自动学习的潜在维度。在电影推荐中，隐因子可能对应"动作程度"、"文艺程度"、"恐怖程度"等潜在主题。用户隐向量表示用户对各主题的偏好程度，物品隐向量表示物品在各主题上的属性。两者内积高=匹配度高。 | ⭐⭐⭐ |
| Q4 | NDCG@K和Precision@K的核心区别是什么？为什么NDCG更适合评估推荐排序质量？ | Precision@K只看Top-K中有多少相关物品，不考虑物品在Top-K中的位置。NDCG@K考虑了排序位置--排在前面的相关物品贡献更大。推荐系统中排序位置极其重要（第1位vs第10位的点击率差异巨大），所以NDCG更贴近实际业务价值。 | ⭐⭐⭐ |
| Q5 | NCF（Neural Collaborative Filtering）相比传统矩阵分解的核心改进是什么？ | 传统MF用用户向量和物品向量的内积预测评分，内积是线性操作。NCF用MLP替代内积，能学习用户和物品之间的非线性关系。NeuMF进一步将GMF（保留线性能力）和MLP（非线性能力）融合，兼顾记忆和泛化。 | ⭐⭐⭐ |
| Q6 | Wide & Deep模型中Wide部分和Deep部分各自的作用是什么？为什么要联合训练？ | Wide部分通过交叉特征记忆频繁共现模式（如"男性+体育"推荐体育内容），Deep部分通过嵌入学习特征的泛化关系。联合训练让模型既有记忆（精确匹配已知模式）又有泛化（发现新关联），单独使用任一部分都有局限。 | ⭐⭐⭐ |
| Q7 | Two-Tower模型为什么适合大规模推荐系统的召回阶段？ | 因为User Tower和Item Tower可以独立计算，物品向量离线预计算并建立FAISS索引，在线只需要计算用户向量+近邻搜索，从百万候选中召回耗时毫秒级。如果是交叉模型（如DeepFM），无法离线预计算，不适合大规模召回。 | ⭐⭐⭐ |
| Q8 | 推荐系统三级架构（召回->排序->重排）中，为什么不在召回阶段直接用排序模型？ | 召回阶段需要从百万候选中筛选，排序模型太慢（需要计算大量特征交叉）。召回用简单模型快速筛选到千级候选，排序用复杂模型在千级候选上精确排序。这是计算成本和精度的工程权衡。 | ⭐⭐⭐ |
| Q9 | 流行度偏差（Popularity Bias）对推荐系统生态有什么长期危害？如何缓解？ | 危害：热门物品越来越热，长尾物品被埋没，导致生态多样性下降、用户审美疲劳、长尾商家流失。缓解方法：流行度惩罚（降低热门物品分数）、长尾扶持（为长尾物品分配探索流量）、多样性约束（MMR重排）。 | ⭐⭐⭐ |
| Q10 | IPS（逆倾向得分）如何解决推荐系统中的曝光偏差？核心思想是什么？ | 核心思想：被曝光概率低的物品的交互数据更"珍贵"（不是因为热门才被看到），应该赋予更高权重。IPS用1/倾向得分作为权重，让低曝光物品的数据影响更大，从而纠正"只从被曝光数据中学习"的偏差。 | ⭐⭐⭐ |

---

## 作业设计

### 必做作业：用Surprise库实现协同过滤推荐

**任务**：

1. 生成或使用真实的用户-内容交互数据（至少100用户×50物品）
2. 分别用User-CF、Item-CF和SVD三种方法训练推荐模型
3. 用5折交叉验证比较三种方法的RMSE和MAE
4. 为3个指定用户各生成Top-5推荐列表
5. 用Precision@5、Recall@5、NDCG@5评估推荐质量
6. 写一份300字的分析报告，比较三种方法的优劣势

**交付物**：可运行的Python代码 + 评估结果表格 + 分析报告

**评分标准**：

| 维度 | 优秀（9-10分） | 良好（7-8分） | 合格（5-6分） | 不合格（<5分） |
|------|-------------|------------|------------|-------------|
| 代码质量 | 可运行、结构化、有注释 | 基本可运行 | 有小bug | 无法运行 |
| 评估完整性 | 三种方法+三种指标+交叉验证 | 三种方法+基本指标 | 仅两种方法 | 评估缺失 |
| 分析深度 | 有洞察的方法对比和建议 | 基本合理的比较 | 仅描述结果 | 缺失分析 |

### 挑战作业：用Two-Tower模型构建营销内容推荐系统

**任务**：

1. 设计营销场景下的用户特征和内容特征体系（各至少5个特征）
2. 用PyTorch实现Two-Tower模型
3. 生成模拟数据（或使用公开数据集）训练模型
4. 实现离线内容向量计算+在线用户向量检索的推荐流程
5. 设计冷启动策略（新用户/新内容）
6. 写一份500字的系统设计文档，包含架构图、特征说明和预期效果

**评分标准**：重点考察特征设计的合理性（是否有业务含义）、模型实现的正确性（Two-Tower架构是否标准）、推荐流程的完整性（是否有离线+在线流程）、以及冷启动策略的实用性。

---

## 费曼学习法演练

### 核心理念
费曼学习法的核心是"以教代学"--如果你不能简单地解释一个概念，说明你还没有真正理解它。

### 演练任务
**任务**：假设你在向电商平台CEO解释为什么传统推荐系统在LLM时代需要升级，以及'对话式推荐'如何改变用户体验

### 演练步骤
1. **选择概念**：从本教材中选一个你觉得最有挑战性的概念
2. **写下解释**：用自己的语言写一段300-500字的解释，目标受众是电商平台CEO
3. **找出空洞**：标记你解释中含糊、跳过或借用术语的地方
4. **回到教材**：针对性补全知识空洞
5. **简化重写**：用更简单的语言重新写一遍，力求让受众真正理解

### 自评标准
- [ ] 解释中没有直接引用教材原文
- [ ] 至少使用了1个类比或比喻
- [ ] 受众能理解核心概念并复述
- [ ] 解释中标注的知识空洞已补全

---

## 推荐资源清单

### 核心论文（必读）
- 📄 **Sarwar et al. (2001) Item-Based CF**: Amazon推荐的学术基础
- 📄 **Koren et al. (2009) Matrix Factorization Techniques for Recommender Systems**: Netflix Prize的经典论文
- 📄 **He et al. (2017) Neural Collaborative Filtering**: NCF原始论文
- 📄 **Cheng et al. (2016) Wide & Deep Learning for Recommender Systems**: Google的Wide & Deep论文
- 📄 **Guo et al. (2017) DeepFM**: 华为的DeepFM论文

### 开源工具（必读）
- 🌐 **Surprise（Python推荐系统库）**: https://surpriselib.com/
- 🌐 **LightFM（混合推荐模型）**: https://github.com/lyst/lightfm
- 🌐 **FAISS（向量检索）**: https://github.com/facebookresearch/faiss
- 🌐 **Microsoft Recommenders**: https://github.com/microsoft/recommenders
- 🌐 **RecBole（一站式推荐框架）**: https://recbole.io/

### 对标课程
- 🌐 **Stanford CS246 Mining Massive Datasets**: https://web.stanford.edu/class/cs246/
- 🌐 **Google Recommendations Course**: https://developers.google.com/machine-learning/recommendation
- 🌐 **UCSD Recommender Systems (Coursera)**: https://www.coursera.org/learn/recommender-systems
- 🌐 **Wharton Customer Analytics**: https://online.wharton.upenn.edu/customer-analytics/

### 进阶阅读（可选）
- 📄 **SASRec (2018) Self-Attentive Sequential Recommendation**: 序列推荐经典
- 📄 **BERT4Rec (2019) Sequential Recommendation with BERT**: 双向序列推荐
- 📄 **MMoE (2018) Multi-gate Mixture-of-Experts**: 多目标推荐
- 📄 **PLE (2020) Progressive Layered Extraction**: MMoE改进版
- 🌐 **DGL-RecGraph（图神经网络推荐）**: https://www.dgl.ai/
- 🌐 **RecSys会议论文**: https://recsys.acm.org/

---

> 💡 **学习建议**：本选修课的知识密度较高，建议分三轮学习。第一轮重点理解概念：能用自己的话解释CF/CB/MF/NCF/Two-Tower各是什么、解决什么问题。第二轮重点跑代码：把Day 1和Day 2的代码全部运行一遍，修改参数观察效果变化。第三轮重点想架构：针对一个你熟悉的业务场景（如你公司的营销内容推荐），用Day 3的架构框架设计一个推荐系统方案。三轮学完后，你就具备了在售前场景中讨论推荐系统方案的能力--不需要能实现生产级系统，但需要能设计架构、评估方案、与工程团队有效沟通。
