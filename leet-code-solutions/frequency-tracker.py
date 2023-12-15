from collections import Counter
class FrequencyTracker:

    def __init__(self):
       self.fTracker = Counter()
       self.freq = Counter()

    def add(self, number: int) -> None:
        frequency = self.fTracker[number]
        self.fTracker[number] = frequency+1
        self.freq[frequency+1] += 1
        self.freq[frequency] -= 1
    def deleteOne(self, number: int) -> None:
        if self.fTracker[number] > 0:
            frequency = self.fTracker[number]
            self.fTracker[number] = frequency-1
            self.freq[frequency] -= 1
            self.freq[frequency-1] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)