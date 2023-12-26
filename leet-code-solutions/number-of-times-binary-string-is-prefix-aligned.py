class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ones = 0
        maxi = 0
        res = 0
        for flip in flips:
            maxi = max(maxi, flip)
            ones += 1
            if maxi == ones:
                res += 1
        return res