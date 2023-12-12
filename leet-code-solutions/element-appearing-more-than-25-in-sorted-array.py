class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        for num, freq in counter.items():
            if freq > (len(arr)*0.25):
                return num
        