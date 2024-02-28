# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = 0
        self.minimum = float('inf')
        self.maximum = float('-inf')
        def min_max_finder(root, prev = None):
            if not root:
                return [prev, prev]
            left = min_max_finder(root.left, root.val)
            right = min_max_finder(root.right, root.val)
            self.minimum = min(left[0], right[0])
            self.maximum = max(left[1], right[1])
            self.max_diff = max(abs(root.val-self.minimum), abs(root.val-self.maximum), self.max_diff)
            return [min(self.minimum, root.val), max(self.maximum, root.val)]
        min_max_finder(root)
        return self.max_diff
            