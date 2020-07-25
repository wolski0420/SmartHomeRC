import paho.mqtt.client as mqtt
import Engine.ConfigSetup.parser as parser
from Engine.behaviours import *
from Engine.utils import *
from Engine.info import *


class RemoteControl:
    def __init__(self, name):
        self.name = name
        self.rooms = parser.setup_rooms()
        self.doors = parser.setup_doors(self.rooms)
        self.alarms = parser.setup_alarms()
        self.utils = Utils(self.send, self.rooms, self.alarms, self.doors)
        self.info = Info('127.0.0.1', 1883)
        self.client = mqtt.Client()

    def __subscribe_all__(self):
        for room in self.rooms.values():
            for light in room.lighting.values():
                self.client.subscribe(light.location)
            for device in room.devices.values():
                self.client.subscribe(device.location)

        for door in self.doors.values():
            self.client.subscribe(str('door/' + door.room1.name + '-' + door.room2.name))

        for alarm in self.alarms.values():
            self.client.subscribe(str('alarm/' + alarm.location + '-' + alarm.name))

    def __setup_client__(self):
        Behaviours(self.client, self.rooms, self.doors, self.alarms).set_all()

    def run(self):
        self.client.connect(self.info.get_ip(), self.info.get_port())
        self.client.loop_start()
        self.__setup_client__()
        self.__subscribe_all__()

    def send(self, topic, message):
        self.client.publish(topic, message)

    def finish(self):
        self.client.loop_stop()
        self.client.disconnect()
