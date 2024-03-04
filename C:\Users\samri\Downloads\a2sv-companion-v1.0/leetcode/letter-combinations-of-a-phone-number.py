class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc', '3':'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
        ans = []
        def backtrack(i, word):
            if not digits:
                return
            if len(word) == len(digits):
                ans.append(word)
                return
            for letter in dic[digits[i]]:
                backtrack(i+1, word+letter)
        backtrack(0, '')
        return ans