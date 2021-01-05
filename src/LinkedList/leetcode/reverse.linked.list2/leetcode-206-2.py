# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归到底
        # 划分子问题
        if head == None or head.next == None:
            return head
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev


if __name__ == '__main__':
    head = ListNode([1, 2, 3, 4, 5])
    print(Solution().reverseList(head))
