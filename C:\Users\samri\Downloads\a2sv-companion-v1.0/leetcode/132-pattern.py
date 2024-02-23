class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minimum = float('inf')
        stack.append((nums[0], minimum))
        for i in range(1, len(nums)):
            #find the previous greater number of the current number
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            # if the minimum number we can find before the previous greater element of the 
            #current element is less than the current number, we've got 132 pattern
            if stack and stack[-1][1] < nums[i]:
                return True
            #store the minimum value before the current element
            minimum = min(minimum, nums[i-1])
            stack.append((nums[i], minimum))
        return False


