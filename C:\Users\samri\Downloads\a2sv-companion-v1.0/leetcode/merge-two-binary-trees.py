# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode], prevOfRoot1=None, prevOfRoot2=None) -> Optional[TreeNode]:
        if not root1:
            return root2
        if root2:
            root2.val = root2.val + root1.val
        else:
            new_node = TreeNode(root1.val)
            if prevOfRoot2:
                if root1 == prevOfRoot1.left:
                    prevOfRoot2.left = new_node
                else:
                    prevOfRoot2.right = new_node
                root2 = new_node
                prevOfRoot2 = new_node
            else:
                return root1
        self.mergeTrees(root1.left, root2.left, root1, root2)
        self.mergeTrees(root1.right, root2.right, root1, root2)
        return root2