class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tracker = 0
        for i in range(len(arr2)):
            for indx in range(len(arr1)):
                if arr1[indx] == arr2[i]:
                    arr1[indx], arr1[tracker] = arr1[tracker], arr1[indx]
                    tracker += 1
                    print(arr1)
        arr1 = arr1[:tracker] + sorted(arr1[tracker:])
        return arr1