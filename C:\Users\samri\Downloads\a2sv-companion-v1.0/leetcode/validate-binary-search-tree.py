# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.output = []
        self.inorderTraverse(root)
        for i in range(1, len(self.output)):
            if self.output[i] <= self.output[i-1]:
                return False
        return True
    def inorderTraverse(self, root):
        if not root:
            return
        self.inorderTraverse(root.left)
        self.output.append(root.val)
        self.inorderTraverse(root.right)
        return self.output
