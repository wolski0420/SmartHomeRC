class Utils:
    def __init__(self, send_func, rooms, alarms, doors):
        self.send_func = send_func
        self.rooms = rooms
        self.alarms = alarms
        self.doors = doors

    def turn_off_the_lights(self):
        for room in self.rooms.values():
            for light in room.lighting.values():
                if light.get_power_status() == 'On':
                    self.send_func(light.location, 'power=off')

    def turn_on_the_lights(self):
        for room in self.rooms.values():
            for light in room.lighting.values():
                if light.get_power_status() == 'Off':
                    self.send_func(light.location, 'power=on')

    def turn_off_the_devices(self):
        for room in self.rooms.values():
            for device in room.devices.values():
                if device.get_power_status() == 'On':
                    self.send_func(device.location, 'power=off')

    def turn_on_the_devices(self):
        for room in self.rooms.values():
            for device in room.devices.values():
                if device.get_power_status() == 'Off':
                    self.send_func(device.location, 'power=on')

    def block_all_doors(self):
        for door in self.doors.values():
            if door.get_blockade_status() == 'Unblocked':
                self.send_func(str('door/' + door.room1.name + '-' + door.room2.name), 'BlockadeStatus=block')

    def unblock_all_doors(self):
        for door in self.doors.values():
            if door.get_blockade_status() == 'Blocked':
                self.send_func(str('door/' + door.room1.name + '-' + door.room2.name), 'BlockadeStatus=unblock')

    def turn_on_the_alarms(self):
        for alarm in self.alarms.values():
            if alarm.get_power_status() == 'Off':
                self.send_func(str('alarm/' + alarm.location + '-' + alarm.name), 'power=on')

    def turn_off_the_alarms(self):
        for alarm in self.alarms.values():
            if alarm.get_power_status() == 'On':
                self.send_func(str('alarm/' + alarm.location + '-' + alarm.name), 'power=off')
