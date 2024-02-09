class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        output = []
        prefixArray = []
        accumulator = 0
        n = len(nums) -1
        for num in nums:
            accumulator += num
            num = accumulator
            prefixArray.append(num)   
        for i in range(n+1):
            prefix = 0 if i == 0 else (nums[i]*i)-prefixArray[i-1]
            suffix = 0 if i == n else (prefixArray[-1]-prefixArray[i])-((n-i)*nums[i])
            output.append(prefix+suffix)
        return output
            