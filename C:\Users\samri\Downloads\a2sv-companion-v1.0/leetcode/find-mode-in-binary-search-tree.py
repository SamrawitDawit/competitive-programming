# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.counter = collections.defaultdict(int)
        self.traverse(root)
        sortedDict = sorted(self.counter.items(), key = lambda x: x[1], reverse=True)
        ans = []
        for i in range(len(sortedDict)):
            if sortedDict[i][1] == sortedDict[0][1]:
                ans.append(sortedDict[i][0])
        return ans
    def traverse(self, root):
        if root == None:
            return 
        else:
            self.counter[root.val] += 1
            self.traverse(root.left)
            self.traverse(root.right)
        return self.counter
        