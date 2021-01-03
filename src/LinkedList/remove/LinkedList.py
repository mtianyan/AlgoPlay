class LinkedList:
    class Node:
        def __init__(self, e, next_node=None):
            self.e = e
            self.next_node = next_node

        def __str__(self):
            return str(self.e)

    def __init__(self):
        self.head = None
        self.size = 0
        self.dummy_head = self.Node(None, None)

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        self.add(0, e)
        # node = self.Node(e)
        # node.next_node = self.head
        # self.head = node
        # self.head = self.Node(e, self.head)
        # self.size = self.size + 1

    def add(self, index, e):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        # if index == 0:
        #     self.add_first(e)
        # else:
        prev = self.dummy_head
        for i in range(index):
            prev = prev.next_node
        # node = self.Node(e)
        # node.next_node = prev.next_node
        # prev.next_node = node
        prev.next_node = self.Node(e, prev.next_node)
        self.size = self.size + 1

    def add_last(self, e):
        self.add(self.size, e)

    def get(self, index):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        cur = self.dummy_head.next_node
        for i in range(index):
            cur = cur.next_node
        return cur.e

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self.size)

    def set(self, index, e):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        cur = self.dummy_head.next_node
        for i in range(index):
            cur = cur.next_node
        cur.e = e

    def contains(self, e):
        cur = self.dummy_head.next_node
        while cur is not None:
            if cur.e == e:
                return True
            cur = cur.next_node
        return False

    def __str__(self):
        ret = []
        cur = self.dummy_head
        # while cur is not None:
        #     if cur:
        #         ret.append(str(cur.next_node))
        #     cur = cur.next_node
        for i in range(self.size):
            if cur:
                ret.append(str(cur.next_node))
            cur = cur.next_node
        return "->".join(ret) + "->None"

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        prev = self.dummy_head
        for i in range(index):
            prev = prev.next_node
        ret_node = prev.next_node
        prev.next_node = ret_node.next_node
        self.size = self.size -1
        return ret_node

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.size - 1)


if __name__ == '__main__':
    l = LinkedList()
    l.add_first(1)
    print(l)
    l.add_first(2)
    print(l)
    l.add_last(3)
    l.add(2, 55)
    print(l)
    l.remove(2)
    print(l)
    l.remove_first()
    print(l)
    l.remove_last()
    print(l)
