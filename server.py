from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(name = "server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

# 서버 실행
if __name__ == "__main__":
    mcp.run()