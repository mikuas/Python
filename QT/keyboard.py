
# keyboard input

import pyautogui
import time


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


if __name__ == '__main__':
    # vc = VideosControl(1)
    kb = Keyboard()
    kb.board('ctrl', 'alt', 'space')


