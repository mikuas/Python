import os
import sys

from method import KeyboardControl

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

        self.keyTaskWindow = QWidget()
        self.keyTaskWindow.setWindowTitle('键盘任务')

        self.keyTaskTimeWindow = QWidget()
        self.keyTaskTimeWindow.setWindowTitle('定时键盘任务')

        self.hotKeyTaskWindow = QWidget()
        self.hotKeyTaskWindow.setWindowTitle('组合键盘任务')

        self.hotKeyTimeTaskWindow = QWidget()
        self.hotKeyTimeTaskWindow.setWindowTitle('定时组合键盘任务')

        self.systemTask = QWidget()
        self.systemTask.setWindowTitle('System')

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
        show_action_tray.triggered.connect(lambda: self.show())
        # 添加分隔符
        tray_menu.addSeparator()

        quit_action = QAction('退出', self)
        quit_action.triggered.connect(lambda: QApplication.quit())

        # 添加到托盘中
        tray_menu.addActions([show_action_tray, quit_action])

        # 设置菜单
        self.tray_icon.setContextMenu(tray_menu)

        # 显示系统托盘图标
        self.tray_icon.show()

        # newWindow
        self.keyBoardButton = QPushButton('逐一执行键盘任务', self.window)
        self.keyBoardButton.clicked.connect(self.openKey)

        self.keyEdit = QLineEdit(self.keyTaskWindow)
        self.keyEdit.setPlaceholderText('输入按键,多个按键用逗号隔开')
        self.keyStartButton = QPushButton('开始', self.keyTaskWindow)
        self.keyStartButton.clicked.connect(self.keyBoardStart)
        # ------------------------------------------------------------------------------------ #

        self.keyBoardTimingButton = QPushButton('定时逐一执行键盘任务', self.window)
        self.keyBoardTimingButton.clicked.connect(self.openTimeKey)
        self.keyTimeEdit = QLineEdit(self.keyTaskTimeWindow)
        self.timeEdit = QLineEdit(self.keyTaskTimeWindow)
        self.timeEdit.setPlaceholderText('输入时间/s')
        self.keyTimeEdit.setPlaceholderText('输入按键,多个按键用逗号隔开')
        self.ketTimeStartButton = QPushButton('开始', self.keyTaskTimeWindow)
        self.ketTimeStartButton.clicked.connect(self.keyBoardStart)
        # ------------------------------------------------------------------------------------ #

        self.hotKeyButton = QPushButton('执行组合按键任务', self.window)
        self.hotKeyButton.clicked.connect(self.openHotKey)
        self.hotkeyEdit = QLineEdit(self.hotKeyTaskWindow)
        self.hotkeyEdit.setPlaceholderText('输入按键,多个按键用逗号隔开')
        self.hotKeyStartButton = QPushButton('开始', self.hotKeyTaskWindow)
        self.hotKeyStartButton.clicked.connect(self.hotKeyStart)
        # ------------------------------------------------------------------------------------ #

        self.hotkeyBoardTimingButton = QPushButton('定时执行行组合键盘任务', self.window)
        self.hotkeyBoardTimingButton.clicked.connect(self.openTimeHotKey)
        self.hotKeyTimeEdit = QLineEdit(self.hotKeyTimeTaskWindow)
        self.hotKeyTime = QLineEdit(self.hotKeyTimeTaskWindow)
        self.hotKeyTime.setPlaceholderText('输入时间/s')
        self.hotKeyTimeEdit.setPlaceholderText('输入按键,多个按键用逗号隔开')
        self.hotKeytimeStartButton = QPushButton('开始', self.hotKeyTimeTaskWindow)
        self.hotKeytimeStartButton.clicked.connect(self.hotKeyTimeStart)

        # ------------------------------------------------------------------------------------ #

        self.systemCommandButton = QPushButton('系统选项', self.window)
        self.systemCommandButton.clicked.connect(self.powerStart)
        self.systemModeEdit = QLineEdit(self.systemTask)
        self.sysTimeEdit = QLineEdit(self.systemTask)
        self.sysStartButton = QPushButton('执行', self.systemTask)
        self.sysStartButton.clicked.connect(self.startSystemCommand)

        self.systemModeEdit.setPlaceholderText('输入模式, 关机(1),重启(2),注销(3),锁定(4)')
        self.sysTimeEdit.setPlaceholderText('输入时间,不写默认为0')

    def openWindow(self):
        self.window.setFixedSize(400, 500)
        layout = QVBoxLayout(self.window)
        layout.addWidget(self.keyBoardButton)
        layout.addWidget(self.keyBoardTimingButton)
        layout.addWidget(self.hotKeyButton)
        layout.addWidget(self.hotkeyBoardTimingButton)
        layout.addWidget(self.systemCommandButton)

        self.keyBoardButton.setMinimumSize(100, 60)
        self.keyBoardTimingButton.setMinimumSize(100, 60)
        self.hotKeyButton.setMinimumSize(100, 60)
        self.hotkeyBoardTimingButton.setMinimumSize(100, 60)
        self.systemCommandButton.setMinimumSize(100, 60)

        self.window.setLayout(layout)
        self.window.show()

    def hotKeyStart(self):
        try:
            if self.hotkeyEdit.text():
                KeyboardControl().Hotkey(self.hotkeyEdit.text())
                QMessageBox.information(self.hotKeyTaskWindow, '提示', '已开始执行')
            else:
                QMessageBox.warning(self.hotKeyTaskWindow, '错误', '请输入!')
        except ValueError:
            pass

    def keyBoardStart(self):
        print(tuple(self.keyEdit.text().replace(" ", "").split(',')))
        try:
            if self.timeEdit.text():
                QTimer.singleShot(int(self.timeEdit.text()) * 1000, lambda: self.getQLineEdit(self.keyTimeEdit.text()))
                QMessageBox.information(self.keyTaskWindow, '提示', '已开始执行')
                return

            if self.keyEdit.text():
                KeyboardControl().keyPress(self.keyEdit.text())
                QMessageBox.information(self.keyTaskWindow, '提示', '已开始执行')
            else:
                QMessageBox.warning(self.keyTaskWindow, '错误', '请输入!')
        except ValueError:
            pass

    def getQLineEdit(self, obj):
        KeyboardControl().keyPress(obj)

        return self

    def hotKeyTimeStart(self):
        pass
        try:
            if self.hotKeyTimeEdit.text():
                QTimer.singleShot(int(self.hotKeyTime.text()) * 1000, lambda: self.getQLineEdit(self.hotKeyTimeEdit.text()))
                QMessageBox.information(self.hotKeyTimeTaskWindow, '提示', '已开始执行')
            else:
                QMessageBox.warning(self.hotKeyTimeTaskWindow, '警告', '输入有误,请重新输入!')
                return

        except ValueError:
            pass

    def startSystemCommand(self):

        if self.sysTimeEdit.text() and self.systemModeEdit.text():
            interval = float(self.sysTimeEdit.text()) * 1000
        else:
            interval = 0

        if self.systemModeEdit.text() == '关机' or self.systemModeEdit.text() == '1':
            # QTimer.singleShot(interval, lambda: print(1))
            QTimer.singleShot(interval, lambda: os.system('shutdown -s -t 0'))
        elif self.systemModeEdit.text() == '重启' or self.systemModeEdit.text() == '2':
            QTimer.singleShot(interval, lambda: os.system('shutdown -r -f -t 0'))
            # QTimer.singleShot(interval, lambda: print(2))
        elif self.systemModeEdit.text() == '注销' or self.systemModeEdit.text() == '3':
            QTimer.singleShot(interval, lambda: os.system('logoff'))
            # QTimer.singleShot(interval, lambda: print(3))
        elif self.systemModeEdit.text() == '锁定' or self.systemModeEdit.text() == '4':
            QTimer.singleShot(interval, lambda: os.system('rundll32.exe user32.dll,LockWorkStation'))
            # QTimer.singleShot(interval, lambda: print(4))
        else:
            QMessageBox.warning(self.systemTask, '警告', '输入有误,请重新输入!')
            return
        QMessageBox.information(self.systemTask, '提示', '已开始执行')

    def openTimeHotKey(self):
        self.hotKeyTimeTaskWindow.setFixedSize(400, 250)
        self.hotKeyTimeTaskWindow.move(self.w + 155, self.h + 100)
        self.hotKeyTimeTaskWindow.show()

        layout = QVBoxLayout(self.hotKeyTimeTaskWindow)
        layout.addWidget(self.hotKeyTime)
        layout.addWidget(self.hotKeyTimeEdit)
        layout.addWidget(self.hotKeytimeStartButton)

        self.hotKeyTime.setMinimumSize(100, 60)
        self.hotKeyTimeEdit.setMinimumSize(100, 60)
        self.hotKeytimeStartButton.setMinimumSize(100, 60)

        self.hotKeyTimeTaskWindow.setLayout(layout)

    def openHotKey(self):
        self.hotKeyTaskWindow.setFixedSize(400, 250)
        self.hotKeyTaskWindow.move(self.w + 155, self.h + 100)
        self.hotKeyTaskWindow.show()

        layout = QVBoxLayout(self.hotKeyTaskWindow)
        layout.addWidget(self.hotkeyEdit)
        layout.addWidget(self.hotKeyStartButton)

        self.hotkeyEdit.setMinimumSize(100, 60)
        self.hotKeyStartButton.setMinimumSize(100, 60)

        self.hotKeyTaskWindow.setLayout(layout)

    def powerStart(self):
        self.systemTask.setFixedSize(400, 250)
        self.systemTask.move(self.w + 155, self.h + 100)
        self.systemTask.show()

        layout = QVBoxLayout(self.systemTask)
        layout.addWidget(self.systemModeEdit)
        layout.addWidget(self.sysTimeEdit)
        layout.addWidget(self.sysStartButton)

        self.systemModeEdit.setMinimumSize(100, 60)
        self.sysTimeEdit.setMinimumSize(100, 60)
        self.sysStartButton.setMinimumSize(100, 60)

        self.systemTask.setLayout(layout)

    def openTimeKey(self):
        self.keyTaskTimeWindow.setFixedSize(400, 250)
        self.keyTaskTimeWindow.move(self.w + 155, self.h + 100)
        self.keyTaskTimeWindow.show()

        layout = QVBoxLayout(self.keyTaskTimeWindow)
        layout.addWidget(self.timeEdit)
        layout.addWidget(self.keyTimeEdit)
        layout.addWidget(self.ketTimeStartButton)

        self.keyTimeEdit.setMinimumSize(100, 60)
        self.timeEdit.setMinimumSize(100, 60)
        self.ketTimeStartButton.setMinimumSize(100, 60)

        self.keyTaskTimeWindow.setLayout(layout)

    def openKey(self):
        self.keyTaskWindow.setFixedSize(400, 250)
        self.keyTaskWindow.move(self.w + 155, self.h + 100)
        self.keyTaskWindow.show()

        layout = QVBoxLayout(self.keyTaskWindow)
        layout.addWidget(self.keyEdit)
        layout.addWidget(self.keyStartButton)

        self.keyEdit.setMinimumSize(100, 60)
        self.keyStartButton.setMinimumSize(100, 60)

        self.keyTaskWindow.setLayout(layout)

    def click(self):
        try:
            time_min = int(self.textEdit.text()) * 1000
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

def a(time, command):
    QTimer.singleShot(int(time), lambda: os.system(command))

if __name__ == '__main__':
    main()