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
from parentMethod import (
    KeyboardControl as Keyboard,
    SystemCtl as System,
    TerminalControl as Terminal,
    FileControl as FileCtl,
    Regedit as Re
)

class KeyboardControl(Keyboard):

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

    def keyPress(self, keys):
        result = keys.split(' ')
        for i in range(len(result)):
            pyautogui.press(result[i])

        return self

    def Hotkey(self, keys):
        pyautogui.hotkey(tuple(keys.split(' ')))

        return self


class SystemCtl(System):

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

    def copyFiles(self, copyFilePath, pastePath):
        if type(copyFilePath) is str:
            for _ in range(len(copyFilePath)):
                os.system(f'copy {copyFilePath[_]} {pastePath}')
        else:
            for _ in range(len(copyFilePath)):
                os.system(f'copy {copyFilePath[_]} {pastePath[_]}')

        return self

    def disableUser(self, userName):
        os.system(f'net user {userName} /active:no')

        return self

    def enableUser(self, userName):
        os.system(f'net user {userName} /active:yes')

        return self

    @staticmethod
    def setPassword(password, **kwargs):
        os.system('echo %username% > userName')

        with open('./userName', 'r') as file:
            userName = [file.readlines()[0].split()[0]][0].split()[0]

        os.system(f'net user {userName} {password}')
        os.remove('./userName')

        return userName

    def createUser(self, userName, password, manager=False):
        if manager:
            os.system(f'net user {userName} {password} /add')
            os.system(f'net localgroup Administrators {userName} /add')
        else:
            os.system(f'net user {userName} {password} /add')
        return self

    def deleteUser(self, userName):
        os.system(f'net user {userName} /del')

        return self

    @staticmethod
    # 获取系统音量
    def getAudioEndpointVolume(**kwargs):
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            return volume, volume.GetMasterVolumeLevelScalar()
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return None

    # 取消静音
    def clearMute(self):
        volume = self.getAudioEndpointVolume()[0]
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

    def setMute(self):
        volume = self.getAudioEndpointVolume()[0]
        if volume is None:
            print('无法获取音频设备')
            return self
        volume.SetMute(1, None)
        print('系统已静音')

        return self

    # 设置音量
    def setAudio(self, audio):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        volume_interface.SetMasterVolumeLevelScalar(audio, None)

        return self


class TerminalControl(Terminal):

    def __init__(self):
        pass

    @staticmethod
    def createTerminalArgs(args, types, helpInfo, requireds, default, defaultValue, isList, **kwargs):
        parser = argparse.ArgumentParser(description='getArgs')
        i = 0
        for arg in args:
            if isList[i]:
                parser.add_argument(f'-{arg}', type=types[i], nargs="+", help=helpInfo[i], required=requireds[i])
            else:
                if arg in default:
                    parser.add_argument(f'-{arg}', nargs=types[i], const=defaultValue[default.index(arg)], help=helpInfo[i], required=requireds[i])
                else:
                    parser.add_argument(f'-{arg}', type=types[i], help=helpInfo[i], required=requireds[i])
            i += 1
        return parser.parse_args()

    def runTerminalArgs(self, element, asynchronous=False):
        import subprocess
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

class FileControl(FileCtl):

    def __init__(self):
        pass

    @staticmethod
    def getDirFiles(path, **kwargs):
        return os.listdir(path)

    @staticmethod
    def getFilePackagePath(fileName, **kwargs):
        print(f"Requested file: {fileName}")
        basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basePath, fileName)

    @staticmethod
    def getFileAbsolutePath(fileName, **kwargs):
        return os.path.abspath(fileName)

    @staticmethod
    def isDir(fileName, **kwargs):
        return os.path.isdir(fileName)

    @staticmethod
    def getSuffixName(fileName, **kwargs):
        return fileName.split('.')[-1]

    @staticmethod
    def getDirPath(parent=None, **kwargs):
        from PySide6.QtWidgets import QFileDialog
        return QFileDialog.getExistingDirectory(parent, "选择目录")

    def imageReName(self, path):
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
        return [result, i]

class Regedit(Re):

    def __init__(self):
        pass

    def addLeftKeyClick(self, name, path, iconPath=None):
        if iconPath:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}" /v Icon /t REG_SZ /d "{iconPath}" /f')
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}\command" /ve /d "{path}" /f')
        else:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}\command" /ve /d "{path}" /f')
        return self

    def addFileLeftKeyClick(self, name, path, iconPath=None, args=False):
        if iconPath:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}" /v Icon /t REG_SZ /d "{iconPath}" /f')
            if args:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path + " %1"}" /f')
            else:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path}" /f')
        else:
            if args:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path + " %1"}" /f')
            else:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path}" /f')
        return self

if __name__ == '__main__':
    # Regedit().addFileLeftKeyClick('leftClick', 'notepad.exe', "C:\IDE\Icons\clion.ico", True)
    pass
