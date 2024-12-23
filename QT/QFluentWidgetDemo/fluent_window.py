import sys

from PySide6.QtGui import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget, QHBoxLayout, QApplication, QVBoxLayout
from qfluentwidgets import *
from qframelesswindow.webengine import FramelessWebEngineView


class Widget(QWidget):
    def __init__(self, text, path, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 150)
        self.layout = QHBoxLayout()
        self.image = ImageLabel(path, self)
        self.image.setBorderRadius(8, 8, 8, 8)
        self.image.setFixedSize(self.width(), self.height())
        self.layout.addWidget(self.image)
        self.setObjectName(text.replace(" ", "_"))

    def resizeEvent(self, event):
        self.image.setFixedSize(self.width(), self.height())


class BtWindget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.mainLayout = QHBoxLayout(self)
        self.layout = QVBoxLayout()
        self.button = ToolButton(self)
        self.button.setFixedSize(200, 120)
        self.button.setText("暗色主题")

        self.button2 = ToolButton(self)
        self.button2.setFixedSize(200, 120)
        self.button2.setText("亮色主题")

        self.button.clicked.connect(lambda: setTheme(Theme.DARK))
        self.button2.clicked.connect(lambda: setTheme(Theme.LIGHT))

        self.layout.addWidget(self.button, Qt.AlignCenter)
        self.layout.addWidget(self.button2, Qt.AlignCenter)

        self.mainLayout.addLayout(self.layout)
        self.setObjectName(text.replace(" ", "_"))


class CustomSearchLineEdit(SearchLineEdit):
    def __init__(self, webView, parent=None):
        super().__init__(parent)
        self.webView = webView

    # 输入回车更新URL
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.webView.setUrl(self.text())
        super().keyPressEvent(event)


class WebView(QWidget):
    def __init__(self, text, url, parent=None):
        super().__init__(parent)
        self.resize(1200, 700)
        self.qHboxLayout = QVBoxLayout(self)
        self.web_view = FramelessWebEngineView(self)

        self.lineEdit = CustomSearchLineEdit(self.web_view, self)
        self.lineEdit.setPlaceholderText('请输入网址')
        self.lineEdit.searchSignal.connect(lambda text: self.web_view.setUrl(text))
        # 加载初始网页
        self.web_view.load(url)  # 替换为需要访问的 URL

        self.qHboxLayout.addWidget(self.lineEdit)
        self.qHboxLayout.addWidget(self.web_view)
        self.setObjectName(text.replace(" ", "_"))


class OpenWeb(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        Window().webView.show()

# class Window(SplitFluentWindow):
class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.webView = WebView('Web', "https://yiyan.baidu.com/")
        # 设置主题色
        # setTheme(Theme.LIGHT)

        # 更改主题颜色
        # setThemeColor('#0078d4')

        self.resize(1200, 700)

        self.home = Widget("Interface 1", r"C:\Users\Administrator\OneDrive\Pictures\12.jpg")
        self.music = Widget("Interface 2", r"C:\Users\Administrator\OneDrive\Pictures\13.jpg")
        self.github = Widget("Interface 3", r"C:\Users\Administrator\OneDrive\Pictures\14.jpg")
        self.setting = Widget("Interface 4", r"C:\Users\Administrator\OneDrive\Pictures\15.jpg")
        self.tool = BtWindget("Button")

        self.initWindow()
        #  初始化导航栏
        self.initNavigation()

        '''
        FluentWindow
        提供了切换当前界面的方法，interface
        为待切换的子界面
        '''

        # def switchTo(self, interface: QWidget) -> None

        '''
        FluentWindow
        内部使用
        StackedWidget
        来存放子界面，切换当前界面时
        StackedWidget
        会发出
        currentChanged(index: int) 信号
        '''
        # self.stackedWidget.currentChanged.connect(lambda: print(self.stackedWidget.currentWidget()))

        # 调整展开状态下侧边导航的宽度
        self.navigationInterface.setExpandWidth(150)

        # 默认情况下侧边导航为收缩状态，当窗口宽度超过阈值时才会展开，如果希望禁用收缩并一直保持展开状态
        # 这行代码必须在 setExpandWidth() 后面调用
        # self.navigationInterface.setCollapsible(False)

        # 如果不想禁用收缩，但是希望窗口创建之后侧边栏是展开的
        # 需要设置允许侧边导航展开的最小窗口宽度
        # self.navigationInterface.setMinimumExpandWidth(150)
        # 展开导航栏
        # self.navigationInterface.expand(useAni=False)

        '''
        定制化标题栏 FluentWindow 使用的是 qframelesswindow 库提供的自定义标题栏，对应 titleBar 属性。标题栏使用水平布局
        hBoxLayout，内部组件如下：

        minBtn：最小化按钮
        maxBtn：最大化按钮
        closeBtn：关闭按钮
        iconLabel：图标标签
        titleLabel：标题标签
        '''
        # self.titleBar.closeBtn.hide()

    def initWindow(self):
        # 窗口图标
        self.setWindowIcon(Icon(FluentIcon.GITHUB))
        # 标题
        self.setWindowTitle("Window")

    def initNavigation(self):
        self.addSubInterface(self.home, FluentIcon.HOME, "主页")
        self.addSubInterface(self.music, FluentIcon.MUSIC, "音乐")
        self.addSubInterface(self.music, FluentIcon.BRUSH, "哔哩哔哩")
        # 添加分隔符
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.github, FluentIcon.GITHUB, "GitHub")
        self.addSubInterface(self.tool, FluentIcon.BLUETOOTH, "Tool")
        self.navigationInterface.addItem(
            "Web",
            FluentIcon.SEND,
            "浏览器",
            onClick=self.webView.show
        )
        self.addSubInterface(self.setting, FluentIcon.SETTING, "设置", NavigationItemPosition.BOTTOM)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #  启用云母特效
    window.setMicaEffectEnabled(True)
    window.show()
    sys.exit(app.exec())
