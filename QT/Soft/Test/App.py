import os
from PySide6.QtWidgets import QMessageBox, QApplication, QFileDialog, QMainWindow, QTextEdit, QWidget, QVBoxLayout, \
    QTabWidget, QColorDialog, QSpinBox, QPushButton
from PySide6.QtGui import QAction, QPainter, Qt, QPixmap, QIcon


class MainWindow(QMainWindow):
    def __init__(self, backgroundPath):
        super().__init__()
        self.tabs = 0
        self.filePath = ""
        self.textObj = []

        self.fz = QWidget()
        layout = QVBoxLayout(self.fz)
        self.fz.resize(300, 160)
        self.spinBox = QSpinBox(self.fz)
        self.spinBox.setValue(24)
        self.spinBox.setMaximum(1145)
        self.spinBox.setFixedSize(100, 50)
        self.button = QPushButton("确定", self)
        self.button.setFixedSize(100, 50)
        layout.addWidget(self.spinBox, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        self.button.clicked.connect(lambda: (self.writeQssFile(str(self.spinBox.value()) + "px"), self.fz.close()))

        self.centerWidget = QWidget()
        self.setCentralWidget(self.centerWidget)
        self.layout = QVBoxLayout(self.centerWidget)
        # 设置窗口大小
        self.setMinimumSize(1000, 600)
        # 读取样式表
        with open('./data/styles/style.qss', 'r', encoding='utf-8') as f:
            style = f.read()
        self.setStyleSheet(style)

        # 添加到布局
        self.tabWidget = QTabWidget(self)
        # 设置标签选中颜色
        with open('./data/styles/QTabBarStyle.qss', 'r', encoding='utf-8') as f:
            self.tabWidget.tabBar().setStyleSheet(f.read())
        self.layout.addWidget(self.tabWidget)
        # 创建菜单
        self.createQAction()

        # 背景图
        self.backgroundPixmap = QPixmap(backgroundPath)

    def createQTab(self, fileName: str = None):

        with open('./data/styles/textStyle.qss', 'r', encoding='utf-8') as f:
            style = f.read()
            tab = QWidget()
            layout = QVBoxLayout()
            textEdit = QTextEdit()
            textEdit.setPlaceholderText("在这里输入文本...")
            textEdit.setStyleSheet(style)
            layout.addWidget(textEdit)
            tab.setLayout(layout)
            self.tabWidget.addTab(tab, fileName or "新文件")
            self.textObj.append(textEdit)
            self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

    def openFile(self):
        try:
            self.filePath, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)")
            with open(self.filePath, 'r', encoding='utf-8') as f:
                result = f.read()
            self.tabs += 1
            self.createQTab(self.filePath.split('/')[-1])
            self.tabWidget.setCurrentIndex(self.tabWidget.count() -1)
            self.getQTextObj().setText(result)
            return
        except Exception:
            pass

    def createQAction(self):
        # 主菜单和对应的子选项
        menus = {
            "File": ["新建文件", "打开文件", "保存文件", "关闭"],
            "Util": ["文字大小", "背景颜色", "文字颜色", "重置"],
            "About": ["About bin", "Version"]
        }
        fc = [
            lambda: (setattr(self, 'tabs', self.tabs + 1), print(self.tabs), self.createQTab()),
            self.openFile,
            self.save,
            lambda checked: (self.tabWidget.removeTab(self.tabWidget.currentIndex())),
            lambda: (self.fz.show(), self.fz.raise_(), self.fz.activateWindow()),
            lambda: self.writeQssFile(bgColor=self.getColor()),
            lambda: self.writeQssFile(textColor=self.getColor()),
            lambda: self.writeQssFile(),
            lambda: QMessageBox.information(self, "提示", "功能为开放"),
            lambda: os.system('start https://www.github.com/mikuas'),
        ]
        keys = [
            "Ctrl+N",
            "Ctrl+O",
            "Ctrl+S",
            "Ctrl+C"
        ]
        # 创建菜单栏
        menuBar = self.menuBar()
        index = 0

        for bar, actions in menus.items():
            print(bar, actions)
            menu = menuBar.addMenu(QIcon('./data/images/icon/setting.png'), bar)
            for actionName in actions:
                # 创建子菜单项
                newAction = QAction(QIcon('./data/images/icon/function-icon.png'), actionName, self)
                newAction.setShortcut(keys[index]) if index < len(keys) else None
                menu.addAction(newAction)
                # 连接信号与槽
                newAction.triggered.connect(fc[index])
                index += 1

    def writeQssFile(self, font='24px', bgColor='rgba(255, 255, 255, 0)', textColor='#000000'):
        qssStyle = f"""
            QTextEdit {{
                font-size: {font};
                background-color: {bgColor};
                color: {textColor};
            }}
        """
        for text in self.textObj:
            text.setStyleSheet(qssStyle)

    def getColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            return color.name()

    def save(self):
        try:
            path, _ = QFileDialog.getSaveFileName(self, "保存文件", "result.txt", "所有文件(*);;文本文件(*.txt)")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(self.getQTextObj().toPlainText())
        except Exception:
            pass

    def getQTextObj(self):
        tab = self.tabWidget.currentWidget()
        return tab.findChild(QTextEdit)

    def paintEvent(self, event):
        # 创建 QPainter 对象
        painter = QPainter(self)

        # 获取窗口的宽度和高度
        windowWidth = self.width()
        windowHeight = self.height()

        # 将背景图片缩放到窗口大小，并使用平滑转换模式
        scaledPixmap = self.backgroundPixmap.scaled(
            windowWidth, windowHeight, Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        # 在窗口内绘制缩放后的背景图片
        painter.drawPixmap(0, 0, scaledPixmap)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow('./data/images/background/background.png')
    window.show()
    app.exec()
