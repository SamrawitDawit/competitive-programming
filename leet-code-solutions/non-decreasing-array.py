class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                case1 = case2 = True
                if i == len(nums)-1:
                    new_nums = nums[:i]
                else:
                    new_nums = nums[:i]+nums[i+1:]
                for j in range(1, len(new_nums)):
                    if new_nums[j] < new_nums[j-1]:
                        case1 = False
                if i == 0:
                    new_nums = nums[i:]
                else:
                    new_nums = nums[:i-1]+nums[i:]
                
                for k in range(1, len(new_nums)):
                    if new_nums[k] < new_nums[k-1]:
                        case2 = False
                if case1 == False and case2 == False:
                    return False
        return True

