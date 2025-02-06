# coding:utf-8


"""
    拖拽事件
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtGui import QKeySequence, Qt



class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 启用拖放功能
        self.setAcceptDrops(True)

    """ 拖动进入事件 """
    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        # if event.mimeData().hasText(): # 是否包含文本数据
        #     print(f'文本: {event.mimeData().text()}')
        # if event.mimeData().urls():
        #     event.acceptProposedAction()
        #     print(event.mimeData().urls())
        event.acceptProposedAction()
    
    """ 拖动移动事件 """
    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)

    """ 拖动离开事件 """
    def dragLeaveEvent(self, event):
        super().dragLeaveEvent(event)
        
    """ 拖动放下事件 """
    def dropEvent(self, event):
        super().dropEvent(event)
        urls = event.mimeData().urls()
        if urls:
            for url in urls:
                print(f"LocalFile: {url.toLocalFile()}")
                print(f"ToString: {url.toString()}")
                print(f"URL: {url.url()}")
                print(f"FileName: {url.fileName()}")
                print(f"后缀名: {url.fileName().split('.')[-1]}")
        event.acceptProposedAction()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())