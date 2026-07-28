# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E9 AI安全与对齐 · Day 1 价值对齐与Constitutional AI
> **scratch 哲学**：不调 trl/DPOTrainer，手写 Bradley-Terry 偏好模型 + DPO 损失，从奖励模型到隐式奖励直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 RLHF 奖励模型损失 + DPO 偏好优化目标**。对应 rohitg00 P18/05 Constitutional AI RLAIF。notes.md/starter.ipynb 用 deepeval BaseMetric（规则评分）+ garak 探针做对齐"评估"，本层补上对齐"训练"的数学底座：从 Bradley-Terry 偏好模型推导 RLHF 奖励模型损失，再用 KL 约束最优策略的闭式解反演出 DPO 的 sigmoid 偏好目标，让"为什么 DPO 不需要显式奖励模型"在白板级代码中显形。

## core_algorithm

RLHF 的第一步是训练奖励模型 $r_\theta(x,y)$。偏好数据形如 $(x, y_w, y_l)$（$y_w$ 优于 $y_l$）。采用 Bradley-Terry 模型，假设偏好概率由奖励差驱动：

$$P(y_w \succ y_l \mid x) = \sigma(r_\theta(x, y_w) - r_\theta(x, y_l)) = \frac{1}{1 + e^{-(r_w - r_l)}}$$

奖励模型损失为负对数似然：

$$\mathcal{L}_{RM}(\theta) = -\log \sigma(r_\theta(x, y_w) - r_\theta(x, y_l))$$

RLHF 第二步用 PPO 优化策略 $\pi_\theta$，目标为奖励最大化带 KL 约束：$\max_\pi \mathbb{E}[r(x,y)] - \beta \, D_{KL}(\pi \| \pi_{ref})$。该 KL 约束问题的最优策略有闭式解：

$$\pi^*(y|x) = \frac{1}{Z(x)} \pi_{ref}(y|x) \exp\!\left(\frac{r(x,y)}{\beta}\right), \quad Z(x) = \sum_y \pi_{ref}(y|x) \exp\!\left(\frac{r(x,y)}{\beta}\right)$$

对该闭式解反解奖励：$r(x,y) = \beta \log \frac{\pi^*(y|x)}{\pi_{ref}(y|x)} + \beta \log Z(x)$。代入 Bradley-Terry 偏好概率，配分函数 $Z(x)$ 在两个响应的奖励差中**相消**：

$$P(y_w \succ y_l \mid x) = \sigma\!\left(\beta \left[\log\frac{\pi^*(y_w|x)}{\pi_{ref}(y_w|x)} - \log\frac{\pi^*(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right)$$

这就是 DPO 的核心洞察：**偏好概率可直接用策略的对数比表达，无需显式奖励模型**。DPO 损失：

$$\mathcal{L}_{DPO}(\theta) = -\log \sigma\!\left(\beta \left[\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right)$$

关键性质：当 $\beta \to 0$ 时偏好概率趋于 0.5（弱约束），$\beta \to \infty$ 时趋于硬偏好；$\log Z(x)$ 的相消是 DPO 可绕开奖励模型的数学根源，也是 DPO 比 PPO 训练更稳定的几何原因（无 RM 与策略的双环耦合）。

## code_artifact

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))

def bradley_terry_prob(r_w, r_l):
    # P(y_w > y_l | x) = sigmoid(r_w - r_l)
    return sigmoid(r_w - r_l)

def rm_loss(r_w, r_l):
    # RLHF reward model loss: -log sigmoid(r_w - r_l)
    return -np.log(sigmoid(r_w - r_l) + 1e-9)

def dpo_loss(logp_w, logp_ref_w, logp_l, logp_ref_l, beta=0.1):
    # DPO: -log sigmoid(beta * (log(pi_w/pi_ref_w) - log(pi_l/pi_ref_l)))
    margin_w = logp_w - logp_ref_w
    margin_l = logp_l - logp_ref_l
    z = beta * (margin_w - margin_l)
    return -np.log(sigmoid(z) + 1e-9)

def reward_model(X, w):
    # linear reward r(x,y) = phi(x,y)^T w
    return X @ w

# verification_property:
#   Z(x) cancellation -> dpo_loss invariant to shared logp shift;
#   rm_loss == dpo_loss under r := beta*log(pi/pi_ref) (consistency);
#   bradley_terry_prob in (0,1); dpo_loss >= 0
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    w = rng.standard_normal(4)
    X = rng.standard_normal((5, 4))
    r = reward_model(X, w)
    r_w, r_l = r[0], r[1]
    p = bradley_terry_prob(r_w, r_l)
    assert 0.0 < p < 1.0
    assert rm_loss(r_w, r_l) >= 0.0
    logp_w, logp_ref_w = -0.5, -0.6
    logp_l, logp_ref_l = -1.2, -0.7
    loss = dpo_loss(logp_w, logp_ref_w, logp_l, logp_ref_l, beta=0.1)
    c = 0.33
    loss2 = dpo_loss(logp_w + c, logp_ref_w, logp_l + c, logp_ref_l, beta=0.1)
    assert abs(loss - loss2) < 1e-9, "DPO loss invariant to shared logp shift (Z cancels)"
    r_w2 = 0.1 * (logp_w - logp_ref_w)
    r_l2 = 0.1 * (logp_l - logp_ref_l)
    assert abs(rm_loss(r_w2, r_l2) - loss) < 1e-6, "RM loss == DPO loss under r=beta*log(pi/pi_ref)"
```

**verification_property**: DPO 损失对 $\log\pi$ 的共同平移不变（配分函数 $Z(x)$ 相消）；当令 $r(x,y)=\beta\log(\pi/\pi_{ref})$ 时 RM 损失与 DPO 损失数值相等（一致性）；偏好概率落在 (0,1)；DPO 损失非负。

## connection_to_unit

1. **评估 vs 训练的分层**：notes.md/starter.ipynb 用 deepeval `BaseMetric` 做 HHH 对齐**评估**（规则打分），from-scratch 版补齐对齐**训练**的数学底座--RLHF 奖励模型损失 + DPO 偏好目标。评估回答"当前输出是否对齐"，训练回答"如何把模型推向对齐"，二者构成对齐工程闭环，缺一不可。
2. **库 vs 手写的奖励建模**：工业 RLHF 用 `trl.RewardTrainer` 训练奖励模型、`DPOTrainer` 训练策略，from-scratch 版用 `sigmoid(r_w - r_l)` 一个函数表达 Bradley-Terry 偏好假设，让"奖励差驱动偏好"这个核心假设不被 trl 的 Trainer 抽象遮蔽--研究者能直接看到 PPO 不稳定时 RM 损失的梯度来源。
3. **DPO 跳过奖励模型的数学根源**：notes.md 关键回顾 2 表格说"DPO 不需要奖励模型（隐式推导）"，from-scratch 版用 $Z(x)$ 相消的不变性验证显式证明--共同平移 $\log\pi$ 损失不变，这是 DPO 可绕开显式 RM 的数值证据，而 trl 版把这个推导藏进 `compute_loss` 内部。
4. **宪法与奖励的衔接**：starter.ipynb TODO6 的"企业宪法"用 LLM-as-a-judge 生成偏好对 $(y_w, y_l)$，from-scratch 版的 `dpo_loss` 正是消费这些偏好对的目标函数--CAI 的"宪法批评"产出偏好数据，DPO 的 sigmoid 目标消费它，衔接点在此显形。

## deep_dive_links

- [P18/05 Constitutional AI RLAIF - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/05-constitutional-ai-rlaif/README.md) - CAI/RLAIF：宪法自我批评产出偏好数据，喂给本 from-scratch 的 DPO 损失
- [P18/11 Scalable Oversight Weak to Strong - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong/README.md) - 弱到强监督：偏好标注的规模化路径，决定 RM/DPO 训练数据质量上限

## exercises

1. 在本单元 `starter.ipynb` TODO2（HarmlessMetric）运行后，把 3 个营销用例的 HHH 评分当作"奖励" $r$，用 `bradley_terry_prob` 计算合规文案优于违规文案的偏好概率。验证：合规文案奖励高时概率 > 0.5，说明 HHH 评分可作为 RM 的廉价替代。
2. 将 `dpo_loss` 的 `beta` 从 0.01 扫到 10.0，绘制损失随 beta 的变化曲线。解释：beta 为何等价于 KL 约束强度？与 notes.md 关键回顾 2 表格中"DPO 简单/稳定"的论断对照--beta 过大时损失梯度会发生什么？
3. 构造"奖励黑客"场景：令奖励模型 $r_\theta$ 对含"最佳"词的文案给高奖励（模拟广告法违规被奖励），验证 RM 损失下降但 HHH Harmless 维度下降。这正是 notes.md 关键回顾 1 所述 Reward Hacking 的 from-scratch 复现。
4. TODO: 在 `practice.md` D2 的 `HarmlessMetric` 实现基础上，为它添加一个"偏好对生成器"：给定两条文案，输出 $(y_w, y_l)$ 与 `dpo_loss` 所需的 `logp` 占位值，把评估 metric 升级为可喂给 DPO 训练的偏好数据源。
