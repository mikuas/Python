import random
import pyautogui
import pyperclip
from pyecharts.charts import *
from pyecharts.options import *


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
        :param kwargs: x_data, y_data, title, HTML_Name
        :return:
        """
        line = Line()
        line.add_xaxis(kwargs['x_data'])
        line.add_yaxis(kwargs['title'], kwargs['y_data'])
        line.set_global_opts(
            title_opts=TitleOpts(title=kwargs['title']),
            legend_opts=LegendOpts(is_show=bools),
            tooltip_opts=TooltipOpts(is_show=bools),
            visualmap_opts=VisualMapOpts(is_show=bools)
        )

        line.render(kwargs['HTML_Name'])

    @staticmethod
    def getMap(**kwargs):
        """
        :param kwargs: data, title HTML_Name, Name dicts
        :return:
        """
        map = Map()
        map.add(kwargs['data'], kwargs['title'], kwargs['Name'])
        if kwargs['set']:
            map.set_global_opts(
                visualmap_opts=VisualMapOpts(
                    is_show=True,
                    is_piecewise=True,
                    pieces=[
                        {'min': kwargs['dicts'][0]['min'],
                         'max': kwargs['dicts'][0]['max'],
                         'label': kwargs['dicts'][0]['label'],
                         'color': kwargs['dicts'][0]['color']},

                        {'min': kwargs['dicts'][1]['min'],
                         'max': kwargs['dicts'][1]['max'],
                         'label': kwargs['dicts'][1]['label'],
                         'color': kwargs['dicts'][1]['color']},

                        {'min': kwargs['dicts'][2]['min'],
                         'max': kwargs['dicts'][2]['max'],
                         'label': kwargs['dicts'][2]['label'],
                         'color': kwargs['dicts'][2]['color']},

                        {'min': kwargs['dicts'][3]['min'],
                         'label': kwargs['dicts'][3]['label'],
                         'color': kwargs['dicts'][3]['color']},
                    ]
                )
            )
        map.render(kwargs['HTML_Name'])

    @staticmethod
    def getBar(reverse=False, **kwargs):
        """
        :param reverse: T | F
        :param kwargs: x_data, y_data, title, dicts, position, HTML_Name
        :return: bar
        """
        bar = Bar()
        bar.add_xaxis(kwargs['x_data'])
        bar.add_yaxis(kwargs['title'], kwargs['y_data'], label_opts=LabelOpts(
            position=kwargs['position'] or 'right'
        ))

        bar.set_global_opts(
            visualmap_opts=VisualMapOpts(
                is_show=True,
                is_piecewise=True,
                pieces=[
                        {'min': kwargs['dicts'][0]['min'],
                         'max': kwargs['dicts'][0]['max'],
                         'label': kwargs['dicts'][0]['label'],
                         'color': kwargs['dicts'][0]['color']},

                        {'min': kwargs['dicts'][1]['min'],
                         'max': kwargs['dicts'][1]['max'],
                         'label': kwargs['dicts'][1]['label'],
                         'color': kwargs['dicts'][1]['color']},

                        {'min': kwargs['dicts'][2]['min'],
                         'max': kwargs['dicts'][2]['max'],
                         'label': kwargs['dicts'][2]['label'],
                         'color': kwargs['dicts'][2]['color']},

                        {'min': kwargs['dicts'][3]['min'],
                         'label': kwargs['dicts'][3]['label'],
                         'color': kwargs['dicts'][3]['color']},
                ]
            )
        )
        if reverse:
            bar.reversal_axis()
        bar.render(kwargs['HTML_Name'])
        return bar

    @staticmethod
    def getTimeBar(**kwargs):
        """
        :param kwargs: Timeline, bar, bars, title, HTML_Name, time, play, For,
        :return: None
        """
        for i in range(len(kwargs['bars'])):
            kwargs['Timeline'].add(kwargs['bars'][i], kwargs['title'])
        kwargs['Timeline'].add_schema(
            play_interval=kwargs['time'],
            is_timeline_show=True,
            is_auto_play=kwargs['play'],
            is_loop_play=kwargs['For']
        )
        if kwargs['HTML_Name'][0]:
            kwargs['Timeline'].render(kwargs['HTML_Name'][1])

    @staticmethod
    def readFileTimeBar(reverse=False, **kwargs):
        """
        :param reverse: T | F
        :param kwargs: line, data, num, time, dicts, echarts, x_data, timeline, play, For, title, HTML_Name, position
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
                reverse=reverse,
                dicts=kwargs['dicts'],
                x_data=kwargs['x_data'],
                y_data=y_data,
                title=kwargs['title'],
                HTML_Name=kwargs['HTML_Name'],
                position=kwargs['position'])
            if i == kwargs['line'] - 1:
                kwargs['echarts'].getTimeBar(
                    Timeline=kwargs['timeline'],
                    bars=[result], title=kwargs['title'],
                    HTML_Name=[True, kwargs['HTML_Name']],
                    time=kwargs['time'], play=kwargs['play'], For=kwargs['For']
                )
            kwargs['echarts'].getTimeBar(
                reverse=reverse,
                Timeline=kwargs['timeline'],
                bars=[result],
                title=kwargs['title'],
                HTML_Name=[False, kwargs['HTML_Name']],
                time=kwargs['time'],
                play=kwargs['play'],
                For=kwargs['For']
            )


class Random:

    @staticmethod
    def getRandom(start, end=None):
        if end is None:
            end = start
            start = 0
        return random.randint(start, end + 1)

    @staticmethod
    def count(data: list, element):
        num = 0
        for i in range(len(data)):
            if element == data[i]:
                num += 1
        return num


class FileIO:

    def __init__(self):
        self.fc = Random()

    def writeNumber(self, path, lines, start, end=None, mode='a', coding='utf-8'):
        file = open(path, mode, encoding=coding)

        for i in range(lines):
            if i == lines - 1:
                file.write(str(self.fc.getRandom(start, end)))
            else:
                file.write(f"{str(self.fc.getRandom(start, end)) + '\n'}")

