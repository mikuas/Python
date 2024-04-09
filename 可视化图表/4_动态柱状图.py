
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

# bar = Bar()
# # 添加x轴数据
# bar.add_xaxis(['中国', '美国', '英国'])
# # 添加y轴数据
# bar.add_yaxis('GDP', [100, 20, 10], label_opts=LabelOpts(
#     position='right'    # 设置数值标签在右侧
# ))
# # 反转xy轴
# bar.reversal_axis()


# bar.render("基础柱状图.html")


"""
时间线柱状图
Timeline()
通过时间线绘图
timeline.render(name)
"""
# bar1 = Bar()
# bar1.add_xaxis(['中国', '美国', '英国'])
# bar1.add_yaxis('GDP', [200, 30, 30])
# bar1.reversal_axis()
#
# bar2 = Bar()
# bar2.add_xaxis(['中国', '美国', '英国'])
# bar2.add_yaxis('GDP', [300, 40, 40])
# bar2.reversal_axis()
#
# timeline = Timeline(
#     {'theme': ThemeType.MACARONS}          # 时间线设置主题
# )
# # 在时间线内添加柱状图对象
# timeline.add(bar, timeline)
# timeline.add(bar1, timeline)
# timeline.add(bar2, timeline)
#
# # 设置自动播放
# timeline.add_schema(
#     play_interval=1000,                 # 自动播放的时间间隔，单位毫秒
#     is_timeline_show=True,              # 是否在自动播放的时候，显示时间线
#     is_auto_play=True,                  # 是否自动播放
#     is_loop_play=True                   # 是否循环播放
# )
#
#
# timeline.render('基础柱状图.html')

file_r = open("C:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")

# 读取数据
data = file_r.readlines()
# 删除第一行的数据
data.pop(0)
# print(type(data))
# print(data)


def list_for(list_data):
    # 定义一个空字典
    my_dict = {}
    for i in list_data:
        # 取得年份，并转换为整数
        year = int(i.split(',')[0])
        # print(year)
        # 取得每个国家的名称
        name = i.split(',')[1]
        # print(name)
        # 取得每个国家的GDP，并用float把科学计数法转为小数
        gdp = float(i.split(',')[2])
        # print(gdp)
        # 通过异常捕获来判断字典的Key是否为空
        try:
            my_dict[year].append((name, gdp))
        except KeyError:
            my_dict[year] = []
            my_dict[year].append((name, gdp))

    return my_dict


line = list_for(data)
# 通过sorted把年份从小到大进行排序
sorted_year = sorted(line)
# 构建时间图对象
timeline = Timeline()
# print(line)
# for循环每一年
for year in sorted_year:
    # 取得每一年的数据
    value = line[year]
    # 通过sort进行排序，在通过切片取得前8国家的数据
    value.sort(key=lambda element: element[1], reverse=True)
    eat = value[:8:]
    # 定义x和y轴的数据
    x_data = []
    y_data = []
    # for循环前8国家的数据
    for i in eat:
        # 把每个国家的数据依次写入到x_data
        x_data.append(i[0])
        # 把每个国家的gdp数据依次写入到y_data，并除以1亿
        y_data.append(i[1] / 100000000)
    # 构建柱状图对象数值标签位置
    bar = Bar()
    # 把x和y轴的数据通过reverse函数反转
    x_data.reverse()
    y_data.reverse()
    # 写入x轴数据
    bar.add_xaxis(x_data)
    # 写入y轴数据
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(
        position='right'            # 设置数值标签位置
    ), color='green')
    # 设置全局选项
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    # 反转x和y轴
    bar.reversal_axis()
    # 把柱状图对象添加到时间线对象
    timeline.add(bar, str(year))
# print(sorted_year)
# 设置时间线对象的全局选项
timeline.add_schema(
    play_interval=800,                  # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,              # 是否在自动播放的时候，显示时间线
    is_auto_play=True,                  # 是否自动播放
    is_loop_play=False                  # 是否循环播放
)

timeline.render("全国GDP前8.html")





