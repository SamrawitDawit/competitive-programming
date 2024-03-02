# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        breadth_dic = collections.defaultdict(list)
        def breadth(root, x, y):           
            if not root:
                return           
            breadth_dic[x].append([root.val, y])
            breadth(root.left, x-1, y+1)
            breadth(root.right, x+1, y+1)    
        breadth(root, 0, 0)
        ans = []
        for item in sorted(breadth_dic.items()):
            arr = []
            for val in sorted(item[1], key = lambda x:[x[1], x[0]]):
                arr.append(val[0])
            ans.append(arr)
        return ans
