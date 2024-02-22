# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []
        return self.traverse(root)
    def traverse(self, root):
        if root == None:
            return 
        else:
            self.output.append (root.val)
            self.traverse(root.left)
            self.traverse(root.right)
        return self.output
        