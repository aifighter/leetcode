# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        ret = l
        previous = 0
        while(True):
            temp = previous
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp, previous = temp%10, temp // 10
            l.val = temp
            if l1 or l2:
                l.next = ListNode(0)
                l = l.next
            else:
                break
        if previous == 1:
            l.next = ListNode(1)
        return ret
        