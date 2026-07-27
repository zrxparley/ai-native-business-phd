# AI原生化商业博士 · 独立教材 · 模块R：博士研究方法论基础

> **修读者**：aha.gare  
> **版本**：v4.0 | **日期**：2026-07-16  
> **学时**：10小时（嵌入五技能，每技能约2h）  
> **对标大学**：NUS IS PhD / Oxford DPhil / Cambridge MPhil / Imperial MRes / Stanford GSB PhD  
> **课程哲学**：研究即贡献（Research as Contribution）  
> **英语教学法**：牛津自然学习法 -- i+1可理解输入，理解先于输出  
> **核心命题**：如何将工程实践转化为学术贡献？

---

## 一、模块概述

### 1.1 为什么需要研究方法论

aha.gare是一位有丰富工程实践经验的售前解决方案产品经理。在AI+企业营销领域，你已经具备了从战略规划到技术落地的完整能力链。但你面临一个根本性的能力缺口：你能够"做出来"，却未必能够将实践成果"说清楚"——这里的"说清楚"不是写技术文档或产品需求说明，而是按照学术界认可的范式，将工程实践升华为可验证、可传播、可被同行引用的知识贡献。

这个缺口正是博士训练和硕士训练的核心区别所在。硕士训练教你"怎么做"，博士训练要求你回答"为什么这样做是对的，以及这样做创造了什么新知识"。

七所全球顶尖大学的博士项目无一例外地在博士第一年安排了密集的研究方法论课程序列。Harvard HBS DBA用Angrist & Pischke的《Mostly Harmless Econometrics》（2009）训练实证计量研究能力；MIT IDSS以Imbens & Rubin的《Causal Inference for Statistics, Social, and Biomedical Sciences》（2015）为因果推断的奠基教材；Stanford GSB要求博士生完成完整的计量经济学序列，并引入Athey & Imbens（2019）将机器学习与因果推断融合的前沿方法；Oxford DPhil Management在第一年安排定量、定性和混合方法三门方法论必修课；Cambridge MPhil按研究方向分为SMOOB（定量方向）和ISO（定性方向）两条方法论轨道；Imperial MRes提供包括Systematic Reviews、Data Analysis Tools和Qualitative Methods在内的系统化方法论训练；NUS PhD通过Qualifying Examination（QE）和Graduate Research Paper（GRP）机制强制要求研究能力达标。

模块R的设计理念是"嵌入而非独立"。它不占用独立的10小时时间块，而是以"研究方法论透镜"的方式，在每个技能学习的关键节点嵌入2小时的方法论训练。学技能1时引入设计科学研究（DSR）框架来定义研究问题；学技能2时用行动研究视角设计企业AI转型实验；学技能3时引入混合方法来设计因果评估方案；学技能4时用PRISMA标准做系统文献综述；学技能5时用IMRaD格式写论文草稿并做研究伦理自查。这种嵌入设计借鉴了Oxford和Cambridge的"方法论贯穿全程"理念，而非将方法论作为孤立的先修课程。

### 1.2 七校方法论训练对比

| 大学 | 方法论核心特色 | 代表性教材/框架 | 对标模块R子模块 |
|------|-------------|--------------|:----------:|
| **Harvard HBS** | 实证计量+案例驱动 | Angrist & Pischke (2009); Eisenhardt (1989) 案例研究 | R3, R5 |
| **MIT IDSS** | 统计学+因果推断深度融合 | Imbens & Rubin (2015); Athey & Imbens (2019) ML因果推断 | R3 |
| **Stanford GSB** | 计量经济+计算营销+论文写作 | Wooldridge (2010); Stanford GSB PhD Writing Workshop | R5 |
| **Oxford** | 定量+定性+混合方法并重 | Creswell & Plano Clark (2018); OII方法论课程序列 | R3, R6 |
| **Cambridge** | 按研究方向区分方法论双轨 | MPhil SMOOB（定量）/ MPhil ISO（定性）; Yin (2018) 案例研究 | R2, R3 |
| **Imperial** | MRes系统化方法论训练 | Systematic Reviews + Data Analysis Tools + Qualitative Methods | R4, R6 |
| **NUS** | QE/GRP研究能力评估+设计科学 | Peffers et al. (2007) DSR; Hevner et al. (2004) Design Science | R1 |

### 1.3 模块R设计理念

模块R的核心设计理念可以用一句话概括：**在工程实践的过程中自然习得研究能力，而不是"先学方法论再做事"**。

这与Kolb（1984）的Experiential Learning Theory（经验学习理论）一致：知识是通过经验的转化而创造的，学习是一个"具体经验→反思性观察→抽象概念化→主动实验"的循环过程。模块R嵌入每个技能的关键节点，让你在学习技术内容的同时，自然地经历研究方法论的训练。

Schön（1983）在《The Reflective Practitioner》中提出，专业人士在实践中不仅是"执行者"，更是"反思性实践者"（reflective practitioner）。模块R就是培养你的研究反思能力——在每一次技术决策时问自己："这个决策背后的设计原则是什么？它如何被泛化？它对学术知识库有什么贡献？"

---

## 二、R1：设计科学研究（Design Science Research）

> 📍 嵌入技能1 Day 1 | ⏱ 2h | 📘 对标：NUS IS PhD / Imperial MRes

### 2.1 核心概念详解

设计科学研究（Design Science Research, DSR）是信息系统（Information Systems）领域的核心研究范式。它与行为科学（Behavioral Science）形成互补：行为科学通过观察和理论来理解和解释现象，而设计科学通过构建和评估artifact（人工制品）来创造新知识。Hevner等人（2004）在MIS Quarterly发表的经典论文《Design Science in Information Systems Research》确立了这一范式的方法论地位，论文被引用超过30,000次，是信息系统领域引用量最高的论文之一。

**Artifact（人工制品）**是DSR的核心概念。March & Smith（1995）将artifact分为四种类型：constructs（构造，即领域的基本概念和词汇）、models（模型，即构造之间的关系）、methods（方法，即解决问题的算法或流程）和instantiations（实例化，即可运行的原型系统）。在AI+营销领域，一个"基于GraphRAG的营销知识增强检索系统"就是一个instantiation类型的artifact；它所体现的"知识图谱社区摘要增强全局推理"这一架构模式是method类型的artifact；而"营销知识的多模态表示框架"则是model类型的artifact。

**Hevner的设计科学cycle**包含三个核心研究活动：build（构建artifact）、evaluate（评估artifact）和theorize（理论化，即从设计和评估经验中抽象出设计原则）。Hevner等人（2004）强调，DSR的学术贡献不在于artifact本身，而在于从设计和评估过程中产出的"design principles"（设计原则）——这些原则可以被其他研究者和实践者复用和改进。

**Peffers六步流程**是DSR的标准执行框架，由Peffers等人（2007）在Journal of Management Information Systems论文《A Design Science Research Methodology for Information Systems Research》中提出：

1. **问题识别与动机（Problem Identification and Motivation）**：明确研究问题为什么重要。这一步需要基于现有文献和实际观察，论证当前存在什么未被解决的问题或机会。关键产出是"problem statement"——一个清晰、具体、可验证的问题陈述。

2. **定义解决方案目标（Define the Objectives for a Solution）**：artifact应该达到什么效果。目标可以来自现有文献中尚未实现的要求、竞品分析发现的差距、或实践中用户反馈的痛点。目标必须是可验证的——你能够在后续的评估步骤中判断是否达成。

3. **设计与开发（Design and Development）**：构建artifact。这一步不仅仅是"写代码"，而是基于理论知识进行有意识的设计决策。每一个设计决策都应有明确的理论依据：为什么选择这种架构而不是另一种？为什么用这个算法而不是另一个？

4. **演示（Demonstration）**：在真实或模拟场景中展示artifact如何解决问题。演示的目的是证明"可行性"——artifact确实能够处理研究问题所描述的场景。

5. **评估（Evaluation）**：系统化评估artifact的效果。评估方法可以是定量的（A/B测试、性能指标对比）或定性的（用户访谈、专家评审），关键是评估必须与第2步定义的目标对应。如果目标说"提高推荐准确率"，评估就必须测量推荐准确率。

6. **传播（Communication）**：发表学术论文，产出设计原则。传播的核心是将具体的工程经验抽象为可复用的知识——其他人在不同场景下应用你的设计原则时，能否获得类似的效果？

### 2.2 案例分析：AI营销内容生成的GraphRAG系统

假设你的Capstone方向是"为企业设计一个基于GraphRAG的营销知识增强检索与内容生成系统"。用DSR六步框架分析：

- **问题识别**：当前企业营销内容生成依赖通用LLM的内部知识，无法准确引用企业自有产品文档、客户案例和市场分析报告。传统RAG用向量检索解决了部分问题，但无法回答"我们产品线的主要差异化方向是什么"这类需要综合推理的全局性问题（Edge et al., 2024, arXiv:2404.16130）。
- **目标定义**：设计一个能同时支持事实性问答和全局推理问答的营销知识检索系统，在营销内容生成的准确性和相关性上显著优于传统向量检索RAG。
- **设计与开发**：采用GraphRAG架构——从企业营销文档中提取实体和关系构建知识图谱，使用Leiden算法进行社区检测，为每个社区生成摘要，查询时根据问题类型选择Global Search或Local Search。
- **演示**：在一个B2B企业的真实营销知识库（500+产品文档、200+客户案例）上部署系统，展示其回答营销策略问题的能力。
- **评估**：设计对照实验，比较GraphRAG系统与传统向量RAG在20个营销问答任务上的表现，评估维度包括事实准确率（Factuality）、相关性（Relevance）、全局推理能力（Global Reasoning）。
- **传播**：论文的核心贡献不是"我做了这个系统"，而是从设计和评估中提炼出的设计原则——例如"社区摘要的粒度如何影响全局推理质量"或"知识图谱构建中的实体抽取策略如何影响下游营销问答的准确性"。

### 2.3 与博士论文/Capstone的关联

DSR是Capstone研究型路径的核心框架。你的Capstone不是"做一个系统"，而是"通过设计和评估一个artifact来产出设计原则"。这个定位转换是从工程实践者到知识创造者跃迁的关键。NUS IS PhD项目将DSR作为其核心研究范式之一，许多毕业生在MIS Quarterly、Information Systems Research、Journal of the AIS等顶刊发表DSR论文。Imperial MRes同样要求学生用DSR框架完成毕业论文。

### 2.4 对标大学说明

- **NUS IS PhD**：NUS的信息系统博士项目以设计科学研究为核心特色，要求博士生在Qualifying Examination中展示用DSR框架定义和论证研究问题的能力。参考：https://www.comp.nus.edu.sg/programmes/pg/phdis/
- **Imperial MRes**：Imperial的MRes项目将Design Science方法作为方法论训练的核心模块之一，强调artifact的设计、评估和理论化循环。

### 2.5 实践练习

**任务**：选择你的Capstone方向，用DSR六步框架写一份一页纸（约500字）的研究计划。

**步骤**：
1. 写一句话的问题陈述（Problem Statement）——不是"做一个系统"，而是"解决什么问题"
2. 列出2-3个可验证的解决方案目标
3. 简述你打算怎么设计和开发artifact，列出关键的设计决策及其理论依据
4. 简述你打算怎么评估——评估指标是什么？对照组是什么？
5. 思考你的核心设计原则可能是什么——其他人在不同场景下能复用什么？

**交付物**：一份一页纸的DSR研究计划，包含六步各2-3句话。

### 2.6 英语轨道材料推荐

- 📄 Peffers et al. (2007) 论文的Abstract和Introduction（中等难度，学术英文）
- 📄 Hevner et al. (2004) 论文的Section 1-2（较高难度，但核心概念集中在这两节）
- 🌐 建议方法：先读中文摘要理解大意，再对照英文原文逐段阅读，不查全部生词，理解70%即可

---

## 三、R2：行动研究（Action Research）

> 📍 嵌入技能2 Day 4 | ⏱ 2h | 📘 对标：Cambridge田野研究 / Oxford参与式研究

### 3.1 核心概念详解

行动研究（Action Research）是一种研究者深入真实组织场景，与实践者协作解决实际问题同时产出学术知识的研究方法。它的核心特征是"双重目标"：既要在实践中产生有用的改变（action），又要产出可验证的学术知识（research）。Lewin（1946）最早提出行动研究的概念，将其定义为"一种将研究和行动结合起来的比较研究"。

**参与-行动-反思螺旋**是行动研究的核心循环结构，由Susman & Evered（1978）在Administrative Science Quarterly论文中系统化：

1. **诊断（Diagnosing）**：识别组织中的问题或机会，分析问题的根因。这一步类似于DSR的"问题识别"，但更强调在真实组织场景中的嵌入式观察。
2. **行动规划（Action Planning）**：设计具体的干预措施。干预措施必须基于理论框架，不能是随意的"试一试"。
3. **行动实施（Action Taking）**：在组织中实施干预。研究者本身是变革的推动者（change agent），这区别于传统研究中研究者的"客观旁观者"角色。
4. **评估（Evaluating）**：评估干预的效果。评估包括预期效果和意外效果——行动研究特别重视"意外的发现"，因为它们往往揭示深层组织动态。
5. **反思与学习（Specifying Learning）**：从经验中提炼可推广的知识。这一步对应DSR的"传播"，但更强调对组织变革过程本身的理解。

这个循环不是一次性的，而是螺旋式的——每一轮的反思都会修正下一轮的诊断和行动规划。Reason & Bradbury（2008）在《Handbook of Action Research》中强调，行动研究的质量取决于循环的深度和反思的诚实度。

**行动研究与案例研究的区别**：Yin（2018）在《Case Study Research》中指出，案例研究是"观察和解释"，研究者尽量不干预场景；行动研究则是"干预和反思"，研究者本身就是干预的一部分。在AI转型研究中，当你不仅是观察者，还是推动者时，行动研究比案例研究更合适。

### 3.2 数据收集方法

行动研究的数据收集具有多样性和持续性的特点：

- **田野笔记（Field Notes）**：研究者每天记录观察到的组织动态、关键事件、非正式对话中的线索。Emerson, Fretz & Shaw（2011）在《Writing Ethnographic Fieldnotes》中提供了系统的田野笔记方法。
- **半结构化访谈（Semi-structured Interviews）**：在干预前后对关键利益相关者进行访谈，了解他们对AI系统的感知、使用模式和态度变化。
- **系统日志（System Logs）**：AI系统的使用数据（调用频率、功能使用分布、错误率）是客观的行为数据。
- **反思日记（Reflective Journal）**：研究者自身的反思记录——你作为推动者，经历了什么阻力？你的预设被证实还是被推翻？

### 3.3 案例分析：企业营销AI治理框架部署

假设你在企业中推进AI治理框架（如NIST AI RMF）的落地。用行动研究视角设计：

- **诊断**：你企业的营销AI系统目前缺乏统一的治理标准。营销团队各自使用不同的AI工具（文案生成、投放优化、用户画像），存在数据泄露风险、算法偏见风险和合规风险。根因不是"没有工具"，而是"没有治理结构和流程"。
- **行动规划**：引入NIST AI RMF的四步循环（Govern-Map-Measure-Manage），在营销部门的一个小组内试点。基于NIST框架（2023版）设计AI用例登记表、风险评估清单和持续监控指标。
- **行动实施**：在试点小组内推行AI用例登记，要求所有AI使用场景必须登记并标注风险等级。研究者（你）作为治理推动者，协助团队完成首次登记和评估。
- **评估**：试点一个月后，评估登记覆盖率（有多少AI用例被登记了）、风险评估完成率、团队满意度。意外发现可能包括：团队对"AI治理"的理解偏差（有人认为是要限制他们用AI）、某些AI用例的风险等级比预期更高。
- **反思**：从试点经验中提炼"企业营销AI治理落地的关键成功因素"——例如"治理框架必须嵌入现有工作流，而不是额外增加审批环节"这一设计原则。

### 3.4 与博士论文/Capstone的关联

行动研究特别适合你的背景——作为售前解决方案产品经理，你在企业中推动AI转型的过程本身就是一个行动研究案例。关键是你要有系统化的数据收集（田野笔记、访谈、系统日志）和多轮反思记录。Cambridge Judge Business School的数字创新研究大量采用行动研究方法，Oxford的参与式研究传统也强调研究者与实践者的协作。

### 3.5 对标大学说明

- **Cambridge**：Cambridge Judge Business School的Digital Innovation Centre大量采用田野研究和行动研究方法研究企业数字化转型。参考：https://www.jbs.cam.ac.uk/faculty-research/centres/digital-innovation/
- **Oxford**：Oxford的参与式研究传统强调研究者与实践者的协作知识生产。Oxford Internet Institute的多个项目采用行动研究方法研究AI对组织的影响。

### 3.6 实践练习

**任务**：用行动研究的"参与-行动-反思"螺旋，设计一个在你企业推进AI治理试点的研究计划。

**步骤**：
1. 诊断：你观察到的企业AI治理中的核心问题是什么？（写2-3句问题陈述）
2. 行动规划：你打算引入什么干预措施？基于什么理论框架？
3. 数据收集：你打算如何收集干预前后的数据？（至少3种数据源）
4. 评估：你如何判断干预是否有效？预期效果和可能的意外效果各是什么？
5. 反思：你预期从这个过程中能学到什么可推广的知识？

**交付物**：一份行动研究计划（约500字），包含上述五个步骤。

### 3.7 英语轨道材料推荐

- 📄 Reason & Bradbury《Handbook of Action Research》前言和Chapter 1（中等难度）
- 🌐 Wikipedia上"Action Research"词条（简单难度，建立概念）
- 🌐 Oxford OII的working papers中与行动研究相关的文章（较高难度）

---

## 四、R3：混合方法研究（Mixed Methods Research）

> 📍 嵌入技能3 Day 1 | ⏱ 2h | 📘 对标：Oxford定量+定性并重 / Cambridge MPhil双轨

### 4.1 核心概念详解

混合方法研究（Mixed Methods Research, MMR）是将定量（quantitative）和定性（qualitative）方法系统整合的研究方法论。Creswell & Plano Clark（2018）在《Designing and Conducting Mixed Methods Research》中定义混合方法为"在单一研究或研究项目中，收集、分析和整合定量和定性数据的系统方法"。

混合方法的理论基础是实用主义（Pragmatism）。Tashakkori & Teddlie（2010）在《SAGE Handbook of Mixed Methods in Social and Behavioral Research》中论证：实证主义偏重定量方法，解释主义偏重定性方法，而实用主义主张"方法应该服从于研究问题"——如果研究问题既需要"是什么"（what）也需要"为什么"（why），就应该使用混合方法。

**Creswell & Plano Clark的三种核心设计**：

**1. 收敛式设计（Convergent Design）**：定量和定性数据同步收集、并行分析，然后将两类结果进行比较和整合。核心逻辑是"三角验证"（triangulation）——如果定量和定性结果一致，结论的可信度更高；如果不一致，不一致本身就是有价值的发现，需要进一步调查。

适用场景：当你需要交叉验证结果时。例如，定量数据显示AI系统提高了营销转化率，定性访谈揭示用户认为AI建议"更精准"——两者一致，增强了结论的可信度。

**2. 解释性序列设计（Explanatory Sequential Design）**：先收集和分析定量数据，再基于定量发现设计定性研究来解释"为什么"。核心逻辑是"定量发现需要定性理解"。

适用场景：当定量结果出乎意料或需要深入理解时。例如，A/B测试显示AI推荐系统在B2B客户中效果显著，但在B2C客户中没有效果——你需要用定性访谈来理解为什么B2C场景下AI推荐不work。

**3. 探索性序列设计（Exploratory Sequential Design）**：先进行定性探索来识别关键变量和概念，再基于定性发现设计定量研究来验证。核心逻辑是"新领域先探索再验证"。

适用场景：当研究领域较新，缺乏理论框架时。例如，"AI Agent如何改变营销团队的决策流程"是一个新议题，你可能需要先做定性访谈来识别关键变量（如"信任度"、"自主性边界"、"反馈频率"），再设计定量问卷来大规模验证这些变量的影响。

### 4.2 定量+定性整合策略

混合方法的难点不在于"同时用两种方法"，而在于"如何整合"。Morse（1991）提出了整合的三个策略：

- **合并（Merging）**：将定量和定性结果放在同一个表格或图中并排比较，识别一致性和差异。这是收敛式设计的常用策略。
- **解释（Explaining）**：用定性数据解释定量结果。这是解释性序列设计的常用策略。
- **构建（Building）**：用定性发现构建定量研究的理论框架和测量工具。这是探索性序列设计的常用策略。

整合的质量是混合方法研究评价的核心标准。Creswell（2015）在《A Concise Introduction to Mixed Methods Research》中强调："一个混合方法研究如果只是分别做了定量和定性分析但从未将两者整合，那它不是真正的混合方法研究。"

### 4.3 案例分析：AI营销系统效果评估

假设你的Capstone评估一个AI驱动的营销内容Agent系统。采用解释性序列设计：

**第一阶段（定量）**：设计A/B测试，对照组使用人工撰写营销文案，实验组使用AI Agent生成文案。测量指标包括CTR（点击通过率）、转化率、互动率。使用因果推断方法（如DID或propensity score matching）控制混杂因素。预期发现：AI Agent在CTR上提升15%，但在高价值客户群体中转化率没有显著提升。

**第二阶段（定性）**：基于第一阶段的发现，设计半结构化访谈。访谈对象包括：使用AI Agent的营销人员（了解他们的使用体验和信任度）、高价值客户群体的销售代表（了解客户对AI生成内容的反馈）。访谈问题聚焦于"为什么AI Agent在高价值客户中没有提升转化率"——可能的原因包括：高价值客户更重视个性化的人工沟通、AI生成内容缺乏品牌调性的一致性、AI Agent对复杂产品理解不足等。

**整合**：将定量发现（CTR提升但高价值转化率无提升）与定性发现（高价值客户偏好人工沟通、AI内容缺乏品牌一致性）整合，产出设计原则："AI营销Agent应采用分级策略——低价值场景自动化，高价值场景人机协作"。

### 4.4 与博士论文/Capstone的关联

博士论文应采用混合方法设计——定量部分用A/B测试和因果推断评估AI系统效果，定性部分用案例研究和用户访谈理解AI如何改变营销决策流程。这使研究既有统计效力又有实践深度。Oxford DPhil Management要求博士生在第一年完成方法论课程序列，其中混合方法是核心模块。Cambridge MPhil提供SMOOB（定量）和ISO（定性）双轨，但鼓励跨轨整合。

### 4.5 对标大学说明

- **Oxford**：Oxford DPhil Management在第一年安排定量方法、定性方法和混合方法三门必修课，强调方法论的系统训练。Oxford Internet Institute的多项研究采用混合方法研究AI对组织和社会的影响。
- **Cambridge**：Cambridge MPhil按研究方向分为SMOOB（定量方向）和ISO（定性方向），但鼓励学生在论文中跨轨整合。参考：https://www.jbs.cam.ac.uk/programmes/phd/pathways/

### 4.6 实践练习

**任务**：为你的Capstone设计一个混合方法评估方案。

**步骤**：
1. 确定设计类型：收敛式、解释性序列还是探索性序列？为什么选择这种设计？
2. 定量部分：用什么实验或统计方法？衡量什么指标？样本量如何确定？
3. 定性部分：访谈谁？问什么核心问题？用什么分析方法（如thematic analysis）？
4. 整合策略：你打算如何整合定量和定性结果？（合并/解释/构建）
5. 预期贡献：混合方法相比纯定量或纯定性，能为你带来什么额外的insight？

**交付物**：一份混合方法评估方案（约500字），包含设计类型选择、定量方法、定性方法和整合策略。

### 4.7 英语轨道材料推荐

- 📄 Creswell《Research Design: Qualitative, Quantitative, and Mixed Methods Approaches》第五版Chapter 1（中等难度，学术英文入门最佳）
- 🌐 MMIRA混合方法研究协会网站: https://mmira.org/ （简单难度，了解领域概况）
- 📄 Creswell & Plano Clark (2018)《Designing and Conducting Mixed Methods Research》Chapter 4-5（较高难度，三种设计的详细说明）

---

## 五、R4：系统文献综述（Systematic Literature Review / PRISMA）

> 📍 嵌入技能4 Day 1 | ⏱ 2h | 📘 对标：Imperial MRes Systematic Reviews训练

### 5.1 核心概念详解

系统文献综述（Systematic Literature Review, SLR）是一种遵循标准化流程的文献综述方法，通过明确的检索策略、纳入排除标准和质量评估流程，系统化梳理某一研究领域的现状。它与传统叙述性综述（narrative review）的区别在于可重复性和透明度——系统文献综述的流程足够明确，使得另一位研究者按照相同流程能够得到类似的结果。

**PRISMA标准**（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）是系统文献综述的报告标准。Page等人（2021）在BMJ发表的《The PRISMA 2020 statement: an updated guideline for reporting systematic reviews》是最新版本，取代了2009年的原始版本（Moher et al., 2009）。PRISMA 2020包含27个 checklist 条目和一个流程图（flow diagram），用于透明地报告文献检索、筛选和纳入过程。

**PRISMA四步流程详解**：

**1. 检索（Search）**：定义数据库、关键词、时间范围和检索逻辑。

数据库选择：在AI+商业研究领域，核心数据库包括Google Scholar、ACM Digital Library、IEEE Xplore、Web of Science、Scopus、AIS eLibrary（信息系统领域专用）。多数据库交叉检索是必须的——单一数据库的覆盖率通常不超过60%。

关键词设计：关键词应覆盖研究问题的多个维度。以"AI驱动的营销内容生成"为例，关键词矩阵包括：
- AI维度：artificial intelligence, large language model, generative AI, LLM, GPT
- 营销维度：marketing, content generation, copywriting, advertising, campaign
- 方法维度：design science, action research, case study, experiment

检索逻辑：使用布尔运算符组合关键词。例如：("large language model" OR "generative AI") AND ("marketing" OR "advertising") AND ("content generation" OR "copywriting")。

时间范围：根据领域发展速度设定。AI领域变化快，通常设为近5年（2021-2026）；成熟领域可扩展到10年。

**2. 筛选（Screening）**：根据纳入/排除标准筛选文献。

筛选通常分两轮：
- 第一轮（Title/Abstract Screening）：阅读标题和摘要，快速排除明显不相关的文献。两名独立筛选者分别筛选，不一致之处协商解决。
- 第二轮（Full-text Screening）：阅读全文，根据详细标准做最终判断。

纳入/排除标准示例：
- 纳入：发表于同行评审期刊或会议的论文；研究AI在营销中的应用；包含实证评估
- 排除：非英文/中文论文；综述论文（除非是方法学综述）；工作论文/预印本（除非已被接收）

**3. 质量评估（Quality Assessment）**：评估纳入文献的研究质量。

质量评估使用标准化工具。在AI+商业领域，可参考Kitchenham & Charters（2007）提出的质量评估清单，包括：
- 研究问题是否清晰陈述？
- 研究方法是否适合回答研究问题？
- 数据收集是否系统化？
- 分析方法是否恰当？
- 结果是否有证据支持？
- 研究局限是否被讨论？

每篇文献按上述维度评分（如0-3分），总分反映研究质量。低质量文献不排除，但在综合时标注质量等级。

**4. 综合（Synthesis）**：系统化综合发现，识别研究空白。

综合方法包括：
- 叙述性综合（Narrative Synthesis）：用表格和文字总结每篇文献的研究问题、方法、发现和局限。适合异质性较高的文献集。
- 主题分析（Thematic Analysis）：识别文献中的共同主题和分歧。例如，所有研究都发现LLM提升了营销内容生成效率，但在"质量控制"上存在分歧——部分研究认为AI生成内容需要人工审核，部分研究探索自动质量控制方法。
- Meta分析（Meta-Analysis）：用统计方法整合多个研究的效应量。适合研究设计相似、效应量可比较的文献集。在AI+商业领域，由于研究异质性高，Meta分析较少使用。

### 5.2 案例分析：AI商业模式创新的文献综述

针对Capstone中"AI原生营销Agent的商业模式"部分，做一次迷你系统文献综述：

- **检索**：在Google Scholar和ACM DL搜索 `("AI business model" OR "AI-native business" OR "agent economy") AND ("marketing" OR "advertising")`，时间范围2023-2026。初始检索结果约450篇。
- **筛选**：Title/Abstract筛选后剩余40篇；Full-text筛选后纳入12篇核心文献。
- **质量评估**：12篇文献中，8篇发表于顶刊/顶会（如MIS Quarterly, ICIS, HICSS），4篇发表于二级期刊。质量评分7-12分（满分15分）。
- **综合**：识别三个主题——(1) AI-as-a-Service模式的价值捕获机制；(2) outcome-based pricing的实施挑战；(3) Agent经济的信任与治理。研究空白：现有文献多关注AI商业模式的类型学，缺乏对"从传统模式向AI原生模式转型"的过程研究。

### 5.3 与博士论文/Capstone的关联

博士论文的第一章（文献综述）必须采用系统文献综述方法。不是"随便找几篇论文读一读"，而是"有策略地搜索、有标准地筛选、有系统地综合"。Imperial MRes将Systematic Reviews作为方法论训练的核心模块，要求学生在毕业论文中完成一次符合PRISMA标准的系统文献综述。

### 5.4 对标大学说明

- **Imperial MRes**：Imperial的MRes项目将Systematic Reviews作为方法论核心模块训练，包括检索策略设计、质量评估工具使用和综合方法。参考：https://www.imperial.ac.uk/business-school/phd/
- **PRISMA官网**：http://prisma-statement.org/ 提供完整的PRISMA 2020 checklist和flow diagram模板。

### 5.5 实践练习

**任务**：针对你的Capstone研究方向，做一次迷你系统文献综述。

**步骤**：
1. 定义检索关键词（中英文各5个），设计布尔检索逻辑
2. 在Google Scholar上检索，记录初始检索结果数量
3. 定义纳入/排除标准（至少各3条）
4. 按标准筛选出10-15篇核心文献，记录筛选流程（仿PRISMA flow diagram）
5. 用表格总结每篇文献的研究问题、方法、发现和质量评分
6. 识别2-3个研究主题和1-2个研究空白

**交付物**：
- PRISMA flow diagram（仿画）
- 文献总结表（10-15篇）
- 研究空白识别（2-3段文字）

### 5.6 英语轨道材料推荐

- 🌐 PRISMA官网的Checklist和Flow Diagram模板（简单难度，清单式英文）
- 📄 Page et al. (2021) PRISMA 2020论文的Abstract和Figure 1（中等难度）
- 📄 ACM Computing Surveys中的综述论文范例（较高难度，但结构清晰）: https://dl.acm.org/journal/csur

---

## 六、R5：学术论文写作（IMRaD格式）

> 📍 嵌入技能5 Day 7 | ⏱ 2h | 📘 对标：Stanford GSB论文写作要求 / Harvard HBS学术写作

### 6.1 核心概念详解

IMRaD格式（Introduction, Methods, Results, and Discussion）是实证研究论文的标准结构。这一结构最早可追溯到19世纪的科学论文，在20世纪被APA（American Psychological Association）和多数学术期刊采纳为标准。Day & Gastel（2016）在《How to Write and Publish a Scientific Paper》中详细阐述了IMRaD结构的历史和方法论基础。

**IMRaD四部分结构详解**：

**1. Introduction（引言）**

引言的核心功能是回答三个问题：研究什么？为什么重要？贡献是什么？

写作结构遵循"倒三角"——从大到小：
- **领域背景（Broad Background）**：用2-3句话勾勒研究领域的大图景。例如："AI驱动的营销内容生成正在改变企业的营销运作模式（Chen et al., 2024）。"
- **具体问题（Specific Problem）**：从大图景缩小到你要解决的特定问题。例如："然而，现有AI营销系统在处理企业专有知识时存在显著局限——通用LLM无法准确引用企业自有产品文档和客户案例（Edge et al., 2024）。"
- **研究空白（Research Gap）**：明确前人没有做什么。例如："尽管GraphRAG（Edge et al., 2024）在通用知识问答中表现出色，但其在营销知识增强场景中的效果尚未被系统评估。"
- **本文贡献（Contributions）**：用1-3个bullet points明确你的贡献。例如："本文的贡献包括：(1) 设计了一个基于GraphRAG的营销知识增强检索框架；(2) 通过对照实验验证了其在营销问答任务上的效果；(3) 提炼了三条可复用的设计原则。"

**2. Methods（方法）**

方法部分的核心功能是"可复现性"——另一个研究者读完你的方法部分后，能够复现你的研究。

写作要点：
- **研究设计**：说明你采用的研究范式（DSR？行动研究？混合方法？）以及选择理由。
- **数据来源**：数据从哪来？样本量多少？如何收集？如果使用业务数据，说明脱敏处理方式。
- **分析方法**：你用什么方法分析数据？如果是定量分析，说明统计模型和工具（如DoWhy、EconML）。如果是定性分析，说明编码方法（如thematic analysis的编码流程）。
- **评估指标**：明确你衡量什么指标、为什么选择这些指标、指标如何计算。

**3. Results（结果）**

结果部分的核心功能是"用证据说话"——客观呈现研究发现，不加入主观解释。

写作要点：
- **先描述再解释**：先呈现数据（表格、图表），用文字描述数据展示了什么，再在Discussion部分解释数据的含义。
- **图表优先**：能用图表说清楚的不用文字。表格适合精确数据对比，图表适合趋势和模式展示。
- **诚实报告**：报告所有结果，包括不显著的结果和出乎意料的结果。负面结果同样有价值。
- **统计严谨**：定量结果必须报告效应量、置信区间和p值，不能只报告"显著"。

**4. Discussion（讨论）**

讨论部分的核心功能是"这意味着什么"——将结果置于更广阔的理论和实践语境中。

写作要点：
- **结果解释**：你的结果意味着什么？与已有文献一致还是矛盾？如果矛盾，可能的原因是什么？
- **理论贡献**：你的研究对理论有什么推进？是否验证或挑战了现有理论？是否提出了新的理论框架？
- **实践启示**：你的研究对实践者有什么指导意义？他们应该如何应用你的发现？
- **局限性（Limitations）**：诚实陈述研究的局限。局限不是弱点，诚实面对局限是学术成熟的标志。常见的局限包括样本量限制、外部效度限制、时间范围限制等。
- **未来方向（Future Work）**：基于你的发现和局限，下一步可以做什么？这为后来的研究者指明方向。

### 6.2 学术引用规范

学术引用是学术写作的核心规范。APA格式（第7版）是商业和管理领域最常用的引用格式。核心规则：

- **文中引用**：作者-年份制。例如：(Hevner et al., 2004)；如果是直接引用，标注页码：(Hevner et al., 2004, p. 80)。
- **参考文献列表**：按作者姓氏字母排序。格式：Author, A. A. (Year). Title of article. Journal Name, Volume(Issue), Pages. DOI。
- **引用的伦理**：所有非你自己原创的观点、数据、方法都必须引用来源。遗漏引用构成学术不端（plagiarism）。

### 6.3 案例分析：GraphRAG营销系统论文大纲

以Capstone为例，IMRaD论文大纲如下：

**Title**: Design and Evaluation of a GraphRAG-Based Marketing Knowledge Augmentation Framework: A Design Science Research Approach

**Abstract** (200 words): 简述研究问题、方法、发现和贡献。

**Introduction** (~800 words):
- 背景：AI营销内容生成的快速发展
- 问题：通用LLM在企业专有知识场景的局限
- 空白：GraphRAG在营销场景的系统性评估缺失
- 贡献：(1) GraphRAG营销框架设计 (2) 对照实验评估 (3) 设计原则

**Methods** (~1000 words):
- 研究设计：DSR六步流程
- Artifact设计：GraphRAG架构、实体抽取策略、社区检测算法
- 数据：500+产品文档、200+客户案例
- 评估方法：对照实验（GraphRAG vs 向量RAG），20个营销问答任务
- 指标：Factuality, Relevance, Global Reasoning (1-5分，专家评分)

**Results** (~800 words):
- 表1：两种RAG在三个维度上的得分对比
- 图1：不同问题类型的性能差异
- 意外发现：GraphRAG在事实性问答上略低于向量RAG，但在全局推理问答上显著优于向量RAG

**Discussion** (~600 words):
- 结果解释：GraphRAG的优势在于社区摘要支持全局推理，代价是实体抽取引入的噪声
- 设计原则：(1) 社区摘要粒度应根据问题类型动态调整 (2) 实体抽取应引入营销领域知识 (3) 混合检索策略（Global + Local）优于单一策略
- 局限：单一企业案例、专家评估的主观性、未考虑实时更新
- 未来方向：多企业验证、自动化评估方法、增量更新机制

### 6.4 与博士论文/Capstone的关联

Capstone的最终交付物应包括一篇符合IMRaD格式的论文草稿（3000-5000字）。这是从"工程实践者"到"知识创造者"的关键交付物。Stanford GSB PhD项目在第一年就要求学生完成论文写作训练，包括IMRaD结构的系统学习和实践。Harvard HBS DBA同样要求学生在案例研究方法训练之外完成学术论文写作课程。

### 6.5 对标大学说明

- **Stanford GSB PhD**：Stanford GSB的博士项目在第一年安排Research Methods序列，其中包括学术论文写作训练。参考：https://www.gsb.stanford.edu/programs/phd
- **Harvard HBS**：HBS DBA项目要求学生完成学术写作课程，包括案例研究写作和IMRaD论文写作。HBS Digital Initiative提供了大量可参考的学术论文范例。参考：https://digital.hbs.edu/

### 6.6 实践练习

**任务**：为你的Capstone写一个IMRaD格式的论文大纲。

**步骤**：
1. 写一个标题（不超过20个词，包含核心概念和方法）
2. Introduction：研究问题是什么？为什么重要？贡献是什么？（每项2-3句话）
3. Methods：你打算用什么方法？数据从哪来？怎么分析？（每项2-3句话）
4. Results：你预期会发现什么？（2-3个预期发现）
5. Discussion：你的研究有什么局限？有什么理论贡献和实践启示？未来方向是什么？（每项2-3句话）

**交付物**：一份IMRaD论文大纲（约800字），包含Title, Abstract（100字）, 四个部分的outline。

### 6.7 英语轨道材料推荐

- 🌐 APA格式指南官网: https://apastyle.apa.org/ （简单难度，规范性文档）
- 📄 找一篇你感兴趣领域的英文论文（推荐从ACM Computing Surveys或MIS Quarterly中选），分析其IMRaD结构——每部分写了多少字？用什么图表？引用格式是什么？（中等难度）
- 📄 Day & Gastel (2016)《How to Write and Publish a Scientific Paper》Chapter 8-11（中等难度，写作指南经典）

---

## 七、R6：研究伦理与AI治理

> 📍 嵌入技能5 Day 5 | ⏱ 2h | 📘 对标：Oxford Institute for Ethics in AI / Stanford HAI / Imperial Data Ethics

### 7.1 核心概念详解

研究伦理和AI治理是博士研究的底线要求。研究伦理确保研究过程不对参与者造成伤害，AI治理确保AI系统的设计和部署符合社会价值观。在AI+营销领域，两者紧密交织——营销AI系统往往涉及用户数据、算法决策和商业利益，伦理风险尤为突出。

**研究伦理核心原则**：

研究伦理的历史可以追溯到二战后的Nuremberg Code（1947）和后来的Declaration of Helsinki（1964）。在美国，Belmont Report（1979）确立了三条核心原则，至今仍是IRB（Institutional Review Board）审查的基础：

1. **尊重个人（Respect for Persons）**：参与者有权自主决定是否参与研究（autonomy），需要充分知情后自愿同意（informed consent）。对于无法自主决策的群体（如未成年人），需要额外保护。
2. **善行（Beneficence）**：研究应最大化收益、最小化伤害（maximize benefits, minimize harms）。研究者必须评估研究的风险-收益比。
3. **公平正义（Justice）**：研究的负担和收益应公平分配。不能让弱势群体承担过多研究风险，也不能让优势群体独享研究收益。

在AI+营销研究中，这些原则的具体体现包括：
- **知情同意**：如果你用用户行为数据做A/B测试，用户是否知道他们的数据被用于研究？GDPR要求"知情、明确、自由"的同意。
- **隐私保护**：用户数据必须脱敏处理。差分隐私（Differential Privacy, Dwork & Roth, 2014）是一种形式化的隐私保护方法。
- **最小风险**：AI实验不应向用户展示有害或冒犯性内容。

### 7.2 NIST AI RMF四步循环

NIST AI风险管理框架（AI Risk Management Framework, AI RMF）是美国国家标准与技术研究院于2023年1月发布的AI治理框架。它不是强制性法规，而是自愿性框架，但已被大量企业采纳为AI治理的标准参考。

NIST AI RMF的四步循环：

**1. Govern（治理）**：建立AI治理结构、政策、流程。核心是在组织层面建立AI治理委员会，定义AI使用政策和问责机制。关键问题：谁对AI系统的决策负责？AI治理政策是否被全体员工知晓？

**2. Map（映射）**：识别AI系统的上下文和风险。核心是梳理所有AI用例，标注每个用例的风险等级和应用场景。关键问题：你的AI系统在什么场景下被使用？涉及什么数据？可能影响什么人？

**3. Measure（度量）**：评估和量化AI风险。核心是建立AI评估指标体系，包括准确性、公平性、安全性、隐私性的量化指标。关键问题：你的AI系统在公平性指标上的得分是多少？是否有可测量的偏见？

**4. Manage（管理）**：优先处理并分配资源应对风险。核心是制定风险缓解措施，建立持续监控机制。关键问题：高风险AI系统的缓解措施是什么？谁负责监控？

### 7.3 EU AI Act风险分级

EU AI Act（欧盟人工智能法案）于2024年正式通过，是全球首部全面的AI监管法律。它按风险将AI系统分为四级：

| 风险等级 | 定义 | 监管要求 | 营销AI示例 |
|---------|------|---------|----------|
| **不可接受风险** | 违背基本权利的AI | 禁止使用 | 利用AI进行操控性营销、针对弱势群体的剥削性广告 |
| **高风险** | 对健康、安全或基本权利有重大影响的AI | 严格监管（风险评估、数据治理、透明度、人工监督、注册） | 信用评分AI（如营销中基于AI的客户信用评估） |
| **有限风险** | 对基本权利影响有限的AI | 透明度义务（用户需知道在与AI交互） | AI客服聊天机器人、AI生成的营销内容（需标注"AI生成"） |
| **最小风险** | 对基本权利影响微小的AI | 自由使用（鼓励自律） | 垃圾邮件过滤、推荐系统（无个人敏感数据时） |

### 7.4 算法偏见评估

算法偏见是AI治理的核心议题。Barocas & Selbst（2016）在California Law Review论文《Big Data's Disparate Impact》中系统分析了算法歧视的法律和伦理维度。偏见来源包括：

- **训练数据偏见**：历史数据中的歧视被AI放大。例如，如果历史营销数据中某群体被系统性地忽略，AI模型会延续这种忽略。
- **算法偏见**：模型设计中的系统性偏差。例如，推荐算法可能偏好热门内容，导致长尾内容被边缘化。
- **部署偏见**：应用场景中的语境偏差。例如，AI营销系统在不同文化语境中可能产生冒犯性内容。

偏见评估方法：Mitchell等人（2019）提出的Model Cards（模型卡片）是一种标准化的模型透明度报告，要求开发者报告模型在不同群体上的性能差异。Fairlearn（微软开源）和AIF360（IBM开源）是常用的偏见评估工具。

### 7.5 案例分析：营销AI系统的伦理自查

假设你的Capstone涉及一个AI驱动的用户定向营销系统。伦理自查：

**研究伦理**：
- 知情同意：你的A/B测试是否告知用户？如果使用历史用户数据，数据使用是否符合隐私政策？→ 需要确保数据脱敏，并获得数据使用授权。
- 隐私保护：用户画像数据是否包含敏感信息（如种族、宗教、健康状况）？→ 需要移除敏感属性，或使用差分隐私技术。
- 最小风险：AI生成的营销内容是否可能对某些用户群体造成伤害？→ 需要内容审核机制。

**NIST AI RMF评估**：
- Govern：你的企业是否有AI治理委员会？→ 如果没有，Capstone可以建议设立。
- Map：你的AI系统涉及哪些用例？风险等级是什么？→ 用户定向营销涉及个人数据，可能是"高风险"或"有限风险"。
- Measure：你的AI系统在不同用户群体上的性能差异是多少？→ 需要测量公平性指标（如demographic parity, equalized odds）。
- Manage：高风险用例的缓解措施是什么？→ 需要人工审核机制、用户反馈渠道和定期偏见审计。

**EU AI Act合规**：
- 你的AI营销系统属于"有限风险"（如果是聊天机器人或AI生成内容，需透明度标注）还是"高风险"（如果涉及信用评估或敏感数据处理，需严格合规）？

### 7.6 与博士论文/Capstone的关联

在Capstone中涉及用户数据时，需要通过伦理审查自查。在部署AI系统时，需要参照NIST AI RMF或EU AI Act设计治理框架。Oxford Institute for Ethics in AI、Stanford HAI和Imperial的Data Management & Ethics课程是这一领域的标杆。

### 7.7 对标大学说明

- **Oxford Institute for Ethics in AI**：Oxford的AI伦理研究所提供从人文社科角度研究AI对商业和社会影响的独特视角。参考：https://www.oii.ox.ac.uk/
- **Stanford HAI**：Stanford以人为本AI研究所（HAI）整合了技术、伦理和政策研究。参考：https://hai.stanford.edu/
- **Imperial**：Imperial的Data Management & Ethics模块覆盖数据治理和AI伦理。参考：https://www.imperial.ac.uk/business-school/programmes/msc-business-analytics/

### 7.8 实践练习

**任务**：为你的Capstone做一次研究伦理和AI治理自查。

**步骤**：
1. 研究伦理：你的研究是否涉及用户数据？如果是，你如何获得知情同意？如何保护隐私？
2. 偏见评估：你的AI系统可能产生什么偏见？你打算用什么方法检测？（列出至少2种偏见来源和1种检测方法）
3. NIST AI RMF：用四步循环评估你的系统——Govern/Map/Measure/Manage各处于什么水平？有什么改进建议？
4. EU AI Act：你的系统属于哪一级风险？需要满足什么合规要求？

**交付物**：一份研究伦理和AI治理自查报告（约500字），包含上述四个维度的分析。

### 7.9 英语轨道材料推荐

- 🌐 NIST AI RMF的Executive Summary（中等难度，政策英文）: https://www.nist.gov/itl/ai-risk-management-framework
- 🌐 EU AI Act官方页面的Risk Classification部分（中等难度）: https://artificialintelligenceact.eu/
- 📄 Barocas & Selbst (2016) 论文的Introduction部分（较高难度，法律英文）
- 🌐 Anthropic对齐研究（较高难度，前沿研究）: https://www.anthropic.com/research

---

## 八、模块R与五技能的嵌入关系

| 模块R | 嵌入技能 | 嵌入时机 | 核心问题 | 产出物 | 对标大学 |
|:-----:|:--------:|---------|---------|--------|---------|
| **R1 DSR** | 技能1 Day 1 | 学表示学习理论时 | "我学的东西怎么变成一篇论文？" | 一页纸DSR研究计划 | NUS IS PhD / Imperial MRes |
| **R2 行动研究** | 技能2 Day 4 | 学AI治理框架时 | "我怎么把框架用到公司，同时产出学术知识？" | 行动研究计划（五步螺旋） | Cambridge / Oxford |
| **R3 混合方法** | 技能3 Day 1 | 学因果推断基础时 | "我怎么用混合方法让研究更严谨？" | 混合方法评估方案 | Oxford / Cambridge |
| **R4 PRISMA** | 技能4 Day 1 | 学商业模式类型时 | "学术界已经研究了什么？还有什么空白？" | 迷你系统文献综述（PRISMA流程图+文献表） | Imperial MRes |
| **R5 IMRaD** | 技能5 Day 7 | 学端到端交付时 | "我怎么把工程成果写成学术论文？" | IMRaD论文大纲（800字） | Stanford GSB / Harvard HBS |
| **R6 研究伦理** | 技能5 Day 5 | 学安全防护时 | "我的研究涉及伦理问题吗？怎么审查？" | 研究伦理和AI治理自查报告 | Oxford / Stanford HAI / Imperial |

**嵌入原则**：模块R不单独安排时间、不单独检查、不单独评分。它的存在方式是"在你学每个技能的时候，用研究方法论的视角重新审视你学到的东西"。就像学做饭时不仅学会"怎么做菜"，还顺便学会了"怎么写食谱"——不是"先花3个月学写食谱，再开始学做饭"。

---

## 九、知识问答（15题）

| # | 问题 | 难度 | 答案要点 |
|:--:|------|:----:|---------|
| Q1 | DSR的Peffers六步流程是什么？与普通工程开发的区别在哪？ | ⭐ | 六步：问题识别→目标定义→设计开发→演示→评估→传播。区别：DSR要求产出可复用的设计原则，不仅是可运行的系统；DSR的评估必须基于理论框架，不仅是用户反馈 |
| Q2 | Hevner的设计科学cycle包含哪三个核心活动？artifact的四种类型是什么？ | ⭐ | 三活动：build, evaluate, theorize。四类型：constructs, models, methods, instantiations（March & Smith, 1995） |
| Q3 | 行动研究的"参与-行动-反思"螺旋包含哪五个步骤？它和案例研究的核心区别是什么？ | ⭐ | 五步：诊断→行动规划→行动实施→评估→反思学习（Susman & Evered, 1978）。区别：行动研究中研究者是干预者，案例研究中研究者是旁观者（Yin, 2018） |
| Q4 | Creswell & Plano Clark的三种混合方法设计分别是什么？各适用什么场景？ | ⭐⭐ | 收敛式（同步收集比较，适合三角验证）、解释性序列（先定量后定性，适合解释"为什么"）、探索性序列（先定性后定量，适合新领域探索） |
| Q5 | 混合方法中"整合"的三种策略是什么？为什么整合是混合方法的核心难点？ | ⭐⭐ | 合并（并排比较）、解释（定性解释定量）、构建（定性构建定量框架）。难点在于定量和定性的范式差异需要研究者同时精通两种方法（Morse, 1991） |
| Q6 | PRISMA四步流程是什么？系统文献综述和叙述性综述的核心区别在哪？ | ⭐ | 四步：检索→筛选→质量评估→综合（Page et al., 2021）。区别：系统综述有明确的检索策略和纳入排除标准，可重复；叙述性综述主观性强，不可重复 |
| Q7 | 在PRISMA检索中，如何设计关键词矩阵？为什么要使用多数据库交叉检索？ | ⭐⭐ | 关键词矩阵覆盖研究问题的多个维度（AI维度×营销维度×方法维度），用布尔运算符组合。多数据库交叉检索是因为单一数据库覆盖率通常不超过60% |
| Q8 | IMRaD格式的四个部分分别是什么？Introduction部分应该遵循什么写作结构？ | ⭐ | Introduction, Methods, Results, Discussion。Introduction遵循"倒三角"结构：领域背景→具体问题→研究空白→本文贡献 |
| Q9 | Discussion部分应该包含哪些内容？为什么"局限性"是Discussion的重要组成部分？ | ⭐⭐ | 结果解释、理论贡献、实践启示、局限性、未来方向。局限性体现学术诚实性，帮助读者判断结论的适用边界，指明后续研究方向 |
| Q10 | Belmont Report的三条研究伦理原则是什么？在AI+营销研究中如何体现？ | ⭐ | 尊重个人（知情同意）、善行（风险-收益评估）、公平正义（负担收益公平分配）。营销研究中体现为：用户数据需知情同意、A/B测试需评估用户风险、偏见评估确保公平 |
| Q11 | NIST AI RMF的四步循环是什么？如果用这四步评估你企业的AI系统，各处于什么水平？ | ⭐⭐ | Govern→Map→Measure→Manage。需结合自己企业现状评估每个维度的成熟度（通常企业在Govern和Measure上最弱） |
| Q12 | EU AI Act按风险将AI系统分为哪四级？你的营销AI系统属于哪一级？为什么？ | ⭐⭐ | 不可接受风险（禁止）、高风险（严格监管）、有限风险（透明度义务）、最小风险（自由使用）。营销AI通常属于有限风险（如AI客服需透明度标注）或高风险（如涉及信用评估） |
| Q13 | 算法偏见的三种来源是什么？如何用Model Cards方法评估偏见？ | ⭐⭐ | 训练数据偏见、算法偏见、部署偏见（Barocas & Selbst, 2016）。Model Cards（Mitchell et al., 2019）要求报告模型在不同群体上的性能差异，作为偏见透明度报告 |
| Q14 | 用DSR六步框架，为你的Capstone研究方向写一个一页纸的研究计划。 | ⭐⭐⭐ | 需完整包含六步，核心是区分"做系统"和"产出设计原则" |
| Q15 | 选择一种混合方法设计，为你的Capstone设计一个评估方案。需说明定量和定性部分如何整合。 | ⭐⭐⭐ | 需明确设计类型选择理由、定量方法、定性方法、整合策略和预期贡献 |

---

## 十、综合作业：用DSR + PRISMA + IMRaD完成完整研究计划

### 10.1 作业描述

综合运用模块R的六个子模块，完成一份完整的Capstone研究计划。这份计划是你后续Capstone执行的蓝图。

### 10.2 作业结构

**第一部分：系统文献综述（PRISMA）**（约1000字）
1. 定义检索关键词和检索逻辑
2. 记录检索结果数量和筛选流程（仿PRISMA flow diagram）
3. 列出10-15篇核心文献的总结表
4. 识别2-3个研究主题和1-2个研究空白

**第二部分：DSR研究框架**（约800字）
1. 问题陈述（基于文献综述中的研究空白）
2. 解决方案目标（2-3个可验证目标）
3. 设计与开发计划（关键设计决策及理论依据）
4. 评估方案（指标、对照组、方法）

**第三部分：混合方法评估设计**（约500字）
1. 选择混合方法设计类型并说明理由
2. 定量部分设计
3. 定性部分设计
4. 整合策略

**第四部分：IMRaD论文大纲**（约800字）
1. Title和Abstract（100字）
2. Introduction outline（研究问题、空白、贡献）
3. Methods outline（研究设计、数据、分析）
4. 预期Results（2-3个预期发现）
5. Discussion outline（理论贡献、实践启示、局限、未来方向）

**第五部分：研究伦理与AI治理自查**（约400字）
1. 研究伦理自查（知情同意、隐私保护、风险-收益评估）
2. NIST AI RMF四步评估
3. EU AI Act风险分级判断
4. 算法偏见评估计划

### 10.3 评分标准（满分100分）

| 维度 | 分值 | 评分标准 |
|------|:----:|---------|
| PRISMA系统文献综述 | 20 | 检索策略合理（5）、筛选流程完整（5）、文献总结表规范（5）、研究空白识别精准（5） |
| DSR研究框架 | 20 | 问题陈述清晰（5）、目标可验证（5）、设计决策有理论依据（5）、评估方案严谨（5） |
| 混合方法设计 | 15 | 设计类型选择合理（5）、定量定性方法恰当（5）、整合策略明确（5） |
| IMRaD论文大纲 | 25 | 结构完整（5）、研究问题清晰（5）、方法可复现（5）、预期发现合理（5）、讨论有深度（5） |
| 研究伦理与AI治理 | 10 | 伦理自查全面（3）、NIST评估到位（3）、EU AI Act判断准确（2）、偏见评估有方法（2） |
| 学术规范 | 10 | 引用格式正确（3）、学术语言准确（3）、逻辑连贯（4） |

### 10.4 交付物清单

- [ ] 完整研究计划文档（约3500字，中英文混合）
- [ ] PRISMA flow diagram（图表）
- [ ] 文献总结表（表格）
- [ ] IMRaD论文大纲

---

## 十一、费曼学习法演练

### 演练主题：向非学术背景的工程师解释"为什么工程实践需要研究方法论"

**场景**：你的一位工程师同事问你："我们每天都在做系统、写代码、解决实际问题，为什么还需要学什么'研究方法论'？那不是搞学术的人的事吗？"

**费曼解释法——用最简单的语言解释最本质的道理**：

---

"想象你做了一道很好吃的菜。

工程师的做法是：做完，吃了，觉得不错，下次凭感觉再做一次。

研究方法论的作用是：把这道菜写成一份**食谱**——用了什么食材、每样放多少、先炒什么后炒什么、为什么这道工序让菜更好吃。

有了食谱，别人也能照着做出来。你的经验不再是'只在你脑子里'的东西，而是变成了**可以被别人学习、改进、传播的知识**。

具体来说，研究方法论给了你几样工具：

**第一，DSR（设计科学研究）教你'问对问题'**。不是'我要做一个系统'，而是'我要解决什么问题，我的解决方案比现有方案好在哪里，别人能从我的设计中学到什么'。这就是从'做了个东西'到'创造了知识'的转变。

**第二，PRISMA教你'看清全貌'**。在你动手之前，先系统地搜索'别人已经做了什么'。不是随便Google几篇论文，而是用标准化的流程确保你没有遗漏重要的工作。这避免你'重新发明轮子'，也帮你找到真正的研究空白。

**第三，IMRaD教你'说清楚'**。把你做的事用Introduction-Methods-Results-Discussion的结构写出来，让另一个没见过你系统的人也能理解你做了什么、为什么这样做、发现了什么。这不是写技术文档——技术文档教人'怎么用'，学术论文教人'为什么这这样做是对的'。

**第四，研究伦理教你'守住底线'**。你的AI系统用到了用户数据？你的A/B测试可能影响用户行为？你的算法可能对某些群体不公平？研究伦理框架（NIST AI RMF、EU AI Act）给你一套系统化的检查清单。

所以，研究方法论不是'学术象牙塔里的东西'。它是让**你的工程经验从'个人技能'变成'公共知识'的转化工具**。这就是博士和硕士的区别——硕士学会'做'，博士学会'把做的过程变成可传播的知识'。"

---

**自我检测**：用上面的解释法，试着向一个完全不懂数据科学的人解释"什么是系统文献综述"。如果你能用3分钟讲清楚，说明你真正理解了PRISMA的核心。

---

## 十二、推荐资源清单

### 12.1 核心论文与教材

| 资源 | 作者/来源 | 类型 | URL |
|------|----------|------|-----|
| DSR六步流程论文 | Peffers et al. (2007) | 论文 | https://desrist.org/desrist/files/peffers2007.pdf |
| Design Science in IS Research | Hevner et al. (2004) MIS Quarterly | 论文 | https://www.jstor.org/stable/25148625 |
| Handbook of Action Research | Reason & Bradbury (2008) SAGE | 教材 | https://uk.sagepub.com/en-gb/eur/handbook-of-action-research/book245073 |
| Research Design (5th ed.) | Creswell (2018) SAGE | 教材 | SAGE出版 |
| Designing Mixed Methods Research | Creswell & Plano Clark (2018) | 教材 | SAGE出版 |
| PRISMA 2020 Statement | Page et al. (2021) BMJ | 论文 | http://prisma-statement.org/ |
| Case Study Research (6th ed.) | Yin (2018) SAGE | 教材 | SAGE出版 |
| How to Write & Publish Scientific Papers | Day & Gastel (2016) | 教材 | Cambridge University Press |
| Causal Inference | Imbens & Rubin (2015) | 教材 | Cambridge University Press |
| Big Data's Disparate Impact | Barocas & Selbst (2016) | 论文 | California Law Review |
| Model Cards | Mitchell et al. (2019) | 论文 | https://arxiv.org/abs/1810.03777 |

### 12.2 框架与标准

| 资源 | 来源 | URL |
|------|------|-----|
| NIST AI RMF | NIST | https://www.nist.gov/itl/ai-risk-management-framework |
| EU AI Act | 欧盟 | https://artificialintelligenceact.eu/ |
| PRISMA声明 | PRISMA Group | http://prisma-statement.org/ |
| APA格式指南（第7版） | APA | https://apastyle.apa.org/ |
| Belmont Report | OHRP | https://www.hhs.gov/ohrp/ |
| GDPR | 欧盟 | https://gdpr.eu/ |

### 12.3 对标大学资源

| 大学 | 资源 | URL |
|------|------|-----|
| NUS IS PhD | 博士项目主页 | https://www.comp.nus.edu.sg/programmes/pg/phdis/ |
| Oxford DPhil Management | 博士项目主页 | https://www.sbs.ox.ac.uk/programmes/doctoral/dphil-management |
| Oxford Internet Institute | AI伦理研究 | https://www.oii.ox.ac.uk/ |
| Cambridge Judge PhD pathways | 博士路径 | https://www.jbs.cam.ac.uk/programmes/phd/pathways/ |
| Cambridge Digital Innovation | 数字创新研究 | https://www.jbs.cam.ac.uk/faculty-research/centres/digital-innovation/ |
| Imperial MSc Business Analytics & AI | 硕士项目 | https://www.imperial.ac.uk/business-school/programmes/msc-business-analytics/ |
| Imperial PhD | 博士项目 | https://www.imperial.ac.uk/business-school/phd/ |
| Stanford GSB PhD | 博士项目 | https://www.gsb.stanford.edu/programs/phd |
| Stanford HAI | 以人为本AI研究所 | https://hai.stanford.edu/ |
| Harvard HBS Digital Initiative | 数字倡议 | https://digital.hbs.edu/ |
| Harvard HBS Working Papers | 工作论文 | https://www.hbs.edu/research/Pages/publications.aspx |

### 12.4 工具与平台

| 资源 | 用途 | URL |
|------|------|-----|
| Google Scholar | 文献检索 | https://scholar.google.com/ |
| ACM Digital Library | CS文献检索 | https://dl.acm.org/ |
| AIS eLibrary | 信息系统文献 | https://aisel.aisnet.org/ |
| MMIRA | 混合方法研究协会 | https://mmira.org/ |
| Fairlearn（微软） | 算法偏见评估 | https://fairlearn.org/ |
| AIF360（IBM） | 算法偏见评估 | https://aif360.res.ibm.com/ |
| Anthropic安全研究 | AI对齐与安全 | https://www.anthropic.com/research |

### 12.5 英语轨道专用资源

| 资源 | 难度 | 说明 |
|------|:----:|------|
| PRISMA官网Checklist | ⭐ | 清单式英文，适合入门 |
| Creswell《Research Design》Ch.1 | ⭐⭐ | 学术英文入门最佳教材 |
| Peffers et al. (2007) Abstract & Introduction | ⭐⭐ | DSR核心论文，学术英文 |
| NIST AI RMF Executive Summary | ⭐⭐ | 政策英文，框架性文档 |
| Wikipedia "Action Research" 词条 | ⭐ | 简单难度，建立概念 |
| ACM Computing Surveys 综述论文 | ⭐⭐⭐ | 综述论文结构清晰，适合学习IMRaD |
| Barocas & Selbst (2016) Introduction | ⭐⭐⭐ | 法律英文，较高难度 |

---

## 附录：模块R学习路线图

```
预科 Day 6：研究方法论入门
  ↓ 建立"学术研究 vs 工程实践"的基本认知
技能1 Day 1：R1 DSR
  ↓ 学会用DSR框架定义研究问题
技能2 Day 4：R2 行动研究
  ↓ 学会在企业实践中产出学术知识
技能3 Day 1：R3 混合方法
  ↓ 学会用定量+定性整合评估
技能4 Day 1：R4 PRISMA
  ↓ 学会用系统文献综述发现研究空白
技能5 Day 5：R6 研究伦理
  ↓ 学会做伦理审查和AI治理自查
技能5 Day 7：R5 IMRaD
  ↓ 学会把工程成果写成学术论文
Capstone：整合R1-R6
  ↓ DSR框架 + PRISMA综述 + 混合方法评估 + IMRaD论文 + 伦理自查
  → 产出一篇可投稿的论文草稿
```

**模块R的终极目标**：不是让你成为研究方法论专家，而是让你具备**将工程实践转化为学术贡献的能力**。这是从"工程实践者"到"知识创造者"的认知跃迁，也是博士训练的核心价值。

---

*本教材为AI原生化商业博士课程v4.0独立教材模块，由Claude基于全球七校博士研究方法论训练标准编制。*  
*最后更新：2026-07-16*  
*版本：v4.0*
