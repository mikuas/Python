import sys

from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import Qt
from .ImageReNameWindow import ImageRenameWindow
# from QT.Soft.Image.ImageReNameWindow import ImageRenameWindow

class ImageMainWindow:
    def __init__(self, width, height):
        self.imageReNameWindow = ImageRenameWindow(width, height)
        self.window = QWidget()
        self.window.setWindowTitle('重命名')
        self.window.closeEvent = lambda event: self.ignoreCloseEvent(event, self.window)
        self.window.setFixedSize(400, 600)
        self.window.setStyleSheet(
            """
                QPushButton:hover {
                    background-color: #00BFFF;
                }
            """
        )

        self.createButton()

    def createButton(self):
        layout = QVBoxLayout(self.window)
        BtName = ['图片重命名']
        BtClick = [lambda: self.openWindow(self.imageReNameWindow)]

        for bt, fc in zip(BtName, BtClick):
            button = QPushButton(bt, self.window)
            button.setStyleSheet('font-size: 18px;')
            button.setFixedSize(250, 50)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(fc)

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
    window = ImageMainWindow(640, 480).window
    window.show()
    app.exec()
