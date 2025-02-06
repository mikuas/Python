# coding:utf-8
from PySide6.QtCore import QPropertyAnimation, QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class ScaleAnimationExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("缩放动画示例")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("点击缩放", self)
        self.button.clicked.connect(self.animate_scale)
        self.button.setGeometry(100, 100, 100, 50)

    def animate_scale(self):
        # 创建缩放动画
        animation_scale = QPropertyAnimation(self.button, b"size")
        animation_scale.setDuration(1000)  # 动画时长1秒
        animation_scale.setStartValue(self.button.size())  # 初始大小
        animation_scale.setEndValue(QSize(200, 100))  # 目标大小：宽200，高100
        animation_scale.start()

    def setSize(self, size):
        # 设置控件的大小
        self.button.resize(size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScaleAnimationExample()
    window.show()
    sys.exit(app.exec())
