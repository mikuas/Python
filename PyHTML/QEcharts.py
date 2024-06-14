import random
import pyautogui
import pyperclip
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *
# from pyecharts.faker import Faker


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
    def getLineChart(
            x_data: list = None,
            y_data: list = None,
            title: str = None,
            width: str = None,
            height: str = None,
            text_color: str = None,
            center: str = 'center',
            html_name: str = 'index.html',
    ):
        """
        :param text_color: Text Color
        :param x_data: x Data: List
        :param y_data: y Data: List
        :param title: Line Title
        :param html_name: Name, defaults to 'index.html'
        :param center: align Mode, default to center
        :param width: Line Width, default to '1200px'
        :param height: Line Height, default to '600px'
        :return: Line()
        """
        try:
            line = (
                Line(init_opts=InitOpts(
                    theme=ThemeType.LIGHT,
                    width=width or '1200px',
                    height=height or '600px',
                    is_horizontal_center=center
                ))
                .add_xaxis(x_data)
                .add_yaxis(
                    title, y_data,
                    color=text_color or 'black'
                )
                .set_global_opts(
                    title_opts=TitleOpts(title=title),
                    legend_opts=LegendOpts(is_show=True),
                    tooltip_opts=TooltipOpts(is_show=True),
                    visualmap_opts=VisualMapOpts(is_show=True)
                )
            ).render(html_name)

            return line
        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getMap(
            data: list = None,
            title: str = None,
            dicts: dict = None,
            name: str = None,
            width: str = None,
            height: str = None,
            center: str = 'center',
            html_name: str = 'index.html'
    ):
        """
        :param width: Map Width
        :param height: Map Height
        :param center: align Mode, default center align
        :param data: Data, [(key, value), (key, value), ...]
        :param title: Map Title
        :param dicts: pieces option, {0: {'min': value, 'max': value, 'label': value, 'color': value}} length = 4
        :param name: country OR province Name
        :param html_name:
        :return: Map()
        """
        try:
            map = (
                Map(init_opts=InitOpts(
                    theme=ThemeType.LIGHT,
                    width=width or '1200px',
                    height=height or '600px',
                    is_horizontal_center=center
                ))
                .add(title, data, name)
                .set_global_opts(
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=True,
                        pieces=[
                            {'min': dicts[0]['min'],
                             'max': dicts[0]['max'],
                             'label': dicts[0]['label'],
                             'color': dicts[0]['color']
                             },

                            {'min': dicts[1]['min'],
                             'max': dicts[1]['max'],
                             'label': dicts[1]['label'],
                             'color': dicts[1]['color']
                             },

                            {'min': dicts[2]['min'],
                             'max': dicts[2]['max'],
                             'label': dicts[2]['label'],
                             'color': dicts[2]['color']
                             },

                            {'min': dicts[3]['min'],
                             'label': dicts[3]['label'],
                             'color': dicts[3]['color']
                             }
                        ]
                    )
                )
            ).render(html_name)

            return map
        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getBars(
            x_data: list = None,
            y_data: list = None,
            title: list = None,
            main_title: str = None,
            dicts: dict = None,
            angle: int = 45,
            position: str = 'top',
            html_name: str = 'index.html',
            display_zoom: bool = False,
            zoom_position: str = '5%',
            text_color: str = None,
            width: str = None,
            height: str = None,
            center: str = 'center',
            reverse: bool = False,
    ):
        """
        :param x_data: x Data: List
        :param y_data: y Data: List -> List [[], ...]
        :param title: Bar Title
        :param main_title: Main Title
        :param position: Title Position
        :param angle: x Data angle
        :param zoom_position: Zoom Position
        :param display_zoom: None
        :param dicts: pieces option, {0: {'min': value, 'max': value, 'label': value, 'color': value}} length = 4
        :param html_name: Name, defaults to 'index.html'
        :param width: Bar Width
        :param height: Bar Height
        :param text_color: Text Color
        :param center: align Mode, default center align
        :param reverse: reverse X Y
        :return: Bar()
        """
        try:
            bar = Bar(init_opts=InitOpts(
                theme=ThemeType.WHITE,
                width=width or '1200px',
                height=height or '600px',
                is_horizontal_center=center
            ))
            bar.add_xaxis(x_data)
            for i in range(len(y_data)):
                bar.add_yaxis(title[i], y_data[i], label_opts=LabelOpts(
                    position=position,
                    color=text_color or 'black'
                ))
            if display_zoom:
                bar.set_global_opts(
                    title_opts=TitleOpts(
                        title=main_title,
                    ),
                    xaxis_opts=AxisOpts(
                        axislabel_opts=LabelOpts(rotate=angle)
                    ),
                    datazoom_opts=DataZoomOpts(
                        is_show=True,
                        type_="slider",
                        orient="horizontal",
                        pos_top=zoom_position
                    )
                )
            else:
                bar.set_global_opts(
                    title_opts=TitleOpts(
                        title=main_title,
                    ),
                    xaxis_opts=AxisOpts(
                        axislabel_opts=LabelOpts(rotate=angle)
                    )
                )
            if reverse:
                bar.reversal_axis()
            bar.render(html_name)

            return bar
        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getPieChart(
            data: list[list] = None,
            color: list = None,
            main_title: str = None,
            render: bool = False,
            center: str = 'center',
            width: str = None,
            height: str = None,
            html_name: str = 'index.html',
            name="",
    ):
        """
        :param data: [[key, key, ...], [value, value, ...]]
        :param color: key -> color, length = data length
        :param main_title: Main Title
        :param width: Pie Width
        :param height: Pie Height
        :param name: None
        :param center: align Mode, default center align
        :param html_name: Name, default to 'index.html'
        :param render: create HTML File
        :return: Pie()
        """
        try:
            pie = (
                Pie(init_opts=InitOpts(
                    is_horizontal_center=center,
                    theme=ThemeType.LIGHT,
                    width=width or '1200px',
                    height=height or '600px'
                ))
                .add(series_name=name, data_pair=[list(z) for z in zip(data[0], data[1])])
                .set_colors(color)
                .set_global_opts(title_opts=TitleOpts(title=main_title))
                .set_series_opts(label_opts=LabelOpts(formatter="{b}: {c}"))
            )
            if render:
                pie.render(html_name)

            return pie
        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getBarChart(
            x_data: list = None,
            y_data: list = None,
            dicts: dict = None,
            title: str = None,
            main_title: str = None,
            html_name: str = 'index.html',
            zoom_position: str = '5%',
            display_zoom: bool = False,
            position: str = 'top',
            width: str = None,
            height: str = None,
            angle: str = 45,
            center: str = 'center',
            text_color: str = None,
            reverse: bool = False,
    ):
        """
        :param x_data: x Data: List
        :param y_data: y Data: List
        :param display_zoom: displayZoom
        :param dicts: pieces option, {0: {'min': value, 'max': value, 'label': value}} length = 4
        :param position: Title Position
        :param html_name: Name
        :param main_title: Main Title
        :param title: Bar Title
        :param zoom_position: Zoom Position
        :param angle: x Data align
        :param center: align Mode, default center align
        :param text_color: Text Color
        :param width: Bar Width
        :param height: Bar Height
        :param reverse: reverse X Y
        :return: Bar()
        """
        try:
            bar = Bar(init_opts=InitOpts(
                theme=ThemeType.LIGHT,
                is_horizontal_center=center,
                width=width or '1200px',
                height=height or '600px'
            ))
            bar.add_xaxis(x_data)
            bar.add_yaxis(
                title, y_data,
                label_opts=LabelOpts(
                    position=position,
                    color=text_color or 'black'
                ))
            if display_zoom:
                bar.set_global_opts(
                    title_opts=TitleOpts(
                        title=main_title,
                    ),
                    xaxis_opts=AxisOpts(
                        axislabel_opts=LabelOpts(rotate=angle)
                    ),
                    datazoom_opts=DataZoomOpts(
                        is_show=True,
                        type_="slider",
                        orient="horizontal",
                        pos_top=zoom_position
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=True,
                        pieces=[
                            {'min': dicts[0]['min'],
                             'max': dicts[0]['max'],
                             'label': dicts[0]['label'],
                             'color': dicts[0]['color']
                             },

                            {'min': dicts[1]['min'],
                             'max': dicts[1]['max'],
                             'label': dicts[1]['label'],
                             'color': dicts[1]['color']
                             },

                            {'min': dicts[2]['min'],
                             'max': dicts[2]['max'],
                             'label': dicts[2]['label'],
                             'color': dicts[2]['color']
                             },

                            {'min': dicts[3]['min'],
                             'label': dicts[3]['label'],
                             'color': dicts[3]['color']
                             }
                        ]
                    )
                )
            else:
                bar.set_global_opts(
                    title_opts=TitleOpts(
                        title=main_title,
                    ),
                    xaxis_opts=AxisOpts(
                        axislabel_opts=LabelOpts(rotate=angle)
                    ),
                    visualmap_opts=VisualMapOpts(
                        is_show=True,
                        is_piecewise=True,
                        pieces=[
                            {'min': dicts[0]['min'],
                             'max': dicts[0]['max'],
                             'label': dicts[0]['label'],
                             'color': dicts[0]['color']
                             },

                            {'min': dicts[1]['min'],
                             'max': dicts[1]['max'],
                             'label': dicts[1]['label'],
                             'color': dicts[1]['color']
                             },

                            {'min': dicts[2]['min'],
                             'max': dicts[2]['max'],
                             'label': dicts[2]['label'],
                             'color': dicts[2]['color']
                             },

                            {'min': dicts[3]['min'],
                             'label': dicts[3]['label'],
                             'color': dicts[3]['color']
                             }
                        ]
                    )
                )
            if reverse:
                bar.reversal_axis()
            bar.render(html_name)
            return bar
        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getTimeBars(
            timeline: Timeline = None,
            time_line_number: int = None,
            x_data: list = None,
            y_data: list = None,
            line_title: list = None,
            title: list = None,
            html_name: list = None,
            main_title: str = None,
            play: bool = False,
            auto: bool = False,
            time: int = 1000,
            display_zoom: bool = False,
            zoom_position: str = '5%',
            position: str = 'top',
            angle: int = 45,
            text_color: str = None,
    ):
        """
        :param timeline: Object -> Timeline()
        :param time_line_number: LineCount
        :param x_data: List
        :param y_data: List -> [[], [], ...]
        :param line_title: List, length = time_line_number
        :param title: Title
        :param position: Title Position
        :param main_title: Main Title
        :param time: interval time, default interval time to 1s
        :param play: autoPlay
        :param auto: cycle Play
        :param display_zoom: displayZoom
        :param html_name: create HTML File: bool, Name
        :param zoom_position: Zoom Position
        :param angle: x Data angle
        :param text_color: Text Color
        :return: None
        """
        try:
            for i in range(time_line_number):
                result = Echarts().getBars(
                    display_zoom=display_zoom,
                    x_data=x_data,
                    y_data=y_data[i],
                    title=title,
                    position=position,
                    main_title=main_title,
                    html_name=html_name[1],
                    zoom_position=zoom_position,
                    angle=angle,
                    text_color=text_color
                )
                timeline.add(result, line_title[i])
                timeline.add_schema(
                    play_interval=time,
                    is_timeline_show=True,
                    is_auto_play=play,
                    is_loop_play=auto,
                )
            if html_name[0]:
                timeline.render(html_name[1])

        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getTimePieChart(
            lines: int = None,
            data: list = None,
            color: list = None,
            main_title: str = None,
            timeline: Timeline = None,
            line_title: list = None,
            play: bool = False,
            auto: bool = False,
            width: str = None,
            height: str = None,
            time: int = 1000,
            html_name: str = 'index.html',
            name: str = ""
    ):
        """
        :param lines: TimelineCount = data length
        :param data: List -> [[(key, value), (key, value), ...], ...]
        :param color: List, length = data length
        :param main_title: Main Title
        :param width: Pie Width
        :param height: Pie Height
        :param timeline: Object -> Timeline()
        :param name: None
        :param line_title: Line Title: List
        :param time: interval time, default interval time to 1s
        :param html_name: Name
        :param play: autoplay
        :param auto: cycle Play
        :return: None
        """
        try:
            for i in range(lines):
                result = Echarts().getPieChart(
                    width=width,
                    height=height,
                    html_name=html_name,
                    name=name,
                    data=data[i],
                    color=color,
                    main_title=main_title
                )
                timeline.add(result, line_title[i])
            timeline.width = width or '1200px'
            timeline.height = height or '600px'
            timeline.add_schema(
                play_interval=time,
                is_timeline_show=True,
                is_auto_play=play,
                is_loop_play=auto
            )
            timeline.render(html_name)

        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def getTimeBarChart(
            timeline: Timeline = None,
            bars: list[Bar] = None,
            title: str = None,
            html_name: list = None,
            play: bool = False,
            auto: bool = False,
            time: int = 1000,
            width: str = None,
            height: str = None,
    ):
        """
        :param timeline: Object -> Timeline()
        :param bars: List[Bar()]
        :param title: Bar Title
        :param html_name: List[Bool, Name]
        :param time: interval time, default interval time to 1s
        :param play: autoplay
        :param auto: cycle Play
        :param width: Bar Width
        :param height: Bar Height
        :return: None
        """
        try:
            for i in range(len(bars)):
                timeline.add(bars[i], title)
                timeline.width = width or '1200px'
                timeline.height = height or '600px'
            timeline.add_schema(
                play_interval=time,
                is_timeline_show=True,
                is_auto_play=play,
                is_loop_play=auto,
            )
            if html_name[0]:
                timeline.render(html_name[1])

        except Exception as e:
            print(f'{e}!!!!!')

    @staticmethod
    def readFileTimeBarCharts(
            x_data: list = None,
            all_y_data: list = None,
            dicts: dict = None,
            echarts: 'Echarts()' = None,
            timeline: Timeline() = None,
            line_title: list = None,
            main_title: list = None,
            title: str = None,
            play: bool = False,
            auto: bool = False,
            text_color: str = None,
            width: str = None,
            height: str = None,
            time: int = 1000,
            position: str = 'top',
            display_zoom: bool = False,
            zoom_position: str = '5%',
            angle: int = 45,
            html_name: str = 'index.html',
            center='center',
            reverse=False,
    ):
        """
        :param x_data: List
        :param all_y_data: List
        :param dicts: pieces option, {0: {'min': value, 'max': value, 'label': value}} length = 4
        :param echarts: Object -> Echarts()
        :param timeline: Object -> Timeline()
        :param time: interval time, default interval time to 1s
        :param line_title: Line Title
        :param position: Title Position
        :param html_name: Name
        :param display_zoom: displayZoom
        :param zoom_position: Zoom Position
        :param main_title: Main Title, List
        :param title: Bar Title
        :param angle: x Data angle
        :param play: autoplay
        :param auto: cycle Play
        :param text_color: Text Color
        :param center: align Mode, default align center
        :param width: Bar Width
        :param height: Bar Height
        :param reverse: reverse X Y
        :return: None
        """
        try:
            num = len(x_data)
            line_title.reverse()
            for i in range(len(x_data)):
                y_data = []
                for j in range(len(all_y_data)):
                    y_data.append(int(all_y_data[j].split()[0]))
                if i == 0:
                    y_data = y_data[:num:]
                else:
                    y_data = y_data[num - len(x_data):num]
                num += 10
                results = echarts.getBarChart(
                    display_zoom=display_zoom,
                    main_title=main_title[i],
                    text_color=text_color,
                    center=center,
                    angle=angle,
                    zoom_position=zoom_position,
                    reverse=reverse,
                    dicts=dicts,
                    x_data=x_data,
                    y_data=y_data,
                    title=title,
                    html_name=html_name,
                    position=position
                )

                if i == len(x_data) - 1:
                    echarts.getTimeBarChart(
                        width=width,
                        height=height,
                        timeline=timeline,
                        bars=[results],
                        title=str(line_title[len(x_data) - (i + 1)]) + 'GDP',
                        html_name=[True, html_name],
                        time=time,
                        play=play,
                        auto=auto
                    )
                else:
                    echarts.getTimeBarChart(
                        width=width,
                        height=height,
                        timeline=timeline,
                        bars=[results],
                        title=str(line_title[len(x_data) - (i + 1)]) + 'GDP',
                        html_name=[False, html_name],
                        time=time,
                        play=play,
                        auto=auto
                    )

        except Exception as e:
            print(f'{e}!!!!!')


class Tools:

    @staticmethod
    def getRandom(start: int, end: int = None) -> int:
        """
        get Random Number Between start to end, end is None start = 0 end = start
        :param start: start Number
        :param end: end Number
        :return: Between start to end Random Number
        """
        if end is None:
            end = start
            start = 0
        return random.randint(start, end)

    @staticmethod
    def count(data: [list, tuple], element) -> int:
        """
        :param data: list OR tuple
        :param element:
        :return: int
        """
        num = 0
        for i in range(len(data)):
            if element == data[i]:
                num += 1
        return num

    def writeNumberToLine(
            self,
            path: str = None,
            lines: int = None,
            start: int = None,
            end: int = None,
            mode: str = 'a',
            coding: str = 'utf-8'
    ):
        """
        :param path: filePath
        :param lines: line count
        :param start: start Number, end is None, default start Number is 0
        :param end: end Number
        :param mode: file open mode, default file open mode is 'a'
        :param coding: coding
        :return: None
        """
        file = open(path, mode, encoding=coding)

        for i in range(lines):
            if i == lines - 1:
                file.write(str(self.getRandom(start, end)))
            else:
                file.write(f"{str(self.getRandom(start, end)) + '\n'}")

    def getRandomColor(self, types=False) -> str:
        """
        get random color, types = False return 16, types = True return RGB
        :param types: Bool
        :return: randomColor
        """
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
        color = '#'
        rgb = 'rgb('
        if types:
            return f"{
                rgb + str(self.getRandom(255)) + ',' + str(self.getRandom(255)) + ',' + str(self.getRandom(255)) + ')'
            }"
        else:
            for i in range(6):
                color += str(random.choice(data))
            return color

    def getEchartsDict(self, line: int, interval: int) -> dict:
        """
        if end = None, start default start Number is 0 end = start
        :param line: line
        :param interval: start to end
        :return: dict
        """
        start = 0
        my_dict = {}
        for i in range(line):
            my_dict[i] = {}
            if i == line - 1:
                my_dict[i]['min'] = start
                my_dict[i]['label'] = f'{start}+'
                my_dict[i]['color'] = self.getRandomColor(True)
            else:
                my_dict[i]['min'] = start
                my_dict[i]['max'] = start + interval
                my_dict[i]['label'] = f'{start}-{start + interval}'
                my_dict[i]['color'] = self.getRandomColor(True)
            if i >= 0:
                start += interval + 1
            else:
                start += interval
        return my_dict

    @staticmethod
    def getYear(start: int, end: int, lens=None, bools=False) -> list[str]:
        """
        :param start: start year
        :param end: end year
        :param lens: display length
        :param bools: Bool: whether display Year
        :return: yearList
        """
        length = lens or end - start + 1
        if length > end - start:
            length = end - start + 1
        years = []
        for i in range(length):
            if bools:
                years.append(str(start + i) + '年')
            else:
                years.append(str(start + i))
        return years

    def getRandomNumberList(self, lines, start, end=None, bools=False) -> list[str]:
        """
        :param bools: Bool
        :param lines: lines Number
        :param start: start Number
        :param end: end Number, if None start = 0, end = start
        :return: NumberList[Str]
        """
        if end is None:
            end = start
            start = 0
        num = []
        for i in range(lines):
            if bools:
                num.append(str(self.getRandom(start, end)))
            else:
                num.append(self.getRandom(start, end))
        return num

    def getTwoListNumber(self, line_count, lines, start, end=None, bools=False) -> list[str]:
        all_data = []
        line_data = []
        for i in range(line_count):
            for j in range(2):
                line_data.append(self.getRandomNumberList(lines, start, end, bools))
            all_data.append(line_data)
            line_data = []

        return all_data

    @staticmethod
    def getProvince(province_names: list) -> list:
        """
        provinceKeys:
        江西省 海南省 安徽省 浙江省 澳门特别行政区 黑龙江省
        江苏省 台湾省 青海省 贵州省 云南省 宁夏回族自治区
        山西省 辽宁省 吉林省 广西壮族自治区 湖南省 天津市
        河北省 北京市 上海市 重庆市 福建省 河南省 广东省
        山东省 甘肃省 香港特别行政区 新疆维吾尔自治区
        西藏自治区 陕西省 四川省 湖北省
        :param province_names: province Name List
        :return: city inside province
        """
        china_cities = {
            '北京市': ['北京市'],
            '天津市': ['天津市'],
            '上海市': ['上海市'],
            '重庆市': ['重庆市'],
            '河北省': [
                '石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市',
                '张家口市', '承德市', '沧州市', '廊坊市', '衡水市'
            ],
            '山西省': [
                '太原市', '大同市', '阳泉市', '长治市', '晋城市', '朔州市',
                '晋中市', '运城市', '忻州市', '临汾市', '吕梁市'
            ],
            '辽宁省': [
                '沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市',
                '营口市', '阜新市', '辽阳市', '盘锦市', '铁岭市', '朝阳市', '葫芦岛市'
            ],
            '吉林省': [
                '长春市', '吉林市', '四平市', '辽源市', '通化市', '白山市', '松原市',
                '白城市', '延边朝鲜族自治州'
            ],
            '黑龙江省': [
                '哈尔滨市', '齐齐哈尔市', '鸡西市', '鹤岗市', '双鸭山市', '大庆市',
                '伊春市', '佳木斯市', '七台河市', '牡丹江市', '黑河市', '绥化市', '大兴安岭地区'
            ],
            '江苏省': [
                '南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市',
                '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市'
            ],
            '浙江省': [
                '杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市',
                '金华市', '衢州市', '舟山市', '台州市', '丽水市'
            ],
            '安徽省': [
                '合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市',
                '铜陵市', '安庆市', '黄山市', '滁州市', '阜阳市', '宿州市',
                '巢湖市', '六安市', '亳州市', '池州市', '宣城市'
            ],
            '福建省': [
                '福州市', '厦门市', '莆田市', '三明市', '泉州市', '漳州市',
                '南平市', '龙岩市', '宁德市'
            ],
            '江西省': [
                '南昌市', '景德镇市', '萍乡市', '九江市', '新余市', '鹰潭市',
                '赣州市', '吉安市', '宜春市', '抚州市', '上饶市'
            ],
            '山东省': [
                '济南市', '青岛市', '淄博市', '枣庄市', '东营市', '烟台市',
                '潍坊市', '济宁市', '泰安市', '威海市', '日照市', '莱芜市',
                '临沂市', '德州市', '聊城市', '滨州市', '菏泽市'
            ],
            '河南省': [
                '郑州市', '开封市', '洛阳市', '平顶山市', '安阳市', '鹤壁市',
                '新乡市', '焦作市', '濮阳市', '许昌市', '漯河市', '三门峡市',
                '南阳市', '商丘市', '信阳市', '周口市', '驻马店市'
            ],
            '湖北省': [
                '武汉市', '黄石市', '十堰市', '宜昌市', '襄阳市', '鄂州市',
                '荆门市', '孝感市', '荆州市', '黄冈市', '咸宁市', '随州市', '恩施土家族苗族自治州'
            ],
            '湖南省': [
                '长沙市', '株洲市', '湘潭市', '衡阳市', '邵阳市', '岳阳市',
                '常德市', '张家界市', '益阳市', '郴州市', '永州市', '怀化市',
                '娄底市', '湘西土家族苗族自治州'
            ],
            '广东省': [
                '广州市', '韶关市', '深圳市', '珠海市', '汕头市', '佛山市',
                '江门市', '湛江市', '茂名市', '肇庆市', '惠州市', '梅州市',
                '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市',
                '潮州市', '揭阳市', '云浮市'
            ],
            '广西壮族自治区': [
                '南宁市', '柳州市', '桂林市', '梧州市', '北海市', '防城港市',
                '钦州市', '贵港市', '玉林市', '百色市', '贺州市', '河池市', '来宾市', '崇左市'
            ],
            '海南省': [
                '海口市', '三亚市', '三沙市', '儋州市'
            ],
            '四川省': [
                '成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市',
                '广元市', '遂宁市', '内江市', '乐山市', '南充市', '眉山市',
                '宜宾市', '广安市', '达州市', '雅安市', '巴中市', '资阳市',
                '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州'
            ],
            '贵州省': [
                '贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市',
                '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州'
            ],
            '云南省': [
                '昆明市', '曲靖市', '玉溪市', '保山市', '昭通市', '丽江市', '普洱市',
                '临沧市', '楚雄彝族自治州', '红河哈尼族彝族自治州', '文山壮族苗族自治州',
                '西双版纳傣族自治州', '大理白族自治州', '德宏傣族景颇族自治州', '怒江傈僳族自治州', '迪庆藏族自治州'
            ],
            '西藏自治区': [
                '拉萨市', '日喀则市', '昌都市', '林芝市', '山南市', '那曲市', '阿里地区'
            ],
            '陕西省': [
                '西安市', '铜川市', '宝鸡市', '咸阳市', '渭南市', '延安市', '汉中市', '榆林市', '安康市', '商洛市'
            ],
            '甘肃省': [
                '兰州市', '嘉峪关市', '金昌市', '白银市', '天水市', '武威市', '张掖市',
                '平凉市', '酒泉市', '庆阳市', '定西市', '陇南市', '临夏回族自治州', '甘南藏族自治州'
            ],
            '青海省': [
                '西宁市', '海东市', '海北藏族自治州', '黄南藏族自治州', '海南藏族自治州',
                '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州'
            ],
            '宁夏回族自治区': [
                '银川市', '石嘴山市', '吴忠市', '固原市', '中卫市'
            ],
            '新疆维吾尔自治区': [
                '乌鲁木齐市', '克拉玛依市', '吐鲁番市', '哈密市', '昌吉回族自治州',
                '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '阿克苏地区', '克孜勒苏柯尔克孜自治州',
                '喀什地区', '和田地区', '伊犁哈萨克自治州', '塔城地区', '阿勒泰地区'
            ],
            '香港特别行政区': [
                '香港岛', '九龙', '新界'
            ],
            '澳门特别行政区': [
                '澳门半岛', '氹仔', '路环', '路氹城'
            ],
            '台湾省': [
                '台北市', '高雄市', '基隆市', '台中市', '台南市', '新竹市', '嘉义市',
                '新北市', '桃园市', '新竹县', '苗栗县', '彰化县', '南投县', '云林县',
                '嘉义县', '屏东县', '宜兰县', '花莲县', '台东县', '澎湖县', '金门县', '连江县'
            ]
        }

        city = []
        for i in range(len(province_names)):
            city += china_cities[province_names[i]]
        return city


if __name__ == '__main__':
    pass
