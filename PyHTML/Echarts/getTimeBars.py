from EchartsFc import *

Echarts().getTimeBars(
    timeline=Timeline(),
    time_line_number=5,
    y_data=Tools().getTwoListNumber(
        len(Tools().getProvince(['江西省'])),
        len(Tools().getProvince(['江西省'])), 2000, 10000),
    x_data=Tools().getProvince(['江西省']),
    title=['商家A', '商家B'],
    time=1000,
    play=True,
    auto=True,
    display_zoom=False,
    line_title=Tools.getYear(2020, 20254),
    position='top',
    main_title='GDP',
    html_name=[True, 'index.html'],
    angle=45,
)
