from lib.Volume import Volume
import keyboard
import threading
import pyautogui
import time

volume = Volume()

class ActivityDetection:
    def __init__(self, on_activity):
        self.on_activity = on_activity
        self.smoothness = 0.02
        
    def keyboard_listener(self):
        keyboard.on_press(lambda event: self.on_activity(port = 'keyboard', smooth = self.smoothness))
        while True:
            time.sleep(0.02)
        
    def mouse_listener(self):
        initial_position = pyautogui.position()
        
        while True:
            current_position = pyautogui.position()
            if current_position != initial_position:
                self.on_activity(port = 'mouse', smooth = self.smoothness)
                initial_position = current_position
            time.sleep(0.02)
        
    def start(self):
        keyboard_thread = threading.Thread(target=self.keyboard_listener)
        keyboard_thread.start()
        
        mouse_thread = threading.Thread(target=self.mouse_listener)
        mouse_thread.start()