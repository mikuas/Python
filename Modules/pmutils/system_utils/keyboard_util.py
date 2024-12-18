import pyautogui


class KeyboardUtils:

    def writeText(self, text: str, interval=0.0):
        """ write text """
        pyautogui.typewrite(text, interval=interval)
        return self

    def writeTexts(self, texts: list[str], interval=0.0):
        """ write multiple text """
        for text in texts:
            self.writeText(text, interval=interval)
        return self

    def keyUp(self, key: str):
        """ key up """
        pyautogui.keyUp(key)
        return self

    def keyDown(self, key: str):
        """ key down"""
        pyautogui.keyDown(key)
        return self

    def keyClick(self, key: str, interval=0.0):
        """ key click """
        pyautogui.press(key, interval=interval)
        return self

    def keysClick(self, keys: list[str] or str, interval=0.0):
        """ keys click """
        for key in keys:
            self.keyClick(key, interval=interval)
        return self

    def Hotkey(self, hotkey: str, interval=0.1):
        """ hot key """
        pyautogui.hotkey(hotkey.split(','), interval=interval)
        return self