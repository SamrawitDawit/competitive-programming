class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_dest = 0
        for trip in trips:
            max_dest = max(max_dest, trip[2])
        prefixArray = [0]*(max_dest+1)
        for trip in trips:
            prefixArray[trip[1]] += trip[0]
            if (trip[2]) < max_dest:
                prefixArray[trip[2]] -= trip[0]
            # print(prefixArray)
        prefix = 0
        for i in range(max_dest):
            prefix += prefixArray[i]
            prefixArray[i] = prefix
            if prefixArray[i] > capacity:
                return False
        return True



        