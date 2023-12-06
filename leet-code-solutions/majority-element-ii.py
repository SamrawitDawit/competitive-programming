class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = collections.Counter(nums)
        answer = set()
        for num in nums:
            if counter[num] > (n/3):
                answer.add(num)
        return answer
