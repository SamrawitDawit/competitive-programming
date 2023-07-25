class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        while arr != sorted(arr):
            k = arr.index(len(arr)) + 1
            arr = list(reversed(arr[:k]))+arr[k:]
            flips.append(k)
            arr = list(reversed(arr))
            flips.append(len(arr))
            arr.pop()
        return flips
