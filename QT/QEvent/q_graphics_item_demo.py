from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtCore import QRectF, Qt


class CustomRectItem(QGraphicsItem):
    def __init__(self):
        super().__init__()

    def boundingRect(self):
        # 返回矩形的边界
        return QRectF(-50, -50, 100, 100)

    def paint(self, painter, option, widget=None):
        # 使用 QPainter 绘制矩形
        painter.setBrush(QBrush(QColor(255, 0, 0)))  # 红色填充
        painter.drawRect(-50, -50, 100, 100)  # 绘制一个矩形


class CustomEllipseItem(QGraphicsItem):
    def __init__(self):
        super().__init__()

    def boundingRect(self):
        # 返回椭圆的边界
        return QRectF(-50, -25, 100, 50)

    def paint(self, painter, option, widget=None):
        # 使用 QPainter 绘制椭圆
        painter.setBrush(QBrush(QColor(0, 0, 255)))  # 蓝色填充
        painter.drawEllipse(-50, -25, 100, 50)  # 绘制一个椭圆


class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        # 创建 QGraphicsScene
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(-200, -200, 400, 400)

        # 添加自定义图形项
        rect_item = CustomRectItem()
        rect_item.setPos(-100, 0)  # 设置位置
        self.scene.addItem(rect_item)

        ellipse_item = CustomEllipseItem()
        ellipse_item.setPos(100, 0)  # 设置位置
        self.scene.addItem(ellipse_item)

        # 设置视图显示场景
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)  # 启用抗锯齿

        self.setWindowTitle("QGraphicsItem 示例")
        self.setGeometry(100, 100, 600, 400)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
