class ListNode:
    def __init__(self, x):
        if isinstance(x, list):
            self.val = x[0]
            cur = self
            for i in range(1, len(x)):
                cur.next = ListNode(x[i])
                cur = cur.next
        else:
            self.val = x
            self.next = None

    def __str__(self):
        cur = self
        ret = []
        while cur is not None:
            ret.append(cur.val)
            cur = cur.next
        return "->".join([str(one) for one in ret])


if __name__ == '__main__':
    print(ListNode([1, 2, 3]))
