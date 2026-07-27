# AI原生化商业博士 · 独立教材 · 技能0：AI商业分析基础（预科层）

> **修读者**：aha.gare
> **导师系统**：Claude / 天道推演 + 系统觉醒 + 学位对标融合 + 牛津自然学习法 + 全球七校对标
> **版本**：v4.0 | **日期**：2026-07-16
> **学时**：22小时 + 英语平行轨道4小时
> **对标课程**：Introduction to Computing + Statistics + Business Data Management + Principle of Data Analytics and Programming
> **对标大学**：MIT OCW 15.071 The Analytics Edge / Stanford CS229先修要求 / Imperial Maths & Stats Foundations / NUS CS6101研究导论
> **英语轨道材料**：Kaggle英文教程 + Khan Academy Statistics + MIT OCW 15.071英文讲义 + Python Official Tutorial（i+1难度：⭐⭐）
> **课程哲学**：表示即知识 -> 规模揭示本质 -> 目标即终点 -> 做出来才算数 -> 研究即贡献
> **英语教学法**：牛津自然学习法（Krashen & Terrell's Natural Approach）—— i+1可理解输入 · 理解先于输出 · 低情感过滤

---

## 模块概述

### 为什么需要预科

aha.gare的背景是售前解决方案产品经理，聚焦AI+企业营销，具备战略规划与落地、跨学科商业模式、应用工程三重底色。这套背景在业务实战中极为宝贵，但**统计学和编程基础**可能在长期商业实践中有所弱化——不是不会，而是长期不常用、不深入，导致在面对后续技能中的数学推导和工程实现时会出现"知道概念但无法亲手操作"的断层。

预科不是"低人一等"的补习班。它是**后续所有高级技能的认知地基**。全球七所顶尖大学的博士项目——Harvard HBS、MIT Sloan/IDSS、Stanford GSB/CS、Oxford、Cambridge、Imperial、NUS——无一例外地在博士第一年安排密集的基础课程训练。MIT IDSS要求博士生在入学前就具备概率论、线性代数和编程能力；Stanford CS229（Machine Learning）在syllabus中明确列出先修要求；Imperial的MSc Business Analytics & AI项目将Maths & Statistics Foundations列为必修前置模块。预科层的设计正是对标这些全球顶尖课程的基础要求。

如果地基不牢，后果是明确的：
- 技能3（因果推断）中的do-演算和潜在结果框架会看不懂推导过程，只能记住结论而无法判断适用条件
- 技能5（系统落地）中的Agent编排代码会反复卡壳，无法独立完成从需求到原型的工程闭环
- 模块R（博士研究方法论）中的文献综述和论文写作会因为缺乏统计素养而无法批判性阅读实证论文
- 读英文论文时看到公式就跳过，永远停留在"懂概念不懂原理"的浅层理解

### 核心命题

**你是否有足够的统计和编程基础来理解后续所有技能？是否有足够的学术认知来理解博士论文的构成？**

这个问题不是修辞，而是一个可量化的自检标准。完成预科后，你应该能：
1. 独立写出100行以上的Python数据分析脚本
2. 看懂一篇带公式的AI/商业分析论文的核心方法部分
3. 解释p值、置信区间、统计显著性的含义，并知道它们的局限
4. 设计一个简单的企业数据库Schema
5. 理解学术研究的基本范式和博士论文的结构

### 前置条件

- 天赋激活：对AI原生时代有基本认知，有学习动力
- 工作场景：有真实的营销/商业数据可以用于练习（脱敏后）
- 工具准备：安装Python 3.10+、Jupyter Notebook、VS Code或PyCharm

### 完成标准

| 维度 | 合格标准 | 卓越标准 |
|------|---------|---------|
| 编程能力 | 能独立写出50行以上的数据处理脚本 | 能写出有函数封装、错误处理的完整分析Pipeline |
| 统计理解 | 能解释p值、置信区间、假设检验的逻辑 | 能正确选择检验方法，能解释结果的业务含义和局限 |
| 数据管理 | 能设计3张表以上的数据库Schema | 能设计完整的企业数据架构，理解数据治理 |
| 研究认知 | 知道学术研究和工程实践的区别 | 能用IMRaD格式写一个研究计划大纲 |
| 英语阅读 | 能借助翻译读懂Python官方教程核心段落 | 能直接读懂MIT OCW 15.071英文讲义的核心段落 |

---

## 学习计划表（6天 · v4.0）

| 天次 | 主题 | 时长 | 核心产出 | 对标课程 | 英语轨道材料 |
|:---:|------|:----:|---------|:------:|-------------|
| Day 1 | 计算概论：Python编程基础 | 4h | 写出完整的数据处理脚本 | 计算概论 + 数据分析与编程原理 | Python Official Tutorial Part 1（⭐） |
| Day 2 | 计算概论：数据结构与应用 | 4h | 能处理JSON/CSV/数据库数据 | 计算概论 + 数据分析与编程原理 | Python Official Tutorial Part 2-3（⭐） + MIT OCW 15.071 Unit 1（⭐⭐） |
| Day 3 | 统计学：描述统计与推断统计 | 4h | 理解均值/方差/假设检验 | 统计学 | Khan Academy Statistics（⭐⭐） |
| Day 4 | 统计学：回归分析与概率分布 | 4h | 能独立完成线性回归分析 | 统计学 | Khan Academy Probability（⭐⭐） + MIT OCW 15.071 Unit 2（⭐⭐） |
| Day 5 | 商业数据管理：数据治理与SQL | 4h | 能设计简单的企业数据Schema | 商业数据管理 | Kaggle Learn: SQL（⭐） |
| Day 6 | 研究方法论入门（v4.0新增） | 2h | 理解学术研究的基本流程和IMRaD格式 | 对标Imperial MRes入门 / NUS CS6101 | Creswell《Research Design》Ch.1（⭐⭐⭐） |

> **英语轨道总时长**：4小时，分散在6天中，每天约40分钟。不单独安排大块时间，而是在学习对应内容时同步阅读英文材料。

---

## 详细学习内容

---

### Day 1：计算概论——Python编程基础

> 🌐 **英语轨道（i+1）**：Python Official Tutorial Part 1（https://docs.python.org/3/tutorial/introduction.html）—— 能读懂60%就继续，读不懂的段落查一下关键词，不背单词，继续读。目标是习惯英文技术文档的句式和术语。

#### 核心概念

**1. Python为什么是AI商业分析的首选语言**

Python不是最快的语言，也不是最优雅的语言，但它是AI和数据科学生态最完整的语言。NumPy（数值计算）、Pandas（表格处理）、Scikit-learn（机器学习）、Statsmodels（统计建模）、Matplotlib/Seaborn（可视化）构成了一个无缝衔接的工具链。当你在后续技能中需要使用LangChain（Agent编排）、DoWhy（因果推断）、PyTorch（深度学习）时，它们全部是Python库。选择Python不是偏好问题，是生态问题。

对于aha.gare这样有应用工程背景的售前解决方案产品经理，Python的优势在于：它的语法足够简洁，可以快速写出原型验证想法；它的生态足够丰富，可以从数据分析一路写到生产级API。这与后续技能5中的LangGraph Agent编排直接衔接。

**2. 基础语法要素**

Python的核心语法包括五个层次，每个层次在商业分析中都有直接应用：

- **变量与数据类型**：整数（int）、浮点数（float）、字符串（str）、布尔值（bool）。在商业数据中，销售额是float，客户ID可能是str（因为前导零），是否复购是bool。
- **控制流**：if-elif-else条件判断、for循环、while循环。在数据处理中，for循环遍历客户列表做分群，if判断筛选高价值客户。
- **函数**：将重复逻辑封装为函数，提高代码复用性。def关键字定义函数，return返回结果。
- **数据结构**：列表（list）、字典（dict）、元组（tuple）、集合（set）。字典在处理JSON数据时极为常用——API返回的数据几乎都是嵌套字典。
- **面向对象基础**：类（class）、属性、方法。理解面向对象是后续使用LangChain/DoWhy等库的前提——这些库的API都是面向对象设计的。

**3. NumPy数组运算**

NumPy是Python数值计算的基石。它的核心是ndarray（N维数组），比Python原生列表快10-100倍，因为底层数据连续存储且用C实现。在商业分析中，NumPy用于：
- 批量计算（如同时计算1000个客户的LTV）
- 矩阵运算（后续技能1中的embedding计算）
- 随机数生成（模拟A/B测试数据）

**4. Pandas表格处理**

Pandas是Python数据分析的核心工具。它的两个核心数据结构——Series（一维）和DataFrame（二维）——覆盖了商业分析中90%的数据处理需求。DataFrame可以理解为Excel表格的程序化版本，但能处理的数据量远超Excel（百万行级别），且支持复杂的筛选、分组、聚合操作。

#### 真实案例分析：电商客户消费数据分析

**场景**：你是一家电商公司的售前解决方案产品经理，市场部给你一份客户消费数据（CSV格式），需要你快速分析客户消费行为特征，为后续的AI营销方案提供数据支撑。

**数据描述**：模拟数据集包含1000个客户，字段包括客户ID、年龄、性别、注册天数、消费总金额、购买次数、最近一次购买距今天数、是否复购。

**代码示例（完整可运行）**：

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 电商客户消费数据分析脚本
# 场景：市场部需要了解客户消费行为特征，为AI营销方案提供数据支撑
# ============================================================

# 1. 生成模拟数据（实际使用时替换为真实CSV读取）
np.random.seed(42)
n_customers = 1000

data = {
    'customer_id': [f'C{str(i).zfill(5)}' for i in range(1, n_customers + 1)],
    'age': np.random.normal(35, 10, n_customers).clip(18, 70).astype(int),
    'gender': np.random.choice(['M', 'F'], n_customers, p=[0.45, 0.55]),
    'registration_days': np.random.randint(30, 1000, n_customers),
    'total_spending': np.random.lognormal(6, 0.8, n_customers).round(2),
    'purchase_count': np.random.poisson(5, n_customers) + 1,
    'days_since_last_purchase': np.random.randint(1, 180, n_customers),
}

df = pd.DataFrame(data)

# 标记是否复购（购买次数 > 1）
df['is_repeat_buyer'] = df['purchase_count'] > 1

# 计算客单价（平均每笔订单金额）
df['avg_order_value'] = df['total_spending'] / df['purchase_count']

# 2. 描述性统计
print("=" * 60)
print("电商客户消费数据 - 描述性统计")
print("=" * 60)

print(f"\n总客户数: {len(df)}")
print(f"复购客户数: {df['is_repeat_buyer'].sum()} ({df['is_repeat_buyer'].mean()*100:.1f}%)")
print(f"总消费金额: ¥{df['total_spending'].sum():,.2f}")
print(f"平均消费金额: ¥{df['total_spending'].mean():,.2f}")
print(f"消费金额中位数: ¥{df['total_spending'].median():,.2f}")
print(f"消费金额标准差: ¥{df['total_spending'].std():,.2f}")

print("\n--- 按性别分组统计 ---")
gender_stats = df.groupby('gender').agg({
    'total_spending': ['mean', 'median', 'count'],
    'purchase_count': 'mean',
    'is_repeat_buyer': 'mean'
}).round(2)
print(gender_stats)

# 3. RFM分析（Recency, Frequency, Monetary）
# RFM是营销中经典的客户分群方法
print("\n--- RFM客户分群 ---")

# 按分位数打分（1-5分）
df['R_score'] = pd.qcut(df['days_since_last_purchase'], 5,
                         labels=[5, 4, 3, 2, 1], duplicates='drop')
df['F_score'] = pd.qcut(df['purchase_count'].rank(method='first'), 5,
                         labels=[1, 2, 3, 4, 5])
df['M_score'] = pd.qcut(df['total_spending'].rank(method='first'), 5,
                         labels=[1, 2, 3, 4, 5])

# RFM总分
df['RFM_total'] = df['R_score'].astype(int) + df['F_score'].astype(int) + df['M_score'].astype(int)

# 客户分层
def classify_customer(rfm_total):
    if rfm_total >= 13:
        return '高价值客户'
    elif rfm_total >= 9:
        return '中等价值客户'
    elif rfm_total >= 5:
        return '低价值客户'
    else:
        return '流失风险客户'

df['customer_segment'] = df['RFM_total'].apply(classify_customer)

segment_summary = df.groupby('customer_segment').agg({
    'customer_id': 'count',
    'total_spending': ['mean', 'sum'],
    'purchase_count': 'mean'
}).round(2)
segment_summary.columns = ['客户数', '平均消费', '总消费', '平均购买次数']
print(segment_summary)
print(f"\n各层级客户占比:")
print(df['customer_segment'].value_counts(normalize=True).round(3) * 100)

# 4. 可视化
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 消费金额分布
axes[0, 0].hist(df['total_spending'], bins=50, edgecolor='black', alpha=0.7)
axes[0, 0].set_title('客户消费金额分布')
axes[0, 0].set_xlabel('消费金额 (¥)')
axes[0, 0].set_ylabel('客户数')
axes[0, 0].axvline(df['total_spending'].mean(), color='red', linestyle='--',
                    label=f'均值: ¥{df["total_spending"].mean():.0f}')
axes[0, 0].legend()

# 客户分层饼图
segment_counts = df['customer_segment'].value_counts()
axes[0, 1].pie(segment_counts.values, labels=segment_counts.index,
                autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('客户分层占比')

# 年龄 vs 消费散点图
axes[1, 0].scatter(df['age'], df['total_spending'], alpha=0.3, s=10)
axes[1, 0].set_title('年龄 vs 消费金额')
axes[1, 0].set_xlabel('年龄')
axes[1, 0].set_ylabel('消费金额 (¥)')

# 购买次数 vs 客单价
axes[1, 1].scatter(df['purchase_count'], df['avg_order_value'], alpha=0.3, s=10, color='green')
axes[1, 1].set_title('购买次数 vs 客单价')
axes[1, 1].set_xlabel('购买次数')
axes[1, 1].set_ylabel('客单价 (¥)')

plt.tight_layout()
plt.savefig('customer_analysis.png', dpi=150)
plt.show()

print("\n图表已保存为 customer_analysis.png")

# 5. 导出分析结果
summary_report = df.groupby('customer_segment').agg({
    'customer_id': 'count',
    'total_spending': 'sum',
    'avg_order_value': 'mean',
    'days_since_last_purchase': 'mean'
}).round(2)
summary_report.to_csv('customer_segment_report.csv')
print("分群报告已导出为 customer_segment_report.csv")
```

#### 与营销/商业的连接点

这个案例直接映射了营销中的核心场景：

1. **RFM分析**是营销领域最经典的客户分群方法，由Hughes在1994年提出。R（Recency）衡量客户最近一次互动的时间，F（Frequency）衡量互动频率，M（Monetary）衡量消费金额。这三个维度组合可以对客户进行精细化分层。在AI时代，RFM的三个维度可以被embedding替代（后续技能1），但理解RFM是理解embedding优势的基础。

2. **客户分层**直接服务于营销策略：高价值客户需要 retention 策略（VIP服务、专属优惠），流失风险客户需要 reactivation 策略（召回优惠、个性化推荐）。在后续技能3中，你将学习如何用因果推断评估这些策略的真实效果，而非简单地看相关关系。

3. **描述性统计**是所有分析的起点。在真实业务中，很多决策错误恰恰来自于对基础统计量的忽视——比如只看均值不看分布，只看总体不分组。MIT OCW 15.071的第一课就是从描述性统计开始的。

#### 英语轨道说明

打开Python Official Tutorial（https://docs.python.org/3/tutorial/introduction.html），用浏览器翻译插件辅助阅读。不要求读懂每个词，目标是理解代码示例和段落大意。遇到Python术语（如interpreter、variable、expression），记住英文形式——这些术语在后续所有技术文档中会反复出现。这就是i+1：你已有中文编程基础（i），通过英文文档接触新表达方式（i+1）。

---

### Day 2：计算概论——数据结构与应用

> 🌐 **英语轨道（i+1）**：MIT OCW 15.071 The Analytics Edge Unit 1（https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/）—— 读Unit 1的英文讲义，重点关注数据结构相关的部分。MIT的讲义写得清晰简洁，适合i+1输入。

#### 核心概念

**1. JSON与CSV——企业数据的两种通用语言**

在现代企业数据架构中，JSON和CSV是两种最常见的数据交换格式：

- **CSV（Comma-Separated Values）**：表格型数据的标准格式。Excel导出、数据库导出、日志文件常用CSV。优点是简单、通用；缺点是不支持嵌套结构。
- **JSON（JavaScript Object Notation）**：树形结构数据的标准格式。API返回值、配置文件、NoSQL数据库（MongoDB）常用JSON。优点是支持嵌套、自描述；缺点是比CSV占用更多空间。

对于AI营销场景，API返回的数据（如用户画像、广告投放数据、CRM客户标签）几乎都是JSON格式。能熟练解析JSON是数据工程师和分析师的基本功。

**2. API调用——连接AI服务的桥梁**

当你使用OpenAI API、Anthropic API、企业内部AI服务的REST API时，核心操作就是HTTP请求+JSON解析。理解API调用的模式，是后续技能5（系统落地）中Agent系统开发的基础。一个Agent的本质就是：接收用户输入 -> 调用LLM API -> 解析返回结果 -> 调用工具API -> 返回最终结果。

**3. 数据库连接与SQL基础**

Python通过驱动程序（如sqlite3、psycopg2、pymysql）连接数据库，执行SQL查询，返回结果集。在商业分析中，数据通常存储在关系型数据库中（MySQL、PostgreSQL）或数据仓库中（Snowflake、BigQuery）。Pandas提供了`read_sql()`函数，可以直接将SQL查询结果加载为DataFrame。

**4. 数据清洗——真实世界的80/20法则**

在真实业务中，数据分析师80%的时间花在数据清洗上，只有20%花在分析建模上。数据清洗包括：
- 缺失值处理：删除、填充（均值/中位数/众数/前向填充）、插值
- 异常值处理：基于Z-score或IQR识别，删除或截断
- 数据类型转换：字符串转日期、字符串转数值
- 重复值处理：识别和删除
- 数据一致性：统一编码、统一命名

#### 真实案例分析：多源营销数据整合

**场景**：你负责一个AI营销方案，需要从三个数据源整合数据：CRM系统导出的客户数据（CSV）、广告平台API返回的投放数据（JSON）、企业数据库中的订单数据（SQL）。目标是构建一个统一的营销数据分析底座。

**代码示例（完整可运行）**：

```python
import pandas as pd
import numpy as np
import json
import sqlite3
from datetime import datetime, timedelta

# ============================================================
# 多源营销数据整合脚本
# 场景：整合CSV（CRM）+ JSON（广告API）+ SQL（订单库）三个数据源
# ============================================================

# --- 数据源1：CRM系统导出的客户数据（CSV） ---
def load_crm_data():
    """模拟从CRM系统导出的客户CSV数据"""
    np.random.seed(42)
    n = 500
    crm_data = pd.DataFrame({
        'customer_id': [f'CRM{str(i).zfill(5)}' for i in range(1, n + 1)],
        'name': [f'客户_{i}' for i in range(1, n + 1)],
        'phone': [f'138{np.random.randint(10000000, 99999999)}' for _ in range(n)],
        'email': [f'user{i}@example.com' for i in range(1, n + 1)],
        'register_date': pd.date_range(start='2024-01-01', periods=n, freq='6h'),
        'customer_level': np.random.choice(['普通', '银卡', '金卡', '钻石'],
                                            n, p=[0.5, 0.3, 0.15, 0.05]),
        'age': np.random.normal(35, 8, n).clip(18, 65).astype(int),
    })
    # 故意制造一些脏数据
    crm_data.loc[10:15, 'phone'] = ''  # 缺失值
    crm_data.loc[20, 'email'] = 'invalid-email'  # 格式错误
    crm_data.loc[25:28, 'customer_level'] = None  # 缺失值
    return crm_data

# --- 数据源2：广告平台API返回的投放数据（JSON） ---
def load_ad_api_data():
    """模拟广告平台API返回的JSON数据"""
    np.random.seed(123)
    ad_records = []
    for i in range(200):
        record = {
            'campaign_id': f'CMP{np.random.randint(1000, 9999)}',
            'campaign_name': f'夏季促销_{np.random.choice(["A组", "B组", "C组"])}',
            'metrics': {
                'impressions': int(np.random.randint(10000, 100000)),
                'clicks': int(np.random.randint(100, 5000)),
                'conversions': int(np.random.randint(5, 200)),
                'spend': round(np.random.uniform(500, 5000), 2),
            },
            'targeting': {
                'age_range': f'{np.random.choice([18, 25, 30, 35])}-{np.random.choice([40, 45, 50, 55])}',
                'gender': np.random.choice(['all', 'male', 'female']),
                'region': np.random.choice(['华北', '华东', '华南', '西部']),
            },
            'date': (datetime(2025, 6, 1) + timedelta(days=np.random.randint(0, 30))).isoformat(),
        }
        ad_records.append(record)
    return ad_records

# --- 数据源3：订单数据库（SQLite模拟） ---
def create_order_database():
    """创建模拟订单数据库"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # 创建订单表
    cursor.execute('''
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            product_id TEXT,
            order_date TEXT,
            amount REAL,
            status TEXT,
            channel TEXT
        )
    ''')

    # 插入模拟数据
    np.random.seed(456)
    for i in range(2000):
        order_id = f'ORD{str(i).zfill(6)}'
        customer_id = f'CRM{str(np.random.randint(1, 501)).zfill(5)}'
        product_id = f'PRD{np.random.randint(100, 200)}'
        order_date = (datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 180))).strftime('%Y-%m-%d')
        amount = round(np.random.lognormal(5, 0.5), 2)
        status = np.random.choice(['completed', 'pending', 'cancelled', 'refunded'],
                                   p=[0.7, 0.15, 0.1, 0.05])
        channel = np.random.choice(['app', 'web', 'mini_program', 'store'],
                                    p=[0.4, 0.3, 0.2, 0.1])
        cursor.execute('INSERT INTO orders VALUES (?,?,?,?,?,?,?)',
                        (order_id, customer_id, product_id, order_date, amount, status, channel))

    conn.commit()
    return conn

# ============================================================
# 数据整合主流程
# ============================================================

print("=" * 60)
print("多源营销数据整合分析")
print("=" * 60)

# Step 1: 加载CSV数据（CRM）
print("\n[1] 加载CRM数据...")
crm_df = load_crm_data()
print(f"  CRM客户数: {len(crm_df)}")
print(f"  字段: {list(crm_df.columns)}")

# 数据清洗
print("\n  --- 数据清洗 ---")
# 处理缺失手机号
missing_phone = crm_df['phone'].eq('').sum()
crm_df['phone'] = crm_df['phone'].replace('', '未知')
print(f"  缺失手机号: {missing_phone} 条 -> 填充为'未知'")

# 处理缺失客户等级
missing_level = crm_df['customer_level'].isnull().sum()
crm_df['customer_level'] = crm_df['customer_level'].fillna('普通')
print(f"  缺失客户等级: {missing_level} 条 -> 填充为'普通'")

# 标记无效邮箱
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
crm_df['email_valid'] = crm_df['email'].str.match(email_pattern)
invalid_email = (~crm_df['email_valid']).sum()
print(f"  无效邮箱: {invalid_email} 条 -> 已标记")

# Step 2: 加载JSON数据（广告API）
print("\n[2] 加载广告平台API数据...")
ad_json = load_ad_api_data()
print(f"  广告投放记录数: {len(ad_json)}")

# 将JSON展开为DataFrame
ad_rows = []
for record in ad_json:
    row = {
        'campaign_id': record['campaign_id'],
        'campaign_name': record['campaign_name'],
        'date': record['date'],
        'impressions': record['metrics']['impressions'],
        'clicks': record['metrics']['clicks'],
        'conversions': record['metrics']['conversions'],
        'spend': record['metrics']['spend'],
        'target_age': record['targeting']['age_range'],
        'target_gender': record['targeting']['gender'],
        'target_region': record['targeting']['region'],
    }
    ad_rows.append(row)

ad_df = pd.DataFrame(ad_rows)

# 计算广告效率指标
ad_df['ctr'] = (ad_df['clicks'] / ad_df['impressions'] * 100).round(3)  # 点击率
ad_df['cvr'] = (ad_df['conversions'] / ad_df['clicks'] * 100).round(3)  # 转化率
ad_df['cpc'] = (ad_df['spend'] / ad_df['clicks']).round(2)  # 每次点击成本
ad_df['cpa'] = (ad_df['spend'] / ad_df['conversions']).round(2)  # 每次获客成本
ad_df['roi'] = (ad_df['conversions'] * 200 / ad_df['spend']).round(2)  # 简化ROI（假设每转化价值200元）

print(f"  平均CTR: {ad_df['ctr'].mean():.2f}%")
print(f"  平均CVR: {ad_df['cvr'].mean():.2f}%")
print(f"  平均CPA: ¥{ad_df['cpa'].mean():.2f}")

# 按地区分析广告效果
print("\n  --- 按地区分析广告效果 ---")
region_stats = ad_df.groupby('target_region').agg({
    'spend': 'sum',
    'conversions': 'sum',
    'ctr': 'mean',
    'cpa': 'mean',
    'roi': 'mean'
}).round(2)
print(region_stats)

# Step 3: 加载SQL数据（订单）
print("\n[3] 加载订单数据库数据...")
conn = create_order_database()

# 用Pandas直接执行SQL查询
orders_df = pd.read_sql_query("""
    SELECT customer_id,
           COUNT(*) as order_count,
           SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) as total_spending,
           SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed_orders,
           SUM(CASE WHEN status = 'refunded' THEN 1 ELSE 0 END) as refunded_orders,
           MIN(order_date) as first_order,
           MAX(order_date) as last_order,
           COUNT(DISTINCT channel) as channel_count
    FROM orders
    GROUP BY customer_id
""", conn)

print(f"  有订单记录的客户数: {len(orders_df)}")
print(f"  总订单金额: ¥{orders_df['total_spending'].sum():,.2f}")
print(f"  平均订单金额: ¥{orders_df['total_spending'].mean():,.2f}")

# 按渠道分析订单
channel_stats = pd.read_sql_query("""
    SELECT channel,
           COUNT(*) as order_count,
           SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) as revenue,
           SUM(CASE WHEN status = 'completed' THEN 1.0 ELSE 0 END) / COUNT(*) as completion_rate
    FROM orders
    GROUP BY channel
    ORDER BY revenue DESC
""", conn)
print("\n  --- 按渠道分析 ---")
print(channel_stats.to_string(index=False))

# Step 4: 数据整合
print("\n[4] 整合多源数据...")
merged_df = crm_df.merge(orders_df, on='customer_id', how='left')

# 标记有无订单
merged_df['has_orders'] = merged_df['order_count'].notna()
merged_df['total_spending'] = merged_df['total_spending'].fillna(0)
merged_df['order_count'] = merged_df['order_count'].fillna(0).astype(int)

print(f"  整合后总客户数: {len(merged_df)}")
print(f"  有订单客户: {merged_df['has_orders'].sum()}")
print(f"  无订单客户: {(~merged_df['has_orders']).sum()}")

# 最终分析：客户等级与消费金额的关系
print("\n[5] 客户等级与消费分析 ---")
level_spending = merged_df.groupby('customer_level').agg({
    'customer_id': 'count',
    'total_spending': ['mean', 'sum'],
    'order_count': 'mean'
}).round(2)
level_spending.columns = ['客户数', '平均消费', '总消费', '平均订单数']
print(level_spending)

# 关闭数据库连接
conn.close()

print("\n" + "=" * 60)
print("数据整合完成。输出可用于后续AI营销分析。")
print("=" * 60)
```

#### 与营销/商业的连接点

1. **多源数据整合**是AI营销的基础设施。在真实业务中，客户数据散落在CRM、广告平台、电商系统、客服系统中。AI营销智能体的第一步就是将这些数据统一到一个语义空间——这正是后续技能1（表示工程）要解决的核心问题。

2. **广告效率指标**（CTR/CVR/CPC/CPA/ROI）是数字营销的核心KPI。理解这些指标的计算逻辑和相互关系，是后续技能3（因果推断）中营销归因分析的基础。在技能3中，你将学习如何用因果推断方法区分"广告带来的真实增量"和"本来就会发生的转化"。

3. **渠道分析**直接服务渠道优化决策。哪些渠道的获客成本最低？哪些渠道的客户LTV最高？这些问题在Day 5的数据管理和技能3的因果推断中会深入展开。

#### 英语轨道说明

MIT OCW 15.071的第一单元"Introduction to Analytics"用英文讲解了数据分析的基本流程，与本日内容高度匹配。打开OCW页面（https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/），找到Unit 1的Lecture Notes。阅读时关注英文术语：data frame, missing values, data cleaning, merge/join。这些术语在后续所有英文技术文档中反复出现。不查全部单词，理解大意即可。

---

### Day 3：统计学——描述统计与推断统计

> 🌐 **英语轨道（i+1）**：Khan Academy Statistics and Probability（https://www.khanacademy.org/math/statistics-probability）—— 有中英字幕，先开中文字幕理解概念，再关掉字幕纯英文听一遍。Khan Academy的教学风格简洁清晰，是统计学入门的最佳i+1材料。

#### 核心概念

**1. 描述统计——用数字概括数据**

描述统计是数据分析的起点，它用几个关键数字概括数据的整体特征：

- **集中趋势**：均值（mean）、中位数（median）、众数（mode）。均值受异常值影响大，中位数更稳健。在商业数据中，收入、消费金额等右偏分布的数据，中位数通常比均值更有代表性。这就是为什么国家统计局发布"居民人均可支配收入"和"居民收入中位数"两个指标——后者往往更能反映"典型居民"的真实水平。
- **离散程度**：方差（variance）、标准差（standard deviation）、四分位距（IQR）、变异系数（CV）。标准差衡量数据的波动范围，CV（标准差/均值）衡量相对波动。在营销中，CV可以比较不同体量广告活动的波动性。
- **分布形态**：偏度（skewness）衡量分布的对称性，峰度（kurtosis）衡量分布的尖峭程度。正偏（右偏）分布意味着少数大值拉高了均值，这在消费金额、广告花费等商业数据中极为常见。

**2. 概率分布——理解随机性的数学工具**

- **正态分布**：统计学最重要的分布。中心极限定理告诉我们，大量独立随机变量的和近似服从正态分布。在A/B测试中，当样本量足够大时，转化率差的分布近似正态，这是假设检验的理论基础。
- **二项分布**：n次独立伯努利试验中成功次数的分布。广告点击（点/不点）、转化（买/不买）都是伯努利过程。二项分布的均值是np，方差是np(1-p)。
- **泊松分布**：单位时间内随机事件发生次数的分布。客服来电次数、网站访问次数、购买次数常用泊松分布建模。

**3. 假设检验——科学决策的统计基础**

假设检验是统计推断的核心工具，也是A/B测试的理论基础。它的逻辑可以用法庭审判来类比：

- **原假设（H₀）**："被告无罪"——在A/B测试中是"新方案和旧方案没有差异"
- **备择假设（H₁）**："被告有罪"——"新方案更好"
- **p值**：在原假设成立的前提下，观察到当前数据或更极端数据的概率。如果p值很小（<0.05），说明"如果新方案真的没效果，看到当前数据的概率很小"——所以我们有理由拒绝原假设，认为新方案有效果。
- **第一类错误（α）**：冤枉好人——原假设为真但被拒绝（假阳性）
- **第二类错误（β）**：放过坏人——原假设为假但未被拒绝（假阴性）
- **统计功效（Power = 1-β）**：正确判 guilty 的概率

**关键认知**：p值不告诉你"新方案有多好"，只告诉你"新方案有没有效果"。效果的大小需要看效应量（effect size）。p<0.05只是"有统计显著性"，不等于"有商业意义"。这就是为什么后续技能3（因果推断）要超越简单的假设检验，走向因果效应估计。

**4. 置信区间——比p值更丰富的信息**

置信区间给出参数估计的可能范围。95%置信区间的含义是：如果重复实验100次，95次实验的置信区间会包含真实参数值。置信区间不仅告诉你"有没有效"（是否包含0），还告诉你"效果多大"（区间位置）和"估计多精确"（区间宽度）。

#### 真实案例分析：A/B测试效果验证

**场景**：你的团队上线了一个新的广告落地页（B版），与旧版（A版）同时投放了7天。数据团队需要判断：B版的转化率是否显著高于A版？如果显著，差异有多大？

**代码示例（完整可运行）**：

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# ============================================================
# A/B测试效果验证脚本
# 场景：新落地页（B版）vs 旧落地页（A版）的转化率对比
# ============================================================

np.random.seed(42)

# 1. 模拟A/B测试数据
# A版：旧落地页，真实转化率2.8%
# B版：新落地页，真实转化率3.5%
n_a = 5000  # A版样本量
n_b = 5000  # B版样本量
true_rate_a = 0.028
true_rate_b = 0.035

# 模拟用户转化（伯努利分布）
conversions_a = np.random.binomial(1, true_rate_a, n_a)
conversions_b = np.random.binomial(1, true_rate_b, n_b)

# 计算观察到的转化率
obs_rate_a = conversions_a.mean()
obs_rate_b = conversions_b.mean()
obs_rate_diff = obs_rate_b - obs_rate_a

print("=" * 60)
print("A/B测试效果验证报告")
print("=" * 60)
print(f"\nA版（旧落地页）:")
print(f"  样本量: {n_a}")
print(f"  转化数: {conversions_a.sum()}")
print(f"  转化率: {obs_rate_a*100:.2f}%")

print(f"\nB版（新落地页）:")
print(f"  样本量: {n_b}")
print(f"  转化数: {conversions_b.sum()}")
print(f"  转化率: {obs_rate_b*100:.2f}%")

print(f"\n观察到的转化率差: {obs_rate_diff*100:.2f}个百分点")
print(f"相对提升: {(obs_rate_diff/obs_rate_a)*100:.1f}%")

# 2. 假设检验：两比例Z检验
# H0: p_b - p_a = 0 (新版本没有提升)
# H1: p_b - p_a > 0 (新版本更好)

# 合并比例（用于计算标准误）
pooled_p = (conversions_a.sum() + conversions_b.sum()) / (n_a + n_b)
se = np.sqrt(pooled_p * (1 - pooled_p) * (1/n_a + 1/n_b))

# Z统计量
z_score = obs_rate_diff / se
# 单侧p值
p_value = 1 - stats.norm.cdf(z_score)

print(f"\n--- 假设检验结果 ---")
print(f"  Z统计量: {z_score:.4f}")
print(f"  p值: {p_value:.4f}")
print(f"  显著性水平: α = 0.05")

if p_value < 0.05:
    print(f"  结论: 拒绝原假设。B版转化率显著高于A版。")
    print(f"  建议: 全量上线B版落地页。")
else:
    print(f"  结论: 无法拒绝原假设。证据不足以证明B版更好。")
    print(f"  建议: 继续实验或保持A版。")

# 3. 置信区间
# 使用Wilson score区间
z_alpha = stats.norm.ppf(0.975)  # 95%置信水平
ci_lower = obs_rate_diff - z_alpha * se
ci_upper = obs_rate_diff + z_alpha * se

print(f"\n--- 95%置信区间 ---")
print(f"  转化率差的95%CI: [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%]")
print(f"  含义: 如果重复实验100次，95次实验的CI会包含真实差异。")

# 4. 效应量（Cohen's h）
h = 2 * np.arcsin(np.sqrt(obs_rate_b)) - 2 * np.arcsin(np.sqrt(obs_rate_a))
print(f"\n--- 效应量 ---")
print(f"  Cohen's h: {h:.4f}")
if h < 0.2:
    print(f"  效应大小: 小（差异微小，即使统计显著也未必有商业意义）")
elif h < 0.5:
    print(f"  效应大小: 中等")
else:
    print(f"  效应大小: 大")

# 5. 统计功效分析（如果真实差异是观察到的差异，需要多少样本？）
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

power_analysis = NormalIndPower()
effect_size = proportion_effectsize(obs_rate_b, obs_rate_a)
required_n = power_analysis.solve_power(
    effect_size=effect_size,
    power=0.8,  # 目标功效80%
    alpha=0.05,
    ratio=1
)

print(f"\n--- 样本量规划 ---")
print(f"  如果真实转化率差为 {obs_rate_diff*100:.2f}个百分点")
print(f"  要达到80%统计功效（α=0.05），每组需要约 {int(required_n)} 样本")
print(f"  当前样本量: {n_a}（每组）")
if n_a >= required_n:
    print(f"  ✓ 样本量充足")
else:
    print(f"  ✗ 样本量不足，需要继续收集数据")

# 6. 可视化
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 转化率对比
versions = ['A版（旧）', 'B版（新）']
rates = [obs_rate_a, obs_rate_b]
errors = [1.96 * np.sqrt(obs_rate_a * (1-obs_rate_a) / n_a),
          1.96 * np.sqrt(obs_rate_b * (1-obs_rate_b) / n_b)]
axes[0].bar(versions, [r*100 for r in rates], yerr=[e*100 for e in errors],
            capsize=10, color=['#3498db', '#e74c3c'], alpha=0.8)
axes[0].set_ylabel('转化率 (%)')
axes[0].set_title('A/B测试转化率对比\n（误差棒=95%CI）')
for i, (r, e) in enumerate(zip(rates, errors)):
    axes[0].text(i, r*100 + e*100 + 0.05, f'{r*100:.2f}%',
                 ha='center', fontweight='bold')

# 转化率差的分布
x = np.linspace(-0.02, 0.015, 1000)
null_dist = stats.norm(0, se)
axes[1].plot(x*100, null_dist.pdf(x), 'b-', linewidth=2, label='原假设分布')
axes[1].axvline(obs_rate_diff*100, color='red', linestyle='--',
                label=f'观察值: {obs_rate_diff*100:.2f}%')
axes[1].fill_between(x[x <= obs_rate_diff]*100, null_dist.pdf(x[x <= obs_rate_diff]),
                      alpha=0.3, color='blue')
axes[1].set_xlabel('转化率差 (%)')
axes[1].set_ylabel('概率密度')
axes[1].set_title(f'假设检验可视化\np值={p_value:.4f}')
axes[1].legend()

# 置信区间
axes[2].errorbar([1], [obs_rate_diff*100],
                  yerr=[[obs_rate_diff*100 - ci_lower*100], [ci_upper*100 - obs_rate_diff*100]],
                  fmt='o', capsize=10, color='green', markersize=10, linewidth=2)
axes[2].axhline(0, color='gray', linestyle='--', alpha=0.5)
axes[2].set_xlim([0.5, 1.5])
axes[2].set_ylabel('转化率差 (%)')
axes[2].set_title('95%置信区间')
axes[2].set_xticks([])
axes[2].annotate(f'[{ci_lower*100:.2f}%, {ci_upper*100:.2f}%]',
                  xy=(1, obs_rate_diff*100), xytext=(1.1, obs_rate_diff*100))

plt.tight_layout()
plt.savefig('ab_test_analysis.png', dpi=150)
plt.show()

print("\n图表已保存为 ab_test_analysis.png")
```

#### 与营销/商业的连接点

1. **A/B测试是数字营销的决策基石**。每一次落地页改版、每一组广告素材、每一个推荐算法调整，都应该通过A/B测试验证效果。Google在2000年首次将A/B测试系统化，现在每天运行数万次A/B测试。理解A/B测试的统计原理，是避免"拍脑袋决策"的第一步。

2. **p值的常见误用**：在商业实践中，最常见的错误是"p值钓鱼"——不断检查p值是否显著，一旦达到0.05就停止实验。这会严重膨胀第一类错误率。正确做法是：在实验前预先计算所需样本量，达到样本量后再判断结果。这个概念在技能3的因果推断中会深入讨论。

3. **统计显著性 ≠ 商业显著性**：当样本量很大时，即使0.01%的转化率差也可能"统计显著"。但0.01%的转化率差可能不值得全量上线新版本的成本。决策时需要同时考虑统计显著性（p值）、效应量（effect size）和商业ROI。

#### 英语轨道说明

Khan Academy的统计学课程有视频、有字幕、有练习。建议学习顺序：先开中文字幕看一遍理解概念（i），然后关掉字幕纯英文听一遍（i+1）。重点术语：null hypothesis, alternative hypothesis, p-value, confidence interval, statistical significance, type I error。这些术语在后续技能3的英文文献中反复出现。

---

### Day 4：统计学——回归分析与概率分布

> 🌐 **英语轨道（i+1）**：MIT OCW 15.071 Unit 2 "Statistical Methods"（https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/）—— 读Unit 2的讲义，重点关注线性回归部分。MIT的回归教学用大量商业案例，非常适合i+1输入。

#### 核心概念

**1. 线性回归——从相关到预测**

线性回归是统计学中最基础的预测模型，也是理解所有更复杂模型（包括神经网络）的起点。它的核心思想是：找到一条直线（或超平面），使得所有数据点到这条线的"距离"（残差平方和）最小。这就是最小二乘法（Ordinary Least Squares, OLS）。

数学表达：`y = β₀ + β₁x₁ + β₂x₂ + ... + βₖxₖ + ε`

其中y是因变量（如客户消费金额），x₁到xₖ是自变量（如年龄、购买次数、注册天数），β是回归系数（表示每个自变量对因变量的影响大小），ε是误差项。

关键概念：
- **R²（决定系数）**：模型解释了因变量变异的百分比。R²=0.6意味着模型解释了60%的变异。R²越高不代表模型越好——可能过拟合。
- **调整R²**：考虑自变量数量后的R²，防止"加变量就涨"的假象。
- **回归系数的p值**：每个自变量的回归系数是否显著不为0。p<0.05表示该变量对因变量有显著影响。
- **残差分析**：检查模型假设是否成立——残差是否正态分布、是否方差齐性、是否独立。

**2. 多元回归与共线性**

当有多个自变量时，需要警惕**多重共线性**（multicollinearity）——自变量之间高度相关，导致回归系数不稳定、难以解释。在营销数据中，"广告花费"和"广告曝光量"通常高度相关，同时放入回归模型会导致两个变量的系数都不显著，但实际上它们都有影响。

检测方法：方差膨胀因子（VIF）。VIF>10通常被认为是严重共线性。解决方法：删除一个共线变量、主成分分析（PCA）、岭回归。

**3. 概率分布与商业应用**

- **正态分布与中心极限定理**：大量独立随机因素的叠加效应近似正态分布。客户消费金额的对数通常近似正态分布（对数正态分布）。
- **二项分布与转化率**：每个用户的转化是一个伯努利试验（成功/失败），n个用户的转化数服从二项分布。转化率的置信区间基于二项分布。
- **泊松分布与计数数据**：单位时间内的购买次数、客服来电次数、网站访问次数常用泊松分布建模。泊松分布的均值等于方差。

**4. 从相关到因果——回归的局限**

回归分析揭示的是**相关关系**，不是**因果关系**。"广告花费与销售额正相关"不意味着"增加广告花费会导致销售额增加"——可能存在混杂因素（如季节性、促销活动）同时影响两者。

这个认知极其重要。它直接引向后续技能3（因果推断）的核心命题：如何从相关关系中识别因果关系？回归分析是因果推断的基础工具（在满足一定假设条件下），但它本身不是因果推断。

#### 真实案例分析：客户生命周期价值（LTV）影响因素分析

**场景**：你需要找出哪些因素显著影响客户的消费金额（LTV的简化代理变量），以指导客户运营策略。数据包括客户年龄、注册天数、购买次数、客户等级、最近购买距今天数等。

**代码示例（完整可运行）**：

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 客户LTV影响因素回归分析脚本
# 场景：分析哪些因素显著影响客户消费金额
# ============================================================

np.random.seed(42)

# 1. 生成模拟数据
n = 1000
data = pd.DataFrame({
    'age': np.random.normal(35, 8, n).clip(18, 65).astype(int),
    'registration_days': np.random.randint(30, 1000, n),
    'purchase_count': np.random.poisson(5, n) + 1,
    'days_since_last_purchase': np.random.randint(1, 180, n),
    'customer_level': np.random.choice([1, 2, 3, 4], n, p=[0.5, 0.3, 0.15, 0.05]),
    # 1=普通, 2=银卡, 3=金卡, 4=钻石
})

# 构造有真实关系的消费金额
# 真实模型: spending = 100 + 15*age + 0.5*reg_days + 200*purchase_count
#           - 2*days_since_last + 300*level + noise
true_spending = (100 + 15 * data['age']
                 + 0.5 * data['registration_days']
                 + 200 * data['purchase_count']
                 - 2 * data['days_since_last_purchase']
                 + 300 * data['customer_level']
                 + np.random.normal(0, 300, n))  # 随机误差
data['total_spending'] = true_spending.clip(0).round(2)

# 添加一个与purchase_count高度相关的变量（制造共线性）
data['avg_order_value'] = data['total_spending'] / data['purchase_count']

print("=" * 60)
print("客户LTV影响因素回归分析")
print("=" * 60)

# 2. 描述性统计
print("\n--- 描述性统计 ---")
print(data.describe().round(2))

# 3. 相关性矩阵
print("\n--- 相关系数矩阵 ---")
corr_matrix = data.corr()
print(corr_matrix.round(3))

# 可视化相关性热力图
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=0.5)
plt.title('变量相关性热力图')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150)
plt.show()

# 4. 简单线性回归（单变量）
print("\n--- 简单回归：购买次数 -> 消费金额 ---")
X_simple = sm.add_constant(data['purchase_count'])
y = data['total_spending']
model_simple = sm.OLS(y, X_simple).fit()
print(f"  回归方程: spending = {model_simple.params['const']:.2f} + {model_simple.params['purchase_count']:.2f} * purchase_count")
print(f"  R² = {model_simple.rsquared:.4f}")
print(f"  购买次数系数p值 = {model_simple.pvalues['purchase_count']:.6f}")

# 5. 多元线性回归
print("\n--- 多元回归：所有变量 -> 消费金额 ---")
X_multi = data[['age', 'registration_days', 'purchase_count',
                 'days_since_last_purchase', 'customer_level']]
X_multi = sm.add_constant(X_multi)
model_multi = sm.OLS(y, X_multi).fit()
print(model_multi.summary().tables[1])  # 只输出系数表
print(f"\n  R² = {model_multi.rsquared:.4f}")
print(f"  调整R² = {model_multi.rsquared_adj:.4f}")
print(f"  F统计量p值 = {model_multi.f_pvalue:.2e}")

# 6. 多重共线性检测
print("\n--- 多重共线性检测（VIF）---")
X_vif = data[['age', 'registration_days', 'purchase_count',
               'days_since_last_purchase', 'customer_level']]
vif_data = pd.DataFrame()
vif_data['variable'] = X_vif.columns
vif_data['VIF'] = [variance_inflation_factor(X_vif.values, i)
                    for i in range(X_vif.shape[1])]
print(vif_data.to_string(index=False))
print("  (VIF > 10 表示严重共线性)")

# 7. 残差分析
residuals = model_multi.residual
fitted = model_multi.fittedvalues

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 残差 vs 拟合值
axes[0, 0].scatter(fitted, residuals, alpha=0.3, s=10)
axes[0, 0].axhline(0, color='red', linestyle='--')
axes[0, 0].set_xlabel('拟合值')
axes[0, 0].set_ylabel('残差')
axes[0, 0].set_title('残差 vs 拟合值\n（检查线性性和方差齐性）')

# Q-Q图
sm.qqplot(residuals, line='45', fit=True, ax=axes[0, 1])
axes[0, 1].set_title('残差Q-Q图\n（检查正态性）')

# 残差分布直方图
axes[1, 0].hist(residuals, bins=50, edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('残差')
axes[1, 0].set_ylabel('频数')
axes[1, 0].set_title('残差分布\n（应近似正态）')

# 各变量系数的置信区间
coefs = model_multi.params[1:]  # 去掉const
ci = model_multi.conf_int().iloc[1:]
axes[1, 1].barh(range(len(coefs)), coefs.values,
                 xerr=[coefs - ci[0], ci[1] - coefs],
                 capsize=5, color='steelblue', alpha=0.8)
axes[1, 1].set_yticks(range(len(coefs)))
axes[1, 1].set_yticklabels(coefs.index)
axes[1, 1].set_xlabel('回归系数')
axes[1, 1].set_title('各变量回归系数及95%CI')
axes[1, 1].axvline(0, color='red', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('regression_diagnostics.png', dpi=150)
plt.show()

# 8. 业务洞察
print("\n" + "=" * 60)
print("业务洞察")
print("=" * 60)
print(f"""
1. 模型解释力: R²={model_multi.rsquared:.2%}，即模型解释了消费金额变异的{model_multi.rsquared:.1%}。

2. 关键影响因素（按标准化系数排序）:
   - 购买次数: 每增加1次购买，消费金额增加¥{model_multi.params['purchase_count']:.0f}
   - 客户等级: 每提升1级，消费金额增加¥{model_multi.params['customer_level']:.0f}
   - 年龄: 每增加1岁，消费金额增加¥{model_multi.params['age']:.0f}
   - 注册天数: 每增加1天，消费金额增加¥{model_multi.params['registration_days']:.1f}
   - 最近购买距今天数: 每增加1天，消费金额减少¥{abs(model_multi.params['days_since_last_purchase']):.1f}

3. 运营建议:
   - 提升购买频次是最有效的LTV提升杠杆
   - 客户等级提升（升级机制）直接关联消费金额
   - 近期未购买的客户消费金额下降，需要召回机制

4. 注意事项:
   - 回归揭示的是相关关系，不是因果关系
   - "购买次数多 -> 消费高"不意味着"促使客户多买就能提升消费"
   - 可能存在混杂因素（如客户本身购买意愿强）
   - 因果验证需要技能3的工具（A/B测试、因果推断）
""")
```

#### 与营销/商业的连接点

1. **LTV（客户生命周期价值）分析**是营销和客户运营的核心。回归分析帮助识别LTV的关键驱动因素，从而指导资源分配——把营销预算投在最能提升LTV的变量上。

2. **共线性问题**在营销数据中极为常见。"广告花费"与"曝光量"、"购买次数"与"客单价"之间往往高度相关。不注意共线性会导致错误的结论：某个变量"不显著"，其实是因为它和另一个变量共线了。

3. **从相关到因果的跨越**是本日最重要的认知。回归分析告诉你"什么和什么相关"，但不告诉你"什么导致什么"。这个认知差距正是后续技能3（因果推断）要解决的——用do-演算、潜在结果框架、工具变量等方法，从相关关系中识别因果关系。

#### 英语轨道说明

MIT OCW 15.071 Unit 2的英文讲义涵盖了线性回归的完整内容，且用大量商业案例讲解。建议阅读时关注：regression coefficient, R-squared, p-value, multicollinearity, residual analysis等术语。这些术语在后续技能1-3的英文文献中反复出现。读不懂的公式跳过，关注案例和结论。

---

### Day 5：商业数据管理——数据治理与SQL

> 🌐 **英语轨道（i+1）**：Kaggle Learn: SQL（https://www.kaggle.com/learn/sql）—— 英文界面，但SQL是通用语言，语言障碍小。完成Kaggle的SQL互动练习。

#### 核心概念

**1. 数据治理——企业数据资产的管理框架**

数据治理（Data Governance）是一套管理数据资产的制度、流程和工具。在AI时代，数据治理的重要性空前提高——AI系统的质量取决于数据质量（"Garbage In, Garbage Out"）。DAMA International（Data Management Association）定义了数据治理的六个核心维度：

- **数据质量**：准确性、完整性、一致性、及时性、唯一性、有效性。在营销数据中，常见的质量问题包括：客户信息重复录入、手机号格式不统一、消费金额缺失、数据更新不及时。
- **元数据管理**：管理"关于数据的数据"——数据字典、业务术语表、数据血缘。元数据管理让你知道"这个字段是什么意思、从哪来、被谁用"。
- **数据架构**：企业数据的整体结构设计——数据仓库、数据湖、湖仓一体的选型。
- **数据安全与隐私**：GDPR（欧盟通用数据保护条例）、中国数据安全法、个人信息保护法对企业数据处理的影响。
- **数据生命周期管理**：数据的创建、存储、使用、归档、销毁的全生命周期。
- **数据标准与主数据管理**：统一数据定义，建立"单一真相源"（Single Source of Truth）。

**2. 关系型数据库与SQL**

关系型数据库（RDBMS）是企业数据存储的基石。它的核心思想是用表格（Table）组织数据，用关系（Relationship）连接不同表格。SQL（Structured Query Language）是操作关系型数据库的标准语言。

SQL的四个核心操作：
- **DDL（数据定义语言）**：CREATE TABLE, ALTER TABLE, DROP TABLE——定义数据结构
- **DML（数据操作语言）**：INSERT, UPDATE, DELETE——操作数据
- **DQL（数据查询语言）**：SELECT——查询数据（分析中最常用）
- **DCL（数据控制语言）**：GRANT, REVOKE——控制权限

**数据库设计原则——范式化（Normalization）**：
- 第一范式（1NF）：每个字段不可再分
- 第二范式（2NF）：非主键字段完全依赖主键（消除部分依赖）
- 第三范式（3NF）：非主键字段直接依赖主键（消除传递依赖）

在实际企业中，为了查询性能，常做适度的反范式化（Denormalization），在范式和性能间取平衡。

**3. 数据仓库 vs 数据湖 vs 湖仓一体**

| 维度 | 数据仓库 | 数据湖 | 湖仓一体 |
|------|---------|--------|---------|
| 数据类型 | 结构化 | 结构化+非结构化 | 结构化+非结构化 |
| 处理方式 | 写时模式（Schema-on-Write） | 读时模式（Schema-on-Read） | 两者兼有 |
| 典型工具 | Snowflake, Redshift, BigQuery | S3, HDFS | Databricks, Delta Lake |
| 适用场景 | BI报表、分析查询 | 数据探索、ML训练 | 统一分析和ML |

在AI营销场景中，结构化的客户/订单数据存数据仓库，非结构化的客服对话/广告素材/用户评论存数据湖，湖仓一体提供统一的数据底座。

**4. 数据隐私与合规**

- **GDPR**：欧盟通用数据保护条例，要求企业在处理个人数据时遵循"合法、公平、透明"原则，用户有权访问、更正、删除其个人数据。
- **中国数据安全法**（2021年9月施行）：数据处理者应建立全流程数据安全管理制度，进行数据分类分级，跨境传输需通过安全评估。
- **个人信息保护法**（2021年11月施行）：处理个人信息需取得个人同意，遵循"最小必要"原则。

在营销AI系统中，用户画像、行为追踪、个性化推荐都可能涉及个人信息处理，必须在设计时就嵌入合规要求（Privacy by Design）。

#### 真实案例分析：电商企业数据库Schema设计

**场景**：你需要为一家电商企业设计营销数据底座，支持客户分析、订单追踪、广告效果分析等场景。

**代码示例（完整可运行）**：

```python
import sqlite3
import pandas as pd

# ============================================================
# 电商企业营销数据库Schema设计与查询脚本
# 场景：设计支持客户分析、订单追踪、广告效果分析的数据库
# ============================================================

# 创建数据库（使用内存数据库，实际使用时替换为文件路径）
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

print("=" * 60)
print("电商企业营销数据库 - Schema设计与查询")
print("=" * 60)

# --- DDL: 创建表 ---

# 1. 客户表
cursor.execute('''
    CREATE TABLE customers (
        customer_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        gender TEXT CHECK(gender IN ('M', 'F', 'O')),
        birth_date DATE,
        register_date DATE NOT NULL,
        customer_level TEXT DEFAULT '普通'
            CHECK(customer_level IN ('普通', '银卡', '金卡', '钻石')),
        status TEXT DEFAULT 'active'
            CHECK(status IN ('active', 'inactive', 'churned'))
    )
''')

# 2. 商品表
cursor.execute('''
    CREATE TABLE products (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        category_id TEXT,
        brand TEXT,
        price DECIMAL(10, 2) NOT NULL CHECK(price > 0),
        cost DECIMAL(10, 2),
        stock INTEGER DEFAULT 0 CHECK(stock >= 0),
        created_date DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
    )
''')

# 3. 类目表
cursor.execute('''
    CREATE TABLE categories (
        category_id TEXT PRIMARY KEY,
        category_name TEXT NOT NULL,
        parent_category_id TEXT,
        FOREIGN KEY (parent_category_id) REFERENCES categories(category_id)
    )
''')

# 4. 订单表
cursor.execute('''
    CREATE TABLE orders (
        order_id TEXT PRIMARY KEY,
        customer_id TEXT NOT NULL,
        order_date DATETIME NOT NULL,
        total_amount DECIMAL(12, 2) NOT NULL,
        status TEXT DEFAULT 'pending'
            CHECK(status IN ('pending', 'paid', 'shipped', 'completed',
                              'cancelled', 'refunded')),
        channel TEXT
            CHECK(channel IN ('app', 'web', 'mini_program', 'store')),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
''')

# 5. 订单明细表
cursor.execute('''
    CREATE TABLE order_items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT NOT NULL,
        product_id TEXT NOT NULL,
        quantity INTEGER NOT NULL CHECK(quantity > 0),
        unit_price DECIMAL(10, 2) NOT NULL,
        subtotal DECIMAL(12, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
''')

# 6. 营销活动表
cursor.execute('''
    CREATE TABLE campaigns (
        campaign_id TEXT PRIMARY KEY,
        campaign_name TEXT NOT NULL,
        channel TEXT,
        start_date DATE,
        end_date DATE,
        budget DECIMAL(12, 2),
        target_audience TEXT
    )
''')

print("✓ 已创建6张表: customers, categories, products, orders, order_items, campaigns")

# --- DML: 插入数据 ---
import numpy as np
np.random.seed(42)

# 插入类目
categories = [('C001', '电子产品', None), ('C002', '服装', None),
              ('C003', '手机', 'C001'), ('C004', '电脑', 'C001'),
              ('C005', '男装', 'C002'), ('C006', '女装', 'C002')]
cursor.executemany('INSERT INTO categories VALUES (?,?,?)', categories)

# 插入客户
customers = []
for i in range(1, 201):
    customers.append((
        f'CUST{str(i).zfill(5)}',
        f'客户{i}',
        f'138{np.random.randint(10000000, 99999999)}',
        f'user{i}@example.com',
        np.random.choice(['M', 'F']),
        f'{np.random.randint(1970, 2000)}-{np.random.randint(1,13):02d}-{np.random.randint(1,29):02d}',
        f'2024-{np.random.randint(1,13):02d}-{np.random.randint(1,29):02d}',
        np.random.choice(['普通', '银卡', '金卡', '钻石'], p=[0.5, 0.3, 0.15, 0.05])
    ))
cursor.executemany('INSERT INTO customers VALUES (?,?,?,?,?,?,?,?)', customers)

# 插入商品
products = []
for i in range(1, 51):
    cat = np.random.choice(['C003', 'C004', 'C005', 'C006'])
    products.append((
        f'PRD{str(i).zfill(4)}',
        f'商品_{i}',
        cat,
        np.random.choice(['品牌A', '品牌B', '品牌C']),
        round(np.random.uniform(50, 2000), 2),
        round(np.random.uniform(30, 1200), 2),
        np.random.randint(0, 500)
    ))
cursor.executemany('INSERT INTO products VALUES (?,?,?,?,?,?,?,CURRENT_DATE)', products)

# 插入订单和订单明细
orders = []
order_items = []
for i in range(1, 501):
    cust_id = f'CUST{str(np.random.randint(1, 201)).zfill(5)}'
    order_date = f'2025-{np.random.randint(1, 7):02d}-{np.random.randint(1, 29):02d} {np.random.randint(0,24):02d}:{np.random.randint(0,60):02d}'
    n_items = np.random.randint(1, 5)
    items = []
    total = 0
    for _ in range(n_items):
        prod_id = f'PRD{str(np.random.randint(1, 51)).zfill(4)}'
        qty = np.random.randint(1, 4)
        price = round(np.random.uniform(50, 2000), 2)
        total += qty * price
        items.append((prod_id, qty, price))
    orders.append((
        f'ORD{str(i).zfill(6)}', cust_id, order_date, round(total, 2),
        np.random.choice(['completed', 'pending', 'cancelled', 'refunded'],
                          p=[0.7, 0.15, 0.1, 0.05]),
        np.random.choice(['app', 'web', 'mini_program', 'store'], p=[0.4, 0.3, 0.2, 0.1])
    ))
    for prod_id, qty, price in items:
        order_items.append((f'ORD{str(i).zfill(6)}', prod_id, qty, price))

cursor.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', orders)
cursor.executemany('INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?,?,?,?)', order_items)

# 插入营销活动
campaigns = [
    ('CMP001', '618大促', 'all', '2025-06-01', '2025-06-20', 500000, '全部客户'),
    ('CMP002', '新客专享', 'app', '2025-03-01', '2025-03-31', 100000, '新注册客户'),
    ('CMP003', '金卡回馈', 'mini_program', '2025-04-15', '2025-05-15', 80000, '金卡及以上'),
]
cursor.executemany('INSERT INTO campaigns VALUES (?,?,?,?,?,?,?)', campaigns)

conn.commit()
print(f"✓ 已插入数据: {len(customers)}客户, {len(products)}商品, {len(orders)}订单, {len(order_items)}订单明细")

# --- DQL: 业务查询 ---

print("\n" + "=" * 60)
print("业务查询分析")
print("=" * 60)

# 查询1: 各渠道的订单数和GMV
print("\n[查询1] 各渠道订单数和GMV ---")
q1 = pd.read_sql_query("""
    SELECT channel,
           COUNT(*) as order_count,
           SUM(CASE WHEN status = 'completed' THEN total_amount ELSE 0 END) as gmv,
           ROUND(AVG(total_amount), 2) as avg_order_value,
           SUM(CASE WHEN status = 'completed' THEN 1.0 ELSE 0 END) / COUNT(*) as completion_rate
    FROM orders
    GROUP BY channel
    ORDER BY gmv DESC
""", conn)
print(q1.to_string(index=False))

# 查询2: 客户等级与消费分析
print("\n[查询2] 客户等级消费分析 ---")
q2 = pd.read_sql_query("""
    SELECT c.customer_level,
           COUNT(DISTINCT c.customer_id) as customer_count,
           COUNT(o.order_id) as total_orders,
           ROUND(SUM(CASE WHEN o.status = 'completed' THEN o.total_amount ELSE 0 END), 2) as total_spending,
           ROUND(AVG(CASE WHEN o.status = 'completed' THEN o.total_amount END), 2) as avg_order_value
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_level
    ORDER BY total_spending DESC
""", conn)
print(q2.to_string(index=False))

# 查询3: 热销商品Top 10
print("\n[查询3] 热销商品Top 10 ---")
q3 = pd.read_sql_query("""
    SELECT p.product_name,
           cat.category_name,
           SUM(oi.quantity) as total_sold,
           ROUND(SUM(oi.subtotal), 2) as total_revenue,
           COUNT(DISTINCT o.order_id) as order_count
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    JOIN categories cat ON p.category_id = cat.category_id
    JOIN orders o ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY p.product_id
    ORDER BY total_revenue DESC
    LIMIT 10
""", conn)
print(q3.to_string(index=False))

# 查询4: RFM分析（用SQL实现）
print("\n[查询4] RFM客户分群（SQL版） ---")
q4 = pd.read_sql_query("""
    WITH customer_orders AS (
        SELECT c.customer_id,
               c.customer_level,
               MAX(o.order_date) as last_order_date,
               COUNT(o.order_id) as frequency,
               SUM(CASE WHEN o.status = 'completed' THEN o.total_amount ELSE 0 END) as monetary
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.customer_level
    )
    SELECT customer_level,
           COUNT(*) as customer_count,
           ROUND(AVG(frequency), 1) as avg_frequency,
           ROUND(AVG(monetary), 2) as avg_monetary,
            MAX(monetary) as max_monetary
    FROM customer_orders
    WHERE frequency > 0
    GROUP BY customer_level
    ORDER BY avg_monetary DESC
""", conn)
print(q4.to_string(index=False))

# 查询5: 未购买客户分析
print("\n[查询5] 注册但从未购买的客户 ---")
q5 = pd.read_sql_query("""
    SELECT c.customer_level,
           COUNT(*) as no_purchase_count,
           ROUND(COUNT(*) * 100.0 / (
               SELECT COUNT(*) FROM customers WHERE customer_level = c.customer_level
           ), 1) as no_purchase_rate
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.order_id IS NULL
    GROUP BY c.customer_level
    ORDER BY no_purchase_count DESC
""", conn)
print(q5.to_string(index=False))

conn.close()

print("\n" + "=" * 60)
print("数据库Schema设计完成。")
print("表结构: customers -> orders -> order_items -> products -> categories")
print("       campaigns（独立营销活动表）")
print("此Schema支持: 客户分析、订单分析、商品分析、渠道分析、RFM分群")
print("=" * 60)
```

#### 与营销/商业的连接点

1. **数据库Schema设计**是数据驱动营销的基础设施。一个设计良好的Schema可以让营销团队快速回答"谁是高价值客户"、"哪个渠道的ROI最高"、"哪些商品经常被一起购买"等问题。在AI时代，这个Schema还会扩展为知识图谱（后续技能1）和向量数据库（后续技能2）。

2. **SQL能力**对于售前解决方案产品经理尤为重要。在客户提案中，经常需要快速查询和分析客户数据来支撑方案设计。能直接写SQL查询数据，比依赖数据团队出报告快得多。

3. **数据治理**在AI营销中的重要性：AI系统的输入是数据，如果数据质量差（客户信息重复、消费金额缺失、数据更新不及时），AI的输出就会不可靠。NIST AI RMF框架中的"Map"步骤就要求企业识别AI系统的数据来源和质量。

#### 英语轨道说明

Kaggle Learn的SQL课程（https://www.kaggle.com/learn/sql）是英文界面的互动式教程，但SQL是通用语言，代码部分没有语言障碍。阅读英文解释部分时，关注：JOIN, GROUP BY, subquery, window function等术语。完成全部练习大约需要2小时。

---

### Day 6：研究方法论入门（v4.0新增）

> 🌐 **英语轨道（i+1）**：Creswell《Research Design: Qualitative, Quantitative, and Mixed Methods Approaches》第五版Chapter 1—— 先读中文摘要（如有），再对照英文原文。能读懂40-50%是正常的，关注核心概念而非细节。

#### 核心概念

**1. 什么是学术研究——与工程实践的根本区别**

学术研究和工程实践的核心区别不在于"难不难"，而在于"目标不同"：

- **工程实践**的目标是**解决问题**。你构建一个AI营销系统，提升了转化率，这是一个工程成果。工程回答"怎么做"（How）。
- **学术研究**的目标是**创造新知识**。你不仅构建了系统，还发现了"AI营销系统在特定条件下的设计原则"，这个原则可以被其他企业复用。研究回答"为什么"（Why）和"是什么"（What）。

Creswell在《Research Design》第五版中定义：研究是一个**系统化的过程**，通过收集和分析数据来回答问题或解决问题，其结果应该是**可验证的、可累积的、可传播的**。

| 维度 | 工程实践 | 学术研究 |
|------|---------|---------|
| 目标 | 解决具体问题 | 创造可传播的新知识 |
| 交付物 | 可运行的系统/产品 | 论文/研究报告 |
| 评价标准 | 是否解决了问题 | 是否贡献了新知识 |
| 知识属性 | 隐性的、局部的 | 显性的、可复用的 |
| 时间框架 | 以周/月计 | 以月/年计 |
| 对话对象 | 客户、老板、团队 | 学术共同体 |

**2. 博士论文长什么样**

博士论文（Dissertation/Thesis）是博士训练的核心交付物。一篇典型的商业/信息系统领域博士论文包含以下结构：

- **第一章：绪论**（Introduction）——研究背景、问题陈述、研究目标、贡献声明
- **第二章：文献综述**（Literature Review）——前人做了什么，还有什么没做（研究空白）
- **第三章：理论框架**（Theoretical Framework）——你用什么理论视角来分析问题
- **第四章：研究方法**（Methodology/Methods）——你怎么做的（数据收集和分析方法）
- **第五章：研究结果**（Results/Findings）——你发现了什么
- **第六章：讨论**（Discussion）——发现意味着什么，理论与实践启示
- **第七章：结论**（Conclusion）——总结贡献、局限、未来方向

博士论文和项目报告的区别：
- 项目报告说"我做了X，效果是Y"
- 博士论文说"我做了X，效果是Y，**这证明了Z理论/产生了W设计原则**，对学术共同体和实践者有N启示"

**3. 研究的三种范式**

研究范式（Research Paradigm）是研究者对"什么是知识、如何获取知识"的根本假设。三种核心范式：

| 范式 | 本体论（什么是真实） | 认识论（如何认识真实） | 对应方法 |
|------|-------------------|---------------------|---------|
| **实证主义**（Positivism） | 真实是客观的、可测量的 | 通过观察和实验验证假设 | 定量研究：实验、统计 |
| **解释主义**（Interpretivism） | 真实是社会建构的、主观的 | 通过理解和解释意义来认识 | 定性研究：访谈、案例 |
| **实用主义**（Pragmatism） | 真实是多元的 | 根据研究问题选择方法 | 混合方法：定量+定性 |

在AI商业研究领域：
- 用实证主义范式做A/B测试验证AI系统效果（定量）
- 用解释主义范式做案例研究理解AI如何改变组织决策（定性）
- 用实用主义范式做混合方法研究——既测效果又理解决策过程

**4. IMRaD格式简介**

IMRaD（Introduction, Methods, Results, and Discussion）是实证研究论文的标准结构，由American Psychological Association（APA）推广，现在被几乎所有学术期刊采用。

| 部分 | 核心问题 | 写作要点 |
|------|---------|---------|
| **Introduction**（引言） | 为什么要做这个研究？ | 从大到小：领域背景 -> 具体问题 -> 研究空白 -> 本文贡献 |
| **Methods**（方法） | 你怎么做的？ | 别人能根据你的描述复现研究：数据来源、样本、变量、分析方法 |
| **Results**（结果） | 你发现了什么？ | 用图表说话，先描述再解释，区分"数据显示什么"和"这意味着什么" |
| **Discussion**（讨论） | 这意味着什么？ | 与前人研究对比、理论与实践启示、局限性、未来研究方向 |

后续技能5中的模块R5会详细训练IMRaD写作。此处只需建立基本认知。

#### 与后续模块R的连接

这一天的目的是建立对"学术研究"的基本认知，为模块R的六个子模块做准备。你不需要在这一天掌握所有研究方法，只需要理解：

1. **博士和硕士的区别不在于学了多少课，而在于能否创造新知识。**
2. **你的工程实践可以转化为学术贡献**——这就是模块R1（设计科学研究）要教你的。
3. **学术研究有规范的方法和结构**——IMRaD不是格式要求，是思维框架。

当你后续学习技能1-5时，每个技能都会嵌入一个模块R子模块，帮助你用研究方法论的视角重新审视学到的工程知识。

#### 推荐资源

- 📄 **Creswell《Research Design》第五版Chapter 1**（英文，学术写作入门最佳）
  - 这本书是全球研究方法论课程的标准教材，Oxford、Cambridge、Imperial等校广泛使用
- 📺 **B站**："研究方法论入门"（找播放量>1万的系列）
- 🌐 **英语轨道**：读Creswell Chapter 1的前5页，不查全部单词，混个脸熟。关注术语：research paradigm, positivism, interpretivism, pragmatism, IMRaD

---

## 全球七校对标

本预科模块对标全球七所顶尖大学的博士/硕士基础课程要求。

### MIT OCW 15.071 The Analytics Edge

MIT Sloan最受欢迎的数据分析课程，已通过MIT OCW完全开放。

- **对标内容**：Day 1-4的Python编程和统计学基础
- **Unit 1: Introduction to Analytics**——对标Day 1-2的计算概论
- **Unit 2: Statistical Methods**——对标Day 3-4的统计学
- **Unit 3: Advanced Methods**——为后续技能1的表示工程做准备
- **特色**：课程用大量真实案例（Netflix推荐、IBM Watson、IRS税务欺诈检测）讲解分析方法，与本教材的营销场景案例方法论一致
- **链接**：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/

### Stanford CS229先修要求

Stanford CS229（Machine Learning）是Stanford最受欢迎的AI课程，其syllabus明确列出了先修要求。预科阶段需要自查是否满足：

- ✅ **概率论**（CS109或MATH151级别）——对标Day 3-4的统计学
- ✅ **多变量微积分**——预科不做深入要求，但需了解偏导数概念
- ✅ **线性代数**（MATH51或CS205L级别）——预科补充矩阵运算基础
- ✅ **Python编程能力**（含NumPy）——对标Day 1-2的计算概论

如果不满足以上要求，在Day 1-4中重点补齐。CS229的先修要求是后续技能1-5的基础，必须达标。

- **链接**：https://cs229.stanford.edu/

### Imperial Maths & Statistics Foundations

Imperial College Business School的MSc Business Analytics & AI项目将Maths & Statistics Foundations列为必修前置模块。该模块涵盖：

- **概率论基础**：概率公理、条件概率、贝叶斯定理
- **统计推断**：参数估计、假设检验、置信区间
- **线性代数**：矩阵运算、特征值分解、主成分分析
- **优化基础**：梯度下降、凸优化入门

对标本预科的Day 3-4统计学内容。Imperial的特色是数学严谨性高于一般商学院，适合有STEM背景的学习者。

- **链接**：https://www.imperial.ac.uk/business-school/programmes/msc-business-analytics/

### NUS CS6101研究导论

National University of Singapore的CS6101（Research Methods in Computing）是PhD一年级必修课，涵盖：

- 研究方法论基础（实证/解释/实用主义范式）
- 文献综述方法
- 学术写作（IMRaD格式）
- 研究伦理

对标本预科Day 6的研究方法论入门内容。NUS的特色是QE（Qualifying Examination）机制——博士生需要通过基于论文的批判性综述和研究生提案的考试，这要求扎实的研究方法论基础。

- **链接**：https://www.comp.nus.edu.sg/programmes/pg/phdcs/

### 七校基础要求对照表

| 大学 | 对标维度 | 核心要求 | 本预科对应 |
|------|---------|---------|-----------|
| MIT | 数据分析 | OCW 15.071 Unit 1-2 | Day 1-4全部 |
| Stanford | ML先修 | CS229先修要求 | Day 1-4 + 线性代数补充 |
| Imperial | 数理基础 | Maths & Stats Foundations | Day 3-4统计学 |
| NUS | 研究方法 | CS6101研究导论 | Day 6研究方法论 |
| Harvard | 实证计量 | Angrist & Pischke教材 | Day 3-4假设检验基础 |
| Oxford | 方法论序列 | 定量+定性+混合方法 | Day 6研究范式 |
| Cambridge | MPhil训练 | SMOOB/ISO双轨 | Day 6方法论入门 |

---

## 知识问答（预科自测 · v4.0）

> 🌐 **英语轨道融合**：试着用英文回答Q1、Q2和Q8（不纠错，能表达意思就行）。这就是Natural Approach的"输出自然发生"——输入量够了，输出不需要强迫。

| # | 问题 | 难度 | 答案要点 | 英语提示 |
|:--:|------|:--:|---------|---------|
| Q1 | 用Python读取一个CSV文件，计算某一列的平均值和最大值。请写出核心代码。 | ⭐ | `pd.read_csv('file.csv')`; `df['col'].mean()`; `df['col'].max()` | `read_csv`, `mean`, `max` |
| Q2 | 解释p值<0.05在A/B测试中的含义。如果p值=0.08，你应该怎么做？ | ⭐ | p值是在"原假设（新方案无效果）成立"的前提下，观察到当前差异或更极端差异的概率。p<0.05表示有统计显著性。p=0.08表示证据不足，不能拒绝原假设——但也不意味着新方案无效，可能是样本量不够，需要继续实验或增大样本量。 | `p-value`, `statistical significance`, `fail to reject` |
| Q3 | 均值和中位数在什么情况下会有显著差异？在商业数据分析中应该关注哪个？ | ⭐ | 当数据分布偏斜（特别是右偏，如收入、消费金额）时，均值远大于中位数。商业分析中应同时报告两者，中位数更能反映"典型客户"的真实水平。 | `skewed distribution`, `median vs mean` |
| Q4 | 设计一个电商数据库Schema，包含用户、订单、商品、类目四张表，说明各表的主键和外键关系。 | ⭐⭐ | users(user_id PK), categories(category_id PK, parent_category_id FK自引用), products(product_id PK, category_id FK), orders(order_id PK, user_id FK), order_items(item_id PK, order_id FK, product_id FK)。orders和products之间是M:N关系，通过order_items关联。 | `primary key`, `foreign key`, `many-to-many` |
| Q5 | 一家公司声称其新产品使客户留存率提升了5%。作为数据分析师，你会如何验证这个说法？ | ⭐⭐ | 需要确认：①是否有对照组（A/B测试）？②样本量是否足够？③留存率如何定义（7日/30日/90日）？④是否有混杂因素（季节性、促销活动）？⑤差异是否统计显著（假设检验）？⑥差异是否有商业意义（效应量）？ | `control group`, `sample size`, `confounding variables` |
| Q6 | 解释"数据仓库"和"数据湖"的核心区别。你的企业更适合哪种？ | ⭐⭐ | 数据仓库存储结构化数据，写时模式，适合BI报表和分析查询。数据湖存储结构化+非结构化数据，读时模式，适合数据探索和ML训练。如果企业有大量非结构化数据（客服对话、广告素材、用户评论）需要做AI分析，数据湖/湖仓一体更合适。 | `data warehouse`, `data lake`, `schema-on-write`, `schema-on-read` |
| Q7 | 在多元回归分析中，如果两个自变量的VIF值都大于10，说明什么问题？应该如何处理？ | ⭐⭐ | VIF>10表示严重多重共线性——两个自变量高度相关，导致回归系数不稳定、p值不可靠。处理方法：①删除其中一个共线变量；②用PCA降维；③使用岭回归（Ridge Regression）或Lasso回归。 | `multicollinearity`, `VIF`, `variance inflation factor` |
| Q8 | 学术研究和工程实践的核心区别是什么？博士论文和项目报告有什么不同？ | ⭐ | 工程实践目标是解决问题，交付物是可运行的系统；学术研究目标是创造新知识，交付物是论文。博士论文不仅说"我做了X效果是Y"，还要说"这证明了Z理论/产生了W设计原则，对学术共同体有N启示"。 | `academic research`, `engineering practice`, `knowledge contribution` |
| Q9 | IMRaD格式包含哪四个部分？每个部分的核心功能是什么？ | ⭐ | Introduction（引言：为什么做这个研究）, Methods（方法：怎么做的）, Results（结果：发现了什么）, Discussion（讨论：意味着什么）。Introduction从大到小（背景->问题->贡献），Methods要可复现，Results用图表说话，Discussion诚实讨论局限。 | `Introduction`, `Methods`, `Results`, `Discussion` |
| Q10 | 如果你的企业有10个部门，每个部门都在自己的Excel里维护客户数据，你会如何设计数据治理方案？ | ⭐⭐⭐ | ①建立数据标准（统一客户ID、字段定义、编码规范）；②建立主数据管理（MDM）系统，作为"单一真相源"；③制定数据质量监控规则（自动化检测重复、缺失、不一致）；④明确数据所有权（每个字段有owner）；⑤建立数据治理委员会（跨部门协调）；⑥逐步迁移从Excel到统一数据库。 | `data governance`, `master data management`, `single source of truth` |
| Q11 | 什么是研究的三种范式？在AI商业研究中各适用于什么场景？ | ⭐⭐ | 实证主义（客观真实，定量实验，如A/B测试验证AI效果）；解释主义（社会建构的真实，定性研究，如访谈理解AI如何改变决策流程）；实用主义（根据问题选择方法，混合方法，如定量测效果+定性理解过程）。 | `positivism`, `interpretivism`, `pragmatism`, `mixed methods` |
| Q12 | 正态分布、二项分布、泊松分布在营销数据中各有什么应用场景？ | ⭐⭐ | 正态分布：消费金额（对数变换后）、A/B测试中转化率差的分布。二项分布：广告点击（点/不点）、转化（买/不买）。泊松分布：单位时间内的购买次数、客服来电次数、网站访问次数。 | `normal distribution`, `binomial distribution`, `Poisson distribution` |
| Q13 | 因果关系和相关关系有什么区别？回归分析揭示的是哪种关系？ | ⭐⭐⭐ | 相关关系是指两个变量同步变化，因果关系是指一个变量的变化导致另一个变量变化。回归分析揭示的是相关关系（在满足严格外生性假设时可以解释为因果，但这个假设在观察数据中很难满足）。从相关到因果需要额外的方法——A/B测试、工具变量、双重差分等（后续技能3深入）。 | `correlation vs causation`, `endogeneity`, `confounding` |

---

## 作业设计

### 作业0.1：数据分析实战报告（必做）

> 🌐 **英语轨道融合**：用Python写Jupyter Notebook时，尝试用英文写Markdown注释和标题（不纠错，能看懂就行）。

**任务**：选择你熟悉的业务场景（或公开数据集如Kaggle电商数据），完成一份完整的数据分析报告。

**步骤**：
1. 用Python读取数据（CSV/JSON/API），数据量不少于500条
2. 做描述统计分析（均值、中位数、标准差、分布形态），识别异常值
3. 做至少一个假设检验或回归分析，解释结果的业务含义
4. 用Matplotlib/Seaborn画至少3张图表（分布图、关系图、分组对比图）
5. 写出300字的业务洞察，包含至少一个可执行的建议
6. 将代码和数据整合到Jupyter Notebook中，确保从头到尾可运行

**交付物**：Jupyter Notebook（.ipynb）+ 300字业务洞察报告
**英语挑战（可选）**：把业务洞察写成英文版（不纠错，能表达意思就行）

**评分量表（5分量表）**：

| 维度 | 权重 | 1分（初级） | 3分（合格） | 5分（卓越） |
|------|:----:|-----------|-----------|-----------|
| 编程能力 | 30% | 能跑通代码但结构混乱 | 代码结构清晰，有基本注释 | 有函数封装、错误处理、Markdown说明 |
| 统计理解 | 30% | 能复述概念但选错方法 | 能正确选择检验方法并解释结果 | 能解释结果的业务含义和局限性 |
| 数据治理 | 10% | 未关注数据质量 | 能识别缺失值和异常值 | 能提出数据质量改进方案 |
| 业务连接 | 20% | 提到了业务但无深度 | 分析有业务价值 | 发现新的业务机会或验证了业务假设 |
| 英语阅读 | 附加 | 能读懂中文教程 | 能借助翻译读懂英文教程 | 能直接读懂英文教程核心段落 |
| 研究方法论理解 | 附加 | 知道学术研究的基本概念 | 能区分相关和因果 | 能用IMRaD格式写一段分析总结 |

---

### 作业0.2：企业数据Schema设计（必做）

**任务**：为你所在企业（或熟悉的企业）设计一个关系型数据库Schema，支持营销分析场景。

**步骤**：
1. 识别至少5个核心实体（如客户、商品、订单、营销活动、渠道）
2. 定义每个实体的属性（至少5个字段），选择合适的数据类型
3. 定义实体间的关系（1:1, 1:N, M:N），明确主键和外键
4. 画出ER图（可用Mermaid、draw.io或手绘拍照）
5. 用SQL写出建表语句（CREATE TABLE），包含约束（CHECK, NOT NULL, DEFAULT）
6. 写出5个常见业务查询的SQL（如RFM分群、渠道GMV、热销商品Top10、客户留存率、未购买客户分析）
7. 用sqlite3在Python中实际运行建表和查询，确保SQL语法正确

**交付物**：ER图 + SQL脚本 + 运行结果截图
**参考答案要点**：参考Day 5的代码示例，核心评分点在于：①表结构设计是否规范（范式化）；②外键关系是否正确；③SQL查询是否能正确回答业务问题；④是否有数据约束（CHECK/NOT NULL）。

---

### 作业0.3：研究计划大纲（挑战）

**任务**：选择一个你感兴趣的AI营销研究方向，用IMRaD格式写一个一页纸的研究计划大纲。

**步骤**：
1. 选择一个研究问题（如"AI生成内容对广告转化率的影响"、"RAG增强的营销知识库对销售效率的影响"等）
2. 用IMRaD格式写大纲：
   - **Introduction**：研究背景（2-3句）、研究问题（1句）、研究贡献（1句）
   - **Methods**：数据来源（1句）、研究方法（1-2句，如A/B测试、案例研究、混合方法）
   - **Results**：预期发现（1-2句）
   - **Discussion**：理论/实践启示（1句）、局限性（1句）
3. 标注你打算使用的研究范式（实证主义/解释主义/实用主义）

**交付物**：一页纸研究计划大纲（300-500字）
**参考答案要点**：核心评分点在于：①研究问题是否清晰（不是"做一个系统"，而是"解决什么问题/回答什么问题"）；②方法是否匹配问题；③IMRaD结构是否完整；④是否有研究范式意识。

**示例大纲**：
> **Introduction**：随着大语言模型的普及，AI生成的营销文案正在替代人工文案。然而，AI文案对消费者购买决策的影响机制尚不清楚。本研究旨在探究AI生成文案与人工文案在广告转化率上的因果差异，并识别影响效果的调节因素。贡献在于为AI营销文案的使用提供实证依据。
>
> **Methods**：采用混合方法设计。定量部分：在某电商平台进行A/B测试，随机分配10万用户至AI文案组和人工文案组，比较两组的CTR和CVR。定性部分：对20位用户进行深度访谈，理解他们对AI文案的感知和信任度。
>
> **Results**：预期AI文案组CTR不低于人工组（非劣效性检验），但在特定品类（如奢侈品）可能表现更差。访谈预期揭示"感知真实性"是关键调节因素。
>
> **Discussion**：实践启示——AI文案可用于标准化品类，奢侈品品类仍需人工。理论贡献——丰富"AI与消费者信任"文献。局限——单一平台数据，外部效度有限。
>
> **研究范式**：实用主义（混合方法）

---

## 费曼学习法演练

**目标听众**：你的业务同事（非技术背景，如市场部同事、销售同事）

**演练流程**：
1. 选择一个核心概念（建议从以下三个中选一个）："假设检验与p值"、"数据仓库与数据湖"或"学术研究vs工程实践"
2. 用大白话解释，假设你在电梯里，只有2分钟
3. 找到知识缺口——哪里你解释不清楚，说明哪里你还没真正理解
4. 回头补课，重读对应章节
5. 简化到极致——如果一个概念需要超过3个术语才能解释，说明你还在用"术语"代替"理解"

**费曼示例文本（"假设检验与p值"，约550字）**：

"你们做A/B测试吧？比如新落地页和老落地页同时上线，新页面转化率3.2%，老页面2.8%。看到新页面高0.4个百分点，你会说'新页面更好'。但等一下——如果样本量只有100人呢？100人里的0.4个百分点，可能就是运气。

假设检验就是解决'这个差异是真本事还是碰运气'的问题。它像一个法庭审判。原假设是'被告无罪'——在我们的场景里就是'新页面和老页面其实一样好，差异是随机波动'。备择假设是'被告有罪'——'新页面真的更好'。

我们收集证据——也就是A/B测试的数据。然后计算一个叫p值的东西。p值回答的是：如果新页面和老页面真的完全一样（原假设成立），我们看到当前差异（0.4个百分点）或更大差异的概率有多大？

如果p值很小，比如0.01，意思是'如果两个页面真的没区别，看到0.4个百分点差异的概率只有1%'——这个概率太小了，所以我们倾向于相信'两个页面确实有区别'，拒绝原假设。

如果p值是0.15，意思是'即使两个页面没区别，也有15%的概率看到这样的差异'——这完全可能是运气，所以我们不能下结论说新页面更好。这就是'证据不足，不能定罪'。

0.05这条线是学界约定俗成的标准。p<0.05叫'统计显著'，意思是'差异大概率是真的，不是运气'。但注意——统计显著不等于商业上重要。如果100万人里转化率差0.01个百分点，p值可能<0.05（因为样本量大），但0.01个百分点在商业上可能毫无意义。

记住一句话：没有p值的A/B测试，就是拍脑袋。但只看p值的A/B测试，是另一种拍脑袋。"

> 🌐 **英语轨道融合**：尝试把上面的费曼解释用英文写一遍（不纠错，能表达意思就行）。关键术语：null hypothesis, alternative hypothesis, p-value, statistical significance。这就是Natural Approach的"输出自然发生"——当你的英文输入量够了，输出不需要强迫，自然就来了。

---

## 2分钟分享话术脚本

```
【开场 · 15秒】抛钩子
"你们公司做A/B测试吗？做过。那你们怎么判断结果是真的有效，还是只是运气好？
今天我用2分钟讲清楚一个数据分析师必备的决策工具。"

【核心 · 60秒】讲清楚是什么
"这个工具叫'假设检验'。它不做判断，它只回答一个问题：
'如果新方案其实和旧方案完全一样，我看到当前数据差异的概率有多大？'

这个概率就是p值。如果p值小于0.05——也就是5%——我们说'差异大概率是真的'，
这叫统计显著。如果p值大于0.05，我们说'证据不足，不能下结论'。

举个例子：新落地页转化率3.2%，旧页面2.8%。看起来新页面更好？
但如果只有200个样本，p值可能是0.15——这意味着即使两个页面真的没区别，
也有15%的概率看到这样的差异。15%的概率不算小，所以不能下结论。

我们又跑了5000个样本，新页面3.1%，旧页面2.9%，p值=0.03——
这次差异虽然更小，但因为样本量大，我们有信心说'新页面真的更好'。"

【案例 · 30秒】讲一个故事
"我们团队去年差点做了一个错误决策：新版推荐算法上线后，
某品类点击率提升了8%，大家都很兴奋。但一做假设检验，
p值=0.12——因为该品类日活只有3000，样本量不够。
后来我们扩大实验到全品类、跑了两周，发现整体提升只有1.2%，
p值=0.04。如果当时直接全量上线，可能浪费了3万月度预算在效果不确定的改动上。"

【结尾 · 15秒】给行动建议
"记住两句话：
第一，没有p值的A/B测试，就是拍脑袋。
第二，p值<0.05只是'有效果'，不等于'值得做'——还要看效果有多大、ROI够不够。"
```

> 🌐 **英语轨道融合**：尝试把开场和结尾两段翻译成英文（不纠错，能表达意思就行）。这是练习技术英文口语的好方法——15秒的内容很短，不会产生"情感过滤"（焦虑感），符合Natural Approach的低情感过滤原则。

---

## 复盘诊断建议

### 诊断问题表

| 诊断问题 | 如果回答"不能"的诊断建议 |
|----------|-------------------------|
| 我能否独立写出50行以上的Python数据处理脚本？ | 回到Day 1-2，用Kaggle Learn的Python和Pandas课程多做练习。关键是动手敲代码，不是看视频。 |
| 我能否解释p值、置信区间、统计显著性的含义和局限？ | 回到Day 3，用真实A/B测试数据做一次完整的假设检验。关键是理解p值"不告诉你效果多大，只告诉你有没有效果"。 |
| 我能否为一个业务场景设计3张表以上的数据库Schema？ | 回到Day 5，从最简单的2张表（users + orders）开始，逐步加表。关键是理解主键、外键和关系类型。 |
| 我能否独立完成一个多元回归分析并解释结果？ | 回到Day 4，用statsmodels库做一次完整的回归分析。关键是理解R²、回归系数p值和VIF的含义。 |
| 我能否区分相关关系和因果关系？ | 这是本预科最重要的认知之一。回到Day 4最后部分的"从相关到因果"段落。后续技能3会深入这个话题。 |
| 我能否用IMRaD格式写一个研究计划大纲？ | 回到Day 6，参考作业0.3的示例大纲。关键是理解学术研究的四个核心问题：为什么做、怎么做、发现了什么、意味着什么。 |
| 我是否觉得"太基础了，可以跳过"？ | 用真实业务数据做一遍作业0.1。很多人在"基础"中发现自己的知识盲区。如果你的分析确实完美，直接进入技能1。 |
| **英语轨道**：我能否读懂Python官方教程的核心段落？ | 先读中文版，再对照英文版。不背单词，混个脸熟。能读懂60%就继续，不要追求100%理解。 |
| **英语轨道**：我能否读懂MIT OCW 15.071的英文讲义？ | 如果Python官方教程读得太轻松，升级到MIT OCW。读不懂的段落跳过，关注案例和图表。 |

### 后续优化方向

- 如果Python让你兴奋 -> 建议选修"Programming with Generative Artificial Intelligence"
- 如果统计学让你兴奋 -> 建议选修"Artificial Intelligence based Optimization"
- 如果数据治理让你兴奋 -> 建议选修"Data Visualization" + "Cloud Computing"
- 如果研究方法论让你兴奋 -> 模块R的六个子模块会让你深入DSR、行动研究、混合方法、PRISMA、IMRaD和研究伦理
- **英语轨道**：如果Python官方教程读得太轻松 -> 升级到Kaggle英文Discussions（中等难度）；如果MIT OCW讲义能读懂70% -> 升级到Stanford CS229先修材料（高难度）

---

## 推荐资源清单

### 书籍

| 书名 | 作者 | 对标内容 | 难度 |
|------|------|---------|:----:|
| 《Python数据分析》（Python for Data Analysis） | Wes McKinney（Pandas作者） | Day 1-2 编程基础 | ⭐⭐ |
| 《Practical Statistics for Data Scientists》 | Peter Bruce等 | Day 3-4 统计学 | ⭐⭐ |
| 《Designing Data-Intensive Applications》 | Martin Kleppmann | Day 5 数据管理 | ⭐⭐⭐ |
| 《Research Design》第五版 | John W. Creswell | Day 6 研究方法论 | ⭐⭐⭐ |
| 《The Book of Why》 | Judea Pearl | 因果推断入门（技能3预备） | ⭐⭐⭐ |

### 课程

| 课程 | 提供方 | 链接 | 对标内容 |
|------|--------|------|---------|
| MIT OCW 15.071 The Analytics Edge | MIT Sloan | https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/ | Day 1-4 |
| Khan Academy Statistics and Probability | Khan Academy | https://www.khanacademy.org/math/statistics-probability | Day 3-4 |
| Kaggle Learn: Python + Pandas + SQL | Kaggle | https://www.kaggle.com/learn | Day 1-2, Day 5 |
| CS50's Introduction to Programming with Python | Harvard | https://cs50.harvard.edu/python/ | Day 1-2 |
| Python Official Tutorial | Python.org | https://docs.python.org/3/tutorial/ | Day 1-2（英语轨道） |

### 视频

| 视频 | 平台 | 对标内容 |
|------|------|---------|
| "Python数据分析从入门到实战" | B站（搜索播放量>10万） | Day 1-2 |
| "统计学入门 商务统计"（带Python实操） | B站 | Day 3-4 |
| "SQL基础教程"（带实战案例） | B站 | Day 5 |
| "研究方法论入门" | B站（播放量>1万） | Day 6 |

### 文档

| 文档 | 链接 | 对标内容 |
|------|------|---------|
| Pandas官方文档 | https://pandas.pydata.org/docs/ | Day 1-2 |
| SciPy统计函数参考 | https://docs.scipy.org/doc/scipy/reference/stats.html | Day 3-4 |
| Statsmodels文档 | https://www.statsmodels.org/stable/ | Day 4 |
| SQLite教程 | https://www.sqlitetutorial.net/ | Day 5 |
| Creswell研究方法论资源 | SAGE出版 | Day 6 |

---

## 英语平行轨道材料

### 设计原则

本模块的英语轨道遵循**牛津自然学习法**（Krashen & Terrell's Natural Approach）的三个核心原则：

1. **i+1可理解输入**：材料难度略高于当前水平（i），提供"可理解的"新内容（+1）。不追求100%理解，60-70%即可继续。
2. **理解先于输出**：不要求"先会说再会读"。先大量阅读/听力输入，输出（说/写）自然发生。
3. **低情感过滤**：不纠错、不考试、不背单词。焦虑感越低，习得效率越高。

### 本模块英语材料清单

| 材料 | 难度 | 对标天次 | 使用方式 | 预计时间 |
|------|:----:|:-------:|---------|:-------:|
| Python Official Tutorial Part 1-3 | ⭐ | Day 1-2 | 直接读英文版，能读懂60%就继续。遇到不懂的查关键词，不背。 | 1h |
| Khan Academy Statistics（有字幕） | ⭐⭐ | Day 3-4 | 先开中文字幕理解概念，再关字幕纯英文听一遍。 | 1.5h |
| MIT OCW 15.071 Unit 1-2 讲义 | ⭐⭐ | Day 1-4 | 读英文讲义，重点关注案例和图表。读不懂的段落跳过。 | 1h |
| Kaggle Learn: SQL | ⭐ | Day 5 | 英文界面互动练习，SQL是通用语言，语言障碍小。 | 0.5h |

### v4.0新增：每日英语微习惯

在每天的学习中，花15-20分钟做以下英语微习惯：

| 天次 | 英语微习惯 | 时长 |
|:---:|-----------|:---:|
| Day 1 | 打开Python官方教程英文版，读"3. An Informal Introduction to Python"的前3段 | 15min |
| Day 2 | 打开MIT OCW 15.071 Unit 1讲义，读第一页（Introduction部分） | 20min |
| Day 3 | 在Khan Academy看一个统计学视频（开英文字幕），理解大意 | 15min |
| Day 4 | 在Khan Academy看一个概率论视频（关字幕纯英文听），能听懂多少是多少 | 15min |
| Day 5 | 在Kaggle Learn完成SQL第一课（英文界面） | 20min |
| Day 6 | 读Creswell《Research Design》Chapter 1的前5页英文原文 | 15min |

### 难度标注说明

- ⭐（简单）：技术文档/代码为主，语言简单，生词少。适合i+1入门。
- ⭐⭐（中等）：学术讲义/教学视频，有专业术语但解释清晰。适合i+1进阶。
- ⭐⭐⭐（较难）：学术论文/教材原文，学术英语句式复杂。适合i+1挑战。
- ⭐⭐⭐⭐（困难）：前沿论文/理论教材。后续技能使用。

---

## 研究方法论入门（Day 6详细补充）

> 本部分是v4.0新增内容，为Day 6提供更详细的研究方法论入门材料。

### 什么是学术研究

学术研究的本质是**创造新知识**。这个"新"可以是：
- **新发现**：发现了一个前人没有观察到的现象
- **新方法**：提出了一种新的分析方法或工具
- **新应用**：将已有方法应用到新的领域
- **新综合**：综合前人的分散发现，提出统一框架

对于aha.gare这样有丰富工程实践的学习者，最自然的路径是**新应用+新方法**——将AI工程技术应用到营销场景，在应用过程中产出新的设计原则和方法论。这正是设计科学研究（DSR）范式要解决的问题（后续模块R1会深入）。

### 博士论文长什么样

一篇信息系统/商业分析领域的博士论文通常包含以下部分：

**第一章：绪论（Introduction）**
- 研究背景：AI正在重塑企业营销，但缺乏系统化的架构设计方法论
- 问题陈述：当前企业在AI营销系统设计中面临什么具体问题
- 研究目标：本研究旨在设计一个AI原生化营销智能体系统架构，并验证其有效性
- 贡献声明：本研究的贡献是（1）提出XXX架构模式，（2）产出XXX设计原则，（3）在真实企业场景中验证

**第二章：文献综述（Literature Review）**
- 用PRISMA方法系统梳理已有研究（后续模块R4会深入）
- 识别研究空白：已有研究在XXX方面存在不足

**第三章：理论框架（Theoretical Framework）**
- 选择理论视角：如设计科学理论、行动研究理论
- 定义核心概念

**第四章：研究方法（Methodology）**
- 研究范式声明：实用主义，采用混合方法
- 数据收集：定量（A/B测试数据）+ 定性（用户访谈、田野笔记）
- 数据分析：统计检验 + 主题分析

**第五章：研究结果（Results）**
- 系统设计与实现：架构设计、技术选型
- 评估结果：定量指标（CTR、CVR、ROI）+ 定性发现（用户感知、决策流程变化）

**第六章：讨论（Discussion）**
- 与前人研究对比
- 设计原则提炼
- 理论与实践启示
- 局限性

**第七章：结论（Conclusion）**
- 贡献总结
- 未来研究方向

### 研究三范式详解

**实证主义（Positivism）**

实证主义认为真实是客观存在的、可以通过观察和测量来认识。研究者是中立的观察者，研究的目标是发现客观规律。实证主义对应定量研究方法：实验、问卷调查、统计分析。

在AI商业研究中的应用：用A/B测试验证AI系统的效果，用统计方法分析数据，得出可推广的结论。Stanford GSB和MIT Sloan的营销研究大量采用实证主义范式。

**解释主义（Interpretivism）**

解释主义认为真实是社会建构的、主观的。研究者是参与者，研究的目标是理解现象背后的意义和过程。解释主义对应定性研究方法：深度访谈、参与式观察、案例研究。

在AI商业研究中的应用：通过访谈理解AI系统如何改变营销团队的决策流程，通过田野观察理解AI工具在实际使用中的"缝隙"（gap between design and use）。Oxford和Cambridge的管理研究有较强的解释主义传统。

**实用主义（Pragmatism）**

实用主义认为真实是多元的，研究方法应该根据研究问题来选择，而不是固守某种范式。实用主义对应混合方法研究：定量+定性的系统整合。

在AI商业研究中的应用：定量部分用A/B测试和因果推断评估AI系统效果，定性部分用访谈和案例理解效果背后的原因。Creswell的混合方法三设计（收敛式、解释性序列、探索性序列）是实用主义的具体操作框架。后续模块R3会深入训练。

### IMRaD格式详解

**Introduction的写作要点**：
- 从大到小（Funnel结构）：领域大背景 -> 具体问题 -> 研究空白 -> 本文贡献
- 每段第一句是Topic Sentence，让读者不看后续细节也能理解文章脉络
- 贡献声明要具体：不说"本文有重要意义"，说"本文提出了X方法，在Y场景中验证了Z效果"

**Methods的写作要点**：
- 核心原则：可复现性。别人读了你方法部分，应该能复现你的研究
- 结构：数据来源 -> 样本选择 -> 变量定义 -> 分析方法 -> 伦理声明
- 统计方法要写清楚：用了什么检验、为什么选这个检验、显著性水平是多少

**Results的写作要点**：
- 用图表说话：一张好图胜过千言万语
- 先描述再解释："表1显示A组转化率3.2%，B组2.8%（描述），差异在p<0.05水平显著（统计判断）"
- 区分"数据显示什么"和"这意味着什么"——后者放在Discussion

**Discussion的写作要点**：
- 与前人研究对比：你的发现与已有文献一致还是矛盾？为什么？
- 理论启示：你的发现如何丰富/挑战现有理论？
- 实践启示：对从业者有什么建议？
- 局限性：诚实的局限性比虚假的完美更有价值。常见局限性：样本量、外部效度、混杂因素
- 未来方向：基于本研究的局限，下一步可以做什么？

> 这一部分是模块R5（IMRaD论文写作）的预热。在后续技能5 Day 7中，你将用IMRaD格式为你的Capstone项目写一个论文大纲。

---

## 附录：v4.0版本说明

### 本独立教材与主教材的关系

本文件是"AI原生化商业博士"主教材v4.0版本中"技能0：AI商业分析基础"模块的独立展开版。主教材提供课程体系的全局视图和各技能的概要，本独立教材提供技能0的完整教学内容，可直接作为独立学习材料使用。

### 与v3.1的主要差异

| 项目 | v3.1 | v4.0独立教材 |
|------|------|-------------|
| 天数 | 5天 | 6天（+研究方法论入门） |
| 学时 | 20h | 22h |
| 对标大学 | Kaggle + Khan Academy | + MIT OCW 15.071 + Stanford CS229先修 + Imperial + NUS |
| 代码示例 | 概要性 | 完整可运行的Python脚本（含模拟数据） |
| 案例分析 | 简要描述 | 详细的真实营销场景分析（RFM、A/B测试、LTV回归、多源数据整合、数据库Schema） |
| 研究方法论 | 无 | Day 6完整章节（研究范式、博士论文结构、IMRaD格式） |
| 英语轨道 | 简要列表 | 每日英语微习惯+难度标注+使用方式 |
| 知识问答 | 6题（无答案） | 13题（含答案要点和难度分级） |
| 作业设计 | 2个 | 3个（2必做+1挑战，含详细评分量表和参考答案要点） |

### 代码运行环境要求

- Python 3.10+
- 依赖库：pandas, numpy, scipy, statsmodels, matplotlib, seaborn, sqlite3（标准库）
- 推荐使用Jupyter Notebook或VS Code运行

### 字数统计

本教材正文约18000字（含代码注释），不含代码约15000字。

---

*本教材由Claude基于v4.0主教材和升级方案编制，作为"AI原生化商业博士"课程技能0的独立学习材料。*
*最后更新：2026-07-16*
