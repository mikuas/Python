"""
元字符匹配
"""
import re

myStr = 'pyTHon114514191981007210d00.,>,//==!!@@#$^&&&(*'

# 字符串前面带上r标记,表示字符串中转移字符无效,就是普通字符
result = re.findall(r'\d', myStr)
# 匹配数字
# print(result)

result = re.findall(r'\W', myStr)
# 匹配特殊字符
# print(result)

result = re.findall(r'[A-z]', myStr)
# 匹配英文字母
# print(result)


"""案例"""


def zhMatch(str_data: str) -> list:
    """
    匹配账号,只能由字母和数字组成,长度限制6-10位
    :param str_data
    :return: result
    """
    results = re.findall(r'^[a-zA-Z0-9]{6,10}$', str_data)

    if not results:
        print('账号有误,请重新输入!')
    else:
        print(results)
        return results


def qqMatch(str_data: str) -> list:
    """
    匹配qq号,长度5-11位
    :param str_data:
    :return:
    """

    results = re.findall(r'^[1-9]\d{4,10}$', str_data)

    if not results:

        print('QQ号输入有误,请重新输入!')
    else:
        print(results)
        return results


def mailMatch(str_data: str) -> list:
    """
    匹配邮箱地址,只允许qq,163,gmail这三种邮箱地址
    :param str_data:
    :return:
    """
    results = re.findall(r'(^[\w-]+(\.[\w-]+)*@(qq|gmail|163)(\.[\w-]+)$)', str_data)
    # 有几个组就返回几个
    if not results:
        print('邮箱地址不正确,请重新输入!')

    else:
        print(results)
        return results


mailMatch('users@gmail.com')





