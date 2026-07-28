# _from_scratch_map: skill-1-representation (v11.0)

> skill-1 表示工程与营销智能（4 Day）对应 rohitg00 P1 Math / P5 NLP / P12 Multimodal。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P1 Math(embeddings/SVD), P5 NLP, P12 Multimodal(alignment only)
- **from-scratch 主题**: 表示学习的 from-scratch 实现（手写 word2vec/TF-IDF/两塔/CLIP/KG抽取）

## Day 映射

### day-1-representation-theory: 表示学习理论
- **from-scratch 主题**: 手写 word2vec SGNS + SVD 降维
- **rohitg00 链接**:
  - [P5/03 Word Embeddings Word2Vec](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/README.md) - word2vec from scratch
  - [P1/11 Singular Value Decomposition](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/11-singular-value-decomposition/README.md) - SVD 降维
- **核心算法**: Skip-gram 负采样 + SVD

### day-2-marketing-representation: 营销数据表示+多模态
- **from-scratch 主题**: 手写 TF-IDF + 两塔检索模型
- **rohitg00 链接**:
  - [P5/02 Bag of Words TF-IDF](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/README.md) - TF-IDF from scratch
  - [P5/22 Embedding Models Deep Dive](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/README.md) - 嵌入模型深挖
- **核心算法**: TF-IDF + 两塔点积相似度

### day-3-knowledge-graph-graphrag: 企业知识图谱+GraphRAG
- **from-scratch 主题**: 手写 KG 三元组抽取 + 图检索
- **rohitg00 链接**:
  - [P5/26 Relation Extraction KG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/README.md) - 关系抽取与 KG 构建
  - [P11/06 RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/README.md) - RAG 基础
  - [P5/23 Chunking Strategies RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/README.md) - RAG 分块
- **核心算法**: 三元组抽取 + 多跳图检索

### day-4-multimodal-alignment: 多模态融合+跨域对齐
- **from-scratch 主题**: 手写 CLIP 对比损失 + 跨模态对齐
- **rohitg00 链接**:
  - [P12/02 CLIP Contrastive Pretraining](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/12-multimodal-ai/02-clip-contrastive-pretraining/README.md) - CLIP 对比预训练
  - [P12/03 BLIP2 QFormer Bridge](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/12-multimodal-ai/03-blip2-qformer-bridge/README.md) - BLIP-2 Q-Former 桥接
- **核心算法**: InfoNCE 对比损失 $\log\frac{\exp(\text{sim}(z_i,z_i^+)/\tau)}{\sum_j \exp(\text{sim}(z_i,z_j^-)/\tau)}$
