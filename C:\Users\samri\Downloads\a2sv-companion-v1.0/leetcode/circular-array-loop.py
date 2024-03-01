class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                k = 1
            else:
                k = -1
            while i < len(nums):
                if nums[i]*k < 0:
                    dic = {}
                    break                
                if (i+nums[i])%len(nums) == i:
                    dic = {}
                    break
                if (i+nums[i])%len(nums) in dic:
                    return True
                dic[i] = 1            
                i = (i + nums[i])%len(nums)
                
        return False
                