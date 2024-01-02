class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = []
        upperBound = n
        while upperBound > 0:
            maxIndx = arr.index(max(arr[:upperBound]))
            output.append(maxIndx+1)
            arr = arr[:maxIndx+1][::-1] + arr[maxIndx+1:]
            arr = arr[:upperBound][::-1] + arr[upperBound:]
            output.append(upperBound)
            upperBound -= 1
        return output
