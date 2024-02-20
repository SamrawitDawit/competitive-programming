class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            output =  [1]*(rowIndex+1)
            aboveRow = self.getRow(rowIndex-1)
            for i in range(1, len(output)-1):
                output[i] = aboveRow[i-1] + aboveRow[i]
                print(output)
            return output