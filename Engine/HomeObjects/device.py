from Engine.HomeObjects.object import *


class Device(Object):
    def __init__(self, name, location, power=False):
        Object.__init__(self, name, location, power)
