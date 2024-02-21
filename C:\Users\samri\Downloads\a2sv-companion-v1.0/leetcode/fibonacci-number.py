class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n == 0 or n == 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]