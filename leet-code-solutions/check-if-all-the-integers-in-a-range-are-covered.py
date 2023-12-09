class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            for rng in ranges:
                if num >= rng[0] and num <=rng[1]:
                    break
            else:
                return False
        return True