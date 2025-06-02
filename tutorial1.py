from mcp.server.fastmcp import FastMCP

# MCP 서버 생성
mcp = FastMCP(name = "tutorial1")

@mcp.tool()
def echo(message: str) -> str:
    '''
    입려받은 메시지를 그대로 반환하는 도구입니다.
    '''
    return message + " 라는 메시지가 입력되었습니다. 안찍어 볼수 없죠. Hello World!"

# 서버 실행
if __name__ == "__main__":
    mcp.run()
