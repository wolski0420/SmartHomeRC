from GUI.HomeObjects.tobject import *


class TDevice(TObject):
    def __init__(self, send_func, device, master=None):
        super().__init__(send_func, device, master)
        self._power_property_label.configure(text="Power:")
