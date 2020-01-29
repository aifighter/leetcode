# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # 长度和结尾节点，并且拼接成首尾相连
        n = 1
        tmp = head
        while(tmp.next is not None):
            n += 1
            tmp = tmp.next
        end = tmp
        end.next = head
        # 找到开始节点和开始节点前一个
        start_idx = (n - k % n) % n
        prev_idx = (n + start_idx - 1) % n
        start = head
        for i in range(start_idx):
            start = start.next
        prev = head
        for i in range(prev_idx):
            prev = prev.next
        prev.next = None
        return start