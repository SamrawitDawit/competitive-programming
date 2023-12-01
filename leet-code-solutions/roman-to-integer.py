class Solution:
    def romanToInt(self, s: str) -> int:
        roman = 0
        for i in range(len(s)):
            if s[i] == 'M':
                roman += 1000
            elif s[i] == 'D':
                roman += 500
            elif s[i] == 'C':
                if i < len(s)-1 and s[i+1] in ['D', 'M']:
                    roman -= 100
                else:
                    roman += 100
            elif s[i] == 'L':
                roman += 50
            elif s[i] == 'X':
                if i < len(s)-1 and s[i+1] in ['L', 'C']:
                    roman -= 10
                else:
                    roman += 10
            elif s[i] == 'V':
                roman += 5
            elif s[i] == 'I':
                if i < len(s)-1 and s[i+1] in ['X', 'V']:
                    roman -= 1
                else:
                    roman += 1
        return roman
            