import abc


class QueueInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass

    @abc.abstractmethod
    def enqueue(self):
        pass

    @abc.abstractmethod
    def dequeue(self):
        pass

    @abc.abstractmethod
    def get_front(self):
        pass
