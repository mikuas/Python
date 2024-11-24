"""
文件的追加

打开文件，通过a模式
file_name = open(file, '', encoding='UTF-8')

文件写入
file_name.write(内容)

内容刷新
file_name.flush()
注意：
a模式，文件不存在会创建文件，文件存在会在最后，追加写入文件
"""
# 打开文件
# file = open('C:/test.txt', 'a', encoding='UTF-8')
# write写入
# file.write("Hello World!\n")
# flush刷新
# file.flush()
# close关闭
# file.close()


# 练习案例

# 读取文件
file_r = open("C:/bill.txt", "r", encoding='UTF-8')

# 创建文件
file_w = open("C:/bill.txt.bak", "w", encoding='UTF-8')
# 将文件写入file_w备份
file_w.write(file_r.read())

file_r.close()
# 丢弃标记为测试的数据
file_r = open("C:/bill.txt", "r", encoding='UTF-8')

file_a = open("C:/newbill.txt", "a", encoding='UTF-8')


for line in file_r:
    line = line.strip()
    if line.split(',')[-1] == "正式":
        file_a.write(line)
        file_a.write("\n")
    else:
        continue

file_w.close()
file_a.close()


file_r = open("C:/bill.txt", "r", encoding='UTF-8')

print(file_r.readlines())

file_r.close()
