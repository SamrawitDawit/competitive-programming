# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []
        def inorderTraverse(root):
            if not root:
                return
            inorderTraverse(root.left)
            sortedArr.append(root.val)
            inorderTraverse(root.right)
        inorderTraverse(root)
        return sortedArr[k-1]
