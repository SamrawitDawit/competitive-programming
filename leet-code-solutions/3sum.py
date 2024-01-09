class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                summ = nums[l]+nums[r]
                if summ == -nums[i]:
                    answer.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif summ > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return answer
