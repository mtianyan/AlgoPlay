import abc


class StackInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass

    @abc.abstractmethod
    def push(self):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

    @abc.abstractmethod
    def peek(self):
        pass
