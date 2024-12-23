import sys
from symtable import Function

from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import Qt
from qfluentwidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        centerWindget = QWidget(self)
        mainLayout = QVBoxLayout(centerWindget)

        '''复选框'''
        self.check = CheckBox(self)
        self.check.setText("Check")
        self.check.setChecked(True)
        # 连接信号插槽
        self.check.stateChanged.connect(lambda: (print("Check"), print(self.check.checkState().value)))


        mainLayout.addWidget(self.check)

        self.setCentralWidget(centerWindget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())