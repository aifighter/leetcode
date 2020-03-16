# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, a, b):
        # 两树为空，对称
        if not a and not b:
            return True
        # 两树不空，继续比较
        elif a and b:
            return a.val == b.val and self.helper(a.left, b.right) and self.helper(a.right, b.left)
        # 一树为空，不对称
        else:
            return False
