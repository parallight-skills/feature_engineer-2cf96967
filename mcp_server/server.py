"""feature_engineer skill 的 MCP server —— 只暴露一件 tool: engineer_features。
别的 agent 经 MCP 调它,拿到变换后的特征(不是预测)。
这是「单件 skill 作为独立商品」的落地:能单独被检索到、单独被买、单独被调。"""
import os
from mcp.server.fastmcp import FastMCP
from skill import feature_engineer

mcp = FastMCP("feature-engineer", host="0.0.0.0", port=int(os.environ.get("SKILL_PORT", "8000")))


@mcp.tool()
def engineer_features(X: list[list[float]]) -> list[list[float]]:
    """把 6 维原始特征变换成 27 维(原始+平方+两两交互)。输出是变换后的特征矩阵,不是预测。"""
    return feature_engineer.engineer(X)


if __name__ == "__main__":
    import sys
    remote = "--remote" in sys.argv or os.environ.get("MCP_TRANSPORT") == "sse"
    mcp.run(transport="sse" if remote else "stdio")
