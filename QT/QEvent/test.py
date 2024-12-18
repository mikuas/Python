from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpacerItem 示例")
        self.setGeometry(100, 100, 300, 200)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 添加按钮
        button1 = QPushButton("按钮 1")
        layout.addWidget(button1)

        # 创建一个 SpacerItem，设置为动态高度
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # 添加第二个按钮
        button2 = QPushButton("按钮 2")
        layout.addWidget(button2)

        # 设置布局
        self.setLayout(layout)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
