# _from_scratch_map: skill-3-causal (v11.0)

> skill-3 因果推断与规模实验（5 Day）对应 rohitg00 P2 ML / P9 RL。rohitg00 因果较薄，部分 from-scratch 合成。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P2 ML(corr vs causation, eval), P9 RL(bandits)
- **from-scratch 主题**: 因果推断的 from-scratch 实现（手写 do-calculus/IPW/DML/PC算法/uplift）

## Day 映射

### day-1-causal-basics: 因果基础
- **from-scratch 主题**: 手写 do-calculus 骨架 + 后门调整
- **rohitg00 链接**:
  - [P2/09 Model Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/README.md) - 模型评估（相关 vs 因果）
  - [P1/21 Graph Theory](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/21-graph-theory/README.md) - 图论（因果图基础）
- **核心算法**: 后门调整 $P(y|do(x)) = \sum_z P(y|x,z)P(z)$

### day-2-ab-testing: A/B测试
- **from-scratch 主题**: 手写 A/B 检验 + Thompson sampling bandit
- **rohitg00 链接**:
  - [P2/09 Model Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/README.md) - 评估与假设检验
  - [P9/04 Q Learning SARSA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/04-q-learning-sarsa/README.md) - bandit 基础
- **核心算法**: Welch t 检验 + Thompson sampling

### day-3-observational-causal: 观测因果
- **from-scratch 主题**: 手写 IPW + 双重机器学习 (DML)
- **rohitg00 链接**:
  - [P2/15 Statistics for ML](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/15-statistics-for-ml/README.md) - 统计（注：此处 15 在 P2 目录，统计推断）
  - [P1/18 Convex Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/18-convex-optimization/README.md) - 凸优化（DML 正交化）
- **核心算法**: IPW $\hat\tau_{IPW} = \frac{1}{n}\sum \frac{TY}{\hat e(X)}$ + DML 正交

### day-4-causal-discovery: 因果发现
- **from-scratch 主题**: 手写 PC 算法骨架 + 条件独立性检验
- **rohitg00 链接**:
  - [P1/21 Graph Theory](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/21-graph-theory/README.md) - 图论（DAG）
  - [P2/07 Unsupervised Learning](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/07-unsupervised-learning/README.md) - 无监督（结构学习）
- **核心算法**: PC 算法 + 条件独立性检验

### day-5-scale-marketing: 规模营销
- **from-scratch 主题**: 手写 uplift modeling + MAB 预算分配
- **rohitg00 链接**:
  - [P2/13 ML Pipelines](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/13-ml-pipelines/README.md) - ML pipeline
  - [P9/06 Policy Gradients REINFORCE](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/06-policy-gradients-reinforce/README.md) - 策略梯度
- **核心算法**: Uplift Qini + MAB 预算分配
