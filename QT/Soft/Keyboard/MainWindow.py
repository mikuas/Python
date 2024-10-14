import sys

from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import Qt

from .KeyboardTaskWindow import KeyboardTaskWindow
from .KeyboardHotTaskWindow import KeyboardHotTaskWindow
# from QT.Soft.Keyboard.KeyboardTaskWindow import KeyboardTaskWindow
# from QT.Soft.Keyboard.KeyboardHotTaskWindow import KeyboardHotTaskWindow

class KeyboardMainWindow:
    def __init__(self, width, height):
        self.keyboardTaskWindow = KeyboardTaskWindow(width, height)
        self.keyboardHotTaskWindow = KeyboardHotTaskWindow(width, height)
        self.window = QWidget()
        self.window.setWindowTitle('键盘任务')
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
        BtName = ['依次点击键盘任务', '组合键任务']
        BtClick = [
            lambda: self.openWindow(self.keyboardTaskWindow),
            lambda: self.openWindow(self.keyboardHotTaskWindow)
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
    window = KeyboardMainWindow(400, 600)
    window.window.show()
    app.exec()