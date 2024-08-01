import time
from lib.InactivityMonitor import InactivityMonitor

monitor = InactivityMonitor()
monitor.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    monitor.stop()