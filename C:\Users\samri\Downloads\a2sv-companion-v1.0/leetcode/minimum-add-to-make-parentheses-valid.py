class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        closing = 0
        for parenthesis in s:
            if parenthesis == '(':
                opening += 1
            elif opening > 0:
                opening -= 1
            else:
                closing += 1
        return opening + closing