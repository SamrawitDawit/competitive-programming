class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ptr1 = 0
        ptr2 = 0
        count = 0
        while ptr1 < len(g) and ptr2 < len(s):
            if g[ptr1] > s[ptr2]:
                ptr2 += 1
            else:
                count += 1
                ptr1 += 1
                ptr2 += 1
        return count