# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                ans.append(depth_dic[y])
            else:
                ans.append(depth_dic[y][::-1])
        return ans
