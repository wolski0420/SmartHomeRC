from GUI.HomeObjects.tobject import *


class TDoor(TObject):
    def __init__(self, send_func, door, master=None):
        TObject.__init__(self, send_func, door, master)
        self.pack(padx=8)

    def __set_power_property__(self):
        self.power_property_label = Label(self, text=str(
            self.obj.room1.name.capitalize() + '-' + self.obj.room2.name.capitalize()
        ))
        self.power_property_label.pack(side=LEFT, padx=3)
        self.power_status_label = Label(self, text='(currently unblocked)', foreground='green')
        self.power_status_label.pack(side=LEFT, padx=3)
        self.power_property_button = Button(self, textvariable=self.power_btn_text,
                                            command=self.__power_button_event__, foreground='red')
        self.power_property_button.pack(side=LEFT, padx=3)
        self.power_btn_text.set(self.obj.get_blockade_status_for_button().upper())

    def __power_button_event__(self):
        self.send_func(str('door/' + self.obj.room1.name + '-' + self.obj.room2.name),
                       str('blockade_status=' + self.obj.get_blockade_status_for_button()))

    def notify(self, information=None):
        if information is None:
            return
        elif information == 'blockade_status':
            self.power_btn_text.set(self.obj.get_blockade_status_for_button().upper())
            if self.obj.get_blockade_status() == 'Blocked':
                self.power_property_button.configure(foreground='green')
                self.power_status_label.configure(text='(currently blocked)', foreground='red')
            else:
                self.power_property_button.configure(foreground='red')
                self.power_status_label.configure(text='(currently unblocked)', foreground='green')
