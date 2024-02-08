class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        accumulator = 0
        ans = 0
        for num in nums:
            accumulator += num
            remainder = accumulator % k
            if remainder in dic:
                ans += dic[remainder]
            dic[remainder] += 1
        return ans