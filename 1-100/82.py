# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head

        start, current = None, None
        tmp = head
        prev = None
        while tmp:
            # 找到唯一的节点，即与前一个节点不同(或没有前一个节点)，且与后一个节点不同（或不存在后一个节点）
            if (prev is None or tmp.val != prev.val) and (tmp.next is None or tmp.next.val != tmp.val):
                if start is None:
                    start = tmp
                    current = tmp
                else:
                    current.next = tmp
                    current = tmp
            prev = tmp
            tmp = tmp.next
        if current:
            current.next = None
        return start