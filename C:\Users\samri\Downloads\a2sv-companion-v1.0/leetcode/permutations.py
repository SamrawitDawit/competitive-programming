class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(arr):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    backtrack(arr)
                    arr.pop() 
        backtrack([])
        return ans