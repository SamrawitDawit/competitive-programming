class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        mine, n = 0, len(piles)
        if n == 3:
            return piles[1]
        i, bobsStarting = 1, 2*(n/3)
        while i < bobsStarting:
            mine += piles[i]
            i += 2
        return mine
        