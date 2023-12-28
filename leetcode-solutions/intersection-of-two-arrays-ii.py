class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1)<len(nums2):
            small = nums1
            large = nums2
        else:
            small = nums2
            large = nums1
        for num in small:
            if num in large:
                ans.append(num)
                large.remove(num)
        return ans
        