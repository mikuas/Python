"""
pip install pycaw
控制声音
"""


from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
import comtypes


class VideosControl:

    def __init__(self, num):
        # 获取默认的音频渲染设备
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

        # 转换成IAudioEndpointVolume接口
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # 获取当前音量范围
        volume_range = volume.GetVolumeRange()
        min_volume = volume_range[0]
        max_volume = volume_range[1]

        # 获取当前音量
        current_volume = volume.GetMasterVolumeLevelScalar()
        print("当前音量:", current_volume)

        # 设置音量
        volume.SetMasterVolumeLevelScalar(num, None)
        print("音量已设置为50%")

        # 如果需要静音，可以使用下面的代码
        # volume.SetMute(True, None)
        # print("音量已静音")

        # 如果需要取消静音，可以使用下面的代码
        # volume.SetMute(False, None)
        # print("音量已取消静音")


def set_audio(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    # 设置音量（0.0到1.0之间的浮点数）
    volume_interface.SetMasterVolumeLevelScalar(volume, None)


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


def set_audio():
    volume = get_audio_endpoint_volume()
    if volume is None:
        print('Error')

    try:
        if volume.GetMute():
            volume.SetMute(0, None)
            print("系统已解除静音")
        else:
            print("系统未处于静音状态")
    except comtypes.COMError as e:
        print(f"COMError: {e}")


if __name__ == '__main__':
    pass
