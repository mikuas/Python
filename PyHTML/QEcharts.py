import time

from PySide6.QtWidgets import *
import tkinter as tk
from tkinter import filedialog
import random
import pyautogui
import pyperclip
from pyecharts.charts import Bar, Map, Timeline, Line
from pyecharts.options import LabelOpts, TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts, AxisOpts, DataZoomOpts


class Keyboard:

    @staticmethod
    def getCopy():
        return pyperclip.paste()

    @staticmethod
    def keyDown(*args):
        for i in range(len(args)):
            pyautogui.press(args[i])

    @staticmethod
    def inputText(text):
        pyautogui.typewrite(text)


class Echarts:

    @staticmethod
    def getLineChart(bools=True, **kwargs):
        """
        :param bools: T | F
        :param kwargs:
        x_data: list
        y_data: list
        title: str
        HTML_Name: Name
        :return:
        """
        line = (
            Line()
            .add_xaxis(kwargs['x_data'])
            .add_yaxis(kwargs['y_data'], kwargs['title'])
            .set_global_opts(
                title_opts=TitleOpts(title=kwargs['title']),
                legend_opts=LegendOpts(is_show=bools),
                tooltip_opts=TooltipOpts(is_show=bools),
                visualmap_opts=VisualMapOpts(is_show=bools)
            )
        ).render(kwargs['HTML_Name'])

    @staticmethod
    def getMap(**kwargs):
        """
        :param kwargs:
        data: [(), (), ...]
        title: str
        HTML_Name: str
        Name: China ...
        dicts: dist
        :return:
        """
        map = (
            Map()
            .add(kwargs['data'], kwargs['title'], kwargs['Name'])
            .set_global_opts(
                visualmap_opts=VisualMapOpts(
                    is_show=True,
                    is_piecewise=True,
                    pieces=[
                        {'min': kwargs['dicts'][0]['min'],
                         'max': kwargs['dicts'][0]['max'],
                         'label': kwargs['dicts'][0]['label'],
                         'color': kwargs['dicts'][0]['color']
                         },

                        {'min': kwargs['dicts'][1]['min'],
                         'max': kwargs['dicts'][1]['max'],
                         'label': kwargs['dicts'][1]['label'],
                         'color': kwargs['dicts'][1]['color']
                         },

                        {'min': kwargs['dicts'][2]['min'],
                         'max': kwargs['dicts'][2]['max'],
                         'label': kwargs['dicts'][2]['label'],
                         'color': kwargs['dicts'][2]['color']
                         },

                        {'min': kwargs['dicts'][3]['min'],
                         'label': kwargs['dicts'][3]['label'],
                         'color': kwargs['dicts'][3]['color']
                         },
                    ]
                )
            )
        ).render(kwargs['HTML_Name'])

    @staticmethod
    def getBar(reverse=False, **kwargs):
        """
        :param reverse: Bool
        :param kwargs:
        x_data: list
        y_data: list
        title: str
        dicts: dict
        position: position
        HTML_Name: str
        PT: *%
        angle: angle
        :return: bar
        """
        bar = (
            Bar()
            .add_xaxis(kwargs['x_data'])
            .add_yaxis(kwargs['title'], kwargs['y_data'], label_opts=LabelOpts(
                position=kwargs['position'],
            ))
            .set_global_opts(
                title_opts=TitleOpts(
                    title=kwargs['title'],
                ),
                xaxis_opts=AxisOpts(
                    axislabel_opts=LabelOpts(rotate=kwargs['angle'])
                ),
                datazoom_opts=DataZoomOpts(
                    is_show=True,
                    type_="slider",
                    orient="horizontal",
                    pos_top=kwargs['PT']
                ),
                visualmap_opts=VisualMapOpts(
                    is_show=True,
                    is_piecewise=True,
                    pieces=[
                        {'min': kwargs['dicts'][0]['min'],
                         'max': kwargs['dicts'][0]['max'],
                         'label': kwargs['dicts'][0]['label'],
                         'color': kwargs['dicts'][0]['color']
                         },

                        {'min': kwargs['dicts'][1]['min'],
                         'max': kwargs['dicts'][1]['max'],
                         'label': kwargs['dicts'][1]['label'],
                         'color': kwargs['dicts'][1]['color']
                         },

                        {'min': kwargs['dicts'][2]['min'],
                         'max': kwargs['dicts'][2]['max'],
                         'label': kwargs['dicts'][2]['label'],
                         'color': kwargs['dicts'][2]['color']
                         },

                        {'min': kwargs['dicts'][3]['min'],
                         'label': kwargs['dicts'][3]['label'],
                         'color': kwargs['dicts'][3]['color']
                         },
                    ]
                )
            )
        )
        if reverse:
            bar.reversal_axis()
        bar.render(kwargs['HTML_Name'])
        return bar

    @staticmethod
    def getTimeBar(**kwargs):
        """
        :param kwargs:
        timeline: -> Timeline()
        bars: list
        title: str
        HTML_Name: list: [Bool, Name]
        time: Number
        play, For: Bool
        :return: None
        """
        for i in range(len(kwargs['bars'])):
            kwargs['timeline'].add(kwargs['bars'][i], kwargs['title'])
        kwargs['timeline'].add_schema(
            play_interval=kwargs['time'],
            is_timeline_show=True,
            is_auto_play=kwargs['play'],
            is_loop_play=kwargs['For'],
        )
        if kwargs['HTML_Name'][0]:
            kwargs['timeline'].render(kwargs['HTML_Name'][1])

    @staticmethod
    def readFileTimeBar(reverse=False, **kwargs):
        """
        :param reverse: Bool
        :param kwargs:
        x_data: list
        dicts: dict
        line: int
        data: fileReadLines
        num: int
        echarts: -> Echarts()
        timeline: -> Timeline()
        time: int
        title: list
        position: str
        HTML_Name: str
        PT: *%
        angle: Number
        play, For: Bool
        :return:
        """
        for i in range(kwargs['line']):
            y_data = []
            for j in range(len(kwargs['data'])):
                y_data.append(int(kwargs['data'][j].split()[0]))
            if i == 0:
                y_data = y_data[:kwargs['num']:]
            else:
                y_data = y_data[kwargs['num'] - len(kwargs['x_data']):kwargs['num']]
            kwargs['num'] += 10
            print(y_data)
            result = kwargs['echarts'].getBar(
                angle=kwargs['angle'],
                PT=kwargs['PT'],
                reverse=reverse,
                dicts=kwargs['dicts'],
                x_data=kwargs['x_data'],
                y_data=y_data,
                title=str(kwargs['title'][len(kwargs['x_data']) - (i + 1)]) + 'GDP',
                HTML_Name=kwargs['HTML_Name'],
                position=kwargs['position'])
            if i == kwargs['line'] - 1:
                kwargs['echarts'].getTimeBar(
                    timeline=kwargs['timeline'],
                    bars=[result],
                    title=str(kwargs['title'][len(kwargs['x_data']) - (i + 1)]) + 'GDP',
                    HTML_Name=[True, kwargs['HTML_Name']],
                    time=kwargs['time'],
                    play=kwargs['play'],
                    For=kwargs['For']
                )
            kwargs['echarts'].getTimeBar(
                reverse=reverse,
                timeline=kwargs['timeline'],
                bars=[result],
                title=kwargs['title'][len(kwargs['x_data']) - (i + 1)],
                HTML_Name=[False, kwargs['HTML_Name']],
                time=kwargs['time'],
                play=kwargs['play'],
                For=kwargs['For']
            )


class Tools:

    @staticmethod
    def getRandom(start, end=None):
        if end is None:
            end = start
            start = 0
        return random.randint(start, end)

    @staticmethod
    def count(data: list, element):
        num = 0
        for i in range(len(data)):
            if element == data[i]:
                num += 1
        return num

    def writeNumber(self, path, lines, start, end=None, mode='a', coding='utf-8'):
        file = open(path, mode, encoding=coding)

        for i in range(lines):
            if i == lines - 1:
                file.write(str(self.getRandom(start, end)))
            else:
                file.write(f"{str(self.getRandom(start, end)) + '\n'}")

    def getRandomColor(self, types=False):
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
        color = '#'
        rgb = 'rgb('
        if types:
            for i in range(6):
                color += str(random.choice(data))
            return color
        else:
            return f"{
                rgb + str(self.getRandom(255)) + ',' + str(self.getRandom(255)) + ',' + str(self.getRandom(255)) + ')'
            }"


class Miku:

    def __init__(self, app_title='Echarts', win_width=500, win_height=200):
        self.x_data_path = None
        self.y_data_path = None
        # 创建主窗口对象
        self.window = QMainWindow()
        # 设置窗口的大小
        self.window.resize(win_width, win_height)
        # 设置窗口显示的位置
        self.window.move(600, 400)
        # 设置窗口的标题
        self.window.setWindowTitle(app_title)

        self.win_width = win_width
        self.win_height = win_height
        self.rError = QMessageBox(self.window)
        self.wError = QMessageBox(self.window)

        self.box = QMessageBox(self.window)
        self.info = QMessageBox(self.window)

        # 设置按钮
        self.button = QPushButton('执行', self.window)
        self.button.move(win_width * 0.6, win_height * 0.3)
        # set button size
        self.button.setFixedSize(100, 50)

        self.ibt = QPushButton('读取', self.window)
        self.ibt.move(500, 200)
        self.ibt.clicked.connect(self.index)
        self.ibt.setFixedSize(100, 50)

        self.x_path = QPushButton('选择x轴数据', self.window)
        self.x_path.move(20, 20)
        self.x_path.setFixedSize(150, 50)

        self.y_path = QPushButton('选择y轴数据', self.window)
        self.y_path.move(20, 100)
        self.y_path.setFixedSize(150, 50)
        # 按钮点击事件
        self.button.clicked.connect(self.all)

        self.x_path.clicked.connect(self.x_file)
        self.y_path.clicked.connect(self.y_file)

        self.info = QMessageBox(self.window)
        self.info.resize(100, 100)
        self.info.move(win_width + 280, win_height + 220)

        self.x_data = []
        self.y_data = []

        self.my_dict = {}

        self.title = []

    def all(self):
        self.index()
        self.start()

    def x_file(self):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        # 让用户选择文件
        self.x_data_path = filedialog.askopenfilename(
            title="打开文件",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # 文件类型过滤器
        )
        root.destroy()  # 销毁主窗口

    def y_file(self):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        # 让用户选择保存文件的路径
        self.y_data_path = filedialog.askopenfilename(
            title="打开文件",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # 文件类型过滤器
        )
        root.destroy()  # 销毁主窗口

    def my_dicts(self):
        color = Tools()

        start = 0
        end = 4000
        for i in range(4):
            self.my_dict[i] = {}
            self.my_dict[i]['min'] = start
            self.my_dict[i]['max'] = end
            self.my_dict[i]['label'] = f'{start}-{end}'
            self.my_dict[i]['color'] = color.getRandomColor(True)
            if start == 0:
                start += end + 1
            else:
                start += 4000
            end += 4000

    def getTitle(self):
        date = 2024

        for i in range(len(self.x_data)):
            self.title.append(str(date) + '年')
            date -= 1

    def x_read(self):

        file = open(self.x_data_path, 'r', encoding='utf-8')
        self.x_data = []
        file = file.readlines()
        for i in range(len(file)):
            self.x_data.append(file[i].split()[0])

    def index(self):
        self.getTitle()
        self.my_dicts()
        self.x_read()

    def start(self):
        try:

            if self.x_data_path is None:
                self.info.show()
                self.info.setInformativeText('请选择文件!')
            elif self.y_data_path is None:
                self.info.show()
                self.info.setInformativeText('请选择文件!')
            elif self.x_data_path is not None and self.y_data_path is not None:
                echarts = Echarts()
                file = open(self.y_data_path, 'r', encoding='utf-8')
                data = file.readlines()
                timeline = Timeline()
                timeline.width = '1200px'
                timeline.height = '600px'
                print(len(self.x_data))
                echarts.readFileTimeBar(
                    x_data=self.x_data,
                    dicts=self.my_dict,
                    line=len(self.x_data),
                    data=data,
                    num=len(self.x_data),
                    echarts=echarts,
                    title=self.title,
                    timeline=timeline,
                    time=1000,
                    position='top',
                    HTML_Name='index.html',
                    PT='1%',
                    angle=45,
                    play=True,
                    For=True
                )
                self.info.show()
                self.info.setInformativeText('执行完毕!')
        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication([])
    stats = Miku()
    stats.window.show()
    app.exec()


