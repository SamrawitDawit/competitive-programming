class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination > start:
            clockwise_move = sum(distance[start:destination])
            counter_clockwise_move = sum(distance[destination:])+sum(distance[:start])
        else:
            clockwise_move = sum(distance[start:len(distance)])+sum(distance[0:destination])
            counter_clockwise_move = sum(distance[destination:start])
        return min(clockwise_move, counter_clockwise_move)