from PySide6.QtWidgets import QWidget, QApplication


class TopMenu(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication([])
    widget = TopMenu()
    widget.show()
    app.exec()