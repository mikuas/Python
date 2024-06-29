import os
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QWidgetAction,
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
        # 添加点击功能
        self.button.clicked.connect(self.click)

        # 创建布局管理器并设置布局
        layout = QVBoxLayout(self)  # 创建一个垂直布局管理器，并将其绑定到当前窗口（self）上
        layout.addWidget(self.textEdit)  # 将文本输入框 (self.textEdit) 添加到垂直布局中
        layout.addWidget(self.textCommand)  # 将命令输入框 (self.textCommand) 添加到垂直布局中
        layout.addWidget(self.button)  # 将按钮 (self.button) 添加到垂直布局中

        self.setLayout(layout)

        # 添加系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        print('System tray icon created')  # 添加调试输出

        self.tray_icon.setIcon(QIcon(path))
        self.tray_icon.setToolTip('后台运行示例')

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

    def showWindow(self):
        self.show()

    @staticmethod
    def quitWindow():
        QApplication.quit()

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

def main():
    # 获取打包后的可执行文件所在的临时目录
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    # 构建视频文件的绝对路径
    picture_path = os.path.join(base_path, 'icon.png')
    app = QApplication([])
    main_window = Windows(500, 300, picture_path)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
