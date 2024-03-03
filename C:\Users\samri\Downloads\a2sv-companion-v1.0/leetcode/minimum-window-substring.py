class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        min_str = ""
        isSubstring = False
        t_counter = collections.Counter(t)
        s_counter = collections.defaultdict(int)
        l, r = 0, 0
        for r in range(len(s)):
            if s[r] in t_counter:
                s_counter[s[r]] += 1        
            for letter in t_counter:
                if t_counter[letter] > s_counter[letter]:     
                    break
            else:
                isSubstring = True
                while isSubstring:
                    if s_counter[s[l]] > 0:
                        s_counter[s[l]] -= 1
                    l += 1
                    for letter in t_counter:
                        if t_counter[letter] > s_counter[letter]:
                            isSubstring = False
                            break
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_str = s[l-1:r+1]  
        return min_str                  