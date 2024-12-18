from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGraphicsScene 示例")
        self.setGeometry(100, 100, 600, 400)

        # 创建 QGraphicsScene
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(-300, -200, 600, 400)  # 设置场景的可视区域

        # 创建矩形图形项
        rect_item = QGraphicsRectItem(-50, -50, 100, 100)  # 创建一个矩形
        rect_item.setBrush(QBrush(QColor(255, 0, 0)))  # 设置矩形填充颜色为红色
        self.scene.addItem(rect_item)  # 将矩形添加到场景中

        # 创建椭圆图形项
        ellipse_item = QGraphicsEllipseItem(-100, -100, 100, 50)  # 创建一个椭圆
        ellipse_item.setBrush(QBrush(QColor(0, 0, 255)))  # 设置椭圆填充颜色为蓝色
        self.scene.addItem(ellipse_item)  # 将椭圆添加到场景中

        # 创建 QGraphicsView 来显示 QGraphicsScene
        self.view = QGraphicsView(self.scene, self)

        # 设置渲染提示：开启抗锯齿
        self.view.setRenderHint(QPainter.Antialiasing)  # 开启抗锯齿
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)  # 平滑图片变换
        self.view.setRenderHint(QPainter.TextAntialiasing)  # 字体抗锯齿
        self.view.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # 设置视图对齐方式

        # 设置视图的大小和位置
        self.setCentralWidget(self.view)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
