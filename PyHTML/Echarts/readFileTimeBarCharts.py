from EchartsFc import Echarts, Tools, Timeline

main_title = []
year = Tools().getYear(2024 - len(Tools().getProvince('keys')) + 1, 2024, bools=True)

for i in range(len(Tools().getProvince('keys'))):
    main_title.append(year[i] + 'GDP')


Echarts().readFileTimeBarCharts(
    Tools().getProvince(Tools.getProvince('keys')),
    Tools().getRandomNumberList(10000, 2000, 16000, True),
    Tools().getEchartsDict(4, 4000),
    Echarts(),
    Timeline(),
    year,
    main_title,
    '江西省GDP',
    True,
    True,
    display_zoom=True
)

