class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        self.min_unfairness = float('inf')
        def backtrack(i, bucket):
            if i >= len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(bucket))
                return 
            if self.min_unfairness <= max(bucket):
                return 
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i+1, bucket)
                bucket[j] -= cookies[i]
        backtrack(0, bucket)
        return self.min_unfairness