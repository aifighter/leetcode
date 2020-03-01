# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nodes = [root]
        root.used = False
        while True:
            new_nodes = []
            all_used = True
            for node in nodes:
                if node.used:
                    new_nodes.append(node)
                    continue
                if node.left is not None:
                    all_used = False
                    node.left.used = False
                    new_nodes.append(node.left)
                node.used = True
                new_nodes.append(node)
                if node.right is not None:
                    all_used = False
                    node.right.used = False
                    new_nodes.append(node.right)
            nodes = new_nodes
            if all_used:
                break
        return [node.val for node in nodes]