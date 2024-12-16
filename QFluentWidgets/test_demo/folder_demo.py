import sys

from PySide6.QtWidgets import QWidget, QApplication
from QFluentWidgets.FluentWidgetModule.FluentWidgets import FolderListCard


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 520)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())