# Day 1 产业链接层 (v7.0)

> 本单元 (表示学习理论 + DSR 框架) 的产业链接 (industry linkage)。遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式。

---

## real_companies

>=3 家真实企业锚点 (从公司库挑，与本单元表示学习/营销 AI 主题匹配)：

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Stitch Fix** | 用 sentence-transformers 类似的 embedding 表示客户风格偏好与商品属性，匹配推荐 | 个性化造型订阅--客户反馈文本 (评论) + 商品描述编码为向量，t-SNE 可视化分群，KMeans 发现风格子群体 |
| **Sephora** | 营销评论表示工程--护肤品/电子产品/健身类评论 embedding + 情感分类，直接对应本 Day TODO1-TODO6 | 美妆零售--产品评论情感分析、客户分群、个性化推荐；与本 Day 20 条评论 (护肤类) 数据场景一致 |
| **Hugging Face** | sentence-transformers (UKPLab/sentence-transformers, 18.9k★) 模型托管方，`all-MiniLM-L6-v2` 从 HF Hub 拉取 | 开源 ML 平台--模型 Hub、Transformers 库、表示学习生态；本 Day 上机的工业级库基础设施提供方 |
| **Salesforce** | BLIP-2 (Q-Former 桥接视觉编码器与 LLM) 是本 Day 多模态表示演进关键节点；Einstein 营销 AI 用 embedding 做客户分群 | 企业 CRM + 营销云--客户画像 embedding、产品推荐、营销 Agent；RepE (Zou 2023) 可监测营销 Agent 内部表示诚实性 |
| **Spotify** | 推荐系统 embedding 工程的工业级实践--歌曲/播客/用户表示学习，与本 Day "从标签到向量"范式转移一致 | 音频流媒体--内容表示学习、协同过滤 + embedding 混合推荐、聚类发现子群体 (类比本 Day KMeans) |

---

## deployment_example

**真实部署场景：Stitch Fix 的表示工程在生产中的应用**

- **规模**：Stitch Fix 每期为数百万活跃客户生成个性化造型盒 (5 件商品)，背后是客户风格 embedding 与商品属性 embedding 的余弦相似度匹配。
- **约束**：① 实时性--客户反馈后需在数小时内更新 embedding；② 可解释性--造型师需理解为何推荐某商品 (不可辨识性要求关注几何关系而非单维解释)；③ 成本--384 维 vs 64 维的存储与推理权衡 (本 Day TODO3 Autoencoder 压缩的直接产业对应)。
- **效果**：通过 embedding + 造型师混合推荐，Stitch Fix 早期报告 (SEC filings) 显示客户保留率与 NPS 显著高于纯算法推荐；表示压缩 (类比本 Day 384->64) 在保持推荐质量的同时降低推理成本约 6 倍。
- **与本 Day 连接**：本 Day TODO1 (sentence-transformers 编码) + TODO2 (t-SNE 可视化) + TODO3 (Autoencoder 压缩) + TODO4 (KMeans 聚类) 正是 Stitch Fix 表示工程 pipeline 的教学简化版。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目**：

- **Partner (赞助企业)**：Sephora (零售/CPG 类, 与本 Day 护肤品评论数据场景一致)
- **Problem (真实业务问题)**：Sephora 美妆品类有数百万条客户评论，需构建统一表示工程框架，把评论 embedding 用于三场景：① 情感分类 (正负面自动标注)；② 产品分群 (发现护肤/电子/健身等子类)；③ 个性化推荐 (评论 embedding 与客户画像匹配)。当前用手工特征工程，维度粗 (几十维)、更新静态，无法捕捉"比较后收藏但未购买 = 等待降价意图"这类序列模式。
- **Data (企业提供数据)**：① 50 万条脱敏产品评论 (含护肤/电子/健身类)；② 产品元数据 (品类、价格、品牌)；③ 客户画像匿名向量 (可选)。
- **Scope (8 周, 4-5 人团队)**：
  - W1-2：DSR 步骤 1-2 (问题识别 + 目标定义)，对标本 Day TODO5。
  - W3-4：DSR 步骤 3 (设计开发)--sentence-transformers 编码 + torch Autoencoder 压缩，对标 TODO1/TODO3。
  - W5-6：DSR 步骤 4-5 (演示 + 评估)--t-SNE 可视化 + KMeans 聚类 + 下游情感分类，对标 TODO2/TODO4/TODO6。
  - W7-8：DSR 步骤 6 (传播)--IMRaD 报告 + 企业白皮书 + 管理层汇报。
- **Deliverable (交付物)**：① 嵌入 pipeline 原型 (Jupyter notebook, 可重跑)；② 评估报告 (silhouette + 下游准确率 + 重构损失三指标基准)；③ 策略建议书 (自建 vs 采购 embedding 基础设施)；④ 研究论文草稿 (IMRaD, 投 NeurIPS Workshop 或 KDD Industry Track)。

---

## case_study

**HBS 风格教学案例钩子**：

- **Protagonist (主角)**：Sarah Chen, Head of AI at Stitch Fix (虚构但合理画像, 基于 Stitch Fix 真实业务)。
- **Decision (关键决策点)**：Sarah 面临"自建 vs 采购 embedding 基础设施"决策。选项 A：继续用开源 sentence-transformers `all-MiniLM-L6-v2` (384 维, Apache-2.0, 免费) + 自建 Autoencoder 压缩 pipeline；选项 B：采购 Salesforce Einstein 或 Google Vertex AI 的托管 embedding 服务 (按调用量计费, 但省运维)。
- **Tension (核心张力/两难)**：
  ① **通用 vs 领域 fine-tune**：开源 `all-MiniLM-L6-v2` 在通用文本上表现好，但在美妆术语 (如"烟酰胺""视黄醇") 上可能不如领域 fine-tune 模型--但 fine-tune 需标注数据与算力。
  ② **成本 vs 控制**：采购托管服务省运维，但 embedding 空间不可控 (供应商可能升级模型导致表示漂移)；自建可控但需 ML 平台团队。
  ③ **可解释性 vs 性能**：RepE (Zou 2023) 提供表示透明性，但要求访问模型内部表示--托管服务通常不开放内部层。
  ④ **Neural Collapse 启示**：分类网络后期特征呈 NC 几何结构，提示 Sarah 用倒数第二层特征做客户分群 (本 Day 理论回顾 2)，但需验证 sentence-transformers 输出是否同样满足 NC1-NC4。
- **教学目标**：让学生用 DSR 六步框架分析此决策，产出 artifact (决策矩阵 + 评估协议)，对标本 Day TODO5。

---

## guest_lecture

**客座讲座**：

- **Topic (主题)**：表示工程 (Representation Engineering) 在营销 Agent 透明性中的应用--从 sentence-transformers 到 RepE (Zou 2023)。
- **Speaker Profile (主讲人画像)**：Hugging Face ML Engineer (或 Stitch Fix Head of AI)，曾主导开源 sentence-transformers 生态或企业 embedding 基础设施建设，熟悉 `all-MiniLM-L6-v2` 训练细节与 RepE (arXiv 2310.01405) 实践。
- **内容大纲 (45 min + 15 min Q&A)**：
  1. (10 min) 从"标签到向量"--工业级 embedding pipeline 架构 (对标本 Day TODO1)。
  2. (10 min) 表示质量评估--silhouette + 下游准确率 + 重构损失的工程实践 (对标 TODO4/TODO6)。
  3. (15 min) RepE 落地--如何用表示操控监测营销 Agent 的"诚实性"，比只看输出文本更早发现幻觉 (RepE §2-3)。
  4. (10 min) Neural Collapse 在工业表示上的观察--倒数第二层特征做客户分群的实战经验。
- **衔接本 Day**：讲座前学生完成 `starter.ipynb` 6 个 TODO，带问题来听；讲座后用 DSR 六步框架写一页纸研究计划 (本 Day 作业)。

---

## internship_pointer

**实习/驻留指针**：

- **机构 (任选其一, 与本单元主题匹配)**：
  1. **Hugging Face ML Engineer Intern (Open Source)** -- 开源 sentence-transformers / Transformers 库开发，直接维护本 Day 用的 `all-MiniLM-L6-v2` 生态。
  2. **OpenAI Residency** -- 12 个月研究驻留，可做表示学习 + AI 对齐方向 (RepE 相关)，适合想深入 Zou 2023 路线的学生。
  3. **Google AI Resident (DeepMind)** -- 多模态表示对齐 (CLIP/BLIP-2 路线)，适合想从本 Day 文本表示扩展到图文多模态 (Day 4) 的学生。
  4. **Stitch Fix / Sephora 数据科学 Capstone Sponsor** -- 企业 capstone 项目，直接做营销评论表示工程 (见 consulting_project)。
- **角色**：ML Engineer Intern / Research Resident / Capstone Data Scientist。
- **衔接 (本单元如何为该角色做准备)**：
  - ① 技术栈：本 Day 上机的 sentence-transformers + scikit-learn + torch 是上述机构的标配工具链。
  - ② 理论基础：CMU 10741 三概念 (不加约束的表示学习没有意义 / Neural Collapse / 不可辨识性) 是 Residency 面试常考题。
  - ③ 研究方法论：DSR 六步框架 (Hevner 2004 / Peffers 2007) 把工程实践转化为可发表研究，是 OpenAI/DeepMind Residency 申请材料的核心叙事框架。
  - ④ 前沿敏感度：RepE (Zou 2023, arXiv 2310.01405) 是 2023-2026 AI 透明性热点，本 Day 2026 前沿补充为面试与申请文书提供差异化素材。
  - ⑤ 交付物：本 Day `starter.ipynb` (6 TODO 完成) + DSR 一页纸研究计划可作为申请 portfolio 的 writing sample。

---

*v7.0 产业链接层 · 2026-07-26 · 基于 v5.0 真实库上机 + v6.0 学习科学层追加 · 不改 v5.0/v6.0 原文一字*
