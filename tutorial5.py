from mcp.server.fastmcp import FastMCP, Context

# Create an MCP server
mcp = FastMCP(name = "tutorial5")

@mcp.tool()
async def greeting(name: str, ctx: Context) -> str:
    """Get a greeting using the greeting resouce"""
    try:
        result = await ctx.read_resource(f"greeting://{name}")
        context = result[0] if isinstance(result, tuple) else result
        return f"Tool response {context}"
    except Exception as e:
        return f"Error retrieving greeting: {str(e)}"

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!! Welcome to FastMCP!"

# 서버 실행
if __name__ == "__main__":
    mcp.run()                                       
