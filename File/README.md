# 文件操作

### open()打开函数
~~~python
file = open('files_path', 'r|w|a', encoding='UTF-8')

'''
r：以只读方式打开文件，文件指针将会放在文件的开头，这是默认模式
w：打开一个文件用于写入，如果该文件以存在则打开文件，并从头开始编辑，原有内容会被删除，如果该文件不存在，创建新文件
a：打开一个文件用于追加，如果该文件以存在，新的内容将会被写入到已有内容之后，如果该文件不存在，创建新文件进行写入
'''
~~~

### 读取文件-read()方法

语法：文件对象.read(num)
~~~python
file = open('', 'r', encoding='utf-8')

file.read(num) # num 表示要从文件中读取的数据长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有的数据
~~~

### readlines()方法

语法：文件对象.readlines()
~~~python
# readlines可以按照行的方式把整个文件中的内容进行一次性读取

file.readlines() # 返回一个列表 其中每一行的数据为一个元素
~~~

### readline()方法

语法：文件对象.readline()
~~~python
# 一次读取一行内容
file.readline()
~~~

### for循环读取文件

语法：for 临时变量 in open(file_name, mode='r'):

~~~python
for i in open('file_path', 'r'): # 每一个临时变量，就记录了文件的一行数据
    pass
~~~

### close()关闭文件对象

语法：文件对象.close()

~~~python
file.colse()  # 如果不调用close，同时程序没有停止运行，那么这个文件将一直被python程序占用
~~~

### with open语法

~~~python
with open('file_path', 'r|w|a', encoding='utf-8') as name:
    name.readlines()

'''
可通过在with open的语句块中对文件进行操作
可以在操作完成后自动关闭close文件，避免遗忘掉close方法
'''# Python 文件打开模式

~~~

# Python 文件打开模式
~~~python
# 只读模式
- 'r'：只读（默认）

# 写入模式
- 'w'：写入（覆盖）
- 'x'：排他性创建（文件不存在时创建）

# 追加模式
- 'a'：追加

# 更新模式
- 'r+'：读写
- 'w+'：写入和读取（覆盖）
- 'a+'：追加和读取

# 二进制模式
- 'rb'：二进制只读
- 'wb'：二进制写入
- 'ab'：二进制追加
- 'r+b' 或 'rb+'：二进制读写
- 'w+b' 或 'wb+'：二进制写入和读取
- 'a+b' 或 'ab+'：二进制追加和读取

# 文本模式
- 'rt'：文本只读（默认）
- 'wt'：文本写入
- 'at'：文本追加
- 'r+t' 或 'rt+'：文本读写
- 'w+t' 或 'wt+'：文本写入和读取
- 'a+t' 或 'at+'：文本追加和读取
~~~