## PySide6

~~~python
from PySide6.QtWidgets import QLabel, QMenuBar, QWidget, QComboBox, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QMainWindow, QPlainTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap


class Window(QWidget):

    def __init__(self, path):
        super().__init__()
        self.path = path
        # 创建主窗口对象
        self.window = QMainWindow()
        # 设置窗口大小
        self.window.resize(300, 200)
        # 设置窗口显示位置
        self.window.move(500, 500)
        # 设置窗口标题
        self.window.setWindowTitle('Title')
        # 设置窗口始终位于前方
        # self.window(Qt.WindowStaysOnTopHint)
        self.window(Qt.WindowType.WindowStaysOnTopHint)
        # 设置窗口位于前方
        self.window.raise_()
        # 激活窗口
        self.window.activateWindow()
        
        # 创建标签
        self.label = QLabel('Selector')
    
        # 创建下拉菜单
        self.comboBox = QComboBox()
        # 添加内容
        self.comboBox.addItem('element')
        # 获取当前内容
        self.comboBox.currentText()

        # 设置文本控件
        self.textEdit = QPlainTextEdit(self.window)
        # 设置提示内容
        self.textEdit.setPlaceholderText('Text')
        # 文本控件位置
        self.textEdit.move(200, 200)
        # 文本控件大小
        self.textEdit.resize(100, 50)
        # 设置只读
        self.textEdit.setReadOnly(True)
        '''获取文本控件内容'''
        self.info = self.textEdit.toPlainText()

        self.textCommand = QLineEdit()
        # 获取内容
        self.info = self.textCommand.text()
        
        # 设置按钮
        self.button = QPushButton('Name', self.window)
        # 设置悬停为点击手势
        1. Qt.CursorShape.ArrowCursor：标准箭头光标。
        2. Qt.CursorShape.PointingHandCursor：手形光标。
        3. Qt.CursorShape.IBeamCursor：文本输入光标。
        4. Qt.CursorShape.CrossCursor：十字光标。
        5. Qt.CursorShape.WaitCursor：等待（沙漏）光标。
        
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)
        # 设置按钮背景颜色
        self.button.setStyleSheet("background-color: COLOR")
        # 设置按钮背景图片
        self.button.setStyleSheet(
            """
            QPushButton {
                border: none;
                background-image: url(ImagePath);
                background-repeat: no-repeat;
                background-position: center;
            }
            """
        )
        # 设置字体大小
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;           /* 设置字体大小为16点 */
                font-family: Arial;        /* 设置字体为Arial */
                font-weight: bold;         /* 设置字体粗细为加粗 */
                color: #333333;            /* 设置字体颜色 */
            }
        """)
        # 设置单独样式
        self.button.setObjectName('button')
        """
                QPushButton#button {
                    background-color: pink;
                    font-size: 40px;
                }
                QPushButton#button:hover {
                    background-color: aqua;
                }
        """

        # 设置按钮大小
        self.button.resize(50, 20)
        # 设置按钮位置
        self.button.move(100, 100)
        # 按钮点击事件
        self.button.clicked.connect('function')

        # 创建菜单栏'
        menuBar = self.menuBar()
        # menuBar = QMenuBar(self)
        # window.setMenuBar(menuBar)
        # 添加菜单
        fileMenu = menuBar.addMenu("file")
        # fileMenu = menuBar.addMenu("file")
        
        # 添加菜单项
        newAction = QAction("New", self)
        fileMenu.addAction(newAction)
        # newAction = QAction("New", window)
        # fileMenu.addAction(newAction)
        
        # 连接信号与槽
        newAction.triggered.connect(self.click)

        # 列表空间
        # 创建 QListWidget
        self.list_widget = QListWidget()
        self.list_widget.addItems(["项 1", "项 2", "项 3"])  # 添加项
        # 获取选中的项
        result = self.list_widget.selectedItems()
        
        # 多个选项卡之间切换的 Qt 小部件
        # 创建 QTabWidget 实例
        self.tab_widget = QTabWidget()
        # 创建不同的标签页
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        # 将标签页添加到 QTabWidget
        self.tab_widget.addTab(self.tab1, "标签 1")
        self.tab_widget.addTab(self.tab2, "标签 2")
        
        # 数字输入框
        # 创建 QSpinBox 实例
        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(0)  # 设置最小值
        self.spin_box.setMaximum(100)  # 设置最大值
        self.spin_box.setValue(50)  # 设置默认值
        
        # 获取当前值
        self.spin_box.value()
         # 更新标签内容
        self.label.setText(f"当前值: {self.spin_box.value()}")
        
        # 滑动条
        # 创建 QSlider 实例
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        
        # 自定义样式表
        self.slider.setStyleSheet("""
            QSlider {
                background: #ddd;  /* 背景颜色 */
            }
            QSlider::handle {
                background: #0078d7; /* 滑块颜色 */
                border: 2px solid #0056a3; /* 滑块边框 */
                width: 20px; /* 滑块宽度 */
                height: 20px; /* 滑块高度 */
                margin: -10px 0; /* 滑块边距 */
            }
            QSlider::groove:horizontal {
                background: #ccc; /* 导轨颜色 */
                height: 8px; /* 导轨高度 */
            }
            QSlider::groove:horizontal:pressed {
                background: #aaa; /* 按下时的导轨颜色 */
            }
        """)
        
        # 进度条
        # 创建 QProgressBar 实例
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        # 自定义样式表
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #0078d7; /* 边框颜色 */
                border-radius: 5px; /* 圆角边框 */
                text-align: center; /* 文本居中 */
                background-color: #ddd; /* 背景颜色 */
            }
            QProgressBar::chunk {
                background-color: #0078d7; /* 进度条颜色 */
                border-radius: 5px; /* 圆角 */
            }
        """)
        def start_progress(self):
            self.progress_bar.setValue(0)  # 重置进度条
            self.thread = Thread(target=self.run_progress)
            self.thread.start()

        def run_progress(self):
            for i in range(101):
                time.sleep(0.1)  # 模拟长时间操作
                self.progress_bar.setValue(i)  # 更新进度条的值
                
        # 分组相关空间
        # 创建第一个 QGroupBox
        group_box1 = QGroupBox("选择你的性别")
        gender_layout = QVBoxLayout()
        self.male_radio = QRadioButton("男")
        self.female_radio = QRadioButton("女")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        group_box1.setLayout(gender_layout)
        
        # 创建第二个 QGroupBox
        group_box2 = QGroupBox("爱好")
        hobby_layout = QVBoxLayout()
        self.sports_checkbox = QCheckBox("运动")
        self.music_checkbox = QCheckBox("音乐")
        self.reading_checkbox = QCheckBox("阅读")
        hobby_layout.addWidget(self.sports_checkbox)
        hobby_layout.addWidget(self.music_checkbox)
        hobby_layout.addWidget(self.reading_checkbox)
        group_box2.setLayout(hobby_layout)

        # 工具栏
        # 创建工具栏
        self.tool_bar = QToolBar("工具栏", self)
        self.addToolBar(self.tool_bar)
        # 创建工具栏操作
        self.action1 = QAction("操作 1", self)
        self.action1.triggered.connect(self.perform_action1)
        self.tool_bar.addAction(self.action1)

        self.action2 = QAction("操作 2", self)
        self.action2.triggered.connect(self.perform_action2)
        self.tool_bar.addAction(self.action2)

        self.tool_bar.addSeparator()  # 添加分隔符

        self.action3 = QAction("退出", self)
        self.action3.triggered.connect(self.close)
        self.tool_bar.addAction(self.action3)
        
        # 显示层级结构目录
        # 创建 QTreeWidget
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabel("树形结构")
         # 添加树节点
        root_item = QTreeWidgetItem(self.tree_widget, ["根节点"])
        child_item1 = QTreeWidgetItem(root_item, ["子节点 1"])
        child_item2 = QTreeWidgetItem(root_item, ["子节点 2"])
        # 添加更深层次的子节点
        grandchild_item = QTreeWidgetItem(child_item1, ["孙节点 1"])

        # 展开树节点
        root_item.setExpanded(True)
        
        # 选择框
        # 创建 QCheckBox
        self.check_box = QCheckBox("我同意使用条款", self)
        self.check_box.stateChanged.connect(self.on_check_state_change)  # 连接信号
        def on_check_state_change(self, state):
        # 根据复选框的状态更新标签文本
        if state == 0:  # 复选框未选中
            self.label.setText("未选中")
        else:  # 复选框选中
            self.label.setText("已选中")
        
        # 单一选项控件
        # 创建 QRadioButton
        self.radio_button1 = QRadioButton("选项 1", self)
        self.radio_button2 = QRadioButton("选项 2", self)
        self.radio_button3 = QRadioButton("选项 3", self)
        # 连接信号
        self.radio_button1.toggled.connect(self.on_radio_button_toggled)
        self.radio_button2.toggled.connect(self.on_radio_button_toggled)
        self.radio_button3.toggled.connect(self.on_radio_button_toggled)
        # 创建标签用于显示选择的选项
        self.label = QLabel("未选择任何选项", self)
            def on_radio_button_toggled(self):
        # 检查哪个单选按钮被选中并更新标签文本
        if self.radio_button1.isChecked():
            self.label.setText("已选择：选项 1")
        elif self.radio_button2.isChecked():
            self.label.setText("已选择：选项 2")
        elif self.radio_button3.isChecked():
            self.label.setText("已选择：选项 3")
        else:
            self.label.setText("未选择任何选项")
        
        # 调节窗口大小分隔符
        # 创建 QSplitter
        splitter = QSplitter(self)
        # 创建两个 QTextEdit 控件
        text_edit1 = QTextEdit("左侧文本编辑器")
        text_edit2 = QTextEdit("右侧文本编辑器")
        # 将控件添加到 QSplitter
        splitter.addWidget(text_edit1)
        splitter.addWidget(text_edit2)
    
        # 选择日期
        # 创建 QCalendarWidget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)  # 设置网格可见
        # 创建标签用于显示选择的日期
        self.label = QLabel("选择的日期将显示在这里", self)

        # 连接信号
        self.calendar.clicked.connect(self.on_date_selected)
            def on_date_selected(self, date):
        # 更新标签显示选择的日期
        self.label.setText(f"选择的日期：{date.toString()}")
            
        # 日期输入控件
        # 创建中心窗口部件
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 创建垂直布局
        layout = QVBoxLayout(self.central_widget)

        # 创建 QDateTimeEdit 控件
        self.date_time_edit = QDateTimeEdit(self)
        self.date_time_edit.setDateTime(QDateTime.currentDateTime())  # 设置当前日期时间
        self.date_time_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置显示格式

        # 创建标签用于显示选择的日期时间
        self.label = QLabel("选择的日期和时间将显示在这里", self)
        # 连接信号
        self.date_time_edit.dateTimeChanged.connect(self.on_date_time_changed)

        # 将控件添加到布局
        layout.addWidget(self.date_time_edit)
        layout.addWidget(self.label)

        def on_date_time_changed(self, date_time):
            # 更新标签显示选择的日期和时间
            self.label.setText(f"选择的日期和时间：{date_time.toString()}")
   
        
        # 创建布局管理器并设置布局
        layout = QVBoxLayout(self)  # 创建一个垂直布局管理器，并将其绑定到当前窗口（self）上
        layout.addWidget(self.textEdit)  # 将文本输入框 (self.textEdit) 添加到垂直布局中
        layout.addWidget(self.textCommand)  # 将命令输入框 (self.textCommand) 添加到垂直布局中
        layout.addWidget(self.button)  # 将按钮 (self.button) 添加到垂直布局中

        self.setLayout(layout)
        
        QMessageBox.warning(self, '弹出警告窗口', 'Text')
        QMessageBox.information(self, '弹出提示窗口', 'Text')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(100, 50)
        self.setMaximumSize(500, 100)
        # Set the central widget of the Window.
        self.setCentralWidget(QPushButton('button'))
        '''
        setFixedSize()可以调用.setMinimumSize()和.setMaximumSize()分别设置最小和最大尺寸
        '''
        
    '''忽略窗口关闭'''
    def closeEvent(self, event):
        # 重载关闭事件，使得窗口关闭时只是隐藏而不是退出应用程序
        event.ignore()  # 忽略关闭事件
        self.hide()     # 隐藏窗口
        
    '''忽略多个窗口关闭'''
    @staticmethod
    def ignoreCloseEvent(event, window):
        event.ignore()
    # 使用lambda
    window1 = QWidget()
    window2 = QWidget()
    window1.closeEvent = lambda event: ignoreCloseEvent(event, window1.hide())
    window2.closeEvent = lambda event: ignoreCloseEvent(event, window2.hide())
    
# 系统托盘
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

class systemIcon(QMainWindow, Window):
    def __init__(self):
        super().__init__()
        # 添加系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        print('System tray icon created')  # 添加调试输出

        self.tray_icon.setIcon(QIcon(self.path))
        self.tray_icon.setToolTip('后台运行示例')

        # 托盘图标菜单
        tray_menu = QMenu()
        show_action_tray = QAction('显示窗口', self)
        # 添加托盘点击事件
        self.tray_icon.activated.connect(lambda: None)
        # 判断点击
        # 左键单击 lambda reason: if reason == QSystemTrayIcon.Trigger:  # 左键单击
        # 左键双击 lambda reason: if reason == QSystemTrayIcon.DoubleClick:  # 左键双击
        
        show_action_tray.triggered.connect(self.showWindow)
        # tray_menu.addAction(show_action_tray)

        tray_menu.addSeparator()

        quit_action = QAction('退出', self)
        quit_action.triggered.connect(self.quitWindow)
        # tray_menu.addAction(quit_action)

        tray_menu.addActions([show_action_tray, quit_action])
        self.tray_icon.setContextMenu(tray_menu)

        # 显示系统托盘图标
        self.tray_icon.show()
        
    # 设置背景图片
    @staticmethod
    def setBackground(imagePath):
        # 创建调色板
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap(imagePath)))
        return palette
        
    def showWindow(self):
        self.show()
        
    @staticmethod
    def quitWindow(): 
        QApplication.quit()
        
if __name__ == '__main__':
    import os
    app = QApplication(sys.argv)
    # 获取打包后的可执行文件所在的临时目录
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    # 构建视频文件的绝对路径
    file_path = os.path.join(base_path, 'fileName')
    
    win = Window(file_path)
    win.window.show()
    app.exec()
~~~
### 设置布局
~~~python
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PySide6.QtGui import QPainter, QPixmap
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        # 创建主部件和主布局
        main_widget = QWidget()
        # 垂直布局
        main_layout = QVBoxLayout()

        # 创建QHBoxLayout并在其中添加两个按钮
        # 水平布局
        h_layout = QHBoxLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # 设置按钮最大大小
        button1.setMaximumSize(500, 200)  
        button2.setMaximumSize(500, 200)        
    
        # 设置按钮的大小策略，使其在窗口大小改变时调整高度
        button1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        h_layout.addWidget(button1)
        h_layout.addWidget(button2)

        # 将QHBoxLayout添加到QVBoxLayout
        main_layout.addLayout(h_layout)

        # 设置主部件的布局
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        """设置一张背景图片平铺"""
        
        window.background_pixmap = QPixmap(imagePath)
        
        def paintEvent(self, event):
            # 创建 QPainter 对象
            painter = QPainter(self)
    
            # 获取窗口的宽度和高度
            window_width = self.width()
            window_height = self.height()
    
            # 将背景图片缩放到窗口大小
            scaled_pixmap = self.background_pixmap.scaled(window_width, window_height)
    
            # 在窗口内绘制缩放后的背景图片
            painter.drawPixmap(0, 0, scaled_pixmap)
        
        '''清晰一点'''
        def paintEvent(self, event):
            # 创建 QPainter 对象
            painter = QPainter(self)
    
            # 获取窗口的宽度和高度
            window_width = self.width()
            window_height = self.height()
    
            # 将背景图片缩放到窗口大小，并使用平滑转换模式
            scaled_pixmap = self.background_pixmap.scaled(
                window_width, window_height, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
    
            # 在窗口内绘制缩放后的背景图片
            painter.drawPixmap(0, 0, scaled_pixmap)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()

~~~


