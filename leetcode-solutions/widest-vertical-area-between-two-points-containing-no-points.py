class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxArea = 0
        for i in range(1,len(points)):
            maxArea = max(maxArea, (points[i][0]-points[i-1][0]))
        return maxArea