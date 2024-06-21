
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


if __name__ == '__main__':
    # vc = VideosControl(1)
    kb = Keyboard()
    kb.open_web()


