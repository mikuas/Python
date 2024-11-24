from PySide6.QtWidgets import QApplication, QWidget, QMenuBar, QVBoxLayout, QMessageBox, QMenu
from PySide6.QtGui import QAction, QColor
from numpy.ma.core import arccos
from pyautogui import shortcut
from qfluentwidgets import RoundMenu, Action, FluentIcon, PushButton, setTheme, Theme, Icon

from QFluentWidgets.FluentWidgetModule.FluentWidgets import MenuBar, Menu


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget 顶部菜单栏示例")
        self.setGeometry(100, 100, 400, 300)
        # 创建布局
        layout = QVBoxLayout(self)
        # 创建菜单栏
        self.menuBar = MenuBar(self)
        self.menuBar.addAction(
            Action(FluentIcon.COPY, "File", self)
        )
        layout.setMenuBar(self.menuBar)
        RoundMenu()
        m1 = Menu(self)
        action = self.menuBar.addItem(
            "文件",
            # FluentIcon.MENU,
            self
        )
        action.setMenu(m1)
        m1.addActions([
            QAction(Icon(FluentIcon.COPY), "Copy", self, shortcut="Ctrl+c"),
            QAction(Icon(FluentIcon.COPY), "Copy", self),
            QAction(Icon(FluentIcon.COPY), "Copy", self),
        ])
        self.menuBar.setMinimumWidth(160)

        m1.setStyleSheet("""
            QMenu::item {
                min-height: 20px;          /* 设置 QAction 高度 */
                padding: 5px 10px;        /* 设置内边距 */
                background-color: white;  /* 背景色 */
                border-radius: 5px 5px;
                box-shadow: none;
            }
            QMenu::item:selected {       /* 鼠标悬停样式 */
                background-color: #f0f0f0;
                box-shadow: none;
            }
        """)
        m1.setMinimumWidth(100)


if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    setTheme(Theme.AUTO)
    widget.show()
    app.exec()
