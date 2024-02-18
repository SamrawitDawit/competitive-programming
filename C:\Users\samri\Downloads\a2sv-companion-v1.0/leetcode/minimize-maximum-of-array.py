class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        summ = nums[0]
        for i in range(1, len(nums)):
            summ += nums[i]
            average = (summ //(i+1)) if summ % (i+1) == 0 else  (summ //(i+1))+1
            ans = max(average, ans)
        return ans
