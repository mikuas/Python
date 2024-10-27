import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("侧边栏示例")
        self.setGeometry(100, 100, 300, 500)

        # 创建主窗口部件
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # 左侧的侧边栏
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar.setFixedWidth(80)  # 设置固定宽度
        sidebar.setStyleSheet("background-color: lightgray;")  # 背景颜色

        # 添加按钮
        home_button = QPushButton("主页")
        expand_button = QPushButton("扩展")
        settings_button = QPushButton("设置")
        help_button = QPushButton("帮助")

        # 设置按钮的样式
        home_button.setStyleSheet("background-color: white; color: teal;")
        expand_button.setStyleSheet("background-color: white;")
        settings_button.setStyleSheet("background-color: white;")
        help_button.setStyleSheet("background-color: white;")

        # 添加按钮到侧边栏布局
        sidebar_layout.addWidget(home_button)
        sidebar_layout.addWidget(expand_button)
        sidebar_layout.addWidget(settings_button)
        sidebar_layout.addWidget(help_button)
        sidebar_layout.addStretch()  # 留出空间

        # 主内容区（右侧）
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # 添加控件到主内容区
        content_layout.addWidget(QPushButton("这里是主内容"))

        # 添加侧边栏和主内容到主布局
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_widget)

        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
