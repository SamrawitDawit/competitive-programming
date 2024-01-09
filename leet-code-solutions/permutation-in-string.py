class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = collections.Counter(s1)
        s2_dic = collections.Counter(s2[:len(s1)])
        l = 0
        for r in range(len(s1),len(s2)):
            if s1_dic == s2_dic:
                return True
            s2_dic[s2[l]] -= 1
            s2_dic[s2[r]] += 1
            l += 1
        if s1_dic == s2_dic:
            return True
        return False

