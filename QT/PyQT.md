# PySide6

## 系统托盘对象
```python
from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

class TrayIconWidget:
    def __init__(self, parent, path):
        self.trayIcon = QSystemTrayIcon(parent)
        self.trayIcon.setIcon(QIcon(path))
        self.trayIcon.setToolTip('Ciallo～(∠・ω< )⌒☆')
        self.trayIcon.activated.connect(lambda reason: (parent.show(), parent.raise_(), parent.activateWindow()) if reason == QSystemTrayIcon.ActivationReason.Trigger else reason)
        # 托盘图标菜单
        trayMenu = QMenu()
        # 添加分隔符
        trayMenu.addSeparator()

        showActionTray = QAction('显示窗口', parent)
        showActionTray.triggered.connect(lambda: (parent.show(), parent.raise_(), parent.activateWindow()))
        quitAction = QAction('退出', parent)
        quitAction.triggered.connect(parent.quitApp)
        # 添加到托盘中
        trayMenu.addActions([showActionTray, quitAction])
        # 设置菜单
        self.trayIcon.setContextMenu(trayMenu)
        # 显示系统托盘图标
        self.trayIcon.show()

```

---

## 列表布局对象
```python
from PySide6.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
# 列表布局
listWidget = QListWidget()
# 添加列表项
item = QListWidgetItem('Name')
# 设置项的图标
item.setIcon(QIcon('iconPath'))
# 添加到列表
listWidget.addItem(item)
# 设置图标大小
listWidget.setIconSize(QSize(w, h))
# 创建连接信号与槽
listWidget.clicked.connect('Method') # 单击信号
# 自定义发出信号
listWidget.itemChanged. connect | emit ('Method') # 更改信号
listWidget.itemDoubleClicked.connect('Method') # 双击信号
listWidget.itemEntered.connect('Method') # 鼠标悬停信号
listWidget.itemPressed.connect('Method') # 当鼠标按下某个项时触发，不管按的是哪一个键
# 设置当前列表选择的项
listWidget.setCurrentItem('Index')
# 获取当前选中项的索引
listWidget.currentRow()
# 设置为多选
listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
# 获取选中的所有项
listWidget.selectedItems()
# 设置样式
listWidget.setStyleSheet('Style')
```

---

## 视频播放对象
```python
from PySide6.QtCore import QUrl
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# 创建媒体播放对象
media = QMediaPlayer()
# 视频播放对象
video = QVideoWidget()
# video.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
# video.setGeometry(self.rect())
# 音频输出对象
audio = QAudioOutput()
# 设置音频输出对象
media.setVideoOutput(video)
# 设置视频输出对象
media.setAudioOutput(audio)
# 设置视频URL
media.setSource(QUrl('videoPath'))
# 播放
media.play()
# 暂停
media.pause()
# 停止
media.stop()
```

---

## 音频播放对象
```python
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# 创建音频播放对象
player = QMediaPlayer()
# 创建音频输出对象
audioOutput = QAudioOutput()
# 设置音频输出对象
player.setAudioOutput(audioOutput)
# 设置音频路径
player.setSource(QUrl.fromLocalFile('audioPath'))
# 获取媒体的总时长
QMediaPlayer.duration(player)
# 获取媒体播放位置
player.position()
# 播放
player.play()
# 暂停
player.stop()
# 连接媒体状态更改的信号插槽
player.mediaStatusChanged.connect('Method')
# 信号
QMediaPlayer.MediaStatus.EndOfMedia # 媒体结束
QMediaPlayer.MediaStatus.LoadedMedia # 媒体加载 ...
```

---

## 窗口叠堆对象
```python
from PySide6.QtWidgets import QStackedWidget
# 创建窗口叠堆对象
stackedWidget = QStackedWidget()
# 添加小部件
stackedWidget.addWidget('WidgetObj')
# 切换视图
stackedWidget.setCurrentIndex('Index')
stackedWidget.setCurrentWidget('Index')
# 获取当前的小部件
stackedWidget.currentWidget()
stackedWidget.currentIndex()
```

---

## 按工具钮组对象
```python
from PySide6.QtWidgets import QButtonGroup, QToolButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt
# 创建按钮组对象
buttonGroup = QButtonGroup()
# 设置只能同时选择一个
buttonGroup.setExclusive(True)
# 创建工具按钮对象
button = QToolButton()
# 默认选中 点击
button.animateClick()
# 设置按钮名称
button.setText('Name')
# 设置按钮图标
button.setIcon(QIcon('iconPath'))
# 设置图标大小
button.setIconSize(QSize(w, h))
# 设置工具按钮显示样式
button.setToolButtonStyle(Qt.ToolButtonStyle.'Style')
# Style Option
1. ToolButtonIconOnly: 只显示图标,不显示文本
2. ToolButtonTextOnly: 只显示文本,不显示图标
3. ToolButtonTextBesideIcon: 文本显示在图标旁边(默认样式)
4. ToolButtonTextUnderIcon: 文本显示在图标下方
5. ToolButtonFollowStyle: 根据当前样式自动选择显示模式
# 设置按钮大小
button.setFixedSize(w, h) # 固定大小
button.resize(w, h) # 大小
# 设置按钮为可选中
button.setCheckable(True)
# 点击信号插槽
button.clicked.connect('Method')
# 按钮样式
button.setStyleSheet('Style')
# 添加到组
buttonGroup.addButton(button)
# 鼠标悬停样式
button.setCursor(Qt.CursorShape.PointingHandCursor)
'''
默认箭头光标。
通常用于表示正常的指针状态。
Qt.CursorShape.CrossCursor：

十字光标。
常用于绘图应用程序或选择区域的情况。
Qt.CursorShape.WaitCursor：

等待光标（沙漏）。
表示程序正在处理某个操作，用户需要等待。
Qt.CursorShape.IBeamCursor：

文本光标（I-beam）。
通常用于文本编辑器，表示文本可以被选择或编辑。
Qt.CursorShape.SizeAllCursor：

全局移动光标。
表示可以移动对象或内容。
Qt.CursorShape.SizeVerCursor：

垂直调整大小光标。
表示可以向上或向下调整大小。
Qt.CursorShape.SizeHorCursor：

水平调整大小光标。
表示可以向左或向右调整大小。
Qt.CursorShape.SizeBDiagCursor：

斜向调整大小光标（右上到左下）。
表示可以在该方向上调整大小。
Qt.CursorShape.SizeFDiagCursor：

斜向调整大小光标（左上到右下）。
表示可以在该方向上调整大小。
Qt.CursorShape.PointingHandCursor：

手形光标。
通常用于表示可点击的元素，例如按钮或链接。
Qt.CursorShape.ForbiddenCursor：

禁止光标。
表示该操作不可用。
Qt.CursorShape.BusyCursor：

忙碌光标。
表示程序正在执行某项任务，无法进行其他操作。
'''
```

---

## 横向,纵向布局对象
```python
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import Qt
mainWidget = QWidget()
# 横向布局
hLayout = QHBoxLayout()
# 纵向布局
zLayout = QVBoxLayout()
# 添加控件
hLayout.addWidget('Widget')
zLayout.addWidget('Widget')
# 添加布局
hLayout.addLayout(zLayout)
# 设置布局对齐
hLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
zLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
self.setCentralWidget(mainWidget)
```

---

## 标签对象
```python
from PySide6.QtWidgets import QLabel
# 创建标签对象
label = QLable()
# 设置文本
label.setText('Text')
# 获取文本
label.text()
# 设置样式
label.setStyleSheet('Style')
```

---

## 进度条对象
```python
from PySide6.QtWidgets import QProgressBar
# 创建进度条对象
progressBar = QProgressBar()
# 设置默认值
progressBar.setValue(Value)
# 设置最小值
progressBar.setMinimum(Valeu)
# 设置最大值
progressBar.setMaximum(Valeu)
```

---

## 设置定时器
```python
from PySide6.QtCore import QTimer
# 创建定时器对象
timer = QTimer()
# 连接信号插槽
timer.timeout.connect('Method')
# 启动定时器
timer.start(Value) # Value 更新时间 毫秒
# 暂停定时器
timer.stop()
```

---

## 滑动条对象
```python
from PySide6.QtWidgets import QSlider
slider = QSlider()
slider = QSlider(Qt.Orientation.Horizontal) # 方向
# 设置最小值
slider.setMinimum(Value)
# 设置最大值
slider.setMaximum(Value)
# 默认值
slider.setValue(Value)
# 连接改变信号插槽
slider.valueChanged.connect('Method')
```

---

## 写入json文件

```python
import json

with open('filePath', 'w', encoding='utf-8') as f:
    json.dump({'key': Value}, f) # 写入json文件
# 写入多个数据
data = {
    'key1': Value,
    'key2': Value,
    'key3': Value,
}
with open('filePath', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4) # 格式化方式写入 indent 缩进

'''读取'''
with open('filePath', 'r', encoding='utf-8') as f:
    data = json.load(f)
```