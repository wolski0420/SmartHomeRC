from Observation.observable import *


class Object(Observable):
    def __init__(self, name, location, power=False):
        super().__init__()
        self.name = name
        self.location = location
        self.power = power

    def change_power(self, signal):
        signal = signal.lower()
        if signal == 'on':
            self.power = True
        elif signal == 'off':
            self.power = False

        print(f'Changed power status in \"{self.location}\" '
              f'from \"{self.get_power_status_for_button()}\" '
              f'to \"{self.get_power_status()}\"!!!')
        self.notify_observers('power')

    def get_power_status(self):
        if self.power:
            return 'On'
        else:
            return 'Off'

    def get_power_status_for_button(self):
        if not self.power:
            return 'On'
        else:
            return 'Off'
