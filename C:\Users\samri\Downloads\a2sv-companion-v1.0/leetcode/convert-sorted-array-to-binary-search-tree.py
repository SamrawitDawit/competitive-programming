# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left, right = 0, len(nums)-1
        def DAQ(l, r):
            mid = (l+r)//2
            if l>r:
                return None     
            left = DAQ(l, mid-1)
            right = DAQ(mid+1, r)
            root = TreeNode(nums[mid], left, right)
            return root
        return DAQ(left, right)
