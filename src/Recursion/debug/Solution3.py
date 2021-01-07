from ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def gen_depth(depth):
    return (depth+1) * "--"
class Solution:
    def removeElements(self, head: ListNode, val: int, depth) -> ListNode:
        depth_str = gen_depth(depth)
        print(depth_str, end="\t")
        print("call: remove", val, "in", head)
        # 问题规模最小的解
        if head is None:
            print(depth_str, end="\t")
            print("return:", head)
            return head
        res = self.removeElements(head.next, val, depth+1)
        print(depth_str, end="\t")
        print("after remove", val, ":", res)

        if head.val == val:
            ret = res
        else:
            head.next = res
            ret = head

        print(depth_str, end="\t")
        print("after remove", val, ":", res)

        return ret


if __name__ == '__main__':
    head = ListNode([1, 2, 6, 3, 4, 5, 6])
    print(Solution().removeElements(head, 6, 0))
