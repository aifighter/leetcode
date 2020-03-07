# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 左边的最大值要比根小
        if root.left and self.findmax(root.left) >= root.val:
            return False
        # 右边的最小值要比根大
        if root.right and self.findmin(root.right) <= root.val:
            return False
        # 左右都要是二叉搜索树
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def findmax(self, root):
        res = 0
        tmp = root
        while tmp:
            res = tmp.val
            tmp = tmp.right
        return res

    def findmin(self, root):
        res = 0
        tmp = root
        while tmp:
            res = tmp.val
            tmp = tmp.left
        return res