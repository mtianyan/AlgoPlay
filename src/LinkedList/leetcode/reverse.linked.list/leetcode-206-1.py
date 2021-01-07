# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next  # cur 不能为空
            cur.next = pre  # 反转已完成
            pre = cur  # 为下次做准备
            cur = next
        # cur 为空时跳出循环，pre 为原链表最后一个节点
        return pre


if __name__ == '__main__':
    head = ListNode([1, 2, 3, 4, 5])
    print(Solution().reverseList(head))
