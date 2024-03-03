class Solution:
    def trap(self, height: List[int]) -> int:
        array = [[0,0,0]]* len(height)
        left_max, right_max = 0, 0
        rain = 0 
        for i in range(len(height)):
            array[i] = [height[i], left_max, 0]
            left_max = max(left_max, height[i])
        for j in range(len(height)-1, -1, -1):
            array[j][2] = right_max
            right_max = max(right_max, height[j])
        for h in array:
            rain += max(0, (min(h[1], h[2])-h[0]))
        return rain
            