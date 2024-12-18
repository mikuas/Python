import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import TitleLabel, FluentIcon

from QtFluentWidgets.FluentWidgetModule.FluentWidgets import FluentWindow, SplitFluentWindow


class Demo(FluentWindow):
# class Demo(SplitFluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1200, 800)
        self.contents = ["INTERFACE_ONE", "INTERFACE_TWO", "INTERFACE_THREE"]
        self.icons = [FluentIcon.HOME, FluentIcon.APPLICATION, FluentIcon.SETTING]
        self.texts = ["HOME", "APPLICATION", "SETTING"]

        for content, text, icon in zip(self.contents, self.texts, self.icons):
            title = TitleLabel(content, self)
            title.setObjectName(content)
            self.addSubInterface(
                title,
                icon,
                text
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())