# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        nums = [i + 1 for i in range(n)]
        return self.helper(nums)

    def helper(self, nums):
        if not nums:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        trees = []
        for i in range(len(nums)):
            left_trees = self.helper(nums[:i])
            right_trees = self.helper(nums[i+1:])
            for l in left_trees:
                for r in right_trees:
                    tree = TreeNode(nums[i])
                    tree.left = l
                    tree.right = r
                    trees.append(tree)
        return trees