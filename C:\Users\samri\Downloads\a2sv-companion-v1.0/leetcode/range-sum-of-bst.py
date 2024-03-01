# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int, summ = 0) -> int:
        # if not root:
        #     return 0
        # if root.val >= low and root.val <= high:
        #     summ += root.val
        #     summ += self.rangeSumBST(root.right, low, high, summ)
        #     summ += self.rangeSumBST(root.left, low, high, summ)
        # elif root.val < low:
        #     summ += self.rangeSumBST(root.right, low, high, summ)
        #     return 0
        # elif root.val > high:
        #     summ += self.rangeSumBST(root.left, low, high, summ)
        #     return 0        
        # return summ
        self.summ = 0
        return self.traverse(root, low, high)
    def traverse(self, node, low, high):
        if not node:
            return 
        self.traverse(node.left, low, high)
        if node.val >= low and node.val <= high:
            self.summ += (node.val)
        self.traverse(node.right, low, high)
        return self.summ