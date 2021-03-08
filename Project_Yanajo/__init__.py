from Ui.ui import Ui_class

"""
수동 로그인 성공후 윈도우 하단 메뉴바 아이콘을 보시면 키움 API 아이콘이 있습니다.
거기서 계좌 비밀번호 입력을 설정해 주신후 등록 해주면 자동로그인 설정을 하실수 있습니다.
"""

class Main():
    def __init__(self):
        print("메인 접촉")

        Ui_class()

if __name__=="__main__":
    Main()