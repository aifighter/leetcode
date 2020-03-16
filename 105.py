# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])

        left_len = inorder.index(preorder[0])
        right_len = len(preorder) - left_len - 1

        left_preorder = preorder[1:1+left_len]
        right_preorder = preorder[1+left_len:]

        left_inorder = inorder[:left_len]
        right_inorder = inorder[1+left_len:]

        left_node = self.buildTree(left_preorder, left_inorder)
        right_node = self.buildTree(right_preorder, right_inorder)

        root.left = left_node
        root.right = right_node

        return root