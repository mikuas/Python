from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("选择特定类型的文件")

        layout = QVBoxLayout(self)

        self.button = QPushButton("选择文件", self)
        layout.addWidget(self.button)

        # 连接按钮点击事件
        self.button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        # 使用过滤器指定文件类型
        file, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Python 文件 (*.py);;文本文件 (*.txt);;所有文件 (*.*)")

        if file:
            print(f"选择的文件路径: {file}")
        else:
            print("没有选择文件")

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
