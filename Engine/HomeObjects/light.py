from Engine.HomeObjects.object import *


class Light(Object):
    def __init__(self, name, location, power=False, brightness=50, colors=None):
        Object.__init__(self, name, location, power)
        self.brightness = brightness    # 0-100 value
        self.colors = []                # list of possibly colors in current light
        self.current_color = None

        if colors:
            self.colors = colors
            self.current_color = colors[0]

    def change_brightness(self, signal):
        signal = int(signal)
        if 0 <= signal <= 100:
            self.brightness = signal
            print(f'Changed brightness of \"{self.location}\" '
                  f'to \"{self.brightness}\"!!!')
            self.notify_observers('brightness')

    def change_color(self, signal):
        self.current_color = signal
        print(f'Changed color of \"{self.location}\" '
              f'to \"{self.current_color}\"!!!')
        self.notify_observers('color')
