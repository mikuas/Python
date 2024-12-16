import sys

from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import PrimaryPushButton, TitleLabel

from QFluentWidgets.FluentWidgetModule.FluentWidgets import (
    VerticalScrollWidget,
    Dialog, MessageBox, UrlDialog, ColorDialog, CustomDialog,
    FlowLayoutWidget, FlipViewWidget,
    WinFluentIcon, Icon
)


class Demo(VerticalScrollWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 650)
        self.buttons = []
        self.setWindowIcon(Icon(WinFluentIcon.WIN_11_LOG))

        self.initFlowLayoutWidget()
        self.initFlipViewWidget()
        self.initDialog()
        self.initLayout()
        self.connectSignalSlots()

    def initFlowLayoutWidget(self):
        self.flowLayoutWidget = FlowLayoutWidget()
        self.flowLayoutWidget.resize(self.size())
        self.addButton = PrimaryPushButton("Add Button", self)
        self.flowLayoutWidget.addWidget(self.addButton)
        for _ in range(10):
            button = PrimaryPushButton(f"Button", self)
            self.flowLayoutWidget.addWidget(button)

    def initFlipViewWidget(self):
        self.flipViewWidget = (
            FlipViewWidget(aspectRation=Qt.AspectRatioMode.IgnoreAspectRatio)
            .setAutoPlay(500)
        )
        self.flipViewWidget.addImages([
            r"C:\Users\Administrator\OneDrive\Pictures\0.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\1.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\2.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\3.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\4.jpg",
        ])
        self.flipViewWidget.resize(800, 520)

    def initDialog(self):
        self.dialog = Dialog("Dialog", "This is the dialog", self)
        self.messageBox = MessageBox("MessageBox", "This is the message box", self)
        self.urlDialog = UrlDialog(self)
        self.colorDialog = ColorDialog(QColor(114, 114, 114), 'ColorDialog', self)
        self.customDialog = CustomDialog(self)
        self.customDialog.addWidget(TitleLabel("This is CustomDialog", self))

    def initLayout(self):
        texts = [
            "Click Me Display Dialog",
            "Click Me Display MessageBox",
            "Click Me Display UrlDialog",
            "Click Me Display ColorDialog",
            "Click Me Display CustomDialog",
            "Click Me Show FlowLayoutWidget",
            "Click Me Show FlipViewWidget",
        ]
        for text in texts:
            button = PrimaryPushButton(text, self)
            self.buttons.append(button)
            self.vBoxLayout.addWidget(button)

    def connectSignalSlots(self):
        functions = [
            self.dialog.show,
            self.messageBox.show,
            self.urlDialog.show,
            self.colorDialog.show,
            self.customDialog.show,
            self.flowLayoutWidget.show,
            self.flipViewWidget.show,
        ]
        for button, function in zip(self.buttons, functions):
            button.clicked.connect(function)
        self.addButton.clicked.connect(
            lambda: self.flowLayoutWidget.addWidget(PrimaryPushButton("Button", self))
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())