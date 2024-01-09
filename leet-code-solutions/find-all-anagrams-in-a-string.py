class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = collections.Counter(p)
        s_counter = collections.Counter()
        leng, ans = len(p)-1, []
        for i in range(len(s)):
            s_counter[s[i]] += 1
            if i >= leng:
                if s_counter == p_counter:
                    ans.append(i-leng)
                s_counter[s[i-leng]] -= 1
        return ans

            
            
            
            

        