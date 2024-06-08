import os
import tkinter as tk
from PySide6.QtWidgets import *


class Windows:

    def __init__(self, w, h):
        self.window = QMainWindow()
        self.window.setWindowTitle('Command')
        self.window.resize(500, 300)
        self.window.move(w, h)

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText('请输入时间/min')

        self.textEdit.move(w * 0.2, h * 0.1)
        self.textEdit.resize(w * 0.5, 30)

        self.textCommand = QPlainTextEdit(self.window)
        self.textCommand.setPlaceholderText('请输入要执行的命令')
        self.textCommand.move(w * 0.1, h * 0.3)
        self.textCommand.resize(w * 0.8, 30)

        self.button = QPushButton('开始执行', self.window)
        self.button.move(w * 0.4, h * 0.5)
        self.button.resize(w * 0.2, h * 0.1)

        self.button.clicked.connect(self.click)

        self.time_min = None
        self.command = None

        self.info = QMessageBox(self.window)
        self.start = QMessageBox(self.window)
        self.stop = QMessageBox(self.window)

    def click(self):
        try:
            self.time_min = float(self.textEdit.toPlainText()) * 1000 * 60
            self.command = self.textCommand.toPlainText()
            if not self.command:
                self.info.show()
                self.info.setInformativeText('请输入命令!')
        except:
            self.info.show()
            self.info.setInformativeText('请输入时间!')

        if self.time_min and self.command:
            sleep = tk.Tk()
            self.start.show()
            self.start.setWindowTitle('正在执行!')

            sleep.after(int(self.time_min))
            os.system(self.command)
            self.start.close()
            self.stop.show()
            self.stop.setInformativeText('执行完毕!')


if __name__ == '__main__':
    # timeStop(10, 'taskkill /F /T /IM QQMusic.exe')
    app = QApplication([])
    main = Windows(500, 400)
    main.window.show()
    app.exec()
