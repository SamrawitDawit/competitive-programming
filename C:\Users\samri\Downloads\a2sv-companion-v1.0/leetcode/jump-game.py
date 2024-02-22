class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums) - 1
        while good > 0:
            j = good-1
            while j > 0 and nums[j] < (good-j):
                j -= 1
            if nums[j] >= (good-j):
                good = j
            else:
                return 0
        if good == 0:
            return True
        return False