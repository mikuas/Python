import os
import sys

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import comtypes
import pyautogui

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
    QMenu, QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QAction, QPalette, QBrush, QPixmap, QPainter

class MainWindow(QMainWindow):

    def __init__(self, width, height, path=None, backgroundPath=None):
        super().__init__()

        self.setWindowTitle('Timing Task')
        self.resize(800, 450)

        # 背景图
        # self.setPalette(self.setBackground(backgroundPath))
        self.background_pixmap = QPixmap(backgroundPath)

        # 创建输入控件并设置大小策略
        self.textEdit = QLineEdit(self)
        self.textEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.textEdit.setStyleSheet("""
            QLineEdit {
                font-size:20px;
                background-color: rgba(72, 209, 204, 128);
                color: deeppink;  
            }
        """)

        self.textEdit.setMinimumSize(200, 80)
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.textCommand = QLineEdit(self)
        self.textCommand.setPlaceholderText('请输入要执行的命令')
        self.textCommand.setStyleSheet("""
            QLineEdit {
                font-size:20px;
                background-color: rgba(72, 209, 204, 128);
                color: deeppink;    
            }
        """)
        self.textCommand.setMinimumSize(250, 100)
        self.textCommand.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # 创建按钮
        self.button = QPushButton('开始执行', self)
        self.button.bgc = QPixmap(backgroundPath)
        self.button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                color: dodgerblue;
                background-color: pink;
            }
        """)
        self.button.setMaximumSize(200, 100)
        self.openWindowButton = QPushButton('更多功能', self)
        self.openWindowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.openWindowButton.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                color: dodgerblue;
                background-color: pink;
            }
        """)
        self.openWindowButton.setMaximumSize(200, 100)

        # 添加点击功能
        self.button.clicked.connect(self.click)
        self.openWindowButton.clicked.connect(self.newWindow)

        self.keyboardTaskWindow = QWidget()
        self.keyboardTaskWindow.closeEvent = lambda event: self.ignoreCloseEvent(event, self.keyboardTaskWindow)
        self.keyboardTaskWindow.setFixedSize(width, height)
        self.keyboardTaskWindow.setWindowTitle('执行依次点击键盘任务')

        self.keyboardEdit = QLineEdit(self.keyboardTaskWindow)
        self.keyboardEdit.setPlaceholderText('请输入按键,多个按键之间用逗号隔开')
        self.keyboardEdit.setStyleSheet("""
            QLineEdit {
                font-size:18px;    
            }
        """)
        self.keyboardEdit.setMinimumSize(200, 80)
        self.keyboardEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.keyboardTimeEdit = QLineEdit(self.keyboardTaskWindow)
        self.keyboardTimeEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.keyboardTimeEdit.setStyleSheet("""
            QLineEdit {
                font-size:18px;    
            }
        """)
        self.keyboardTimeEdit.setMinimumSize(200, 80)
        self.keyboardTimeEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.keyboardTaskButton = QPushButton('开始执行', self.keyboardTaskWindow)
        self.keyboardTaskButton.setFixedSize(150, 50)
        self.keyboardTaskButton.clicked.connect(self.keyboardClick)

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

        self.keyboardHotTaskWindow = QWidget()
        self.keyboardHotTaskWindow.closeEvent = lambda event: self.ignoreCloseEvent(event, self.keyboardHotTaskWindow)
        self.keyboardHotTaskWindow.setFixedSize(width, height)
        self.keyboardHotTaskWindow.setWindowTitle('执行组合键盘任务')

        self.keyboardHotEdit = QLineEdit(self.keyboardHotTaskWindow)
        self.keyboardHotEdit.setPlaceholderText('请输入按键,多个按键之间用逗号隔开')
        self.keyboardHotEdit.setStyleSheet("""
            QLineEdit {
                font-size:18px;    
            }
        """)
        self.keyboardHotEdit.setMinimumSize(200, 80)
        self.keyboardHotEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.keyboardTimeHotEdit = QLineEdit(self.keyboardHotTaskWindow)
        self.keyboardTimeHotEdit.setPlaceholderText('请输入时间/s,不写默认为0')
        self.keyboardTimeHotEdit.setStyleSheet("""
            QLineEdit {
                font-size:18px;    
            }
        """)
        self.keyboardTimeHotEdit.setMinimumSize(200, 80)
        self.keyboardTimeHotEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.keyboardTaskHotButton = QPushButton('开始执行', self.keyboardHotTaskWindow)
        self.keyboardTaskHotButton.setFixedSize(150, 50)
        self.keyboardTaskHotButton.clicked.connect(self.keyboardHotClick)

        layout = QVBoxLayout(self.keyboardHotTaskWindow)
        layout.addWidget(self.keyboardHotEdit)
        layout.addStretch(1)
        layout.addWidget(self.keyboardTimeHotEdit)
        layout.addStretch(1)
        layout.addWidget(self.keyboardTaskHotButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)

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
        self.window.setFixedSize(400, 559)
        # self.window.setPalette(self.setBackground('./yuexia.jpg'))

        self.keyboardButton = QPushButton('依次点击键盘任务', self.window)
        # self.keyboardButton.setStyleSheet("background-color: pink")
        self.keyboardButton.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                }
        """)
        self.keyboardButton.setFixedSize(250, 50)
        self.keyboardButton.clicked.connect(self.keyboardTask)

        self.keyboardHotButton = QPushButton('组合键任务', self.window)
        self.keyboardHotButton.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                }
        """)
        self.keyboardHotButton.setFixedSize(250, 50)
        self.keyboardHotButton.clicked.connect(self.keyboardHotTask)

        layout = QVBoxLayout(self.window)
        layout.addWidget(self.keyboardButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(self.keyboardHotButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)

    def paintEvent(self, event):
        # 创建 QPainter 对象
        painter = QPainter(self.button)

        # 获取窗口的宽度和高度
        window_width = self.width()
        window_height = self.height()

        # 将背景图片缩放到窗口大小，并使用平滑转换模式
        scaled_pixmap = self.background_pixmap.scaled(
            window_width, window_height, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        scaled_pixmap = self.button.bgc.scaled(
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
    # 点击功能

    def keyboardClick(self):
        try:
            if self.keyboardTimeEdit.text():
                time_min = float(self.keyboardTimeEdit.text()) * 1000
            else:
                time_min = 0
            keys = self.keyboardEdit.text()

            if not keys:
                QMessageBox.warning(self.keyboardTaskWindow, '提示', '请输入按键!')
                return

            QTimer.singleShot(time_min, lambda: KeyboardControl().keyPress(keys))
            if time_min:
                QMessageBox.information(self.keyboardTaskWindow, '提示', '任务已启动!')
            else:
                QMessageBox.information(self.keyboardTaskWindow, '提示', '执行完毕!')
            print(self.keyboardTimeEdit.text())
        except ValueError:
            QMessageBox.warning(self.keyboardTaskWindow, '错误', '请输入正确的时间!')

    def keyboardHotClick(self):
        try:
            if not self.keyboardTimeHotEdit.text():
                time_min = 0
            else:
                time_min = float(self.keyboardTimeHotEdit.text()) * 1000
            hotKeys = self.keyboardHotEdit.text()

            if not hotKeys:
                QMessageBox.warning(self.keyboardHotTaskWindow, '提示', '请输入按键!')
                return

            QTimer.singleShot(time_min, lambda: KeyboardControl().keyHotkey(hotKeys))
            if time_min:
                QMessageBox.information(self.keyboardHotTaskWindow, '提示', '任务已启动!')
            else:
                QMessageBox.information(self.keyboardTaskWindow, '提示', '执行完毕!')

        except ValueError:
            QMessageBox.warning(self.keyboardHotTaskWindow, '错误', '请输入正确的时间!')

    def keyboardTask(self):
        self.keyboardTaskWindow.show()

    def keyboardHotTask(self):
        self.keyboardHotTaskWindow.show()

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

class SystemControl:

    def __init__(self):
        pass

    def copyFile(self, copyPath, pastePath):
        os.system(f'copy {copyPath} {pastePath}')

        return self

    def copyFiles(self, copyFilePath: list, pastePath):
        for _ in range(len(copyFilePath)):
            os.system(f'copy {copyFilePath[_]} {pastePath}')

        return self

    @staticmethod
    def getFilePath(fileName):
        # 获取打包后的可执行文件所在的临时目录
        basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 构建文件的绝对路径
        return os.path.join(basePath, fileName)

    @staticmethod
    # 获取系统音量
    def getAudioEndpointVolume():
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            return volume
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return None

    # 取消静音
    def clearMute(self):
        volume = self.getAudioEndpointVolume()
        if volume is None:
            print("无法获取音频设备")
            return

        try:
            if volume.GetMute():
                volume.SetMute(0, None)
                print("系统已解除静音")
            else:
                print("系统未处于静音状态")
        except comtypes.COMError as e:
            print(f"COMError: {e}")

    # 设置音量
    def setAudio(self, num: float):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        # 设置音量（0.0到1.0之间的浮点数）
        volume_interface.SetMasterVolumeLevelScalar(num, None)

        return self

class KeyboardControl:

    def __init__(self):
        pass

    def keyUp(self, key):
        pyautogui.keyUp(key)

        return self

    def keyDown(self, key):
        pyautogui.keyDown(key)

        return self

    def keyPress(self, key: str):
        # 依次点击
        result = key.replace(' ', '').split(',')
        for i in range(len(result)):
            pyautogui.press(result[i])

        return self

    def keyHotkey(self, key: str):
        # 共同点击
        pyautogui.hotkey(tuple(key.replace(' ', '').split(',')))

        return self

def main():
    app = QApplication(sys.argv)
    window = MainWindow(
        650,
        350,
        SystemControl.getFilePath('./icon.png'),
        SystemControl.getFilePath('ATRI.png')
    )
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()




