class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, arr, summ):
            if summ > n:
                return
            if len(arr) == k:
                if summ == n:
                    ans.append(arr.copy())
                return
            for i in range(start, 10):
                arr.append(i)
                backtrack(i+1, arr, summ+i)
                arr.pop()
        ans = []
        backtrack(1, [], 0)
        return ans