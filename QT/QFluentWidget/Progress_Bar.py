import sys

from PySide6.QtCore import Qt, QEasingCurve
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication, QVBoxLayout
from qfluentwidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 350)
        '''进度条'''
        # 对比QProgressBar取消了文本显示功能
        hLayout = QHBoxLayout(self)
        layout = QVBoxLayout()
        hLayout.addLayout(layout)
        pb = ProgressBar(self)
        pb.setFixedSize(200, 50)

        # 设置取值范围
        pb.setRange(0, 100)
        # 设置当前值
        pb.setValue(0)
        # 设置暂停和错误状态
        pb.pause()
        pb.error()
        # 恢复运行状态
        pb.resume()
        # 自定义颜色进度条
        pb.setCustomBarColor(QColor(255, 0, 0), QColor(0, 255, 110))

        layout.addWidget(pb)
        ipb = IndeterminateProgressBar()
        layout.addWidget(ipb)
        # 表示一个正在进行但其完成时间未知的长时间运行任务

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
