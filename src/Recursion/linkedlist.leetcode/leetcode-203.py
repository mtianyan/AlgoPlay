# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = head
        if head is None:
            return head
        while prev.next is not None:
            if prev.next.val == val:
                del_node = prev.next
                prev.next = del_node.next
                # 如果删除了，那么prev 不向后挪
            else:
                prev = prev.next
        while head is not None and head.val == val:
            head = head.next
        return head
