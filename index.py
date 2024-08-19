import os
import sys
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import comtypes
import pyautogui

class KeyboardControl:

    def __init__(self):
        pass

    def keyUp(self, key):
        pyautogui.keyUp(key)

        return self

    def keyDown(self, key):
        pyautogui.keyDown(key)

        return self

    def keyPress(self, key: str):
        # 依次点击
        result = key.replace(' ', '').split(',')
        for i in range(len(result)):
            pyautogui.press(result[i])

        return self

    def keyHotkey(self, key: str):
        # 共同点击
        pyautogui.hotkey(tuple(key.replace(' ', '').split(',')))

        return self


class SystemControl(object):

    def __init__(self):
        pass

    def copyFile(self, copyPath, pastePath):
        os.system(f'copy {copyPath} {pastePath}')

        return self

    def disableTaskManage(self, num):
        # 1 disable | 0 enable
        os.system(f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')

        return self

    @staticmethod
    def getFilePath(self, fileName):
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
            return volume
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return None

    # 取消静音
    def clearMute(self):
        volume = self.getAudioEndpointVolume()
        if volume is None:
            print("无法获取音频设备")
            return

        try:
            if volume.GetMute():
                volume.SetMute(0, None)
                print("系统已解除静音")
            else:
                print("系统未处于静音状态")
        except comtypes.COMError as e:
            print(f"COMError: {e}")

    # 设置音量
    def setAudio(self, num: float):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        # 设置音量（0.0到1.0之间的浮点数）
        volume_interface.SetMasterVolumeLevelScalar(num, None)

        return self

if __name__ == '__main__':
    KeyboardControl().keyHotkey('ctrl,alt,space')






