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

### 其他可调用的布尔函数 用于检查给定条件的真假

* all()：如果可迭代对象中的所有元素都为真，则返回 True

* any()：如果可迭代对象中的任何元素都为真，则返回 True

  