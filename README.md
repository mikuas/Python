# Python for循环写法

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

#
~~~