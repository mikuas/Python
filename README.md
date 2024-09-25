# for循环写法

~~~python
# 1. 遍历列表
items = [1, 2, 3, 4]
for item in items:
    print(item)

# 2. 遍历字符串
text = "hello"
for char in text:
    print(char)

# 3. 使用 range()
for i in range(5):  # 0 到 4
    print(i)

# 4. 遍历字典
data = {'a': 1, 'b': 2, 'c': 3}
for key, value in data.items():
    print(f"键: {key}, 值: {value}")

# 5. 使用 enumerate()
items = ['apple', 'banana', 'cherry']
for index, value in enumerate(items):
    print(f"索引: {index}, 值: {value}")

# 6. 嵌套循环
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# 7. 列表推导式
squares = [x**2 for x in range(10)]
print(squares)

# 8. 使用 zip() 遍历多个可迭代对象
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} 的年龄是 {age}")

# 9. 反向遍历
items = [1, 2, 3, 4]
for item in reversed(items):
    print(item)

# 10. 使用生成器
def generate_numbers():
    for i in range(5):
        yield i

for num in generate_numbers():
    print(num)

# 11. 使用 itertools 模块
import itertools

# 生成笛卡尔积
for item in itertools.product(['A', 'B'], [1, 2]):
    print(item)

~~~

# if写法
### 逻辑运算符  用于连接多个条件，构建复杂的条件表达式

* and(于)

* or(或)

* not(非)

### 成员运算符 用于检查一个值是否存在于另一个集合中

* in(存在于)

* not in(不存在于)

  ~~~ 1pyt
  str = '1'

  strs = '123'

  print(str in strs) // 输出 True
  print(str not in strs) // 输出 False

  fruits = ['apple', 'banana', 'cherry']
  if 'banana' in fruits:
      print("香蕉在列表中")

  ~~~


### 身份运算符 用于比较两个对象的内存地址

* is(是同一对象)
* is not(不是同一对象)

~~~pyt
bool1 = True
bool2 = False

print(bool1 is bool2) // 输出 False
print(bool1 is not bool2) // 输出 True
~~~

~~~python
### 其他可调用的布尔函数 用于检查给定条件的真假
# any() 和 all()
conditions = [True, False, True]
if any(conditions):
    print("至少一个条件为真")

if all(conditions):
    print("所有条件都为真")

# 列表推导式中的条件

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# 使用 assert 语句
x = 10
assert x > 5, "x 必须大于 5"

# match 语句（Python 3.10 及更高版本）

def check_value(x):
    match x:
        case 1:
            print("值为 1")
        case 2:
            print("值为 2")
        case _:
            print("其他值")

check_value(1)

# 三元运算符

x = 10
result = "大于 5" if x > 5 else "不大于 5"
print(result)

~~~

