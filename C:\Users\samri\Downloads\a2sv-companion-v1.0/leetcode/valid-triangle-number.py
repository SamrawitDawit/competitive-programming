
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for i in range(len(nums)-1, 1, -1):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += (right-left)
                    right -= 1
                else:
                    left += 1
        return ans

        #     mini, maxi = j+1, len(nums)-1
        #     while mini in range(j+1, len(nums)) and maxi in range(j+1, len(nums)):   
        #         summ = nums[i] + nums[j]
        #         if nums[mini] >= summ:
        #             if mini == j+1:
        #                 j = j + 1
        #                 mini, maxi = j+1, len(nums)-1
        #             else:
        #                 maxi = mini -1
        #                 if mini == maxi:
        #                     j = j + 1
        #                     mini, maxi = j+1, len(nums)-1
        #                 else:
        #                     mini = (mini+(j+1))//2
        #         elif nums[maxi] < summ:
        #             ans += (maxi-j)
        #             if maxi == len(nums)-1:
        #                 j = j + 1
        #                 mini, maxi = j+1, len(nums)-1
        #             else:
        #                 mini = maxi+1
        #                 maxi = (len(nums)+maxi)//2
        #         elif nums[mini] < summ:
        #             ans += 1
        #             maxi =(mini+maxi)//2
        #             if mini == maxi:
        #                 j = j + 1
        #                 mini, maxi = j+1, len(nums)-1
        # return ans