class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f,s,ans= 0,0,[]
        while f<len(firstList) and s<len(secondList):
            if firstList[f][0] > secondList[s][1]:
                s += 1
            elif secondList[s][0] > firstList[f][1]:
                f += 1
            else:
                x = max(firstList[f][0], secondList[s][0])
                y = min(firstList[f][1], secondList[s][1])
                ans.append([x,y])
                if firstList[f][1] > secondList[s][1]:
                    s += 1
                elif secondList[s][1] > firstList[f][1]:
                    f += 1
                else:
                    f += 1
                    s += 1
        return ans