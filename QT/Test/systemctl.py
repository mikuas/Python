import os
from PySide6.QtCore import QTimer

class Systemctl:

    def __init__(self):
        pass

    def systemOption(self, time, element):
        if element == '关机':
            QTimer.singleShot(time, lambda: os.system("shutdown /s /f /t 0"))
        elif element == '重启':
            QTimer.singleShot(time, lambda: os.system("shutdown /r /f /t 0"))
        elif element == '注销':
            QTimer.singleShot(time, lambda: os.system("logoff"))
        elif element == '锁定':
            QTimer.singleShot(time, lambda: os.system("rundll32.exe user32.dll,LockWorkStation"))

        return self
