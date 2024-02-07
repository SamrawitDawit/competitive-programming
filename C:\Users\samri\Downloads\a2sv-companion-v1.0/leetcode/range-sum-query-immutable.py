class NumArray:

    def __init__(self, nums: List[int]):
        prefix = 0
        self.prefixArray = []
        for num in nums:
            prefix += num
            self.prefixArray.append(prefix)
        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefixArray[right] - self.prefixArray[left-1]
        return self.prefixArray[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)