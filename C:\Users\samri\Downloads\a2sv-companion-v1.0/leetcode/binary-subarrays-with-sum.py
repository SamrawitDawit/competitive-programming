class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq_sum = {}
        accumulator = 0
        ans = 0
        for i in range(len(nums)):
            accumulator += nums[i]
            nums[i] = accumulator
            if accumulator == goal:
                ans += 1
            if accumulator -goal in freq_sum:
                ans += freq_sum[accumulator-goal]
            freq_sum[accumulator] = freq_sum.get(accumulator, 0)+1   
        print(nums)
        print(freq_sum)
        return ans