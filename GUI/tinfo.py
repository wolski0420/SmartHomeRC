from tkinter import Frame, Label, LEFT
from Observation.observer import Observer


class TInfo(Frame, Observer):
    def __init__(self, info, master=None):
        Frame.__init__(self, master=master)
        Observer.__init__(self, info)
        self.info = info
        self.__info_label = None
        self.__ip_frame = None
        self.__ip_property_label = None
        self.__ip_value_label = None
        self.__port_frame = None
        self.__port_property_label = None
        self.__port_value_label = None
        self.__setup_all__()

    def __setup_all__(self):
        self.__info_label = Label(self, text='Information', font='Ubuntu 20 bold')
        self.__info_label.pack(pady=10)
        self.__ip_frame = Frame(self)
        self.__ip_frame.pack(pady=6)
        self.__ip_property_label = Label(self.__ip_frame, text='Address IP: ')
        self.__ip_property_label.pack(side=LEFT, padx=3)
        self.__ip_value_label = Label(self.__ip_frame, text=self.info.get_ip(), background='orange')
        self.__ip_value_label.pack(side=LEFT, padx=3)
        self.__port_frame = Frame(self)
        self.__port_frame.pack(pady=6)
        self.__port_property_label = Label(self.__port_frame, text='Port: ')
        self.__port_property_label.pack(side=LEFT, padx=3)
        self.__port_value_label = Label(self.__port_frame, text=self.info.get_port(), background='orange')
        self.__port_value_label.pack(side=LEFT, padx=3)

    def notify(self, information=None):
        self.__ip_value_label.configure(text=self.info.get_ip())
        self.__port_value_label.configure(text=self.info.get_port())
