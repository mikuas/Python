import random
import pyautogui
import pyperclip
from pyecharts.charts import *
from pyecharts.options import *


class Miku:
    # tp T return: list | F return: dict

    @staticmethod
    def Keyboard(tp=False):

        def getCopy():
            return pyperclip.paste()

        def keyDown(*args):
            """
            :param args: keys OR key + key
            :return: None
            """
            for i in range(len(args)):
                pyautogui.press(args[i])

        def inputText(text):
            """
            :param text: Text to be inputted
            :return: None
            """
            pyautogui.typewrite(text)

        if tp:
            return [getCopy, keyDown, inputText]
        else:
            return {'getCopy': getCopy, 'keyDown': keyDown, 'keyUp': keyDown}

    @staticmethod
    def Echarts(tp=False):

        def getLineChart(**kwargs):
            """
            :param kwargs:
            [line: Line()]
            x_data: list
            y_data: list
            title: str
            global: Bool
            dicts: dict[4]
            HTML_Name: fileName
            :return: None
            """
            if kwargs['line'] is None:
                line = Line()
                line.add_xaxis(kwargs['x_data']),
                line.add_yaxis(kwargs['title'], kwargs['y_data']),
                line.set_global_opts(
                    title_opts=TitleOpts(
                        title=kwargs['title']
                    ),
                    legend_opts=LegendOpts(
                        is_show=True
                    ),
                    toolbox_opts=ToolboxOpts(
                        is_show=True
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=kwargs['global'],
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

                line.render(kwargs['HTML_Name'])
            else:
                kwargs['line'].add_xaxis(kwargs['x_data']),
                kwargs['line'].add_yaxis(kwargs['title'], kwargs['y_data'])
                kwargs['line'].setglobal_opts(
                    title_opts=TitleOpts(
                        title=kwargs['title']
                    ),
                    legend_opts=LegendOpts(
                        is_show=True
                    ),
                    toolbox_opts=ToolboxOpts(
                        is_show=True
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=kwargs['global'],
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
                kwargs['line'].render(kwargs['HTML_Name'])

        def getMap(**kwargs):
            """
            :param kwargs:
            [map: Map()]
            data: type:[(), (), ...]
            title: str
            MapName: str
            global: Bool
            dicts: dict[4]
            HTML_Name: fileName
            :return: None
            """
            if kwargs['map'] is None:
                map = Map()
                map.add(kwargs['data'], kwargs['title'], kwargs['MapName'])
                map.set_global_opts(
                    title_opts=TitleOpts(
                        title=kwargs['title']
                    ),
                    legend_opts=LegendOpts(
                        is_show=True
                    ),
                    toolbox_opts=ToolboxOpts(
                        is_show=True
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=kwargs['global'],
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
                map.render(kwargs['HTML_Name'])

            else:
                kwargs['map'].add(kwargs['data'], kwargs['title'], kwargs['MapName'])
                kwargs['map'].setglobal_opts(
                    title_opts=TitleOpts(
                        title=kwargs['title']
                    ),
                    legend_opts=LegendOpts(
                        is_show=True
                    ),
                    toolbox_opts=ToolboxOpts(
                        is_show=True
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=kwargs['global'],
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
                kwargs['map'].render(kwargs['HTML_Name'])

        def getBar(reverse=False, **kwargs):
            """
            :param reverse: Bool
            :param kwargs:
            [bar: Bar()]
            x_data: list
            y_data: list
            title: str
            global: Bool
            position: location:str
            PT: 1% - 100%
            dicts: dict[4]
            HTML_Name: fileName
            :return: bar | kwargs['bar']
            """
            if kwargs['bar'] is None:
                bar = Bar()
                bar.add_xaxis(kwargs['x_data'])
                bar.add_yaxis(
                    kwargs['title'],
                    kwargs['y_data'],
                    label_opts=LabelOpts(
                        position=kwargs['position']
                    )
                )
                bar.set_global_opts(
                    title_opts=TitleOpts(
                        title=kwargs['title']
                    ),
                    xaxis_opts=AxisOpts(
                        axislabel_opts=LabelOpts(rotate=45)
                    ),
                    datazoom_opts=DataZoomOpts(
                        is_show=True,
                        type_='slider',
                        orient='horizontal',
                        pos_top=kwargs['PT']
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=kwargs['global'],
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
                if reverse:
                    bar.reversal_axis()
                bar.render(kwargs['HTML_Name'])
                return bar
            else:
                kwargs['bar'].add(kwargs['data'], kwargs['title'], kwargs['MapName'])
                kwargs['bar'].add_xaxis(kwargs['x_data'])
                kwargs['bar'].add_yaxis(
                    kwargs['title'],
                    kwargs['y_data'],
                    label_opts=LabelOpts(
                        position=kwargs['position']
                    )
                )
                kwargs['bar'].set_global_opts(
                    title_opts=TitleOpts(
                        title=kwargs['title']
                    ),
                    xaxis_opts=AxisOpts(
                        axislabel_opts=LabelOpts(rotate=45)
                    ),
                    datazoom_opts=DataZoomOpts(
                        is_show=True,
                        type_='slider',
                        orient='horizontal',
                        pos_top='1%'
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=kwargs['global'],
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
                if reverse:
                    kwargs['bar'].reverse_axis()
                kwargs['bar'].render(kwargs['HTML_Name'])
                return kwargs['bar']

        def getTimeBar(**kwargs):
            """
            :param kwargs:
            bars: [bar1, bar2, ...]
            Timeline: Timeline()
            title: str
            HTML_Name: Bool str
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

        def readLinesFileTimeBar(reverse=False, **kwargs):
            """
            :param reverse: Bool
            :param kwargs:
            line: line
            data: fileData
            num: y_data_Length
            x_data: list
            bar: bar -> Bar()
            dicts: dict[4]
            title: str
            HTML_Name: Bool str
            time: Time: Int
            play: Play: Bool
            For: Bool
            :return: None
            """
            for i in range(kwargs['line']):
                y_data = []
                for j in range(len(kwargs['data'])):
                    y_data.append(kwargs['data'][j].split()[0])
                if i == 0:
                    y_data = y_data[:kwargs['num']:]
                else:
                    y_data = y_data[kwargs['num'] - len(kwargs['x_data']):kwargs['num']]
                kwargs['num'] += 10

                print(y_data)
                result = kwargs['bar'].getBar(
                    reverse=reverse,
                    dicts=kwargs['dicts'],
                    x_data=kwargs['x_data'],
                    y_data=y_data,
                    title=str(kwargs['title'][len(kwargs['x_data']) - (i + 1)]) + '年GDP',
                    HTML_Name=kwargs['HTML_Name'],
                    position=kwargs['position'])
                if i == kwargs['line'] - 1:
                    kwargs['bar'].getTimeBar(
                        Timeline=kwargs['timeline'],
                        bars=[result],
                        title=str(kwargs['title'][len(kwargs['x_data']) - (i + 1)]) + '年GDP',
                        HTML_Name=[True, kwargs['HTML_Name']],
                        time=kwargs['time'],
                        play=kwargs['play'],
                        For=kwargs['For']
                    )
                kwargs['bar'].getTimeBar(
                    reverse=reverse,
                    Timeline=kwargs['timeline'],
                    bars=[result],
                    title=kwargs['title'][len(kwargs['x_data']) - (i + 1)],
                    HTML_Name=[False, kwargs['HTML_Name']],
                    time=kwargs['time'],
                    play=kwargs['play'],
                    For=kwargs['For']
                )

        if tp:
            return [getLineChart, getMap, getBar, getTimeBar, readLinesFileTimeBar]
        else:
            return {
                'getLineChart': getLineChart, 'getMap': getMap, 'getBar': getBar,
                'getTimeBar': getTimeBar, 'readLinesFileTimeBar': readLinesFileTimeBar
            }

    @staticmethod
    def Random(tp=False):

        def getRandom(start, end=None):
            """
            :param start: Int
            :param end: Int
            :return: start - end Number
            """
            if end is None:
                end = start
                start = 0
            return random.randint(start, end)

        def count(data: list, element):
            """
            :param data: dataLine
            :param element: is dataLine element
            :return: Number
            """
            num = 0
            for i in range(len(data)):
                if element == data[i]:
                    num += 1
            return num

        if tp:
            return [getRandom, count]
        else:
            return {'getRandom': getRandom, 'count': count}

    def FileIO(self, tp=False):

        def writeNumber(path, lines, start, end=None, mode='a', coding='utf-8'):
            """
            :param path: filePath
            :param lines: lineNumber
            :param start: Int
            :param end: Int
            :param mode: readMode
            :param coding: codingType
            :return: None
            """
            file = open(path, mode, encoding=coding)

            for i in range(lines):
                if i == lines - 1:
                    file.write(str(self.Random()['getRandom'](start, end)))
                else:
                    file.write(f"{str(self.Random()['getRandom'](start, end)) + '\n'}")

        if tp:
            return [writeNumber]
        else:
            return {'writeNumber': writeNumber}

    def Tools(self, tp=False):

        def getRandomColor(types=False):
            """
            :param types: T | F
            :return: 16 OR RGB
            """
            data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
            color = '#'
            rgb = 'rgb'
            if types:
                for i in range(6):
                    color += str(random.choice(data))
                return color
            else:
                return f'{
                    rgb + '(' + str(self.Random()['getRandom'](255)) + ',' +
                    str(self.Random()['getRandom'](255)) + ',' + str(self.Random()['getRandom'](255)) + ')'
                }'

        if tp:
            return [getRandomColor]
        else:
            return {'getRandomColor': getRandomColor}
