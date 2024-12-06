from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QPushButton, QWidget
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在 QListWidget 中添加 QWidget")
        self.setGeometry(100, 100, 300, 400)

        # 创建 QListWidget
        list_widget = QListWidget(self)
        list_widget.setGeometry(10, 10, 280, 380)

        # 添加自定义项
        self.add_item(list_widget, "歌曲1", "path_to_icon.png")
        self.add_item(list_widget, "歌曲2", "path_to_icon.png")
        self.add_item(list_widget, "歌曲3", "path_to_icon.png")

        self.setCentralWidget(list_widget)

    def add_item(self, list_widget, title, icon_path):
        # 创建一个自定义 QWidget 作为每个列表项的内容
        item_widget = QWidget()

        # 创建布局管理器
        layout = QHBoxLayout()

        # 创建图标标签
        icon_label = QLabel()
        icon_label.setPixmap(QIcon(icon_path).pixmap(50, 50))  # 设置图标的大小

        # 创建文本标签
        text_label = QLabel(title)

        # 创建按钮
        download_button = QPushButton("下载")

        # 将控件加入布局
        layout.addWidget(icon_label)
        layout.addWidget(text_label)
        layout.addWidget(download_button)

        # 设置 QWidget 布局
        item_widget.setLayout(layout)

        # 创建 QListWidgetItem，并将自定义的 QWidget 设置为该项的内容
        item = QListWidgetItem()
        list_widget.addItem(item)
        list_widget.setItemWidget(item, item_widget)

# 程序入口
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
