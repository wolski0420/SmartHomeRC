from Observation.observer import *
from tkinter import Frame, Label, Button, StringVar, LEFT


class TObject(Frame, Observer):
    def __init__(self, send_func, obj, master=None):
        Frame.__init__(self, master=master)
        Observer.__init__(self, obj)
        self.send_func = send_func
        self.obj = obj
        self.pack()
        self.power_frame = None
        self.power_btn_text = StringVar()
        self.power_property_label = None
        self.power_property_status_label = None
        self.power_property_button = None
        self.__set_power_property__()

    def __set_power_property__(self):
        self.power_frame = Frame(self)
        self.power_frame.pack()
        self.power_property_label = Label(self.power_frame, text=self.obj.name.capitalize())
        self.power_property_label.pack(side=LEFT, padx=3)
        self.power_property_status_label = Label(self.power_frame, text='(currently OFF)', foreground='red')
        self.power_property_status_label.pack(side=LEFT, padx=3)
        self.power_property_button = Button(self.power_frame, textvariable=self.power_btn_text,
                                            command=self.__power_button_event__, foreground='green')
        self.power_property_button.pack(side=LEFT, padx=3)
        self.power_btn_text.set(str('Turn ' + self.obj.get_power_status_for_button().upper()))

    def __power_button_event__(self):
        self.send_func(self.obj.location, str('power=' + self.obj.get_power_status_for_button()))

    def __update_power_property__(self):
        self.power_btn_text.set(str('Turn ' + self.obj.get_power_status_for_button().upper()))
        if self.obj.get_power_status() == 'On':
            self.power_property_button.configure(foreground='red')
            self.power_property_status_label.configure(text='(currently ON)', foreground='green')
        else:
            self.power_property_button.configure(foreground='green')
            self.power_property_status_label.configure(text='(currently OFF)', foreground='red')

    def notify(self, information=None):
        if information is None:
            return
        elif information == 'power':
            self.__update_power_property__()
