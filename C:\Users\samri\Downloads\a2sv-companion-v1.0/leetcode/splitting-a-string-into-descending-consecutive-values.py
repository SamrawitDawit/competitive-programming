class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(curr, prev):
            if curr == len(s):
                return True
            for j in range(curr, len(s)):
                currSplice = int(s[curr:j+1])
                if currSplice + 1 == prev and backtrack(j+1, currSplice):
                    return True
            return False
        for i in range(len(s)-1):
            firstSplice = int(s[:i+1])
            if backtrack(i+1, firstSplice):
                return True
        return False
        