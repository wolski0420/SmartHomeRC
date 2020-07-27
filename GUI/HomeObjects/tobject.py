from Observation.observer import *
from tkinter import Frame, Label, Button, StringVar, LEFT


class TObject(Frame, Observer):
    def __init__(self, send_func, obj, master=None):
        Frame.__init__(self, master=master)
        Observer.__init__(self, obj)
        self._send_func = send_func
        self.obj = obj
        self.pack()
        self._power_frame = None
        self._power_btn_text = StringVar()
        self._power_property_label = None
        self._power_property_status_label = None
        self._power_property_button = None
        self.__set_power_property__()

    def __set_power_property__(self):
        self._power_frame = Frame(self)
        self._power_frame.pack()
        self._power_property_label = Label(self._power_frame, text=self.obj.name.capitalize())
        self._power_property_label.pack(side=LEFT, padx=3)
        self._power_property_status_label = Label(self._power_frame, text='(currently OFF)', foreground='red')
        self._power_property_status_label.pack(side=LEFT, padx=3)
        self._power_property_button = Button(self._power_frame, textvariable=self._power_btn_text,
                                              command=self.__power_button_event__, foreground='green')
        self._power_property_button.pack(side=LEFT, padx=3)
        self._power_btn_text.set(str('Turn ' + self.obj.get_power_status_for_button().upper()))

    def __power_button_event__(self):
        self._send_func(self.obj.location, str('power=' + self.obj.get_power_status_for_button()))

    def __update_power_property__(self):
        self._power_btn_text.set(str('Turn ' + self.obj.get_power_status_for_button().upper()))
        if self.obj.get_power_status() == 'On':
            self._power_property_button.configure(foreground='red')
            self._power_property_status_label.configure(text='(currently ON)', foreground='green')
        else:
            self._power_property_button.configure(foreground='green')
            self._power_property_status_label.configure(text='(currently OFF)', foreground='red')

    def notify(self, information=None):
        if information is None:
            return
        elif information == 'power':
            self.__update_power_property__()
