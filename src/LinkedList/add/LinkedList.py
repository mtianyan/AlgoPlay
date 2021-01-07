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

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        # node = self.Node(e)
        # node.next_node = self.head
        # self.head = node
        self.head = self.Node(e, self.head)
        self.size = self.size + 1

    def add(self, index, e):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        if index == 0:
            self.add_first(e)
        else:
            prev = self.head
            for i in range(index - 1):
                prev = prev.next_node
            # node = self.Node(e)
            # node.next_node = prev.next_node
            # prev.next_node = node
            prev.next_node = self.Node(e, prev.next_node)
            self.size = self.size + 1

    def add_last(self, e):
        self.add(self.size, e)

