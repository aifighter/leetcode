# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ret = head.next
        curr = head.next
        prev = head
        while(True):
            if not curr.next:
                curr.next = prev
                prev.next = None
                return ret
            if not curr.next.next:
                prev.next = curr.next
                curr.next = prev
                return ret
            new_prev, new_curr = curr.next, curr.next.next
            prev.next = curr.next.next
            curr.next = prev
            prev, curr = new_prev, new_curr