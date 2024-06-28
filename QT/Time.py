import os
import tkinter as tk
from PySide6.QtWidgets import *


class Windows(QWidget):

    def __init__(self, w, h):
        super().__init__()
        self.window = QMainWindow()
        self.window.setWindowTitle('Timing Task')
        self.window.resize(500, 300)
        self.window.move(w, h)

        self.textEdit = QLineEdit(self.window)
        self.textEdit.setPlaceholderText('请输入时间/s')

        self.textEdit.move(w * 0.1, h * 0.1)
        self.textEdit.resize(w * 0.8, 50)

        self.textCommand = QLineEdit(self.window)
        self.textCommand.setPlaceholderText('请输入要执行的命令')
        self.textCommand.move(w * 0.1, h * 0.3)
        self.textCommand.resize(w * 0.8, 50)

        self.button = QPushButton('开始执行', self.window)
        self.button.move(w * 0.4, h * 0.5)
        self.button.resize(w * 0.2, h * 0.1)

        self.button.clicked.connect(self.click)

        self.time_min = None
        self.command = None

        self.info = QMessageBox(self.window)
        self.start = QMessageBox(self.window)
        self.stop = QMessageBox(self.window)
        self.window.setTabOrder(self.textEdit, self.textCommand)

    def center(self):
        # 获取屏幕的尺寸和居中点
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2

        # 将窗口移到屏幕中心
        self.window.move(x, y)

    def click(self):
        try:
            self.time_min = float(self.textEdit.text()) * 1000
            self.command = self.textCommand.text()  # 获取 QLineEdit的内容 .text()
            if not self.command:
                self.info.show()
                self.info.setInformativeText('请输入命令!')
        except:
            self.info.show()
            self.info.setInformativeText('请输入正确的时间!')

        if self.time_min and self.command:
            sleep = tk.Tk()
            self.start.show()
            self.start.setWindowTitle('正在执行!')
            sleep.after(int(self.time_min))
            os.system(self.command)
            self.start.close()
            self.stop.show()
            self.stop.setInformativeText('执行完毕!')

def main():
    # timeStop(10, 'taskkill /F /T /IM QQMusic.exe')
    app = QApplication([])
    main_window = Windows(500, 400)
    main_window.center()
    main_window.window.show()
    app.exec()


if __name__ == '__main__':
    main()