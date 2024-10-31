from PySide6.QtGui import QIcon
from .fileControl import File

length = len(File.getImagePath('../data/images/musicPictures'))

class QC:

    @staticmethod
    def setIT(button, icon, text):
        button.setIcon(QIcon(icon))
        button.setText(text)

    @staticmethod
    def getListIndex(listWidget):
        index = listWidget.currentRow()
        if index == 0:
            return 0
        elif index == length - 1:
            return length - 1
        elif 0 < index < length:
            return index
        else:
            return -1

    def getLastIndex(self, listWidget):
        index = self.getListIndex(listWidget)
        if index > 0:
            return index - 1
        else:
            return length - 1

    def getNextIndex(self, listWidget):
        index = self.getListIndex(listWidget)
        if index == -1 or index == length:
            return 0
        elif index < length:
            return index + 1
