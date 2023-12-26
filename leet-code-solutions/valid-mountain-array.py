class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] <= arr[0]:
            return False
        for i in range(2,len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if arr[i] < arr[i-1]:
                for j in range(i, len(arr)-1):
                    if arr[j] <= arr[j+1]:
                        return False
                return True
        return False