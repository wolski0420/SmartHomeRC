from tkinter import Tk, Frame, Label, Button, Entry, LEFT


class TConnectWindow(Tk):
    def __init__(self, info, run_rc_func):
        Tk.__init__(self)
        self.main_frame = Frame(self)
        self.info = info
        self.run_rc = run_rc_func
        self.__connect_label = Label(self, text='Enter connect data')
        self.__ip_frame = Frame(self)
        self.__ip_label = Label(self.__ip_frame, text='Address IP ')
        self.__ip_entry = Entry(self.__ip_frame)
        self.__port_frame = Frame(self)
        self.__port_label = Label(self.__port_frame, text='Port ')
        self.__port_entry = Entry(self.__port_frame)
        self.__submit_button = Button(self, text='Start', command=self.__button_event__)
        self.__setup_all__()

    def __setup_all__(self):
        self.__connect_label.pack()
        self.__ip_frame.pack()
        self.__ip_label.pack(side=LEFT)
        self.__ip_entry.pack(side=LEFT)
        self.__ip_entry.insert(0, '127.0.0.1')
        self.__port_frame.pack()
        self.__port_label.pack(side=LEFT)
        self.__port_entry.pack(side=LEFT)
        self.__port_entry.insert(0, 1883)
        self.__submit_button.pack()

    def __button_event__(self):
        ip = self.__ip_entry.get()
        port = self.__port_entry.get()

        if ip != '':
            self.info.change_ip(ip)

        if port != '':
            self.info.change_port(int(port))

        self.destroy()
        self.run_rc()
