import sys

from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import Qt
from .RegeditAddLeftClickWindow import RegeditAddLeftWindow
from .RegeditAddBootWindow import RegeditAddBootWindow
from .SetMaxUpdateDays import SetMaxUpdateDays
# from QT.Soft.regedit.RegeditAddLeftClickWindow import RegeditAddLeftWindow
# from QT.Soft.regedit.RegeditAddBootWindow import RegeditAddBootWindow
# from QT.Soft.regedit.SetMaxUpdateDays import SetMaxUpdateDays

class RegeditMainWindow:
    def __init__(self):
        self.regeditAddLeftClickWindow = RegeditAddLeftWindow()
        self.regeditAddBootWindow = RegeditAddBootWindow()
        self.setWindowsDayWindow = SetMaxUpdateDays()
        self.window = QWidget()
        self.window.setWindowTitle('注册表操作')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.createButton()

        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """
        )

    def createButton(self):
        layout = QVBoxLayout(self.window)
        BtName = ['添加鼠标右键点机选项', '添加开机自启动', '设置Windows暂停更新天数']
        BtClick = [
            lambda: self.openWindow(self.regeditAddLeftClickWindow),
            lambda: self.openWindow(self.regeditAddBootWindow),
            lambda: self.openWindow(self.setWindowsDayWindow),
        ]

        for name, function in zip(BtName, BtClick):
            button = QPushButton(name, self.window)
            button.setStyleSheet("font-size: 18px")
            button.setFixedSize(250, 50)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(function)
            layout.addStretch()
            layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addStretch()

    @staticmethod
    def ignoreCloseEvent(event, windows):
        event.ignore()
        windows.hide()

    @staticmethod
    def openWindow(parent):
        parent.show()
        parent.raise_()
        parent.activateWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegeditMainWindow()
    window.window.show()
    sys.exit(app.exec())
