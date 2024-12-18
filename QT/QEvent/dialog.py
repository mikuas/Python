import sys

from qfluentwidgets import ColorDialog, isDarkTheme, MaskDialogBase

from PySide6.QtWidgets import QDialog, QApplication, QWidget
from qfluentwidgets.components.dialog_box.color_dialog import HuePanel


class Dialog(HuePanel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        Dialog(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec())