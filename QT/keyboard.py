
# keyboard input

import pyautogui
import time


# 按下和释放空格键
class Keyboard:

    # 睡眠
    @staticmethod
    def sleep(num):
        time.sleep(num)

    # 按住传入的键
    @staticmethod
    def press(key):
        pyautogui.press(key)

    @staticmethod
    def _input(text):
        pyautogui.typewrite(text)

    # 组合键
    @staticmethod
    def board(key: tuple):
        pyautogui.hotkey(key)

if __name__ == '__main__':
    Keyboard().board(('ctrl', 'alt', 'space'))
