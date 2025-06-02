from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(name = "tutorial2")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://hello")
def get_greeting() -> str:
    """Get a greeting message"""
    return f"Hello, World!"

# 서버 실행
if __name__ == "__main__":
    mcp.run()
