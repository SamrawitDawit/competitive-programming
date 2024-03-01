class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sett = set()
        candidates.sort()
        ans = []
        def backtrack(start, arr, summ):
            if summ  == target:
                # if tuple(arr) not in sett:
                ans.append(arr.copy())
                #     sett.add(tuple(arr))
            if summ > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                backtrack(i+1, arr, summ+candidates[i])              
                arr.pop()           
        backtrack(0, [], 0)
        return ans
        [1,1, 2, 5, 6, 7,10]
