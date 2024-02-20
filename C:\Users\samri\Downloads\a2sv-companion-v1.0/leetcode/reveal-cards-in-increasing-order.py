class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        output = [0]*len(deck)
        skip = 2
        pos = 0
        if len(deck) == 1:
            return deck
        for i in range(len(deck)-1):
            output[pos] = deck[i]
            zeros = 0
            while zeros != 2:
                pos += 1
                pos = pos%len(deck)
                if output[pos] == 0:
                    zeros += 1
        output[output.index(0)] = deck[i+1]
        return output
            