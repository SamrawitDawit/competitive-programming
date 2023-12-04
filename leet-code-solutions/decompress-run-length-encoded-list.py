class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(1,len(nums),2):
            for freq in range(nums[i-1]):
                output.append(nums[i])
        return output