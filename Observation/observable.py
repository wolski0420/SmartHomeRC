class Observable:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, information=None):
        for observer in self._observers:
            observer.notify(information=information)
