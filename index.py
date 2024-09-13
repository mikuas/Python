import os
import sys
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import pygetwindow as gw
import comtypes
import pyautogui
import argparse

class KeyboardControl:

    def __init__(self):
        pass

    def inputText(self, text) -> 'KeyboardControl':
        pyautogui.typewrite(text)

        return self

    def keyUp(self, key) -> 'KeyboardControl':
        pyautogui.keyUp(key)

        return self

    def keyDown(self, key) -> 'KeyboardControl':
        pyautogui.keyDown(key)

        return self

    def keyPress(self, key: str) -> 'KeyboardControl':
        # 依次点击
        result = key.split(' ')
        for i in range(len(result)):
            pyautogui.press(result[i])

        return self

    def Hotkey(self, key: str) -> 'KeyboardControl':
        # 共同点击
        pyautogui.hotkey(tuple(key.split(' ')))

        return self


class SystemControl:

    def __init__(self):
        pass

    def copyFile(self, copyPath, pastePath) -> 'SystemControl':
        os.system(f'copy {copyPath} {pastePath}')

        return self

    def copyFiles(self, copyFilePath: list, pastePath) -> 'SystemControl':
        for _ in range(len(copyFilePath)):
            os.system(f'copy {copyFilePath[_]} {pastePath}')

        return self

    class OS:
        def __init__(self):
            pass

        def powerOff(self):
            os.system('shutdown -s -f -t 0')

            return self

        def reboot(self):
            os.system('shutdown -r -t 0')

            return self

        def logout(self):
            os.system('logoff')

            return self

        def lockout(self):
            os.system('rundll32.exe user32.dll,LockWorkStation')

            return self

    def disableUser(self, userName, parameters) -> 'SystemControl':
        os.system(f'net user {userName} /active:{parameters}')

        return self

    def disableCMD(self) -> 'SystemControl':
        os.system('reg add "HKCU\Software\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 2 /f')

        return self

    def disablePowershell(self) -> 'SystemControl':
        os.system('reg add "HKCU\Software\Microsoft\PowerShell/1\ShellIds\Microsoft.PowerShell" /v ExecutionPolicy /t REG_SZ /d Restricted /f')

        return self

    def disableTaskManage(self, num) -> 'SystemControl':
        os.system(f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')

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

    def createUser(self, userName, password, manager=False) -> 'SystemControl':
        if manager:
            os.system(f'net user {userName} {password} /add')
            os.system(f'net localgroup Administrators {userName} /add')
        else:
            os.system(f'net user {userName} {password} /add')

        return self

    @staticmethod
    def getFilePath(fileName):
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
    def clearMute(self) -> 'SystemControl':
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
    def setAudio(self, num: float) -> 'SystemControl':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        # 设置音量（0.0到1.0之间的浮点数）
        volume_interface.SetMasterVolumeLevelScalar(num, None)

        return self

class Terminal:
    def __init__(self):

        pass

    @staticmethod
    def TerminalCommand():
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
    def getArgs(fileName, args1, args2, args3):
        import subprocess
        processes = []
        subprocess.run(['bash', fileName, args1, args2, args3])
        # 异步运行
        proc = subprocess.Popen(['bash', fileName, args1, args2, args3])
        processes.append(proc)

        for proc in processes:
            # 等待所有的进程完成
            proc.wait()

def is_user_on_desktop():
    # 获取当前激活的窗口
    active_window = gw.getActiveWindow()

    # 检查窗口标题是否为空（通常桌面窗口没有标题）
    if active_window and active_window.title == '':
        return True
    return False

if __name__ == '__main__':
    # SystemControl.disablePowershell(None)
    KeyboardControl.Hotkey(KeyboardControl, 'win tab')



