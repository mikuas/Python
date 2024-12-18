from ctypes import cast

import comtypes
from _ctypes import POINTER
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.utils import AudioUtilities


class VolumeUtil:
    @staticmethod
    def getVolumeInterface():
        """ get volume interface"""
        try:
            devices = AudioUtilities.GetSpeakers()
            # noinspection PyProtectedMember
            interface = devices.Activate(IAudioEndpointVolume._iid_, 1, None)
            return cast(interface, POINTER(IAudioEndpointVolume))
        except comtypes.COMError:
            return None

    def getVolumeLevel(self):
        """ get volume level """
        return f"{self.getVolumeInterface().GetMasterVolumeLevelScalar()*100:.2f}"

    def clearMute(self):
        """ clear mute """
        volume = self.getVolumeInterface()
        if volume is not None:
            volume.SetMute(0, None)
        return self

    def setMute(self):
        """ set mute """
        volume = self.getVolumeInterface()
        if volume is not None:
            volume.SetMute(1, None)
        return self

    def setVolumeLevel(self, level: int):
        """ set volume level, range 0-100 """
        self.getVolumeInterface().SetMasterVolumeLevelScalar(level / 100, None)
        return self
