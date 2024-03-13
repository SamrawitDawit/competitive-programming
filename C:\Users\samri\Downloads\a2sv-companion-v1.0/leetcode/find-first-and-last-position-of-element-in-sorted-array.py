class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums)-1
        mid = (left + right)//2
        leftBound = None
        while left <= right:
            if nums[mid] == target:
                leftBound = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            mid = (left + right)//2
        print(leftBound)
        if leftBound == None:
            return [-1, -1]
        left, rightBound = leftBound, leftBound
        right = len(nums) -1
        mid = (left + right)//2
        while left <= right:
            if nums[mid] == target:
                rightBound = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            mid = (left + right)//2
        return [leftBound, rightBound]
        