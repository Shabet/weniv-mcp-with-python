from mcp.server.fastmcp import FastMCP

# MCP 서버 생성
mcp = FastMCP(name="practice_server")

@mcp.tool()
def create_folder(folder_name: str) -> str:
    """
    c:/test/ 아래에 폴더를 생성합니다.

    Parameters
    ----------
    folder_name: str
      생성할 폴더 이름

    Returns
    -------
    str
      생성 결과 메시지
    """
    import os

    folder_path = os.path.join("c:/test", folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return f"{folder_name} 폴더가 생성되었습니다."
    else:
        return f"{folder_name} 폴더가 이미 존재합니다."

@mcp.tool()
def delete_folder(folder_name: str) -> str:
    """
    c:/test/ 아래에 폴더를 삭제합니다.

    Parameters
    ----------
    folder_name: str
      삭제할 폴더 이름
    
    Returns
    -------
    str
      삭제 결과 메시지
    """
    import os

    folder_path = os.path.join("c:/test", folder_name)
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        return f"{folder_name} 폴더가 삭제되었습니다."
    else:
        return f"{folder_name} 폴더가 존재하지 않습니다."

@mcp.tool()
def list_folder() -> list:
    """
    c:/test/ 아래 폴더 목록을 반환합니다.

    Returns
    -------
    list
      폴더 목록
    """
    import os

    folder_path = "c:/test"
    folders = [
        f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))
    ]
    return folders

@mcp.tool()
def write_file(file_name: str, content: str) -> str:
    """
    c:/test/ 아래에 파일을 생성하고 내용을 작성합니다.

    Parameters
    ----------
    file_name: str
      생성할 파일 이름(확장자 포함)

    content: str
      파일에 작성할 내용

    Returns
    -------
    str
      파일 작성 결과 메시지
    """
    import os

    file_path = os.path.join("c:/test", file_name)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"'{file_name}'에 내용이 성공적으로 작성되었습니다."
    except Exception as e:
        return f"파일 작성중 오류가 발생하였습니다.: {str(e)}"

@mcp.tool()
def read_file(file_name: str) -> str:
    """
    c:/test/ 아래에 있는 파일의 내용을 읽어옵니다.

    Parameters
    ----------
    file_name: str
      읽어올 파일 이름(확장자 포함)

    Returns
    -------
    str
      파일 내용 또는 오류 메시지
    """
    import os

    file_path = os.path.join("c:/test", file_name)
    if not os.path.exists(file_path):
        return f"'{file_name}' 파일이 존재하지 않습니다."
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"파일 읽기중 오류가 발생하였습니다.: {str(e)}"

@mcp.tool()
def append_to_file(file_name: str, content: str) -> str:
    """
    c:/test/ 아래에 있는 파일에 내용을 추가합니다.

    Parameters
    ----------
    file_name: str
      내용을 추가할 파일 이름(확장자 포함)

    content: str
      파일에 추가할 내용

    Returns
    -------
    str
      추가 결과 메시지
    """
    import os

    file_path = os.path.join("c:/test", file_name)
    if not os.path.exists(file_path):
        return f"'{file_name}' 파일이 존재하지 않습니다."
    
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)
        return f"'{file_name}'에 내용이 성공적으로 추가되었습니다."
    except Exception as e:
        return f"파일 추가중 오류가 발생하였습니다.: {str(e)}"
    
@mcp.tool()
def list_files() -> list:
    """
    c:/test/ 아래 파일 목록을 반환합니다.

    Returns
    -------
    list
      파일 목록
    """
    import os
    folder_path = "c:/test"
    files = [
        f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))
    ]
    return files

@mcp.tool()
def read_excel(file_name: str) -> list:
    """
    c:/test/ 아래에 있는 엑셀 파일을 읽어 데이터를 리스트로 반환합니다.

    Parameters
    ----------
    file_name: str
      읽어올 엑셀 파일 이름(확장자 포함)
      예: 'data.xlsx'
    
    Returns
    ------- 
    list
      엑셀 데이터가 포함된 딕셔너리 리스트
      예: [{'name': '김철수', 'age': 30}, {...}]
    """
    import pandas as pd
    import os

    # pandas와 openpyxl 라이브러리필요
    # pip install pandas openpyxl

    file_path = os.path.join("c:/test", file_name)

    try:
        # 엑셀 파일이 존재하는지 확인
        if not os.path.exists(file_path):
            return f"'{file_name}' 파일이 존재하지 않습니다."
        
        # 엑셀 파일 읽기
        df = pd.read_excel(file_path)

        # 데이터프레임을 딕셔너리 리스트로 변환
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        return f"엑셀 파일 '{file_name}' 읽기중 오류가 발생하였습니다.: {str(e)}"
    
@mcp.tool()
def write_excel(contents: list, file_name: str = "test.xlsx") -> str:
    """
    리스트를 엑셀 파일로 저장합니다.

    Parameters
    ----------
    contents: list
      딕셔너리 리스트 형태의 데이터
      예: [{'name': '김철수', 'age': 30}, {...}]
    
    file_name: str, optional
      저장할 파일 이름(확장자 포함), 기본값은 'data.xlsx'
    
    Returns
    -------
    str
      파일 생성 완료 메시지
    """
    import pandas as pd
    import os

    file_path = os.path.join("c:/test", file_name)

    try:
        # 딕셔너리 리스트를 데이터프레임으로 변환
        df = pd.DataFrame(contents)

        # 엑셀 파일 저장
        df.to_excel(file_path, index=False)
        return f"'{file_name}' 파일이 성공적으로 생성되었습니다."
    except Exception as e:
        return f"엑셀 파일 생성중 오류가 발생하였습니다.: {str(e)}"
    
@mcp.tool()
def create_excel_with_formatting(contents: list, file_name: str = "formatted_data.xlsx") -> str:
    """
    리스트를 서식이 지정될 엑셀 파일로 저장합니다.

    Parameters
    ----------
    contents: list
      딕셔너리 리스트 형태의 데이터
      예: [{'name': '김철수', 'age': 30}, {...}]
    
    file_name: str, optional
      저장할 파일 이름(확장자 포함), 기본값은 'formatted_data.xlsx'
    
    Returns
    -------
    str
      파일 생성 완료 메시지
    """
    import pandas as pd
    import os
    import xlsxwriter

    file_path = os.path.join("c:/test", file_name)

    try:
        # 엑셀 워크북 생성
        workbook = xlsxwriter.Workbook(file_path)

        # 워크시트 추가
        worksheet = workbook.add_worksheet("Data")

        # 헤더 스타일 정의
        header_format = workbook.add_format({
            "bold": True,
            "font_color": "white",
            "bg_color": "#4F81BD",
            "align": "center",
            "valign": "vcenter",
            "border": 1
        })

        # 데이터 스타일 정의
        data_format = workbook.add_format({
            'border': 1,
        })

        # 헤더가 있는지 확인
        if contents and len(contents) > 0:
            # 헤더 작성
            headers = list(contents[0].keys())
            for col_idx, header in enumerate(headers):
                worksheet.write(0, col_idx, header, header_format)

            # 데이터 작성
            for row_idx, row_data in enumerate(contents):
                for col_idx, key in enumerate(headers):
                    worksheet.write(row_idx + 1, col_idx, row_data.get(key, ""), data_format)

            # 열 너비 자동 지정
            for col_idx, header in enumerate(headers):
                worksheet.set_column(col_idx, col_idx, 15)
    
        workbook.close()
        return f"서식이 지정된 엑셀 파일 '{file_name}' 이 성공적으로 생성되었습니다."
    except Exception as e:
        return f"서식이 지정된 엑셀 파일 생성중 오류가 발생하였습니다.: {str(e)}"

@mcp.tool()
def append_to_excel(file_name: str, new_data: list) -> str:
    """
    기존 엑셀 파일에 새로운 데이터를 추가합니다.

    Parameters
    ----------
    file_name: str
      데이터를 추가할 엑셀 파일 이름(확장자 포함)
    
    new_data: list
      추가할 데이터가 포함된 딕셔너리 리스트
      예: [{'name': '이영희', 'age': 25}, {...}]

    Returns
    -------
    str
      데이터 추가 결과 메시지
    """
    import pandas as pd
    import os

    file_path = os.path.join("c:/test", file_name)

    try:
        # 엑셀 파일이 존재하는지 확인
        if not os.path.exists(file_path):
            return f"'{file_name}' 파일이 존재하지 않습니다."
        
        # 기존 엑셀 파일 읽기
        existing_df = pd.read_excel(file_path)

        # 새 데이터를 데이터프레임으로 변환
        new_df = pd.DataFrame(new_data)

        # 두 데이터프레임을 병합
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        # 병합된 데이터프레임을 다시 엑셀 파일로 저장
        combined_df.to_excel(file_path, index=False)

        return f"'{file_name}' 파일에 데이터가 성공적으로 추가되었습니다."
    except Exception as e:
        return f"엑셀 파일 추가중 오류가 발생하였습니다.: {str(e)}"

@mcp.tool()
def crawl_url_return_book_name(url: str) -> list:
    """
    URL을 입력 받아 해당 URL의 책 제목을 크롤링하여 반환합니다. 각 데이터는 콤마로 연결됩니다.
    따라서 사용자에서 보여줄 때에는 콤마를 개행하여 보여주세요.

    Parameters
    ----------
    url: str
      크롤링할 웹 페이지 URL

    Returns
    -------
    str
      콤마로 구분된 책 제목 목록
    """
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = []

    for book in soup.select(".book_name"):
        result.append(book.text.strip())

    return ",".join(result)

# 서버 실행
if __name__ == "__main__":
    mcp.run()