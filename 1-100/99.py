# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        a = self.find_a(root)
        self.prev = None
        b = self.find_b(root)
        a.val, b.val = b.val, a.val

    def find_a(self, root):
        if root.left:
            left = self.find_a(root.left)
            if left:
                return left
        if self.prev and root.val < self.prev.val:
            return self.prev
        else:
            self.prev = root
        if root.right:
            right = self.find_a(root.right)
            if right:
                return right
        return None

    def find_b(self, root):
        if root.right:
            right = self.find_b(root.right)
            if right:
                return right
        if self.prev and root.val > self.prev.val:
            return self.prev
        else:
            self.prev = root
        if root.left:
            left = self.find_b(root.left)
            if left:
                return left
        return None