# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode], max_sum = 0) -> int:
        self.ans = 0 
        def helper(root):
            if not root:
                return True,0,inf,-inf 
            
            isLeftBST,leftSum,leftMin,leftMax = helper(root.left)           
            isRightBST,rightSum,rightMin,rightMax = helper(root.right)
            
            if (isLeftBST and root.val>leftMax) and (isRightBST and root.val<rightMin):
                thisSum = root.val+leftSum+rightSum
                new_max = max(rightMax,root.val)
                new_min = min(leftMin,root.val)
                self.ans = max(self.ans, thisSum) 
                return True, thisSum, new_min, new_max
            else:
                return False,-math.inf,0,0
        helper(root)
        return self.ans
    #     if not root:
    #         return
    #     self.max_sum = max_sum
    #     thisSum = self.inorder_traverse(root)
    #     self.max_sum = max(self.max_sum, thisSum)
    #     if self.max_sum != 0:
    #         return (self.max_sum + prev.val)
    #     self.maxSumBST(root.left, self.max_sum)
    #     self.maxSumBST(root.right, self.max_sum)
    #     return self.max_sum
    # def inorder_traverse(self, root):
    #     self.output = []
    #     self.traverse(root)
    #     for i in range(1, len(self.output)):
    #         if self.output[i] <= self.output[i-1] or self.output[i] < 0:
    #             return 0      
    #     return sum(self.output)
    # def traverse(self, node):
    #     if not node:
    #         return 
    #     self.traverse(node.left)
    #     self.output.append(node.val)
    #     self.traverse(node.right)
    #     return self.output
    