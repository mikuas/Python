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
def getMute(num):
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

parser = argparse.ArgumentParser(description="设置音量")

# 添加参数
parser.add_argument('-a', '--Audio', type=float, help='设置音量大小0-100', required=False)
parser.add_argument('-M', '--Mute', type=int, help='静音', required=False)

args = parser.parse_args()

if __name__ == '__main__':
    if args.Audio is not None:
        setAudio(args.Audio / 100)
        print(f'当前音量: {args.Audio}%', type(args.Audio))
    if args.Mute == 0:
        getMute(1)
        print(False)
    else:
        getMute(0)
        print(True)