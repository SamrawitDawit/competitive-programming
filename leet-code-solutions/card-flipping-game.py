class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        possible_ans = {}
        impossible_ans = {}
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                impossible_ans[fronts[i]] = 1
                if fronts[i] in possible_ans:
                    possible_ans.pop(fronts[i])        
            else:
                if fronts[i] not in impossible_ans:
                    possible_ans[fronts[i]] = 1
                if backs[i] not in impossible_ans:
                    possible_ans[backs[i]] = 1
        if possible_ans:
            return sorted(possible_ans)[0]
        return 0



            
