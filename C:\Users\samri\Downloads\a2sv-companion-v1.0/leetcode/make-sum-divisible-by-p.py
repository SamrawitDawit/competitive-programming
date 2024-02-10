class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        min_len = len(nums)
        dic = {}
        dic[0] = -1
        desired_remainder = sum(nums) % p
        accumulator = 0
        if desired_remainder == 0:
            return 0
        for i in range(len(nums)):
            accumulator += nums[i]
            nums[i] = accumulator
            diff = (accumulator-desired_remainder)%p
            if diff in dic:
                min_len = min(min_len, i-dic[diff])
            dic[accumulator%p] = i
        return -1 if min_len == len(nums) else min_len