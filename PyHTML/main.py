from Tools import *

mainTitle = Tools().getYear(2024 - len(Tools().getProvince(['江西省', '江苏省'])) + 1, 2024, bools=True)

for i in range(len(mainTitle)):
    mainTitle[i] += '江西省GDP'

print(mainTitle)
print(Tools().getProvince(['江苏省', '江西省']))

Echarts().readFileTimeBarCharts(
    mainTitle=mainTitle,
    x_data=Tools().getProvince(['江苏省', '江西省']),
    dicts=Tools().getEchartsDict(4, 3000),
    data=Tools().getRandomNumberList(1000, 2000, 15000, True),
    echarts=Echarts(),
    title='江西省GDP',
    lineTitle=Tools().getYear(2024 - len(Tools().getProvince(['江西省', '江苏省'])), 2024, bools=True),
    timeline=Timeline(),
    time=1000,
    text_color='blue',
    position='top',
    HTML_Name='index.html',
    dataZoom=True,
    PT='5%',
    angle=45,
    play=True,
    For=True
)

