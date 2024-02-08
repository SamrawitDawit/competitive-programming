class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(num) for num in s]
        curr = sum(nums)
        if nums[0] == 0:
            ans = curr + 1
        else:
            ans = curr-1
        for num in nums[:-1]:
            if num == 0:
                curr += 1
                ans = max(curr, ans)
            else:
                curr -= 1
        return ans
