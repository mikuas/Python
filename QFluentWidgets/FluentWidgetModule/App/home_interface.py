from FluentWidgets import VerticalScrollWidget
from qfluentwidgets import ImageLabel


class HomeWidget(VerticalScrollWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "_"))
        self.__initWindow()

    def __initWindow(self):
        self.vLayout.addWidget(ImageLabel(r"C:\Users\Administrator\OneDrive\FORZA\38.png", self))