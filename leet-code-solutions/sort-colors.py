class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        last = len(nums)-1
        while l<=r and r<=last:
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[r] == 2:
                nums[last], nums[r] = nums[r], nums[last]
                last -= 1
            else:
                r += 1
            