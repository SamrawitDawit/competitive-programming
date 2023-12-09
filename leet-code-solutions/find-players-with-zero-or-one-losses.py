class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners_dict = collections.defaultdict(int)
        loosers_dict = collections.defaultdict(int)
        winners, loosers = [], []
        for match in matches:
            winners_dict[match[0]] += 1
            loosers_dict[match[1]] += 1
        for winner in winners_dict.keys():
            if winner not in loosers_dict:
                winners.append(winner)
            elif loosers_dict[winner] == 1:
                loosers.append(winner)
        for looser in loosers_dict:
            if looser not in winners_dict and loosers_dict[looser] == 1:
                loosers.append(looser)
        return [sorted(winners), sorted(loosers)]
            
            