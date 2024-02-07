class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        for i in range(len(nums)):
            nums[i] += nums[i-1]
        for i in range(1, len(nums)-1):
            if nums[i-1] == nums[-1]-nums[i]:
                return i-1
        return -1
                    