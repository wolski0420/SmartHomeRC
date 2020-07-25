from Observation.observable import Observable


class Info(Observable):
    def __init__(self, ip, port):
        Observable.__init__(self)
        self.ip = ip
        self.port = port

    def change_ip(self, ip):
        self.ip = ip
        self.notify_observers()

    def change_port(self, port):
        self.port = port
        self.notify_observers()

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port
