from PySide6.QtWidgets import QPushButton, QMessageBox, QVBoxLayout, QWidget
from PySide6.QtGui import Qt


class SubWindow:
    def __init__(self, keyboardWindow, imageWindow, regeditWindow, calcWindow):
        self.window = QWidget()
        self.window.setWindowTitle('Methods')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.keyboardWindowButton = QPushButton('键盘操作', self.window)
        self.keyboardWindowButton.setStyleSheet("font-size: 18px")
        self.keyboardWindowButton.setFixedSize(250, 50)
        self.keyboardWindowButton.setCursor(Qt.PointingHandCursor)
        self.keyboardWindowButton.clicked.connect(lambda: self.openWindow(keyboardWindow))

        self.imageWindowButton = QPushButton('重命名', self.window)
        self.imageWindowButton.setStyleSheet("font-size: 18px")
        self.imageWindowButton.setFixedSize(250, 50)
        self.imageWindowButton.setCursor(Qt.PointingHandCursor)
        self.imageWindowButton.clicked.connect(lambda: self.openWindow(imageWindow))

        self.regeditWindowButton = QPushButton('添加注册表值', self.window)
        self.regeditWindowButton.setStyleSheet("font-size: 18px")
        self.regeditWindowButton.setFixedSize(250, 50)
        self.regeditWindowButton.setCursor(Qt.PointingHandCursor)
        self.regeditWindowButton.clicked.connect(lambda: self.openWindow(regeditWindow))

        self.calcWindowButton = QPushButton('简易计算器', self.window)
        self.calcWindowButton.setStyleSheet("font-size: 18px")
        self.calcWindowButton.setFixedSize(250, 50)
        self.calcWindowButton.setCursor(Qt.PointingHandCursor)
        self.calcWindowButton.clicked.connect(lambda: self.openWindow(calcWindow))

        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """
        )

        layout = QVBoxLayout(self.window)
        layout.addStretch()
        layout.addWidget(self.keyboardWindowButton, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.imageWindowButton, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.regeditWindowButton, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.calcWindowButton, alignment=Qt.AlignCenter)
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