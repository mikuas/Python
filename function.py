import random
import pyautogui
import pyperclip
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.faker import Faker


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

    def getDict(self, lens, start, end=None):
        if end is None:
            end = start
            start = 0
        my_dict = {}
        add = None
        for i in range(lens):
            if i == lens - 1:
                my_dict[i] = {}
                my_dict[i]['min'] = start
                my_dict[i]['label'] = f'{start}-{end}'
                my_dict[i]['color'] = self.getRandomColor(True)
            else:
                my_dict[i] = {}
                my_dict[i]['min'] = start
                my_dict[i]['max'] = end
                my_dict[i]['label'] = f'{start}-{end}'
                my_dict[i]['color'] = self.getRandomColor(True)
            if start == 0:
                start += end + 1
                add = end
            else:
                start += add
            end += add
        return my_dict



