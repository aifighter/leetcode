# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        nodes = [root]
        depth = 0
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
                nodes = next_nodes
                depth += 1
        return depth