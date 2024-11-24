
def str_reverse(str_data):
    """
    将传入的字符串反转返回
    :param str_data: 要反转的字符串
    :return: 反转后的结果
    """

    return str_data[::-1]


def str_slice(str_data, x, y, num=1):
    """
    接受传入的字符串，按照下标x，y，步长num，对字符串进行切片
    :param str_data: 要切片的字符串
    :param x: 起始下标
    :param y: 结束下标
    :param num: 步长，不写默认为1
    :return: 切片后的结果
    """

    return str_data[x:y:num]
