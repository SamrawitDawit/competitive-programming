class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        my_coin = 0
        k = -2
        for i in range(len(piles)//3):
            my_coin += piles[k]
            k-=2
        return my_coin
