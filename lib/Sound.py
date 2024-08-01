import sounddevice as sd
import numpy as np

class Sound:
    def __init__(self, on_sound, threshold_volume = 0.0175):
        self.threshold_volume = threshold_volume
        self.on_sound = on_sound

    def Listener(self, indata, frames, time, status):
        rms = np.sqrt(np.mean(np.square(indata)))
        if rms > self.threshold_volume:
            self.on_sound()
              
    def start(self):
        # Set up the audio stream
        with sd.InputStream(callback=self.Listener):
            sd.sleep(1000000000)
                
    def stop(self):
        pass
    
