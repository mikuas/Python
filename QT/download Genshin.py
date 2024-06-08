import os
import pyautogui
import pyperclip
import time

os.system('explorer https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default')

time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('enter')

result = pyperclip.paste()
path = f"C:/Users/Administrator/Downloads/{result}"

os.system(f'start {path}')

print(path)
