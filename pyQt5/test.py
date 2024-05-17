from PySide6 import QtWidgets
import sys


class Window2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口2')

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        button = QtWidgets.QPushButton('按钮2')

        grid = QtWidgets.QGridLayout(central_widget)
        grid.addWidget(button)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口1')

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        button = QtWidgets.QPushButton('打开新窗口')
        button.clicked.connect(self.open_new_window)

        grid = QtWidgets.QGridLayout(central_widget)
        grid.addWidget(button)

    def open_new_window(self):
        # 实例化另外一个窗口
        self.window2 = Window2()
        # 显示新窗口
        self.window2.show()
        # 关闭自己
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
