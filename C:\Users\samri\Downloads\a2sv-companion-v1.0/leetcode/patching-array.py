class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        patch, prefix, target = 0, 0, 1
        while target <= n:
            if i < len(nums):
                if nums[i] > target:
                    patch += 1
                    prefix += target
                else:
                    prefix += nums[i]
                    i += 1
                print(prefix)
                target = prefix + 1
            else:
                patch += 1
                prefix += target 
                target = prefix + 1
        return patch
        # num = 1
        # patches = 0
        # i = 0
        # prefix = 0
        # desired = 1
        # while prefix < n:
        #     if prefix == desired:
        #         prefix += nums[i]
        #         i += 1
        #         desired = prefix +1
        #     # num = num + 1                                                                                                     
            
        #     # if num+1 == prefix:
        #     #     num 
        #     # prefix += (num + 1)