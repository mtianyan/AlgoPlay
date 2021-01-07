class LinkedList:
    class Node:
        def __init__(self, e, next_node):
            self.e = e
            self.next_node = next_node

        def __str__(self):
            return str(self.e)
