class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for p in s:
            if p in dic.keys():
                stack.append(p)
            elif not stack or dic.get(stack.pop()) != p:
                return False
        if stack: return False
        return True
