class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        equalNums = collections.defaultdict(list)
        output = 0
        for i, num in enumerate(nums):
            if num in equalNums:
                for indx in equalNums[num]:
                    if (indx*i)%k == 0:
                        output += 1
            equalNums[num].append(i)
        return output