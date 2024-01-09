class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_1s=post_1s=max_len= 0
        for i in range(len(nums)):
            if nums[i] == 1:
                post_1s += 1
                if i == len(nums)-1:
                    max_len = max(max_len, prev_1s + post_1s)
            else:
                max_len = max(max_len, prev_1s + post_1s)
                prev_1s = post_1s
                post_1s = 0
        if max_len == len(nums):
            return max_len -1
        return max_len
        