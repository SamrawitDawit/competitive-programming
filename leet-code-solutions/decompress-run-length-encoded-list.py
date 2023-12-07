class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = [nums[1]]*nums[0]
        for i in range(2, len(nums)-1, 2):
            answer += [nums[i+1]]*nums[i]
        return answer