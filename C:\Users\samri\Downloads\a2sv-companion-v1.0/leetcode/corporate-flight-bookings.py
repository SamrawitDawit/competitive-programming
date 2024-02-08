class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixArray = [0]*n
        for booking in bookings:
            prefixArray[booking[0]-1] += booking[2]
            if (booking[1]-1) < n-1:
                prefixArray[booking[1]] -= booking[2]
        prefix = 0
        for i in range(n):
            prefix += prefixArray[i]
            prefixArray[i] = prefix
        return prefixArray