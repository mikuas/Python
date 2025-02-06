from PySide6.QtCore import QPropertyAnimation, Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout
import sys

class SideNavBarExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("侧边导航栏示例")
        self.setGeometry(100, 100, 400, 300)

        # 创建主布局
        self.layout = QHBoxLayout(self)

        # 创建侧边导航栏（最初宽度为0）
        self.sidebar = QFrame(self)
        self.sidebar.setStyleSheet("background-color: #2d2d2d;")

        # 创建侧边导航栏内容
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(QLabel("导航项 1", self))
        sidebar_layout.addWidget(QLabel("导航项 2", self))
        sidebar_layout.addWidget(QLabel("导航项 3", self))
        self.sidebar.setLayout(sidebar_layout)

        # 创建内容区域
        self.content = QLabel("内容区域", self)

        # 创建展开/收起按钮
        self.toggle_button = QPushButton("展开侧边栏", self)
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # 将控件添加到主布局
        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.content)
        self.layout.addWidget(self.toggle_button)

        # 定义动画
        self.animation = QPropertyAnimation(self.sidebar, b"maximumWidth")
        self.animation.setDuration(300)  # 动画持续时间300毫秒

        # 状态变量，用于跟踪侧边导航栏是否展开
        self.is_sidebar_expanded = False

    def toggle_sidebar(self):
        # 切换侧边导航栏展开或收起的状态
        if self.is_sidebar_expanded:
            # 设置收起的动画
            self.animation.setStartValue(self.sidebar.width())
            self.animation.setEndValue(0)
            self.toggle_button.setText("展开侧边栏")
        else:
            # 设置展开的动画
            self.animation.setStartValue(self.sidebar.width())
            self.animation.setEndValue(150)  # 展开到150px宽度
            self.toggle_button.setText("收起侧边栏")

        # 启动动画
        self.animation.start()

        # 更新状态
        self.is_sidebar_expanded = not self.is_sidebar_expanded

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SideNavBarExample()
    window.show()
    sys.exit(app.exec())
