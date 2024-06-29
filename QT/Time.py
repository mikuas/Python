import os
import sys

from QTFunction import *
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QSystemTrayIcon,

    QMenu,
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QTimer

class Windows(QWidget):

    def __init__(self, w, h, path):
        super().__init__()
        self.w = w
        self.h = h
        self.window = QWidget()
        self.window.setWindowTitle('功能')
        self.keyWindow = QWidget()
        self.keyWindow.setWindowTitle('键盘任务')
        self.keyTimeWindow = QWidget()
        self.keyTimeWindow.setWindowTitle('定时键盘任务')
        self.sysWindow = QWidget()
        self.sysWindow.setWindowTitle('System')

        self.setWindowTitle('Timing Task')
        self.resize(w, h)

        # 创建控件
        self.textEdit = QLineEdit()
        # 设置宽高
        self.textEdit.setMinimumSize(w * 0.8, h * 0.2)
        self.textEdit.move(w * 0.1, h * 0.2)
        self.textEdit.setPlaceholderText('请输入时间/s')

        self.textCommand = QLineEdit()
        # 设置宽高
        self.textCommand.setMinimumSize(w * 0.8, h * 0.2)
        self.textCommand.move(w * 0.1, h * 0.6)
        self.textCommand.setPlaceholderText('请输入要执行的命令')

        # 设置按钮
        self.button = QPushButton('开始执行')
        self.button.setMinimumSize(w * 0.3, h * 0.2)

        self.openButton = QPushButton('打开新窗口')

        # 添加点击功能
        self.button.clicked.connect(self.click)
        self.openButton.clicked.connect(self.openWindow)
        self.openButton.setMinimumSize(100, 50)

        # 创建布局管理器并设置布局
        layout = QVBoxLayout(self)  # 创建一个垂直布局管理器，并将其绑定到当前窗口（self）上
        layout.addWidget(self.textEdit)  # 将文本输入框 (self.textEdit) 添加到垂直布局中
        layout.addWidget(self.textCommand)  # 将命令输入框 (self.textCommand) 添加到垂直布局中
        layout.addWidget(self.button)  # 将按钮 (self.button) 添加到垂直布局中
        layout.addWidget(self.openButton)

        self.setLayout(layout)

        # 添加系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        print(True)  # 添加调试输出

        self.tray_icon.setIcon(QIcon(path))
        self.tray_icon.setToolTip('Ciallo～(∠・ω< )⌒☆')

        # 托盘图标菜单
        tray_menu = QMenu()
        show_action_tray = QAction('显示窗口', self)
        show_action_tray.triggered.connect(self.showWindow)

        # 添加分隔符
        tray_menu.addSeparator()

        quit_action = QAction('退出', self)
        quit_action.triggered.connect(self.quitWindow)

        # 添加到托盘中
        tray_menu.addActions([show_action_tray, quit_action])

        # 设置菜单
        self.tray_icon.setContextMenu(tray_menu)

        # 显示系统托盘图标
        self.tray_icon.show()

        # newWindow
        self.keyBoardButton = QPushButton('执行键盘任务', self.window)
        self.keyBoardButton.clicked.connect(self.openKey)
        self.keyBoardTimingButton = QPushButton('定时执行键盘任务', self.window)
        self.keyBoardTimingButton.clicked.connect(self.openTimeKey)
        self.systemCommandButton = QPushButton('系统选项', self.window)
        self.systemCommandButton.clicked.connect(self.powerStart)

        self.keyEdit = QLineEdit(self.keyWindow)
        self.keyStartButton = QPushButton('开始', self.keyWindow)

        self.timeEdit = QLineEdit(self.keyTimeWindow)
        self.keyTimeEdit = QLineEdit(self.keyTimeWindow)
        self.ketTimeStartButton = QPushButton('开始', self.keyTimeWindow)

        self.systemModeEdit = QLineEdit(self.sysWindow)
        self.sysTimeEdit = QLineEdit(self.sysWindow)
        self.sysStartButton = QPushButton('执行', self.sysWindow)

        self.keyStartButton.clicked.connect(self.keyBoardStart)
        self.ketTimeStartButton.clicked.connect(self.keyBoardTimeStart)
        self.sysStartButton.clicked.connect(self.startCommand)

        self.keyEdit.setPlaceholderText('输入按键,多个按键用逗号隔开')
        self.keyTimeEdit.setPlaceholderText('输入按键,多个按键用逗号隔开')
        self.timeEdit.setPlaceholderText('输入时间/s')
        self.systemModeEdit.setPlaceholderText('输入模式, 重启, 关机, 注销')
        self.sysTimeEdit.setPlaceholderText('输入时间,不写默认为0')

    def showWindow(self):
        self.show()

    def keyBoardStart(self):
        print(tuple(self.keyEdit.text().replace(" ", "").split(',')))
        try:
            if self.keyEdit.text():
                KeyBoardControl().keyHotkey(tuple(self.keyEdit.text().replace(" ", "").split(',')))
                QMessageBox.information(self.keyWindow, '提示', '已开始执行')
            else:
                QMessageBox.warning(self.keyWindow, '错误', '请输入!')
        except ValueError:
            pass

    def keyBoardTimeStart(self):
        print(tuple(self.keyTimeEdit.text().replace(" ", "").split(',')), self.timeEdit.text())
        try:
            if self.keyTimeEdit.text() and self.timeEdit.text():
                QTimer.singleShot(float(self.timeEdit.text()) * 1000, lambda: self.getQLineEdit(self.keyTimeEdit))
                print('OK')
                QMessageBox.information(self.keyWindow, '提示', '已开始执行')
            else:
                QMessageBox.warning(self.keyWindow, '错误', '请输入!')
        except ValueError:
            pass

    def getQLineEdit(self, obj):
        KeyBoardControl().keyHotkey(tuple(obj.text().replace(" ", "").split(',')))

        return self

    @staticmethod
    def quitWindow():
        QApplication.quit()

    def startCommand(self):

        if self.sysTimeEdit.text() and self.systemModeEdit.text():
            interval = float(self.sysTimeEdit.text()) * 1000
        else:
            interval = 0

        if self.systemModeEdit.text() == '关机':
            QTimer.singleShot(interval, lambda: os.system('shutdown -s -t 0'))
        elif self.systemModeEdit.text() == '重启':
            QTimer.singleShot(interval, lambda: os.system('shutdown -r -f -t 0'))
        elif self.systemModeEdit.text() == '注销':
            QTimer.singleShot(interval, lambda: os.system('logoff'))
        else:
            QMessageBox.warning(self.sysWindow, '警告', '输入有误,请重新输入!')

    def powerStart(self):
        self.sysWindow.setFixedSize(400, 250)
        self.sysWindow.move(self.w + 155, self.h + 100)
        self.sysWindow.show()

        layout = QVBoxLayout(self.sysWindow)
        layout.addWidget(self.systemModeEdit)
        layout.addWidget(self.sysTimeEdit)
        layout.addWidget(self.sysStartButton)

        self.systemModeEdit.setMinimumSize(100, 60)
        self.sysTimeEdit.setMinimumSize(100, 60)
        self.sysStartButton.setMinimumSize(100, 60)

        self.sysWindow.setLayout(layout)

    def openTimeKey(self):
        self.keyTimeWindow.setFixedSize(400, 250)
        self.keyTimeWindow.move(self.w + 155, self.h + 100)
        self.keyTimeWindow.show()

        layout = QVBoxLayout(self.keyTimeWindow)
        layout.addWidget(self.timeEdit)
        layout.addWidget(self.keyTimeEdit)
        layout.addWidget(self.ketTimeStartButton)

        self.keyTimeEdit.setMinimumSize(100, 60)
        self.timeEdit.setMinimumSize(100, 60)
        self.ketTimeStartButton.setMinimumSize(100, 60)

        self.keyTimeWindow.setLayout(layout)

    def openKey(self):
        self.keyWindow.setFixedSize(400, 250)
        self.keyWindow.move(self.w + 155, self.h + 100)
        self.keyWindow.show()

        layout = QVBoxLayout(self.keyWindow)
        layout.addWidget(self.keyEdit)
        layout.addWidget(self.keyStartButton)

        self.keyEdit.setMinimumSize(100, 60)
        self.keyStartButton.setMinimumSize(100, 60)

        self.keyWindow.setLayout(layout)

    def click(self):
        try:
            time_min = float(self.textEdit.text()) * 1000
            command = self.textCommand.text()

            if not command:
                # 警告窗口 warning
                QMessageBox.warning(self, '提示', '请输入命令!')
                return
            # 执行命令
            QTimer.singleShot(time_min, lambda: os.system(command))
            # 提示窗口 information
            QMessageBox.information(self, '提示', '任务已启动!')

        except ValueError:
            QMessageBox.warning(self, '错误', '请输入正确的时间!')

    def closeEvent(self, event):
        # 重载关闭事件，使得窗口关闭时只是隐藏而不是退出应用程序
        event.ignore()  # 忽略关闭事件
        self.hide()     # 隐藏窗口

    def openWindow(self):
        self.window.resize(400, 500)
        layout = QVBoxLayout(self.window)
        layout.addWidget(self.keyBoardButton)
        layout.addWidget(self.keyBoardTimingButton)
        layout.addWidget(self.systemCommandButton)

        self.keyBoardTimingButton.setMinimumSize(100, 60)
        self.keyBoardButton.setMinimumSize(100, 60)
        self.systemCommandButton.setMinimumSize(100, 60)

        self.window.setLayout(layout)
        self.window.show()

def getFilePath(file_name):
    # 获取打包后的可执行文件所在的临时目录
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    # 构建视频文件的绝对路径
    return os.path.join(base_path, file_name)

def main():
    app = QApplication(sys.argv)
    main_window = Windows(500, 300, getFilePath('icon.png'))
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
