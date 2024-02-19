class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        output = []
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack[-1]] = num
                stack.pop()
            stack.append(num)
        for num in nums1:
            output.append(dic.get(num, -1))
        return output
        
            



