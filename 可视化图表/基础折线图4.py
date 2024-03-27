"""
基础折线图
"""
import json
import my_def
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts, TooltipOpts, LabelOpts

"""
# 得到折线图对象 line = Line()
line = Line()

# 添加x轴数据line.add_xaxis
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据line.add_yaxis
line.add_yaxis("GDP", [100, 20, 10])

"""

"""
全局配置: set_global_opts
文档:https://pyecharts.org/#/zh-cn/
title_opts = TitleOpts(title="标题名称", pos_left="位置", pos_bottom="上下")
legend_opts = LegendOpts(is_show=True/False) 图例
tooltip_opts = LegendOpts(is_show=True/False) 工具箱
visualmap_opts = VisualMapOpts(is_show=True/False) 视觉映射
"""
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     tooltip_opts=TooltipOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
#
# )

# 生成图表line.render([name])
# line.render("line.html")


# json数据处理

# 打开文件
file_r = open("C:/美国.txt", 'r', encoding='UTF-8')
# file_in = open("C:/印度.txt", 'r', encoding='UTF-8')
# file_rb = open("C:/日本.txt", 'r', encoding='UTF-8')
# 读取文件全部内容
us_data = file_r.read()
# in_data = file_in.read()
# rb_data = file_rb.read()
# 去除前面多余的字符
us_data = us_data.replace('jsonp_1629344292311_69436(', '')
# in_data = in_data.replace('jsonp_1629350745930_63180(', '')
# rb_data = rb_data.replace('jsonp_1629350871167_29498(', '')
# 去除后面多余的字符
us_dict = us_data[:-2]
# in_data = in_data[:-2]
# rb_data = rb_data[:-2]
# 转为dict
us_dict = json.loads(us_dict)
# in_data = json.loads(in_data)
# rb_data = json.loads(rb_data)
# print(type(us_dict))
# print(us_dict)
# 取得trend中的value
us_dict = us_dict['data'][0]['trend']
# in_data = in_data['data'][0]['trend']
# rb_data = rb_data['data'][0]['trend']
# print(type(us_dict))
# print(us_dict)

# 取得updateDate的全部Value,并进行切片到314位
x_date = us_dict['updateDate'][:314]
# in_data = in_data['updateDate'][:314]
# rb_data = rb_data['updateDate'][:314]
# 创建折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(x_date)
# line.add_xaxis(in_data)
# line.add_xaxis(rb_data)
# 取得data的key,并进行切片到314位
name_dict = us_dict['list'][0]['data'][:314]
# in_data = in_data['list'][0]['data'][:314]
# rb_data = rb_data['list'][0]['data'][:314]
# 添加y轴数据
line.add_yaxis("确诊", name_dict, label_opts=LabelOpts(is_show=False)) # 是否显示数字
# line.add_yaxis("确诊", in_data)
# line.add_yaxis("确诊", rb_data)
# 生成折线图
line.render("index.html")

file_r.close()


