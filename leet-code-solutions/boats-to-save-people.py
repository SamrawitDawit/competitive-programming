class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r = len(people)-1
        l = 0
        boat = 0
        while l <= r:
            summ = people[r] + people[l]
            if summ <= limit:
                l += 1
            r-=1
            boat += 1
        return boat
            

                
        
            



        