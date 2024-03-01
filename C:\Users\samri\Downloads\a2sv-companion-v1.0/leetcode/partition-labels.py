class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {num:i for i, num in enumerate(s)}
        size, end, ans = 0, 0, []
        for i in range(len(s)):
            size += 1
            end = max(dic[s[i]], end)
            if i == end:
                ans.append(size)
                size = 0
        return ans


            

            