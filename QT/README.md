## QT

~~~python
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QMainWindow, QPlainTextEdit
from PySide6.QtCore import QTimer, Qt
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

        # 设置文本控件
        self.textEdit = QPlainTextEdit(self.window)
        # 设置提示内容
        self.textEdit.setPlaceholderText('Text')
        # 文本控件位置
        self.textEdit.move(200, 200)
        # 文本控件大小
        self.textEdit.resize(100, 50)
        '''获取文本控件内容'''
        self.info = self.textEdit.toPlainText()

        self.textCommand = QLineEdit()
        # 获取内容
        self.info = self.textCommand.text()
        
        # 设置按钮
        self.button = QPushButton('Name', self.window)
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

        # 设置按钮大小
        self.button.resize(50, 20)
        # 设置按钮位置
        self.button.move(100, 100)
        # 按钮点击事件
        self.button.clicked.connect('function')
        
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
    # 使用
    window1 = QWidget()
    window2 = QWidget()
    window1.closeEvent = lambda event: ignoreCloseEvent(event, window1)
    window2.closeEvent = lambda event: ignoreCloseEvent(event, window2)
    
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
        palette.setBrush(QPalette.Window, QBrush(QPixmap(imagePath)))
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
        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

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
        def paintEvent(self,event):
            # 创建 QPainter 对象
            painter = QPainter(self)
    
            # 获取窗口的宽度和高度
            window_width = self.width()
            window_height = self.height()
    
            # 将背景图片缩放到窗口大小，并使用平滑转换模式
            scaled_pixmap = self.background_pixmap.scaled(
                window_width, window_height, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    
            # 在窗口内绘制缩放后的背景图片
            painter.drawPixmap(0, 0, scaled_pixmap)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()

~~~


