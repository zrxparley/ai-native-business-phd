# _from_scratch_map: elective-e3-llm-intro (v11.0)

> 选修E3 LLM工程入门（3 Day）对应 rohitg00 P7 Transformer / P10 LLMs from Scratch / P11 LLM Eng。最厚选修，旗舰。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P7 Transformers(self-attention/full), P10 LLMs from Scratch(pretrain/mini-GPT), P11 LLM Eng(RAG/function-calling)
- **from-scratch 主题**: LLM 全栈 from-scratch（手写 attention/mini-GPT/RAG/serving）— 旗舰单元

## Day 映射

### day-1-transformer-architecture-training: Transformer架构+训练
- **from-scratch 主题**: 手写 scaled dot-product attention + mini-GPT 前向（旗舰）
- **rohitg00 链接**:
  - [P7/02 Self Attention from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch/README.md) - 自注意力 from scratch
  - [P7/05 Full Transformer](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/05-full-transformer/README.md) - 完整 transformer
  - [P10/04 Pre-training Mini GPT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/04-pre-training-mini-gpt/README.md) - mini-GPT 预训练
- **核心算法**: $\text{softmax}(QK^T/\sqrt{d_k})V$ + 残差/LayerNorm 块堆叠

### day-2-llm-application-engineering: LLM应用工程
- **from-scratch 主题**: 手写 RAG 检索 + function calling 分发
- **rohitg00 链接**:
  - [P11/06 RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/README.md) - RAG 基础
  - [P11/09 Function Calling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/09-function-calling/README.md) - 函数调用
  - [P11/14 Model Context Protocol](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/14-model-context-protocol/README.md) - MCP
- **核心算法**: top-k 向量检索 + JSON schema 工具分发

### day-3-llm-evaluation-deployment: LLM评估+部署
- **from-scratch 主题**: 手写 LLM eval harness + 简易 serving 骨架
- **rohitg00 链接**:
  - [P11/10 Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/10-evaluation/README.md) - 评估
  - [P17/04 vLLM Serving Internals](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/04-vllm-serving-internals/README.md) - vLLM 内部
- **核心算法**: 指标矩阵 + 连续批处理骨架
