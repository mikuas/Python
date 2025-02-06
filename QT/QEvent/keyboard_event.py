# coding:utf-8


"""
    键盘事件
"""
import sys
import keyboard

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton
from PySide6.QtGui import QKeySequence, Qt, QShortcut


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        """ 设置快捷键 """

        # self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut = QShortcut(Qt.Modifier.CTRL | Qt.Key.Key_Q, self)
        self.shortcut.activated.connect(lambda: print('快捷键: Ctrl + Q'))
        # 禁用快捷键
        self.shortcut.setEnabled(False)
        # 启用快捷键
        self.shortcut.setEnabled(True)

        # 全局捕获键盘事件, 在控件内有效
        self.grabKeyboard()

        # 监听全局快捷键, 后台生效
        keyId = keyboard.add_hotkey('ctrl+shift+h', lambda: print('快捷键: Ctrl + Shift + H'))
        # 解除监听全部
        # keyboard.unhook_all_hotkeys()
        # 接触监听指定快捷键
        keyboard.remove_hotkey(keyId)

    """ 让控件捕获所有键盘事件 """
    def grabKeyboard(self):
        super().grabKeyboard()
        ...

    """ 释放键盘焦点 """
    def releaseKeyboard(self):
        super().releaseKeyboard()
        ...

    """ 键盘按下事件 """
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.isAutoRepeat():
            print("长按重复触发")
            return
        # 检测组合键
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key.Key_C:
            print("Ctrl + C")
            return
        if event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
            print("按下回车键")
            return
        print(f"按下的按键: {QKeySequence(event.key()).toString()}")

    """ 键盘释放事件 """
    def keyReleaseEvent(self, event):
        super().keyReleaseEvent(event)
        print(f"释放的按键: {QKeySequence(event.key()).toString()}")



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.lineEdit = LineEdit(self)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(QPushButton('Button', self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec())