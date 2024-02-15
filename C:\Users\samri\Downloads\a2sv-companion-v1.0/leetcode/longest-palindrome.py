class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        longest = 0
        single = False
        for count in counter.values():
            if count % 2 != 0:
                single = True
            longest += 2*(count//2)
        if single:
            longest += 1
        return longest
