# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])

        left_len = inorder.index(postorder[-1])
        right_len = len(inorder) - left_len - 1

        left_postorder = postorder[:left_len]
        right_postorder = postorder[left_len:left_len+right_len]

        left_inorder = inorder[:left_len]
        right_inorder = inorder[1+left_len:]

        left_node = self.buildTree(left_inorder, left_postorder)
        right_node = self.buildTree(right_inorder, right_postorder)

        root.left = left_node
        root.right = right_node

        return root