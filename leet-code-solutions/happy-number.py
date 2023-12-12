class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        n = str(n)
        while i < 7:
            summ = 0
            for letter in n:
                summ += (int(letter)**2)
                n = str(summ)
            if summ == 1:
                return True
            i += 1
        return False
  