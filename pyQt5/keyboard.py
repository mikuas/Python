
# keyboard input

import pyautogui
import time

# 控制音量
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# 在当前位置输入 "Hello, World!"
# pyautogui.typewrite('Hello, World!')


# 按下和释放空格键
class Keyboard:

    # 睡眠2s
    @staticmethod
    def sleep(num):
        time.sleep(num)

    # 按住传入的键
    @staticmethod
    def press(key):
        pyautogui.press(key)

    @staticmethod
    def _input(substance):
        pyautogui.typewrite(substance)

    @staticmethod
    def board(*args):
        if len(args) == 1:
            pyautogui.hotkey(args[0])
            print(1)
        elif len(args) == 2:
            pyautogui.hotkey(args[0], args[1])
            print(2)
        elif len(args) == 3:
            pyautogui.hotkey(args[0], args[1], args[2])
            print(3)

    def open_web(self):

        self.press('win')
        self.sleep(0.5)
        self._input('chrome')
        self.sleep(1.5)
        self.board('Enter')
        self.sleep(1)
        self.board('Enter')
        self.sleep(5)
        self._input('https://www.bilibili.com/video/BV13C41147Pm?t=3.1')
        # self._input('https://bilibili.com')
        self.board('Enter')
        self.sleep(0.5)
        self.board('Enter')
        self.sleep(3)
        self.board('m')
        # self.sleep(8)
        # for i in range(10):
        #     self.board('Tab')
        # self.sleep(5)
        # self.board('CapsLk')
        # self.sleep(0.5)
        # self._input('BV13C41147P')
        # self.board('CapsLk')
        # self._input('m')
        # self.sleep(0.5)
        # self.board('Enter')
        # self.board('Enter')
        # self.sleep(3)
        # for i in range(19):
        #     self.board('Tab')
        # self.sleep(0.5)
        # self.board('Enter')


class VideosControl:

    def __init__(self, num):
        # 获取默认的音频渲染设备
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

        # 转换成IAudioEndpointVolume接口
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # 获取当前音量范围
        volume_range = volume.GetVolumeRange()
        min_volume = volume_range[0]
        max_volume = volume_range[1]

        # 获取当前音量
        current_volume = volume.GetMasterVolumeLevelScalar()
        # print("当前音量:", current_volume)

        # 设置音量
        volume.SetMasterVolumeLevelScalar(num, None)
        # print("音量已设置为50%")


if __name__ == '__main__':
    # vc = VideosControl(1)
    kb = Keyboard()
    kb.open_web()


