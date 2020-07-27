from tkinter import Frame, Button, Label


class TUtils(Frame):
    def __init__(self, utils, master=None):
        Frame.__init__(self, master=master)
        self.__utils = utils
        self.__utils_label = Label(self, text='Utils', font='Ubuntu 20 bold')
        self.__off_lights_btn = Button(self, text='Turn OFF all lights', command=utils.turn_off_the_lights, bg='red')
        self.__on_lights_btn = Button(self, text='Turn ON all lights', command=utils.turn_on_the_lights, bg='green')
        self.__off_devices_btn = Button(self, text='Turn OFF all devices', command=utils.turn_off_the_devices, bg='red')
        self.__on_devices_btn = Button(self, text='Turn ON all devices', command=utils.turn_on_the_devices, bg='green')
        self.__off_alarms_btn = Button(self, text='Turn OFF all alarms', command=utils.turn_off_the_alarms, bg='red')
        self.__on_alarms_btn = Button(self, text='Turn ON all alarms', command=utils.turn_on_the_alarms, bg='green')
        self.__block_doors_btn = Button(self, text='BLOCK all doors', command=utils.block_all_doors, bg='red')
        self.__unblock_doors_btn = Button(self, text='UNBLOCK all doors', command=utils.unblock_all_doors, bg='green')
        self.__setup_all__()

    def __setup_all__(self):
        self.__utils_label.pack(pady=10)
        self.__off_lights_btn.pack(pady=6)
        self.__on_lights_btn.pack(pady=6)
        self.__off_devices_btn.pack(pady=6)
        self.__on_devices_btn.pack(pady=6)
        self.__block_doors_btn.pack(pady=6)
        self.__unblock_doors_btn.pack(pady=6)
        self.__off_alarms_btn.pack(pady=6)
        self.__on_alarms_btn.pack(pady=6)
