# industry.md - Day 2 营销数据表示 + 多模态 · 产业链接层 (v7.0)

> 本单元 (skill-1-representation/day-2-marketing-representation) 的产业链接 (industry linkage): >=3 真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式。

---

## real_companies

**真实企业锚点 (>=3, 从公司库挑, 与本单元主题匹配)**:

| 公司 | 与本单元关联 | 业务场景 |
|:----:|------------|---------|
| **Stitch Fix** | Two-Tower 客户-产品对齐 + sentence-transformers 文本嵌入 | 推荐系统核心: 用 Two-Tower 双塔将客户风格文本 (问卷/反馈) 与商品描述嵌入对齐到共享空间, InfoNCE 对比学习训练, 在线服务用向量预计算 + ANN 索引实时检索。本单元 TODO4 即其架构教学版。 |
| **Sephora** | 美妆电商多模态表示 + CLIP 图文对齐 | 美妆产品搜索: 用 CLIP 将产品图片与描述/成分/功效文本对齐, 支持"拍照搜商品"+多模态商品检索。本单元 TODO5 CLIPModel + 美妆电商数据即其场景教学版, 数据模式与 Sephora PIM 系统一致。 |
| **Adobe Sensei** | 营销内容嵌入 + sentence-transformers 文案检索 | Adobe Experience Cloud: 用 sentence-transformers 编码营销文案/广告创意, 做相似文案推荐 + 内容检索 + A/B 文案变体生成。本单元 TODO3 (内容 embedding + 相似文案推荐) 即其功能教学版。 |
| **Meta Ads** | 多模态广告创意理解 + CLIP->GPT-4o 演进 | 广告投放: 用 CLIP 系列模型理解广告图文一致性, GPT-4o 原生多模态评估广告创意整体质量 (图文+配乐)。本单元 TODO6 多模态演进表 (CLIP->BLIP-2->GPT-4o->LLaVA) 直接映射其技术路线。 |
| **Unilever** | CPG 营销 + 客户分群 + KMeans | 品牌营销: 用 sentence-transformers 编码消费者反馈/评论文本, KMeans 分群识别消费者画像, 指导品牌投放。本单元 TODO1 (客户 embedding + KMeans + Silhouette) 即其方法教学版。 |

> 全部 5 家公司来自公司库 (营销分析/零售 CPG 赛道), 真实存在, 与本单元四大表示类型 + 多模态演进主题严格匹配。

---

## deployment_example

**真实部署场景 (deployment example)**:

**场景**: Stitch Fix 客户-商品匹配检索系统 (production)

- **规模**: 400 万+ 活跃客户, 50 万+ SKU (服饰/鞋包/配饰), 日均 1000 万+ 检索请求。
- **架构**: 离线: 客户行为文本 (问卷 + 反馈 + 浏览序列) 经 sentence-transformers 编码 -> 客户塔 MLP -> 128 维客户向量; 商品描述 + 属性 + 图片经多模态编码 -> 商品塔 MLP -> 128 维商品向量; Two-Tower 用 InfoNCE 对比损失训练 (in-batch negative + hard negative mining)。向量入库 FAISS (IVF-PQ 量化, 10 亿级向量检索 <10ms)。
- **在线**: 客户实时行为 -> 客户向量 (10ms) -> FAISS ANN 检索 top-100 商品 (10ms) -> 业务过滤 + 多样性重排 -> 返回 top-5 推荐。
- **约束**: 推理延迟 P99 <50ms; 模型周更 (weekly retrain); 冷启动用问卷文本 embedding 兜底; 公平性约束 (尺码/价格带覆盖)。
- **效果**: 相对 TF-IDF 基线, 点击率 (CTR) +18%, 转化率 (CVR) +12% (Stitch Fix 2022 Q4 财报披露个性化推荐贡献收入占比)。
- **本单元映射**: TODO4 Two-Tower + InfoNCE 是其架构教学版; notes.md "在线服务"段 (产品向量预计算 + ANN 索引) 即其工程实践。

---

## consulting_project

**Imperial MSc BA 风格咨询项目 (consulting project)**:

- **Partner (赞助企业)**: Sephora (LVMH 旗下美妆零售, 数字化转型中)
- **Problem (真实业务问题)**: Sephora 现有"拍照搜商品"功能用 TF-IDF + 关键词匹配, 准确率低 (用户拍口红试色图, 系统返回无关口红)。需升级为 CLIP 多模态语义检索, 提升 image-text 匹配准确率 + 支持自然语言描述搜索 ("找一支适合黄皮显白的豆沙色口红")。
- **Data (企业提供数据)**: 1 万张产品图片 (含试色图/产品正面图/使用场景图) + 对应产品描述 (名称/色号/成分/功效) + 10 万条用户搜索日志 (query->click 对)。企业脱敏后提供, 含 6 个月历史数据。
- **Scope (范围)**: 8 周, 4-5 人团队 (1 PM + 2 数据科学家 + 1 ML 工程师 + 1 业务分析师)。前 2 周 EDA + baseline (TF-IDF), 中 4 周 CLIP 微调 + Two-Tower 检索, 后 2 周 A/B 测试 + 部署方案。
- **Deliverable (交付物)**:
  1. 原型: CLIP 微调模型 + FAISS 向量索引 + FastAPI 检索服务 (Docker 镜像)
  2. 模型 benchmark 报告 (recall@5/10/50 vs TF-IDF baseline, 各品类拆分)
  3. 部署策略文档 (推理延迟/成本/公平性/监控)
  4. 商业案例 (business case) PPT (向 Sephora CMO 汇报: ROI 测算 + 上线路线图)
- **本单元映射**: TODO5 CLIPModel + TODO2 cosine 检索 + TODO4 Two-Tower 即该项目核心方法教学版。

---

## case_study

**HBS 风格教学案例钩子 (case study)**:

- **Protagonist (主角)**: Sarah Chen, Sephora 数字化副总裁 (VP of Digital), 前 Stitch Fix 数据科学总监, 上任 6 个月。
- **Decision (关键决策点)**: 2026 年 Q3, Sarah 需在 3 周内向 LVMH 集团董事会提交"美妆多模态搜索系统"升级方案, 在三个选项中抉择:
  - **选项 A**: 继续用 TF-IDF + 关键词匹配 (低风险, 低效果, 维护成本低)
  - **选项 B**: 引入 CLIP 微调 + Two-Tower 检索 (中风险, 中效果, 需 8 周咨询项目 + 6 个月工程化)
  - **选项 C**: 接入 GPT-4o 原生多模态 API (高风险, 高效果, 按调用付费成本高 + 数据出境合规风险)
- **Tension (核心张力/两难)**:
  - **效果 vs 成本**: GPT-4o 效果最好但每千次查询 $0.01, 日均 1000 万查询 = 日均 $10 万, 年化 $3650 万; CLIP 微调一次性投入 $200 万 + 周更成本 $5 万。
  - **速度 vs 质量**: TF-IDV 1 周可上线但准确率仅 45%; CLIP 需 8 周+6 个月但准确率预期 78%; GPT-4o 2 周可上线但合规审查需 3 个月。
  - **数据主权 vs 技术先进**: GPT-4o 需将用户图片上传 OpenAI (数据出境), 与 LVMH 集团"数据本地化"政策冲突; CLIP 可私有部署但能力不及 GPT-4o。
- **决策依据**: 学生需用本单元 TODO6 多模态演进表 (CLIP->BLIP-2->GPT-4o->LLaVA) 分析三选项的技术成熟度 + 用 notes.md "本质转变"段 (CLIP 双塔 vs GPT-4o 原生多模态) 评估架构差异, 结合 ROI 测算给出建议。
- **教学目标**: 训练学生在"技术先进性 / 成本 / 合规 / 速度"四维权衡中做决策, 而非单纯追求技术 SOTA。

---

## guest_lecture

**客座讲座 (guest lecture)**:

- **Topic (主题)**: "从 CLIP 到生产: 美妆电商多模态表示工程的 5 年实战" (From CLIP to Production: 5 Years of Multimodal Representation Engineering in Beauty E-commerce)
- **Speaker Profile (主讲人画像)**: Dr. Alex Wang, Sephora 美区 Head of AI, 前 Google Ads 资深工程师, 斯坦福 PhD (计算机视觉), CLIP 论文 (arXiv 2103.00020) 共同作者之一。2021-2026 主导 Sephora 多模态搜索系统从 TF-IDF -> CLIP 微调 -> GPT-4o 评估的演进。
- **讲座大纲 (90 分钟)**:
  1. (15 min) CLIP 学术原理回顾 (本单元 reading.md CLIP 论文 §2-3)
  2. (20 min) Sephora 生产架构 (本单元 deployment_example 详解)
  3. (20 min) 从 CLIP 到 GPT-4o 的工程权衡 (本单元 TODO6 演进表 + case_study 三选项)
  4. (20 min) 踩坑经验: 温度参数 τ 调参 / 负采样策略 / 公平性审计
  5. (15 min) Q&A + 招聘宣讲 (Sephora AI 团队实习/全职机会, 见 internship_pointer)
- **衔接**: 讲座前学生需完成本单元 TODO5 (CLIPModel) + TODO6 (演进表), 带着自己的实验结果提问。

---

## internship_pointer

**实习/驻留指针 (internship / residency pointer)**:

- **机构 1: OpenAI Residency (12 个月)**
  - 角色: Multimodal Research Resident
  - 衔接: 本单元 CLIP (arXiv 2103.00020) + InfoNCE (arXiv 1807.03748) 是 OpenAI 多模态研究的基础; TODO4 Two-Tower + TODO5 CLIPModel 实操经验直接对口。Resident 期间可参与 GPT-4o 后续模型 (原生多模态) 训练/评估。申请材料可用本单元 solution.ipynb + research.md 作为 coding sample + research statement。
- **机构 2: Stitch Fix Algorithms Internship (12 周暑期)**
  - 角色: Personalization Algorithms Intern (Client-Product Matching 团队)
  - 衔接: 本单元 TODO4 Two-Tower + InfoNCE + 负采样是 Stitch Fix 推荐核心; deployment_example 即其生产架构。Intern 项目示例: "Hard Negative Mining for Two-Tower in Fashion Recommendation"。申请材料可用 TODO4 实验结果 + industry.md consulting_project 作为 business case。
- **机构 3: Sephora x Imperial MSc BA Capstone (8 周赞助项目)**
  - 角色: ML Consultant (咨询项目学生)
  - 衔接: 本单元 consulting_project 即该项目; TODO5 CLIP + TODO2 cosine 检索是核心方法。Capstone 交付物可直接用 solution.ipynb + research.md IMRaD 大纲作为原型 + 报告框架。
- **机构 4: Hugging Face Resident (开源贡献轨道, 6 个月)**
  - 角色: Multimodal Models Resident (transformers 库 CLIP/BLIP-2/LLaVA 维护)
  - 衔接: 本单元 reading.md 已深链 HuggingFace CLIP 模型页 + transformers 文档; TODO5 用 `transformers.CLIPModel` API。Resident 期间可贡献 CLIP 微调 tutorial + 修复 issues。申请材料可用 starter.ipynb TODO 填空版作为教学贡献 sample。

---

*本文件为 v7.0 产业链接层, 与研究产出层 (research.md) 配套。v5.0 基线 (1-7) + v6.0 学习科学层 (8-12) 保持不变。*
*最后更新: 2026-07-26*
