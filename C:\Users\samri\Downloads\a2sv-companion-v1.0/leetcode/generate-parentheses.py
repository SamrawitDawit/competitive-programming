class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dic = {'(': 0, ')':0}
        ans = []
        options = ['(', ')']
        def backtrack(string):
            if dic['(']> n or (dic[')'] > dic['(']) :
                return
            if len(string) == 2*n:
                copy = string[:]
                ans.append(''.join(copy))
                return       
            for i in range(2):
                string.append(options[i])
                dic[options[i]] += 1
                backtrack(string)
                string.pop()
                dic[options[i]] -= 1
        backtrack([])
        return ans