from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
# QaxWidget 파이썬 파일중 컨테이너부분을 직접적으로 접근할수 있는 API로 서비스.서비스임플.맵퍼.DB (구현부안에 상속된건 아님) 추정됨
class Kiwoom(QAxWidget):

    """
    https://wikidocs.net/5755
    키움증권에서로 부터 설치한것은 OCX 방식에 컨포넌트 객체로 설치가 되었다.
    응용프로그램에서 키움Open API를 실행 할 수 있게 한거다.
    덕분에 제어가 된다.
    제어 할수 있는 함수는 PytQ5
    시그널 = 요청
    """

    def __init__(self):

        super().__init__() # 분모에있는 초기값들을 사용하기위해 분모에 있는 init을 사용한다.

        print("키움 API 연동")

        ############event_loop
        self.login_exec = None
        ######################

        self.get_Ocx_Install()

        self.event_List()

        self.signal_login_CommConnect()

    def get_Ocx_Install(self):

        """
        키움 API를 설치함으로써 응용프로그램들이 우리 window 레지스트리에 저장된다.
        레지스트리 편집기에 찾을수 있다.
        KHOPENAPI.KHOpenAPICtrl.1 폴더명으로 저장되며 DKHOPENAPI 기본값으로 설정되어있다.
        """

        self.setControl("KHOPENAPI.KHOpenAPICtrl.1") # 응용프로그램을 제어하기 위한 그 설치된 경로를 지정해주어야됨

    def event_List(self):

        self.OnEventConnect.connect(self.login_Function)

    # 로그인 성공시 이벤트
    def login_Function(self, nErrCode):
        print(nErrCode)

    # 키움 로그인 기능창 출력 or 자동설정 (로그인 시도)
    def signal_login_CommConnect(self):

        """
         로그인 성공시에 대한 이벤트 지정을 안해주면 로그인 성공시에 이벤트값이 없기에
         이벤트 핸들러 오류 발생할수 있음
        """

        # 네트워크적이거나 다른 서버 응용프로그램에다가 데이터를 전송할수 있음음
        self.dynamicCall("CommConnect()")

        self.login_exec = QEventLoop() # QtCore 이벤트 루프 초기화

        self.login_exec.exec_() # 이벤트 루프 지정