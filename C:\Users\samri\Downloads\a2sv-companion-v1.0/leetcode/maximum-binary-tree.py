# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def traverse(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])  
            mid = nums.index(max(nums[l:r+1]))
            root = TreeNode(nums[mid])
            root.left = traverse(l, mid-1)
            root.right = traverse(mid+1, r)
            return root
        return traverse(0, len(nums)-1)
  
        


            

            
