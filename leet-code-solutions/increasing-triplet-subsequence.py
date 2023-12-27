class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:      
        minimum = nums[0]
        maximum = nums[-1]
        minimumArray = [0]*len(nums)
        maximumArray = [0]*len(nums)
        for i in range(len(nums)):
            minimum = min(minimum, nums[i])
            minimumArray[i] = minimum
            maximum = max(maximum, nums[len(nums)-1-i])
            maximumArray[len(nums)-1-i] = maximum
        for i in range(1, len(nums)-1):
            if minimumArray[i-1] < nums[i] and nums[i] < maximumArray[i+1]:
                return True
        return False

            
