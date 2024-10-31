import sys

from PySide6.QtWidgets import QApplication
from centerWidget import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()