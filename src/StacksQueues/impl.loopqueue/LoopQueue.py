from Queue import QueueInterface
from ArrayTyping import Array


class LoopQueue(QueueInterface):
    def __init__(self, capacity):
        self.data = [None] * capacity
        self._capacity = capacity
        self.front = 0
        self.tail = 0
        self.size = 0

    def get_capacity(self):
        return self._capacity - 1

    def is_empty(self):
        return self.front == self.tail

    def get_size(self):
        return self.size

    def enqueue(self, e):
        if (self.tail + 1) % self._capacity == self.front:
            self.resize(self._capacity * 2)
        self.data[self.tail] = e
        self.tail = (self.tail + 1) % self._capacity
        self.size = self.size + 1

    def resize(self, new_capacity):
        new_data = [None for one in range(new_capacity)]
        for i, one in enumerate(self.data[:new_capacity]):
            new_data[i] = self.data[(i + self.front) % self._capacity]
        self.data = new_data
        self.front = 0
        self._capacity = new_capacity

    def dequeue(self):
        if self.is_empty():
            raise ValueError("队列为空，不可出队")
        print("self.front", self.front)
        print("self._capacity", self._capacity)
        ret = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self._capacity
        self.size = self.size - 1
        if self.size == self._capacity // 4:
            self.resize(self._capacity // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise ValueError("队列为空")
        return self.data[self.front]

    def __str__(self):
        return f'size: {self.get_size()} capacity: {self.get_capacity()} front: {self.front} tail: {self.tail} ' + "loop queue->" + str(self.data)


if __name__ == '__main__':
    aq = LoopQueue(10)
    for i in range(10):
        aq.enqueue(i)
        if i % 3 == 1:
            aq.dequeue()
    print(aq)
