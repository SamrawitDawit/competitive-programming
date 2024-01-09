class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, summ, min_len = 0, 0, len(nums)+1
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                min_len = min(min_len, r-l+1)
                summ -= nums[l]
                l += 1
        if min_len == len(nums)+1:
            return 0
        return min_len

        
