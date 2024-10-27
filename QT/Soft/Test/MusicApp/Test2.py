import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("进度条暂停示例")
        self.setGeometry(300, 300, 300, 150)
        self.value = 0
        self.timer = QTimer(self)

        # 创建进度条
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        # 创建按钮
        self.start_button = QPushButton("开始")
        self.start_button.clicked.connect(self.start)
        self.pause_button = QPushButton("暂停")
        self.pause_button.clicked.connect(self.timer.stop)
        self.resume_button = QPushButton("继续")
        self.resume_button.clicked.connect(lambda: self.timer.start(100))

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.resume_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start(self):
        self.value = 0
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(self.value)
        self.timer.timeout.connect(lambda: (self.updateValue(),self.progress_bar.setValue(self.value)))
        self.timer.start(100)

    def updateValue(self):
        self.value += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())