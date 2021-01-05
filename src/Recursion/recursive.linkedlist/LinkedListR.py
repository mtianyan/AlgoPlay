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
        # self.dummy_head = self.Node(None, None)

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

    #  在以node为头结点的链表的index位置插入元素e，递归算法
    def _add(self, node, index, e):
        if index == 0:
            # 最基本问题
            return self.Node(e, next_node=node)
        node.next_node = self._add(node.next_node, index - 1, e)
        return node

    # 在链表的index(0-based)位置添加新的元素e
    def add(self, index, e):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        self.head = self._add(self.head, index, e)
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
        cur = self.head
        # while cur is not None:
        #     if cur:
        #         ret.append(str(cur.next_node))
        #     cur = cur.next_node
        for i in range(self.size):
            if cur:
                ret.append(str(cur))
            cur = cur.next_node
        return "->".join(ret) + "->None"

    # 从以node为头结点的链表中，删除第index位置的元素，递归算法
    # 返回值包含两个元素，删除后的链表头结点和删除的值：）
    def _remove(self, node, index):
        if index == 0:
            return node.next_node, node.e
        ret_node, value = self._remove(node.next_node, index - 1)
        node.next_node = ret_node
        return node, value

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("index error")
        head, value = self._remove(self.head, index)
        self.size = self.size - 1
        return value

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
