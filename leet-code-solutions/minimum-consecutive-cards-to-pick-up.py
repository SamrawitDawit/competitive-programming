class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lastIndx = {}
        distance = {}
        for i in range(len(cards)):
            if cards[i] in distance:
                distance[cards[i]] = min(distance[cards[i]], (i-lastIndx[cards[i]]+1))
            else:
                distance[cards[i]] = float("inf")
            lastIndx[cards[i]] = i
        minimum = min(distance.values())
        if minimum == float("inf"):
            return -1
        return minimum