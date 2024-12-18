import pyautogui


class MouseUtils:

    @staticmethod
    def getMousePosition():
        """ get mouse position """
        return pyautogui.position()

    def moveMouseTo(self, x: int, y: int, duration=0.1):
        """ move mouse to specified position """
        pyautogui.moveTo(x, y, duration=duration)
        return self

    def moveMouseRelative(self, x: int, y: int, duration=0.1):
        """ in current mouse position move """
        pyautogui.moveRel(x, y, duration=duration)
        return self

    def clickMouse(self, position='left'):
        """ click mouse """
        pyautogui.click(button=position)
        return self

    def doubleClickMouse(self, position='left'):
        """ double click mouse """
        pyautogui.doubleClick(button=position)
        return self