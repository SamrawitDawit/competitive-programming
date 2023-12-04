class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curr_capacity = capacity
        for i in range(len(plants)):
            if curr_capacity >= plants[i]:
                steps += 1
            else:
                steps += (2*i+1)
                curr_capacity = capacity
            curr_capacity -=plants[i]
        return steps
