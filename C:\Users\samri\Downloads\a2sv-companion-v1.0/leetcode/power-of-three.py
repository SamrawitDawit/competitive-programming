class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 0 and n%3 == 0:
            if n == 3: 
                return True
            return Solution.isPowerOfThree(self,n/3)
        return False
        
    

        

        