

from FluentWidgets import VerticalScrollWidget
from qfluentwidgets import TitleLabel


class HomeInterface(VerticalScrollWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "_"))

        TitleLabel("Home_Interface", self)

