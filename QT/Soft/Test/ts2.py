import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图标+文字按钮示例")
        self.setGeometry(300, 300, 300, 300)

        # 创建主窗口部件和布局
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # 创建 QToolButton 并设置图标和文本
        button = QToolButton()
        button.setText("主页")
        button.setIcon(QIcon("function-icon.png"))  # 替换为你的图标路径
        button.setIconSize(QSize(64, 64))  # 设置图标大小
        # 设置按钮透明
        button.setStyleSheet("""
                    QToolButton {
                        border: none;  /* 移除边框 */
                        background: transparent;  /* 背景透明 */
                    }
                    QToolButton:hover {
                        color: teal;  /* 悬停时的文字颜色 */
                    }
                """)

        # 设置按钮文本和图标布局：图标在上，文字在下
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # 设置按钮大小
        button.setFixedSize(100, 100)

        # 添加按钮到布局
        main_layout.addWidget(button)
        main_layout.setAlignment(Qt.AlignTop)

        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
