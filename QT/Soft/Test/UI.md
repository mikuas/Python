## 左侧菜单栏
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton, QVBoxLayout, QWidget, QButtonGroup
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("左侧菜单栏示例")
        self.setGeometry(300, 300, 150, 400)

        # 创建主窗口部件和布局
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # 设置按钮样式的公用样式表
        button_style = """
            QToolButton {
                border: none;
                background-color: transparent;
                color: #6F6F6F;
                font-size: 12px;
                border-radius: 10px;  /* 圆角 */
                padding-top: 5px;
                padding-bottom: 5px;
            }
            QToolButton:hover {
                background-color: #E0E0E0;  /* 悬停时的背景色 */
                color: teal;  /* 悬停时的文字颜色 */
            }
            QToolButton:checked {
                border-left: solid #2880f1 3px;
                background-color: #B0E0E6;  /* 选中时的背景色 */
                color: green;
            }
        """

        # 创建按钮组来管理按钮的互斥性
        button_group = QButtonGroup(self)
        button_group.setExclusive(True)  # 设置为互斥，即只能选中一个

        # 创建第一个按钮 (主页)
        home_button = QToolButton()
        home_button.setText("主页")
        home_button.setIcon(QIcon("function-icon.png"))  # 替换为你的主页图标路径
        home_button.setIconSize(QSize(32, 32))
        home_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        home_button.setFixedSize(80, 80)
        home_button.setCheckable(True)  # 按钮可选中
        home_button.setStyleSheet(button_style)
        button_group.addButton(home_button)  # 将按钮添加到按钮组

        # 创建第二个按钮 (扩展)
        extension_button = QToolButton()
        extension_button.setText("扩展")
        extension_button.setIcon(QIcon("function-icon.png"))  # 替换为你的扩展图标路径
        extension_button.setIconSize(QSize(32, 32))
        extension_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        extension_button.setFixedSize(80, 80)
        extension_button.setCheckable(True)
        extension_button.setStyleSheet(button_style)
        button_group.addButton(extension_button)

        # 创建其他按钮...
        settings_button = QToolButton()
        settings_button.setText("设置")
        settings_button.setIcon(QIcon("function-icon.png"))  # 替换为你的设置图标路径
        settings_button.setIconSize(QSize(32, 32))
        settings_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        settings_button.setFixedSize(80, 80)
        settings_button.setCheckable(True)
        settings_button.setStyleSheet(button_style)
        button_group.addButton(settings_button)
        
        # 帮助按钮
        help_button = QToolButton()
        help_button.setText("帮助")
        help_button.setIcon(QIcon("function-icon.png"))  # 替换为你的帮助图标路径
        help_button.setIconSize(QSize(32, 32))
        help_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        help_button.setFixedSize(80, 80)
        help_button.setCheckable(True)
        help_button.setStyleSheet(button_style)
        button_group.addButton(help_button)

        # 将按钮添加到布局
        main_layout.addWidget(home_button)
        main_layout.addWidget(extension_button)
        main_layout.addWidget(settings_button)
        main_layout.addWidget(help_button)

        # 设置布局对齐
        main_layout.setAlignment(Qt.AlignTop)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

```
## 带图标的菜单栏
```python
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

```




