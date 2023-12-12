from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.ug_system = {}
        self.trips = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ug_system[id] = [id,stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starting = self.ug_system[id][1]
        ending = stationName
        starting_time = self.ug_system[id][2]
        ending_time = t
        self.trips[(starting,ending)].append(ending_time-starting_time)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time = 0
        number_of_trips = len(self.trips[(startStation, endStation)])
        for time in self.trips[(startStation, endStation)]:
            total_time += time
        average = total_time/number_of_trips
        return average
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)