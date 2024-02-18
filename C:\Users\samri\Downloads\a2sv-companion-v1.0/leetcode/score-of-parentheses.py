class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = list(s)
        multiplier = 1
        count = 0
        while stack:
            popped = stack.pop()
            if popped == ')' and  stack[-1] == ')':
                multiplier *= 2
            elif popped == ')' and stack[-1] == '(':
                count += multiplier
                stack.pop()
            elif popped == '(':
                multiplier = multiplier // 2
        return count