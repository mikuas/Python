from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import comtypes
import argparse

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
        # GetMasterVolumeLevelScalar()

        return volume
    except comtypes.COMError as e:
        print(f"COMError: {e}")
        return None

# 静音
def setMute(num):
    volume = getAudioEndpointVolume()
    if volume is None:
        print("无法获取音频设备")
        return

    try:
        if volume.GetMute():
            volume.SetMute(num, None)
        else:
            volume.SetMute(num, None)
    except comtypes.COMError as e:
        print(f"COMError: {e}")

argparse = argparse.ArgumentParser()
argparse.add_argument('-n', type=float, help='设置声音大小0-100', required=False)
argparse.add_argument('-m', nargs='?', const=True, help='静音', required=False)
argparse.add_argument('-c', nargs='?', const=True, help='取消静音', required=False)

result = argparse.parse_args()

if __name__ == '__main__':
    if result.m:
        setMute(1)
        print('已静音')
    elif result.c:
        setMute(0)
        print('已取消静音')
    elif  result.n is not None:
        setAudio(result.n / 100)
        print(f'当前音量: {result.n}%', type(result.n))