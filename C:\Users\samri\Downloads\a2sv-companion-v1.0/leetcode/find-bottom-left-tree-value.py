# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.leftMost = root
        def maxDepth(root, prev, y):
            if not root:
                if y > self.max_depth:
                    self.leftMost = prev
                    self.max_depth = y
                return 
            maxDepth(root.left, root, y+1)
            maxDepth(root.right, root, y+1)
        maxDepth(root, None, 0)
        return self.leftMost.val
            

            
        