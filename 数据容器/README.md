
# 数据容器

### [列表](1_list列表.py)

列表的下表索引(从零开始,依次递增)
反向索引,从后往前:从-1开始,依次递减

~~~python
# 语法:   列表[下标索引]

ls = [1, 2, 3]
print(ls[0])         # 输出 1
print(ls[-1])        # 输出 3

# 如果列表是嵌套的列表,同样也支持下标索引
# 语法:   列表[下标索引][下标索引]

ls = [1, 2, 3, [1, 2, 3]]

print(ls[3][0])  # 输出 1
~~~

### 列表的查询功能(方法)
#### 查找某元素的下标
#### 功能：查找指定元素在列表的下标，如果找不到，报错ValueError

语法：列表.index(元素)

index就是列表的对象(变量)内置的方法(函数)

~~~python
ls = [1, 2, 3]

ind = ls.index(2)

print(ind)      # 输出 1
~~~

### 列表的修改功能(方法)
#### 修改特定位置(索引)的元素值

语法：列表[下标] = 值
~~~python
ls = [1, 2, 3, 4, 5]

ls[2] = 'Hello'

print(ls)   # 输出 [1, 2, 'Hello', 3, 4, 5]

ls[-1] = 'Python'
print(ls)   # 输出 [1, 2, 'Hello', 3, 4, 'Python']
~~~

### 插入元素

语法：列表.insert(下标，元素)，在指定的下标位置，插入指定的元素
~~~python
ls = [1, 2, 3, 4, 5]

ls.insert(1, 'Hello')

print(ls)       # 输出 [1, 'Hello', 2, 3, 4, 5]
~~~

### 追加元素：

语法：列表.append(元素)，将指定元素，追加到列表的尾部
~~~python
ls = [1, 2, 3, 4, 5]

ls.append('Hello')

print(ls)       # 输出 [1, 2, 3, 4, 5, 'Hello']
~~~

### 追加一批元素

语法：列表.extend(其他数据容器)，将其它数据容器的内容依次取出，依次追加到列表尾部

~~~python
ls = [1, 2, 3, 4, 5]
ls2 = [1, 1, 4, 5]

ls.extend(ls2)

print(ls)       # 结果是 [1, 2, 3, 4, 5, 1, 1, 4, 5]
~~~

### 删除元素：

语法1：del 列表 [下标]

语法2：列表.pop(下标)

~~~python
ls = [1, 2, 3, 4, 5]

del ls[-1]

print(ls)       # 输出 [1, 2, 3, 4]

result = ls.pop(0)      # pop()方法的返回值是被删除的数
print(ls, result)       # 结果是 [2, 3, 4], 1
~~~

### 删除某元素在列表中的第一个匹配项

语法：列表.remove(元素)

~~~python
ls = [1, 1, 4, 5]

ls.remove(1)

print(ls)       # 输出 [1, 4, 5]
~~~

### 清空列表内容

语法：列表.clear()
~~~python
ls = [1, 2, 3, 4, 5]

print(ls)       # 输出 []
~~~

### 统计某元素在列表内的数量

语法：列表.count(元素)
~~~python
ls = [1, 1, 4, 1, 5]

print(ls.count(1))      # 输出 3
~~~

### 统计列表内，有多少元素

语法：len(列表)

~~~python
ls  = [1, 2, 3, 4, 5]
# len的返回值是 int
print(len(ls))      # 输出 5
~~~

### 列表的sort方法

~~~python
""" 
语法 
sort(Key = 选择排序依据的函数, reverse=True|False)
"""

# 参数Key,是要求传入一个函数,表示将列表的每一个元素都传入函数中,返回排序的依据
# 参数reverse,是否反转排序结果,True表示降序,False表示升序

ls = [['a', 33], ['b', 55], ['c', 11]]

def sorts(element):
    element[0]

ls.sort(key=sorts, reverse=False)
print('!!!', ls)        # 输出 !!! [['a', 33], ['b', 55], ['c', 11]]

ls.sort(key=sorts, reverse=True)
print('!!!', ls)        # 输出 !!! [['c', 11], ['b', 55], ['a', 33]]

# 匿名函数lambda形式
ls.sort(key=lambda element: element[1], reverse=True)
print('!!!!', ls)       # !!!! [['b', 55], ['a', 33], ['c', 11]]
~~~

### 反转列表

语法：列表.reverse()
~~~python
ls = [1, 2, 3, 4, 5]

ls.reverse()
print(ls)       # 输出 [5, 4, 3, 2, 1]
~~~

---

[元组](2_tuple元组.py)

元组一旦定义完成，就不可以修改
~~~python
# 定义单个元素

tp = ("hello", ) # 如果元组只有一个元素，那么这个元素后面要加,
print(type(tp), tp)

# 元组也支持嵌套

tp = ("hello", "world", ("hello", "world"))

# 通过下标索引取出内容
print(tp[2][0])

# 查找某个数据 index
print(tp.index("world"))

# 统计某个数据在当前元组出现的次数 count
print(tp.count("hello"))

# 统计元组内的元素个数 len
print((len(tp)))
~~~

---

[字符串](3_str字符串.py)

字符串是一个无法修改的数据容器
~~~python
my_str = "fuck you"

# 通过下标索引取出元素
print(my_str[5])        # 输出 y

# 通过指定元素查找指定下标索引
# 语法：字符串.index(字符串)
print(my_str.index("y"))    # 输出 5
~~~

### 字符串的替换
语法：字符串.replace(字符串1,字符串2)

* 功能：将字符串内的`全部内容`：字符串1，替换为字符串2

* 注意：不是修改字符串本身，而是得到了一个新的字符串
~~~python
my_str = "fuck in the fuck"

new_my_str = my_str.replace("fuck", "good")

print(my_str, new_my_str)   # 输出 fuck in the fuck, good in the good
~~~

### 字符串的分割

语法：字符串.split(分隔字符串)

* 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中

* 注意：字符串本身不变，而是得到了一个列表对象
~~~python
my_str = "Hello World Fan Ikun"

new_list = my_str.split(' ')

print(new_list)     # 输出 Hello World Fan Ikun， ['Hello', 'World', 'Fan', 'Ikun']
~~~

### 字符串的规整操作(去除前后空格,回车换行符)

语法：字符串.strip()

* 字符串本身不变，而是得到了一个新的字符串
* 字符串的规整操作(去除前后指定字符串)

语法：字符串.strip(字符串)-->按照单个字符

~~~python
my_str = " Hello World "

new_str = my_str.strip()

print(my_str)   # 输出 \'空格'Hello World
print(new_str)  # 输出 Hello World

my_str = "114Hello World114"

new_str = my_str.strip("14")

print(my_str)
print(new_str)  # 输出 Hello World
~~~

### 统计字符串中某字符串出现的次数,count

~~~python
my_str = "114Hello World114"

count = my_str.count("l")

print(f"字符串{my_str}中l出现的次数是{count}次") # 输出 3

### 统计字符串的长度,len

my_str = "114Hello World114"

print(len(my_str)) # 输出 17
~~~

---

[集合](5_set集合.py)

集合是无序的，所以集合不支持下标索引访问

### 添加新元素

语法：集合.add(元素) 将指定元素，添加到集合内
* 结果：集合本身被修改，添加了新元素
~~~python
my_set = {"Hello"}

my_set.add("World")

print(my_set)   # 输出   {'Hello', 'World'}
~~~

### 移除元素

语法：集合.remove(元素) 将指定元素，从集合内移除
* 结果：集合本身被修改，移除了元素

~~~python
my_set = {'Hello', 'World'}

my_set.remove('World')

print(my_set)   # 输出 Hello
~~~

### 从集合中随机取出元素

语法：集合.pop() 功能：从集合中随机取出一个元素
* 结果：会得到一个元素的结果，同时集合本身被修改，元素被移除

~~~python
my_set = {"Hello", "World"}
# 返回被移除的元素
element = my_set.pop()  # 假设移除的是 Hello

print(my_set)   # 输出 World
print(element)  # 输出 Hello
~~~

### 清空集合

语法：集合.clear
~~~python
my_set = {"Hello", "World"}

my_set.clear()

print(my_set)   # 输出 {}
~~~

### 取出两个集合的差集

语法：集合1.difference(集合2) 功能：取出集合1和集合2的差集(集合1有而集合2没有的)
* 结果：得到一个新的集合，集合1和集合2不变

~~~python
set1 = {1, 1, 4, 5}
set2 = {1, 9, 1, 9}

set3 = set1.difference(set2)

print(set3)     # 输出 {4， 5}
~~~

### 消除两个集合的差集

语法：集合1.difference_update(集合2)
* 功能：对比集合1和集合2，在集合1内，删除集合2相同的元素。
* 结果：集合1被修改，集合2不变

~~~python
set1 = {1, 1, 4, 5}
set2 = {1, 9}

set1.difference_update(set2)
    
print(set1)     # 输出 {4, 5}
print(set2)     # 输出 {1, 9}
~~~

### 两个集合合并为一个

语法：集合1.union(集合2)
* 功能：将集合1和集合2组成新集合
* 结果：得到新集合，集合1和集合2不变

~~~python
set1 = {1, 1, 4, 5}
set2 = {1, 9, 1, 9}

set3 = set1.union(set2)

print(set3)     # 输出 {1, 4, 5, 9}
~~~

### 统计集合元素数量

语法：len(集合)

---

[字典](6_dict字典(字典，映射).py)

字典数据的获取

字典同集合一样，不可以使用下标索引

但是字典可以通过`key值`来取得对应的`value`

~~~python
my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}\

print(my_dict['周杰轮'])       # 输出 88
~~~

### 字典的嵌套

字典key和value可以是任意数据类型(`key不可为字典`)

### 新增元素

语法：字典[key] = value 结果：字典被修改，新增了元素

### 更新元素

语法：字典[key] = [value] 结果：字典被修改，元素被更新
* 注意：字典key不可以重复，所以对已存在的key执行上述操作，就是更行value值
~~~python
my_dict = {'chinese': 88, 'english': 77}

my_dict['chinese'] = 100
print(my_dict)      # 输出 {'chinese': 100, 'english': 77}

my_dict['math'] = 100
print(my_dict)      # 输出 {'chinese': 100, 'english': 77, 'math': 100}
~~~

### 删除元素
语法：字典.pop(key)
* 结果：获得指定key的value，同时字典被修改，指定key的数据被删除
~~~python
my_dict = {'chinese': 100, 'english': 77, 'math': 100}
# 返回Value
result = my_dict.pop('chinese')

print(my_dict, result)   # 输出 {'english': 77, 'math': 100}, 100
~~~

### 清空字典

语法：字典.clear() 
* 结果：字典被修改，元素被清空
~~~python
my_dict = {'chinese': 100, 'english': 77, 'math': 100}

my_dict.clear()

print(my_dict)      # 输出 {}
~~~

### 获取全部的key

语法：字典.keys()
* 结果：得到字典中的全部key
~~~python
my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

print(my_dict.keys())   # 结果 dict_keys(['王力鸿', '周杰轮', '林俊节'])
~~~

### 统计字典的元素数量

语法：len(字典)

---

[序列/切片](4_数据容器(序列)的切片.py)

### 序列的常用操作--切片
#### 序列支持切片，即：列表，元组，字符串，均支持进行切片操作
    切片：从一个序列中，取出一个子序列
        语法：序列[起始下标:结束下标:步长]
        表示从序列中，从指定位置开始，依次去除元素，到指定位置结束，得到一个新序列：
        起始下标表示从何处开始，可以留空，留空视作从头开始
        结束下标(不含)表示何处结束，可以留空，留空视作截取到结尾
        步长表示，依次取元素的间隔
            步长1表示，一个个的取元素
            步长2表示，每次跳过1个元素取
            步长N表示，每次跳过N-1个元素取
            步长为负数表示，反向取(注意，起始下标和结束下标也要反向标记)

~~~python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new = my_list[-1:-7:-2]     # 不包括结束下标
new2 = my_list[1:7:3]
print(new, new2)    # 输出 [9, 7, 5], [2, 5]
~~~

---

## python中的数据容器:

>一种可以容纳多分数据的数据类型,容纳的每一份数据称之为1个元素 \
每一个元素可以是任意类型的数据,如字符串,数字,布尔等...

---

## 数据容器根据特点的不同,如:

    *是否支持重复元素
    *是否可以修改
    *是否有序,等...
    分五类,分别是:
    1.列表(list) --> []
    2.元组(tuple) --> ()
    3.字符串(str) --> ""
    4.集合(set) --> {}
    5.字典(dict) --> {}

---

## 数据容器分类

---

### 是否支持下标索引

    支持：列表，元组，字符串，--序列类型
    不支持：集合，字典 --非序列类型

---

### 是否支持重复元素

    支持：列表，元组，字符串 --序列类型
    不支持：集合，字典 --非序列类型

---

### 是否可以修改

    支持：列表，集合，字典
    不支持：元组，字符串
    
---

### 基于各类数据容器的特点，它们的应用场景如下

    列表：一批数据，可修改，可重复的存储场景
    元组：一批数据，不可修改，可重复的存储场景
    字符串：一串字符串的存储场景
    集合：一批数据，去重存储场景
    字典：一批数据，可用Key检索Vaue的存储场景l

---

### 数据容器的通用操作--遍历

    5类数据容器都支持for循环遍历
    列表，元组，字符串支持while循环，集合，字典不支持(无法下标索引)

---

### 数据容器的通用统计功能
#### 大小比较，通过ASCII码表比较
>字符串比较 \
字符串是按位比较，也就是一位位进行对比，只要有一位大，那么整体就大
~~~python
len(容器)     # 统计容器的元素个数
max(容器)     # 统计容器的最大元素
min(容器)     # 统计容器的最小元素
~~~

---
### 数据的通用转换功能

~~~python
list(容器)            # 将给定容器转换为列表
str(容器)             # 将给定容器转换为字符串
tuple(容器)           # 将给定容器转换为元组
set(容器)           # 将给定容器转换为集合
~~~

### 容器的通用排序功能

sorted(容器,[revers=True])
* <revers默认是False,True表示将结果进行反转>
* 将给定容器进行排序,排序的结果会变为列表
~~~python
my_list = [1, 1, 4, 5, 1, 4, 1, 9, 1]

fs = sorted(my_list)
ts = sorted(my_list, reverse=True)

print(fs, ts)   # 输出 [1, 1, 1, 1, 1, 4, 4, 5, 9],  [9, 5, 4, 4, 1, 1, 1, 1, 1]
~~~