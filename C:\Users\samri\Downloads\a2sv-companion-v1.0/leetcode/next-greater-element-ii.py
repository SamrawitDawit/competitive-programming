class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        #stack to store decreasing nums
        stack = []
        # dictionary to store the incdices with thier corresponding index where next greater element 
        # the elements are found
        dic = {}
        for i in range(len(nums)):
            while stack and stack[-1][1] < nums[i]:
                dic[stack[-1][0]%n] = nums[i]
                stack.pop()
            stack.append([i, nums[i]])
        output= [-1]*n
        for key in dic:
            output[key] = dic[key]
        return output
