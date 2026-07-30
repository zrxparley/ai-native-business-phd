# Capstone：AI和商业分析项目

> **版本**：v4.0 | **日期**：2026-07-16 | **学时**：贯穿始终（建议12-24周）  
> **修读者**：aha.gare  
> **学位要求**：AI原生化商业博士课程的最终整合交付  
> **论文方向**：「AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构」  
> **方法论骨架**：Design Science Research（DSR）框架  
> **英语轨道**：英文技术写作（GitHub Pages / Jupyter Notebook / 技术博客 / 论文草稿）  
> **前置条件**：完成全部核心技能（技能1-5）+ 模块R + 至少3门选修  
> **课程哲学**：做出来才算数 -> **研究即贡献**--Capstone不只是"做一个项目"，而是"创造一份可传播的知识"

---

## 一、Capstone概述

### 1.1 博士论文方向

本Capstone的论文方向已锚定为：

> **「AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构」**

这个方向是整个博士课程五技能的整合点：

```
技能1（表示工程）──→ 数据表示层：客户/产品/内容的向量化表示与知识图谱
        │
技能2（原生架构）──→ 架构设计层：Agent编排架构与人机协作治理
        │
技能3（因果推断）──→ 决策验证层：因果实验设计与效果评估
        │
技能4（商业模式）──→ 价值闭环层：商业模式设计与ROI评估
        │
技能5（系统落地）──→ 工程实现层：LangGraph编排+生产部署+可观测性
```

**为什么选择这个方向**：

1. **与工作直接相关**：aha.gare是售前解决方案产品经理，聚焦AI+企业营销，这个方向可以直接应用于工作
2. **学术贡献潜力**："从表示工程到因果决策的闭环"是一个完整的研究框架，有明确的研究空白
3. **技术前沿性**：融合了GraphRAG、LangGraph、因果推断、Agent经济等2026年前沿技术
4. **实践可验证性**：可以在真实企业场景中验证，不是纯理论研究

### 1.2 双路径设计

v4.0提供两条Capstone路径，学习者根据自身目标和条件选择：

| 维度 | 研究型Capstone | 工程型Capstone |
|------|---------------|---------------|
| **定位** | 学术研究 | 工程实践 |
| **核心交付物** | IMRaD论文草稿（3000-5000字）+ 系统原型 + 文献综述 | 可运行系统 + 技术文档 + Demo视频 + 论文大纲 |
| **方法论** | DSR + PRISMA + 混合方法 | DSR + 行动研究 |
| **评估重点** | 学术贡献度、研究严谨性 | 工程完成度、实践价值 |
| **适合人群** | 有学术发表意向 | 侧重工程落地 |
| **预计工作量** | 80-120h | 60-100h |
| **后续路径** | 投稿学术期刊/会议 | 产品化/创业/内部推广 |

**路径选择决策树**：

```
你的目标是什么？
├─ 学术发表（期刊/会议论文）
│  └─ → 研究型Capstone
│
├─ 工程交付（产品/系统/方案）
│  └─ → 工程型Capstone
│
└─ 两者兼顾
   ├─ 时间充裕（>100h）→ 研究型（论文+系统）
   └─ 时间有限（<80h）→ 工程型（系统+大纲）
```

**路径选择建议**：

对于aha.gare的背景（售前解决方案产品经理，聚焦AI+企业营销），建议选择**研究型Capstone**，原因：
1. 已有较强的工程实践能力，需要补的是学术研究能力
2. 博士课程的核心区别在于"创造新知识"
3. 论文草稿可以作为职业发展的差异化资产
4. 如果时间不允许，可以中途切换到工程型

### 1.3 DSR框架作为方法论骨架

Design Science Research（DSR）是本Capstone的方法论骨架，贯穿六个阶段：

**DSR六步流程与Capstone六阶段的映射**：

| DSR步骤 | 核心问题 | Capstone阶段 |
|---------|---------|-------------|
| 1. 问题识别与动机 | 研究问题为什么重要？ | Phase 1：问题定义与文献综述 |
| 2. 定义解决方案目标 | artifact应该达到什么效果？ | Phase 1-2：目标定义 + 表示设计 |
| 3. 设计与开发 | 构建artifact | Phase 2-3：知识图谱 + Agent架构 |
| 4. 演示 | 在真实场景中展示 | Phase 3-4：系统实现 + 实验验证 |
| 5. 评估 | 系统化评估效果 | Phase 4-5：因果验证 + 价值评估 |
| 6. 传播 | 发表论文，产出设计原则 | Phase 6：论文撰写与发表 |

**DSR的核心产出--设计原则（Design Principles）**：

DSR不仅要求"做出一个系统"，更要求"从中提炼出可复用的设计原则"。例如：
- "在营销Agent系统中，将因果推断嵌入决策回路（而非仅作为事后分析工具）可以显著提升决策质量"
- "企业知识图谱与GraphRAG的融合可以有效解决营销知识库的全局推理问题"
- "人机协作治理框架中，引入'安全检查Agent'作为独立审计层可以将Prompt Injection成功率降低至5%以下"

这些设计原则是Capstone的学术贡献核心。

---

## 二、六阶段详细指导

### Phase 1：问题定义与文献综述

> **预计时间**：2-3周 | **核心交付物**：文献综述报告（20-30篇核心文献）+ 研究问题定义书

#### 1.1 阶段目标

本阶段的目标是：
1. 明确研究问题--你要解决什么问题？为什么这个问题重要？
2. 完成系统文献综述--前人已经做了什么？还有什么空白？
3. 用DSR框架定义artifact目标--你要设计什么？它应该达到什么效果？

#### 1.2 用PRISMA方法做系统文献综述

PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）是系统文献综述的标准方法。

**PRISMA四步流程**：

```
Step 1: 检索（Identification）
  ├─ 定义数据库：Google Scholar, ACM Digital Library, IEEE Xplore, SSRN
  ├─ 定义关键词（中英文）：
  │   ├─ 英文：AI marketing agent, representation engineering, causal decision making,
  │   │        LLM agent architecture, knowledge graph RAG, agentic marketing
  │   └─ 中文：AI营销智能体, 表示工程, 因果决策, Agent架构, 知识图谱增强检索
  ├─ 定义时间范围：2020-2026（聚焦近5年前沿）
  └─ 记录检索到的文献总数

Step 2: 筛选（Screening）
  ├─ 纳入标准：
  │   ├─ 与AI营销/Agent架构/因果决策直接相关
  │   ├─ 发表在同行评审期刊/会议，或高质量预印本
  │   ├─ 有明确的研究方法和结果
  │   └─ 英文或中文
  ├─ 排除标准：
  │   ├─ 纯概念性文章无实证数据
  │   ├─ 与主题仅边缘相关
  │   └─ 质量评估不达标
  └─ 记录筛选过程和排除原因

Step 3: 质量评估（Quality Assessment）
  ├─ 评估维度：样本量、方法严谨性、理论贡献、实践价值
  ├─ 评分标准：高/中/低
  └─ 保留高质量文献（目标：20-30篇核心文献）

Step 4: 综合（Synthesis）
  ├─ 用表格总结每篇文献：作者、年份、研究问题、方法、发现、局限
  ├─ 识别研究空白（gap analysis）
  └─ 定位你的研究在文献中的位置
```

**文献综述报告模板**：

```markdown
## 文献综述报告

### 1. 检索策略
- 数据库：Google Scholar, ACM DL, IEEE Xplore, SSRN
- 关键词：[列出关键词]
- 检索时间范围：2020-2026
- 检索结果：共找到XXX篇

### 2. 筛选结果
- 初步检索：XXX篇
- 标题/摘要筛选后：XX篇
- 全文阅读后：XX篇
- 质量评估后纳入：XX篇

### 3. 文献分类与综合

#### 3.1 AI营销Agent架构
| 文献 | 研究问题 | 方法 | 发现 | 局限 |
|------|---------|------|------|------|
| [1] | ... | ... | ... | ... |

#### 3.2 表示工程与知识图谱
| 文献 | 研究问题 | 方法 | 发现 | 局限 |
|------|---------|------|------|------|
| [5] | ... | ... | ... | ... |

#### 3.3 因果推断在营销中的应用
...

### 4. 研究空白分析
基于文献综述，识别以下研究空白：
1. 空白1：...
2. 空白2：...
3. 空白3：...

### 5. 本研究的位置
本研究通过[方法]填补[空白]，预期贡献是...
```

#### 1.3 用DSR框架定义研究问题

**研究问题定义书模板**：

```markdown
## 研究问题定义书

### 1. 问题识别（Problem Identification）
研究背景：企业营销决策面临[具体问题]...
现有方案的不足：[为什么现有方案不够好]...
研究的重要性：[为什么解决这个问题很重要]...

### 2. 解决方案目标（Solution Objectives）
artifact目标：设计一个[具体描述]的系统/框架/方法...
目标指标：
- 功能性目标：[系统能做什么]
- 性能目标：[量化指标，如准确率、效率提升]
- 安全性目标：[安全要求]

### 3. artifact描述
artifact类型：[模型/方法/框架/原型系统]
核心组件：
1. [组件1]：[描述]
2. [组件2]：[描述]
3. [组件3]：[描述]

### 4. 预期贡献
理论贡献：[对学术知识的贡献]
实践贡献：[对企业实践的贡献]
设计原则：[预期产出的可复用设计原则]
```

#### 1.4 具体示例：营销智能体系统的研究问题定义

**问题识别**：

当前企业营销决策面临三个核心挑战：
1. **数据表示碎片化**：客户数据、产品数据、内容数据分散在不同系统中，缺乏统一的表示框架
2. **决策缺乏因果验证**：营销决策主要基于相关性分析，无法确认"什么导致了什么"
3. **Agent系统缺乏治理**：营销Agent的自主性带来了安全、伦理和效率问题

**解决方案目标**：

设计一个"AI原生化营销智能体系统"，包含：
1. **统一数据表示层**：基于embedding和知识图谱的客户/产品/内容统一表示
2. **因果决策回路**：将因果推断嵌入Agent的决策流程，而非仅作为事后分析
3. **人机协作治理层**：基于NIST AI RMF的Agent治理框架

**预期设计原则**：
1. "统一表示+GraphRAG"如何提升营销知识检索的全局推理能力
2. "因果推断嵌入决策回路"如何提升营销决策的质量
3. "独立安全检查Agent"如何降低Agent系统的安全风险

#### 1.5 Phase 1交付物清单

- [ ] PRISMA文献综述报告（20-30篇核心文献，结构化表格）
- [ ] 研究问题定义书（DSR框架，1-2页）
- [ ] 研究空白分析（gap analysis，识别2-3个研究空白）
- [ ] 选择Capstone路径（研究型 vs 工程型）并说明理由

---

### Phase 2：数据表示与知识图谱

> **预计时间**：2-3周 | **核心交付物**：知识图谱设计文档 + embedding pipeline代码

#### 2.1 阶段目标

本阶段将Phase 1的研究问题转化为具体的数据表示方案：
1. 设计企业知识图谱--如何结构化表示营销领域的实体和关系
2. 构建embedding pipeline--如何将客户/产品/内容数据转化为向量表示
3. 设计GraphRAG方案--如何将知识图谱与RAG融合

#### 2.2 企业知识图谱设计

**知识图谱本体设计**：

```
营销领域本体设计：

实体类型（Nodes）：
├─ Customer（客户）
│  ├─ 属性：customer_id, demographics, lifecycle_stage, value_segment
│  └─ 关系：PURCHASED -> Product, INTERACTED_WITH -> Content, BELONGS_TO -> Segment
│
├─ Product（产品）
│  ├─ 属性：product_id, category, features, price, lifecycle_stage
│  └─ 关系：CATEGORIZED_AS -> Category, COMPETES_WITH -> Product, DEPICTED_IN -> Content
│
├─ Content（内容）
│  ├─ 属性：content_id, type, topic, channel, performance_metrics
│  └─ 关系：TARGETS -> Customer, PROMOTES -> Product, DERIVED_FROM -> Campaign
│
├─ Campaign（营销活动）
│  ├─ 属性：campaign_id, objective, budget, timeline, roi
│  └─ 关系：INCLUDES -> Content, TARGETS -> Segment, MEASURED_BY -> Metric
│
├─ Channel（渠道）
│  ├─ 属性：channel_id, type, reach, cost
│  └─ 关系：DISTRIBUTES -> Content, REACHES -> Customer
│
└─ Metric（指标）
   ├─ 属性：metric_id, type, value, timestamp
   └─ 关系：MEASURES -> Campaign/Product/Content
```

**知识图谱嵌入（KGE）选择**：

| 方法 | 原理 | 优势 | 适用场景 |
|------|------|------|---------|
| TransE | h + r ≈ t（头实体+关系≈尾实体） | 简单高效 | 一对一关系 |
| RotatE | 在复数空间中旋转 | 处理对称/反对称关系 | 复杂关系 |
| ComplEx | 复数嵌入 | 处理非对称关系 | 推荐场景 |
| GraphSAGE | 邻域聚合 | 归纳式学习（可处理新节点） | 动态图 |

**对于营销场景的建议**：使用GraphSAGE或GAT（图注意力网络），因为营销数据是动态的（新客户、新产品、新内容不断出现），归纳式学习更适合。

#### 2.3 Embedding Pipeline设计

```python
# === 营销数据Embedding Pipeline（架构示例）===

"""
Pipeline目标：将企业营销数据转化为统一的向量表示
输入：CRM数据、产品数据、内容数据、交互数据
输出：客户嵌入、产品嵌入、内容嵌入、交互图嵌入
"""

# Step 1: 数据预处理
class DataPreprocessor:
    """处理多源异构数据"""
    def process_crm_data(self, raw_crm):
        # 清洗、去重、标准化客户数据
        pass

    def process_product_data(self, raw_products):
        # 产品属性标准化、分类映射
        pass

    def process_content_data(self, raw_content):
        # 内容文本清洗、多模态处理
        pass

    def process_interaction_data(self, raw_interactions):
        # 客户-产品-内容交互日志处理
        pass

# Step 2: 特征工程与Embedding
class EmbeddingGenerator:
    """生成多维度嵌入"""
    def generate_customer_embedding(self, customer_data):
        """
        客户嵌入 = 人口统计特征 + 行为特征 + 偏好特征
        使用Two-Tower模型或对比学习
        """
        # 人口统计特征 -> MLP编码
        demo_emb = self.demo_encoder(customer_data["demographics"])
        # 行为特征 -> 序列编码（Transformer）
        behavior_emb = self.behavior_encoder(customer_data["interactions"])
        # 偏好特征 -> 偏好向量
        pref_emb = self.pref_encoder(customer_data["preferences"])
        # 融合
        customer_emb = self.fusion_layer(demo_emb, behavior_emb, pref_emb)
        return customer_emb

    def generate_product_embedding(self, product_data):
        """产品嵌入 = 属性特征 + 文本描述 + 图像特征"""
        attr_emb = self.attr_encoder(product_data["attributes"])
        text_emb = self.text_encoder(product_data["description"])
        image_emb = self.image_encoder(product_data["images"])
        product_emb = self.multimodal_fusion(attr_emb, text_emb, image_emb)
        return product_emb

    def generate_content_embedding(self, content_data):
        """内容嵌入 = 文本特征 + 多模态特征 + 性能特征"""
        text_emb = self.text_encoder(content_data["text"])
        multimodal_emb = self.multimodal_encoder(content_data["media"])
        perf_emb = self.perf_encoder(content_data["metrics"])
        content_emb = self.content_fusion(text_emb, multimodal_emb, perf_emb)
        return content_emb

# Step 3: 知识图谱构建
class KnowledgeGraphBuilder:
    """构建企业营销知识图谱"""
    def build_graph(self, entities, relations):
        """
        实体：客户、产品、内容、活动、渠道
        关系：购买、互动、推广、竞争、归属
        """
        graph = nx.MultiDiGraph()
        # 添加节点
        for entity_type, entity_list in entities.items():
            for entity in entity_list:
                graph.add_node(entity["id"], **entity)
        # 添加边
        for relation in relations:
            graph.add_edge(
                relation["source"], relation["target"],
                relation_type=relation["type"],
                weight=relation.get("weight", 1.0)
            )
        return graph

# Step 4: GraphRAG集成
class GraphRAGIntegrator:
    """将知识图谱与RAG融合"""
    def __init__(self, graph, embedding_store):
        self.graph = graph
        self.embedding_store = embedding_store

    def retrieve(self, query, search_mode="hybrid"):
        """
        混合检索：向量检索 + 图谱检索
        """
        if search_mode == "vector":
            # 传统向量检索
            return self.embedding_store.similarity_search(query)
        elif search_mode == "graph":
            # 图谱检索：找到相关实体及其邻居
            entities = self.extract_entities(query)
            return self.graph_traverse(entities)
        elif search_mode == "hybrid":
            # 混合检索：向量+图谱
            vector_results = self.embedding_store.similarity_search(query)
            entities = self.extract_entities(query)
            graph_results = self.graph_traverse(entities)
            return self.fuse_results(vector_results, graph_results)
```

#### 2.4 Phase 2交付物清单

- [ ] 知识图谱设计文档（本体定义、实体类型、关系类型）
- [ ] Embedding pipeline代码（可运行的Python代码或Jupyter Notebook）
- [ ] GraphRAG集成方案（检索策略设计）
- [ ] 数据质量评估报告（数据覆盖率、嵌入质量评估）

---

### Phase 3：Agentic系统架构设计

> **预计时间**：2-3周 | **核心交付物**：系统架构文档 + Agent工作流代码

#### 3.1 阶段目标

本阶段将Phase 2的数据表示层转化为完整的Agent系统架构：
1. 用LangGraph设计Agent编排架构
2. 设计人机协作治理框架
3. 实现Agent工作流原型

#### 3.2 系统架构设计

**三层架构**：

```
┌─────────────────────────────────────────────────────┐
│                 用户交互层                             │
│  ├─ 营销人员界面（自然语言交互）                        │
│  ├─ 管理层仪表盘（监控和审批）                         │
│  └─ API层（系统集成）                                │
├─────────────────────────────────────────────────────┤
│                 Agent编排层（LangGraph）               │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ 洞察Agent │  │ 创意Agent │  │ 投放Agent │          │
│  │          │  │          │  │          │          │
│  │ 分析市场  │->│ 生成内容  │->│ 优化投放  │          │
│  │ 识别机会  │  │ 品牌对齐  │  │ 预算分配  │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│        │              │              │               │
│        └──────────────┼──────────────┘               │
│                       ▼                              │
│              ┌──────────────┐                        │
│              │  协调Agent     │                        │
│              │  任务分配      │                        │
│              │  冲突解决      │                        │
│              │  质量控制      │                        │
│              └──────────────┘                        │
│                       │                              │
│                       ▼                              │
│              ┌──────────────┐                        │
│              │ 安全检查Agent  │                        │
│              │ 输入安全检查   │                        │
│              │ 输出安全审查   │                        │
│              │ 合规性验证     │                        │
│              └──────────────┘                        │
├─────────────────────────────────────────────────────┤
│                 数据与知识层                           │
│  ├─ 向量数据库（Pinecone/Weaviate）                   │
│  ├─ 知识图谱（Neo4j/NetworkX）                        │
│  ├─ GraphRAG引擎                                     │
│  ├─ 因果推断引擎（DoWhy）                              │
│  └─ 监控系统（Langfuse）                              │
└─────────────────────────────────────────────────────┘
```

#### 3.3 LangGraph Agent工作流设计

```python
# === 营销智能体系统LangGraph工作流（架构示例）===

from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional
from enum import Enum

# 定义Agent系统状态
class AgentState(TypedDict):
    # 用户请求
    user_request: str
    # 洞察结果
    market_insights: Optional[str]
    target_audience: Optional[dict]
    # 创意结果
    content_drafts: Optional[List[str]]
    selected_content: Optional[str]
    # 投放结果
    campaign_plan: Optional[dict]
    # 安全检查
    safety_approved: bool
    safety_issues: Optional[List[str]]
    # 人工审批
    human_approved: bool
    # 最终输出
    final_output: Optional[dict]
    # 日志
    execution_log: List[str]

# 定义节点（Agent）
def insight_agent(state: AgentState) -> AgentState:
    """洞察Agent：分析市场和用户，识别营销机会"""
    # 1. 用GraphRAG检索市场知识和客户洞察
    # 2. 分析目标受众特征
    # 3. 识别营销机会
    state["market_insights"] = "基于知识图谱分析的市场洞察..."
    state["target_audience"] = {"segment": "高价值客户", "size": 50000}
    state["execution_log"].append("洞察Agent完成分析")
    return state

def creative_agent(state: AgentState) -> AgentState:
    """创意Agent：基于洞察生成营销内容"""
    # 1. 基于洞察和品牌规范生成内容
    # 2. 生成多个变体
    # 3. 自评和筛选
    state["content_drafts"] = ["文案1...", "文案2...", "文案3..."]
    state["selected_content"] = state["content_drafts"][0]
    state["execution_log"].append("创意Agent完成内容生成")
    return state

def placement_agent(state: AgentState) -> AgentState:
    """投放Agent：设计投放策略和预算分配"""
    # 1. 分析渠道效果（因果推断）
    # 2. 优化预算分配
    # 3. 设计A/B测试方案
    state["campaign_plan"] = {
        "channels": ["email", "social", "search"],
        "budget": {"email": 30, "social": 50, "search": 20},
        "ab_test": {"variant_a": state["selected_content"], "variant_b": state["content_drafts"][1]}
    }
    state["execution_log"].append("投放Agent完成策略设计")
    return state

def safety_check_agent(state: AgentState) -> AgentState:
    """安全检查Agent：独立审查所有输出"""
    issues = []
    # 检查内容安全性
    if "虚假" in state.get("selected_content", ""):
        issues.append("内容可能包含虚假信息")
    # 检查合规性
    if not check_brand_guidelines(state.get("selected_content", "")):
        issues.append("内容不符合品牌规范")
    # 检查数据隐私
    if contains_pii(state.get("campaign_plan", {})):
        issues.append("投放计划包含敏感用户信息")

    state["safety_approved"] = len(issues) == 0
    state["safety_issues"] = issues
    state["execution_log"].append(f"安全检查Agent完成，{'通过' if state['safety_approved'] else '发现问题'}")
    return state

def human_review(state: AgentState) -> AgentState:
    """人工审核节点（Human-in-the-loop）"""
    # 在实际系统中，这里会暂停等待人工审批
    # LangGraph原生支持checkpointing和human-in-the-loop
    state["human_approved"] = True  # 模拟人工批准
    state["execution_log"].append("人工审核完成")
    return state

def coordinator_agent(state: AgentState) -> str:
    """协调Agent：决定下一步执行哪个Agent"""
    if not state.get("market_insights"):
        return "insight"
    elif not state.get("content_drafts"):
        return "creative"
    elif not state.get("campaign_plan"):
        return "placement"
    elif not state.get("safety_approved"):
        return "safety"
    elif not state.get("human_approved"):
        return "human"
    else:
        return "end"

# 构建LangGraph工作流
def build_marketing_agent_graph():
    graph = StateGraph(AgentState)

    # 添加节点
    graph.add_node("insight", insight_agent)
    graph.add_node("creative", creative_agent)
    graph.add_node("placement", placement_agent)
    graph.add_node("safety", safety_check_agent)
    graph.add_node("human", human_review)

    # 设置入口
    graph.set_entry_point("insight")

    # 添加条件边（协调Agent逻辑）
    graph.add_conditional_edges("insight", coordinator_agent,
        {"creative": "creative", "safety": "safety"})
    graph.add_conditional_edges("creative", coordinator_agent,
        {"placement": "placement", "safety": "safety"})
    graph.add_conditional_edges("placement", coordinator_agent,
        {"safety": "safety"})
    graph.add_conditional_edges("safety", coordinator_agent,
        {"insight": "insight", "creative": "creative",  # 如果不安全，重新生成
         "human": "human", "end": END})
    graph.add_conditional_edges("human", coordinator_agent,
        {"insight": "insight",  # 如果人工拒绝，重新开始
         "end": END})

    return graph.compile()
```

#### 3.4 人机协作治理框架

**人机分工矩阵**：

| 任务类型 | 人类角色 | Agent角色 | 决策权 |
|---------|---------|----------|--------|
| **战略决策** | 制定营销战略、设定目标 | 提供数据分析和建议 | 人类 |
| **创意生成** | 审核和选择最终内容 | 生成多个创意变体 | 混合（Agent生成，人类审批） |
| **投放优化** | 设定预算上限和风险参数 | 自动优化投放参数 | Agent（在人类设定的边界内） |
| **客户互动** | 处理高价值客户和复杂问题 | 自动回复常规问题 | 混合（Agent优先，升级人类） |
| **安全审查** | 制定安全政策和品牌规范 | 执行安全检查和内容过滤 | 人类（政策），Agent（执行） |
| **效果评估** | 解读结果和制定下一步策略 | 自动收集和分析数据 | 混合（Agent分析，人类决策） |

**审批流程设计**：

```
Agent输出 -> 安全检查Agent -> 自动审批阈值检查
                           ├─ 低风险（自动通过）-> 执行
                           ├─ 中风险（需人工审核）-> 人工审批 -> 执行/退回
                           └─ 高风险（必须人工审核）-> 人工审批 -> 执行/退回
```

#### 3.5 Phase 3交付物清单

- [ ] 系统架构文档（三层架构图+组件说明，1000-1500字）
- [ ] LangGraph Agent工作流代码（可运行的Python代码）
- [ ] 人机协作治理框架文档（分工矩阵+审批流程）
- [ ] Agent安全检查方案（基于E9的安全框架）

---

### Phase 4：因果实验设计与验证

> **预计时间**：2-3周 | **核心交付物**：实验设计方案 + 数据收集工具

#### 4.1 阶段目标

本阶段用科学方法验证Agent系统的效果：
1. 用混合方法设计评估方案--定量+定性
2. 设计A/B测试+因果推断+用户访谈的整合方案
3. 建立数据收集工具和流程

#### 4.2 混合方法评估设计

**解释性序列设计（Explanatory Sequential Design）**：

```
阶段1: 定量评估（先）
  ├─ A/B测试：Agent系统 vs 传统系统
  ├─ 因果推断：用DoWhy分析因果效应
  └─ 产出：量化指标和统计结论

        ↓ （解释"为什么"）

阶段2: 定性评估（后）
  ├─ 用户访谈：理解定量结果背后的原因
  ├─ 案例研究：深入分析典型用例
  └─ 产出：对定量结果的解释和深度理解

        ↓ （整合）

阶段3: 综合结论
  └─ 定量+定性的综合发现和设计原则
```

#### 4.3 A/B测试设计

**实验设计**：

| 要素 | 设计 |
|------|------|
| **实验假设** | 使用AI营销Agent系统的团队，其营销campaign的转化率比使用传统工具的团队高出至少15% |
| **实验单位** | 营销campaign（每个campaign为一个实验单位） |
| **对照组** | 使用传统营销工具和流程 |
| **实验组** | 使用AI营销Agent系统 |
| **样本量** | 每组至少30个campaign（基于统计功效计算） |
| **实验时长** | 4-8周（覆盖完整的campaign周期） |
| **主要指标** | 转化率（conversion rate） |
| **次要指标** | 内容产出效率、投放ROI、客户满意度、决策时间 |
| **混杂因素控制** | 行业、产品类型、预算规模、季节性 |

**统计功效计算**：

```python
# === A/B测试样本量计算 ===
from statsmodels.stats.power import tt_ind_solve_power

# 参数设定
effect_size = 0.5  # 中等效应量（Cohen's d）
alpha = 0.05       # 显著性水平
power = 0.8        # 统计功效（80%）

# 计算每组所需样本量
sample_size = tt_ind_solve_power(
    effect_size=effect_size,
    alpha=alpha,
    power=power,
    ratio=1.0  # 对照组和实验组比例1:1
)
print(f"每组所需样本量: {sample_size:.0f}")
# 输出：每组约64个样本
```

**如果样本量不足的替代方案**：

如果无法达到足够的样本量（这在企业实验中很常见），可以使用准实验方法：
- **Difference-in-Differences（DiD）**：比较实验前后的变化差异
- **Propensity Score Matching**：匹配相似实验单位和对照单位
- **合成对照法**：用多个对照单位合成一个"虚拟对照"

#### 4.4 因果推断分析

用DoWhy库分析Agent系统对营销效果的因果效应：

```python
# === 因果推断分析示例 ===

import dowhy
from dowhy import CausalModel
import pandas as pd

# 1. 数据准备
data = pd.DataFrame({
    'used_agent': [1, 0, 1, 0, ...],           # 是否使用Agent系统
    'conversion_rate': [0.12, 0.08, 0.15, ...], # 转化率
    'budget': [50000, 45000, ...],              # 预算（混杂因素）
    'industry': [1, 2, 1, ...],                 # 行业（混杂因素）
    'product_type': [1, 1, 2, ...],             # 产品类型（混杂因素）
    'seasonality': [0.8, 1.2, ...]              # 季节性因子（混杂因素）
})

# 2. 因果图建模
model = CausalModel(
    data=data,
    treatment='used_agent',
    outcome='conversion_rate',
    common_causes=['budget', 'industry', 'product_type', 'seasonality']
)

# 3. 识别因果效应
identified_estimand = model.identify_effect()
print(f"识别策略: {identified_estimand}")

# 4. 估计因果效应
estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.propensity_score_matching"
)
print(f"平均因果效应（ATE）: {estimate.value}")
print(f"解释: 使用Agent系统使转化率{'提升' if estimate.value > 0 else '降低'}"
      f" {abs(estimate.value)*100:.1f}%")

# 5. 稳健性检验（反驳）
refutation = model.refute_estimate(
    identified_estimand,
    estimate,
    "placebo_treatment_refuter"
)
print(f"安慰剂检验: {refutation}")

# 如果安慰剂检验的效应接近0，说明原始估计是可靠的
```

#### 4.5 定性评估设计

**用户访谈方案**：

| 要素 | 设计 |
|------|------|
| **访谈对象** | 5-8名使用Agent系统的营销人员 |
| **访谈时长** | 45-60分钟/人 |
| **访谈方式** | 半结构化访谈 |
| **核心问题** | 见下方访谈提纲 |

**访谈提纲**：

```
1. 使用体验
   - 你在什么场景下使用了Agent系统？
   - 使用过程中最让你满意的是什么？最不满意的是什么？

2. 决策影响
   - Agent系统的建议对你的决策有什么影响？
   - 你是完全信任Agent的建议，还是会自己判断？
   - 有没有Agent建议与你直觉相反的情况？你怎么处理的？

3. 效果感知
   - 你觉得使用Agent系统后，工作效率有变化吗？
   - 营销内容的质量有变化吗？
   - 转化效果有变化吗？

4. 信任与安全
   - 你信任Agent系统的输出吗？你的信任边界在哪里？
   - 你有没有遇到过Agent输出不安全或不合适的内容？
   - 你对人机协作的审批流程有什么看法？

5. 改进建议
   - 如果可以改进Agent系统的一个方面，你会改进什么？
   - 你认为Agent系统未来应该增加什么功能？
```

**案例分析方案**：

选择2-3个典型营销campaign，做深入案例分析：
1. **成功案例**：Agent系统显著提升了效果的campaign
2. **失败案例**：Agent系统效果不佳的campaign
3. **边界案例**：Agent系统表现有争议的campaign

每个案例分析：
- 背景：campaign的目标、受众、预算
- 过程：Agent系统如何参与决策
- 结果：量化效果和质性反馈
- 分析：成功/失败的原因
- 启示：对系统改进的启示

#### 4.6 Phase 4交付物清单

- [ ] 实验设计方案（A/B测试+因果推断+定性评估的整合方案）
- [ ] 数据收集工具（问卷、访谈提纲、数据收集脚本）
- [ ] DoWhy因果分析代码（Jupyter Notebook）
- [ ] 定量分析结果（统计报告）
- [ ] 定性分析结果（访谈摘要+案例分析）

---

### Phase 5：商业模式与价值评估

> **预计时间**：1-2周 | **核心交付物**：商业模式画布 + ROI分析报告

#### 5.1 阶段目标

本阶段从商业视角评估Agent系统的价值：
1. 设计商业模式画布--Agent系统如何创造、传递、捕获价值
2. 建立ROI评估框架--量化和非量化的价值评估
3. 用行动研究视角反思--AI系统部署如何改变了组织决策流程

#### 5.2 商业模式画布设计

```
┌──────────────────────────────────────────────────────────────┐
│          AI营销智能体系统 商业模式画布                          │
├──────────────┬───────────────────┬───────────────────────────┤
│              │                   │                           │
│  关键合作伙伴   │    关键活动          │     价值主张               │
│  ├─ AI模型提供商│   ├─ Agent开发维护   │  对企业：                  │
│  ├─ 数据供应商  │   ├─ 数据治理        │  ├─ 营销效率提升40-60%     │
│  ├─ 云服务商    │   ├─ 持续优化        │  ├─ 转化率提升15-30%      │
│  └─ 行业咨询    │   └─ 安全合规        │  ├─ 决策周期缩短50%       │
│              ├───────────────────┤  └─ 人力成本降低30%        │
│  关键资源      │    成本结构          │  对营销人员：               │
│  ├─ AI模型     │   ├─ 模型推理成本    │  ├─ 从重复劳动解放         │
│  ├─ 营销数据    │   ├─ 基础设施成本    │  ├─ 聚焦策略和创意         │
│  ├─ 知识图谱    │   ├─ 人才成本       │  └─ 数据驱动决策           │
│  └─ 品牌资产    │   └─ 合规成本       │                           │
│              │                   │  客户关系                   │
│              ├───────────────────┤  ├─ 自助+专家支持            │
│              │    收入来源          │  ├─ 持续培训               │
│              │   ├─ 平台订阅费     │  └─ 社区生态               │
│              │   ├─ 按效果分成     │                           │
│              │   ├─ 定制开发费     │  渠道                      │
│              │   └─ 数据服务费     │  ├─ 直销（大客户）          │
│              │                   │  ├─ 自助（中小企业）        │
│              │                   │  └─ 合作伙伴               │
│              │                   │  客户细分                   │
│              │                   │  ├─ 中大型企业营销部门      │
│              │                   │  ├─ 营销代理商             │
│              │                   │  └─ DTC品牌               │
└──────────────┴───────────────────┴───────────────────────────┘
```

#### 5.3 ROI评估框架

**多维度ROI评估**：

| 维度 | 指标 | 评估方法 | 预期值 |
|------|------|---------|--------|
| **效率提升** | 内容产出时间 | 使用前后对比 | 降低50-70% |
| **效果提升** | 转化率 | A/B测试 | 提升15-30% |
| **成本节约** | 人力成本 | 财务核算 | 降低20-40% |
| **决策质量** | 决策准确率 | 专家评估 | 提升20-30% |
| **风险降低** | 安全事件数 | 事件记录 | 降低80% |
| **创新加速** | 新campaign上线速度 | 时间追踪 | 加速2-3倍 |

**ROI计算模型**：

```
ROI = (总收益 - 总成本) / 总成本 × 100%

总成本 = 
  开发成本（一次性）+ 部署成本（一次性）+
  运营成本（年度）= 模型推理 + 基础设施 + 人员 + 合规

总收益 =
  效率提升收益（节约的人力时间 × 时薪）+
  效果提升收益（增加的转化 × 客单价）+
  风险规避收益（避免的安全事件损失）+
  创新加速收益（提前上线带来的增量收入）

示例计算：
开发成本：$50,000（一次性）
部署成本：$20,000（一次性）
年度运营成本：$80,000

年度收益：
  效率提升：$120,000（2人×$60,000/年×50%时间节约）
  效果提升：$200,000（转化率提升20%×增量收入$1M）
  风险规避：$30,000（估计值）
  创新加速：$50,000

年度总收益：$400,000
年度ROI = ($400,000 - $80,000) / ($50,000 + $20,000 + $80,000) = 213%
投资回收期 ≈ 4个月
```

#### 5.4 行动研究反思

用行动研究的"参与-行动-反思"螺旋，记录Agent系统部署如何改变组织决策流程：

**反思框架**：

```
第1轮：诊断
  ├─ 部署前：营销决策流程是什么样？
  ├─ 痛点：决策慢、数据散、效果不可测
  └─ 干预计划：部署Agent系统

第2轮：行动
  ├─ 部署Agent系统
  ├─ 观察变化：决策流程如何改变？
  └─ 收集反馈：营销人员的体验如何？

第3轮：反思
  ├─ 什么改变了？什么没改变？
  ├─ 意外发现：Agent系统不仅改变了效率，还改变了决策权分布
  └─ 调整计划：优化人机协作流程

第4轮：再行动
  ├─ 基于反思调整系统
  └─ 持续循环...
```

**组织变革的关键观察点**：

1. **决策权变化**：谁拥有营销决策的最终决定权？人类？Agent？混合？
2. **技能需求变化**：营销人员需要什么新技能？哪些旧技能被淘汰？
3. **组织结构变化**：是否需要新的角色（如"Agent运营师"）？
4. **文化变化**：组织对AI的信任度如何变化？
5. **流程变化**：营销流程的哪些环节被重构了？

#### 5.5 Phase 5交付物清单

- [ ] 商业模式画布（完整填写）
- [ ] ROI分析报告（含计算模型和数据支撑）
- [ ] 行动研究反思报告（组织变革观察）
- [ ] 价值评估综合报告

---

### 战略画布工具应用：跨Phase的战略思维工具集

> **交叉引用**：战略画布工具的完整工具集详见选修E13《战略思维画布工具集》

战略画布工具不是选修课的专利--它们是Capstone全流程的思维基础设施。从选题到评估，从研究记录到文献综述，战略画布工具为博士论文提供了结构化的思考框架，确保研究既有战略高度，又有执行精度。以下四个工具分别对应Capstone的四个关键环节。

#### 1. BLM四类差距诊断用于论文选题

Business Leadership Model（BLM）的四类差距诊断框架为博士论文选题提供了系统化的切入点。在Phase 1（问题定义）阶段，学生需要回答"我的研究解决什么问题"，而BLM的差距分类恰恰提供了答案的四种路径：

**业绩差距（Performance Gap）**：现有AI系统的效果不达预期。例如，当前营销Agent的转化率仅为8%，而行业标杆为15%--这种差距指向**优化方向**的研究选题，研究重点是如何提升现有系统的性能。这类选题实践价值高，但学术创新性相对有限。

**机会差距（Opportunity Gap）**：新的AI能力尚未被利用。例如，多模态大模型已具备图像理解能力，但营销领域尚未将其用于广告创意自动审核--这种差距指向**创新方向**的研究选题，研究重点是探索新技术的应用可能。这类选题有较好的新颖性。

**认知差距（Cognitive Gap）**：行业现有的假设可能存在错误。例如，业界普遍假设"个性化推荐能提升用户满意度"，但如果在B2B场景中这个假设不成立呢？--这种差距指向**验证方向**的研究选题，研究重点是挑战和修正现有认知。

**合规差距（Compliance Gap）**：AI应用存在合规风险但尚无系统性解决方案。例如，营销Agent自动生成的内容可能违反广告法或数据隐私法规--这种差距指向**治理方向**的研究选题，研究重点是构建合规治理框架。

**选题建议**：博士论文的价值在于挑战现有认知而非仅做优化。因此，**建议学生优先选择认知差距型选题**。业绩差距型选题容易变成工程项目而非学术贡献；认知差距型选题天然具备"颠覆性假设"的学术张力，更容易提炼出有价值的设计原则。例如，本Capstone的论文方向"从表示工程到因果决策的闭环架构"本质上是一个认知差距选题--它挑战了"营销决策可以仅基于相关性"这一行业默认假设。

#### 2. 北极星指标用于论文成果衡量

北极星指标（North Star Metric）是产品管理中用于衡量核心价值的单一指标。在Capstone中，选择一个北极星指标可以为论文评估提供清晰的价值锚点。

**选择原则**：北极星指标应满足三个条件--（1）反映论文核心贡献而非次要效果；（2）可量化测量；（3）与评估标准中的"学术贡献"维度直接对应。

**示例**：如果论文方向是Agent营销系统，可能的北极星指标包括：
- "决策准确率提升幅度"（反映因果决策回路的贡献）
- "营销知识检索的全局推理得分"（反映GraphRAG的贡献）
- "Agent安全事件降低率"（反映治理框架的贡献）

本Capstone的推荐北极星指标是**"决策准确率提升幅度"**--它直接反映了"从相关性决策到因果决策"这一核心研究贡献。在Phase 4（因果实验设计）中，这个指标通过A/B测试和DoWhy因果推断来量化；在Phase 5（价值评估）中，它转化为ROI计算中的"决策质量"维度。

**与论文评估标准的关系**：北极星指标不是评分标准本身，而是研究的"指南针"。在论文的Discussion部分，应明确报告北极星指标的测量结果和统计显著性，并诚实地讨论其局限性。这直接对应评估量表中"评估"维度（15分）的"评估严谨，结果可信"标准。

#### 3. 可审计四件套用于研究记录

可审计四件套为博士研究提供了过程透明性和学术诚信保障。在Capstone的全过程中，每一项研究决策都应有可追溯的记录。

**判定依据（Evidence Base）**：每个研究假设的数据来源和分析方法必须明确记录。例如，"GraphRAG提升全局推理能力"这一假设的判定依据包括：知识图谱覆盖率数据、检索召回率测试结果、以及与传统向量检索的对比实验数据。在Phase 1的研究问题定义书中，每个假设都应附注其判定依据。

**置信区间（Confidence Interval）**：实验结果必须报告统计显著性和效应量。Phase 4的A/B测试结果应包含p值、95%置信区间和Cohen's d效应量。如果置信区间包含0，必须如实报告"无法排除零效应"，而非选择性报告有利结果。

**停手线（Stop Condition）**：预设的放弃或切换条件。博士研究容易陷入"沉没成本"陷阱--某个方向探索了3个月没有进展，但因为已经投入了大量时间而不愿放弃。建议在Phase 1就写下停手线："如果方向A在3个月内未取得[具体指标]的进展，则切换到备选方向B"。这确保研究资源的有效分配。

**复盘口径（Pre-registered Hypothesis）**：事前写下的可证伪假设。在收集数据之前，明确写下"我预期X会导致Y，如果Y的变化不超过Z，则假设被证伪"。这避免了事后"p-hacking"--即先看数据再编假设的学术不端行为。

**与模块R的衔接**：可审计四件套与模块R研究方法论中的IMRaD格式和DSR框架深度衔接。判定依据对应IMRaD的Methods部分；置信区间对应Results部分；停手线对应研究的时间规划（四、时间规划）；复盘口径对应Discussion部分对假设的检验和修正。

#### 4. 七看洞察用于文献综述和市场分析

七看洞察框架（看环境/看行业/看客户/看竞争/看自己/AI/规则）为Phase 1的文献综述和市场分析提供了系统化的分析维度，确保研究定位的全面性。

**看环境（Macro Environment）**：AI原生企业的宏观趋势--监管趋严（GDPR、AI Act）、算力民主化（开源模型崛起）、Agent经济兴起。这些趋势为论文的Introduction提供了大背景。

**看行业（Industry）**：企业营销领域的现状和痛点--数据碎片化、决策依赖经验、内容生产瓶颈。Phase 1的PRISMA文献综述应覆盖这些行业研究。

**看客户（Customer）**：企业营销决策者的真实需求--他们需要的不是"更快的工具"，而是"更可信的决策"。这帮助定义研究问题的实践相关性。

**看竞争（Competition）**：学术界和工业界的现有方案--Salesforce Einstein、HubSpot AI、Adobe Sensei等。文献综述的gap analysis应明确你的研究与这些方案的差异。

**看自己（Self）**：aha.gare的背景优势--售前解决方案产品经理，有AI+企业营销的实战经验，有技术实现能力。选题应发挥这一优势。

**看AI（Technology）**：2026年AI技术前沿--GraphRAG、LangGraph、因果LLM、多模态推理。文献综述应覆盖这些技术的前沿论文。

**看规则（Regulation）**：AI合规框架--NIST AI RMF、EU AI Act、中国生成式AI管理办法。这些规则约束了Agent系统的设计边界。

**在Capstone中的应用**：七看洞察应在Phase 1的研究问题定义书中以表格形式呈现，确保研究问题既有学术深度（看行业、看AI、看竞争），又有实践根基（看客户、看自己），还有合规意识（看环境、看规则）。这与PRISMA文献综述互补--PRISMA是"学术文献"的系统综述，七看是"全景洞察"的结构化扫描。

> 🔗 **延伸实践**：七看洞察框架的完整工具集详见选修E13 Day 1。

---

### Phase 6：系统实现与论文撰写

> **预计时间**：2-3周 | **核心交付物**：IMRaD论文草稿（3000-5000字）+ 发表路线图

#### 6.1 阶段目标

本阶段是Capstone的最终交付：
1. 完成系统实现和集成测试
2. 撰写符合IMRaD格式的论文草稿
3. 制定学术发表路线图

#### 6.2 IMRaD论文撰写

**论文结构**：

| 部分 | 字数 | 核心内容 | 写作要点 |
|------|:----:|---------|---------|
| **Title** | - | 简洁、信息量大 | 包含关键概念：Agent、营销、因果决策 |
| **Abstract** | 150-250 | 全文摘要 | 问题、方法、结果、贡献各1-2句 |
| **Introduction** | 800-1000 | 背景、问题、贡献 | 从大到小：领域背景->具体问题->本文贡献 |
| **Related Work** | 600-800 | 文献综述 | 基于Phase 1的PRISMA综述 |
| **Methods** | 1000-1200 | 研究方法 | DSR框架、系统设计、评估方法 |
| **Results** | 800-1000 | 研究发现 | 定量+定性结果，图表呈现 |
| **Discussion** | 600-800 | 讨论、局限、未来 | 诚实的局限性比虚假的完美更有价值 |
| **Conclusion** | 200-300 | 结论 | 核心发现和贡献 |
| **References** | - | 参考文献 | 20-30篇核心文献 |

**论文大纲模板**：

```markdown
# Title: AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构

## Abstract
[150-250字摘要]
背景：企业营销决策面临数据碎片化、因果验证缺失和Agent治理不足三大挑战。
方法：本文基于设计科学研究（DSR）框架，设计并实现了一个AI原生化营销智能体系统...
结果：系统在真实企业场景中验证，转化率提升X%，决策效率提升Y%...
贡献：提出了三条可复用的设计原则...

## 1. Introduction
### 1.1 研究背景
- AI原生企业的概念和趋势
- 营销决策的三大挑战

### 1.2 研究问题
- RQ1: 如何构建企业营销数据的统一表示？
- RQ2: 如何将因果推断嵌入Agent决策回路？
- RQ3: 如何设计Agent系统的治理框架？

### 1.3 研究贡献
- 设计了统一数据表示框架（知识图谱+GraphRAG）
- 提出了因果决策回路架构
- 设计了人机协作治理框架
- 通过实证验证产出了三条设计原则

## 2. Related Work
### 2.1 AI营销Agent架构
### 2.2 表示工程与知识图谱
### 2.3 因果推断在营销中的应用
### 2.4 AI安全与治理

## 3. Methods
### 3.1 DSR框架
### 3.2 系统设计
#### 3.2.1 数据表示层
#### 3.2.2 Agent编排层
#### 3.2.3 治理层
### 3.3 评估方法
#### 3.3.1 定量评估（A/B测试+因果推断）
#### 3.3.2 定性评估（访谈+案例分析）

## 4. Results
### 4.1 系统实现
### 4.2 定量结果
### 4.3 定性结果
### 4.4 设计原则

## 5. Discussion
### 5.1 研究发现的理论意义
### 5.2 实践启示
### 5.3 局限性
### 5.4 未来方向

## 6. Conclusion

## References
```

**写作建议**：

1. **Introduction的漏斗结构**：从大领域（AI原生企业）逐步聚焦到具体问题（营销Agent的因果决策），最后明确本文贡献
2. **Methods的可复现性**：别人读完Methods应该能复现你的研究。包括技术选型、参数设置、数据来源
3. **Results的数据说话**：用图表呈现核心结果，文字描述趋势和关键数字，不堆砌原始数据
4. **Discussion的诚实性**：明确说明研究的局限性。局限性不是弱点，是学术严谨性的体现
5. **Abstract的精炼性**：Abstract是论文的"广告"，要在250字内让读者知道你做了什么、发现了什么、贡献了什么

#### 6.3 学术发表路线图

**目标期刊/会议**：

| 级别 | 期刊/会议 | 影响因子/排名 | 投稿难度 | 适合度 | 预计审稿周期 |
|------|---------|-------------|:-------:|:------:|:-----------:|
| **顶级** | MIS Quarterly | IF~8.0 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 6-12月 |
| **顶级** | Information Systems Research | IF~5.0 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 6-12月 |
| **优秀** | Journal of Management Information Systems | IF~4.0 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 4-8月 |
| **优秀** | Decision Support Systems | IF~7.0 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 3-6月 |
| **良好** | International Journal of Information Management | IF~8.0 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 3-6月 |
| **良好** | Computers in Human Behavior | IF~9.0 | ⭐⭐⭐⭐ | ⭐⭐⭐ | 3-6月 |
| **会议** | ICIS（信息系统国际会议） | AIS Top 1 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 6月（固定截稿） |
| **会议** | AMCIS（美洲信息系统会议） | AIS Top 2 | ⭐⭐⭐ | ⭐⭐⭐⭐ | 6月（固定截稿） |
| **会议** | HICSS（夏威夷系统科学国际会议） | AIS Top 2 | ⭐⭐⭐ | ⭐⭐⭐⭐ | 6月（固定截稿） |
| **前沿** | arXiv预印本 | - | ⭐⭐ | ⭐⭐⭐⭐⭐ | 即时 |

**发表策略建议**：

```
Step 1: arXiv预印本（立即）
  └─ 将论文草稿上传arXiv，建立优先权
  └─ 获取社区反馈，改进论文

Step 2: 投稿会议（3-6月内）
  ├─ 首选：ICIS（如果是信息系统视角）
  └─ 备选：HICSS或AMCIS（如果时间紧迫）

Step 3: 投稿期刊（会议后）
  ├─ 首选：Decision Support Systems（最匹配本研究的跨学科性质）
  └─ 备选：International Journal of Information Management

Step 4: 持续迭代
  └─ 根据审稿意见修改，可能需要2-3轮
```

**投稿时间线**：

| 时间 | 行动 |
|------|------|
| Capstone完成 | arXiv预印本上传 |
| Capstone后1月 | 投稿ICIS或HICSS |
| Capstone后3月 | 根据反馈修改，投稿期刊 |
| Capstone后6月 | 第一轮审稿结果 |
| Capstone后9-12月 | 修改和再投 |
| Capstone后12-18月 | 最终接收（乐观估计） |

#### 6.4 Phase 6交付物清单

**研究型Capstone最终交付物**：
- [ ] IMRaD论文草稿（3000-5000字）
- [ ] 系统原型代码（可运行，GitHub仓库）
- [ ] 系统文献综述报告（PRISMA标准，20-30篇）
- [ ] 研究伦理审查自查清单
- [ ] 学术发表路线图
- [ ] 英文Abstract和Title

**工程型Capstone最终交付物**：
- [ ] 可运行的Agent系统原型
- [ ] 系统架构文档（1000字以上）
- [ ] Demo视频/截图
- [ ] 一页论文大纲（IMRaD格式）
- [ ] 技术博客或README（英文版）
- [ ] 用户手册

---

## 三、评估标准

### 3.1 研究型Capstone评分量表

| 维度 | 满分 | 评分标准 | 优秀(90-100) | 良好(70-89) | 合格(60-69) | 不合格(<60) |
|------|:----:|---------|-------------|------------|------------|------------|
| **研究问题** | 15 | 问题的清晰性、重要性和创新性 | 问题清晰、重要、有创新 | 问题清晰、较重要 | 问题基本清晰 | 问题模糊或不重要 |
| **文献综述** | 15 | PRISMA标准、覆盖面、空白识别 | 30+篇核心文献，空白识别精准 | 20+篇，空白较清晰 | 15+篇，有空白 | 文献不足，无空白 |
| **方法论** | 20 | DSR框架、混合方法、严谨性 | 方法严谨，可复现 | 方法较严谨 | 方法基本合理 | 方法有缺陷 |
| **系统设计** | 15 | 架构创新性、完整性 | 架构创新且完整 | 架构完整 | 架构基本完整 | 架构不完整 |
| **评估** | 15 | 定量+定性、统计严谨性 | 评估严谨，结果可信 | 评估较严谨 | 评估基本完成 | 评估不充分 |
| **论文写作** | 10 | IMRaD格式、学术规范 | 写作规范，表达清晰 | 写作较规范 | 写作基本规范 | 写作不规范 |
| **学术贡献** | 10 | 设计原则、理论/实践贡献 | 贡献明确且有价值 | 贡献较明确 | 有一定贡献 | 贡献不明确 |
| **总计** | **100** | | | | | |

### 3.2 工程型Capstone评分量表

| 维度 | 满分 | 评分标准 | 优秀(90-100) | 良好(70-89) | 合格(60-69) | 不合格(<60) |
|------|:----:|---------|-------------|------------|------------|------------|
| **系统完成度** | 25 | 功能完整性、可运行性 | 功能完整，运行稳定 | 功能较完整 | 基本可运行 | 无法运行 |
| **架构设计** | 20 | 架构合理性、可扩展性 | 架构优秀，可扩展 | 架构合理 | 架构基本合理 | 架构有问题 |
| **技术深度** | 20 | 技术选型、实现难度 | 技术先进，实现深入 | 技术较先进 | 技术基本到位 | 技术浅显 |
| **工程质量** | 15 | 代码质量、文档完整性 | 代码优秀，文档完整 | 代码良好 | 代码基本可读 | 代码质量差 |
| **实践价值** | 10 | 业务价值、可推广性 | 价值高，可推广 | 价值较高 | 有一定价值 | 价值不明 |
| **文档与展示** | 10 | 文档和Demo质量 | 文档优秀，Demo清晰 | 文档良好 | 文档基本完整 | 文档不完整 |
| **总计** | **100** | | | | | |

---

## 四、时间规划

### 4.1 12周紧凑节奏

适合全职投入或有充分时间的学习者。

| 周 | 阶段 | 核心任务 | 交付物 |
|:--:|------|---------|--------|
| 1 | Phase 1 | PRISMA文献检索+筛选 | 文献清单 |
| 2 | Phase 1 | 文献综述+研究问题定义 | 文献综述报告+问题定义书 |
| 3 | Phase 2 | 知识图谱设计+embedding pipeline | 设计文档+代码 |
| 4 | Phase 2 | GraphRAG集成+数据质量评估 | 集成方案+评估报告 |
| 5 | Phase 3 | LangGraph架构设计+Agent工作流 | 架构文档+代码 |
| 6 | Phase 3 | 人机协作治理+安全检查 | 治理框架+安全方案 |
| 7 | Phase 4 | A/B测试设计+数据收集 | 实验方案+数据 |
| 8 | Phase 4 | 因果推断分析+用户访谈 | 分析结果+访谈摘要 |
| 9 | Phase 5 | 商业模式画布+ROI分析 | 商业模式+ROI报告 |
| 10 | Phase 6 | 系统集成测试+论文初稿 | 系统原型+论文初稿 |
| 11 | Phase 6 | 论文修改+英文Abstract | 论文终稿 |
| 12 | Phase 6 | 答辩准备+arXiv上传 | 答辩PPT+预印本 |

### 4.2 24周标准节奏

适合在职学习的学习者，每周投入8-10小时。

| 周 | 阶段 | 核心任务 | 每周投入 |
|:--:|------|---------|:-------:|
| 1-3 | Phase 1 | PRISMA文献综述+研究问题定义 | 8-10h/周 |
| 4-7 | Phase 2 | 知识图谱+embedding+GraphRAG | 8-10h/周 |
| 8-11 | Phase 3 | Agent架构+治理框架+安全方案 | 8-10h/周 |
| 12-15 | Phase 4 | 实验设计+数据收集+因果分析+访谈 | 8-10h/周 |
| 16-18 | Phase 5 | 商业模式+ROI+行动研究反思 | 8-10h/周 |
| 19-22 | Phase 6 | 系统集成+论文撰写+修改 | 8-10h/周 |
| 23-24 | Phase 6 | 答辩准备+发表 | 8-10h/周 |

### 4.3 进度管理建议

| 建议 | 描述 |
|------|------|
| **每周复盘** | 每周末花30分钟回顾本周进度，调整下周计划 |
| **里程碑检查** | 每个Phase结束时对照交付物清单检查 |
| **早期反馈** | Phase 1完成后就找导师/同行获取反馈，不要等到最后 |
| **并行推进** | 某些任务可以并行（如Phase 4的访谈可以和Phase 5的商业分析同步） |
| **留缓冲时间** | 总是预留20%的缓冲时间应对意外 |

---

## 五、常见问题与陷阱

### 陷阱1：选题过大

**问题**：试图解决"所有企业营销AI的问题"，导致每个方面都浅尝辄止。

**解决方案**：聚焦一个具体的研究问题。例如，不是"AI营销Agent系统"（太大），而是"GraphRAG如何提升营销知识库的全局推理能力"（聚焦）。

### 陷阱2：文献综述变成"读书报告"

**问题**：文献综述只是罗列论文摘要，没有识别研究空白和定位自己的研究。

**解决方案**：每篇文献都要总结：研究问题、方法、发现、局限。最后必须有gap analysis，明确你的研究填补了什么空白。

### 陷阱3：系统设计没有设计原则

**问题**：做出了一个系统但没有提炼出可复用的设计原则，变成了"工程项目"而非"研究贡献"。

**解决方案**：在系统设计和评估过程中，不断问自己："从这个系统中，其他研究者/实践者可以学到什么通用原则？"设计原则是DSR研究的核心贡献。

### 陷阱4：评估方法单一

**问题**：只用定量指标或只用定性访谈，缺乏混合方法的严谨性。

**解决方案**：采用解释性序列设计--先做定量A/B测试，再用定性访谈解释"为什么"。两者互为补充。

### 陷阱5：因果推断使用不当

**问题**：混淆相关性和因果性，或者因果推断的假设不满足（如存在未观测的混杂因素）。

**解决方案**：用DoWhy的"反驳"步骤做稳健性检验。诚实地讨论可能的未观测混杂因素。不要过度声称因果结论。

### 陷阱6：安全治理被忽视

**问题**：只关注功能和性能，忽视了Agent系统的安全和伦理问题。

**解决方案**：将安全检查Agent作为系统的核心组件（不是附加功能）。用NIST AI RMF框架做系统化评估。完成研究伦理自查。

### 陷阱7：论文写作结构混乱

**问题**：论文不符合IMRaD格式，或者各部分内容不匹配（如Results写了Methods的内容）。

**解决方案**：严格按照IMRaD格式写作。每个部分有明确的功能：Introduction说"为什么"，Methods说"怎么做"，Results说"发现了什么"，Discussion说"意味着什么"。

### 陷阱8：过度声称贡献

**问题**：声称解决了"所有问题"或"颠覆了整个领域"，实际上只解决了一个具体问题。

**解决方案**：诚实描述贡献的范围。用"在X条件下，Y方法可以提升Z指标W%"这样的精确表述，而非"Y方法可以大幅提升效果"。

### 陷阱9：忽视实践可行性

**问题**：系统设计很先进但在企业环境中无法落地（成本太高、技术太复杂、组织不接受）。

**解决方案**：在设计过程中考虑实践约束。用行动研究视角记录实践中的挑战和解决方案。ROI分析要真实。

### 陷阱10：拖延到最后一刻

**问题**：前期进度缓慢，最后两周突击完成，质量大打折扣。

**解决方案**：用12周或24周的节奏表严格管理进度。每个Phase有明确的交付物和截止日期。找一位"accountability partner"互相监督。

---

## 六、Capstone答辩指南

### 6.1 答辩PPT结构

建议15-20页PPT，20分钟演讲+15分钟问答。

| 页码 | 内容 | 时间 |
|:----:|------|:----:|
| 1 | 封面（标题、姓名、日期） | 30s |
| 2 | 研究背景与动机 | 1min |
| 3 | 研究问题（RQ1-3） | 1min |
| 4 | 文献综述与研究空白 | 2min |
| 5 | DSR框架与方法论 | 1min |
| 6 | 系统架构总览 | 2min |
| 7-8 | 核心组件1：数据表示与知识图谱 | 2min |
| 9-10 | 核心组件2：Agent编排架构 | 2min |
| 11 | 核心组件3：因果决策回路 | 1min |
| 12 | 核心组件4：安全治理框架 | 1min |
| 13 | 评估方法（混合方法） | 1min |
| 14-15 | 定量结果 | 2min |
| 16 | 定性结果 | 1min |
| 17 | 设计原则（核心贡献） | 1min |
| 18 | 局限与未来方向 | 1min |
| 19 | 结论 | 30s |
| 20 | 致谢 | 30s |

### 6.2 答辩话术模板

**开场**：

> 各位评委好，我是aha.gare。我的Capstone题目是"AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构"。
>
> 在过去[X]个月中，我基于设计科学研究框架，设计、实现并评估了一个AI营销Agent系统。今天我将汇报研究的核心发现和贡献。

**研究动机**：

> 这个研究源于我在工作中的观察。作为售前解决方案产品经理，我发现企业营销决策面临三个核心挑战：第一，数据碎片化导致AI无法"理解"完整的营销上下文；第二，营销决策基于相关性而非因果性，导致决策质量不稳定；第三，Agent系统的自主性带来了安全和治理挑战。
>
> 这三个挑战分别对应了课程中的技能1（表示工程）、技能3（因果推断）和选修E9（AI安全）。

**核心贡献**：

> 本研究的主要贡献是提出了三条可复用的设计原则：
> 1. 统一表示+GraphRAG可以显著提升营销知识库的全局推理能力
> 2. 将因果推断嵌入Agent决策回路（而非仅作为事后分析）可以提升决策质量
> 3. 独立安全检查Agent作为审计层可以将Prompt Injection成功率降低至5%以下
>
> 这些设计原则不仅适用于我的企业场景，也可以被其他企业复用。

**结果呈现**：

> 在定量评估中，使用Agent系统的团队相比对照组，转化率提升了[X]%（p<0.05）。因果推断分析（使用DoWhy库）确认了这一效应的因果性，安慰剂检验结果支持估计的稳健性。
>
> 在定性评估中，5名营销人员的访谈揭示了一个有趣的发现：Agent系统不仅提升了效率，还改变了决策权分布--从"少数资深人员决策"变为"人机协作决策"，这降低了决策的偏见但引入了新的信任挑战。

**应对局限**：

> 我的研究有几个重要局限需要诚实说明。第一，样本量有限（N=X），统计功效可能不足以检测小效应。第二，研究在企业内部进行，外部效度可能受限。第三，因果推断可能存在未观测的混杂因素，虽然我做了稳健性检验但无法完全排除。
>
> 这些局限也指向了未来的研究方向：更大规模的跨企业实验、更长的观察周期、以及探索更多混杂因素。

**结尾**：

> 总结来说，本研究通过设计科学研究方法，构建了一个从表示工程到因果决策的闭环营销Agent系统，并通过混合方法验证了其有效性。核心贡献不仅是系统本身，更是从中提炼的三条设计原则。
>
> 感谢评委的聆听，期待您的反馈和问题。

### 6.3 评委常见问题与应对

| 问题 | 应对策略 |
|------|---------|
| "你的研究和已有的XX研究有什么区别？" | 提前准备2-3篇最相关的文献，清晰说明区别。不要说"我的完全不同"，要说"在XX基础上，我增加了YY" |
| "你的样本量够吗？" | 诚实回答。如果不够，说明为什么（企业实验的限制）以及你做了什么补救（准实验方法、稳健性检验） |
| "你怎么确保因果性？" | 说明A/B测试的随机化、DoWhy的反驳步骤、以及诚实地承认局限性 |
| "你的设计原则在其他企业适用吗？" | 说明设计原则的适用条件（boundary conditions），不要声称普适性 |
| "Agent系统的安全风险怎么解决？" | 引用E9的安全框架：多层防御、安全检查Agent、红队测试 |
| "ROI计算的可信度如何？" | 说明数据来源、假设的保守性、以及敏感性分析 |
| "如果重新做，你会改变什么？" | 诚实回答，展示反思能力。这是体现学术成熟度的好机会 |
| "你的研究有什么理论贡献？" | 对标DSR框架：你不仅做了一个系统，还提炼了设计原则，这是理论贡献 |
| "你用了什么具体技术？" | 简洁回答技术栈：LangGraph、DoWhy、GraphRAG、Neo4j等 |
| "下一步你打算做什么？" | 说明发表计划（arXiv->会议->期刊）和系统改进方向 |

### 6.4 答辩准备检查清单

- [ ] PPT完成并演练至少3遍
- [ ] 每页PPT的内容能在2分钟内讲完
- [ ] 准备了5个最可能的问题及应对
- [ ] 准备了2个"安全网"故事（万一紧张可以回到熟悉的内容）
- [ ] Demo系统可运行（如果需要演示）
- [ ] 论文已发给评委预读
- [ | 时间控制在20分钟内（演讲部分）
- [ ] 准备了感谢评委的结尾

---

## 七、AEFS Capstone项目库

### 7.1 概述

AEFS（AI Engineering from Scratch）项目库包含87个Capstone级别的大型实践项目，覆盖从基础AI工程到多Agent系统到安全对齐的全栈能力。这些项目与博士论文方向高度互补：博士论文侧重学术研究和设计原则提炼，AEFS项目侧重工程实现和技术深度。将两者结合，可以构建"理论+实践"的完整能力体系。

> 🔗 **AEFS项目库地址**：https://github.com/rohitg00/ai-engineering-from-scratch

### 7.2 与博士论文方向最相关的7个项目

从87个AEFS Capstone项目中，以下7个与本博士论文方向「AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构」最相关，建议优先学习：

#### 项目1：P19-02: RAG over Codebase

- **AEFS位置**：Capstone Phase 2
- **项目描述**：构建一个能对代码库进行问答的RAG系统，包含代码解析、分块策略、检索优化
- **与论文的关联**：RAG是营销智能体系统的核心检索组件。此项目让你深入理解RAG的工程细节（分块策略、检索质量优化、上下文窗口管理），这些技能直接迁移到营销知识库的GraphRAG实现中
- **迁移建议**：将代码库RAG改为营销知识库RAG，使用相同的工程框架但替换数据源和检索策略

#### 项目2：P19-04: Multimodal Document QA

- **AEFS位置**：营销物料分析方向
- **项目描述**：构建能理解图片、表格、文本的多模态文档问答系统
- **与论文的关联**：营销物料（广告创意、产品手册、品牌指南）天然是多模态的。此项目让你掌握多模态文档理解的技术栈，直接用于营销物料的自动分析和内容审核
- **迁移建议**：将通用文档QA改为营销物料分析QA，支持"分析这个广告创意是否符合品牌指南"类查询

#### 项目3：P19-05: Autonomous Research Agent

- **AEFS位置**：Capstone Phase 1
- **项目描述**：构建能自主进行文献检索、信息综合、报告生成的研究Agent
- **与论文的关联**：此项目与Phase 1（问题定义与文献综述）直接对应。一个自主研究Agent可以加速PRISMA文献综述过程，自动检索、筛选、总结相关文献
- **迁移建议**：将研究Agent用于自动化PRISMA文献综述，生成结构化的文献综述初稿

#### 项目4：P19-08: Production RAG Chatbot

- **AEFS位置**：Capstone Phase 3
- **项目描述**：构建生产级RAG聊天机器人，包含用户认证、对话管理、监控告警
- **与论文的关联**：此项目是Phase 3（Agentic系统架构设计）的工程实现基础。它教你如何将RAG从原型升级到生产级，包含可观测性、错误处理、性能优化等工程要素
- **迁移建议**：将通用Chatbot改为营销知识助手，集成到Agent编排层中

#### 项目5：P19-10: Multi-Agent Software Team

- **AEFS位置**：Capstone Phase 3
- **项目描述**：构建多Agent协作的软件开发团队，包含产品经理Agent、开发Agent、测试Agent
- **与论文的关联**：此项目与论文的Agent编排层高度相关。多Agent协作模式（任务分配、通信协议、冲突解决）可以直接迁移到营销多Agent系统（洞察Agent、创意Agent、投放Agent的协作）
- **迁移建议**：将软件开发团队Agent改为营销团队Agent，保留编排架构但替换角色定义和任务类型

#### 项目6：P19-11: LLM Observability Dashboard

- **AEFS位置**：技能5评估方向
- **项目描述**：构建LLM应用的可观测性仪表盘，监控Token使用、延迟、错误率、成本
- **与论文的关联**：可观测性是生产级Agent系统的必需组件。此项目教你如何设计和实现LLM监控系统，直接用于论文中Agent系统的运营层
- **迁移建议**：将通用监控改为营销Agent专用监控，增加营销KPI（内容质量分、转化率、合规通过率）的追踪

#### 项目7：P19-13: MCP Server with Registry

- **AEFS位置**：技能5工具链方向
- **项目描述**：构建MCP（Model Context Protocol）服务器和工具注册中心，管理Agent可用的工具
- **与论文的关联**：MCP是Agent工具管理的标准协议。此项目让你掌握工具注册、发现、调用的工程实现，直接用于营销Agent系统的工具层（搜索工具、数据库工具、分析工具的管理）
- **迁移建议**：将通用工具注册改为营销工具注册，包含搜索、分析、内容生成、投放配置等营销专用工具

### 7.3 按Capstone六阶段分类的完整项目映射表

| Capstone阶段 | 对应AEFS项目 | 技术重点 | 建议学习顺序 |
|-------------|-------------|---------|------------|
| **Phase 1: 问题定义与文献综述** | P19-05: Autonomous Research Agent | Agent自主检索与信息综合 | 1 |
| **Phase 2: 数据表示与知识图谱** | P19-02: RAG over Codebase, P19-04: Multimodal Document QA | RAG工程化、多模态文档理解 | 2, 3 |
| **Phase 3: Agentic系统架构** | P19-08: Production RAG Chatbot, P19-10: Multi-Agent Software Team | 生产级RAG、多Agent编排 | 4, 5 |
| **Phase 4: 因果实验设计** | AEFS Phase 3 因果推断项目 | 因果推断工具实践 | 6 |
| **Phase 5: 商业模式与价值评估** | AEFS Phase 19 LLM Observability Dashboard | 系统监控与ROI量化 | 7 |
| **Phase 6: 系统实现与论文** | P19-11: LLM Observability Dashboard, P19-13: MCP Server | 可观测性、工具管理 | 8, 9 |

### 7.4 学习建议

**分阶段整合策略**：

```
Capstone Phase 1-2（第1-7周）
  └─ 同步学习：P19-05 (Research Agent) + P19-02 (RAG) + P19-04 (Multimodal QA)
  └─ 目标：将AEFS项目的代码作为Capstone Phase 2的工程基础

Capstone Phase 3（第8-11周）
  └─ 同步学习：P19-08 (Production RAG) + P19-10 (Multi-Agent)
  └─ 目标：将AEFS的多Agent架构作为Capstone系统原型的起点

Capstone Phase 4-6（第12-24周）
  └─ 同步学习：P19-11 (Observability) + P19-13 (MCP Server)
  └─ 目标：将AEFS的工程实践融入Capstone的生产级实现
```

**注意事项**：

1. **不要照搬**：AEFS项目是通用工程实践，你的Capstone需要体现学术贡献（设计原则）。AEFS项目提供工程基础，你的研究提供理论增量
2. **代码复用**：可以直接复用AEFS项目的代码框架，但需要在README和论文中注明来源
3. **深度优先**：不要试图完成全部87个项目。选择与论文方向最相关的7个，深入学习到能修改和扩展的程度
4. **英语轨道**：AEFS项目的文档和代码注释都是英文，阅读它们本身就是英语平行轨道的优质材料

> 💡 **论文与项目的互补关系**：博士论文回答"为什么"（Why--设计原则的理论依据），AEFS项目回答"怎么做"（How--工程实现细节）。两者结合构成了"理论指导实践，实践验证理论"的完整闭环。

---

## 八、附录

### 附录A：Capstone与课程技能的整合矩阵

| Capstone阶段 | 整合的技能 | 整合的模块R | 整合的选修 |
|-------------|----------|-----------|-----------|
| Phase 1 | 技能0+1 | R1(DSR)+R4(PRISMA) | - |
| Phase 2 | 技能1 | R1(DSR) | - |
| Phase 3 | 技能2+5 | R2(行动研究) | E9(安全) |
| Phase 4 | 技能3 | R3(混合方法) | - |
| Phase 5 | 技能4 | R2(行动研究) | E10(商业模式) |
| Phase 6 | 全部 | R5(IMRaD)+R6(伦理) | E9+E10 |

### 附录B：技术栈推荐

| 组件 | 推荐技术 | 替代方案 |
|------|---------|---------|
| Agent编排 | LangGraph | CrewAI, AutoGen |
| 向量数据库 | Pinecone | Weaviate, Chroma |
| 知识图谱 | Neo4j | NetworkX (原型) |
| GraphRAG | Microsoft GraphRAG | 自定义实现 |
| 因果推断 | DoWhy + EconML | CausalML |
| 可观测性 | Langfuse | LangSmith |
| 安全测试 | PyRIT | Garak |
| 部署 | Docker + FastAPI | Flask, Streamlit |
| 代码管理 | Git + GitHub | GitLab |
| 论文写作 | LaTeX (Overleaf) | Markdown + Pandoc |

### 附录C：参考资源

| 资源类型 | 链接 |
|---------|------|
| DSR框架论文 | https://desrist.org/desrist/files/peffers2007.pdf |
| PRISMA声明 | http://prisma-statement.org/ |
| LangGraph文档 | https://www.langchain.com/langgraph |
| GraphRAG文档 | https://microsoft.github.io/graphrag/ |
| DoWhy文档 | https://github.com/py-why/dowhy |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework |
| Anthropic安全研究 | https://www.anthropic.com/research |
| a16z Agent Economy | https://a16z.com/tag/ai/ |
| Creswell《Research Design》 | SAGE出版 |
| APA格式指南 | https://apastyle.apa.org/ |
| ACM Computing Surveys | https://dl.acm.org/journal/csur |

### 附录D：英语轨道建议

| 阶段 | 英语任务 | 难度 |
|------|---------|:----:|
| Phase 1 | 用英文写3-5个关键词的检索策略 | ⭐⭐ |
| Phase 2 | 读GraphRAG官方英文文档 | ⭐⭐⭐ |
| Phase 3 | 读LangGraph Quickstart英文文档 | ⭐⭐⭐ |
| Phase 4 | 读DoWhy官方英文文档 | ⭐⭐⭐ |
| Phase 5 | 读a16z "Agent Economy"英文博客 | ⭐⭐⭐ |
| Phase 6 | 用英文写Abstract和Title | ⭐⭐⭐⭐ |
| Phase 6 | 用英文写README/技术博客 | ⭐⭐⭐ |

---

*本教材为AI原生化商业博士课程v4.0 Capstone教材，基于设计科学研究（DSR）框架，整合全部五技能和模块R。*  
*论文方向：「AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构」*  
*最后更新：2026-07-16*
