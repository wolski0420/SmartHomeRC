from GUI.HomeObjects.troom import *
from GUI.HomeObjects.tdoor import *
from GUI.HomeObjects.talarm import *
from tkinter import ttk
from GUI.tutils import *
from GUI.tinfo import *
from GUI.tconnect import *


class TRemote:
    def __init__(self, remote):
        self.remote_control = remote
        self.window = Tk()
        self.connect_window = TConnectWindow(self.remote_control.info, self.__run__, self.__finish__)
        self.t_rooms = []
        self.t_rooms_frame = Frame(self.window, highlightbackground='black', highlightthickness=0.5)
        self.t_rooms_label = Label(self.t_rooms_frame, text='Rooms', font='Ubuntu 20 bold')
        self.notebook = ttk.Notebook(self.t_rooms_frame)
        self.t_common_frame = Frame(self.window, highlightbackground='black', highlightthickness=0.5)
        self.t_doors = []
        self.t_doors_frame = Frame(self.t_common_frame)
        self.t_doors_label = Label(self.t_doors_frame, text='Doors', font='Ubuntu 20 bold')
        self.t_others_frame = Frame(self.window, highlightbackground='black', highlightthickness=0.5)
        self.t_utils_frame = TUtils(self.remote_control.utils, self.t_others_frame)
        self.t_info_frame = TInfo(self.remote_control.info, self.t_others_frame)
        self.t_alarms = []
        self.t_alarms_frame = Frame(self.t_common_frame)
        self.t_alarms_label = Label(self.t_alarms_frame, text='Alarms', font='Ubuntu 20 bold')
        self.__setup__()

    def __setup__(self):
        self.__setup_window__()
        self.__setup_rooms__()
        self.__setup_doors__()
        self.__setup_alarms__()
        self.__setup_notebook__()
        self.__setup_frames__()

    def __setup_window__(self):
        self.window.title(str('Remote Control ' + self.remote_control.name))
        self.window.protocol("WM_DELETE_WINDOW", self.__finish__)

    def __setup_rooms__(self):
        self.t_rooms_label.pack(pady=10)
        for room in self.remote_control.rooms.values():
            t_room = TRoom(self.remote_control.send, room, self.notebook)
            t_room.pack()
            self.t_rooms.append(t_room)

    def __setup_doors__(self):
        self.t_doors_label.pack(pady=10)
        for door in self.remote_control.doors.values():
            t_door = TDoor(self.remote_control.send, door, self.t_doors_frame)
            t_door.pack(pady=6)
            self.t_doors.append(t_door)

    def __setup_alarms__(self):
        self.t_alarms_label.pack(pady=10)
        for alarm in self.remote_control.alarms.values():
            t_alarm = TAlarm(self.remote_control.send, alarm, self.t_alarms_frame)
            t_alarm.pack(pady=6)
            self.t_alarms.append(t_alarm)

    def __setup_notebook__(self):
        self.notebook.pack(expand=True, fill='both', side=LEFT)
        for t_room in self.t_rooms:
            self.notebook.add(t_room, text=t_room.room.name.capitalize())

    def __setup_frames__(self):
        self.t_others_frame.pack(expand=True, fill='both', side=LEFT, padx=1)
        self.t_rooms_frame.pack(expand=True, fill='both', side=LEFT, padx=1)
        self.t_common_frame.pack(expand=True, fill='both', side=LEFT, padx=1)
        self.t_alarms_frame.pack(expand=True, fill='both', padx=8)
        self.t_doors_frame.pack(expand=True, fill='both', padx=8)
        self.t_info_frame.pack(expand=True, fill='both', padx=8)
        self.t_utils_frame.pack(expand=True, fill='both', padx=8)

    def __run__(self):
        self.connect_window.destroy()
        self.remote_control.run()
        self.window.update()
        self.window.deiconify()
        self.window.mainloop()

    def start(self):
        self.window.withdraw()
        self.connect_window.mainloop()

    def __finish__(self):
        self.window.destroy()
        self.remote_control.finish()
