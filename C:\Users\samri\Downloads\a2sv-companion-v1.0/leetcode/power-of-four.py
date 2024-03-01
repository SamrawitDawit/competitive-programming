class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n > 0 and n%4 == 0:
            if n == 4:
                return True
            return self.isPowerOfFour(n//4)
        return False
