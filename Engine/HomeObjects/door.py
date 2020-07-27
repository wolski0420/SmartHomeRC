from Observation.observable import *


class Door(Observable):
    def __init__(self, room1, room2, typ='interior', blockade=False):
        super().__init__()
        self.room1 = room1
        self.room2 = room2
        self.typ = typ
        self.blockade = blockade

    def change_blockade(self, signal):
        signal = signal.lower()
        if signal == 'block':
            self.blockade = True
        elif signal == 'unblock':
            self.blockade = False

        print(f'Changed blockade status in door \"{self.room1.name}-{self.room2.name}\" '
              f'from \"{self.get_blockade_status_for_button()}ed\" '
              f'to \"{self.get_blockade_status()}\"!!!')
        self.notify_observers('blockade_status')

    def get_blockade_status(self):
        if self.blockade:
            return 'Blocked'
        else:
            return 'Unblocked'

    def get_blockade_status_for_button(self):
        if not self.blockade:
            return 'Block'
        else:
            return 'Unblock'
