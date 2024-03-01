# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.output = []
        self.traverse(root)
        return self.new_traverse(0, len(self.output)-1)
    def traverse(self, node):
        if not node:
            return 
        self.traverse(node.left)
        self.output.append(node.val)
        self.traverse(node.right)
        return self.output
    def new_traverse(self, l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(self.output[l])  
            mid = (l+r)//2
            root = TreeNode(self.output[mid])
            root.left = self.new_traverse(l, mid-1)
            root.right = self.new_traverse(mid+1, r)
            return root