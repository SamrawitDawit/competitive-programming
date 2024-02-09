class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix, maximum= 0, nums[0]
        for i in range(len(nums)):
            prefix = max(0, prefix)
            prefix += nums[i]
            maximum = max(maximum, prefix)
        return maximum
