from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtGui import Qt
import sys


class CaliWindow:
    def __init__(self):
        self.calcWindow = QWidget()
        self.calcWindow.setWindowTitle('简易计算器')
        self.calcWindow.setFixedSize(850, 570)

        self.text = QTextEdit(self.calcWindow)
        self.text.setFixedSize(830, 100)
        self.text.setReadOnly(True)
        self.text.setText('0')
        self.text.setStyleSheet("border: 1px solid black; font-size: 70px;")

        self.createButtons()

        layout = QVBoxLayout(self.calcWindow)
        layout.addWidget(self.text)
        layout.addSpacing(30)
        for row in self.button_rows:
            layout.addLayout(row)
            layout.addStretch(1)

        self.applyButtonStyles()

    def createButtons(self):
        button_texts = [
            ['AC', '<---', '^', '+'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', 'x'],
            ['1', '2', '3', '/'],
            ['%', '0', '.', '=']
        ]

        self.button_dict = {}
        self.button_rows = []

        for row in button_texts:
            hLayout = QHBoxLayout()
            for text in row:
                button = QPushButton(text, self.calcWindow)
                button.setFixedSize(200, 85)
                button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                button.clicked.connect(lambda _, t=text: self.onButtonClick(t))
                self.button_dict[text] = button
                hLayout.addWidget(button, alignment=Qt.AlignCenter)
            self.button_rows.append(hLayout)

    def applyButtonStyles(self):
        operators = ['+', 'x', '/', '%', '^', 'AC', '<---', '.', '-', '=']
        numberArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for op, number in zip(operators, numberArr):
            if op:
                if op in '.-':
                    self.button_dict[op].setStyleSheet(
                        """
                            QPushButton {
                                background-color: pink;
                                font-size: 45px;
                            }
                            QPushButton:hover {
                                color: aqua;
                            }
                        """
                    )
                else:
                    self.button_dict[op].setStyleSheet(
                        """
                            QPushButton {
                            background-color: pink;
                            font-size: 32px;
                            }
                            QPushButton:hover {
                                color: aqua;
                            }
                        """
                    )
                self.button_dict[number].setStyleSheet(
                    """
                        QPushButton {
                            font-size: 32px;
                        }
                        QPushButton:hover {
                            background-color: lightblue;
                            font-size: 32px;
                        }
                    """
                )

        self.button_dict['='].setStyleSheet(
            """
                QPushButton {
                    background-color: aqua;
                    font-size: 40px;
                }
                QPushButton:hover {
                    background-color: #00FF7F;
                }
            """
        )

    def onButtonClick(self, text):
        if text == 'AC':
            self.text.setPlainText('0')
        elif text == '<---':
            self.backspace()
        elif text == '=':
            self.calculateResult()
        else:
            self.updateExpression(text)

    def backspace(self):
        current_text = self.text.toPlainText()
        if len(current_text) == 1:
            self.text.setPlainText('0')
        else:
            self.text.setPlainText(current_text[:-1])

    def updateExpression(self, text):
        current_text = self.text.toPlainText()
        if current_text == '0' and text not in '+-x/%^.':
            self.text.setPlainText(text)
        elif text == 'x':
            self.text.setPlainText(current_text + '*')
        elif text == '^':
            self.text.setPlainText(current_text + '**')
        elif not (current_text[-1] in '+-*/.%^' and text in '+-*/.%^'):
            self.text.setPlainText(current_text + text)

    def calculateResult(self):
        try:
            result = str(eval(self.text.toPlainText()))
            self.text.setPlainText(result.rstrip('0').rstrip('.') if '.' in result else result)
        except Exception as e:
            self.text.setPlainText(f'输入有误:{str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaliWindow().calcWindow
    window.show()
    sys.exit(app.exec())
