from PyHTML.Tools import *

main_title = []
year = Tools().getYear(2024 - len(Tools().getProvince(['江西省'])) + 1, 2024, bools=True)

for i in range(len(Tools().getProvince(['江西省']))):
    main_title.append('江西省' + year[i])


Echarts().readFileTimeBarCharts(
    Tools().getProvince(['江西省']),
    Tools().getRandomNumberList(10000, 2000, 16000, True),
    Tools().getEchartsDict(4, 4000),
    Echarts(),
    Timeline(),
    year,
    main_title,
    '江西省GDP',
    True,
    True,
)

