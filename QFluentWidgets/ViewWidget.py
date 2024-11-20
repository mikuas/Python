import sys
from types import NoneType

from PySide6.QtCore import QSize, QModelIndex, QRect, QTime, QTimer
from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QCompleter, QLineEdit, QStyleOptionViewItem, \
    QListWidgetItem, QTableWidgetItem, QTreeWidgetItem
from PySide6.QtGui import Qt, QColor, QAction, QPainter, QFont, QStandardItemModel, QStandardItem

from qfluentwidgets import SmoothScrollArea, VBoxLayout, FluentLabelBase, CaptionLabel, BodyLabel, StrongBodyLabel, \
    FlipView, HorizontalFlipView, VerticalFlipView, FlipImageDelegate, getFont, ListWidget, ListView, setFont, \
    TableWidget, SmoothMode, TreeWidget, TreeView, TabBar, FluentIcon, TabCloseButtonDisplayMode


class ViewWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.index = 0
        self.count = 1

        self.initWindow()
        self.initWidgets()
        self.initLayout()
        self.imgTimeStart()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initWidgets(self):
        '''翻转视图'''
        '''
            HorizontalFlipView 水平翻转视图
            VerticalFlipView 垂直翻转视图
        '''
        self.flipView = FlipView(self)
        # add image
        self.flipView.addImages([
            r"C:\Users\Administrator\OneDrive\Pictures\17.png",
            r"C:\Users\Administrator\OneDrive\Pictures\18.png",
            r"C:\Users\Administrator\OneDrive\Pictures\19.png",
            r"C:\Users\Administrator\OneDrive\Pictures\20.png",
            r"C:\Users\Administrator\OneDrive\Pictures\21.png",
            r"C:\Users\Administrator\OneDrive\Pictures\22.png",
            r"C:\Users\Administrator\OneDrive\Pictures\23.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\24.jpg",
            r"C:\Users\Administrator\OneDrive\Pictures\25.png"
        ])
        # 通过缩放策略来保持图片的宽高比
        self.flipView.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        # 默认图片大小480x270 调整大小
        self.flipView.setItemSize(QSize(640, 320))
        self.flipView.setFixedSize(QSize(640, 320))
        # 设置间距
        # self.flipView.setSpacing(15)
        # 启用圆角
        self.flipView.setBorderRadius(15)

        # 使用自定义代理
        # self.flipView.setItemDelegate(CustomFlipItemDelegate(self.flipView))

        # 设置当前图像
        # self.flipView.setCurrentIndex(5)

        # 连接信号插槽
        self.flipView.currentIndexChanged.connect(
            lambda index: (
                # print(index),
                self.setIndex(index)
            )
        )

        '''列表部件'''
        self.listWidget = ListWidget(self)  # ListView 列表视图
        # item = QListWidgetItem('name')
        # item.setIcon('icon')
        # self.listWidget.addItem()
        # self.listWidget.addItems([
        #     '绫地宁宁', '因幡爱瑠', '椎叶䌷', '亚托莉', ' 朝武芳乃', '丛雨', '常陆茉子', '上坂茅羽耶', '矢来美羽', '在原七海',
        #     '三司绫濑', '式部茉优', '二条院羽月', '和泉妃爱', '常盘华乃', '锦明日海', '镰仓诗樱', '结城明日奈', '小鸟游六花',
        #     '御坂美琴', '佐天泪子', '后藤一里', '山田凉', '伊地知虹夏', '喜多郁代'
        # ])
        self.listWidget.addItem(
            QListWidgetItem("Hello")
        )
        self.listWidget.setFixedHeight(500)
        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        self.listWidget.setSelectRightClickedRow(True)
        # 连接信号插槽
        self.listWidget.clicked.connect(
            lambda value: print(self.listWidget.model().data(value))
        )
        # 取消焦点
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setStyleSheet("""
            ListWidget::item {
                font-size: 24px;
                background-color: red;
                height: 50px;
            }
            ListWidget::item:selected {
                border: none;
            }
        """)

        '''表格部件'''
        self.tableWidget = TableWidget(self)    # TableView 表格视图
        # 启用并设置圆角
        self.tableWidget.setBorderVisible(True)
        self.tableWidget.setBorderRadius(10)
        # 自动换行
        self.tableWidget.setWordWrap(True)
        # 设置行数
        self.tableWidget.setRowCount(3)
        # 设置列数
        self.tableWidget.setColumnCount(5)

        # add data
        songInfos = [
            ['シアワセ', 'aiko', '秘密', '2008', '5:25'],
            ['なんでもないや', 'RADWIMPS', '君の名は。', '2016', '3:16'],
            ['恋をしたのは', 'aiko', '恋をしたのは', '2016', '6:02'],
        ]
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                self.tableWidget.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.tableWidget.setFixedSize(950, 250)
        # self.tableWidget.setStyleSheet("""
        #     TableWidget::item {
        #         width: 250px;
        #         text-align: center;
        #     }
        # """)
        self.tableWidget.clicked.connect(
            lambda value: print(self.tableWidget.model().data(value))
        )
        self.tableWidget.itemClicked.connect(
            lambda item: print(self.tableWidget.currentItem().text())
        )

        # 设置水平表头并隐藏垂直表头
        self.tableWidget.setHorizontalHeaderLabels(['Title', 'Artist', 'Album', 'Year', 'Duration'])
        self.tableWidget.verticalHeader().hide()

        # 默认情况下，右键单击某个列表项时不会更新该列的选中状态，如需立即选中可调用下述方法
        self.tableWidget.setSelectRightClickedRow(True)
        # 当显示器的分辨率较高时，平滑滚动可能导致表格卡顿，这时候可以禁用平滑滚动
        # self.tableWidget.scrollDelagate.verticalSmoothScroll.setSmoothMode(SmoothMode.NO_SMOOTH)

        '''树状部件'''
        self.treeWidget = TreeWidget(self)
        self.treeWidget.setMinimumHeight(200)
        # add subtree
        item1 = QTreeWidgetItem(['Father1'])
        item1.addChildren([
            QTreeWidgetItem(['Father1 Sub1']),
            QTreeWidgetItem(['Father1 Sub2'])
        ])
        self.treeWidget.addTopLevelItem(item1)
        item2 = QTreeWidgetItem(['Father2'])

        item3 = QTreeWidgetItem(['Father2 Sub'])
        item3.addChildren([
            QTreeWidgetItem(['Father2 Sub1']),
            QTreeWidgetItem(['Father2 Sub2'])
        ])
        item2.addChild(item3)

        self.treeWidget.addTopLevelItem(item2)
        # hide table head
        self.treeWidget.setHeaderHidden(True)
        # 当显示器的分辨率较高时，平滑滚动可能导致卡顿，这时候可以禁用平滑滚动
        # self.treeWidget.scrollDelagate.verticalSmoothScroll.setSmoothMode(SmoothMode.NO_SMOOTH)

        self.treeWidget.currentItemChanged.connect(
            lambda current, previous:
            print(
                current.text(0) if type(current) is not NoneType else '',
                previous.text(0) if type(previous) is not NoneType else ''
            )
        )

        '''树状视图'''
        self.treeView = TreeView(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Items"])
        # create root item
        root = QStandardItem("Root")
        self.model.appendRow(root)
        # create sub item
        sub1 = QStandardItem("Sub1")
        sub2 = QStandardItem("Sub2")

        root.appendRow(sub1)
        root.appendRow(sub2)

        subb = QStandardItem("Sub Sub 1")
        sub1.appendRow(subb)

        self.treeView.setModel(self.model)
        self.treeView.selectionModel().selectionChanged.connect(
            lambda selected, deselected:
            self.onItemSelected(selected)
        )
        # hide table head
        self.treeView.setHeaderHidden(True)
        self.treeView.setMinimumHeight(200)

        '''标签页组件'''
        self.tabWidget = QWidget(self)

        self.tabBar = TabBar(self)
        self.tabBar.addTab(
            'tab1',
            "Text1",
            FluentIcon.TRAIN,
            lambda: print(True)
        )
        # 添加按钮信号插槽
        self.tabBar.addButton.clicked.connect(
            self.addTab
        )
        # 删除信号插槽
        self.tabBar.tabCloseRequested.connect(
            lambda index: self.tabBar.removeTab(index)
        )
        # 设置标签阴影
        self.tabBar.setTabShadowEnabled(True)
        # 设置标签页可关闭
        # self.tabBar.setTabsClosable(False)
        # 设置可拖拽
        self.tabBar.setMovable(True)
        # 设置可滚动
        self.tabBar.setScrollable(True)
        # 设置关闭按钮显示模式
        self.tabBar.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.ON_HOVER)
        # 设置添加按钮可见
        self.tabBar.setAddButtonVisible(True)

    def addTab(self):
        self.count += 1
        self.tabBar.addTab(
            f'tab{self.count}',
            f'Text{self.count}',
            FluentIcon.GITHUB,
            lambda: print(self.count)
        )

    def onItemSelected(self, selected):
        for index in selected.indexes():
            item = self.model.itemFromIndex(index)
            if item:
                print(item.text())

    def imgTimeStart(self):
        self.imgTime = QTimer(self)
        self.imgTime.timeout.connect(self.updateImgIndex)
        self.imgTime.start(2000)

    def updateImgIndex(self):
        self.index += 1
        if self.index >= self.flipView.count():
            self.index = 0
        self.flipView.setCurrentIndex(self.index)

    def setIndex(self, index):
        self.index = index

    def initLayout(self):
        self.vLayout.addWidget(self.flipView, 0, Qt.AlignCenter)
        self.vLayout.addWidget(self.listWidget)
        self.vLayout.addWidget(self.tableWidget)
        self.vLayout.addWidget(self.treeWidget)
        self.vLayout.addWidget(self.treeView)
        self.vLayout.addWidget(self.tabBar)


class CustomFlipItemDelegate(FlipImageDelegate):
    """ 自定义翻转项委托 """

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        super().paint(painter, option, index)
        painter.save()

        # draw mask
        painter.setBrush(QColor(255, 255, 255, 200))
        painter.setPen(Qt.NoPen)
        rect = option.rect
        rect = QRect(rect.x(), rect.y(), 200, rect.height())
        painter.drawRect(rect)

        # draw text
        painter.setPen(Qt.black)
        painter.setFont(getFont(16, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, '🥰\n硝子酱一级棒卡哇伊')

        painter.restore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ViewWidget("VIEW")
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())

