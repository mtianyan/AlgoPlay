from Stack import StackInterface
from ArrayTyping import Array


class ArrayStack(StackInterface):
    def __init__(self, capacity):
        self.array = Array(capacity)

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.is_empty()

    def get_capacity(self):
        return self.array.get_capacity()

    def push(self, e):
        self.array.add_last(e)

    def pop(self):
        return self.array.remove_last()

    def peek(self):
        return self.array.get_last()

    def __str__(self):
        return f'size: {self.get_size()} capacity: {self.get_capacity()} ' + str(self.array) + "<-top"


if __name__ == '__main__':
    a = ArrayStack(10)
    a.push(1)
    a.push(2)
    print(a)
    a.pop()
    print(a)