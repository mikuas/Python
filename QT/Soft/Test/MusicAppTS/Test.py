import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("带图标的菜单栏示例")
        self.setGeometry(300, 300, 600, 400)

        # 创建菜单栏
        menubar = self.menuBar()

        # 文件菜单
        file_menu = menubar.addMenu("文件")

        # 打开动作
        open_action = QAction(QIcon("function-icon.png"), "打开", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)

        # 保存动作
        save_action = QAction(QIcon("function-icon.png"), "保存", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)

        # 退出动作
        exit_action = QAction(QIcon("function-icon.png"), "退出", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        # 将动作添加到文件菜单
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()  # 添加分隔线
        file_menu.addAction(exit_action)

        # 帮助菜单
        help_menu = menubar.addMenu("帮助")

        # 帮助动作
        about_action = QAction(QIcon("help_icon.png"), "关于", self)
        about_action.triggered.connect(self.about)

        help_menu.addAction(about_action)

    def open_file(self):
        print("打开文件")

    def save_file(self):
        print("保存文件")

    def about(self):
        print("关于本软件")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())