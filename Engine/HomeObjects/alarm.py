from Engine.HomeObjects.object import *


class Alarm(Object):
    def __init__(self, name, location, power=False):
        Object.__init__(self, name, location, power)

    def change_power(self, signal):
        signal = signal.lower()
        if signal == 'on':
            self.power = True
        elif signal == 'off':
            self.power = False

        print(f'Changed power status of \"{self.name}\" '
              f'in \"{self.location}\" '
              f'from \"{self.get_power_status_for_button()}\" '
              f'to \"{self.get_power_status()}\"!!!')
        self.notify_observers('power')
