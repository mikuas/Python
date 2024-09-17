import os
import sys

from method import SystemCtl
from KeyboardTaskWindow import KeyboardTaskWindow
from KeyboardHotTaskWindow import KeyboardHotTaskWindow
from ImageReName import ImageRenameWindow

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
        self.flag = True

        self.setWindowTitle('Timing Task')
        self.setMinimumSize(800, 450)
        # 背景图
        self.backgroundPixmap = QPixmap(backgroundPath)

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
        # 创建输入控件并设置大小策略
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
        self.openWindowButton.clicked.connect(lambda: self.window.show())

        # 创建主部件和布局
        mainWidget = QWidget(self)
        # 垂直布局
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.textEdit)
        mainLayout.addWidget(self.textCommand)

        # 水平布局
        layout = QHBoxLayout()
        # 设置按钮大小随窗口改变而改变
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.openWindowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 添加到水平布局
        layout.addWidget(self.button)
        layout.addWidget(self.openWindowButton)
        # 把水平布局添加到垂直布局
        mainLayout.addLayout(layout)
        mainWidget.setLayout(mainLayout)

        self.setCentralWidget(mainWidget)

# ---------------------------------------------------------------------------------------------------------- #

        # 添加系统托盘图标
        self.trayIcon = QSystemTrayIcon(self)
        # print(True)  # 添加调试输出
        self.trayIcon.setIcon(QIcon(path))
        self.trayIcon.setToolTip('Ciallo～(∠・ω< )⌒☆')

        # 托盘图标菜单
        trayMenu = QMenu()
        showActionTray = QAction('显示窗口', self)
        showActionTray.triggered.connect(lambda: self.show())

        # 添加分隔符
        trayMenu.addSeparator()

        quitAction = QAction('退出', self)
        quitAction.triggered.connect(self.quitApp)
        # 添加到托盘中
        trayMenu.addActions([showActionTray, quitAction])
        # 设置菜单
        self.trayIcon.setContextMenu(trayMenu)
        # 显示系统托盘图标
        self.trayIcon.show()

# ---------------------------------------------------------------------------------------------------------- #

        self.window = QWidget()
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.keyboardButton = QPushButton('依次点击键盘任务', self.window)
        self.keyboardButton.setStyleSheet(self.style[2])
        self.keyboardButton.setFixedSize(250, 50)
        self.keyboardButton.clicked.connect(lambda: self.keyboardTaskWindow.show())

        self.keyboardHotButton = QPushButton('组合键任务', self.window)
        self.keyboardHotButton.setStyleSheet(self.style[2])
        self.keyboardHotButton.setFixedSize(250, 50)
        self.keyboardHotButton.clicked.connect(lambda: self.keyboardHotTaskWindow.show())

        self.imageRenameButton = QPushButton('图片重命名', self.window)
        self.imageRenameButton.setStyleSheet(self.style[2])
        self.imageRenameButton.setFixedSize(250, 50)
        self.imageRenameButton.clicked.connect(lambda: (QMessageBox.information(self, '提示', '从0开始,依次命名,当前仅支持jpg,png'), self.imageReNameWindow.show()))

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
        windowWidth = self.width()
        windowHeight = self.height()

        # 将背景图片缩放到窗口大小，并使用平滑转换模式
        scaled_pixmap = self.backgroundPixmap.scaled(
            windowWidth, windowHeight, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

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
        if self.flag:
            self.trayIcon.showMessage(
                "Timing Task",
                "程序已最小化到系统托盘",
                QSystemTrayIcon.Information,
                2000
            )

# ---------------------------------------------------------------------------------------------------------- #

    def click(self):
        try:
            if not self.textEdit.text():
                time = 0
            else:
                time = float(self.textEdit.text()) * 1000
            command = self.textCommand.text()

            if not command:
                QMessageBox.warning(self, '提示', '请输入命令!')
                return
            SystemCtl().systemOption(time, command)
            QTimer.singleShot(time, lambda: os.system(command))
            if time:
                QMessageBox.information(self, '提示', '任务已启动!')
            else:
                QMessageBox.information(self, '提示', '执行完毕!')

        except ValueError:
            QMessageBox.warning(self, '错误', '请输入正确的时间!')

    def quitApp(self):
        # 关闭所有窗口
        self.flag = False
        for widget in QApplication.topLevelWidgets():
            widget.close()
        # 推出软件
        QApplication.quit()

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
        SystemCtl().getFilePath('./icon.png'),
        SystemCtl().getFilePath('./ATRI.png')
    )
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

