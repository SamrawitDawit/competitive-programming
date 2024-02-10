class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count('0')
        ones = s.count('1')
        prefix_zeros, prefix_ones, ans = 0, 0, 0
        for num in s:
            if num == '0':
                prefix_zeros += 1
                ans += (prefix_ones*(ones-prefix_ones))
            else:
                prefix_ones += 1
                ans += (prefix_zeros*(zeros-prefix_zeros))
        return ans
        