class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        max_sum = summ
        for i in range(k, len(nums)):
            summ = summ - nums[i-k] + nums[i]
            if summ > max_sum:
                max_sum = summ
        return max_sum/k
