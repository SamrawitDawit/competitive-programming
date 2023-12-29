class Solution:
    def sortSentence(self, s: str) -> str:
        lst = [word for word in s.split(' ')]
        lst.sort(key = lambda x: x[-1])
        output = ''
        for word in lst:
            output += (word[:-1] + ' ')
        return output.strip()