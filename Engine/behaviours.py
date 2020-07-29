class Behaviours:
    def __init__(self, client, rooms, doors, alarms):
        self.__client = client
        self.__rooms = rooms
        self.__doors = doors
        self.__alarms = alarms

    def __on_message__(self, client, user_data, msg):
        topic = msg.topic.split('/')
        message = str(msg.payload.decode('utf-8')).split('=')

        if topic[0] == 'door':
            door = self.__doors[topic[1]]
            if door is None:
                return

            if message[0] == 'blockade_status':
                door.change_blockade(message[1])
        elif topic[0] == 'alarm':
            alarm = self.__alarms[topic[1]]
            if alarm is None:
                return

            if message[0] == 'power':
                alarm.change_power(message[1])
        elif topic[0] == 'room':
            room = self.__rooms[topic[1]]
            if room is None:
                return

            if topic[2] == 'light':
                light = room.lighting[topic[3]]
                if light is None:
                    return

                if message[0] == 'power':
                    light.change_power(message[1])
                elif message[0] == 'brightness':
                    light.change_brightness(message[1])
                elif message[0] == 'color':
                    light.change_color(message[1])

            elif topic[2] == 'device':
                device = room.devices[topic[3]]
                if device is None:
                    return

                if message[0] == 'power':
                    device.change_power(message[1])

    def set_on_message(self):
        self.__client.on_message = self.__on_message__

    def set_all(self):
        self.set_on_message()
