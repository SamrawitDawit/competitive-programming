class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices_of_1s = [indx for indx,box in enumerate(boxes) if box == '1']
        print(indices_of_1s)
        output = []
        for i in range(len(boxes)):
            operation = 0
            for indx in indices_of_1s:
                operation += abs(indx-i)
            output.append(operation)
        return output
