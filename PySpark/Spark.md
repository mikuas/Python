### Apache Spark是用于大规模数据(large-scala data)处理的统一(unified)分析引擎
* ### Spark是一款分布式的计算框架

#### PySpark编程模型
* #### 通过SparkContext对象,完成数据输入
* #### 输入数据后的到RDD对象,对RDD对象进行迭代计算
* #### 最终通过RDD对象的成员方法,完成数据输出工作

### RDD对象
* #### RDD全称为：弹性分布式数据集(Resilient Distributed Datasets)
* #### PySpark针对数据的处理,都是以RDD对象作为载体,即:
* #### 数据存储在RDD内
* #### 各类数据的计算方法,也都是RDD的成员方法
* #### RDD的数据计算方法,返回值依旧是RDD对象

### Python数据容器转RDD对象
* PySpark支持通过SparkContext对象的parallelize成员方法,将:
    * list
    * tuple
    * set
    * dict
    * str
* 转换为PySpark的RDD对象(
  * 字符串会被拆分为一个个的字符,存入RDD对象
  * 字典仅有Key会被存入RDD对象)

#### 如果要查看RDD里面有什么内容,需要用collect()方法
### 读取文件转RDD对象,textFile(文件路径)
### map方法(算子)
* map算子(功能:map算子,是将RDD的数据一条条处理(处理逻辑 基于map算子中接收的处理函数),返回新的RDD)
* 接受一个处理函数,可以用lambda表达式快速编写
* 对RDD内的元素逐个处理,并返回一个新的RDD
### 链式调用
* 对于返回值是新的RDD的算子,可以通过链式调用的方式多次调用算子
### flatMap算子
* 功能: 对RDD执行map操作,然后进行解除嵌套操作(计算逻辑和map一样,可以比map多出解除一层嵌套的功能)








