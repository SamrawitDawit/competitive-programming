class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        answer = 0
        while tickets[k] != 0:
            if tickets[i] == 0:
                if i == len(tickets) -1:
                    i = 0
                else:
                    i += 1
                continue
            tickets[i] -= 1
            answer += 1
            if i == len(tickets) - 1:
                i = 0
            else:
                i += 1
        return answer