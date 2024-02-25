# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.left = []
        self.right = []
        self.leftSide_traverse(root)
        self.rightSide_traverse(root)
        return self.left == self.right
    def leftSide_traverse(self, root):
        if root == None:
            self.left.append('None')
            return 
        else:
            self.left.append(root.val)
            self.leftSide_traverse(root.left)
            self.leftSide_traverse(root.right)
        return self.left
    def rightSide_traverse(self, root):
        if root == None:
            self.right.append('None')
            return 
        else:
            self.right.append(root.val)
            self.rightSide_traverse(root.right)
            self.rightSide_traverse(root.left)
        return self.right

        