class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(start, arr, summ):
            if summ  == target:
                ans.append(arr.copy())
            if summ > target:
                return
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                backtrack(i, arr, summ+candidates[i])
                arr.pop()
        backtrack(0, [], 0)
        return ans
