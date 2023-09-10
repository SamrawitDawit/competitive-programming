class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dic = collections.Counter(p)
        s_dic = collections.Counter(s[:len(p)])
        l = 0
        r = len(p)-1
        answer = []
        if s_dic == p_dic:
            answer.append(0)
        s_dic[s[l]] -= 1
        l += 1
        r += 1
        while r < len(s):
            s_dic[s[r]] += 1
            if s_dic == p_dic:
                answer.append(l)
            s_dic[s[l]] -= 1
            l += 1
            r += 1
        return answer
