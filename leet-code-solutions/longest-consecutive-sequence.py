class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 0:
            return 0
        i = 0
        longest = 1
        for k in nums:
            if k-1 not in nums:
                j = 1
                while k + j in nums:
                    j += 1
                    longest = max(longest, j)
        return longest
                