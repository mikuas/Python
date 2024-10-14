from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import Qt


class SubWindow:
    def __init__(self, keyboardWindow, imageWindow, regeditWindow, calcWindow):
        self.window = QWidget()
        self.window.setWindowTitle('Methods')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.createButton(keyboardWindow, imageWindow, regeditWindow, calcWindow)

        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """
        )

    def createButton(self, keyboardWindow, imageWindow, regeditWindow, calcWindow):
        layout = QVBoxLayout(self.window)
        BtName = ['键盘操作', '重命名', '添加注册表值', '简易计算器']
        BtClick = [
            lambda: self.openWindow(keyboardWindow),
            lambda: self.openWindow(imageWindow),
            lambda: self.openWindow(regeditWindow),
            lambda: self.openWindow(calcWindow)
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
    def ignoreCloseEvent(event, window):
        event.ignore()
        window.hide()

    @staticmethod
    def openWindow(parent):
        parent.show()
        parent.raise_()
        parent.activateWindow()