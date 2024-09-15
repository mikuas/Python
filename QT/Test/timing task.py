import os
import sys

from jinja2.nodes import Continue

from method import SystemControl
from KeyboardTaskWindow import KeyboardTaskWindow
from KeyboardHotTaskWindow import KeyboardHotTaskWindow
from ImageReName import ImageRenameWindow
from systemctl import Systemctl

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QMainWindow,
    QSizePolicy,
    QSystemTrayIcon,
    QMenu,
    QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QAction, QPalette, QBrush, QPixmap, QPainter

class MainWindow(QMainWindow):

    def __init__(self, width, height, path=None, backgroundPath=None):
        super().__init__()

        self.setWindowTitle('Timing Task')
        self.setMinimumSize(800, 450)
        # self.resize(800, 450)

        # 背景图
        # self.setPalette(self.setBackground(backgroundPath))
        self.background_pixmap = QPixmap(backgroundPath)

        # 创建输入控件并设置大小策略
        self.style = [
            """
            QLineEdit {
            font-size:20px;
            background-color: rgba(72, 209, 204, 128);
            color: deeppink;  
            }
            """,
            """
            QPushButton {
            font-size: 20px;
            color: dodgerblue;
            background-color: pink;
            }
            """,
            """
            QPushButton {
            font-size: 14px;
            }
            """
        ]
        self.textEdit = QLineEdit(self)
        self.textEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.textEdit.setStyleSheet(self.style[0])

        self.textEdit.setMinimumSize(200, 80)
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.textCommand = QLineEdit(self)
        self.textCommand.setPlaceholderText('请输入要执行的命令')
        self.textCommand.setStyleSheet(self.style[0])
        self.textCommand.setMinimumSize(200, 80)
        self.textCommand.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # 创建按钮
        self.button = QPushButton('开始执行', self)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button.setStyleSheet(self.style[1])
        self.button.setMaximumSize(200, 100)
        self.openWindowButton = QPushButton('更多功能', self)
        self.openWindowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.openWindowButton.setStyleSheet(self.style[1])
        self.openWindowButton.setMaximumSize(200, 100)

        # 添加点击功能
        self.button.clicked.connect(self.click)
        self.openWindowButton.clicked.connect(self.newWindow)

        # 创建主部件和布局
        main_widget = QWidget(self)
        # 垂直布局
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.textEdit)
        main_layout.addWidget(self.textCommand)

        # 水平布局
        layout = QHBoxLayout()

        # 设置按钮大小随窗口改变而改变
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.openWindowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 添加到水平布局
        layout.addWidget(self.button)
        layout.addWidget(self.openWindowButton)

        # 把水平布局添加到垂直布局
        main_layout.addLayout(layout)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

# ---------------------------------------------------------------------------------------------------------- #

        # 添加系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        # print(True)  # 添加调试输出
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

# ---------------------------------------------------------------------------------------------------------- #

        self.window = QWidget()
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.keyboardButton = QPushButton('依次点击键盘任务', self.window)
        self.keyboardButton.setStyleSheet(self.style[2])
        self.keyboardButton.setFixedSize(250, 50)
        self.keyboardButton.clicked.connect(self.keyboardTask)

        self.keyboardHotButton = QPushButton('组合键任务', self.window)
        self.keyboardHotButton.setStyleSheet(self.style[2])
        self.keyboardHotButton.setFixedSize(250, 50)
        self.keyboardHotButton.clicked.connect(self.keyboardHotTask)

        self.imageRenameButton = QPushButton('图片重命名', self.window)
        self.imageRenameButton.setStyleSheet(self.style[2])
        self.imageRenameButton.setFixedSize(250, 50)
        self.imageRenameButton.clicked.connect(self.imageRenameWindow)

        layout = QVBoxLayout(self.window)
        layout.addWidget(self.keyboardButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(self.keyboardHotButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(self.imageRenameButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)


        self.keyboardTaskWindow = KeyboardTaskWindow(width, height)
        self.keyboardHotTaskWindow = KeyboardHotTaskWindow(width, height)
        self.imageReNameWindow = ImageRenameWindow(width, height)

    def paintEvent(self, event):
        # 创建 QPainter 对象
        painter = QPainter(self)

        # 获取窗口的宽度和高度
        window_width = self.width()
        window_height = self.height()

        # 将背景图片缩放到窗口大小，并使用平滑转换模式
        scaled_pixmap = self.background_pixmap.scaled(
            window_width, window_height, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # 在窗口内绘制缩放后的背景图片
        painter.drawPixmap(0, 0, scaled_pixmap)

    @staticmethod
    def ignoreCloseEvent(event, window):
        event.ignore()
        window.hide()

    def closeEvent(self, event):

        # 重载关闭事件，使得窗口关闭时只是隐藏而不是退出应用程序
        event.ignore()  # 忽略关闭事件
        self.hide()  # 隐藏窗口
        self.tray_icon.showMessage(
            "Timing Task",
            "程序已最小化到系统托盘",
            QSystemTrayIcon.Information,
            2000
        )

# ---------------------------------------------------------------------------------------------------------- #

    def keyboardTask(self):
        self.keyboardTaskWindow.show()

    def keyboardHotTask(self):
        self.keyboardHotTaskWindow.show()

    def imageRenameWindow(self):
        QMessageBox.information(self, '提示', '从0开始,依次命名,当前仅支持jpg,png')
        self.imageReNameWindow.show()

    def click(self):
        try:
            if not self.textEdit.text():
                time_min = 0
            else:
                time_min = float(self.textEdit.text()) * 1000
            command = self.textCommand.text()

            if not command:
                QMessageBox.warning(self, '提示', '请输入命令!')
                return
            Systemctl().systemOption(time_min, command)
            QTimer.singleShot(time_min, lambda: os.system(command))
            if time_min:
                QMessageBox.information(self, '提示', '任务已启动!')
            else:
                QMessageBox.information(self, '提示', '执行完毕!')

        except ValueError:
            QMessageBox.warning(self, '错误', '请输入正确的时间!')

    def newWindow(self):
        self.window.show()

    @staticmethod
    def setBackground(imagePath):
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap(imagePath)))

        return palette

# ---------------------------------------------------------------------------------------------------------- #

def main():
    app = QApplication(sys.argv)
    window = MainWindow(
        650,
        350,
        SystemControl().getFilePath('./icon.png'),
        SystemControl().getFilePath('./ATRI.png')
    )
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()




