class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, count_0, max_len= 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_0 += 1
            while count_0 > k:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1
            if count_0 == k or r == len(nums)-1:
                max_len = max(max_len, r-l+1)
        return max_len
