import os
import shutil


def getDirFiles(path):
    return os.listdir(path)


def isDir(fileName):
    return os.path.isdir(fileName)


def getSuffixName(fileName):
    return fileName.split('.')[-1]


def reName(path):
    i = 0
    print(getDirFiles(path))
    for name in getDirFiles(path):
        print(name)
        if getSuffixName(name) == 'jpg' or getSuffixName(name) == 'png':
            if os.path.exists(os.path.join(path, f"{str(i)}.{getSuffixName(name)}")):
                i += 1
                continue

            # 移动并重命名文件
            shutil.move(os.path.join(path, name), os.path.join(path, f"{str(i)}.{getSuffixName(name)}"))
            i += 1

if __name__ == '__main__':
    reName('C:/test')
