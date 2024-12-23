import os
import sys

from Calc import CaliWindow
from PyMyMethod import FileControl, SystemCtl
from Keyboard.MainWindow import KeyboardMainWindow
from Image.MainWindow import ImageMainWindow
from regedit.MainWindow import RegeditMainWindow
from SubWindow import SubWindow


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

    def __init__(self, width, height, trayIconPath, backgroundPath):
        super().__init__()
        self.flag = True

        self.setWindowTitle('Timing Task')
        self.setMinimumSize(800, 450)
        # 背景图
        self.backgroundPixmap = QPixmap(backgroundPath)
        # 创建输入控件并设置大小策略
        self.textEdit = QLineEdit(self)
        self.textEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.textEdit.setStyleSheet('font-size:20px; background-color: rgba(72, 209, 204, 128); color: deeppink;')
        self.textEdit.setMinimumSize(200, 80)
        self.textEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.textCommand = QLineEdit(self)
        self.textCommand.setPlaceholderText('请输入要执行的命令')
        self.textCommand.setStyleSheet('font-size:20px; background-color: rgba(72, 209, 204, 128); color: deeppink;')
        self.textCommand.setMinimumSize(200, 80)
        self.textCommand.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # 创建按钮
        self.button = QPushButton('开始执行', self)
        self.button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button.setStyleSheet('font-size: 20px; color: dodgerblue; background-color: pink;')
        self.button.setMaximumSize(200, 100)
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.openWindowButton = QPushButton('更多功能', self)
        self.openWindowButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.openWindowButton.setStyleSheet('font-size: 20px; color: dodgerblue; background-color: pink;')
        self.openWindowButton.setMaximumSize(200, 100)
        self.openWindowButton.setCursor(Qt.CursorShape.PointingHandCursor)

        # 添加点击功能
        self.button.clicked.connect(self.click)
        self.openWindowButton.clicked.connect(lambda: (
            self.subWindow.window.show(),
            self.subWindow.window.raise_(),
            self.subWindow.window.activateWindow()
        ))

        # 创建主部件和布局
        mainWidget = QWidget(self)
        # 垂直布局
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.textEdit)
        mainLayout.addWidget(self.textCommand)

        # 水平布局
        layout = QHBoxLayout()
        # 设置按钮大小随窗口改变而改变
        self.button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.openWindowButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # 添加到水平布局
        layout.addWidget(self.button)
        layout.addWidget(self.openWindowButton)
        # 把水平布局添加到垂直布局
        mainLayout.addLayout(layout)
        mainWidget.setLayout(mainLayout)

        self.setCentralWidget(mainWidget)

# ---------------------------------------------------------------------------------------------------------- #

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon(trayIconPath))
        self.trayIcon.setToolTip('Ciallo～(∠・ω< )⌒☆')
        self.trayIcon.activated.connect(lambda reason: (self.show(), self.raise_(), self.activateWindow()) if reason == QSystemTrayIcon.ActivationReason.Trigger else reason)
        # 托盘图标菜单
        trayMenu = QMenu()
        # 添加分隔符
        trayMenu.addSeparator()

        showActionTray = QAction('显示窗口', self)
        showActionTray.triggered.connect(lambda: (self.show(), self.raise_(), self.activateWindow()))
        quitAction = QAction('退出', self)
        quitAction.triggered.connect(self.quitApp)
        # 添加到托盘中
        trayMenu.addActions([showActionTray, quitAction])
        # 设置菜单
        self.trayIcon.setContextMenu(trayMenu)
        # 显示系统托盘图标
        self.trayIcon.show()

# ---------------------------------------------------------------------------------------------------------- #

        self.subWindow = SubWindow(
            KeyboardMainWindow(width, height).window,
            ImageMainWindow(width, height).window,
            RegeditMainWindow().window,
            CaliWindow().window
        )

# ---------------------------------------------------------------------------------------------------------- #

    def paintEvent(self, event):
        # 创建 QPainter 对象
        painter = QPainter(self)

        # 获取窗口的宽度和高度
        windowWidth = self.width()
        windowHeight = self.height()

        # 将背景图片缩放到窗口大小，并使用平滑转换模式
        scaledPixmap = self.backgroundPixmap.scaled(
            windowWidth, windowHeight, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation
        )

        # 在窗口内绘制缩放后的背景图片
        painter.drawPixmap(0, 0, scaledPixmap)

    def closeEvent(self, event):

        # 重载关闭事件，使得窗口关闭时只是隐藏而不是退出应用程序
        event.ignore()  # 忽略关闭事件
        self.hide()  # 隐藏窗口
        if self.flag:
            self.trayIcon.showMessage(
                'Timing Task',
                '程序已最小化到系统托盘',
                QSystemTrayIcon.MessageIcon.Information,
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
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap(imagePath)))

        return palette

# ---------------------------------------------------------------------------------------------------------- #

def main():
    app = QApplication(sys.argv)
    window = MainWindow(
        650,
        350,
        # package
        # FileControl().getFilePackagePath('./trayIcon.png'),
        # FileControl().getFilePackagePath('./background.png')
        FileControl().getFileAbsolutePath('./trayIcon.png'),
        FileControl().getFileAbsolutePath('./background.png')
    )
    window.show()
    window.raise_()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

