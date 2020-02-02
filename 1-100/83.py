# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        val = None
        current = None
        while tmp:
            if not current:
                current = tmp
                val = tmp.val
            elif tmp.val != val:
                current.next = tmp
                current = tmp
                val = tmp.val
            tmp = tmp.next
        if current:
            current.next = None
        return head