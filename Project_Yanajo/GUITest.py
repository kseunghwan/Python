import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    number1 = 0
    sign = ''
    downNumber = 0
    Jcount = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First yunho Application')
        self.move(700, 300)
        self.resize(500, 500)

        # self.setFixedSize(500, 500)

        btn = QPushButton('인사하기', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())  # 사이즈 자동지정
        btn.pressed.connect(self.Click)  # 눌렀을 때
        # btn.released.connect(self.Click) #눌렀다 땠을 때

        btn2 = QPushButton('닫기', self)
        btn2.move(150, 50)
        btn2.resize(btn.sizeHint())
        btn2.pressed.connect(self.close)

        # 버튼 생성
        onebtn = QPushButton('1', self)
        onebtn.resize(btn.sizeHint())
        onebtn.pressed.connect(self.onef)


        twobtn = QPushButton('2', self)
        twobtn.resize(btn.sizeHint())
        twobtn.pressed.connect(self.twof)

        thrbtn = QPushButton('3', self)
        thrbtn.resize(btn.sizeHint())
        thrbtn.pressed.connect(self.thrf)

        forbtn = QPushButton('4', self)
        forbtn.resize(btn.sizeHint())
        forbtn.pressed.connect(self.forf)

        fivbtn = QPushButton('5', self)
        fivbtn.resize(btn.sizeHint())
        fivbtn.pressed.connect(self.fivf)

        sixbtn = QPushButton('6', self)
        sixbtn.resize(btn.sizeHint())
        sixbtn.pressed.connect(self.sixf)

        sevbtn = QPushButton('7', self)
        sevbtn.resize(btn.sizeHint())
        sevbtn.pressed.connect(self.sevf)

        eigbtn = QPushButton('8', self)
        eigbtn.resize(btn.sizeHint())
        eigbtn.pressed.connect(self.eigf)

        ninbtn = QPushButton('9', self)
        ninbtn.resize(btn.sizeHint())
        ninbtn.pressed.connect(self.ninf)

        zerobtn = QPushButton('0', self)
        zerobtn.resize(btn.sizeHint())
        zerobtn.pressed.connect(self.zerof)

        plsbtn = QPushButton('+', self)
        # pls.move(130, 150)
        plsbtn.resize(btn.sizeHint())
        plsbtn.pressed.connect(self.plsf)

        minubtn = QPushButton('-', self)
        # pls.move(130, 150)
        minubtn.resize(btn.sizeHint())
        minubtn.pressed.connect(self.minuf)

        multibtn = QPushButton('*', self)
        # pls.move(130, 150)
        multibtn.resize(btn.sizeHint())
        multibtn.pressed.connect(self.multif)

        divibtn = QPushButton('/', self)
        # pls.move(130, 150)
        divibtn.resize(btn.sizeHint())
        divibtn.pressed.connect(self.divf)

        equbtn = QPushButton('=', self)
        # equ.move(290, 150)
        equbtn.resize(btn.sizeHint())
        equbtn.pressed.connect(self.equf)

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(onebtn)
        hbox.addWidget(twobtn)
        hbox.addWidget(thrbtn)
        hbox.addWidget(plsbtn)
        hbox.addStretch(1)

        hbox2.addStretch(1)
        hbox2.addWidget(forbtn)
        hbox2.addWidget(fivbtn)
        hbox2.addWidget(sixbtn)
        hbox2.addWidget(minubtn)
        hbox2.addStretch(1)

        hbox3.addStretch(1)
        hbox3.addWidget(sevbtn)
        hbox3.addWidget(eigbtn)
        hbox3.addWidget(ninbtn)
        hbox3.addWidget(multibtn)
        hbox3.addStretch(1)

        hbox4.addStretch(1)
        hbox4.addWidget(zerobtn)
        hbox4.addWidget(divibtn)
        hbox4.addWidget(equbtn)
        hbox4.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(4)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)

        self.setLabel = QLabel(self)
        self.setLabel.move(50, 100)

        self.setLayout(vbox)
        self.show()

    def Click(self):
        self.setLabel.setText("안녕하세요")
        self.setLabel.adjustSize()

    def closeEvent(self, event):  # 이벤트 핸들러
        msg = QMessageBox.question(self, 'Message', '정말 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if msg == QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()

    def onef(self):
        MyApp.number1 = 1
        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def twof(self):

        MyApp.number1 = 2

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def thrf(self):

        MyApp.number1 = 3

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def forf(self):

        MyApp.number1 = 4

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def fivf(self):

        MyApp.number1 = 5

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def sixf(self):

        MyApp.number1 = 6

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def sevf(self):

        MyApp.number1 = 7

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def eigf(self):

        MyApp.number1 = 8

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def ninf(self):

        MyApp.number1 = 9

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def zerof(self):

        MyApp.number1 = 0

        self.setLabel.setText(str(MyApp.number1))
        self.setLabel.adjustSize()

        if (MyApp.Jcount == 0):
            print(MyApp.sign)

            self.tY()
            self.equf2()

            print(MyApp.downNumber)

        elif (MyApp.Jcount > 0):

            self.equf2()

        MyApp.Jcount = MyApp.Jcount + 1

    def plsf(self):

        MyApp.sign = '+'

        self.setLabel.setText(str(MyApp.sign))
        self.setLabel.adjustSize()

        MyApp.Jcount = 1

        if (MyApp.Jcount == 1):
            print(MyApp.downNumber)

            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

        # value = self.sixf.first + self.eitf.second

    def minuf(self):

        MyApp.sign = '-'

        self.setLabel.setText(str(MyApp.sign))
        self.setLabel.adjustSize()

        MyApp.Jcount = 1

        if (MyApp.Jcount == 1):
            print(MyApp.downNumber)

            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

        # value = self.sixf.first + self.eitf.second

    def multif(self):

        MyApp.sign = '*'

        self.setLabel.setText(str(MyApp.sign))
        self.setLabel.adjustSize()

        MyApp.Jcount = 1

        if (MyApp.Jcount == 1):
            print(MyApp.downNumber)

            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

        # value = self.sixf.first + self.eitf.second

    def divf(self):

        MyApp.sign = '/'
        self.setLabel.setText(str(MyApp.sign))
        self.setLabel.adjustSize()

        MyApp.Jcount = 1

        if (MyApp.Jcount == 1):
            print(MyApp.downNumber)
            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

        # value = self.sixf.first + self.eitf.second

    def tY(self):
        MyApp.downNumber = MyApp.number1


    def equf(self):
        if MyApp.sign == '+':
            MyApp.Jvalue = MyApp.downNumber + MyApp.number1
            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

        if MyApp.sign == '-':
            MyApp.Jvalue = MyApp.downNumber - MyApp.number1
            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

        if MyApp.sign == '*':
            MyApp.Jvalue = MyApp.downNumber * MyApp.number1
            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()


        if MyApp.sign == '/':
            MyApp.Jvalue = MyApp.downNumber / MyApp.number1
            self.setLabel.setText(str(MyApp.downNumber))
            self.setLabel.adjustSize()

    def equf2(self):
        if MyApp.sign == '+':
            MyApp.downNumber = MyApp.downNumber + MyApp.number1

        if MyApp.sign == '-':
            MyApp.downNumber = MyApp.downNumber - MyApp.number1

        if MyApp.sign == '*':
            MyApp.downNumber = MyApp.downNumber * MyApp.number1

        if MyApp.sign == '/':
            MyApp.downNumber = MyApp.downNumber / MyApp.number1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
