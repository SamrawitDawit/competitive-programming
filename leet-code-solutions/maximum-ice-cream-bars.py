class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        icecreams = 0 
        for i in range(len(costs)):
            if coins < costs[i]:
                break
            coins -= costs[i]
            icecreams += 1
        return icecreams
