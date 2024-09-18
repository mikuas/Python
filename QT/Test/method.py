import os
import sys
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import shutil
import comtypes
import pyautogui
import argparse
from PySide6.QtCore import QTimer

class KeyboardControl:

    def __init__(self):
        pass

    def inputText(self, text):
        pyautogui.typewrite(text)

        return self

    def keyUp(self, key):
        pyautogui.keyUp(key)

        return self

    def keyDown(self, key):
        pyautogui.keyDown(key)

        return self

    def keyPress(self, keys: str):
        # 依次点击
        result = keys.split(' ')
        for i in range(len(result)):
            pyautogui.press(result[i])

        return self

    def Hotkey(self, keys: str):
        # 共同点击
        pyautogui.hotkey(tuple(keys.split(' ')))

        return self


class SystemCtl:

    def __init__(self):
        pass

    def systemOption(self, time, element):
        if element == '关机':
            QTimer.singleShot(time, lambda: os.system("shutdown /s /f /t 0"))
        elif element == '重启':
            QTimer.singleShot(time, lambda: os.system("shutdown /r /f /t 0"))
        elif element == '注销':
            QTimer.singleShot(time, lambda: os.system("logoff"))
        elif element == '锁定':
            QTimer.singleShot(time, lambda: os.system("rundll32.exe user32.dll,LockWorkStation"))

        return self

    def copyFile(self, copyPath, pastePath):
        os.system(f'copy {copyPath} {pastePath}')

        return self

    def copyFiles(self, copyFilePath: list, pastePath):
        for _ in range(len(copyFilePath)):
            os.system(f'copy {copyFilePath[_]} {pastePath}')

        return self

    def disableUser(self, userName, parameters):
        os.system(f'net user {userName} /active:{parameters}')

        return self

    @staticmethod
    def setPassword(password):
        os.system('echo %username% > userName')

        file = open('./userName', 'r', encoding='utf-8')
        userName = file.readlines()
        userName = userName[0].split()[0]

        print(userName)

        os.system(f'net user {userName} {password}')
        file.close()
        os.remove('./userName')

        return userName

    def createUser(self, userName, password, manager=False):
        if manager:
            os.system(f'net user {userName} {password} /add')
            os.system(f'net localgroup Administrators {userName} /add')
        else:
            os.system(f'net user {userName} {password} /add')

        return self

    @staticmethod
    def getFilePath(fileName):
        print(f"Requested file: {fileName}")
        # 获取打包后的可执行文件所在的临时目录
        basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 构建文件的绝对路径
        return os.path.join(basePath, fileName)

    @staticmethod
    # 获取系统音量
    def getAudioEndpointVolume():
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            # GetMasterVolumeLevelScalar()
            return volume
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return None

    # 取消静音
    def clearMute(self):
        volume = self.getAudioEndpointVolume()
        if volume is None:
            print("无法获取音频设备")
            return self

        try:
            if volume.GetMute():
                volume.SetMute(0, None)
                print("系统已解除静音")
                return self
            else:
                print("系统未处于静音状态")
                return self
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return self

    # 设置音量
    def setAudio(self, num: float):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        # 设置音量（0.0到1.0之间的浮点数）
        volume_interface.SetMasterVolumeLevelScalar(num, None)

        return self

class TerminalControl:
    def __init__(self):

        pass

    @staticmethod
    def terminalArgs():
        # 创建解析器对象
        parser = argparse.ArgumentParser(description="演示如何通过终端传参")

        # 添加参数
        parser.add_argument('-e', '--element', type=str, help='None', required=False)
        parser.add_argument('-t', '--time', type=int, help='None', required=False)

        # 添加到列表
        """
        parser.add_argument('--list', type=str, help='None', nargs='+', required=True)
        """

        # 解析参数
        return parser.parse_args()

    @staticmethod
    def createTerminalArgs(args: list, types: list, helpInfo: list, requireds: list[bool]):
        parser = argparse.ArgumentParser(description='getArgs')
        i = 0
        for arg in args:
            if types[i] == 'list':
                parser.add_argument(f'-{arg}', type=str, nargs="+", help=helpInfo[i], required=requireds[i])
            else:
                parser.add_argument(f'-{arg}', type=str, help=helpInfo[i], required=requireds[i])
            i += 1
        return parser.parse_args()

    def runTerminalArgs(self, element: list,asynchronous=False):
        import subprocess
        '''
        element
        ['运行方式(bash, cmd, python...)', 'filePath', args...]
        python -参数 args...
        '''
        if asynchronous:
            processes = []
            # 异步运行
            # args1,2,3 为 fileName 的 位置传参
            proc = subprocess.Popen(element)
            processes.append(proc)

            for proc in processes:
                # 等待所有的进程完成
                proc.wait()
        else:
            subprocess.run(element)

        return self

class FileControl:

    def __init__(self):
        pass

    @staticmethod
    def getDirFiles(path):
        return os.listdir(path)

    @staticmethod
    def isDir(fileName):
        return os.path.isdir(fileName)

    @staticmethod
    def getSuffixName(fileName):
        return fileName.split('.')[-1]

    @staticmethod
    def getDirPath():
        from PySide6.QtWidgets import QFileDialog
        return QFileDialog.getExistingDirectory(None, "选择目录")

    def imageReName(self, path):
        """
        :param path: DirPath
        :return: self
        支持 jpg png
        """
        i = 0
        print(self.getDirFiles(path))
        result = []
        for name in self.getDirFiles(path):
            if self.getSuffixName(name) == 'jpg' or self.getSuffixName(name) == 'png':
                result.append(name)
                if os.path.exists(os.path.join(path, f"{str(i)}.{self.getSuffixName(name)}")):
                    i += 1
                    continue

                # 移动并重命名文件
                shutil.move(os.path.join(path, name), os.path.join(path, f"{str(i)}.{self.getSuffixName(name)}"))
                i += 1
        return result

if __name__ == '__main__':
    KeyboardControl.Hotkey(None, 'win tab')

