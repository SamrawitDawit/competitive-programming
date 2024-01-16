class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts = sum(cardPoints)
        maximum = 0
        n = len(cardPoints)
        d = n -k
        l = 0
        summ = sum(cardPoints[l:l+d])
        while l <= (n-d):
            maximum = max(maximum, total_pts - summ)
            if l+d in range(n):
                summ -= cardPoints[l]
                summ += cardPoints[l+d]
            l += 1
        return maximum
