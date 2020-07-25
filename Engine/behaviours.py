class Behaviours:
    def __init__(self, client, rooms, doors, alarms):
        self.client = client
        self.rooms = rooms
        self.doors = doors
        self.alarms = alarms

    def __on_message__(self, client, user_data, msg):
        topic = msg.topic.split('/')
        message = str(msg.payload.decode('utf-8')).split('=')

        if topic[0] == 'door':
            door = self.doors[topic[1]]
            if door is None:
                return

            door.change_blockade(message[1])
        elif topic[0] == 'alarm':
            alarm = self.alarms[topic[1]]
            if alarm is None:
                return

            alarm.change_power(message[1])
        else:
            room = self.rooms[topic[0]]
            if room is None:
                return

            if topic[1] == 'light':
                light = room.lighting[topic[2]]
                if light is None:
                    return

                if message[0] == 'power':
                    light.change_power(message[1])
                elif message[0] == 'brightness':
                    light.change_brightness(message[1])

            elif topic[1] == 'device':
                device = room.devices[topic[2]]
                if device is None:
                    return

                device.change_power(message[1])

    def set_on_message(self):
        self.client.on_message = self.__on_message__

    def set_all(self):
        self.set_on_message()
