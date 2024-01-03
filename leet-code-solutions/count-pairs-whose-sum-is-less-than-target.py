class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        l, r, count = 0, len(nums)-1, 0
        while l<r:
            summ = sorted_nums[l] + sorted_nums[r]
            if summ < target:
                count += (r-l)
                l += 1
            else:
                r -= 1
        return count

