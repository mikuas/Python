from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget(self)

        # 添加标签页
        for i in range(4):
            tab_content = QWidget()
            layout = QVBoxLayout(tab_content)
            layout.addWidget(QLabel(f"这是选项卡 {i + 1} 的内容"))
            self.tab_widget.addTab(tab_content, f"新文件{i + 1}")

        # 连接信号
        self.tab_widget.currentChanged.connect(self.update_tab_style)

        # 设置默认样式
        self.update_tab_style(self.tab_widget.currentIndex())

        # 创建按钮（可选）
        self.button = QPushButton("打印当前选项卡索引", self)
        self.button.clicked.connect(self.print_current_tab_index)

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_tab_style(self, index):
        # 设置所有标签页的默认样式
        for i in range(self.tab_widget.count()):
            self.tab_widget.tabBar().setTabTextColor(i, "black")  # 设置文本颜色
            self.tab_widget.tabBar().setStyleSheet("")  # 清除所有样式

        # 为选中的标签页设置样式
        self.tab_widget.tabBar().setTabTextColor(index, "white")  # 设置选中标签文本颜色
        self.tab_widget.tabBar().setStyleSheet(f"QTabBar::tab:selected {{ background-color: blue; }}")  # 设置选中标签背景颜色

    def print_current_tab_index(self):
        print(f"当前选中的标签页索引: {self.tab_widget.currentIndex()}")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
