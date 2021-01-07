from Stack import StackInterface
from LinkedList import LinkedList


class LinkedListStack(StackInterface):
    def __init__(self):
        self.list = LinkedList()

    def get_size(self):
        return self.list.get_size()

    def is_empty(self):
        return self.list.is_empty()

    def push(self, e):
        self.list.add_first(e)

    def pop(self):
        self.list.remove_first()

    def peek(self):
        self.list.get_first()

    def __str__(self):
        return "Stack top:" + str(self.list)


if __name__ == '__main__':
    a = LinkedListStack()
    a.push(1)
    a.push(2)
    print(a)
    a.pop()
    print(a)
