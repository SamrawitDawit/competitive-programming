# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        depth_dic = collections.defaultdict(list)
        def depth(root, y):
            if not root:
                return
            depth_dic[y].append(root.val)
            depth(root.left, y+1)
            depth(root.right, y+1)
        depth(root, 0)
        ans = []
        for y in depth_dic:
            if y % 2 == 0:
                for i in range(len(depth_dic[y])):
                    if depth_dic[y][i] % 2  == 0 or (i > 0 and depth_dic[y][i] <= depth_dic[y][i-1]):
                        return False
            else:
                for i in range(len(depth_dic[y])):
                    if depth_dic[y][i] % 2  != 0 or (i > 0 and depth_dic[y][i] >= depth_dic[y][i-1]):
                        return False
        return True