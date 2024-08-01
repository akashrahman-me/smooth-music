import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import json
import threading

# plt.ion()

class PlotLib:
    def __init__(self):
        self.plot = []
        # self.fig, self.ax = plt.subplots()
        # self.line, = self.ax.plot(self.plot[0], self.plot[1])
        
    def timestamp_to_seconds(self, timestamp):
        datetime_obj = datetime.fromtimestamp(timestamp)
        seconds = datetime_obj.strftime('%S')
        return int(seconds)
        
    def update_data(self):
        while True:
            if self.volume_port in ['keyboard', 'mouse']:
                self.plot.append(1)
                
            elif self.volume_port in ['inactivity']:
                self.plot.append(0)
                
            # Disabled chart as we don't need it anymore. If needed, we'll enable it again.
            # if self.volume_port in ['keyboard', 'mouse', 'inactivity']:
                # self.line.set_ydata(np.array(self.plot[0]))
                # self.line.set_xdata(np.array(self.plot[1]))
                
                # self.ax.relim()
                # self.ax.autoscale_view()
                
                # plt.draw()
                # plt.pause(1)
                
            # working_data = open('working_data.json', 'w')
            # working_data.write(json.dumps(self.plot))
            # working_data.close()
            
            time.sleep(1)
      
    def draw_start(self):
        # self.update_data()
        threading.Thread(target=self.update_data).start()