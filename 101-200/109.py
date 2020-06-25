# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 算出长度
        l = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            l += 1
        # 特殊情况
        if l == 0:
            return None
        if l == 1:
            return TreeNode(head.val)
        # 找到左list，中间value，右list
        mid = l // 2
        left_list = head
        tmp, prev = head, None
        for i in range(mid):
            prev = tmp
            tmp = tmp.next
        prev.next = None
        mid_val = tmp.val
        right_list = tmp.next
        # 构成树
        ret = TreeNode(mid_val)
        ret.left = self.sortedListToBST(left_list)
        ret.right = self.sortedListToBST(right_list)
        return ret