class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        r = len(s)-1
        res = 0
        ctr = 0
        while r >= 0:
            if s[r] == '1':
                res += ctr
            if s[r] == "0":
                while r>= 0 and s[r] == "0":
                    ctr += 1
                    r -= 1
            else:
                r -= 1
        return res