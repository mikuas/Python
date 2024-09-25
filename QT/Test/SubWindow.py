from PySide6.QtWidgets import QPushButton, QMessageBox, QVBoxLayout, QWidget
from PySide6.QtGui import Qt


class SubWindow:
    def __init__(
            self,
            parent,
            style,
            keyboardTaskWindow,
            keyboardHotTaskWindow,
            imageReNameWindow
    ):
        self.window = QWidget()
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.keyboardButton = QPushButton('依次点击键盘任务', self.window)
        self.keyboardButton.setStyleSheet(style[2])
        self.keyboardButton.setFixedSize(250, 50)
        self.keyboardButton.clicked.connect(lambda: keyboardTaskWindow.show())

        self.keyboardHotButton = QPushButton('组合键任务', self.window)
        self.keyboardHotButton.setStyleSheet(style[2])
        self.keyboardHotButton.setFixedSize(250, 50)
        self.keyboardHotButton.clicked.connect(lambda: keyboardHotTaskWindow.show())

        self.imageRenameButton = QPushButton('图片重命名', self.window)
        self.imageRenameButton.setStyleSheet(style[2])
        self.imageRenameButton.setFixedSize(250, 50)
        self.imageRenameButton.clicked.connect(lambda: (
        QMessageBox.information(self.window, '提示', '从0开始,依次命名,当前仅支持jpg,png'), imageReNameWindow.show()))

        layout = QVBoxLayout(self.window)
        layout.addWidget(self.keyboardButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(self.keyboardHotButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(self.imageRenameButton, alignment=Qt.AlignCenter)
        layout.addStretch(1)

    @staticmethod
    def ignoreCloseEvent(event, window):
        event.ignore()
        window.hide()

    def show(self):
        self.window.show()