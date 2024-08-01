import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

class Volume:
    def __init__(self):        
        self.volume_port = None
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
        self.smooth = 0.2
        self.new_volume = 1
        
    def db_to_percent(self, dB):
        return int((10 ** (dB / 35) * 100))

    def percent_to_db(self, percent):
        return 35 * math.log(percent / 100, 10)
    
    def adjust_volume(self, port):
        self.volume_port = port
        current_volume = self.volume.GetMasterVolumeLevel()
        current_volume = self.db_to_percent(current_volume)      
        
        if self.smooth != 0:
            abs_volume = abs(self.new_volume - current_volume)
            
            for index in range(abs_volume):
                if self.new_volume >= current_volume:
                    smooth_vol = current_volume + (index + 1)
                else:
                    smooth_vol = current_volume - (index + 1)
                    
                if self.volume_port != port:
                    break
                
                dB = self.percent_to_db(smooth_vol)
                self.volume.SetMasterVolumeLevel(dB, None)
                time.sleep(self.smooth)
        else:
            dB = self.percent_to_db(self.new_volume)
            self.volume.SetMasterVolumeLevel(dB, None)
