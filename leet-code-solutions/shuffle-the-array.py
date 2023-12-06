class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(len(nums)//2):
            answer.append(nums[i])
            answer.append(nums[i+n])
        return answer