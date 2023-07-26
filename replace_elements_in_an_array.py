class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        for j in operations:
            if my_dict.get(j[0]) != None:
                nums[my_dict[j[0]]] = j[1]
                my_dict[j[1]] = my_dict[j[0]]
                del my_dict[j[0]]
        return nums
