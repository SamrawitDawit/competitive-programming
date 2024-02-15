class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        rabbits_store = {}
        for answer in answers:
            if answer == 0:
                rabbits += 1
            elif answer not in rabbits_store:
                rabbits += (answer + 1)
                rabbits_store[answer] = answer
            else:
                rabbits_store[answer] -= 1
                if rabbits_store[answer] == 0:
                    rabbits_store.pop(answer)
        return rabbits
