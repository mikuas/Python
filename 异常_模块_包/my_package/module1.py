
# __all__ = ['for_list', 'while_list']


def for_list(data):

    print("for循环遍历list")
    for i in data:
        print(f"{data}中的数据是{i}")


def while_list(data, num=0):

    print("while循环遍历list")
    while num < len(data):
        element = data[num]
        print(f"{data}中的数据是{element}")
        num += 1




