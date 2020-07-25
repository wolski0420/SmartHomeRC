from GUI.HomeObjects.tobject import *


class TAlarm(TObject):
    def __init__(self, send_func, alarm, master=None):
        TObject.__init__(self, send_func, alarm, master)

    def __set_power_property__(self):
        self.power_property_label = Label(self, text=str(
            self.obj.location.capitalize() + ' ' + self.obj.name.capitalize()
        ))
        self.power_property_label.pack(side=LEFT, padx=3)
        self.power_property_status_label = Label(self, text='(currently OFF)', foreground='red')
        self.power_property_status_label.pack(side=LEFT, padx=3)
        self.power_property_button = Button(self, textvariable=self.power_btn_text,
                                            command=self.__power_button_event__, foreground='green')
        self.power_property_button.pack(side=LEFT, padx=3)
        self.power_btn_text.set(str('Turn ' + self.obj.get_power_status_for_button().upper()))

    def __power_button_event__(self):
        self.send_func(str('alarm/' + self.obj.location + '-' + self.obj.name),
                       str('power=' + self.obj.get_power_status_for_button()))
