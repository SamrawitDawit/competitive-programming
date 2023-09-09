class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        length = 0
        while r < len(s):
            if s[r] in s[l:r]:
                length = r - l
                max_len = max(max_len, length)
                l+=1
                length-=1
            else:
                r += 1
                length += 1
        max_len = max(max_len, length)
        return max_len
