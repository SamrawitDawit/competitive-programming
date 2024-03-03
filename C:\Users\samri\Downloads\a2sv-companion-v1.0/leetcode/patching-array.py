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
                target = prefix + 1
            else:
                patch += 1
                prefix += target 
                target = prefix + 1
        return patch
        