# _from_scratch_map: elective-e2-marketing-analytics (v11.0)

> 选修E2 营销分析（3 Day）对应 rohitg00 P2 ML。rohitg00 无营销层，映射到回归/偏差方差/pipeline。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P2 ML Fundamentals(regression/eval/pipeline), P9 RL(Markov MTA 辅助)
- **from-scratch 主题**: 营销分析 from-scratch（手写 OLS/BG-NBD/MMM/MTA）

## Day 映射

### day-1-framework-descriptive-diagnostic: 框架+描述诊断
- **from-scratch 主题**: 手写描述性统计 + OLS 回归诊断
- **rohitg00 链接**:
  - [P2/02 Linear Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression/README.md) - 线性回归 from scratch
  - [P1/15 Statistics for ML](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/15-statistics-for-ml/README.md) - ML 统计
- **核心算法**: OLS $(X^TX)^{-1}X^Ty$ + 残差诊断

### day-2-clv-churn-prediction: CLV+流失预测
- **from-scratch 主题**: 手写 BG/NBD 客户生存 + 逻辑回归流失
- **rohitg00 链接**:
  - [P2/03 Logistic Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression/README.md) - 逻辑回归
  - [P2/10 Bias Variance](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/10-bias-variance/README.md) - 偏差-方差
- **核心算法**: BG/NBD 生存函数 + sigmoid 流失概率

### day-3-mmm-mta-incremental: MMM+MTA+增量
- **from-scratch 主题**: 手写 MMM 回归 + Markov MTA 归因
- **rohitg00 链接**:
  - [P2/13 ML Pipelines](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/13-ml-pipelines/README.md) - ML pipeline
  - [P9/04 Q Learning SARSA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/04-q-learning-sarsa/README.md) - MDP 基础（Markov 归因）
- **核心算法**: MMM 岭回归 + Markov 移除效应归因
