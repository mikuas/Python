from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PySide6.QtGui import QAction

class g(QWidget):
    def __init__(self):
        super().__init__()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("菜单栏示例")
        self.setGeometry(100, 100, 600, 400)

        # 创建菜单栏
        menu_bar = self.menuBar()

        # 创建菜单
        file_menu = menu_bar.addMenu("文件")
        edit_menu = menu_bar.addMenu("编辑")

        # 创建菜单项
        open_action = QAction("打开", self)
        save_action = QAction("保存", self)
        exit_action = QAction("退出", self)

        # 添加到菜单
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # 创建编辑菜单项
        copy_action = QAction("复制", self)
        paste_action = QAction("粘贴", self)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # 连接信号到槽
        open_action.triggered.connect(self.open_file)
        exit_action.triggered.connect(self.close)

    def open_file(self):
        QMessageBox.information(self, "打开文件", "你点击了“打开”菜单项！")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
