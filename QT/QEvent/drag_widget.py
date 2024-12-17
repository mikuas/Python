import sys

from FluentWidgets import VBoxLayout
from PySide6.QtCore import QSize, Signal, QFileInfo
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog
from qfluentwidgets import setTheme, Theme, setFont


class DragFolderWidget(QWidget):
    """ get drag folder widget"""
    draggedChange = Signal(list)
    selectionChange = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setMinimumSize(QSize(256, 200))

        self.button = QPushButton("拖动文件夹到此或点击选择文件夹", self)
        self.button.setStyleSheet('border: 3px dotted skyblue; border-radius: 12px; color: aqua;')
        setFont(self.button, 14)
        self.button.clicked.connect(self._showDialog)

    def _showDialog(self):
        return self.selectionChange.emit([QFileDialog.getExistingDirectory(self, "选择文件夹")])

    # """ 拖动离开事件 """
    # def dragLeaveEvent(self, event):
    #     super().dragLeaveEvent(event)

    """ 拖动进入事件 """
    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        if event.mimeData().hasUrls:
            event.acceptProposedAction()
        else:
            event.ignore()

    # """ 拖动移动事件"""
    # def dragMoveEvent(self, event):
    #     super().dragMoveEvent(event)

    """ 拖动放置事件 """
    def dropEvent(self, event):
        super().dropEvent(event)
        urls = [url.toLocalFile() for url in event.mimeData().urls()]
        dirPath = []
        if urls:
            for url in urls:
                if QFileInfo(url).isDir():
                    dirPath.append(url)
            self.draggedChange.emit(dirPath)
        event.acceptProposedAction()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.button.setFixedSize(self.size())


class DragFileWidget(DragFolderWidget):
    """ get dray file widget """
    def __init__(self, parent=None, defaultDir="./", fileFilter="所有文件 (*.*);; 文本文件 (*.txt)"):
        """ 多个文件类型用;;分开 """
        super().__init__(parent)
        self.button.setText("拖动文件到此或点击选择文件")
        self.defaultDir = defaultDir
        self.fileFilter = fileFilter

    def _showDialog(self):
        return self.selectionChange.emit(QFileDialog.getOpenFileNames(self, "选择文件", self.defaultDir, self.fileFilter)[0])

    def dropEvent(self, event):
        urls = [url.toLocalFile() for url in event.mimeData().urls()]
        filePath = []
        if urls:
            for url in urls:
                if not QFileInfo(url).isDir():
                    filePath.append(url)
            self.draggedChange.emit(filePath)
        event.acceptProposedAction()


class Demo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vLayout = VBoxLayout(self)
        self.dragFolderWidget = DragFolderWidget(self)
        self.dragFileWidget = DragFileWidget(self)

        self.vLayout.addWidgets([self.dragFolderWidget, self.dragFileWidget])

        self.dragFolderWidget.draggedChange.connect(lambda value: print(f"拖动的文件夹: {value}"))
        self.dragFileWidget.draggedChange.connect(lambda value: print(f"拖动的文件: {value}"))
        self.dragFolderWidget.selectionChange.connect(lambda value: print(f"选择的文件夹: {value}"))
        self.dragFileWidget.selectionChange.connect(lambda value: print(f"选择的文件: {value}"))


# \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
    """ 拖动放置事件 """
    # def dropEvent(self, event):
    #     super().dropEvent(event)
    #     urls = [url.toLocalFile() for url in event.mimeData().urls()]
    #     dirPath = []
    #     if urls:
    #         for url in urls:
    #             if QFileInfo(url).isDir():
    #                 dirPath.append(url)
    #         self.draggedChange.emit(dirPath)
    #     event.acceptProposedAction()
    #     urls = event.mimeData().urls()
    #     # get file path
    #     if urls:
    #         filePath = [url.toLocalFile() for url in urls]
    #         if QFileInfo(filePath[0]).isDir():
    #             print(f"filePath: {filePath}, This is DIR")
    #             self.button.setText(str(filePath))
    #         else:
    #             InfoBar(
    #                 InfoBarIcon.ERROR,
    #                 '拖入的文件不是文件夹',
    #                 f"FilePath: {filePath[0]}, This is Not DIR",
    #                 isClosable=False,
    #                 duration=2500,
    #                 parent=self
    #             ).show()
    #     event.acceptProposedAction()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())