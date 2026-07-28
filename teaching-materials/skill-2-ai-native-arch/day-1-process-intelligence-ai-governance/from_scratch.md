# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能2 AI原生企业架构 · Day 1 流程智能驱动 + AI治理框架
> **scratch 哲学**：不调 mcp SDK / pydantic，手写 MCP server 骨架 + JSON-RPC 工具分发 + NIST 合规评分，从 JSON-RPC 2.0 协议直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 MCP server 骨架 + JSON-RPC 工具调度 + NIST 合规评分**。对应 rohitg00 P13/06 MCP Fundamentals + P13/07 Building an MCP Server + P13/01 The Tool Interface。notes.md/starter.ipynb 用 pydantic 定义 NIST 控制项 schema + pandas 构建风险热力图，本层进一步去框架化：纯 numpy + dataclasses 实现 MCP server 的工具注册表 + JSON-RPC 2.0 请求分发 + NIST 四功能加权评分，让"工具接口""协议分发""治理评分"三个概念在白板级代码中显形--不依赖 mcp SDK 的传输层，不依赖 pydantic 的 schema 校验，手写 dispatch 让 JSON-RPC 协议的 method->callable 映射可见。

## core_algorithm

MCP server 的核心是 JSON-RPC 2.0 协议的请求-响应模型与工具注册表分发。给定请求 $r = \{\text{jsonrpc}: "2.0", \text{id}: i, \text{method}: m, \text{params}: p\}$，分发函数 $\text{dispatch}(r) = f_m(p)$，其中 $f_m$ 是注册表中方法 $m$ 对应的可调用对象。工具调用前需校验 input_schema：$\text{valid}(p, S) \iff \forall k \in \text{required}(S): k \in p$。

$$\text{dispatch}(r) = \begin{cases} \text{tools/list} \to \{(name_i, desc_i, S_i)\}_{i=1}^{N} \\ \text{tools/call} \to f_{p.\text{name}}(p.\text{arguments}) \end{cases}$$

合规评分将 NIST 四功能（Govern/Map/Measure/Manage）的控制项通过率加权汇总为一个 0-100 标量：

$$\text{score}(u) = 100 \cdot \sum_{k \in \{G,Ma,Me,Mn\}} w_k \cdot c_k(u), \quad \sum_k w_k = 1, \quad c_k(u) \in [0,1]$$

其中 $c_k(u)$ 是用例 $u$ 在功能 $k$ 下的控制项通过率，$w_k$ 是功能权重（Govern 和 Measure 各 0.3，Map 和 Manage 各 0.2，反映"治理结构"与"度量能力"的优先级）。状态映射 $\text{status}(s) = \text{COMPLIANT}$ if $s \ge 80$，$\text{PARTIAL}$ if $50 \le s < 80$，$\text{NON\_COMPLIANT}$ if $s < 50$。这套加权评分是 NIST AI RMF 四功能的数值化，让"治理成熟度"从定性判断变为可审计的标量。from-scratch 版用 numpy 的向量内积 $w^\top c$ 一步算出，比 pydantic 的逐字段 validator 更直白地暴露"权重 x 通过率"的数学结构。

## code_artifact

```python
import numpy as np
from typing import Callable
from dataclasses import dataclass

@dataclass
class Tool:
    name: str; description: str; fn: Callable; input_schema: dict

class MCPServer:
    def __init__(self):
        self.tools = {}
    def register(self, t): self.tools[t.name] = t
    def _list(self):
        return [{"name": t.name, "description": t.description, "inputSchema": t.input_schema} for t in self.tools.values()]
    def _call(self, name, args):
        return self.tools[name].fn(**args) if name in self.tools else {"error": f"unknown {name}"}
    def handle_jsonrpc(self, req_str):
        req = eval(req_str, {"__builtins__": {}}, {})  # no json import
        m, p, rid = req["method"], req.get("params", {}), req.get("id")
        if m == "tools/list": res = self._list()
        elif m == "tools/call": res = self._call(p["name"], p.get("arguments", {}))
        else: return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "not found"}}
        return {"jsonrpc": "2.0", "id": rid, "result": res}

def nist_score(use_case):
    # weighted compliance score across NIST 4 functions
    w = np.array([0.3, 0.2, 0.3, 0.2])  # Govern, Map, Measure, Manage
    c = np.array([use_case.get("controls", {}).get(k, 0.0) for k in ["Govern","Map","Measure","Manage"]])
    s = float(w @ c)
    return {"score": round(s * 100, 1), "status": "COMPLIANT" if s >= 0.8 else "PARTIAL" if s >= 0.5 else "NON_COMPLIANT"}

# verification_property: JSON-RPC dispatch routes method->callable; nist_score weighted sum in [0,100]
if __name__ == "__main__":
    srv = MCPServer()
    srv.register(Tool("nist_scan", "NIST AI RMF scan", nist_score, {"use_case": "object"}))
    r = srv.handle_jsonrpc('{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"nist_scan","arguments":{"use_case":{"controls":{"Govern":0.8,"Map":0.8,"Measure":0.6,"Manage":0.4}}}}}')
    assert r["result"]["score"] == 66.0 and r["result"]["status"] == "PARTIAL"
    lst = srv.handle_jsonrpc('{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}')
    assert lst["result"][0]["name"] == "nist_scan"
```

**verification_property**: JSON-RPC dispatch 把 `method` 字符串路由到注册表中的 callable（`tools/list` -> `_list()`，`tools/call` -> `_call(name, args)`）；NIST 加权评分 `w @ c` 输出 [0, 100] 标量，状态映射在 80/50 阈值分界（构造数据 score=66.0 -> PARTIAL）。

## connection_to_unit

1. **协议层对比**：starter.ipynb 用 pydantic 的 `ControlItem` 模型定义 18 个控制项 + `@field_validator` 校验字段类型，from-scratch 版用 `dataclass Tool` + `eval(req_str, {"__builtins__":{}}, {})` 解析 JSON-RPC 请求--pydantic 的 schema 校验是声明式的（装饰器自动触发），from-scratch 版的校验是命令式的（dispatch 函数里 if/elif 分支），让"协议分发"不被框架抽象遮蔽。
2. **评分逻辑显形**：notes.md 关键回顾 2 的 NIST 四功能（Govern/Map/Measure/Manage）在 starter.ipynb 中用 `assess_control` 逐控制项打分再 `score_to_status` 映射，from-scratch 版用 `np.array([0.3,0.2,0.3,0.2]) @ np.array([c_G,c_Ma,c_Me,c_Mn])` 一行向量内积暴露"加权求和"的数学本质--权重向量 $w$ 的选择直接决定哪个功能对总分影响最大（Govern 和 Measure 各 0.3 > Map 和 Manage 各 0.2）。
3. **MCP 治理即代码的金属层**：notes.md 2026 前沿补充提到"MCP 让 GOVERN-2 从文档化升级为代码化"但停留在概念层，from-scratch 版的 `MCPServer.handle_jsonrpc` 是这个概念的金属实现：Agent 通过 JSON-RPC `tools/call` 调用 `nist_scan` 工具，治理检查从"人工填表"变为"Agent 可调用的工具"--这就是"治理即代码"的最简骨架。
4. **JSON 解析的安全边界**：starter.ipynb 用 pydantic 的 `model_validate_json` 安全解析 JSON，from-scratch 版用 `eval(s, {"__builtins__":{}}, {})` 限制内置函数--这暴露了"为什么不直接 `import json`"的白名单约束，也让研究者意识到 `eval` 的沙箱化（空 `__builtins__`）是受限环境下的 JSON 解析替代方案。

## deep_dive_links

- [P13/06 MCP Fundamentals - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/06-mcp-fundamentals/README.md) - MCP 基础协议，本 from-scratch 单元的 JSON-RPC 分发模型的理论锚点
- [P13/07 Building an MCP Server - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/07-building-an-mcp-server/README.md) - 从零构建 MCP server，本单元 `MCPServer` 类的工程参考
- [P13/01 The Tool Interface - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/01-the-tool-interface/README.md) - 工具接口设计，本单元 `Tool` dataclass 的 schema 定义依据

## exercises

1. 在本单元 `starter.ipynb` TODO3（NIST 合规扫描器 `scan_nist_rmf`）运行后，用上面的 `nist_score` 在同一份 8 个 OECD AI 用例上手动计算加权评分，对比 pydantic 版的逐控制项打分与 from-scratch 版的向量内积，解释差异来源（提示：pydantic 版逐项 0/1 二值，from-scratch 版 $c_k \in [0,1]$ 连续）。
2. 为 `MCPServer` 添加 `eu_ai_act_classify` 工具：实现 Article 5 禁止 -> Annex III 高风险 -> Article 50 有限 -> 最小风险的瀑布式判定，注册为第二个工具，用 `tools/list` 验证两个工具同时可见。对应 notes.md 关键回顾 3 的 EU AI Act 四级分级。
3. 构造"权重敏感性实验"：将 $w = [0.3, 0.2, 0.3, 0.2]$ 改为 $[0.4, 0.1, 0.4, 0.1]$（更偏重 Govern 和 Measure），观察同一组用例的评分排名变化。这与 notes.md 2026 前沿补充的"天道推演预判 AI 风险路径"中"高杠杆点"概念相关--权重选择本身就是治理优先级的量化表达。
4. TODO: 在 `practice.md` 的 D2 drill（双框架合规判定）中，为 from-scratch 版的 `nist_score` 添加"控制项缺失检测"：当某功能 $c_k = 0$（完全缺失）时返回 `"NON_COMPLIANT"` 而非依赖总分阈值。这是 starter.ipynb TODO3 的 from-scratch 补充。
