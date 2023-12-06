class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        middle = [pivot]
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num > pivot:
                after.append(num)
            else:
                middle.append(num)
        return before + middle[1:] + after