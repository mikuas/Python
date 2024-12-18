import sys

from FluentWidgets import VerticalScrollWidget, ColorDialog
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox, QInputDialog, QColorDialog, QFileDialog, \
    QDialogButtonBox, QFontDialog, QFormLayout


class Demo(VerticalScrollWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 520)
        self.bts = []
        self.message = QMessageBox()
        self.inputDialog = QInputDialog(self)
        self.colorDialog = QColorDialog(self)
        self.fileDialog = QFileDialog(self)
        self.fontDialog = QFontDialog(self)

        self.formLayout = QFormLayout(self)

        self.initWidget()
        self.connectSignalSlot()

    def initWidget(self):
        texts = [
            'Click Me Show MessageBox',
            'Click Me Show InputDialog',
            'Click Me Show ColorDialog',
            'Click Me Show FileDialog',
            'Click Me Show FontDialog',
        ]
        for text in texts:
            button = QPushButton(text, self)
            self.bts.append(button)
            self.vBoxLayout.addWidget(button)

    def connectSignalSlot(self):
        functions = [
            self.message.show,
            self.inputDialog.show,
            self.colorDialog.show,
            self.fileDialog.show,
            self.fontDialog.show,
        ]
        for button, function in zip(self.bts, functions):
            button.clicked.connect(function)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec())