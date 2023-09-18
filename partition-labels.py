class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        start = 0
        end = 0
        ans = []
        for i in range(len(s)):
            dic[s[i]] = i
        for i in range(len(s)):
            end = max(dic[s[i]], end)
            if i == end:
                ans.append((end-start)+1)
                start = end+1
        return ans
