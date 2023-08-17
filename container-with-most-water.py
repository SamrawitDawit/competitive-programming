class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        temp_max = 0
        while left < right:
            area = min(height[left], height[right])*(right-left)
            temp_max = max(temp_max, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return temp_max
