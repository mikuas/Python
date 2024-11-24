from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QTimer

class HoverMenuBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("悬停显示菜单栏示例")
        self.setGeometry(100, 100, 400, 300)

        # 创建菜单栏
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # 添加菜单
        file_menu = self.create_menu("文件")
        edit_menu = self.create_menu("编辑")
        help_menu = self.create_menu("帮助")

        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(edit_menu)
        menu_bar.addMenu(help_menu)

        # 启用悬停显示
        self.enable_hover_show(menu_bar)

    def create_menu(self, title):
        """创建带有简单动作的菜单"""
        menu = QMenu(title, self)
        menu.addAction(QAction(f"{title} 选项 1", self))
        menu.addAction(QAction(f"{title} 选项 2", self))
        menu.addAction(QAction(f"{title} 选项 3", self))
        return menu

    def enable_hover_show(self, menu_bar):
        """启用菜单悬停显示"""
        for action in menu_bar.actions():
            menu = action.menu()
            if menu:  # 如果 action 有对应的菜单
                menu.aboutToShow.connect(self._show_menu_on_hover(menu))

    def _show_menu_on_hover(self, menu):
        """返回一个用于显示菜单的槽函数"""
        def show_menu():
            # 如果鼠标悬停在菜单上，则打开
            if menu.isActiveWindow():
                QTimer.singleShot(100, menu.exec)
        return show_menu

if __name__ == "__main__":
    app = QApplication([])
    window = HoverMenuBarDemo()
    window.show()
    app.exec()
