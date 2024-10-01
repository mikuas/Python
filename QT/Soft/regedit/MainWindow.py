from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import Qt
from QT.Soft.regedit.RegeditAddLeftClickWindow import RegeditAddLeftWindow
from QT.Soft.regedit.RegeditAddBootWindow import RegeditAddBootWindow

class RegeditMainWindow:
    def __init__(self):
        self.regeditAddLeftClickWindow = RegeditAddLeftWindow()
        self.regeditAddBootWindow = RegeditAddBootWindow()
        self.window = QWidget()
        self.window.setWindowTitle('注册表操作')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.rLeftButton = QPushButton('添加鼠标右键点机选项', self.window)
        self.rLeftButton.setStyleSheet("font-size: 24px")
        self.rLeftButton.setFixedSize(250, 50)
        self.rLeftButton.setCursor(Qt.PointingHandCursor)
        self.rLeftButton.clicked.connect(lambda: self.openWindow(self.regeditAddLeftClickWindow))

        self.rAddBootButton = QPushButton('添加开机自启动', self.window)
        self.rAddBootButton.setStyleSheet("font-size: 24px")
        self.rAddBootButton.setFixedSize(250, 50)
        self.rAddBootButton.setCursor(Qt.PointingHandCursor)
        self.rAddBootButton.clicked.connect(lambda: self.openWindow(self.regeditAddBootWindow))

        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: aqua;
                }
            """
        )

        layout = QVBoxLayout(self.window)
        layout.addStretch()
        layout.addWidget(self.rLeftButton, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.rAddBootButton, alignment=Qt.AlignCenter)
        layout.addStretch()

    @staticmethod
    def ignoreCloseEvent(event, window):
        event.ignore()
        window.hide()

    @staticmethod
    def openWindow(parent):
        parent.show()
        parent.raise_()
        parent.activateWindow()

