"""
递归
递归在编程中是一种非常重要的算法
递归: 即方法(函数)自己调用自己的一种特殊编程方法
函数调用自己,即称为递归调用
"""

import os


def file_find(path):
    # listdir 列出指定路径有哪些内容
    print(os.listdir(path))
    # 判断给定的路径是否是文件夹,是返回True,反之False
    print(os.path.isdir(path))
    # 判断给定的路径是否存在,是返回True,反之False
    print(os.path.exists(path))


def get_files_recursion_from_dir(path, pt=False) -> list:
    """
    从指定的文件夹中使用递归的方式,获取全部的文件列表
    :param pt:
    :param path: 被判断的文件夹
    :return: list, 包含全部文件,如果目录不存在或无文件就返回一个空list
    """

    file_all = []
    if pt:
        print(f'当前判断的文件夹是{path}')
    # 判断路径是否存在
    if os.path.exists(path):
        # 循环列出的文件
        for file in os.listdir(path):
            new_path = path + "/" + file
            # 如果是文件夹就调用自己重复操作
            if os.path.isdir(new_path):
                # 进入表明这个目录是文件夹
                if pt:
                    file_all += get_files_recursion_from_dir(new_path, pt=True)
                else:
                    file_all += get_files_recursion_from_dir(new_path, pt=False)
            # 如果不是文件夹就收集起来
            else:
                file_all.append(new_path)

    else:
        print(f'指定的目录{path}不存在')

        return []
    # 返回收集的文件
    return file_all


if __name__ == '__main__':
    # file_find('C:/XboxGames')
    result = get_files_recursion_from_dir("C:/test")
    print(result)








