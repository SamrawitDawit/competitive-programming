class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        stack = [letter for letter in senate]
        count_D, count_R = 0, 0
        while 'D' in stack and 'R' in stack:
            i = 0
            while i in range(len(stack)):
                if stack[i] == 'D':
                    if count_R > 0:
                        count_R -= 1
                        stack.pop(i)
                    else:
                        count_D += 1
                        i += 1
                else:
                    if count_D > 0:
                        count_D -= 1
                        stack.pop(i)
                    else:
                        count_R += 1
                        i += 1
        if 'D' in stack:
            return 'Dire'
        else:
            return 'Radiant'


