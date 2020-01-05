# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        c = head
        while c:
            nodes.append(c)
            c = c.next
        if len(nodes) == n:
            return head.next
        prev = nodes[- n - 1]
        delete = nodes[-n]
        prev.next = delete.next
        return head