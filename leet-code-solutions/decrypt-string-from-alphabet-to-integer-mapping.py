class Solution:
    def freqAlphabets(self, s: str) -> str:
        output = ''
        for i in range(len(s)):
            if s[i] == '#':
                temp = chr(96+int(s[i-2:i]))
                output = output[:-2]
                output += temp
            else:
                output += chr(int(s[i])+96)
        return output
