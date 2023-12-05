class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        indx = 0
        while indx < len(nums)-2:
            if nums[indx] < (nums[indx+1] + nums[indx+2]):
                return nums[indx]+nums[indx+1]+nums[indx+2]
            indx += 1
        return 0