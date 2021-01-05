# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        val_list = []
        if head == None:
            return head
        while head.next:
            val_list.append(head.val)
            head = head.next
        # print(val_list[::-1])
        cur = head
        for one in val_list[::-1]:
            cur.next = ListNode(one)
            cur = cur.next
        cur.next = None
        return head


if __name__ == '__main__':
    head = ListNode([1, 2, 3, 4, 5])
    print(Solution().reverseList(head))
