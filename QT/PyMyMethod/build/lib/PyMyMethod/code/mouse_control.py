import pyautogui
from ..doc import MouseControl, KeyboardControl


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
