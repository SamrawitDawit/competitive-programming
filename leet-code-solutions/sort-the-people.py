class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):           
            j = i-1
            while j>=0 and heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                names[i], names[j] = names[j], names[i]
                j -= 1
                i -= 1
        print(heights)
        return names
                