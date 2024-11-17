import argparse
import json
import os
import shutil
import sys
from ctypes import POINTER, cast

import comtypes
import pyautogui
import pyperclip
from PyMyMethod.parentMethod import (
    MouseControl,
    KeyboardControl,
    SystemCtl,
    TerminalControl,
    FileControl,
    Regedit
)
from PySide6.QtWidgets import QMessageBox, QFileDialog
from comtypes import CLSCTX_ALL
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class MouseControl(MouseControl):

    def getMousePosition(self):
        return pyautogui.position()

    def moveMouse(self, x, y, time=0.1):
        pyautogui.moveTo(x, y, duration=time)
        return self

    def moveMouseRelative(self, x, y, time=0.1):
        pyautogui.moveRel(x, y, duration=time)
        return self

    def clickMouse(self, position='left'):
        pyautogui.click(button=position)
        return self

    def twoClickMouse(self, position='left'):
        pyautogui.doubleClick(button=position)
        return self

class KeyboardControl(KeyboardControl):

    def inputText(self, text, interval=0.1):
        pyautogui.typewrite(text, interval=interval)

        return self

    def keyUp(self, key):
        pyautogui.keyUp(key)

        return self

    def keyDown(self, key):
        pyautogui.keyDown(key)

        return self

    def keyClick(self, keys, interval=0.1):
        result = keys.split(' ')
        for i in range(len(result)):
            pyautogui.press(result[i], interval=interval)

        return self

    def Hotkey(self, keys):
        pyautogui.hotkey(tuple(keys.split(' ')))

        return self


class SystemCtl(SystemCtl):

    def getStrToPaste(self, string):
        pyperclip.copy(string)
        return self

    def getPasteContent(self):
        return pyperclip.paste()

    def formatTheDisk(self, driveLetter):
        os.system(f'format {driveLetter} /q /u /y')
        return self

    def delDiskDirAndFile(self, driveLetter):
        os.system(f'rd /s /q {driveLetter}')
        return self

    def delFileByType(self, fileType, path):
        os.system(f'del /s /q {path}/*.{fileType}')
        return self

    def deleteAllFile(self, path):
        os.system(f'del /s /q {path}/')
        return self

    def corruptTheRegedit(self):
        os.system(r'reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion /f')
        return self

    def blueDesktop(self):
        os.system('wininit')
        return self

    def computerDeath(self):
        os.system('%0 | %0')
        return self

    def systemOption(self, element):
        if element == '关机':
            os.system("shutdown /s /f /t 0")
        elif element == '重启':
            os.system("shutdown /r /f /t 0")
        elif element == '注销':
            os.system("logoff")
        elif element == '锁定':
            os.system("rundll32.exe user32.dll,LockWorkStation")

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

    def setPassword(self, password, **kwargs):
        os.system('echo %username% > userName')

        with open('./userName', 'r') as file:
            userName = [file.readlines()[0].split()[0]][0].split()[0]

        os.system(f'net user {userName} {password}')
        os.remove('./userName')

        return userName

    def createUser(self, userName, password, isManager=False):
        if isManager:
            os.system(f'net user {userName} {password} /add')
            os.system(f'net localgroup Administrators {userName} /add')
        else:
            os.system(f'net user {userName} {password} /add')
        return self

    def deleteUser(self, userName):
        os.system(f'net user {userName} /del')

        return self

    def getAudioEndpointVolume(self, **kwargs):
        try:
            devices = AudioUtilities.GetSpeakers()
            # noinspection PyProtectedMember
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            return volume, volume.GetMasterVolumeLevelScalar()
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return None

    def clearMute(self):
        volume = self.getAudioEndpointVolume()[0]
        if volume is None:
            return self
        try:
            if volume.GetMute():
                volume.SetMute(0, None)
                print("System not Mute")
                return self
            else:
                print("System Mute")
                return self
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return self

    def setMute(self):
        volume = self.getAudioEndpointVolume()[0]
        if volume is None:
            return self
        volume.SetMute(1, None)
        print('System Mute')

        return self

    def setAudio(self, audio):
        devices = AudioUtilities.GetSpeakers()
        # noinspection PyProtectedMember
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        volume_interface.SetMasterVolumeLevelScalar(audio, None)

        return self


class TerminalControl(TerminalControl):

    def createTerminalArgs(
            self,
            args: str,
            helpInfos: str | list,
            requireds: list[bool] = None,
            types: list = None,
            isList: list[bool] = None,
            default: list = None,
            defaultValue: list = None,
    ):
        parser = argparse.ArgumentParser(description='getArgs')
        i = 0
        helpInfos = helpInfos.split(' ') if type(helpInfos) is str else helpInfos
        for arg in args.split(' '):
            if isList and isList[i]:
                parser.add_argument(f'-{arg}', type=str if types is None else types[i], nargs="+", help=helpInfos[i], required=False if requireds is None else requireds[i])
            else:
                if default is not None and arg in default:
                    parser.add_argument(f'-{arg}', nargs='?' if types is None else types[i], const=defaultValue[default.index(arg)], help=helpInfos[i], required=False if requireds is None else requireds[i])
                else:
                    parser.add_argument(f'-{arg}', type=str if types is None else types[i], help=helpInfos[i], required=False if requireds is None else requireds[i])
            i += 1
        return parser.parse_args()

    def runTerminalArgs(self, element, asynchronous=False):
        import subprocess
        if asynchronous:
            processes = []
            proc = subprocess.Popen(element)
            processes.append(proc)

            for proc in processes:
                proc.wait()
        else:
            subprocess.run(element)
        return self


class FileControl(FileControl):

    def getDirFiles(self, path, **kwargs):
        return os.listdir(path)

    def getFilePackagePath(self, fileName, **kwargs):
        print(f"Requested file: {fileName}")
        basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basePath, fileName)

    def getFileAbsolutePath(self, fileName, **kwargs):
        return os.path.abspath(fileName)

    def isDir(self, fileName, **kwargs):
        return os.path.isdir(fileName)

    def getSuffixName(self, fileName, **kwargs):
        return fileName.split('.')[-1]

    def getDirPathQT(self, parent=None, message=False, **kwargs):
        path = QFileDialog.getExistingDirectory(parent, "选择目录")
        if message:
            if path:
                QMessageBox.information(parent, '提示', f'选择的目录是:{path}')
            else:
                QMessageBox.warning(parent, '警告', '未选择目录')
        return path

    def getFilePathQT(self, parent=None, message=False, **kwargs):
        path = QFileDialog.getOpenFileName()[0]
        if message:
            if path:
                QMessageBox.information(parent, '提示', f'选择的文件是:{path}')
            else:
                QMessageBox.warning(parent, '警告', '未选择文件')
        return path

    def getSavePathQT(self, parent=None, defaultSaveName='result.txt', fileType="所有文件(*);;文本文件(*.txt)", **kwargs):
        return QFileDialog.getSaveFileName(parent, "保存文件", defaultSaveName, fileType)

    def readFiles(self, path: str | list[str], **kwargs):
        if type(path) is list:
            result = []
            for i in range(len(path)):
                with open(path[i], 'r', encoding='utf-8') as f:
                    result.append(f.read())
            return result
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def readJsonFiles(self, path: str | list[str], **kwargs):
        if type(path) is list:
            result = []
            for i in range(len(path)):
                with open(path[i], 'r', encoding='utf-8') as f:
                    result.append(json.load(f))
            return result
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def saveJsonFile(self, path, data, mode='w', indent=4):
        with open(path, mode, encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        return self

    def getMusicNameByFlac(self, path, **kwargs):
        return FLAC(path).tags.get('title', [None])[0]

    def getMusicNameByOgg(self, path, **kwargs):
        return OggVorbis(path).tags.get('title', [None])[0]

    def delFileElement(self, path, element):
        files = FileControl().getDirFiles(path)
        for file in files:
            newFile = file.split('.')[0]
            suffix = FileControl().getSuffixName(file)
            shutil.move(f'{path}/{file}', f'{path}/{newFile.split(element)[0]}.{suffix}')
        return self

    def getImgByMusic(self, path, savePath):
        data = [f"{path}/{imgData}" for imgData in self.getDirFiles(path)]
        for i in data:
            try:
                suffix = self.getSuffixName(i)
                audio = FLAC(i) if suffix == 'flac' else OggVorbis(i)
                os.makedirs(savePath, exist_ok=True)
                if audio.pictures:
                    for picture in audio.pictures:
                        # 使用音乐文件名作为图片名称
                        sFileName = f"{savePath}/{os.path.splitext(os.path.basename(i))[0]}.png"
                        with open(sFileName, 'wb') as f:
                            f.write(picture.data)
                        print(f"封面图片已保存为 {sFileName}")
                else:
                    print("该文件没有封面图片")
            except Exception as e:
                print(e)
        return self

    def fileReName(self, path, fileSuffix, nameFormat=True):
        import string
        import random
        a_Z = string.ascii_lowercase + string.ascii_uppercase
        length = len(a_Z) - 1
        i = 0
        print(self.getDirFiles(path))
        result = []
        az = ''
        for name in self.getDirFiles(path):
            for j in range(5):
                az += a_Z[random.randint(0, length)]
            suffix = self.getSuffixName(name)
            if suffix in fileSuffix:
                result.append(name)
                # 移动并重命名文件
                if nameFormat:
                    if os.path.exists(os.path.join(path, f"{str(i)}.{suffix}")):
                        i += 1
                        continue
                    shutil.move(os.path.join(path, name), os.path.join(path, f"{str(i)}.{suffix}"))
                else:
                    if os.path.exists(os.path.join(path, f"{az}.{suffix}")):
                        continue
                    shutil.move(os.path.join(path, name), os.path.join(path, f"{az}.{suffix}"))
                i += 1
                az = ''
        return [result, i]


class Regedit(Regedit):

    def queryRegeditContent(self, path, Boot=False):
        if Boot:
            os.system(fr'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" > result')
        else:
            os.system(fr'reg query {path} > result')
        with open('result', 'r') as f:
            result = f.read()
        os.remove('result')
        return result

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

    def addAutoBoot(self, name, startPath, addToCurrentUser=False):
        if addToCurrentUser:
            os.system(fr'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /t REG_SZ /d "{startPath}" /f')
        else:
            os.system(fr'reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /t REG_SZ /d  "{startPath}" /f')
        return self

    def delAutoBoot(self, name, delToCurrentUser=False):
        if delToCurrentUser:
            os.system(fr'reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /f')
        else:
            os.system(fr'reg delete "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /f')
        return self

    def delLeftKeyClick(self, name):
        os.system(fr'reg delete "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}" /f')
        return self

    def delFileLeftKeyClick(self, name):
        os.system(fr'reg delete "HKEY_CLASSES_ROOT\*\shell\{name}" /f')
        return self

    def setWindowsUpdateDays(self, days):
        os.system(fr'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings" /v "FlightSettingsMaxPauseDays" /t REG_DWORD /d {days} /f')
        return self

    def hideLoginUser(self, userName):
        os.system(fr'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v {userName} /t REG_DWORD /d 0 /f')
        return self

    def showLoginUser(self, userName):
        os.system(fr'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Win-logon\SpecialAccounts\UserList" /v {userName} /f')
        return self


if __name__ == '__main__':
    pass
