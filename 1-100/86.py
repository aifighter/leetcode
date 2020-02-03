# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = None, None
        tmp_l, tmp_r = None, None
        tmp = head
        cnt = 0
        while tmp:
            if tmp.val < x:
                if not left:
                    left = tmp
                    tmp_l = tmp
                else:
                    tmp_l.next = tmp
                    tmp_l = tmp
            else:
                if not right:
                    right = tmp
                    tmp_r = tmp
                else:
                    tmp_r.next = tmp
                    tmp_r = tmp
            tmp = tmp.next
        if tmp_r:
            tmp_r.next = None
        if not left:
            return right
        else:
            tmp_l.next = right
            return left