class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_difference = float(inf)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums)-1
            while l < r:
                summ = nums[l] + nums[r] + nums[i]
                difference = abs(target - summ) 
                if difference < min_difference:
                    min_difference = difference
                    output = summ
                if summ == target:
                    return output
                elif summ < target:
                    l += 1
                else:
                    r -= 1
        return output
            