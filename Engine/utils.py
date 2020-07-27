class Utils:
    def __init__(self, send_func, rooms, alarms, doors):
        self.__send_func = send_func
        self.__rooms = rooms
        self.__alarms = alarms
        self.__doors = doors

    def turn_off_the_lights(self):
        for room in self.__rooms.values():
            for light in room.lighting.values():
                if light.get_power_status() == 'On':
                    self.__send_func(light.location, 'power=off')

    def turn_on_the_lights(self):
        for room in self.__rooms.values():
            for light in room.lighting.values():
                if light.get_power_status() == 'Off':
                    self.__send_func(light.location, 'power=on')

    def turn_off_the_devices(self):
        for room in self.__rooms.values():
            for device in room.devices.values():
                if device.get_power_status() == 'On':
                    self.__send_func(device.location, 'power=off')

    def turn_on_the_devices(self):
        for room in self.__rooms.values():
            for device in room.devices.values():
                if device.get_power_status() == 'Off':
                    self.__send_func(device.location, 'power=on')

    def block_all_doors(self):
        for door in self.__doors.values():
            if door.get_blockade_status() == 'Unblocked':
                self.__send_func(str('door/' + door.room1.name + '-' + door.room2.name), 'blockade_status=block')

    def unblock_all_doors(self):
        for door in self.__doors.values():
            if door.get_blockade_status() == 'Blocked':
                self.__send_func(str('door/' + door.room1.name + '-' + door.room2.name), 'blockade_status=unblock')

    def turn_on_the_alarms(self):
        for alarm in self.__alarms.values():
            if alarm.get_power_status() == 'Off':
                self.__send_func(str('alarm/' + alarm.location + '-' + alarm.name), 'power=on')

    def turn_off_the_alarms(self):
        for alarm in self.__alarms.values():
            if alarm.get_power_status() == 'On':
                self.__send_func(str('alarm/' + alarm.location + '-' + alarm.name), 'power=off')
