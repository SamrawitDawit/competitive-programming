class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_of_nums = 0
        res = []
        for num in nums:
            if num%2 == 0:
                sum_of_nums += num
        for i in range(len(nums)):
            indx = queries[i][1]
            value = queries[i][0]
            if nums[indx] % 2 == 0 and (nums[indx] + value) % 2 == 0:
                sum_of_nums -= nums[indx]
                nums[indx] += value
                sum_of_nums += nums[indx]
            elif nums[indx] % 2 != 0 and (nums[indx] + value) % 2 == 0:
                nums[indx] += value
                sum_of_nums += nums[indx]
            elif nums[indx] % 2 == 0 and (nums[indx] + value) % 2 != 0:     
                sum_of_nums -= nums[indx]
                nums[indx] += value
            else:
                nums[indx] += value
            res.append(sum_of_nums)
        return res
