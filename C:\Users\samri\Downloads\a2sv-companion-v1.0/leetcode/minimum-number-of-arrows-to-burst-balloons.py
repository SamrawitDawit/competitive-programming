class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        print(points)
        prev_ballon = ''
        arrows = 0
        for point in points:
            if not prev_ballon:
                arrows += 1
                prev_ballon = point
            elif point[0] > prev_ballon[1]:
                arrows += 1
                prev_ballon = point
        return arrows
