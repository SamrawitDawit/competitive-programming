class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1=0
        pointer2=len(height)-1
        max_area =0
        while pointer1<pointer2:
            width=pointer2-pointer1
            length=min(height[pointer2],height[pointer1])
            max_area = max((width*length),max_area)         
            if height[pointer1]>height[pointer2]:  
                pointer2-=1 
            else:
                pointer1+=1
        return max_area