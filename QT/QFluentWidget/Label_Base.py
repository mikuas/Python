import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        '''标签'''
        label = BodyLabel("标签", self)
        # 浅 深 色主题
        label.setTextColor(QColor(0, 255, 0), QColor(255, 0, 0))

        # 链接标签
        label2 = HyperlinkLabel(QUrl('https://www.bilibili.com'), 'Bili', self)
        # 显示下划线
        label2.setUnderlineVisible(True)

        # 更换超链接
        label2.setUrl('https://www.bilibili.com')

        # 显示图片
        image = ImageLabel(r"C:\Users\Administrator\OneDrive\Pictures\12.jpg", self)
        # 按比例缩放到指定高度
        image.scaledToHeight(300)
        # 圆角
        image.setBorderRadius(8, 8, 8, 8)

        # 显示圆型头像 图片 GIF
        w = AvatarWidget(r"C:\Users\Administrator\OneDrive\Pictures\12.jpg", self)
        # 设置头像半径
        w.setRadius(64)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
