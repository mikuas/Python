"""
open()打开函数
语法：open(filename, mode='', encoding='')
name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)
mode：设置打开文件的模式(访问模式)：只读(r)，写入(w)，追加(a)
encoding：编码格式(推荐使用UTF-8)
    r：以只读方式打开文件，文件指针将会放在文件的开头，这是默认模式
    w：打开一个文件用于写入，如果该文件以存在则打开文件，并从头开始编辑，原有内容会被删除，如果该文件不存在，创建新文件
    a：打开一个文件用于追加，如果该文件以存在，新的内容将会被写入到已有内容之后，如果该文件不存在，创建新文件进行写入
"""

file = open('C:/test.txt', 'r', encoding='UTF-8')

"""
读取文件-read()方法
语法：文件对象.read(num)
num表示要从文件中读取的数据长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有的数据

readlines()方法
语法：文件对象.readlines()
readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素

readline()方法
语法：文件对象.readline()
一次读取一行内容
"""
# file = file.read()

# print(file)

# file = file.readlines()

# print(file)

# file1 = file.readline()
# file2 = file.readline()
# file3 = file.readline()

# print(file1)
# print(file2)
# print(file3)

"""
for循环读取文件
语法：for 临时变量 in open(file_name, mode='r'):
每一个临时变量，就记录了文件的一行数据
"""

# for i in open("C:/test.txt", "r"):
#     print(i)

"""
close()关闭文件对象
语法：文件对象.close()
如果不调用close，同时程序没有停止运行，那么这个文件将一直被python程序占用
"""

# time.sleep(1145)

file.close()

"""
/with open语法
with open(file, mode='', encoding="UTF-8") as name:
    # name.readlines()
可通过在with open的语句块中对文件进行操作
可以在操作完成后自动关闭close文件，避免遗忘掉close方法
"""

# with open('C:/test.txt', 'r', encoding="UTF-8") as name:
#     print(name.readlines())


# 练习案例

file = open('C:/test.txt', 'r', encoding="UTF-8")

data = file.readlines()

num = 0
for i in data:
    if i.count("hanser"):
        num += 1

print(f"{data}\n中有{num}个hanser")

file.close()

num = 0

# file = open('C:/test.txt', 'r', encoding="UTF-8")
#
# data = file.readlines()
#
# for i in data:
#     i.strip("\n")
#     strs = i.split(' ')
#     if strs.count("hanser"):
#         num += 1
#
# print(f"{data}\n中有{num}个hanser")
#
# file.close()


# file = open('C:/test.txt', 'r', encoding="UTF-8")
#
# data = file.read()
#
# print(f"{data}\n中有{data.count("hanser")}个hanser")

