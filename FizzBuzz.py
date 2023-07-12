class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
       Array = [] 
       for i in range(1,n+1):
           if i%3 == 0 and i%5 == 0:
               p = ("FizzBuzz")
           elif i%3 == 0:
               p = ("Fizz")
           elif i%5 == 0:
               p = ("Buzz")
           else:
               p = str(i)
           Array.append(p)
       return Array
        
