class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_lst = [0]*len(s) 
        for i in range(len(s)):
            shuffled_lst[indices[i]] = s[i]
        return ''.join(shuffled_lst)
