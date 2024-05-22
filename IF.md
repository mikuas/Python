## if

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

  ​

