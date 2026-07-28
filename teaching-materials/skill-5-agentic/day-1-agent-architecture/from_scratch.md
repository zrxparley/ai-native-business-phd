# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能5 Agentic系统工程 · Day 1 Agent系统架构设计
> **scratch 哲学**：不调 LangChain/LangGraph，手写 ReAct agent loop，从 thought-action-observation 循环直译到纯 Python。

## scratch_topic

本单元 from-scratch 主题：**手写 ReAct agent loop + 工具分发器**。对应 rohitg00 P14/01 The Agent Loop + P14/06 Tool Use and Function Calling。notes.md 用 LangChain `@tool` + LangGraph 构建 ReAct Agent，本层把 agent 的"感知-思考-行动-观察"循环拆到裸 Python：状态机 + 工具注册表 + JSON 解析 + 终止判定，让"Agent 如何决策"不再是 LangChain 的黑箱，而是可逐行审计的 50 行控制流。

## core_algorithm

ReAct（Reasoning + Acting）把 LLM 的推理与工具调用交织为一个循环。形式化：状态 $s_t = (\text{history}, \text{pending})$，每步 LLM 生成一个"思考-行动"对 $(\text{thought}_t, \text{action}_t)$，其中 $\text{action}_t = \text{tool}_k(\text{args})$ 或 $\text{finish}(\text{answer})$。环境返回观察 $\text{obs}_t = \text{tool}_k(\text{args})$ 的执行结果，拼入历史：

$$\text{history}_{t+1} = \text{history}_t \oplus (\text{thought}_t, \text{action}_t, \text{obs}_t)$$

循环终止条件：LLM 输出 `finish` 或达到 `max_steps`。工具分发的关键是**结构化解析**：LLM 输出文本中提取 JSON `{"tool": name, "args": {...}}`，校验 schema 后路由到注册表 `registry[name]`。这个分发器是所有 Agent 框架（LangChain/LangGraph/AutoGen）的最小公共内核--理解了它，就理解了 Agent 的"行动"机制。

ReAct 的本质优势：**延迟推理**。LLM 不必一开始就规划全部步骤，而是在每步根据最新观察重新决策，适合信息逐步揭示的营销场景（先查库存，再算折扣，最后生成文案）。代价是 $O(\text{steps})$ 次 LLM 调用，成本随步数线性增长--这就是 notes.md 讲的"成本不可控"的数学根源。

## code_artifact

```python
import re

def parse_action(llm_text):
    # extract {"tool":..., "args":...} or {"finish":...}
    # use eval with sandboxed builtins (json not in from-scratch whitelist)
    m = re.search(r'\{[^{}]*\}', llm_text)
    if not m:
        return None
    try:
        return eval(m.group(0), {"__builtins__": {}}, {})
    except Exception:
        return None

def react_loop(llm_fn, tools, query, max_steps=5):
    # llm_fn(history, query) -> text; tools: dict name->callable
    history = []
    for step in range(max_steps):
        text = llm_fn(history, query)
        history.append({"thought": text})
        call = parse_action(text)
        if call is None:
            history.append({"obs": "parse_error"})
            continue
        if "finish" in call:
            return call["finish"], history
        name = call.get("tool")
        args = call.get("args", {})
        if name not in tools:
            history.append({"obs": f"unknown_tool:{name}"})
            continue
        try:
            obs = tools[name](**args)
        except Exception as e:
            obs = f"error:{e}"
        history.append({"action": name, "args": args, "obs": obs})
    return None, history

# verification_property:
#   react_loop terminates within max_steps; returns finish answer or None;
#   every action in history has a matching observation
if __name__ == "__main__":
    script = [
        '{"tool":"calc","args":{"x":100,"y":0.1}}',
        '{"finish":"final"}',
    ]
    def fake_llm(hist, q):
        return script[len([h for h in hist if "thought" in h])]
    tools = {"calc": lambda x, y: x * y}
    ans, hist = react_loop(fake_llm, tools, "query", max_steps=5)
    assert ans == "final", "loop must return finish answer"
    # every action has an observation
    actions = [h for h in hist if "action" in h]
    obs = [h for h in hist if "obs" in h]
    assert len(actions) + 1 == len(hist), "history must interleave thought/action/obs"
```

**verification_property**: react_loop 在 `max_steps` 内终止；返回 `finish` 答案或 None；history 中每个 action 有对应 observation（思考-行动-观察三元组完整）。

## connection_to_unit

1. **库 vs 手写的抽象层**：notes.md 用 LangChain `AgentExecutor` 一行跑 ReAct，from-scratch 版把 `AgentExecutor` 拆成"解析-分发-观察-拼历史"四步裸 Python；LangChain 的 `@tool` 装饰器对应这里的 `tools` 字典，`AgentExecutor.invoke` 对应这里的 `react_loop` 主循环。
2. **工具契约对比**：notes.md 强调 docstring 是 LLM 看到的"接口契约"，from-scratch 版用 `parse_action` 的 JSON 解析把这个契约显式化--LLM 必须输出 `{"tool":name,"args":{}}`，否则 `parse_error`。这暴露了"结构化输出"是 Agent 可靠性的硬约束（库内部用 function calling API 隐藏了这点）。
3. **记忆机制对比**：notes.md 讲 LangGraph `MemorySaver` 按 `thread_id` 隔离会话，from-scratch 版的 `history` 列表就是短期记忆的最简形式--每个 `thread_id` 对应一个 `history` 列表，长期记忆需外接向量库（本 from-scratch 不实现，留给 day-2）。
4. **成本可观测性**：LangChain 的 token 计费藏在回调里，from-scratch 版的 `for step in range(max_steps)` 让"步数=LLM 调用次数"一目了然，直接对应 notes.md "成本不可控"的担忧--研究者能精确算出"每多一步多花多少钱"。

## deep_dive_links

- [P14/01 The Agent Loop - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/01-the-agent-loop/README.md) - agent loop from scratch，本单元的核心理论锚点
- [P14/06 Tool Use and Function Calling - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/06-tool-use-and-function-calling/README.md) - 工具调用与函数分发机制

## exercises

1. 在本单元 `starter.ipynb` TODO（LangChain ReAct Agent）运行后，用上面的 `react_loop` 接入同一个 `calculate_roi` 工具和同一个营销查询，对比两版的输出与步数。提示：用 mock LLM（预设脚本）替代真实 LLM 调用，聚焦控制流验证。
2. 扩展 `parse_action` 支持"多工具并行调用"（一次输出 `{"tools":[...]}` 数组），对应 rohitg00 P13/03 Parallel and Streaming Tool Calls。观察并行 vs 串行的步数差异。
3. 实现"Reflection"变体：在 `react_loop` 的 `finish` 前，加一个 `critic` 步骤对答案打分，低于阈值则继续循环。对应 notes.md 讲的"评估者-优化者"循环，本 from-scratch 让你看到多花的 token 在哪。
4. TODO: 在 `practice.md` 的工具设计练习中，为本 from-scratch 估计器添加"工具 schema 校验"（用 `jsonschema` 或手写类型检查），拒绝参数类型不符的调用。这是 LangChain `@tool` 自动做的事，from-scratch 让你显式实现。
