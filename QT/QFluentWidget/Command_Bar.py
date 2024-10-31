import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout,QWidget, QApplication
from qfluentwidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        comBar = CommandBar()

        # 逐个添加动作
        comBar.addAction(Action(FluentIcon.ADD, '添加', triggered=lambda: print("添加")))

        # 添加分隔符
        comBar.addSeparator()

        # 批量添加动作
        comBar.addActions([
            Action(FluentIcon.EDIT, '编辑', checkable=True, triggered=lambda: print("编辑")),
            Action(FluentIcon.COPY, '复制'),
            Action(FluentIcon.SHARE, '分享'),
        ])

        # 添加始终隐藏的动作
        comBar.addHiddenAction(Action(FluentIcon.SCROLL, '排序', triggered=lambda: print('排序')))
        comBar.addHiddenAction(Action(FluentIcon.SETTING, '设置', shortcut='Ctrl+S'))

        # 添加自定义组件
        # 创建透明下拉菜单按钮
        button = TransparentDropDownPushButton(FluentIcon.MENU, 'Menu')
        button.setFixedHeight(34)
        setFont(button, 12)

        menu = RoundMenu(parent=self)
        menu.addActions([
            Action(FluentIcon.COPY, 'Copy'),
            Action(FluentIcon.CUT, 'Cut'),
            Action(FluentIcon.PASTE, 'Paste'),
            Action(FluentIcon.CANCEL, 'Cancel'),
            Action('Select all'),
        ])
        button.setMenu(menu)

        # 添加自定义组件
        comBar.addWidget(button)

        # 默认只显示图标
        # 图标右侧文本
        comBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        # 图标底部显示文本
        comBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        commandBar = CommandBarView()

        commandBar.addAction(Action(FluentIcon.SHARE, 'Share'))
        commandBar.addAction(Action(FluentIcon.SAVE, 'Save'))
        commandBar.addAction(Action(FluentIcon.DELETE, 'Delete'))

        commandBar.addHiddenAction(Action(FluentIcon.APPLICATION, 'App', shortcut='Ctrl+A'))
        commandBar.addHiddenAction(Action(FluentIcon.SETTING, 'Settings', shortcut='Ctrl+S'))
        commandBar.resizeToSuitableWidth()

        target = PushButton("Click Me")
        Flyout.make(commandBar, target=target, parent=target, aniType=FlyoutAnimationType.FADE_IN)

        layout.addWidget(comBar)
        layout.addWidget(commandBar)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
