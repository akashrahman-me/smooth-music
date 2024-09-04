from utils.text_to_speech import text_to_speech
from lib.ActivityDetection import ActivityDetection
from lib.Volume import Volume
# from lib.PlotLib import PlotLib
import threading

INITIAL_VOLUME = 32
ACTIVITY_VOLUME = 12
INACTIVITY_VOLUME = 32
VOICE_NOISE = 0.0175

class InactivityMonitor(Volume):
    def __init__(self):
        self.timeout = 1
        self.timer = None
        self.activity_listener = ActivityDetection(self.on_activity)
        self.inactive = False
        self.deep_mind_level = 0.02
        
        # disabled deep mind
        # PlotLib.__init__(self)
        Volume.__init__(self)
        
    def on_activity(self, port, smooth):
        self.new_volume = ACTIVITY_VOLUME
        self.smooth = smooth
        if self.inactive:
            threading.Thread(target=self.adjust_volume, args=(port,)).start()
            self.inactive = False
        self.reset_timer()
    
    def on_inactivity(self, port, smooth):
        self.new_volume = INACTIVITY_VOLUME
        self.smooth = smooth
        threading.Thread(target=self.adjust_volume, args=(port,)).start()
        self.inactive = True

    def reset_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        
        # currently we're disabled deep mind mood
        # if len(self.plot) >= 120:
        #     last_20_plot = self.plot[-60:]
        # else:
        #     last_20_plot = self.plot
            
        # if last_20_plot.count(1) >= len(last_20_plot) / 3:
        #     self.deep_mind_level = 0.2
        # else:
        #     self.deep_mind_level = 0.005

            
        self.timer = threading.Timer(self.timeout, self.on_inactivity, args=('inactivity', self.deep_mind_level))
        self.timer.start()

    def start(self):
        self.new_volume = INITIAL_VOLUME
        self.smooth = 0
        self.adjust_volume('initial')
        print("Inactivity Monitor initialized")
        text_to_speech("Inactivity Monitor initialized")
        self.reset_timer()
        self.activity_listener.start()
        print("Inactivity Monitor started listening")
        text_to_speech("Inactivity Monitor started listening")
        # self.draw_start()
        
    def stop(self):
        pass
