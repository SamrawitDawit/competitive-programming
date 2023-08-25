class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        right = len(people)-1
        left = 0
        count = 0
        while left <= right:
            if left == right:
                count += 1
                break
            summ = people[right] + people[left]
            if summ <= limit:
                left += 1
            right-=1
            count += 1
        return count
