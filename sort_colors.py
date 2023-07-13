class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)-i):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    swap += 1
            if swap == 0:
                break
