from PyHTML.Tools import *


def rd():
    return Tools().getRandom(2000, 5000)


Echarts().getPieChart(
    [
        ['A', 'B', 'C', 'D', 'E'], [rd(), rd(), rd(), rd(), rd()],
    ],
    [
        Tools().getRandomColor(),
        Tools().getRandomColor(),
        Tools().getRandomColor(),
        Tools().getRandomColor(),
        Tools().getRandomColor()
    ],
    'GDP',
    True
)
