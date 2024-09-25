from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, \
    QSizePolicy
from PySide6.QtGui import Qt
import sys

class CaliWindow:
    def __init__(self):
        self.calcWindow = QWidget()
        self.calcWindow.setWindowTitle('Calc')
        self.calcWindow.setFixedSize(850, 570)
        self.text = QTextEdit(self.calcWindow)
        self.text.setFixedSize(830, 100)
        self.text.setReadOnly(True) # 设置只读
        self.text.setText('0')
        self.text.setStyleSheet(
            """
            border: 1px solid black;
            font-size: 70px;
            """
        )
        self.buttonStyle = [
            """
                font-size: 24px;
            """
        ]

        # Line 1
        self.buttonAC = QPushButton('AC', self.calcWindow)
        self.buttonAC.setStyleSheet(
            """
                font-size: 24px;
                background-color: pink;
            """
        )
        self.buttonDelete = QPushButton('<---', self.calcWindow)
        self.buttonDelete.setStyleSheet(
            """
                font-size: 24px;
                background-color: pink;
            """
        )
        self.buttonCiFang = QPushButton('^', self.calcWindow)
        self.buttonCiFang.setStyleSheet(
            """
                font-size: 24px;
                background-color: pink;
            """
        )
        self.buttonJia = QPushButton('+', self.calcWindow)
        self.buttonJia.setStyleSheet(
            """
                font-size: 24px;
                background-color: pink;
            """
        )

        self.buttonAC.setFixedSize(200, 85)
        self.buttonDelete.setFixedSize(200, 85)
        self.buttonCiFang.setFixedSize(200, 85)
        self.buttonJia.setFixedSize(200, 85)

        self.buttonAC.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonDelete.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonCiFang.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonJia.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Line 2
        self.button7 = QPushButton('7', self.calcWindow)
        self.button7.setStyleSheet(self.buttonStyle[0])
        self.button8 = QPushButton('8', self.calcWindow)
        self.button8.setStyleSheet(self.buttonStyle[0])
        self.button9 = QPushButton('9', self.calcWindow)
        self.button9.setStyleSheet(self.buttonStyle[0])
        self.buttonJian = QPushButton('-', self.calcWindow)
        self.buttonJian.setStyleSheet(
            """
                font-size: 24px;
                background-color: pink;
            """
        )

        self.button7.setFixedSize(200, 85)
        self.button8.setFixedSize(200, 85)
        self.button9.setFixedSize(200, 85)
        self.buttonJian.setFixedSize(200, 85)

        self.button7.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button8.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button9.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonJian.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Line 3
        self.button4 = QPushButton('4', self.calcWindow)
        self.button4.setStyleSheet(self.buttonStyle[0])
        self.button5 = QPushButton('5', self.calcWindow)
        self.button5.setStyleSheet(self.buttonStyle[0])
        self.button6 = QPushButton('6', self.calcWindow)
        self.button6.setStyleSheet(self.buttonStyle[0])
        self.buttonX = QPushButton('x', self.calcWindow)
        self.buttonX.setStyleSheet(
            """
                font-size: 24px;
                background-color: pink;
            """
        )

        self.button4.setFixedSize(200, 85)
        self.button5.setFixedSize(200, 85)
        self.button6.setFixedSize(200, 85)
        self.buttonX.setFixedSize(200, 85)

        self.button4.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button5.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button6.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonX.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Line 4
        self.button1 = QPushButton('1', self.calcWindow)
        self.button1.setStyleSheet(self.buttonStyle[0])
        self.button2 = QPushButton('2', self.calcWindow)
        self.button2.setStyleSheet(self.buttonStyle[0])
        self.button3 = QPushButton('3', self.calcWindow)
        self.button3.setStyleSheet(self.buttonStyle[0])
        self.buttonCu = QPushButton('/', self.calcWindow)
        self.buttonCu.setStyleSheet(
            """
                font-size: 32px;
                background-color: pink;
            """
        )

        self.button1.setFixedSize(200, 85)
        self.button2.setFixedSize(200, 85)
        self.button3.setFixedSize(200, 85)
        self.buttonCu.setFixedSize(200, 85)

        self.button1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonCu.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Line 5
        self.buttonQuYu = QPushButton('%', self.calcWindow)
        self.buttonQuYu.setStyleSheet(
            """
                font-size: 32px;
                background-color: pink;
            """
        )
        self.button0 = QPushButton('0', self.calcWindow)
        self.button0.setStyleSheet(self.buttonStyle[0])
        self.buttonDian = QPushButton('.', self.calcWindow)
        self.buttonDian.setStyleSheet(
            """
                font-size: 45px;
                background-color: pink;
            """
        )
        self.buttonDengYu = QPushButton('=', self.calcWindow)
        self.buttonDengYu.setStyleSheet(
            """
                font-size: 32px;
                background-color: #00FFFF;
            """
        )

        self.buttonQuYu.setFixedSize(200, 85)
        self.button0.setFixedSize(200, 85)
        self.buttonDian.setFixedSize(200, 85)
        self.buttonDengYu.setFixedSize(200, 85)

        self.buttonQuYu.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button0.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonDian.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonDengYu.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #------------------------------------------

        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(self.buttonAC, alignment=Qt.AlignCenter)
        hLayout1.addWidget(self.buttonDelete, alignment=Qt.AlignCenter)
        hLayout1.addWidget(self.buttonCiFang, alignment=Qt.AlignCenter)
        hLayout1.addWidget(self.buttonJia, alignment=Qt.AlignCenter)

        hLayout2 = QHBoxLayout()
        hLayout2.addWidget(self.button7, alignment=Qt.AlignCenter)
        hLayout2.addWidget(self.button8, alignment=Qt.AlignCenter)
        hLayout2.addWidget(self.button9, alignment=Qt.AlignCenter)
        hLayout2.addWidget(self.buttonJian, alignment=Qt.AlignCenter)

        hLayout3 = QHBoxLayout()
        hLayout3.addWidget(self.button4, alignment=Qt.AlignCenter)
        hLayout3.addWidget(self.button5, alignment=Qt.AlignCenter)
        hLayout3.addWidget(self.button6, alignment=Qt.AlignCenter)
        hLayout3.addWidget(self.buttonX, alignment=Qt.AlignCenter)

        hLayout4 = QHBoxLayout()
        hLayout4.addWidget(self.button1, alignment=Qt.AlignCenter)
        hLayout4.addWidget(self.button2, alignment=Qt.AlignCenter)
        hLayout4.addWidget(self.button3, alignment=Qt.AlignCenter)
        hLayout4.addWidget(self.buttonCu, alignment=Qt.AlignCenter)

        hLayout5 = QHBoxLayout()
        hLayout5.addWidget(self.buttonQuYu, alignment=Qt.AlignCenter)
        hLayout5.addWidget(self.button0, alignment=Qt.AlignCenter)
        hLayout5.addWidget(self.buttonDian, alignment=Qt.AlignCenter)
        hLayout5.addWidget(self.buttonDengYu, alignment=Qt.AlignCenter)

        layout = QVBoxLayout(self.calcWindow)
        layout.addWidget(self.text)
        layout.addStretch(1)
        layout.addStretch(1)
        layout.addLayout(hLayout1)
        layout.addStretch(1)
        layout.addLayout(hLayout2)
        layout.addStretch(1)
        layout.addLayout(hLayout3)
        layout.addStretch(1)
        layout.addLayout(hLayout4)
        layout.addStretch(1)
        layout.addLayout(hLayout5)
        layout.addStretch(1)

        # Button Click Events
        self.button0.clicked.connect(lambda: self.click(self.button0))
        self.button1.clicked.connect(lambda: self.click(self.button1))
        self.button2.clicked.connect(lambda: self.click(self.button2))
        self.button3.clicked.connect(lambda: self.click(self.button3))
        self.button4.clicked.connect(lambda: self.click(self.button4))
        self.button5.clicked.connect(lambda: self.click(self.button5))
        self.button6.clicked.connect(lambda: self.click(self.button6))
        self.button7.clicked.connect(lambda: self.click(self.button7))
        self.button8.clicked.connect(lambda: self.click(self.button8))
        self.button9.clicked.connect(lambda: self.click(self.button9))
        self.buttonJia.clicked.connect(lambda: self.click(self.buttonJia))
        self.buttonJian.clicked.connect(lambda: self.click(self.buttonJian))
        self.buttonX.clicked.connect(lambda: self.click(self.buttonX))
        self.buttonCu.clicked.connect(lambda: self.click(self.buttonCu))
        self.buttonDian.clicked.connect(lambda: self.click(self.buttonDian))
        self.buttonCiFang.clicked.connect(lambda: self.click(self.buttonCiFang))
        self.buttonQuYu.clicked.connect(lambda: self.click(self.buttonQuYu))

        self.buttonAC.clicked.connect(lambda: self.text.setPlainText('0'))
        self.buttonDelete.clicked.connect(self.backspace)

        self.buttonDengYu.clicked.connect(self.getSum)
        #-------------------------

        # Get Text Content
        content = self.text.toPlainText()
        print(content)

    def backspace(self):
        if len(self.text.toPlainText()) == 1:
            self.text.setPlainText('0')
        else:
            self.text.setPlainText(self.text.toPlainText()[:-1])

    def click(self, obj):
        element = [self.buttonJia, self.buttonJian, self.buttonX, self.buttonCu, self.buttonCiFang, self.buttonDian, self.buttonQuYu]
        if self.text.toPlainText() == '0' and obj == self.button0:
            self.text.setPlainText('0')
        elif self.text.toPlainText() == '0' and obj not in element:
            self.text.setPlainText(obj.text())
        elif self.text.toPlainText()[-1] in ['+', '-', 'x', '/', '.', '^'] and obj in element:
            return
        else:
            self.text.setPlainText(self.text.toPlainText() + obj.text())

    def getSum(self):
        result = self.text.toPlainText()
        index = 0
        for string in result:
            if string == '+' or string == '-' or string == 'x' or string == '/'or string == '^' or string == '%':
                print(index)
                if result[index] == '+':
                    result = float(result[:index]) + float(result[index + 1:])
                    break
                elif result[index] == '-':
                    result = float(result[:index]) - float(result[index + 1:])
                    break
                elif result[index] == 'x':
                    result = float(result[:index]) * float(result[index + 1:])
                    break
                elif result[index] == '/':
                    result = float(result[:index]) / float(result[index + 1:])
                    break
                elif result[index] == '^':
                    result = float(result[:index]) ** float(result[index + 1:])
                elif result[index] == '%':
                    result = float(result[:index]) % float(result[index + 1:])
            else:
                index += 1
        re = str(result).split('.')
        if int(re[-1]) > 0:
            self.text.setPlainText(str(result))
        else:
            self.text.setPlainText(re[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaliWindow().calcWindow
    window.show()
    sys.exit(app.exec())