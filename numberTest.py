import random

numberList = list(range(1, 17))  # 简化生成numberList的过程

elementDict = {
 'a': 0,
 'b': 0,
 'c': 0,
 'd': 0,
 'e': 0,
 'f': 0,
 'g': 0,
 'h': 0,
 'j': 0,
 'k': 0,
 'l': 0,
 'm': 0,
 'n': 0,
 'o': 0,
 'p': 0,
 'q': 0
}

flag = True

while flag:
    numberList = list(range(1, 17))  # 重置 numberList
    dictIndex = list(elementDict.keys())  # 重置 dictIndex

    # 分配随机值给字典
    for key in dictIndex:
        randomIndex = random.randint(0, len(numberList) - 1)
        elementDict[key] = numberList[randomIndex]
        del numberList[randomIndex]

    # 计算各行、列、对角线的和
    _one = elementDict['a'] + elementDict['b'] + elementDict['c'] + elementDict['d']
    _two = elementDict['e'] + elementDict['f'] + elementDict['g'] + elementDict['h']
    _three = elementDict['j'] + elementDict['k'] + elementDict['l'] + elementDict['m']
    _four = elementDict['n'] + elementDict['o'] + elementDict['p'] + elementDict['q']

    _five = elementDict['a'] + elementDict['e'] + elementDict['j'] + elementDict['n']
    _six = elementDict['b'] + elementDict['f'] + elementDict['k'] + elementDict['o']
    _seven = elementDict['c'] + elementDict['g'] + elementDict['l'] + elementDict['p']
    _eight = elementDict['d'] + elementDict['h'] + elementDict['m'] + elementDict['q']

    left = elementDict['a'] + elementDict['f'] + elementDict['l'] + elementDict['q']
    right = elementDict['d'] + elementDict['g'] + elementDict['k'] + elementDict['n']

    print(_one, _two, _three, _four, _five, _six, _seven, _eight, left, right)

    # 检查是否满足条件
    if _one == _two == _three == _four == _five == _six == _seven == _eight == left == right == 34:
        flag = False  # 满足条件时退出循环

print('---------------------------------------------------------------------------------------------')
print(elementDict)
