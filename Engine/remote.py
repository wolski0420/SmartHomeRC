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
        self.subscriber = mqtt.Client()
        self.publisher = mqtt.Client()

    def __subscribe_all__(self):
        for room in self.rooms.values():
            for light in room.lighting.values():
                self.subscriber.subscribe(light.location)
            for device in room.devices.values():
                self.subscriber.subscribe(device.location)

        for door in self.doors.values():
            self.subscriber.subscribe(str('door/' + door.room1.name + '-' + door.room2.name))

        for alarm in self.alarms.values():
            self.subscriber.subscribe(str('alarm/' + alarm.location + '-' + alarm.name))

    def __setup_client__(self):
        Behaviours(self.subscriber, self.rooms, self.doors, self.alarms).set_all()

    def __setup__(self):
        self.__setup_client__()
        self.__subscribe_all__()

    def run(self):
        self.subscriber.connect(self.info.ip, self.info.port)
        self.subscriber.loop_start()
        self.publisher.connect(self.info.ip, self.info.port)
        self.publisher.loop_start()
        self.__setup_client__()
        self.__subscribe_all__()

    def send(self, topic, message):
        self.publisher.publish(topic, message)

    def finish(self):
        self.subscriber.loop_stop()
        self.subscriber.disconnect()
        self.publisher.loop_stop()
        self.publisher.disconnect()
