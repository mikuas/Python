# coding:utf-8
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class ColorAnimationExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("颜色动画示例")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("点击改变颜色", self)
        self.button.clicked.connect(self.animate_color)

    def animate_color(self):
        # 创建一个颜色动画来改变背景颜色
        animation_color = QPropertyAnimation(self, b"backgroundColor")
        animation_color.setDuration(1000)  # 动画时长1秒
        animation_color.setStartValue(QColor(255, 255, 255))  # 初始颜色：白色
        animation_color.setEndValue(QColor(0, 255, 0))  # 目标颜色：绿色
        animation_color.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorAnimationExample()
    window.show()
    sys.exit(app.exec())
