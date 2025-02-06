from PySide6.QtCore import QPropertyAnimation, QRectF, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsRectItem
import sys

class RotateAnimationExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("旋转动画示例")
        self.setGeometry(100, 100, 300, 200)

        # 创建视图和场景
        self.view = QGraphicsView(self)
        self.view.setGeometry(50, 50, 200, 150)

        # 创建场景
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        # 创建一个矩形
        self.rect_item = QGraphicsRectItem(QRectF(50, 50, 100, 50))
        self.rect_item.setBrush(Qt.blue)
        self.scene.addItem(self.rect_item)

        # 创建一个按钮来启动旋转动画
        self.button = QPushButton("点击旋转", self)
        self.button.setGeometry(100, 180, 100, 30)
        self.button.clicked.connect(self.animate_rotation)

    def animate_rotation(self):
        # 创建旋转动画
        animation_rotation = QPropertyAnimation(self.rect_item, b"rotation")
        animation_rotation.setDuration(2000)  # 动画时长2秒
        animation_rotation.setStartValue(0)   # 初始旋转角度为0
        animation_rotation.setEndValue(360)   # 目标旋转角度为360度
        animation_rotation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RotateAnimationExample()
    window.show()
    sys.exit(app.exec())
