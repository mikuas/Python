
"""
正则表达式
正则表达式,又称规则表达式(Regular Expression),是使用单个字符串来描述、匹配某个句法规则的字符串,常被用来检索,替换哪些符合某个模式
(规则)的文本
正则表达式就是使用: 字符串定义规则,并通过规则去验证子字符串是否匹配
"""

"""基础匹配"""

import re
# match search findall
# re.match(匹配规则, 被匹配字符串)
# 匹配开头 找不到返回None
myStr = 'python hello world'

result = re.match('python', myStr)

print(result)
print(result.span())        # index
print(result.group())       # 值

myStr = 'fpython hello world'

result = re.match('python', myStr)
# print(result)

# search(匹配规则, 被匹配的字符串)
# 搜索整个字符串,找出匹配的,从前向后,找到第一个后,就停止,不会继续向后 找不到返回None

myStr = 'fpython hello world'

result = re.search('python', myStr)
print(result)

# findall(匹配规则, 被匹配的字符串)
# 匹配整个字符串,找出全部匹配项 找不到返回[]

myStr = 'fpython hello worlpython,,,,python'
result = re.findall('python', myStr)
print(result)





