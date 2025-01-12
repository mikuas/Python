from PySide6.QtWidgets import QApplication, QPushButton, QWidget
from PySide6.QtCore import QPropertyAnimation, Property, Qt
from PySide6.QtGui import QPainter, QTransform


class RotatingButton(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Rotation", self)

        # 初始化旋转角度
        self._rotation = 0

        # 创建动画对象，绑定到 rotation 属性
        self.animation = QPropertyAnimation(self.button, b"rotation", self)
        self.animation.setDuration(2000)  # 动画持续时间（毫秒）
        self.animation.setStartValue(0)  # 起始角度
        self.animation.setEndValue(360)  # 结束角度
        self.animation.setLoopCount(-1)  # 无限循环

        # 点击按钮启动动画
        self.button.clicked.connect(self.animation.start)


if __name__ == "__main__":
    app = QApplication([])
    button = RotatingButton()
    button.show()
    app.exec()
