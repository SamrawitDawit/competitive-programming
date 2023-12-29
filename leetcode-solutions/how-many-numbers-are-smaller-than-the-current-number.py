class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        storageArray = [0]*(max(nums)+1)
        for num in nums:
            storageArray[num] += 1
        prefix = 0
        prefixArray = []
        for i in range(len(storageArray)):
            prefixArray.append(prefix)
            prefix += storageArray[i]
        for i in range(len(nums)):
            nums[i] = prefixArray[nums[i]]
        return(nums)