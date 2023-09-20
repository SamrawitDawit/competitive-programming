class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        accumulator = 0
        ans = 0
        for num in nums:
            accumulator += num
            if accumulator - k in dic:
                ans += dic[accumulator -k]
            dic[accumulator] += 1
        return ans
