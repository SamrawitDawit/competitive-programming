class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        l = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                count += 1
                ans = 0
            while count == k:
                ans += 1
                if nums[l] %2 != 0:
                    count -= 1
                l += 1
            res += ans
        return res
