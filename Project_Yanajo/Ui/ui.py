from kiwoomApi.kiwoom import Kiwoom
from PyQt5.QtWidgets import *

import sys

"""
Terminal PyQt5 Install
- activate py37_32
- pip install PyQt5
"""
class Ui_class():
    def __init__(self):
        print("UI연동")

        #UI를 실행하기 위해서 필요한 함수나 변수를 초기화 시키기위한 용도도
        #sys 파이썬 기본적인 라이브러리 argv 리스트 형태로 인자들을 불러옴
        self.app = QApplication(sys.argv)

        Kiwoom()

        #PyQt5에서는 이벤트 루프 실행하고 나면은 프로그래머가 종료시키지 않는이상 종료되지 않는다.
        self.app.exec_() # exec_() 이벤트 루프 사용