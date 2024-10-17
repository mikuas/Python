import easyocr
import time
import torch
import pyautogui

from PyMyMethod.parentScreen import ScreenControl as SC

class ScreenControl(SC):

    def __init__(self):
        self.text = ''
        self.gpuAvailable = torch.cuda.is_available()
        print(f"CUDA 可用: {self.gpuAvailable}")
        if self.gpuAvailable:
            print(f"CUDA 版本: {torch.version.cuda}")
            print(f"当前设备: {torch.cuda.get_device_name(0)}")
        else:
            print("未检测到可用的 GPU")

    def getResolution(self):
        return list(pyautogui.size())

    def getScreenColor(self, x, y):
        x, y = pyautogui.position(x, y)
        return pyautogui.pixel(x, y)

    def isColor(self, x, y, rgbColor = (255, 255, 255)):
        return pyautogui.pixelMatchesColor(x, y, rgbColor)

    def takeAScreenshot(self, savePath):
        pyautogui.screenshot().save(savePath)
        return self

    def zoneTakeAScreenshot(self, left, top, width, height, savePath):
        pyautogui.screenshot(region=(left, top, width, height)).save(savePath)
        return

    def getScreenFullText(
            self,
            left = None,
            top = None,
            width = None,
            height = None,
            language = None,
            zone = False
    ):
        print("脚本将在5秒后开始运行,请准备好要截取的区域...")
        time.sleep(5)
        if zone:
            self.zoneTakeAScreenshot(left, top, width, height, './result_zone.png')
        else:
            self.takeAScreenshot("./result_img.png")
        results = easyocr.Reader(language or ['ch_sim', 'en'], gpu=self.gpuAvailable).readtext("./result_img.png")
        return '\n'.join([result[1] for result in results])