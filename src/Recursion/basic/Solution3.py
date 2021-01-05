from ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 问题规模最小的解
        if head is None:
            return head
        res = self.removeElements(head.next, val)
        if head.val == val:
            return res
        else:
            head.next = res
            return head


if __name__ == '__main__':
    head = ListNode([1, 2, 6, 3, 4, 5, 6])
    print(Solution().removeElements(head, 6))
