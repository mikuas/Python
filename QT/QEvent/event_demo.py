import sys

from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLayout
from qfluentwidgets import LineEdit, PrimaryPushButton
from FluentWidgets import VerticalScrollWidget


class LineEdit(LineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setClearButtonEnabled(True)

    """ 控件获得焦点事件 """
    def focusInEvent(self, event):
        super().focusInEvent(event)
        print("LineEdit获得焦点")

    """ 控件失去焦点事件 """
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        print("LineEdit失去焦点")

    """ 鼠标进入控件事件 """
    def enterEvent(self, event):
        super().enterEvent(event)
        print("鼠标进入了LineEdit")

    """ 鼠标离开控件事件 """
    def leaveEvent(self, event):
        super().leaveEvent(event)
        print("鼠标离开了LineEdit")

    """ 键盘按下事件 """
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_Enter:
            print("按下了Enter键")
        elif event.key() == Qt.Key.Key_Escape:
            print("按下了ESC键")
        elif event.key() == Qt.Key.Key_Space:
            print("按下了Space键")
        else:
            print(f"键盘被按下了, 按下的键是{event.text()}") # 获取按键的值

    """ 键盘释放事件 """
    def keyReleaseEvent(self, event):
        super().keyReleaseEvent(event)
        if event.key() == Qt.Key.Key_Enter:
            print("释放了Enter键")
        elif event.key() == Qt.Key.Key_Escape:
            print("释放了ESC键")
        elif event.key() == Qt.Key.Key_Space:
            print("释放了Space键")
        else:
            print(f"释放了{event.text()}键")


class VBoxLayout(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

    """ 布局改变信号 """
    def invalidate(self):
        super().invalidate()
        print("LayoutChange")


class KeyEventFilter(QObject):

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Enter:
                print("Enter Input")
                return True
        return super().eventFilter(obj, event)


class Layout(QLayout):
    def __init__(self):
        super().__init__()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 250)
        self.setContentsMargins(20, 20, 20, 0)
        self.layout = VBoxLayout(self)

        self.addButton = PrimaryPushButton("Add Button", self)
        self.layout.addWidget(self.addButton)

        self.addButton.clicked.connect(lambda: self.layout.addWidget(PrimaryPushButton("Button", self)))

    def closeEvent(self, event):
        super().closeEvent(event)
        # 忽略关闭事件
        event.ignore()
        self.hide()

    def moveEvent(self, event):
        super().moveEvent(event)
        print(event.pos())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        print(self.size())

    def showEvent(self, event):
        super().showEvent(event)
        event.ignore()

    def hideEvent(self, event):
        super().hideEvent(event)
        event.ignore()


class DragWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filter = KeyEventFilter(self)
        self.installEventFilter(self.filter)
        # 设置可接受拖放
        self.setAcceptDrops(True)

    """ 鼠标滚动事件 """
    def wheelEvent(self, event):
        super().wheelEvent(event)
        print("Mouse Wheel")
        if event.angleDelta().y() > 0:
            print('up wheel')
        else:
            print('down wheel')

    """ 拖动事件 """
    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        # print("拖动对象进入了控件")
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)
        print("拖动对象在控件内移动")

    def dragLeaveEvent(self, event):
        super().dragLeaveEvent(event)
        print("拖动对象离开控件")

    def dropEvent(self, event):
        super().dropEvent(event)
        # print("拖动对象放置到控件")
        urls = event.mimeData().urls()
        if urls:
            filePath = [url.toLocalFile() for url in urls]
            print(f"文件路径: {filePath[0]}")
        event.acceptProposedAction()


class MouseWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    """ 鼠标点击事件 """
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            print("鼠标左键按下")
        elif event.button() == Qt.MouseButton.RightButton:
            print("鼠标右键按下")

        # 阻止事件传递给父类控件
        event.accept()

    """ 鼠标释放事件 """
    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

    """ 鼠标双击事件 """
    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        self.lineEdit = LineEdit(self)
        self.setStyleButton = PrimaryPushButton("设置为蓝色背景", self)
        self.widget = Widget()
        self.dragWidget = DragWidget()

        self.vBoxLayout.addWidget(self.lineEdit)
        self.connectSignalSlot(self.initButton())
        self.vBoxLayout.addWidget(self.setStyleButton)

    def connectSignalSlot(self, buttons):
        functions = [
            self.widget.show,
            self.dragWidget.show
        ]
        for button, function in zip(buttons, functions):
            button.clicked.connect(function)

        self.setStyleButton.clicked.connect(lambda: self.setStyleSheet('background-color: skyblue;'))

    def initButton(self):
        texts = [
            "Show New Widget",
            "Show Drag Widget"
        ]
        buttons = []
        for text in texts:
            button = PrimaryPushButton(text, self)
            self.vBoxLayout.addWidget(button)
            buttons.append(button)
        return buttons

    """ 鼠标进入控件事件 """
    def enterEvent(self, event):
        super().enterEvent(event)
        print("鼠标进入了Demo")

    """ 鼠标离开控件事件 """
    def leaveEvent(self, event):
        super().leaveEvent(event)
        print("鼠标离开了Demo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())