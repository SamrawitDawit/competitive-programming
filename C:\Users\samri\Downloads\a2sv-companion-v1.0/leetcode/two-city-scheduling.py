class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key = lambda x: x[0]-x[1])
        return (sum(pair[0] for pair in costs[:n//2]) + sum(pair[1] for pair in costs[n//2:]))
        
