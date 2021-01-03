from Queue import QueueInterface
from ArrayTyping import Array


class ArrayQueue(QueueInterface):
    def __init__(self, capacity):
        self.array = Array(capacity)

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.array.is_empty()

    def enqueue(self, e):
        return self.array.add_last(e)

    def dequeue(self):
        return self.array.remove_first()

    def get_front(self):
        return self.array.get_first()

    def get_capacity(self):
        return self.array.get_capacity()

    def __str__(self):
        return f'size: {self.get_size()} capacity: {self.get_capacity()} ' + "queue->" + str(self.array)


if __name__ == '__main__':
    aq = ArrayQueue(10)
    aq.enqueue(1)
    aq.enqueue(2)
    aq.dequeue()
    print(aq)
