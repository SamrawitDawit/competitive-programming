class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        left = 1
        while nums[left] != "_":
            if nums[left] == nums[left-1]:
                nums.pop(left)
                nums.append("_")
                left -= 1
            elif left == len(nums)-1:
                return len(nums)
            left += 1
        return left
