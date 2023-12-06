class Solution:
    def numberOfMatches(self, n: int) -> int:
        winners = n
        matches = 0
        while winners > 1:
            if winners % 2 == 0:
                winners = winners/2
                matches += winners
            else:
                winners = winners//2+1
                matches += (winners -1)
        return int(matches)