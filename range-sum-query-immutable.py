    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sum[left]
        right_sum = self.prefix_sum[right+1]
        return right_sum - left_sum
