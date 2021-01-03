from Queue import QueueInterface


class Node:
    def __init__(self, e, next_node=None):
        self.e = e
        self.next_node = next_node

    def __str__(self):
        return str(self.e)


class LinkedListQueue(QueueInterface):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        if self.tail is None:
            self.tail = Node(e)
            self.head = self.tail
        else:
            self.tail.next_node = Node(e)
            self.tail = self.tail.next_node
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("empty")
        ret_node = self.head
        self.head = self.head.next_node
        ret_node.next_node = None
        if self.head is None:
            # 只有一个元素
            self.tail = None
        self.size = self.size - 1
        return ret_node

    def get_front(self):
        if self.is_empty():
            raise ValueError("empty")
        return self.head.e

    def __str__(self):
        ret = []
        cur = self.head
        while cur is not None:
            ret.append(str(cur))
            cur = cur.next_node
        return "queue: front:" + "->".join(ret) + "->tail"


if __name__ == '__main__':
    aq = LinkedListQueue()
    for i in range(10):
        aq.enqueue(i)
        print(aq)
        if i % 3 == 2:
            aq.dequeue()
            print(aq)
