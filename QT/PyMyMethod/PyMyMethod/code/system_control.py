import os
from ctypes import POINTER, cast

import comtypes
import pyperclip
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class SystemCtl:

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

if __name__ == '__main__':
    s = SystemCtl()
    s.getStrToPaste('string')
    print(s.getPasteContent())