
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        currZeros = 0
        currOnes = nums.count(1)
        maximum = currOnes
        output = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                currZeros += 1
            else:
                currOnes -= 1
            if currOnes + currZeros > maximum:
                maximum = currOnes + currZeros
                output = [i+1]
            elif currOnes + currZeros == maximum:
                output.append(i+1)
        return output