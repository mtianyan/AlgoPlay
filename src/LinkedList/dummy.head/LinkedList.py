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

    def __str__(self):
        ret = []
        a = self.head
        while a.next_node:
            a = a.next_node
            ret.append(str(a.next_node))
        return "->".join(ret)


if __name__ == '__main__':
    l = LinkedList()
    l.add_first(1)
    l.add_last(2)
    print(l)
