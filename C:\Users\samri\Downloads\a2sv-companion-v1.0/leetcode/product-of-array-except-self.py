class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]*(len(nums)+1)
        for i in range(len(p)-2, 0, -1):
            p[i] = p[i+1]*nums[i]
        prefix = 1
        for i in range(len(nums)):
            p[i] = p[i+1]*prefix
            prefix*= nums[i]
        return p[:len(nums)]