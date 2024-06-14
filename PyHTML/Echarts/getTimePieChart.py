from EchartsFc import *


def rd():
    return Tools().getRandom(1000)


Echarts().getTimePieChart(
    2,
    [
        [
            ['A', 'B', 'C', 'D', 'E'], [rd(), rd(), rd(), rd(), rd()],
        ],
        [
            ['A', 'B', 'C', 'D', 'E'], [rd(), rd(), rd(), rd(), rd()],
        ]
    ],
    [
        Tools().getRandomColor(),
        Tools().getRandomColor(),
        Tools().getRandomColor(),
        Tools().getRandomColor(),
        Tools().getRandomColor()
    ],
    'GDP',
    Timeline(),
    Tools().getProvince(['江西省'])[:2:],
    True,
    True,
)