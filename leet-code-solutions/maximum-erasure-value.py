class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, summ, max_sum = 0, 0, 0
        dic = {}
        for r in range(len(nums)):
            if nums[r] in dic:
                while l<r and l < dic[nums[r]] + 1:
                    summ -= nums[l]
                    l += 1
            dic[nums[r]] = r
            summ += nums[r]
            max_sum = max(max_sum, summ)
        return max_sum
