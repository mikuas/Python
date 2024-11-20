from PySide6.QtCore import QEasingCurve, QModelIndex, QRect, QTimer
from PySide6.QtGui import Qt, QPainter, QColor, QFont
from PySide6.QtWidgets import QWidget, QStyleOptionViewItem
from qfluentwidgets import (
    Dialog as View, MessageBoxBase, SubtitleLabel, LineEdit, MessageBox as MsbBox, ColorDialog as ColorD, FlowLayout,
    FlipImageDelegate, getFont, HorizontalFlipView
)
from .scroll_widget import SmoothScrollWidget

class Dialog(View):
    """ 无边框对话框 """
    def __init__(self, title, content, parent):
        super().__init__(title, content, parent)
        setButtonText(self.yesButton, self.cancelButton)


class MessageBox(MsbBox):
    """ 带遮罩的对话框 """
    def __init__(self, title, content, parent=None):
        super().__init__(title, content, parent)
        setButtonText(self.yesButton, self.cancelButton)


class UrlDialog(MessageBoxBase):
    """ 链接对话框 """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # add widget to layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # set min width
        self.widget.setMinimumWidth(350)

        setButtonText(self.yesButton, self.cancelButton)


class ColorDialog(ColorD):
    def __init__(self, color, title, parent=None, enableAlpha=False):
        super().__init__(color, title, parent, enableAlpha)
        setButtonText(self.yesButton, self.cancelButton)

    def getColor(self):
        self.exec()
        return self.color.name()


class FlowLayoutWidget(SmoothScrollWidget):
    """ 流式布局 """
    def __init__(self, duration: int = 250, ease: QEasingCurve = QEasingCurve.Type.InCurve, parent=None):
        # InCurve
        # OutBack
        super().__init__(parent)
        self.__initLayout(duration, ease)
        self.__widgets = []

    def __initLayout(self, duration: int, ease: QEasingCurve):
        self.__flowLayout = FlowLayout(self, True)
        self.__flowLayout.setAnimation(duration, ease)
        self.vLayout.addLayout(self.__flowLayout)

    def addWidget(self, widget: QWidget):
        self.__widgets.append(widget)
        self.__flowLayout.addWidget(widget)
        self.__reLoadWidget()
        return self

    def addWidgets(self, widgets: list[QWidget]):
        for widget in widgets:
            self.__widgets.append(widget)
            self.__flowLayout.addWidget(widget)
        self.__reLoadWidget()
        return self

    def __reLoadWidget(self):
        self.__flowLayout.removeAllWidgets()
        for widget in self.__widgets:
            self.__flowLayout.addWidget(widget)


class FlipViewWidget(HorizontalFlipView):
    """ 翻转视图组件 """
    def __init__(self, parent, aspectRation: Qt.AspectRatioMode = Qt.AspectRatioMode.KeepAspectRatio):
        super().__init__(parent)
        self.parent = parent
        self.__index = 0
        self.num = 1
        self.setAspectRatioMode(aspectRation)
        self.setBorderRadius(24)
        self.resize(parent.width(), parent.height())

    def setDelegate(self, color: QColor, fontSize: int, fontColor: QColor, text: str, width: int = None, height: int = None):
        self.setItemDelegate(FlipItemDelegate(color, fontSize, fontColor, text, width, height, self))
        return self

    def setAutoPlay(self, interval: int = 1500):
        self.currentIndexChanged.connect(lambda index: self.__setIndex(index))
        self.__initTimer(interval)
        return self

    def addImages(self, images, targetSize=None):
        super().addImages(images, targetSize)
        return self

    def addImage(self, image):
        super().addImage(image)
        return self

    def __initTimer(self, interval: int = 1500):
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: (self.__updateIndex(), self.__setIndex(self.__index + self.num)))
        self.timer.start(interval)

    def __updateIndex(self):
        if self.__index == 0:
            self.num = 1
        if self.__index == self.count() - 1:
            self.num = -1
        self.setCurrentIndex(self.__index)

    def __setIndex(self, index: int):
        self.__index = index


class FlipItemDelegate(FlipImageDelegate):
    def __init__(self, color: QColor, fontSize: int, fontColor: QColor, text: str, width: int = None, height: int = None, parent=None):
        super().__init__(parent)
        self.color = color
        self.width = width
        self.height = height
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.text = text

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        super().paint(painter, option, index)
        painter.save()

        painter.setBrush(self.color)
        painter.setPen(Qt.PenStyle.NoPen)
        rect = option.rect
        rect = QRect(rect.x(), rect.y(), self.width or 200, self.height or rect.height())
        painter.drawRect(rect)

        painter.setPen(self.fontColor)
        painter.setFont(getFont(self.fontSize, QFont.Weight.Bold))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, self.text)

        painter.restore()


def setButtonText(yesBt, cancelBt):
    yesBt.setText('确定')
    cancelBt.setText('取消')
