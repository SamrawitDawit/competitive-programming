class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
        while r < len(nums):
            while len(set(nums[l:r+1])) == len(set(nums)):
                res += (len(nums)-r)
                l += 1
            r += 1
        return res