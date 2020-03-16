# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        tmp = dummy.next
        prev = dummy
        cnt = 1

        while(tmp):
            if cnt < m:
                prev = tmp
                tmp = tmp.next
            if cnt == m:
                node_m = tmp
                node_m_prev = prev
                prev = tmp
                tmp = tmp.next
            if m < cnt <= n:
                current = tmp
                tmp = tmp.next
                current.next = prev
                prev = current
                if cnt == n:
                    node_n = current
                    node_n_next = tmp
                    break
            cnt += 1
        
        node_m_prev.next = node_n
        node_m.next = node_n_next

        return dummy.next