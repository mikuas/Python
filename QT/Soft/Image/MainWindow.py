from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import Qt
from .ImageReNameWindow import ImageRenameWindow

class ImageMainWindow:
    def __init__(self, width, height):
        self.imageReNameWindow = ImageRenameWindow(width, height)
        self.window = QWidget()
        self.window.setWindowTitle('重命名')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)

        self.imageReNameButton = QPushButton('图片重命名', self.window)
        self.imageReNameButton.setStyleSheet("font-size: 18px")
        self.imageReNameButton.setFixedSize(250, 50)
        self.imageReNameButton.setCursor(Qt.PointingHandCursor)
        self.imageReNameButton.clicked.connect(lambda: self.openWindow(self.imageReNameWindow))

        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """
        )

        layout = QVBoxLayout(self.window)
        layout.addStretch()
        layout.addWidget(self.imageReNameButton, alignment=Qt.AlignCenter)
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

