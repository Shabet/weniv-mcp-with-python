from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage
import os

mcp = FastMCP(name = "tutorial4")

@mcp.tool()
def create_thumbnail() -> Image:
    """Create a thunbnail from an image"""
    try:
        import io

        img_path = os.path.join("D:\work\weniv-mcp-with-python", "image.png")
        img = PILImage.open(img_path)
        img.thumbnail((100, 100)) #썸네일 크기 지정

        # 바이트 스트림으로 이미지를 저장
        buffer = io.BytesIO()
        img.save(buffer, format = "PNG")

        # 바이트 스트림의 내용을 가져와 변환
        return Image(data=buffer.getvalue(), format="PNG")
    except Exception as e:
        return f"Error creating thumbnail: {e}"

# 서버 실행
if __name__ == "__main__":
    mcp.run()
