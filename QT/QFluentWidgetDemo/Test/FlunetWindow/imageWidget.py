from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtGui import Qt
from PySide6.QtCore import QSize

from qfluentwidgets import HorizontalFlipView


class ImageWidget(QWidget):
    def __init__(self, text, imagePath: list, parent=None):
        super().__init__(parent)
        self.hLayout = QHBoxLayout(self)
        self.setObjectName(text.replace(" ", "_"))

        '''翻转视图'''
        self.fpv = HorizontalFlipView(self)

        # 添加图片
        self.fpv.addImages(imagePath)

        # 页码改变信号
        self.fpv.currentIndexChanged.connect(lambda index: print(index))

        # 设置缩放来保持图片的宽高比
        self.fpv.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        # 调整默认视图大小
        self.fpv.setItemSize(QSize(self.width(), self.height()))
        self.fpv.setFixedSize(QSize(self.width(), self.height()))

        # 间距
        self.fpv.setSpacing(15)
        # 启用圆角
        self.fpv.setBorderRadius(15)

        # self.hLayout.addWidget(self.fpv)

    def resizeEvent(self, event):
        self.fpv.setItemSize(QSize(self.width(), self.height()))
        self.fpv.setFixedSize(QSize(self.width(), self.height()))
