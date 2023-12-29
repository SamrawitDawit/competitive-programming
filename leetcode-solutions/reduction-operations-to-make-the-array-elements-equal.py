class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operations = 0
        nums.sort(reverse = True)
        distinctNums = sorted(list(set(nums)), reverse = True)
        print(distinctNums)
        j = 0
        n = len(distinctNums)
        for i in range(len(nums)):
            if nums[i] != distinctNums[j]:
                j += 1
            operations += (n-j-1)
        return operations