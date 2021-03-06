from GUI.HomeObjects.tobject import *
from tkinter import Scale, HORIZONTAL, ttk


class TLight(TObject):
    def __init__(self, send_func, light, master=None):
        super().__init__(send_func, light, master)
        self._power_property_label.configure(text="Power:")
        self.__brightness_frame = None
        self.__brightness_property_label = None
        self.__brightness_property_scale = None
        self.__brightness_property_status_label = None
        self.__brightness_property_button = None
        self.__set_brightness_property__()
        self.__color_frame = None
        self.__color_property_label = None
        self.__color_property_combobox = None
        self.__color_property_status_label = None
        self.__color_property_button = None
        self.__set_color_property__()

    def __set_brightness_property__(self):
        self.__brightness_frame = Frame(self)
        self.__brightness_frame.pack()
        self.__brightness_property_label = Label(self.__brightness_frame, text='Brightness:')
        self.__brightness_property_label.pack(side=LEFT, padx=3)
        self.__brightness_property_status_label = Label(self.__brightness_frame, text=f'(currently {self.obj.brightness})')
        self.__brightness_property_status_label.pack(side=LEFT, padx=3)
        self.__brightness_property_scale = Scale(self.__brightness_frame, from_=0, to=100, orient=HORIZONTAL)
        self.__brightness_property_scale.set(50)
        self.__brightness_property_scale.pack(side=LEFT, padx=3)
        self.__brightness_property_button = Button(self.__brightness_frame, text='Change',
                                                   command=self.__brightness_button_event__)
        self.__brightness_property_button.pack(side=LEFT, padx=3)

    def __set_color_property__(self):
        if self.obj.colors:
            self.__color_frame = Frame(self)
            self.__color_frame.pack()
            self.__color_property_label = Label(self.__color_frame, text='Color:')
            self.__color_property_label.pack(side=LEFT, padx=3)
            self.__color_property_status_label = Label(self.__color_frame, text=f'(currently {self.obj.current_color})')
            self.__color_property_status_label.pack(side=LEFT, padx=3)
            self.__color_property_combobox = ttk.Combobox(self.__color_frame, state='readonly')
            self.__color_property_combobox['values'] = self.obj.colors
            self.__color_property_combobox.current(0)
            self.__color_property_combobox.pack(side=LEFT, padx=3, pady=5)
            self.__color_property_button = Button(self.__color_frame, text='Change',
                                                  command=self.__color_button_event__)
            self.__color_property_button.pack(side=LEFT, padx=3)

    def __brightness_button_event__(self):
        self._send_func(self.obj.location, str('brightness=' + str(self.__brightness_property_scale.get())))

    def __update_brightness_property__(self):
        self.__brightness_property_status_label.configure(text=f'(currently {self.obj.brightness})')

    def __color_button_event__(self):
        self._send_func(self.obj.location, str('color=' + self.__color_property_combobox.get()))

    def __update_color_property(self):
        self.__color_property_status_label.configure(text=f'(currently {self.obj.current_color})')

    def notify(self, information=None):
        if information is None:
            return
        elif information == 'power':
            self.__update_power_property__()
        elif information == 'brightness':
            self.__update_brightness_property__()
        elif information == 'color':
            self.__update_color_property()
