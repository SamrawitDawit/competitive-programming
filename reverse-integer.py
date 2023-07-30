class Solution:
    def reverse(self, x: int) -> int:
            r = ''
            for i in reversed(str(abs(x))):
                r += i
            if int(r) not in range(-2**31 , 2**31-1):
                return 0
            if x > 0:
                return int(r)
            return - int(r)
