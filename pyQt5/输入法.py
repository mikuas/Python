import pygetwindow
import pyautogui


def is_chinese_input():
    # 获取当前焦点窗口
    active_window = pygetwindow.getActiveWindow()
    if active_window is not None:
        # 获取窗口标题
        window_title = active_window.title
        # 判断标题中是否包含中文字符
        for char in window_title:
            if '\u4e00' <= char <= '\u9fff':
                return True
    return False


# 测试判断当前输入法语言
if is_chinese_input():
    print("当前输入法为中文")
else:
    print("当前输入法为英文")
