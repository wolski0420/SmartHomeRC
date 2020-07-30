from Observation.observable import Observable


class Info(Observable):
    def __init__(self, ip, port):
        Observable.__init__(self)
        self.ip = ip
        self.port = port
        self.description = 'This is the remote control for your smart home system. ' \
                           'You can block any door, turn on any alarm or change light color or brightness. ' \
                           'It is also possible to turn on/off any device which can be managed from without. ' \
                           'To change something, just click the button \"change\" close to your chosen property!'

    def change_ip(self, ip):
        self.ip = ip
        self.notify_observers()

    def change_port(self, port):
        self.port = port
        self.notify_observers()
