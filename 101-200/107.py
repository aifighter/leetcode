# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        nodes = [root]
        while True:
            next_nodes = []
            level = []
            for node in nodes:
                if node:
                    level.append(node.val)
                    next_nodes += [node.left, node.right]
            if not level:
                break
            else:
                res.append(level)
                nodes = next_nodes
        return res[::-1]