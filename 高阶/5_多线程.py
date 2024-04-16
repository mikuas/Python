"""
threading

"""

import threading
import time

"""
thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])

* group: 暂时无用,未来功能的预留参数
* target: 执行的目标任务名
* args: 以元组的方式给执行任务传参
* kwargs: 以字典的方式给执行任务传参
* name: 线程名,一般不用设置

启动线程,让线程开始工作
thread_obj.start()
"""


def thread(element, two):

    while True:
        print(element, two)
        time.sleep(1)


def thread_t(element, two):

    while True:
        print(element, two)
        time.sleep(1)


# 创建两个线程
# threading.Thread(target=thread).start()
# threading.Thread(target=thread_t).start()

# 通过元组进行传参
threading.Thread(target=thread, args=('Hello_Python', 'Hello_World')).start()
# 通过字典进行传参
threading.Thread(target=thread_t, kwargs={'element': 24, 'two': 18}).start()





