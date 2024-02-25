# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.number = 0
        return self.traverse(root)
    def traverse(self, root, string = ''):
        if root == None:
            return 
        if not root.left and not root.right:
            string += str(root.val)
            self.number += int(string)
        else:
            string +=  str((root.val))
            self.traverse(root.left, string)
            self.traverse(root.right, string)
        return self.number