from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt

from qfluentwidgets import FluentWindow, PushButton, TransparentToolButton, PrimaryPushButton
from qfluentwidgets.components.material import AcrylicWidget
from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush, AcrylicLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Acrylic Widget Example")
        self.resize(1200, 800)

        self.acrylicLabel = AcrylicLabel(16, QColor(105, 114, 168, 50), parent=self)
        self.acrylicLabel.setImage(r"C:\Users\Administrator\OneDrive\Pictures\0.jpg")
        self.acrylicLabel.show()

        button = PrimaryPushButton(self)
        button.setText("Hello")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.acrylicLabel.setFixedSize(self.width(), self.height())

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
