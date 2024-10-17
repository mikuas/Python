import pyautogui

class ControlMouse:
    def __init__(self):
        pass

    def getResolution(self):
        # 获取屏幕分辨率
        return list(pyautogui.size())

    def getMousePosition(self):
        # 获取当前鼠标位置
        return pyautogui.position()

    def moveMouse(self, x, y, time):
        # 移动鼠标到指定位置
        pyautogui.moveTo(x, y, duration=time)
        return self

    def moveMouseRelative(self, x, y, time=0):
        # 相对移动鼠标
        pyautogui.moveRel(x, y, duration=time)
        return self

    def clickMouse(self, position='left'):
        # 点击鼠标
        pyautogui.click(button=position)

    def twoClickMouse(self):
        pyautogui.doubleClick()

class KeyboardControl:
    def __init__(self):
        pass

    def writeText(self, text, interval=0.1):
        pyautogui.write(text, interval=interval)

    def pressKey(self, key, interval=0.1):
        pyautogui.press(key, interval=interval)

    def hotKey(self, key):
        pyautogui.hotkey(key)

    def keyDown(self, key):
        pyautogui.keyDown(key)

    def keyUp(self, key):
        pyautogui.keyUp(key)

class Display:
    def __init__(self):
        pass

    def getDisplayColor(self, x, y):
        x, y = pyautogui.position(x, y)
        return pyautogui.pixel(x, y)

    def isWirte(self, x, y, rgbColor=(255, 255, 255)):

        return pyautogui.pixelMatchesColor(x, y, rgbColor)  # 判断当前位置是否为白色

    def takeAScreenshot(self, savePath):
        pyautogui.screenshot().save(savePath)

    def zoneTakeAScreenshot(self, left, top, width, height, savePath):
        pyautogui.screenshot(region=(left, top, width, height)).save(savePath)

if __name__ == '__main__':
    mouse = ControlMouse()
    result = mouse.getMousePosition()
    print(list(result))
    pass