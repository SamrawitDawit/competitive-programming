class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives =[]
        negatives = []
        answer = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else: negatives.append(num)
        for i in range(len(positives)):
            answer.append(positives[i])
            answer.append(negatives[i])
        return answer