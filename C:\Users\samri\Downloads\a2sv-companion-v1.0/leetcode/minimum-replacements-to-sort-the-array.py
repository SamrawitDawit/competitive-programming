class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                space = ceil(nums[i]/nums[i+1])
                count += (space-1)
                nums[i] = nums[i]//space
        return count