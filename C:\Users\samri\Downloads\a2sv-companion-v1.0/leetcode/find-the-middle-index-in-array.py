class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        accumulator = 0
        for i in range(len(nums)):
            accumulator += nums[i]
            nums[i] = accumulator
        prev = 0
        for i in range(len(nums)):
            if prev == nums[-1]-nums[i]:
                return i
            prev = nums[i]
        return -1
