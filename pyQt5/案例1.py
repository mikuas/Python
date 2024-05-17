from PySide6 import QtWidgets
from PySide6.QtWidgets import *


class MainWindow:

    def __init__(self, win_width, win_height, app_title):
        self.window = QMainWindow()
        self.window.resize(win_width, win_height)
        self.window.move(300, 300)
        self.window.setWindowTitle(app_title)
        list_widget = QtWidgets.QListWidget(parent=self.window)
        list_item = QListWidgetItem()
        # list_item.setWindowIcon()
        list_widget.addItem(list_item)
        list_widget.addItems(['Hello', 'Python', 'Pyside6'])


if __name__ == '__main__':

    app = QApplication([])

    main_win = MainWindow(800, 500, 'HTTP 接口测试')
    main_win.window.show()
    app.exec()



