class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic, i = {}, 1
        for letter in order:
            dic[letter] = i
            i += 1
        for indx in range(1, len(words)):
            for i in range(min(len(words[indx]),len(words[indx-1]))):
                if dic[words[indx][i]] < dic[words[indx-1][i]]:
                    return False
                elif dic[words[indx][i]] > dic[words[indx-1][i]]:
                    break
            else:
                if len(words[indx]) < len(words[indx-1]):
                    return False
        return True
        
        
