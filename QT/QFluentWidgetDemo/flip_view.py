import sys

from PySide6.QtCore import Qt, QSize, QRect, QModelIndex
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QStyleOptionViewItem,QWidget, QApplication
from qfluentwidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        '''翻转视图'''
        self.fpv = HorizontalFlipView(self)

        # 添加图片
        self.fpv.addImages([
            r"C:\Users\Administrator\OneDrive\Pictures\14.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\15.jpg"
        ])

        # 页码改变信号
        self.fpv.currentIndexChanged.connect(lambda index: print(index))

        # 设置缩放来保持图片的宽高比
        self.fpv.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

        # 调整默认视图大小
        self.fpv.setItemSize(QSize(self.width(), self.height()))
        self.fpv.setFixedSize(QSize(self.width(), self.height()))

        # 间距
        self.fpv.setSpacing(15)
        # 启用圆角
        self.fpv.setBorderRadius(15)
        # 使用自定义代理
        self.fpv.setItemDelegate(CustomFlipItemDelegate(self.fpv))

    def resizeEvent(self, event):
        self.fpv.setItemSize(QSize(self.width(), self.height()))
        self.fpv.setFixedSize(QSize(self.width(), self.height()))

# 控制绘制结果
class CustomFlipItemDelegate(FlipImageDelegate):
    """ Custom flip item delegate """

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        super().paint(painter, option, index)
        painter.save()

        # 绘制蒙版
        painter.setBrush(QColor(255, 255, 255, 200))
        painter.setPen(Qt.NoPen)
        rect = option.rect
        rect = QRect(rect.x(), rect.y(), 200, rect.height())
        painter.drawRect(rect)

        # 绘制文本
        painter.setPen(Qt.black)
        painter.setFont(getFont(16, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, '🥰\n硝子酱一级棒卡哇伊')

        painter.restore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
