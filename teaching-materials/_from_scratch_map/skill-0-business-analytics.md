# _from_scratch_map: skill-0-business-analytics (v11.0)

> skill-0 AI商业分析基础（预科6 Day）对应 rohitg00 P0 Setup / P1 Math / P2 ML。wave agent 离线消费，链接必须从此文件取，禁止编造。

## 模块概述
- **对应 rohitg00 phase**: P0 Setup & Tooling, P1 Math Foundations, P2 ML Fundamentals
- **from-scratch 主题**: 统计/编程地基的 from-scratch 实现（手写线性回归/逻辑回归/贝叶斯/梯度下降/张量运算）

## Day 映射

### day-1-python-fundamentals: Python编程基础
- **from-scratch 主题**: 手写 numpy 张量运算 + 广播机制
- **rohitg00 链接**:
  - [P0/01 Dev Environment](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/01-dev-environment/README.md) - 开发环境与工具链
  - [P1/12 Tensor Operations](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/12-tensor-operations/README.md) - 张量运算直觉
- **核心算法**: 张量 shape 变换 + 广播

### day-2-data-structures: 数据结构与应用
- **from-scratch 主题**: 手写向量/矩阵运算 + 线性系统求解
- **rohitg00 链接**:
  - [P1/02 Vectors Matrices Operations](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/02-vectors-matrices-operations/README.md) - 向量矩阵运算 from scratch
  - [P1/17 Linear Systems](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/17-linear-systems/README.md) - 线性系统求解
- **核心算法**: 矩阵乘法 + 高斯消元

### day-3-statistics-inference: 描述统计与推断统计
- **from-scratch 主题**: 手写贝叶斯后验更新 + 概率分布采样
- **rohitg00 链接**:
  - [P1/06 Probability and Distributions](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/06-probability-and-distributions/README.md) - 概率分布 from scratch
  - [P1/07 Bayes Theorem](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/07-bayes-theorem/README.md) - 贝叶斯定理
  - [P1/15 Statistics for ML](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/15-statistics-for-ml/README.md) - ML 统计
- **核心算法**: Beta-Binomial 共轭后验

### day-4-regression-probability: 回归分析与概率分布
- **from-scratch 主题**: 手写线性回归 OLS + 梯度下降
- **rohitg00 链接**:
  - [P2/02 Linear Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression/README.md) - 线性回归 from scratch
  - [P2/03 Logistic Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression/README.md) - 逻辑回归
  - [P1/08 Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/08-optimization/README.md) - 梯度下降族
- **核心算法**: OLS 闭式解 $(X^TX)^{-1}X^Ty$ + SGD

### day-5-sql-data-governance: 数据治理与SQL
- **from-scratch 主题**: 手写关系代数 select/project/join
- **rohitg00 链接**:
  - [P0/09 Data Management](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/README.md) - 数据管理
  - [P1/14 Norms and Distances](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/14-norms-and-distances/README.md) - 范数与距离（数据质量度量）
- **核心算法**: 关系代数 + RFM 距离度量

### day-6-research-methodology: 研究方法论入门
- **from-scratch 主题**: 手写可复现实验 + 数值稳定技巧
- **rohitg00 链接**:
  - [P0/12 Debugging and Profiling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/12-debugging-and-profiling/README.md) - 调试与性能分析
  - [P1/13 Numerical Stability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/13-numerical-stability/README.md) - 数值稳定
- **核心算法**: 随机种子控制 + log-sum-exp 稳定
