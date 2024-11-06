import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget, QApplication, QSystemTrayIcon, QStackedWidget, QLabel
from PySide6.QtGui import Qt, QAction, QColor, QActionGroup, QIcon, QPainter, QBrush, QFont

from qfluentwidgets import SmoothScrollArea, VBoxLayout, RoundMenu, PrimaryPushButton, Action, FluentIcon, AvatarWidget, \
    NavigationPushButton, NavigationToolButton, NavigationSeparator, NavigationTreeWidget, NavigationAvatarWidget, \
    NavigationPanel, NavigationInterface, NavigationBar, Pivot, PivotItem, SegmentedItem, isDarkTheme, SegmentedWidget, \
    SegmentedToolWidget, SegmentedToggleToolWidget, BreadcrumbItem, BreadcrumbBar


class NavWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.initWindow()
        self.initNav()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initNav(self):
        '''
            NavigationWidget    导航小部件基类
            BreadcrumbWidget    面包屑导航按钮基类
        '''

        '''导航按钮'''
        self.navButton = NavigationPushButton(
            FluentIcon.SEND,
            "Text",
            True,
            self
        )

        '''导航工具按钮'''
        self.navToolButton = NavigationToolButton(
            FluentIcon.HOME,
            self
        )

        '''导航分隔符'''
        self.navSeparator = NavigationSeparator(self)

        '''导航树状组件'''
        # self.navTreeWidget = NavigationTreeWidget(
        #     FluentIcon.TRAIN,
        #     "Text",
        #     True,
        #     self
        # )

        '''导航头像组件'''
        self.navAvatarWidget = NavigationAvatarWidget(
            "Name",
            r"C:\Users\Administrator\OneDrive\Pictures\47.jpg",
            self
        )

        '''侧边导航面板'''
        self.navPanel = NavigationPanel(self, isMinimalEnabled=500)

        '''侧边导航界面'''
        self.navInterface = NavigationInterface(self)

        '''侧边导航按钮'''
        self.navBarPushButton = NavigationPushButton(
            FluentIcon.HOME,
            'HOME',
            True,
            parent=self
        )

        '''侧边导航栏'''
        self.navBar = NavigationBar(self)

        '''顶部导航栏'''
        self.pivot = Pivot(self)
        # 添加标签项 绑定全局唯一的routeKey
        self.pivot.addItem(
            "HOMEInterface",
            "HOME",
            lambda: self.pivot.setCurrentItem('HOMEInterface')
        )
        self.pivot.addItem(
            "MUSICInterface",
            "MUSIC",
            lambda: self.pivot.setCurrentItem('MUSICInterface')
        )
        self.pivot.addItem(
            "VIDEOInterface",
            'VIDEO',
            lambda: self.pivot.setCurrentItem('VIDEOInterface')
        )
        # 设置当前标签项
        self.pivot.setCurrentItem("MUSICInterface")

        # def __init__(self):
        #     super().__init__()
        #     self.pivot = Pivot(self)
        #     self.stackedWidget = QStackedWidget(self)
        #     self.vBoxLayout = QVBoxLayout(self)
        #
        #     self.songInterface = QLabel('Song Interface', self)
        #     self.albumInterface = QLabel('Album Interface', self)
        #     self.artistInterface = QLabel('Artist Interface', self)
        #
        #     # 添加标签页
        #     self.addSubInterface(self.songInterface, 'songInterface', 'Song')
        #     self.addSubInterface(self.albumInterface, 'albumInterface', 'Album')
        #     self.addSubInterface(self.artistInterface, 'artistInterface', 'Artist')
        #
        #     # 连接信号并初始化当前标签页
        #     self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        #     self.stackedWidget.setCurrentWidget(self.songInterface)
        #     self.pivot.setCurrentItem(self.songInterface.objectName())
        #
        #     self.vBoxLayout.setContentsMargins(30, 0, 30, 30)
        #     self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignHCenter)
        #     self.vBoxLayout.addWidget(self.stackedWidget)
        #     self.resize(400, 400)
        #
        # def addSubInterface(self, widget: QLabel, objectName: str, text: str):
        #     widget.setObjectName(objectName)
        #     widget.setAlignment(Qt.AlignCenter)
        #     self.stackedWidget.addWidget(widget)
        #
        #     # 使用全局唯一的 objectName 作为路由键
        #     self.pivot.addItem(
        #         routeKey=objectName,
        #         text=text,
        #         onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        #     )
        #
        # def onCurrentIndexChanged(self, index):
        #     widget = self.stackedWidget.widget(index)
        #     self.pivot.setCurrentItem(widget.objectName())

        '''顶部导航栏按钮'''
        # self.pivotButton = PivotItem(self.pivot)
        # self.pivotButton.setIcon(FluentIcon.STOP_WATCH)

        '''分段导航栏按钮'''
        # self.segmentedItem = SegmentedItem(self.pivot)
        # self.segmentedItem.setIcon(FluentIcon.FOLDER)

        '''分段导航栏'''
        self.segmentedWidget = SegmentedWidget(self)
        self.segmentedWidget.addItem(
            'interface1',
            'HOME',
            lambda: print("interface1")
            # ,icon=
        )
        self.segmentedWidget.addItem(
            'interface2',
            'MUSIC',
            lambda: print("interface2")
        )
        self.segmentedWidget.addItem(
            'interface3',
            'VIDEO',
            lambda: print("interface3")
        )
        self.segmentedWidget.setCurrentItem('interface2')

        '''工具分段导航栏'''
        self.segmentedToolWidget = SegmentedToolWidget(self)
        self.segmentedToolWidget.addItem(
            'it1',
            FluentIcon.HOME,
            lambda: print("it1")
        )
        self.segmentedToolWidget.addItem(
            'it2',
            FluentIcon.MUSIC,
            lambda: print("it2")
        )
        self.segmentedToolWidget.addItem(
            'it3',
            FluentIcon.VIDEO,
            lambda: print("it3")
        )

        '''开关工具分段导航栏'''
        self.segmentedToggleToolWidget = SegmentedToggleToolWidget()
        self.segmentedToggleToolWidget.addItem(
            'i1',
            FluentIcon.HOME,
            lambda: print("i1")
        )
        self.segmentedToggleToolWidget.addItem(
            'i2',
            FluentIcon.MUSIC,
            lambda: print("i2")
        )
        self.segmentedToggleToolWidget.addItem(
            'i3',
            FluentIcon.VIDEO,
            lambda: print("i3")
        )

        '''面包屑导航按钮'''
        # self.breadButton = BreadcrumbItem(
        #     'N',
        #     'Button',
        #     0,
        #     self
        # )

        '''面包屑导航栏'''
        self.breadBar = BreadcrumbBar()
        self.breadBar.addItem(
            'b1',
            "HOME"
        )
        self.breadBar.addItem(
            'b2',
            'MUSIC'
        )
        self.breadBar.addItem(
            'b3',
            'VIDEO',
        )

    def initLayout(self):
        self.vLayout.addWidget(self.navButton)
        self.vLayout.addWidget(self.navToolButton)
        self.vLayout.addWidget(self.navSeparator)
        # self.vLayout.addWidget(self.navTreeWidget)
        self.vLayout.addWidget(self.navAvatarWidget)
        self.vLayout.addWidget(self.navPanel)
        self.vLayout.addWidget(self.navInterface)
        self.vLayout.addWidget(self.navBarPushButton)
        self.vLayout.addWidget(self.pivot)
        self.vLayout.addWidget(self.segmentedWidget)
        self.vLayout.addWidget(self.segmentedToolWidget, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.segmentedToggleToolWidget, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.breadBar, 0, Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = NavWidget("NAV")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())
