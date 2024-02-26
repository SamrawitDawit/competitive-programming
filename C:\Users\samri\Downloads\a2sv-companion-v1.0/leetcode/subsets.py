class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        subset = []
        def backtrack(indx, arr):
            if indx == len(nums):
                return 
            for i in range(indx, len(nums)):
                arr.append(nums[i])
                ans.append(arr.copy())
                backtrack(i+1, arr)
                arr.pop()

        backtrack(0, subset)
        return ans