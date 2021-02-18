import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QFont

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): # 클래스의 인스턴스를 나타내는 변수
        self.setWindowTitle('My First Leesuhuck TOP Coppy Application')
        self.move(300, 300)
        self.setGeometry(500, 500, 500, 500)

        btn = QPushButton('끼요욧', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint()) # 기본 우리가 알고있는 버튼 사이즈로 출력된다.
        #btn.pressed.connect(self.Click) # 눌럿을때
        btn.released.connect(self.Click) # 눌럿따 떘을때

        btn2 = QPushButton('닫아', self)
        btn2.move(150,50)
        btn2.resize(btn2.sizeHint())
        btn2.pressed.connect(self.close)

        self.setLabel = QLabel(self)
        self.setLabel.move(90, 30)

        EditView = QLineEdit(self)
        EditView.move(100, 90)
        EditView.textChanged[str].connect(self.onChanged)

        self.show()

    def onChanged(self, text):
        self.setLabel.setText(text)
        self.setLabel.adjustSize() # 반응형으로 크기에 맞춰 사이즈가 변환

    def Click(self):
        self.setLabel.setText('입력되었어요')
        self.setLabel.adjustSize()


    def closeEvent(self, event): # 이벤트 핸들러 (이 이벤트 핸들러가 windowAPI에서도 자주사용해 보통 이걸로 제어해)
        msg = QMessageBox.question(self, 'message', '너 정말 끌거야?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            event.accept()
            print('windowClose')
        else:
            event.ignore()

# 내일은 알림창을 띄우고 그 알림창에 난 지금 끌꺼다 안끌꺼다 만들고 끌꺼다 하면은 앱 종료하기

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
