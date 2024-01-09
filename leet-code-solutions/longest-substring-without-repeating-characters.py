class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        maximum = 0
        for letter in s:
            while letter in dic:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    dic.pop(s[l])
                l += 1
            dic[letter] = 1
            maximum = max(maximum, len(dic))
        return maximum