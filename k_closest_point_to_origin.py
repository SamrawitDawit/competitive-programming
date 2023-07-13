class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        new_list = []
        for i in points:
            distance.append((i[0]*i[0]) + (i[1]*i[1]))
        for j in range(k):
            m = distance.index(min(distance))
            new_list.append(points[m])
            distance[m] = 1000000000
        return new_list
