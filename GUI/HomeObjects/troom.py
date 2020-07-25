from GUI.HomeObjects.tdevice import *
from GUI.HomeObjects.tlight import *
from tkinter import *


class TRoom(Frame):
    def __init__(self, send_func, room, master=None):
        super().__init__(master=master)
        self.send_func = send_func
        self.room = room
        self.lights_frame = Frame(self, highlightbackground='grey', highlightthickness=0.5)
        self.devices_frame = Frame(self, highlightbackground='grey', highlightthickness=0.5)
        self.t_lights = []
        self.t_devices = []
        self.lights_label = Label(self.lights_frame, text='Lights', font='Ubuntu 15 bold')
        self.devices_label = Label(self.devices_frame, text='Devices', font='Ubuntu 15 bold')
        self.on_lights_button = Button(self.lights_frame, text='Turn ON all',
                                       command=self.turn_on_the_lights, bg='green')
        self.off_lights_button = Button(self.lights_frame, text='Turn OFF all',
                                        command=self.turn_off_the_lights, bg='red')
        self.on_devices_button = Button(self.devices_frame, text='Turn ON all',
                                        command=self.turn_on_the_devices, bg='green')
        self.off_devices_button = Button(self.devices_frame, text='Turn OFF all',
                                         command=self.turn_off_the_devices, bg='red')
        self.pack()
        self.__setup__()

    def __setup__(self):
        if self.room.lighting:
            self.lights_frame.pack(fill=BOTH, side=LEFT, expand=True, padx=1)
            self.lights_label.pack(pady=10)
            self.on_lights_button.pack(pady=6)
            self.off_lights_button.pack(pady=6)

            for light in self.room.lighting.values():
                label_frame = LabelFrame(self.lights_frame)
                label_frame.pack(pady=6)
                t_light = TLight(self.send_func, light, label_frame)
                label_frame.configure(text=t_light.obj.name.capitalize(), font="Ubuntu 12 bold")
                # t_light.pack(pady=6)
                self.t_lights.append(t_light)

        if self.room.devices:
            self.devices_frame.pack(fill=BOTH, side=LEFT, expand=True, padx=1)
            self.devices_label.pack(pady=10)
            self.on_devices_button.pack(pady=6)
            self.off_devices_button.pack(pady=6)

            for device in self.room.devices.values():
                device_frame = LabelFrame(self.devices_frame)
                device_frame.pack(pady=6)
                t_device = TDevice(self.send_func, device, device_frame)
                device_frame.configure(text=t_device.obj.name.capitalize(), font="Ubuntu 12 bold")
                # t_device.pack(pady=6)
                self.t_devices.append(t_device)

    def turn_off_the_devices(self):
        for t_device in self.t_devices:
            if t_device.obj.get_power_status() == 'On':
                self.send_func(t_device.obj.location, 'power=off')

    def turn_on_the_devices(self):
        for t_device in self.t_devices:
            if t_device.obj.get_power_status() == 'Off':
                self.send_func(t_device.obj.location, 'power=on')

    def turn_off_the_lights(self):
        for t_light in self.t_lights:
            if t_light.obj.get_power_status() == 'On':
                self.send_func(t_light.obj.location, 'power=off')

    def turn_on_the_lights(self):
        for t_light in self.t_lights:
            if t_light.obj.get_power_status() == 'Off':
                self.send_func(t_light.obj.location, 'power=on')
