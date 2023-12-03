class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary = ''
        while n != 0:
            r = n%3
            n = n//3
            ternary += str(r)
        if '2' in ternary:
            return False
        return True

