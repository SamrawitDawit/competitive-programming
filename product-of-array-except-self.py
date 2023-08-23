class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]*len(nums)
        prefix = 1
        for i in range(len(p)):
            p[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(p)-1, -1, -1):
            p[i] *= postfix
            postfix *= nums[i]
        return p
