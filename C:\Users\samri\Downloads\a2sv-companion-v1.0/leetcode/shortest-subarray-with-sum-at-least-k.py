class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]*(len(nums)+1)
        queue = collections.deque()
        n = len(nums)
        min_len = n + 1
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        for i in range(n+1):
            while queue and prefix_sum[i] < prefix_sum[queue[-1]]:
                queue.pop()
            while queue and prefix_sum[i]- prefix_sum[queue[0]] >= k:
                min_len = min(min_len, (i-queue[0]))
                queue.popleft()
            queue.append(i)
        if min_len == n+1:
            return -1
        return min_len

        