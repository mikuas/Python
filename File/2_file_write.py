"""
文件的写入
打开文件
file_name = open(file, 'w', encoding='UTF-8')

文件写入
file_name.write('内容')

内容刷新
file_name.flush()
注意：直接调用write，内容并未真正写入文件，而是积攒在程序的内存中，称之为缓冲区
     当调用flush时，内容会真正写入文件
     这样做是避免频繁的操作，导致效率下降
"""


file = open('C:/test.txt', 'w', encoding='UTF-8')
# write写入，内容写入到内存中
file.write('Hello World!')
# 将内存中的内容，写入到硬盘的文件
# file.flush()
# 关闭文件，close方法内置了flush功能
file.close()

