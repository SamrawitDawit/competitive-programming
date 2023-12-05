class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst = [word for word in s.split(' ')]
        sorted_lst = sorted(lst, key = lambda x:len(x))
        output = [0]*len(sorted_lst[-1])
        for i in range(len(output)):
            vertical_string = ''
            for word in lst:
                if i >= len(word):
                    vertical_string += ' '
                elif i < len(word):
                    vertical_string += word[i]
                else:
                    break
            stripped = vertical_string.strip()
            if stripped != '':
                starting = vertical_string.index(stripped[0])
            vertical_string = vertical_string[:starting] + vertical_string[starting:].strip()
            output[i] = vertical_string
        return output
         