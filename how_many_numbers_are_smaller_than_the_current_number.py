class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        my_list = []
        for i in nums:
            my_list.append(sorted_nums.index(i))
        return my_list
