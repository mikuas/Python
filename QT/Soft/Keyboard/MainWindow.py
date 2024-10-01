from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import Qt
from QT.Soft.Keyboard.KeyboardTaskWindow import KeyboardTaskWindow
from QT.Soft.Keyboard.KeyboardHotTaskWindow import KeyboardHotTaskWindow

class KeyboardMainWindow:
    def __init__(self, width, height):
        self.keyboardTaskWindow = KeyboardTaskWindow(width, height)
        self.keyboardHotTaskWindow = KeyboardHotTaskWindow(width, height)
        self.window = QWidget()
        self.window.setWindowTitle('键盘任务')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.keyboardButton = QPushButton('依次点击键盘任务', self.window)
        self.keyboardButton.setStyleSheet("font-size: 24px")
        self.keyboardButton.setFixedSize(250, 50)
        self.keyboardButton.setCursor(Qt.PointingHandCursor)
        self.keyboardButton.clicked.connect(lambda: self.openWindow(self.keyboardTaskWindow))

        self.keyboardHotButton = QPushButton('组合键任务', self.window)
        self.keyboardHotButton.setStyleSheet("font-size: 24px")
        self.keyboardHotButton.setFixedSize(250, 50)
        self.keyboardHotButton.setCursor(Qt.PointingHandCursor)
        self.keyboardHotButton.clicked.connect(lambda: self.openWindow(self.keyboardHotTaskWindow))

        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: aqua;
                }
            """
        )

        layout = QVBoxLayout(self.window)
        layout.addStretch()
        layout.addWidget(self.keyboardButton, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.keyboardHotButton, alignment=Qt.AlignCenter)
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

