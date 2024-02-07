class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_shifts = [0]*len(s)
        output = ''
        for shift in shifts:
            if shift[2] == 0:
                prefix_shifts[shift[0]] -= 1
                if shift[1] < len(s)-1:
                    prefix_shifts[shift[1]+1] += 1
            else:
                prefix_shifts[shift[0]] += 1
                if shift[1] < len(s)-1:
                    prefix_shifts[shift[1]+1] -= 1
        prefix = 0
        for i in range(len(prefix_shifts)):
            prefix += prefix_shifts[i]
            prefix_shifts[i] = prefix
        for indx in range(len(s)):
            conv_dic = {}
            i = 0
            for j in range(97, 123):
                conv_dic[i] = chr(j)
                i += 1
            conv_value = ((ord(s[indx])-97) + prefix_shifts[indx])%26  
            output += conv_dic[conv_value]
        return output
        
       
