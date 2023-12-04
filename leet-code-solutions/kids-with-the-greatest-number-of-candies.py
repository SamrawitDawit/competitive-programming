class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        output = []
        for candy in candies:
            if (candy + extraCandies) < maximum:
                output.append(False)
            else:
                output.append(True)
        return output