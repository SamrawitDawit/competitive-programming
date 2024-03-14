class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        min_sum, max_sum = max(nums), sum(nums)
        l, r = min_sum , max_sum
        while l <= r:
            mid = (l+r)//2
            summ, curr = 0, 1
            for num in nums:
                summ += num
                if summ > mid:
                    curr += 1
                    summ = num
            if curr > k:
                l = mid + 1
            else:
                r = mid - 1
        return(l)
