from Engine.HomeObjects.object import *


class Light(Object):
    def __init__(self, name, location, power=False, brightness=50):
        Object.__init__(self, name, location, power)
        self.brightness = brightness    # 0-100

    def change_brightness(self, signal):
        signal = int(signal)
        if 0 <= signal <= 100:
            self.brightness = signal
            print(f'Changed brightness of \"{self.location}\" '
                  f'to \"{self.get_brightness()}\"!!!')
            self.notify_observers('brightness')

    def get_brightness(self):
        return self.brightness
