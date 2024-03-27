

def print_file_info(file_name):
    """
    通过给出的路径打开对应的文件，并输出
    :param file_name: 文件路径
    :return: None
    """

    file_r = None
    try:
        file_r = open(file_name, 'r', encoding='UTF-8')
        print(file_r.read())

    except Exception as e:
        print(f"路径错误!\n原因:{e}")

    finally:
        if file_r:
            file_r.close()


def append_to_file(file_name, data):
    """
    通过传入的文件路径，内容，把内容追加到文件中
    :param file_name: 文件路径
    :param data: 内容
    :return: None
    """

    file_a = open(file_name, 'a', encoding='UTF-8')

    file_a.write(data)
    file_a.write('\n')
    file_a.close()

