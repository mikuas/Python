import json
from pyecharts.charts import Line


def line_data(file, sp, name, title, line_name, is_show=False):

    name = Line()
    file_r = open(file, 'r', encoding='UTF-8')
    file_dict = file_r.read()
    file_dict = file_dict.replace(sp, '')
    file_dict = file_dict[:-2]
    file_dict = json.loads(file_dict)
    file_dict = file_dict['data'][0]['trend']
    x_date = file_dict['updateDate'][:314]
    name.add_xaxis(x_date)
    y_dict = file_dict['list'][0]['data'][:314]
    name.add_yaxis(title, y_dict)
    if is_show:
        name.render(line_name)


if __name__ == '__main__':
    pass
