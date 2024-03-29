class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder, seeker = 0, 0
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                placeholder += 1
            seeker += 1