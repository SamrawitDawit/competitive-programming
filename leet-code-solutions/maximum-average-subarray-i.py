class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, i, summ, maximum= 0, 0, 0, float("-inf")
        while i < len(nums):
            summ += nums[i]
            if i >= k-1:
                maximum = max(summ, maximum)
                summ -= nums[l] 
                l+= 1
            i += 1
        return (maximum/k)
            
        