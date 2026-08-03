# AI原生化商业博士 · 独立教材：选修E5 商业生成式AI应用与流程自动化

> **修读者**：aha.gare  
> **导师系统**：Claude / 天道推演 + 系统觉醒 + 学位对标融合 + 牛津自然学习法 + 全球七校对标  
> **版本**：v4.0 | **日期**：2026-07-30  
> **学时**：6h | 建议节奏：3天集中学习  
> **对标课程**：MIT Sloan AI Implications for Business + Stanford GSB GenAI for Business + Harvard HBS AI in Marketing + Wharton AI Strategy + Imperial Business AI  
> **对应技能**：技能2（AI原生企业架构）+ 技能5（Agentic系统工程）应用层  
> **前置条件**：完成技能2核心课程，具备基本Python编程能力，使用过至少一个LLM API  
> **定位**：从"会调API"升级到"能端到端设计企业级GenAI自动化方案"，掌握从无代码工具到RPA到企业AI助手的完整能力链

---

## 课程概述

### 核心命题

**如何将生成式AI从"聊天工具"升级为"业务流程自动化引擎"？**

生成式AI在企业中的真正价值不是"帮你写一封邮件"，而是"自动化整个邮件营销流程--从受众分析到内容生成到A/B测试到发送优化到效果分析"。这个从"单点辅助"到"流程自动化"的跨越，是AI从成本中心走向价值创造中心的关键路径。

对于售前解决方案产品经理而言，GenAI自动化能力直接决定了方案的"可落地性"和"ROI可信度"。客户越来越不满足于"AI可以帮你做X"的演示性价值，他们要问的是：这个AI方案能替代多少人力？能缩短多少流程时间？能带来多少增量收入？要回答这些问题，你需要理解从无代码工具到RPA到企业AI应用的完整技术栈，并能在不同场景下做出正确的架构选择。

### 学习目标

完成本课程后，你将能够：

1. **工具层**：掌握主流无代码/低代码AI工具（Zapier/Make/n8n/Power Automate）的功能边界和适用场景，能根据业务需求选择合适的工具
2. **API层**：熟练调用ChatGPT/Claude API，掌握Prompt模板设计方法论，能用Python构建AI助手原型
3. **自动化层**：理解RPA的核心概念（规则驱动vs AI驱动），掌握流程挖掘基础，能用流程评估矩阵识别自动化机会
4. **架构层**：掌握GenAI应用的三种架构模式（嵌入式/对话式/自主式），能为企业设计AI助手方案
5. **商业层**：能用ROI计算框架评估自动化方案的价值，撰写企业级自动化方案提案

---

## 学习计划表（3天）

| 天次 | 主题 | 时长 | 核心产出 |
|:---:|------|:----:|---------|
| **Day 1** | 无代码/低代码AI工具生态 | 2h | Zapier自动化邮件回复流程 + Python AI助手代码 |
| **Day 2** | 业务流程自动化设计 | 2h | n8n营销内容流程代码 + 流程评估矩阵 + PyAutoGUI RPA代码 |
| **Day 3** | 企业级GenAI应用设计 | 2h | LangChain AI助手代码 + 自动化方案提案文档 |

---

## 详细学习内容

---

### Day 1：无代码/低代码AI工具生态

#### 一、工具全景图

企业AI自动化不是"选一个工具解决所有问题"，而是根据场景复杂度、定制化需求和团队技术能力选择合适的工具层级。

**三层工具生态**：

| 层级 | 工具代表 | 定制化程度 | 技术门槛 | 适用场景 |
|:----:|---------|:---------:|:--------:|---------|
| **无代码** | Zapier, Make, Power Automate | 低 | 极低 | 简单流程串联（触发->AI处理->输出） |
| **低代码** | n8n, Retool, Bubble | 中 | 低-中 | 需要自定义逻辑、条件分支、数据转换 |
| **代码** | Python+LangChain, TypeScript | 高 | 高 | 复杂AI推理、自定义模型、深度集成 |

**主流工具对比**：

| 维度 | Zapier | Make | n8n | Power Automate |
|------|--------|------|-----|----------------|
| **定位** | 最易上手的集成平台 | 可视化自动化工作流 | 开源可自部署的自动化平台 | 微软生态自动化 |
| **AI集成** | 内置OpenAI/Anthropic模块 | 内置OpenAI模块 | 需自定义HTTP节点 | 内置AI Builder |
| **定价模式** | 按任务计费（贵） | 按操作计费（中等） | 社区版免费/企业版付费 | 按用户计费（含在M365中） |
| **复杂逻辑** | 简单条件分支 | 路由/循环/错误处理 | 代码节点/自定义逻辑 | 条件/循环/审批流 |
| **数据安全** | 云端处理 | 云端处理 | 可自部署（数据不出企业） | 微软云（企业级合规） |
| **适用场景** | 快速POC、简单流程 | 中等复杂度营销自动化 | 数据敏感场景、定制需求高 | 已用微软生态的企业 |

> 💡 **售前洞察**：给客户推荐工具时，先判断两个维度：(1) 数据敏感度--如果涉及客户数据，n8n自部署或Power Automate更合规；(2) 流程复杂度--如果超过5个步骤且有复杂条件分支，Make或n8n比Zapier更合适。不要一上来就推最贵的方案--有时候Zapier+一个Python脚本就够了。

#### 二、ChatGPT/Claude API基础调用

API调用是GenAI应用的最基础能力。理解API调用模式是从"用网页版聊天"到"构建AI应用"的第一步。

```python
import openai
import json
from typing import List, Dict

# ===== OpenAI API基础调用 =====

class AIAssistant:
    """基于OpenAI API的简单AI助手"""

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.conversation_history: List[Dict] = []

    def set_system_prompt(self, prompt: str):
        """设置系统提示词，定义AI助手的角色和行为规则"""
        self.conversation_history = [{"role": "system", "content": prompt}]

    def chat(self, user_message: str, temperature: float = 0.7) -> str:
        """发送消息并获取回复"""
        self.conversation_history.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=temperature,
            max_tokens=2000
        )

        reply = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": reply})

        return reply

    def chat_with_structured_output(self, user_message: str, output_schema: dict) -> dict:
        """获取结构化输出（JSON格式）"""
        schema_prompt = f"\n请以JSON格式回复，结构如下：\n{json.dumps(output_schema, ensure_ascii=False)}"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Always respond in valid JSON."},
                {"role": "user", "content": user_message + schema_prompt}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)


# ===== 营销AI助手示例 =====

# 系统提示词：定义AI助手的角色
MARKETING_ASSISTANT_PROMPT = """你是一个专业的营销内容AI助手，具备以下能力：

1. 根据产品信息和目标受众生成营销文案
2. 为不同渠道（邮件、社媒、落地页）调整文案风格
3. 生成A/B测试变体
4. 分析营销数据并给出优化建议

规则：
- 文案必须包含明确的行动号召（CTA）
- 遵循AIDA模型（注意-兴趣-渴望-行动）
- 每次生成3个变体供选择
- 标注每个变体的适用场景
"""

# 使用示例
assistant = AIAssistant(api_key="your-api-key")
assistant.set_system_prompt(MARKETING_ASSISTANT_PROMPT)

# 生成营销文案
result = assistant.chat(
    "产品：智能客服SaaS平台\n"
    "目标受众：中小企业CTO\n"
    "渠道：LinkedIn帖子\n"
    "请生成3个文案变体"
)
print(result)

# 结构化输出示例：营销分析
analysis_schema = {
    "summary": "数据概述",
    "key_findings": ["发现1", "发现2", "发现3"],
    "recommendations": [
        {"action": "行动建议", "priority": "高/中/低", "expected_impact": "预期效果"}
    ]
}

structured_result = assistant.chat_with_structured_output(
    "以下是我们Q2的营销数据：\n"
    "- 总花费：120万元\n- 总收入：380万元\n- ROAS: 3.17\n"
    "- Search: ROAS 4.0 | Social: ROAS 3.0 | Display: ROAS 1.0 | Email: ROAS 5.67\n"
    "请分析并给出优化建议",
    analysis_schema
)
print(json.dumps(structured_result, ensure_ascii=False, indent=2))
```

#### 三、Prompt模板设计

Prompt不是"随便写一段话"，而是一种新的编程范式。好的Prompt模板应该像函数一样有明确的输入、输出和处理逻辑。

**Prompt模板设计四要素**：

| 要素 | 含义 | 示例 |
|------|------|------|
| **角色定义** | AI扮演什么角色 | "你是一位资深营销文案专家" |
| **任务说明** | 要做什么 | "为以下产品生成3个社媒文案变体" |
| **约束条件** | 有什么限制 | "每个文案不超过100字，包含CTA" |
| **输出格式** | 怎么输出 | "以JSON数组格式输出" |

**可复用Prompt模板库示例**：

```python
# ===== Prompt模板系统 =====

class PromptTemplate:
    """可复用的Prompt模板"""

    def __init__(self, template: str, input_variables: list):
        self.template = template
        self.input_variables = input_variables

    def format(self, **kwargs) -> str:
        """填充模板变量"""
        for var in self.input_variables:
            if var not in kwargs:
                raise ValueError(f"Missing required variable: {var}")
        return self.template.format(**kwargs)


# 营销文案生成模板
CONTENT_GEN_TEMPLATE = PromptTemplate(
    template="""你是一位专业的营销文案专家。

任务：为以下产品生成{num_variants}个{channel}文案变体。

产品信息：
- 名称：{product_name}
- 描述：{product_description}
- 核心卖点：{key_benefits}

目标受众：{target_audience}

要求：
1. 遵循AIDA模型（注意-兴趣-渴望-行动）
2. 每个文案不超过{max_length}字
3. 包含明确的行动号召（CTA）
4. 为每个变体标注适用场景

输出格式（JSON）：
{{
  "variants": [
    {{
      "content": "文案内容",
      "style": "风格描述",
      "best_for": "适用场景",
      "cta": "行动号召"
    }}
  ]
}}""",
    input_variables=["num_variants", "channel", "product_name", "product_description",
                     "key_benefits", "target_audience", "max_length"]
)

# 使用示例
prompt = CONTENT_GEN_TEMPLATE.format(
    num_variants=3,
    channel="邮件主题行",
    product_name="DataFlow CRM",
    product_description="AI驱动的客户关系管理系统，自动分析客户行为并推荐最佳跟进时机",
    key_benefits="提升转化率35%、减少手动跟进时间60%、客户留存率提升25%",
    target_audience="中小企业销售总监",
    max_length=50
)

# 调用AI生成
# result = assistant.chat_with_structured_output(prompt, {"variants": []})
```

#### 四、AI工具串联模式

在真实业务场景中，单个AI调用很少能完成完整流程。需要将多个AI能力串联起来，形成自动化工作流。

**三种核心串联模式**：

| 模式 | 结构 | 适用场景 | 示例 |
|------|------|---------|------|
| **串联** | A -> B -> C | 前一步输出是后一步输入 | 数据收集 -> AI分析 -> 文案生成 -> 发送 |
| **并行** | A -> [B, C, D] -> E | 同一输入多路处理 | 同一产品 -> [邮件文案, 社媒文案, 落地页文案] -> 汇总 |
| **条件分支** | A -> 判断 -> B/C | 根据AI输出路由 | 客户反馈 -> 情感分析 -> (正面:感谢信 / 负面:投诉处理) |

#### 五、实操：用Zapier+OpenAI构建自动化邮件回复

**场景**：客户发来咨询邮件 -> AI分析意图并生成回复 -> 人工审核后发送

**Zapier流程设计**：

1. **Trigger**：Gmail新邮件到达
2. **Action 1**：OpenAI - 分析邮件意图（咨询/投诉/合作/其他）
3. **Filter**：仅在意图为"咨询"时继续
4. **Action 2**：OpenAI - 根据知识库生成回复草稿
5. **Action 3**：Gmail - 创建草稿（不直接发送，需人工审核）
6. **Action 4**：Slack - 通知团队有新草稿待审核

**关键设计决策**：
- 不直接自动发送，而是创建草稿--AI生成的回复可能有错误，人工审核是必要的安全网
- 通知团队--确保草稿不会被遗忘
- 用Filter区分邮件类型--不同类型需要不同的回复策略

#### 六、实操：用Make构建社媒内容自动发布

**场景**：产品经理输入产品信息 -> AI生成多平台内容 -> 定时发布

**Make流程设计**：

1. **Module 1**：HTTP webhook接收产品信息（JSON格式）
2. **Module 2**：OpenAI生成LinkedIn长文（专业风格，500字）
3. **Module 3**：OpenAI生成Twitter短文（精炼风格，280字符）
4. **Module 4**：OpenAI生成微信公众号摘要（吸引点击，150字）
5. **Router**：并行发送到3个平台
6. **Module 5-7**：各平台API发布（或存入草稿）
7. **Module 8**：记录发布日志到Google Sheets

#### 七、Function Calling驱动的智能自动化（2026前沿补丁）

> 🌐 **跨学科桥梁**：本节连接AI工程与业务流程管理（BPM）。Function Calling将LLM从"文本生成器"升级为"流程编排器"，使自动化从"按规则执行"进化为"按意图执行"。

##### 从Prompt Chaining到Function Calling：精确性的飞跃

Day 1前面几节展示了用prompt chaining串联AI步骤的自动化方式（如Zapier+OpenAI的邮件回复流程）。这种方式有一个根本局限：LLM的输出是自然语言，下游模块需要用正则或二次LLM调用来解析，容易出错且不可扩展。

Function Calling从根本上解决了这个问题：LLM不再以自然语言输出"我想创建一个工单"，而是直接返回结构化的工具调用请求（函数名+参数），下游模块可以直接执行。这让自动化流程的精确性从"大概对"提升到"机器可执行"。

##### 结构化输出：确保LLM输出可解析

**JSON Mode**：OpenAI的`response_format={"type": "json_object"}`强制LLM输出合法JSON，但不约束schema。

**Structured Outputs**（2024+）：在function calling的parameters中定义JSON Schema，LLM的输出严格符合schema。这是生产环境推荐做法：

```python
from pydantic import BaseModel, Field
from openai import OpenAI

client = OpenAI()

# 用Pydantic定义输出结构
class TicketInfo(BaseModel):
    title: str = Field(description="工单标题，简洁概括问题")
    priority: str = Field(description="优先级", pattern="^(低|中|高|紧急)$")
    category: str = Field(description="问题分类", pattern="^(技术|商务|售后|其他)$")
    description: str = Field(description="问题详细描述")
    assignee: str = Field(description="建议处理人，如不确定填'unassigned'")

# 使用Structured Outputs
response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是客服工单分类助手。根据用户描述创建结构化工单。"},
        {"role": "user", "content": "我们的营销系统从昨天开始无法导出报表，很急，影响月度汇报。"}
    ],
    response_format=TicketInfo,
)

ticket = response.choices[0].message.parsed
print(f"标题: {ticket.title}")
print(f"优先级: {ticket.priority}")
print(f"分类: {ticket.category}")
# 输出：
# 标题: 营销系统报表导出功能异常
# 优先级: 高
# 分类: 技术
```

**instructor库**：第三方库`instructor`封装了上述逻辑，支持OpenAI/Anthropic/多家模型，提供更简洁的API和自动重试机制。

##### 自动化流程中的工具编排

Function Calling不仅仅是"调一个函数"，更强大的能力是编排多个函数的执行顺序：

- **串行编排**：步骤A的输出是步骤B的输入。LLM调用工具A -> 获取结果 -> 调用工具B。适合有依赖关系的流程。
- **并行编排**：多个工具无依赖关系，LLM通过parallel function calling一次性返回多个调用，并行执行。适合数据聚合场景。
- **条件分支**：LLM根据中间结果决定走哪条分支。例如工单分类后，"技术"类走开发团队API，"商务"类走销售团队API。这取代了传统的if-else硬编码。

##### 实操：用OpenAI Function Calling构建智能工单系统

**场景**：用户用自然语言描述问题 -> LLM提取结构化信息并调用对应API -> 创建工单/分配/通知 -> 结果验证

**步骤1：接收用户描述 -> LLM提取结构化信息**

```python
"""
智能工单系统：Function Calling + 结构化输出
依赖：pip install instructor openai pydantic
"""
import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Literal

# 用instructor包装OpenAI客户端（自动重试+schema校验）
client = instructor.from_openai(OpenAI())

# ===== 定义输出结构 =====
class ParsedTicket(BaseModel):
    title: str = Field(description="工单标题")
    priority: Literal["低", "中", "高", "紧急"]
    category: Literal["技术", "商务", "售后", "其他"]
    description: str = Field(description="问题详细描述")

# 步骤1：解析用户描述
def parse_user_request(user_message: str) -> ParsedTicket:
    """用LLM从自然语言提取结构化工单信息"""
    return client.chat.completions.create(
        model="gpt-4o",
        response_model=ParsedTicket,
        messages=[
            {"role": "system", "content": "你是客服工单分类助手。根据用户描述创建结构化工单。"},
            {"role": "user", "content": user_message}
        ],
    )
```

**步骤2：调用对应API（创建工单/分配/通知）**

```python
# ===== 模拟工单管理API =====
def create_ticket(title, priority, category, description):
    """调用工单系统API创建工单"""
    print(f"  [API调用] 创建工单: {title} (优先级: {priority})")
    return {"ticket_id": "TKT-2026-0042", "status": "created"}

def assign_ticket(ticket_id, category):
    """根据分类自动分配处理人"""
    assignee_map = {"技术": "dev-team", "商务": "sales-team", "售后": "support-team", "其他": "general"}
    assignee = assignee_map.get(category, "general")
    print(f"  [API调用] 工单 {ticket_id} 分配给: {assignee}")
    return {"ticket_id": ticket_id, "assignee": assignee}

def notify_assignee(ticket_id, assignee, priority):
    """通知处理人（邮件/Slack/钉钉）"""
    print(f"  [通知] {assignee}: 新工单 {ticket_id} (优先级: {priority})")
    return {"notification_sent": True}

# 步骤2：执行工具编排
def process_ticket(parsed: ParsedTicket) -> dict:
    """串行执行：创建 -> 分配 -> 通知"""
    # 创建工单
    create_result = create_ticket(
        parsed.title, parsed.priority, parsed.category, parsed.description
    )
    # 分配工单
    assign_result = assign_ticket(create_result["ticket_id"], parsed.category)
    # 通知处理人
    notify_result = notify_assignee(
        create_result["ticket_id"], assign_result["assignee"], parsed.priority
    )
    return {
        "ticket": create_result,
        "assignment": assign_result,
        "notification": notify_result
    }
```

**步骤3：结果验证 + 异常处理**

```python
# 步骤3：完整流程 + 异常处理
def handle_user_request(user_message: str) -> str:
    """完整工单处理流程"""
    try:
        # 步骤1：LLM解析
        parsed = parse_user_request(user_message)
        print(f"解析结果: {parsed.title} | {parsed.priority} | {parsed.category}")

        # 步骤2：工具编排执行
        result = process_ticket(parsed)

        # 步骤3：结果验证
        if result["ticket"]["status"] != "created":
            return "工单创建失败，已转人工处理"

        return f"工单已创建: {result['ticket']['ticket_id']}，已分配给{result['assignment']['assignee']}"

    except Exception as e:
        # 异常处理：LLM解析失败或API调用失败
        print(f"[异常] {type(e).__name__}: {e}")
        return f"处理失败，已转人工。错误信息: {e}"

# ===== 运行示例 =====
if __name__ == "__main__":
    user_msg = "我们上周投放的朋友圈广告突然停了，后台显示余额充足但无法恢复，影响很大，请尽快处理！"
    result = handle_user_request(user_msg)
    print(f"\n最终结果: {result}")
    # 输出：
    # 解析结果: 朋友圈广告投放异常暂停 | 紧急 | 技术
    #   [API调用] 创建工单: 朋友圈广告投放异常暂停 (优先级: 紧急)
    #   [API调用] 工单 TKT-2026-0042 分配给: dev-team
    #   [通知] dev-team: 新工单 TKT-2026-0042 (优先级: 紧急)
    # 最终结果: 工单已创建: TKT-2026-0042，已分配给dev-team
```

> 💡 **售前价值**：当客户说"我们想建一个智能客服系统"时，你可以展示这个Function Calling工单流程，解释"传统方案需要训练NLP分类模型+编写大量if-else规则，我们的方案用一个LLM+Function Calling就实现了分类+分配+通知全流程，且新增问题类型只需修改工具定义，无需重新训练模型"。这体现了AI原生化的"简洁即强大"理念。

---

### Day 2：业务流程自动化设计

#### 一、RPA概念：规则驱动vs AI驱动

**RPA（Robotic Process Automation）**是通过软件机器人模拟人类操作电脑的行为，自动执行重复性业务流程。RPA的核心价值不是"智能"，而是"不知疲倦地精确重复"。

**两代RPA的对比**：

| 维度 | 传统RPA（规则驱动） | AI驱动RPA（智能自动化） |
|------|-------------------|----------------------|
| **决策方式** | 预定义规则（if-else） | ML模型+LLM推理 |
| **适用流程** | 结构化、规则明确 | 半结构化、需要判断 |
| **异常处理** | 报错并停止 | 理解异常并自适应 |
| **维护成本** | UI变化即失效 | 更鲁棒（AI理解语义） |
| **代表工具** | UiPath, Blue Prism, Automation Anywhere | UiPath AI, Power Automate AI, n8n+LLM |
| **典型场景** | 数据录入、报表生成、系统间数据搬运 | 邮件分类回复、合同审查、智能客服 |

**传统RPA的核心局限**：传统RPA依赖UI元素定位（如按钮的XPath、输入框的ID）。当目标系统的UI发生变化时，RPA脚本就会失效。这导致传统RPA的维护成本很高--每次系统更新都需要重新调整脚本。

**AI驱动RPA的突破**：AI驱动RPA不依赖精确的UI定位，而是通过屏幕理解（Screen Understanding）和自然语言指令来操作。例如，Claude的Computer Use能力可以直接"看"屏幕并操作，不依赖底层API。

> 💡 **售前洞察**：给客户推RPA方案时，一定要评估目标系统的稳定性。如果客户的内部系统经常更新UI，传统RPA的维护成本会吞噬掉自动化带来的效率收益。此时应推荐API集成方案或AI驱动RPA方案。

#### 二、传统RPA工具

**UiPath**：全球市场份额最大的RPA平台。核心组件包括Studio（设计器）、Orchestrator（调度中心）、Robot（执行机器人）。适合大型企业的复杂流程自动化。

**Blue Prism**：企业级RPA，强调安全性和可审计性。适合金融、医疗等强合规行业。

**Automation Anywhere**：云原生RPA平台，内置IQ Bot（AI能力）实现文档提取和智能自动化。

**选择建议**：对于中小企业，不建议直接采购传统RPA平台（License成本高、实施周期长）。更推荐用n8n + Python脚本 + LLM API的组合，以更低成本实现80%的功能。

#### 三、流程挖掘（Process Mining）基础

流程挖掘是从企业系统的事件日志中自动发现真实业务流程的技术。它回答一个关键问题："流程实际上是怎么走的？"（而不是"流程应该怎么走"）。

**三个核心分析类型**：

| 类型 | 核心问题 | 输出 | 价值 |
|------|---------|------|------|
| **发现** | 实际流程是什么样的？ | 流程图（自动生成） | 发现流程的真实路径和变体 |
| **一致性检查** | 实际流程符合规定流程吗？ | 偏差报告 | 识别违规操作和流程漏洞 |
| **性能分析** | 流程的瓶颈在哪里？ | 时间分析报告 | 定位优化机会 |

**流程挖掘的输入**：事件日志（Event Log），每条记录包含：案例ID、活动名称、时间戳、资源（执行者）、成本等。

```
案例ID | 活动         | 时间戳             | 资源    | 耗时
C001   | 提交申请     | 2026-07-01 09:00   | 张三    | -
C001   | 主管审批     | 2026-07-01 14:30   | 李四    | 5.5h
C001   | 财务审核     | 2026-07-02 10:00   | 王五    | 19.5h
C001   | 打款         | 2026-07-02 15:00   | 系统    | 5h
```

通过流程挖掘，你可能会发现：实际流程平均经过7个步骤（而非规定的4个），主管审批平均耗时5.5小时（预期2小时），15%的案例需要返工。这些都是自动化机会的线索。

#### 四、流程自动化机会评估矩阵

不是所有流程都值得自动化。需要一个系统化的评估框架来判断哪些流程应该优先自动化。

**评估矩阵的四个维度**：

| 维度 | 高优先级（自动化价值高） | 低优先级（自动化价值低） |
|------|----------------------|----------------------|
| **频率** | 每天执行多次 | 每月执行一次 |
| **复杂度** | 规则明确、步骤固定 | 需要大量人工判断和创意 |
| **错误成本** | 人工错误代价高（合规/财务） | 错误影响小且易纠正 |
| **数据可得性** | 数据已在系统中结构化存储 | 数据分散在邮件/文档/口头沟通中 |

**评分公式**：自动化优先级 = 频率得分 × (1 + 复杂度适宜度) × 错误成本 × 数据可得性

**营销场景中的典型自动化机会**：

| 流程 | 频率 | 复杂度 | 错误成本 | 数据可得性 | 优先级 |
|------|:----:|:------:|:--------:|:----------:|:------:|
| 社媒内容发布 | 高 | 低 | 中 | 高 | 极高 |
| 营销报表生成 | 高 | 低 | 高 | 高 | 极高 |
| 客户咨询邮件回复 | 高 | 中 | 中 | 中 | 高 |
| Campaign效果分析 | 中 | 中 | 中 | 高 | 高 |
| 营销预算审批 | 低 | 高 | 高 | 中 | 中 |
| 创意策略brainstorm | 低 | 高 | 低 | 低 | 低 |

#### 五、实操：用n8n构建营销内容生成-审核-发布流程

**n8n流程设计**：

```
[Webhook触发] -> [OpenAI生成内容] -> [存储到Google Sheets草稿]
-> [Slack通知审核人] -> [等待审核结果] -> [审核通过?]
-> [是: 发布到CMS + 通知社媒] / [否: 返回修改意见给AI重新生成]
```

**n8n关键节点配置**：
- Webhook节点：接收产品信息JSON
- OpenAI节点：Prompt模板生成3个文案变体
- Google Sheets节点：存储到草稿表，状态为"待审核"
- Slack节点：发送审核通知，包含草稿链接
- Wait节点：等待Webhook回调审核结果
- IF节点：判断审核结果（通过/拒绝）
- HTTP Request节点：调用CMS API发布内容

#### 六、Python代码：用PyAutoGUI实现简单RPA

当没有API可用时，可以用PyAutoGUI模拟人工操作实现自动化。这是传统RPA的Python实现方式。

```python
import pyautogui
import pyperclip
import time
import pandas as pd

class SimpleRPA:
    """用PyAutoGUI实现的简单RPA--自动填写营销报表"""

    def __init__(self, safety_delay=1.0):
        self.safety_delay = safety_delay
        # 安全设置：鼠标移到屏幕左上角时紧急停止
        pyautogui.FAILSAFE = True

    def wait_and_click(self, image_name: str, timeout: int = 10):
        """等待并点击指定元素（通过图像识别）"""
        start = time.time()
        while time.time() - start < timeout:
            try:
                location = pyautogui.locateOnScreen(
                    f'images/{image_name}.png', confidence=0.8
                )
                if location:
                    center = pyautogui.center(location)
                    pyautogui.click(center)
                    time.sleep(self.safety_delay)
                    return True
            except pyautogui.ImageNotFoundException:
                pass
            time.sleep(0.5)
        raise TimeoutError(f"Element {image_name} not found within {timeout}s")

    def type_text(self, text: str, use_clipboard=True):
        """输入文本（支持中文--通过剪贴板）"""
        if use_clipboard:
            # 中文输入需要通过剪贴板，因为pyautogui不支持直接输入中文
            pyperclip.copy(text)
            pyautogui.hotkey('command', 'v')  # Mac
            # pyautogui.hotkey('ctrl', 'v')  # Windows
        else:
            pyautogui.typewrite(text, interval=0.05)
        time.sleep(self.safety_delay)

    def fill_marketing_report(self, report_data: pd.DataFrame):
        """自动填写营销报表到内部系统"""
        print("开始RPA自动化填写营销报表...")

        # Step 1: 打开报表系统（假设已打开浏览器）
        self.wait_and_click('report_system_icon')
        time.sleep(2)

        # Step 2: 点击"新建报表"按钮
        self.wait_and_click('new_report_button')

        # Step 3: 逐行填写数据
        for idx, row in report_data.iterrows():
            print(f"填写第 {idx+1}/{len(report_data)} 行...")

            # 填写日期
            self.wait_and_click('date_field')
            self.type_text(str(row['date']))

            # 填写渠道
            self.wait_and_click('channel_field')
            self.type_text(row['channel'])

            # 填写花费
            self.wait_and_click('spend_field')
            self.type_text(str(row['spend']))

            # 填写转化数
            self.wait_and_click('conversions_field')
            self.type_text(str(row['conversions']))

            # 点击"添加行"
            self.wait_and_click('add_row_button')

        # Step 4: 保存报表
        self.wait_and_click('save_button')
        print("报表填写完成！")

        # Step 5: 截图确认
        screenshot = pyautogui.screenshot()
        screenshot.save('output/report_filled.png')
        print("已保存确认截图")


# 使用示例
if __name__ == '__main__':
    # 模拟营销数据
    report_data = pd.DataFrame({
        'date': ['2026-07-01', '2026-07-02', '2026-07-03'],
        'channel': ['Search', 'Social', 'Email'],
        'spend': [12000, 8500, 3000],
        'conversions': [156, 92, 210]
    })

    rpa = SimpleRPA(safety_delay=1.5)
    rpa.fill_marketing_report(report_data)
```

**PyAutoGUI RPA的注意事项**：
1. **图像识别依赖**：需要提前截取UI元素的图片，且分辨率和缩放比例必须一致
2. **中文输入限制**：pyautogui.typewrite不支持中文，必须通过剪贴板
3. **脆弱性**：任何UI变化（窗口位置、弹窗、加载延迟）都可能导致失败
4. **替代方案**：如果目标系统有API，优先用API；如果没有API，考虑用Selenium/Playwright操作Web应用

---

### Day 3：企业级GenAI应用设计

#### 一、GenAI应用架构模式

企业级GenAI应用不是简单的"API调用+前端界面"，而是需要根据业务场景选择合适的架构模式。

**三种架构模式**：

| 模式 | 核心 | 适用场景 | 复杂度 | 示例 |
|------|------|---------|:------:|------|
| **嵌入式** | AI作为功能嵌入已有产品 | 提升已有产品体验 | 低 | Gmail智能补全、Excel AI分析 |
| **对话式** | 以对话为核心的AI助手 | 知识查询、内容生成、客服 | 中 | 企业知识库Chatbot、营销文案助手 |
| **自主式** | AI Agent自主规划和执行多步任务 | 复杂业务流程自动化 | 高 | 自动化营销Campaign管理 |

**架构选择决策树**：

```
用户需要什么？
├─ 在已有流程中获得AI辅助 -> 嵌入式
├─ 通过对话获取信息/生成内容 -> 对话式
│   └─ 需要查询企业知识库？ -> 对话式 + RAG
│   └─ 需要执行操作（发邮件/建报表）？ -> 对话式 + Function Calling
└─ AI自主完成端到端任务 -> 自主式
    └─ 任务步骤是否可预测？ -> 是: 工作流编排(n8n/Make)
    └─ 任务步骤需要动态规划？ -> Agent框架(LangGraph/AutoGen)
```

> 💡 **售前洞察**：不要一上来就推"自主式Agent"--这是最复杂也最容易失败的模式。大多数企业需求用"对话式+RAG"就能满足。先交付一个可靠的对话式AI助手，建立信任后再逐步升级到自主式。这是"先可用后好用"的渐进式策略。

#### 二、企业AI助手设计：知识库+RAG+对话界面

**RAG（Retrieval-Augmented Generation）**是企业AI助手的核心架构。它通过"先检索后生成"的方式，让AI能够基于企业私有知识回答问题，避免幻觉。

**RAG系统架构**：

```
用户问题 -> [Embedding] -> 向量检索 -> Top-K相关文档
                                        ↓
用户问题 + 检索到的文档 -> LLM生成 -> 回答
```

**LangChain实现企业AI助手**：

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import pandas as pd

# ===== 企业知识库构建 =====

class EnterpriseKnowledgeBase:
    """企业知识库--从多种数据源构建向量索引"""

    def __init__(self, openai_api_key: str):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", "。", " ", ""]
        )
        self.vectorstore = None

    def add_documents(self, documents: list[Document]):
        """添加文档到知识库"""
        splits = self.text_splitter.split_documents(documents)
        if self.vectorstore is None:
            self.vectorstore = Chroma.from_documents(
                splits, self.embeddings,
                persist_directory="./chroma_db"
            )
        else:
            self.vectorstore.add_documents(splits)
        self.vectorstore.persist()
        print(f"已添加 {len(splits)} 个文档片段到知识库")

    def add_marketing_data(self, data: pd.DataFrame, metadata_cols: list = None):
        """将营销数据转化为文档存入知识库"""
        docs = []
        for _, row in data.iterrows():
            content = f"""
            日期：{row.get('date', 'N/A')}
            渠道：{row.get('channel', 'N/A')}
            花费：{row.get('spend', 'N/A')}元
            展示量：{row.get('impressions', 'N/A')}
            点击量：{row.get('clicks', 'N/A')}
            转化量：{row.get('conversions', 'N/A')}
            收入：{row.get('revenue', 'N/A')}元
            ROAS：{row.get('roas', 'N/A')}
            """
            metadata = {col: str(row[col]) for col in (metadata_cols or [])}
            docs.append(Document(page_content=content, metadata=metadata))

        self.add_documents(docs)

    def search(self, query: str, k: int = 5):
        """检索相关文档"""
        return self.vectorstore.similarity_search(query, k=k)


# ===== RAG问答系统 =====

class MarketingAIAssistant:
    """营销AI助手--基于RAG的企业知识问答"""

    SYSTEM_PROMPT = """你是一个专业的营销分析AI助手。

你的职责：
1. 基于提供的营销数据回答用户问题
2. 如果数据中没有相关信息，明确告知用户而非编造答案
3. 给出数据驱动的建议，避免泛泛而谈
4. 量化分析结果，用具体数字支撑结论

回答格式：
- 直接回答问题
- 列出关键数据支撑
- 如适用，给出行动建议

参考数据：
{context}
"""

    def __init__(self, api_key: str, knowledge_base: EnterpriseKnowledgeBase):
        self.llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.3,
            openai_api_key=api_key
        )
        self.kb = knowledge_base

    def ask(self, question: str) -> str:
        """基于知识库回答问题"""
        # Step 1: 检索相关文档
        docs = self.kb.search(question, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])

        # Step 2: 构建Prompt
        prompt = ChatPromptTemplate.from_template(self.SYSTEM_PROMPT)

        # Step 3: 生成回答
        chain = (
            {"context": lambda x: context, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )

        return chain.invoke(question)


# ===== 使用示例 =====

if __name__ == '__main__':
    API_KEY = "your-openai-api-key"

    # 1. 构建知识库
    kb = EnterpriseKnowledgeBase(openai_api_key=API_KEY)

    # 2. 添加营销数据
    marketing_data = pd.DataFrame({
        'date': ['2026-07-01']*4 + ['2026-07-02']*4,
        'channel': ['Search', 'Social', 'Email', 'Display']*2,
        'spend': [12000, 8500, 3000, 5000, 11500, 9000, 3200, 4800],
        'impressions': [180000, 220000, 45000, 300000, 175000, 210000, 42000, 280000],
        'clicks': [5400, 3300, 2700, 1200, 5200, 3150, 2520, 1100],
        'conversions': [156, 92, 210, 24, 148, 95, 225, 22],
        'revenue': [62400, 27600, 84000, 4800, 59200, 28500, 90000, 4400],
    })
    marketing_data['roas'] = (marketing_data['revenue'] / marketing_data['spend']).round(2)
    marketing_data['ctr'] = (marketing_data['clicks'] / marketing_data['impressions'] * 100).round(2)
    marketing_data['cpa'] = (marketing_data['spend'] / marketing_data['conversions']).round(2)

    kb.add_marketing_data(marketing_data, metadata_cols=['date', 'channel'])

    # 3. 创建AI助手
    assistant = MarketingAIAssistant(api_key=API_KEY, knowledge_base=kb)

    # 4. 提问
    questions = [
        "哪个渠道的ROAS最高？",
        "Display渠道的表现如何？有什么建议？",
        "如果我要优化预算分配，应该怎么调整？"
    ]

    for q in questions:
        print(f"\n{'='*60}")
        print(f"问题：{q}")
        print(f"{'='*60}")
        answer = assistant.ask(q)
        print(answer)
```

> 🔗 **延伸实践**：详见 AEFS Phase 13 · Lesson 06-08: MCP Fundamentals / Server / Client（Model Context Protocol--让AI助手安全连接企业工具和数据源的标准协议）

#### 三、自动化方案提案撰写模板

作为售前解决方案产品经理，你需要能将技术方案转化为客户能理解的商业提案。以下是一个经过验证的提案结构：

**提案结构**：

```
1. 执行摘要（1页）
   - 客户痛点（1-2句）
   - 方案概述（1-2句）
   - 预期收益（量化）

2. 现状分析（2-3页）
   - 当前流程梳理（流程图）
   - 痛点量化（时间成本、错误率、人力成本）
   - 自动化机会评估矩阵

3. 方案设计（3-5页）
   - 技术架构图
   - 核心组件说明
   - 与现有系统集成方案
   - 数据安全与合规方案

4. 实施计划（1-2页）
   - 分阶段路线图（POC -> 试点 -> 推广）
   - 时间线与里程碑
   - 资源需求

5. 价值评估（1-2页）
   - ROI计算
   - 定量收益（节省人力、缩短时间、减少错误）
   - 定性收益（员工满意度、客户体验提升）

6. 风险与应对（1页）
   - 技术风险及应对
   - 组织变革风险及应对
```

#### 四、ROI计算与价值评估

ROI计算是方案提案中最关键的部分。如果ROI算不清楚，方案就不会被批准。

**自动化ROI计算框架**：

```python
# ===== 自动化ROI计算器 =====

class AutomationROICalculator:
    """营销自动化ROI计算器"""

    def __init__(self):
        self.costs = {}
        self.benefits = {}

    # ===== 成本计算 =====

    def calculate_costs(self, implementation_cost: float, annual_license: float,
                        maintenance_cost: float, training_cost: float):
        """计算总拥有成本（TCO）"""
        self.costs = {
            'implementation': implementation_cost,  # 一次性实施成本
            'license': annual_license,              # 年度License费
            'maintenance': maintenance_cost,        # 年度维护成本
            'training': training_cost,              # 一次性培训成本
        }

        # 3年TCO
        tco_3year = (implementation_cost + training_cost +
                     (annual_license + maintenance_cost) * 3)
        self.costs['tco_3year'] = tco_3year
        return tco_3year

    # ===== 收益计算 =====

    def calculate_benefits(self, manual_hours_per_day: float, hourly_rate: float,
                           error_rate_manual: float, error_cost_per_case: float,
                           daily_volume: int, automation_efficiency: float = 0.8):
        """计算自动化收益"""
        # 1. 人力节省
        annual_hours_saved = manual_hours_per_day * 250 * automation_efficiency  # 250个工作日
        annual_labor_saving = annual_hours_saved * hourly_rate

        # 2. 错误减少
        automated_error_rate = error_rate_manual * 0.1  # 自动化后错误率降低90%
        annual_errors_reduced = daily_volume * 250 * (error_rate_manual - automated_error_rate)
        annual_error_saving = annual_errors_reduced * error_cost_per_case

        # 3. 效率提升带来的营收增长（更快的响应时间 -> 更高转化率）
        # 假设响应时间缩短50%，转化率提升5%
        revenue_uplift = daily_volume * 250 * 0.05 * 200  # 假设客单价200元

        self.benefits = {
            'labor_saving': annual_labor_saving,
            'error_reduction': annual_error_saving,
            'revenue_uplift': revenue_uplift,
            'total_annual': annual_labor_saving + annual_error_saving + revenue_uplift
        }

        return self.benefits['total_annual']

    # ===== ROI计算 =====

    def calculate_roi(self) -> dict:
        """计算3年ROI"""
        total_cost = self.costs['tco_3year']
        total_benefit = self.benefits['total_annual'] * 3

        roi = (total_benefit - total_cost) / total_cost * 100
        payback_months = (self.costs['implementation'] + self.costs['training']) / \
                         (self.benefits['total_annual'] / 12)

        return {
            'total_cost_3year': total_cost,
            'total_benefit_3year': total_benefit,
            'roi_percentage': round(roi, 1),
            'payback_months': round(payback_months, 1),
            'net_benefit_3year': total_benefit - total_cost,
            'annual_breakdown': self.benefits,
            'cost_breakdown': self.costs
        }


# ===== 使用示例 =====

calculator = AutomationROICalculator()

# 成本：实施15万 + License 8万/年 + 维护2万/年 + 培训3万
calculator.calculate_costs(
    implementation_cost=150000,
    annual_license=80000,
    maintenance_cost=20000,
    training_cost=30000
)

# 收益：每天4小时手动工作，时薪100元，错误率5%，每次错误成本500元，日处理量200
calculator.calculate_benefits(
    manual_hours_per_day=4,
    hourly_rate=100,
    error_rate_manual=0.05,
    error_cost_per_case=500,
    daily_volume=200,
    automation_efficiency=0.8
)

result = calculator.calculate_roi()
print(f"3年总成本：¥{result['total_cost_3year']:,.0f}")
print(f"3年总收益：¥{result['total_benefit_3year']:,.0f}")
print(f"3年ROI：{result['roi_percentage']}%")
print(f"投资回收期：{result['payback_months']}个月")
print(f"3年净收益：¥{result['net_benefit_3year']:,.0f}")
print(f"\n收益分解：")
for k, v in result['annual_breakdown'].items():
    if isinstance(v, (int, float)) and k != 'total_annual':
        print(f"  {k}: ¥{v:,.0f}/年")
```

#### 五、案例分析：零售企业营销流程自动化全方案

**客户背景**：某区域性零售连锁企业，50家门店，年营收3亿元。营销团队8人，每周花费大量时间在重复性工作上：手动制作各门店周报、人工回复客户咨询、手动调整社媒发布排期。

**痛点量化**：

| 流程 | 当前耗时/周 | 错误率 | 人力成本/年 |
|------|:----------:|:------:|:----------:|
| 门店周报制作 | 20小时 | 8% | 10万元 |
| 客户咨询回复 | 30小时 | 3% | 15万元 |
| 社媒内容发布 | 15小时 | 5% | 7.5万元 |
| Campaign数据汇总 | 10小时 | 10% | 5万元 |
| **合计** | **75小时/周** | - | **37.5万元/年** |

**方案设计**：

1. **数据层**：建立统一营销数据仓库（用Python ETL + PostgreSQL），自动从各系统（POS、CRM、广告平台API）抽取数据
2. **AI层**：部署企业AI助手（LangChain+RAG），覆盖营销知识查询、文案生成、数据分析
3. **自动化层**：用n8n编排营销内容生成-审核-发布流程；用Python脚本自动生成门店周报
4. **前端层**：用Dash构建营销仪表盘，替代手动Excel报表

**预期效果**：
- 每周节省60小时人力（80%自动化率）
- 年节省人力成本30万元
- 错误率从6.5%降至1%以下
- 营销响应速度提升3倍（从平均4小时到1小时）
- 3年ROI：285%，投资回收期8.5个月

> 💡 **售前洞察**：这个案例的关键不是技术有多先进，而是ROI计算有多扎实。客户买的不是"AI很酷"，而是"投入15万能省30万/年"。在方案提案中，技术架构只占30%篇幅，价值论证占50%，实施计划占20%。这个比例反映了客户的真实决策逻辑。

---

## 知识问答

| # | 问题 | 参考答案要点 | 难度 |
|:--:|------|------------|:----:|
| Q1 | Zapier、Make、n8n三个工具的核心区别是什么？在什么场景下应该选n8n？ | Zapier最易上手但最贵且定制化低；Make支持复杂逻辑且性价比中等；n8n可自部署、数据不出企业且支持代码节点。选n8n的场景：数据敏感（金融/医疗）、需要深度定制、预算有限且团队有技术能力。 | ⭐⭐ |
| Q2 | Prompt模板设计的四要素是什么？为什么"输出格式"要素对工程化应用至关重要？ | 角色定义、任务说明、约束条件、输出格式。输出格式至关重要因为：程序需要解析AI输出，如果格式不稳定（有时JSON有时纯文本），下游代码就会出错。用JSON Schema约束输出是工程化的基础。 | ⭐⭐⭐ |
| Q3 | 传统RPA（规则驱动）和AI驱动RPA的核心区别是什么？为什么传统RPA的维护成本高？ | 传统RPA依赖UI元素定位（XPath/ID），UI变化即失效；AI驱动RPA通过屏幕理解操作，更鲁棒。传统RPA维护成本高因为企业系统频繁更新UI，每次更新都需要调整脚本。 | ⭐⭐⭐ |
| Q4 | 流程挖掘的三个核心分析类型是什么？它如何帮助识别自动化机会？ | 发现（生成实际流程图）、一致性检查（对比规定vs实际流程）、性能分析（定位瓶颈）。通过流程挖掘发现：哪些步骤耗时最长、哪些步骤有返工、哪些路径是异常变体--这些都是自动化优先目标。 | ⭐⭐⭐ |
| Q5 | GenAI应用的三种架构模式（嵌入式/对话式/自主式）各自的适用场景是什么？ | 嵌入式适合在已有产品中增加AI辅助（如智能补全）；对话式适合知识查询和内容生成（如企业知识库Chatbot）；自主式适合复杂多步任务自动化（如Agent管理营销Campaign）。 | ⭐⭐ |
| Q6 | RAG系统中"先检索后生成"的流程是什么？为什么RAG比直接让LLM回答更可靠？ | 流程：用户问题->Embedding->向量检索Top-K文档->拼接为Context->LLM基于Context生成回答。RAG更可靠因为：(1)回答有据可查（引用来源）；(2)可以回答企业私有知识；(3)减少幻觉（LLM基于检索到的真实文档回答）。 | ⭐⭐⭐ |
| Q7 | 在自动化方案提案中，"执行摘要"应该包含哪些要素？为什么放在第一页？ | 包含：客户痛点（1-2句）、方案概述（1-2句）、预期收益（量化ROI）。放第一页因为决策者通常只看第一页--如果执行摘要不能说服他们，后面的详细方案不会被看到。 | ⭐⭐ |
| Q8 | 自动化ROI计算中，"投资回收期"和"3年ROI"分别怎么计算？各自有什么业务含义？ | 回收期=一次性投入/月度收益，表示多久"回本"。3年ROI=(3年总收益-3年总成本)/3年总成本×100%，表示投资回报率。回收期<12个月通常被认为是"快速回报"方案。 | ⭐⭐⭐ |
| Q9 | 在LangChain实现的企业AI助手中，为什么使用RecursiveCharacterTextSplitter而不是固定长度切割？ | RecursiveCharacterTextSplitter按语义边界（段落->句子->词）递归切割，尽量保持每个chunk的语义完整性。固定长度切割可能在一个句子中间断开，导致检索到的chunk语义不完整，影响RAG质量。 | ⭐⭐⭐ |
| Q10 | 在设计AI驱动的邮件自动回复系统时，为什么不建议直接自动发送AI生成的回复？ | AI生成的内容可能有事实错误、语气不当或泄露敏感信息。应该创建草稿+人工审核（Human-in-the-loop），在保证效率的同时确保安全。可以设置置信度阈值：高置信度自动回复，低置信度转人工。 | ⭐⭐ |

---

## 作业设计

### 必做作业：用Python构建营销AI助手

**任务**：

1. 用OpenAI API构建一个营销文案生成助手
2. 设计至少3个Prompt模板（不同渠道/不同受众）
3. 实现结构化输出（JSON格式）
4. 为一个真实产品生成3个渠道的营销文案
5. 写一份300字的使用说明和效果评估

**交付物**：可运行的Python代码 + 生成的文案示例 + 使用说明

**评分标准**：

| 维度 | 优秀（9-10分） | 良好（7-8分） | 合格（5-6分） | 不合格（<5分） |
|------|-------------|------------|------------|-------------|
| 代码质量 | 可运行、结构化、有注释 | 基本可运行 | 有小bug | 无法运行 |
| Prompt设计 | 模板可复用、约束清晰 | 模板基本合理 | 仅基础Prompt | 缺少模板设计 |
| 输出质量 | 文案有商业价值、格式规范 | 文案基本可用 | 文案泛泛 | 输出不可用 |

### 挑战作业：企业营销自动化方案提案

**任务**：选择一个你熟悉的行业（零售/B2B SaaS/金融/教育），设计一个完整的营销自动化方案：

1. 梳理当前营销流程（流程图），量化痛点
2. 设计自动化方案架构（技术架构图）
3. 用LangChain构建一个RAG-based营销知识库助手原型
4. 计算方案ROI（用ROI计算器框架）
5. 撰写一份800字的方案提案（按提案模板结构）

**评分标准**：重点考察痛点量化的准确性、方案架构与痛点的匹配度、ROI计算的可信度、以及提案的商业说服力。

---

## 推荐资源清单

### 核心文档（必读）
- 🌐 **OpenAI API文档**: https://platform.openai.com/docs
- 🌐 **Anthropic API文档**: https://docs.anthropic.com/
- 🌐 **LangChain文档**: https://python.langchain.com/
- 🌐 **n8n文档**: https://docs.n8n.io/
- 🌐 **Make（Integromat）文档**: https://www.make.com/en/help

### 无代码/低代码工具
- 🌐 **Zapier**: https://zapier.com/
- 🌐 **Make**: https://www.make.com/
- 🌐 **n8n**: https://n8n.io/ (可自部署)
- 🌐 **Power Automate**: https://make.powerautomate.com/
- 🌐 **Retool**: https://retool.com/ (内部工具构建)

### RPA工具
- 🌐 **UiPath**: https://www.uipath.com/
- 🌐 **Automation Anywhere**: https://www.automationanywhere.com/
- 🌐 **PyAutoGUI文档**: https://pyautogui.readthedocs.io/
- 🌐 **Selenium**: https://www.selenium.dev/
- 🌐 **Playwright**: https://playwright.dev/ (现代Web自动化)

### 对标课程
- 🌐 **MIT Sloan AI Implications for Business**: https://executive-education.mit.edu/artificial-intelligence
- 🌐 **Stanford GSB GenAI for Business**: https://www.gsb.stanford.edu/exec-ed/
- 🌐 **Wharton AI Strategy**: https://execed.wharton.upenn.edu/
- 🌐 **Google Cloud Generative AI**: https://www.cloudskillsboost.google/paths/118

### 进阶阅读（可选）
- 📄 **"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"**: RAG原始论文
- 📄 **LangChain RAG教程**: https://python.langchain.com/docs/tutorials/rag/
- 🌐 **LlamaIndex（RAG框架）**: https://www.llamaindex.ai/
- 🌐 **AutoGen（多Agent框架）**: https://microsoft.github.io/autogen/
- 🌐 **CrewAI（Agent编排）**: https://www.crewai.com/

---

> 💡 **学习建议**：本选修课的核心方法论是"从工具到架构到商业"的递进。Day 1学工具（能用），Day 2学设计（会选），Day 3学商业（能卖）。建议在学习过程中始终带着一个真实场景："如果客户问我'能不能帮我自动化营销流程'，我该怎么回答？"--这个场景驱动能帮助你把三天内容串联为一个完整的方案能力。另外，强烈建议动手搭建n8n环境（可以Docker自部署）和注册OpenAI API，实操远比阅读有效。
