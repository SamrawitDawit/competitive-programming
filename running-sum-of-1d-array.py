class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        return prefix_sum[1:]
