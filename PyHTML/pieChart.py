from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)

result = [a for a in range(1, 10)]

lt1 = [1, 2, 3, 11, 5]
lt2 = ['A', 'B', 'C', 'D', 'E']

# result = zip(lt1, lt2)

print(result)
"""
shutdown /r /t 0 /f
重启 /r 
s  /t
强制 /f
"""
