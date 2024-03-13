# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        mid = (left+right)//2
        while left < right:
            result = isBadVersion(mid)
            if result:
                right = mid
            else:
                left = mid + 1
            mid = (left+right)//2
        return mid