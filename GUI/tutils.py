from tkinter import Frame, Button, Label


class TUtils(Frame):
    def __init__(self, utils, master=None):
        Frame.__init__(self, master=master)
        self.utils = utils
        self.utils_label = Label(self, text='Utils', font='Ubuntu 20 bold')
        self.off_lights_btn = Button(self, text='Turn OFF all lights', command=utils.turn_off_the_lights, bg='red')
        self.on_lights_btn = Button(self, text='Turn ON all lights', command=utils.turn_on_the_lights, bg='green')
        self.off_devices_btn = Button(self, text='Turn OFF all devices', command=utils.turn_off_the_devices, bg='red')
        self.on_devices_btn = Button(self, text='Turn ON all devices', command=utils.turn_on_the_devices, bg='green')
        self.off_alarms_btn = Button(self, text='Turn OFF all alarms', command=utils.turn_off_the_alarms, bg='red')
        self.on_alarms_btn = Button(self, text='Turn ON all alarms', command=utils.turn_on_the_alarms, bg='green')
        self.block_doors_btn = Button(self, text='BLOCK all doors', command=utils.block_all_doors, bg='red')
        self.unblock_doors_btn = Button(self, text='UNBLOCK all doors', command=utils.unblock_all_doors, bg='green')
        self.__setup_all__()

    def __setup_all__(self):
        self.utils_label.pack(pady=10)
        self.off_lights_btn.pack(pady=6)
        self.on_lights_btn.pack(pady=6)
        self.off_devices_btn.pack(pady=6)
        self.on_devices_btn.pack(pady=6)
        self.block_doors_btn.pack(pady=6)
        self.unblock_doors_btn.pack(pady=6)
        self.off_alarms_btn.pack(pady=6)
        self.on_alarms_btn.pack(pady=6)
