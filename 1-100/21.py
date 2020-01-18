# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        ret = ListNode(0)
        tmp = ret
        while True:
            if not l1:
                tmp.val = l2.val
                tmp.next = l2.next
                break
            if not l2:
                tmp.val = l1.val
                tmp.next = l1.next
                break
            if l1.val < l2.val:
                tmp.val = l1.val
                tmp.next = ListNode(0)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.val = l2.val
                tmp.next = ListNode(0)
                tmp = tmp.next
                l2 = l2.next
        return ret
