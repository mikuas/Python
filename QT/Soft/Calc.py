from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtGui import Qt
import sys


class CaliWindow:
    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle('简易计算器')
        self.window.setFixedSize(850, 570)
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)

        self.text = QTextEdit(self.window)
        self.text.setFixedSize(830, 100)
        self.text.setReadOnly(True)
        self.text.setText('0')
        self.text.setStyleSheet("border: 1px solid black; font-size: 70px;")

        self.createButtons()

        layout = QVBoxLayout(self.window)
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
                button = QPushButton(text, self.window)
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
                                color: #00BFFF;
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
                                color: #00BFFF;
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
                    background-color: rgb(0,255,127);
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
        elif text == 'x' and not (current_text[-1] in '+-*/.%^' and text in '+-x/.%^'):
            self.text.setPlainText(current_text + '*')
        elif text == '^' and not (current_text[-1] in '+-*/.%^' and text in '+-x/.%^'):
            self.text.setPlainText(current_text + '**')
        elif not (current_text[-1] in '+-*/.%^' and text in '+-x/.%^'):
            self.text.setPlainText(current_text + text)

    def calculateResult(self):
        try:
            result = str(eval(self.text.toPlainText()))
            self.text.setPlainText(result.rstrip('0').rstrip('.') if '.' in result else result)
        except Exception:
            self.text.setPlainText(f'输入有误,表达式不正确')

    @staticmethod
    def ignoreCloseEvent(event, windows):
        event.ignore()
        windows.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaliWindow().window
    window.show()
    sys.exit(app.exec())
